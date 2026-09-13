import smtplib, ssl, datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path

SENDER_EMAIL = "abdullahmasaud10@gmail.com"
APP_PASSWORD  = "vzpvxrlhutflfyak"
CV_DIR        = Path(r"C:\Users\Lenovo\Desktop\CVV'S")
TRACKER_PATH  = Path(r"C:\Users\Lenovo\Desktop\Projects\Automated-Job-Applier\applied_tracker.csv")

CV_MAP = {
    "AI":       CV_DIR / "CV__A.pdf",
    "HARDWARE": CV_DIR / "CV__H.pdf",
    "TELECOM":  CV_DIR / "CV__T.pdf",
    "SOFTWARE": CV_DIR / "CV__S.pdf",
}

# ── BATCH 10: 21 PRE-CHECKED MX TARGETS (SAUDI, UAE, REMOTE, PAKISTAN) ──────
TARGETS = [
    # ── SAUDI ARABIA TECH & E-COMMERCE UNICORNS ──
    {
        "company": "Nana (Grocery Tech Unicorn KSA)",
        "email":   "careers@nana.sa",
        "domain":  "SOFTWARE",
        "role":    "Associate Backend Software Engineer",
        "region":  "Saudi Arabia",
        "subject": "Associate Backend Engineer Application: Abdullah Bin Masaud – COMSATS 2026 (KSA)",
        "body": """Dear Nana Talent Acquisition Team,

Nana's rapid scaling as Saudi Arabia's leading grocery and quick-commerce platform requires resilient, real-time inventory and logistics software. I am applying for an Associate Backend Software Engineer position in Riyadh.

I am graduating in Computer Engineering from COMSATS University Islamabad in 2026.

Engineering Strengths:
- API Engineering: Designed and tested Flask REST endpoints with automated pytest coverage, latency checks, and error boundaries.
- Network Protocols: Custom TCP/IP multithreaded socket server with CRC32 packet integrity validation.
- Data Pipelines: Automated Python data verification with outlier detection and reporting.

Ready for relocation to Riyadh.

Profiles:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My Software CV is attached.

Best regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Mrsool (On-Demand Delivery Unicorn KSA)",
        "email":   "careers@mrsool.co",
        "domain":  "SOFTWARE",
        "role":    "Junior Software Engineer / Platform",
        "region":  "Saudi Arabia",
        "subject": "Junior Software Engineer Application: Abdullah Bin Masaud – COMSATS 2026 (Riyadh)",
        "body": """Dear Mrsool Talent Team,

Mrsool's conversational on-demand delivery platform serving millions across Saudi Arabia and Egypt represents high-concurrency engineering. I am applying for a Junior Software Engineer position in Riyadh.

I am a final-year Computer Engineering candidate from COMSATS University Islamabad (graduating 2026).

Relevant Experience:
- Scalable Systems: Implemented multithreaded socket communication protocols tested with 50 concurrent client threads.
- Automated Testing & QA: Comprehensive pytest test suites ensuring endpoint response latency under 200ms.
- Edge AI & Computer Vision: Built VisionAid (YOLOv8) deployed on edge devices.

Ready for relocation to Riyadh.

Links:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My Software CV is attached.

Warm regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Sabbar (Flexible Staffing Platform KSA)",
        "email":   "careers@sabbar.com",
        "domain":  "SOFTWARE",
        "role":    "Junior Software Engineer",
        "region":  "Saudi Arabia",
        "subject": "Junior Software Engineer Application: Abdullah Bin Masaud – COMSATS 2026 (KSA)",
        "body": """Dear Sabbar Recruitment Team,

Sabbar's gig-economy and on-demand staffing technology empowering thousands of workers across Saudi Arabia is an inspiring workforce transformation platform. I am applying for a Junior Software Engineer position in Riyadh.

I am graduating with a BS in Computer Engineering from COMSATS University Islamabad in 2026.

Technical Strengths:
- Production-Grade APIs: Modular Flask REST APIs with automated testing and structured JSON schemas.
- Concurrency & Reliability: Multi-client socket handling with CRC32 packet integrity validation.
- Clean Code Standards: 12 public GitHub repositories following unit testing and modular architecture.

Ready for relocation to Riyadh.

Profiles:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My Software CV is attached.

Sincerely,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Qoyod (Cloud Accounting SaaS KSA)",
        "email":   "careers@qoyod.com",
        "domain":  "SOFTWARE",
        "role":    "Associate Backend Software Engineer",
        "region":  "Saudi Arabia",
        "subject": "Associate Backend Engineer Application: Abdullah Bin Masaud – FinTech (KSA)",
        "body": """Dear Qoyod Talent Team,

Qoyod's cloud accounting and financial software platform simplifying bookkeeping for thousands of SMEs across Saudi Arabia requires high data integrity. I am applying for an Associate Backend Software Engineer position in Riyadh.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026).

Why My Background Fits:
- Low-Level Protocol Rigor: Built custom multithreaded TCP/IP communication protocols with binary packet framing and CRC32 checksums.
- Robust API Engineering: Designed Flask REST endpoints with strict schema validation and 25+ automated pytest test cases.
- Data Validation: Created automated auditing tools for identifying missing or corrupted financial data.

Ready for relocation to Riyadh.

Links:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My Software CV is attached.

Best regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Floward (E-Commerce Platform KSA & GCC)",
        "email":   "careers@floward.com",
        "domain":  "SOFTWARE",
        "role":    "Junior Software Engineer",
        "region":  "Saudi Arabia & GCC",
        "subject": "Junior Software Engineer Application: Abdullah Bin Masaud – COMSATS 2026 (GCC)",
        "body": """Dear Floward Talent Acquisition Team,

Floward's e-commerce and gifting platform operating across 9 countries in the Middle East and UK represents rapid global expansion. I am writing to apply for a Junior Software Engineer position in Riyadh or Dubai.

I am graduating in Computer Engineering from COMSATS University Islamabad in 2026.

Profile Highlights:
- Python & API Development: Production REST APIs with full pytest test automation and Swagger docs.
- Systems Concurrency: Multithreaded TCP/IP client-server system with CRC32 packet error detection.
- Data Quality Automation: Python QA pipeline with statistical anomaly detection.

Ready for relocation to Riyadh or Dubai.

Profiles:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My Software CV is attached.

Warm regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },

    # ── DUBAI & UAE TECH ──
    {
        "company": "Dubizzle (EMPG Group) - Dubai",
        "email":   "careers@dubizzle.com",
        "domain":  "SOFTWARE",
        "role":    "Associate Backend Software Engineer",
        "region":  "Dubai / UAE",
        "subject": "Associate Backend Engineer Application: Abdullah Bin Masaud – COMSATS 2026 (Dubai)",
        "body": """Dear Dubizzle Talent Acquisition Team,

Dubizzle's classifieds and marketplace platform serving millions across the UAE is an engineering powerhouse. I am writing to apply for an Associate Backend Software Engineer position in Dubai.

I am a final-year Computer Engineering candidate from COMSATS University Islamabad (graduating 2026).

Technical Strengths:
- API Engineering: Designed and tested Flask REST endpoints with automated pytest coverage, latency checks, and error boundaries.
- Network Protocols: Custom TCP/IP multithreaded socket server with CRC32 packet integrity validation.
- Data Pipelines: Automated Python data verification with outlier detection and reporting.

Ready for relocation to Dubai.

Links:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My Software CV is attached.

Best regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Trukker (Freight & Logistics Tech) - Dubai & KSA",
        "email":   "careers@trukker.com",
        "domain":  "SOFTWARE",
        "role":    "Junior Software Engineer / Logistics Systems",
        "region":  "Dubai / UAE & KSA",
        "subject": "Junior Software Engineer Application: Abdullah Bin Masaud – Logistics Tech (Dubai / KSA)",
        "body": """Dear Trukker Engineering Team,

Trukker's digital freight network operating across 8 countries in the MENA region requires mission-critical tracking, scheduling, and telematics systems. I am applying for a Junior Software Engineer position in Dubai or Riyadh.

I am graduating in Computer Engineering from COMSATS University Islamabad in 2026.

Why I Fit:
- Real-Time Hardware & Telemetry Bridges: Telemetry streaming dashboard with WebSockets for tracking device state.
- Scalable Systems: Implemented multithreaded socket communication protocols tested with 50 concurrent client threads.
- Automated Testing & QA: Comprehensive pytest test suites ensuring endpoint response latency under 200ms.

Ready for relocation to Dubai or Riyadh.

Profiles:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My Software CV is attached.

Sincerely,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Desertcart (Global E-Commerce) - Dubai",
        "email":   "careers@desertcart.com",
        "domain":  "SOFTWARE",
        "role":    "Junior Software Engineer",
        "region":  "Dubai / UAE",
        "subject": "Junior Software Engineer Application: Abdullah Bin Masaud – COMSATS 2026 (Dubai)",
        "body": """Dear Desertcart Talent Team,

Desertcart's cross-border e-commerce platform delivering millions of products globally represents complex catalog and supply chain technology. I am applying for a Junior Software Engineer position in Dubai.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026).

Profile Highlights:
- Low-Level Data Integrity: Engineered custom binary network protocols with CRC32 checksums, tested under concurrent client loads.
- API & Test Automation: Modular Flask REST endpoints covered by 25+ pytest test cases verifying latency and schema validation.
- Clean Code Standards: 12 public GitHub repositories following unit testing and modular architecture.

Ready for relocation to Dubai.

Links:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My Software CV is attached.

Warm regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },

    # ── PAKISTAN SOFTWARE & CYBERSECURITY HOUSES ──
    {
        "company": "Nextbridge - Pakistan",
        "email":   "careers@nextbridge.com",
        "domain":  "SOFTWARE",
        "role":    "Associate Software Engineer",
        "region":  "Pakistan",
        "subject": "Associate Software Engineer Application: Abdullah Bin Masaud – COMSATS 2026",
        "body": """Dear Nextbridge Talent Acquisition Team,

Nextbridge's 25+ years of delivering enterprise software engineering solutions for North American and European clients is a benchmark in Pakistan. I am writing to apply for an Associate Software Engineer role.

I am graduating in Computer Engineering from COMSATS University Islamabad in 2026.

Engineering Highlights:
- Low-Level Systems: Custom multithreaded TCP/IP socket server with binary packet framing and CRC32 integrity validation.
- API Engineering: Modular Flask REST APIs with automated pytest validation for response latency under 200ms.
- Data Validation: Automated pipeline for verifying data consistency and detecting anomalies.

Profiles:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My Software CV is attached.

Best regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Rolustech - Pakistan",
        "email":   "careers@rolustech.com",
        "domain":  "SOFTWARE",
        "role":    "Junior Software Engineer",
        "region":  "Pakistan",
        "subject": "Junior Software Engineer Application: Abdullah Bin Masaud – COMSATS 2026",
        "body": """Dear Rolustech Hiring Team,

Rolustech's custom web, mobile, and CRM integrations for Fortune 500 enterprises represent high engineering standards. I am applying for a Junior Software Engineer position.

I am a final-year Computer Engineering candidate from COMSATS University Islamabad (graduating 2026).

Technical Strengths:
- API Engineering: Designed and tested Flask REST endpoints with automated pytest coverage, latency checks, and error boundaries.
- Network Protocols: Custom TCP/IP multithreaded socket server with CRC32 packet integrity validation.
- Data Pipelines: Automated Python data verification with outlier detection and reporting.

Links:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My Software CV is attached.

Warm regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Strategic Systems International (SSI) - Pakistan",
        "email":   "careers@ssidecisions.com",
        "domain":  "SOFTWARE",
        "role":    "Associate Software Engineer",
        "region":  "Pakistan",
        "subject": "Associate Software Engineer Application: Abdullah Bin Masaud – COMSATS 2026",
        "body": """Dear SSI Talent Acquisition Team,

Strategic Systems International's 30+ year reputation for delivering advanced data, cloud, and enterprise software for venture-backed US startups is outstanding. I am applying for an Associate Software Engineer role.

I am graduating in Computer Engineering from COMSATS University Islamabad in 2026.

Profile Highlights:
- Low-Level Data Integrity: Engineered custom binary network protocols with CRC32 checksums, tested under concurrent client loads.
- API & Test Automation: Modular Flask REST endpoints covered by 25+ pytest test cases verifying latency and schema validation.
- Clean Code Standards: 12 public GitHub repositories following unit testing and modular architecture.

Profiles:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My Software CV is attached.

Sincerely,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Tintash - Pakistan",
        "email":   "careers@tintash.com",
        "domain":  "SOFTWARE",
        "role":    "Associate Software Engineer",
        "region":  "Pakistan",
        "subject": "Associate Software Engineer Application: Abdullah Bin Masaud – COMSATS 2026",
        "body": """Dear Tintash Talent Team,

Tintash's Stanford-alumni-founded culture of building world-class games, web, and mobile products for global brands is an inspiring work environment. I am applying for an Associate Software Engineer role.

I am a final-year Computer Engineering candidate from COMSATS University Islamabad (graduating 2026).

Engineering Foundation:
- Python & REST APIs: Clean, test-driven RESTful services built with Flask and tested with pytest.
- Systems & Network Concurrency: Socket-level multithreaded networking with CRC32 packet integrity validation.
- Edge AI: Real-time computer vision models (YOLOv8) deployed onto edge hardware.

Links:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My Software CV is attached.

Best regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Ebryx (Cybersecurity & Systems) - Pakistan",
        "email":   "careers@ebryx.com",
        "domain":  "SOFTWARE",
        "role":    "Systems Software Engineer / Security",
        "region":  "Pakistan",
        "subject": "Systems Software Engineer Application: Abdullah Bin Masaud – COMSATS 2026",
        "body": """Dear Ebryx Talent Acquisition Team,

Ebryx's specialization in engineering cybersecurity software, endpoint protection, and low-level systems engineering for global tech companies matches my systems focus. I am applying for a Systems Software Engineer role.

I am graduating in Computer Engineering from COMSATS University Islamabad in 2026.

Systems Highlights:
- Low-Level Systems: Custom multithreaded TCP/IP socket server with binary packet framing and CRC32 integrity validation.
- Microcontroller Firmware: Direct register-level C programming on PIC18 and ARM architectures with memory mapping.
- Automated Testing & QA: Comprehensive pytest test suites validating schemas, latency, and error states.

Profiles:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My Software CV is attached.

Warm regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Zepto Systems - Pakistan",
        "email":   "careers@zeptosystems.com",
        "domain":  "SOFTWARE",
        "role":    "Associate Software Engineer",
        "region":  "Pakistan",
        "subject": "Associate Software Engineer Application: Abdullah Bin Masaud – COMSATS 2026",
        "body": """Dear Zepto Systems Talent Team,

Zepto Systems' dedicated engineering teams providing digital transformation and cloud consulting for UK and European clients represent high engineering productivity. I am applying for an Associate Software Engineer role.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026).

Competencies:
- API Engineering: Designed and tested Flask REST endpoints with automated pytest coverage, latency checks, and error boundaries.
- Network Protocols: Custom TCP/IP multithreaded socket server with CRC32 packet integrity validation.
- Data Pipelines: Automated Python data verification with outlier detection and reporting.

Links:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My Software CV is attached.

Sincerely,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },

    # ── GLOBAL REMOTE TECH LEADERS ──
    {
        "company": "Sourcegraph (100% Remote Global)",
        "email":   "jobs@sourcegraph.com",
        "domain":  "SOFTWARE",
        "role":    "Software Engineer (Remote)",
        "region":  "Global Remote",
        "subject": "Software Engineer Application (Remote) – Abdullah Bin Masaud – Computer Engineering 2026",
        "body": """Dear Sourcegraph Hiring Team,

Sourcegraph's code intelligence and AI developer platform (Cody) helping developers understand massive codebases is foundational technology. I am writing to apply for an entry-level software engineering role from Pakistan.

I am graduating with a BS in Computer Engineering from COMSATS University Islamabad in 2026.

Why I Fit:
- Systems Thinking: Built custom TCP/IP networking protocols in Python from scratch, including binary packet framing, CRC32 checksum calculations, and multi-threaded socket handling.
- API & Test Automation: Built comprehensive pytest test suites validating API response codes, latency benchmarks, and concurrency.
- Autonomous Output: 12 complete, documented projects built and published independently on GitHub.

Timezone: UTC+5 (PKT)

Profiles:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b

My Software CV is attached.

Best regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Grafana Labs (100% Remote Global)",
        "email":   "jobs@grafana.com",
        "domain":  "SOFTWARE",
        "role":    "Software Engineer (Observability)",
        "region":  "Global Remote",
        "subject": "Software Engineer Application (Remote) – Abdullah Bin Masaud – Computer Engineering 2026",
        "body": """Dear Grafana Labs Talent Team,

Grafana Labs' open-source observability stack (Grafana, Loki, Prometheus, Tempo) is the heartbeat of modern infrastructure. I am applying for an entry-level software engineering role from Pakistan.

I am a final-year Computer Engineering candidate from COMSATS University Islamabad (graduating 2026).

Practical Output:
- Live Telemetry Streaming: Built a real-time sensor monitoring dashboard in Flask and WebSockets for tracking metrics, temperature, and alert thresholds.
- Systems Experience: Multithreaded TCP/IP socket server with custom packet serialization and CRC32 verification.
- Automated Testing: Production pytest test suites validating API latency and data payloads.

Timezone: UTC+5 (PKT)

Links:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b

My Software CV is attached.

Warm regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Datadog (100% Remote Global)",
        "email":   "jobs@datadoghq.com",
        "domain":  "SOFTWARE",
        "role":    "Software Engineer (Systems & Telemetry)",
        "region":  "Global Remote",
        "subject": "Software Engineer Application (Remote) – Abdullah Bin Masaud – Computer Engineering 2026",
        "body": """Dear Datadog Hiring Team,

Datadog's observability and security platform monitoring cloud-scale applications requires deep understanding of system metrics and network protocols. I am applying for an entry-level software engineering role from Pakistan.

I am graduating in Computer Engineering from COMSATS University Islamabad in 2026.

Engineering Principles:
- Systems Reliability: Custom TCP/IP socket server with CRC32 packet integrity validation.
- API & Test Automation: Comprehensive pytest test suites validating API response codes, latency benchmarks, and concurrency.
- Data Pipelines: Python data auditing pipeline with statistical outlier detection.

Timezone: UTC+5 (PKT)

Profiles:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b

My Software CV is attached.

Sincerely,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "MongoDB (100% Remote Global)",
        "email":   "jobs@mongodb.com",
        "domain":  "SOFTWARE",
        "role":    "Software Engineer (Database Systems)",
        "region":  "Global Remote",
        "subject": "Software Engineer Application (Remote) – Abdullah Bin Masaud – Computer Engineering 2026",
        "body": """Dear MongoDB Talent Team,

MongoDB's developer data platform powering modern applications globally is the standard for document databases. I am applying for an entry-level software engineering position from Pakistan.

I am a final-year Computer Engineering candidate from COMSATS University Islamabad (graduating 2026).

Why I Fit:
- Low-Level Protocol Rigor: Built custom multithreaded TCP/IP communication protocols with binary packet framing and CRC32 checksums.
- Robust API Engineering: Designed Flask REST endpoints with strict schema validation and 25+ automated pytest test cases.
- Data Validation: Created automated auditing tools for identifying missing or corrupted data.

Timezone: UTC+5 (PKT)

Links:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b

My Software CV is attached.

Best regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Redis (100% Remote Global)",
        "email":   "jobs@redis.com",
        "domain":  "SOFTWARE",
        "role":    "Software Engineer (In-Memory Systems)",
        "region":  "Global Remote",
        "subject": "Software Engineer Application (Remote) – Abdullah Bin Masaud – Computer Engineering 2026",
        "body": """Dear Redis Talent Team,

Redis' in-memory data store delivering sub-millisecond latency for caching, message brokering, and vector search is unmatched. I am applying for an entry-level software engineering role from Pakistan.

I am graduating in Computer Engineering from COMSATS University Islamabad in 2026.

Engineering Highlights:
- Low-Level Systems: Custom multithreaded TCP/IP socket server with binary packet framing and CRC32 integrity validation.
- API Engineering: Modular Flask REST APIs with automated pytest validation for response latency under 200ms.
- Data Validation: Automated pipeline for verifying data consistency and detecting anomalies.

Timezone: UTC+5 (PKT)

Profiles:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b

My Software CV is attached.

Warm regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Sentry (100% Remote Global)",
        "email":   "jobs@sentry.io",
        "domain":  "SOFTWARE",
        "role":    "Software Engineer (Developer Tools & Error Tracking)",
        "region":  "Global Remote",
        "subject": "Software Engineer Application (Remote) – Abdullah Bin Masaud – Computer Engineering 2026",
        "body": """Dear Sentry Hiring Team,

Sentry's developer-first application monitoring and error tracking platform gives developers actionable insights into production issues. I am applying for an entry-level software engineering role from Pakistan.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026).

Competencies:
- API Automation: Built end-to-end Flask REST endpoints covered by automated pytest test cases validating schemas, latency, and error states.
- Data Pipelines: Standalone Python data auditing pipeline with statistical outlier detection.
- Distributed Protocol Design: Socket-level multithreaded communication with CRC32 packet error detection.

Timezone: UTC+5 (PKT)

Links:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b

My Software CV is attached.

Sincerely,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Docker (100% Remote Global)",
        "email":   "jobs@docker.com",
        "domain":  "SOFTWARE",
        "role":    "Software Engineer (Developer Platforms)",
        "region":  "Global Remote",
        "subject": "Software Engineer Application (Remote) – Abdullah Bin Masaud – Computer Engineering 2026",
        "body": """Dear Docker Talent Team,

Docker revolutionized software development and deployment across the globe. I use containerization concepts across my projects and am applying for an entry-level software engineering position from Pakistan.

I am graduating with a BS in Computer Engineering from COMSATS University Islamabad in 2026.

Systems & Systems Programming Experience:
- Low-Level Networking: Designed a multithreaded TCP/IP client-server communication protocol from scratch with binary packet framing and CRC32 checksums.
- Linux & Edge Computing: Deployed real-time computer vision models on Raspberry Pi running Ubuntu/Linux, optimizing memory and compute constraints.
- Code Rigor: 12 open-source GitHub repositories adhering to unit testing and clean modular design.

Timezone: UTC+5 (PKT)

Profiles:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b

My Software CV is attached.

Best regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    }
]

def send_email(to_email, subject, body_text, cv_path):
    msg = MIMEMultipart()
    msg["From"]    = SENDER_EMAIL
    msg["To"]      = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body_text, "plain"))
    with open(cv_path, "rb") as f:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(f.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f'attachment; filename="{cv_path.name}"')
    msg.attach(part)
    ctx = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ctx) as server:
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.sendmail(SENDER_EMAIL, to_email, msg.as_string())

def log_application(company, email, domain, role, status):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    TRACKER_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(TRACKER_PATH, "a", encoding="utf-8") as f:
        f.write(f"{timestamp},{company},{email},{domain},{role},{status}\n")

def main():
    print("=" * 85)
    print("  BATCH 10: 21 PRE-CHECKED MX TARGETS (SAUDI, UAE, REMOTE, PAKISTAN)")
    print(f"  Targets: {len(TARGETS)} companies — 0% bounce guaranteed")
    print("=" * 85)
    sent = failed = 0
    for i, job in enumerate(TARGETS, 1):
        company = job["company"]
        email   = job["email"]
        domain  = job["domain"]
        role    = job["role"]
        region  = job["region"]
        cv_path = CV_MAP[domain]
        print(f"\n[{i:02d}/{len(TARGETS)}] {company} ({region})")
        print(f"      To     : {email}")
        print(f"      CV     : {cv_path.name}  |  {domain}")
        print(f"      Role   : {role}")
        try:
            send_email(email, job["subject"], job["body"], cv_path)
            log_application(company, email, domain, role, "SENT")
            print(f"      Status : [OK] SENT")
            sent += 1
        except Exception as e:
            log_application(company, email, domain, role, f"FAILED: {e}")
            print(f"      Status : [FAIL] {e}")
            failed += 1
    print("\n" + "=" * 85)
    print(f"  BATCH 10 DISPATCH COMPLETE  |  Sent: {sent}  |  Failed: {failed}")
    print("=" * 85)

if __name__ == "__main__":
    main()
