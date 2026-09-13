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

# ── BATCH 8: 23 PRE-CHECKED MX TARGETS (SAUDI, UAE, REMOTE, PAKISTAN) ───────
TARGETS = [
    # ── SAUDI ARABIA TECH GIANTS & UNICORNS ──
    {
        "company": "Geidea (FinTech & POS Leader KSA)",
        "email":   "careers@geidea.net",
        "domain":  "SOFTWARE",
        "role":    "Junior Software Engineer (Payments)",
        "region":  "Saudi Arabia",
        "subject": "Junior Software Engineer Application: Abdullah Bin Masaud – FinTech (KSA)",
        "body": """Dear Geidea Talent Acquisition Team,

Geidea's leadership in digital payment solutions, point-of-sale terminals, and payment processing infrastructure across Saudi Arabia requires resilient systems engineering. I am writing to apply for a Junior Software Engineer position in Riyadh.

I am graduating in Computer Engineering from COMSATS University Islamabad in 2026.

Engineering Highlights:
- Low-Level Systems: Custom multithreaded TCP/IP socket server with binary packet framing and CRC32 integrity validation.
- API Engineering: Modular Flask REST APIs with automated pytest validation for response latency under 200ms.
- Data Validation: Automated pipeline for verifying data consistency and detecting anomalies.

Ready for immediate relocation to Riyadh.

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
        "company": "Foodics (Restaurant Tech Unicorn KSA)",
        "email":   "careers@foodics.com",
        "domain":  "SOFTWARE",
        "role":    "Associate Backend Software Engineer",
        "region":  "Saudi Arabia",
        "subject": "Associate Backend Engineer Application: Abdullah Bin Masaud – COMSATS 2026 (Riyadh)",
        "body": """Dear Foodics Talent Team,

Foodics' cloud POS and restaurant management ecosystem powering thousands of businesses across the GCC represents high-scale product engineering. I am writing to apply for an Associate Backend Engineer role.

I am a final-year Computer Engineering candidate from COMSATS University Islamabad, Pakistan (graduating 2026).

Relevant Experience:
- Production REST APIs: Flask services covered by pytest test suites verifying endpoints, error handling, and concurrency.
- Network Protocols: Custom TCP/IP client-server protocol with CRC32 packet integrity validation.
- Data Reliability: Custom Python pipeline for statistical validation of operational datasets.

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
        "company": "Unifonic (Cloud Communications Platform KSA)",
        "email":   "careers@unifonic.com",
        "domain":  "TELECOM",
        "role":    "Communications & Network Software Engineer",
        "region":  "Saudi Arabia",
        "subject": "Communications Software Engineer: Abdullah Bin Masaud – COMSATS 2026 (Riyadh / Remote)",
        "body": """Dear Unifonic Talent Team,

Unifonic's customer communication platform (SMS, voice, WhatsApp, APIs) delivering billions of messages across the Middle East is the gold standard for CPaaS. I am applying for an engineering position in Riyadh or remote.

I am graduating in Computer Engineering from COMSATS University Islamabad in 2026.

Communications & Telecommunications Portfolio:
- Custom Network Protocol Engine: Built a multithreaded TCP/IP client-server system in Python with custom binary packet framing, CRC32 integrity validation, and concurrent load testing.
- Real-Time Streaming: Built live telemetry broadcasting systems over WebSockets and Socket.IO.
- Hardware Communications: Low-level serial UART transmission on PIC18 microcontrollers.

Profiles:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My Telecom & Network CV is attached.

Sincerely,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Salla (E-Commerce Platform Leader KSA)",
        "email":   "careers@salla.sa",
        "domain":  "SOFTWARE",
        "role":    "Associate Backend Software Engineer",
        "region":  "Saudi Arabia",
        "subject": "Associate Backend Engineer Application: Abdullah Bin Masaud – COMSATS 2026 (KSA)",
        "body": """Dear Salla Recruitment Team,

Salla's platform enabling tens of thousands of e-commerce stores across Saudi Arabia is driving the Kingdom's digital commerce transformation. I am writing to apply for an Associate Backend Engineer role.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026).

Technical Strengths:
- API Engineering: Modular Flask REST APIs with automated testing and structured JSON schemas.
- Concurrency & Reliability: Multi-client socket handling with CRC32 packet integrity validation.
- Clean Code Standards: 12 public GitHub repositories following unit testing and modular architecture.

Ready for relocation to Saudi Arabia.

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
        "company": "Zid (Retail & E-Commerce Platform KSA)",
        "email":   "careers@zid.sa",
        "domain":  "SOFTWARE",
        "role":    "Junior Software Engineer",
        "region":  "Saudi Arabia",
        "subject": "Junior Software Engineer Application: Abdullah Bin Masaud – COMSATS 2026 (KSA)",
        "body": """Dear Zid Talent Acquisition Team,

Zid's retail enablement platform across Saudi Arabia and the GCC empowers modern merchants. I am writing to apply for a Junior Software Engineer position in Riyadh.

I am graduating in Computer Engineering from COMSATS University Islamabad in 2026.

Profile Highlights:
- Python & API Development: Production REST APIs with full pytest test automation and Swagger docs.
- Systems Concurrency: Multithreaded TCP/IP client-server system with CRC32 packet error detection.
- Data Quality Automation: Python QA pipeline with statistical anomaly detection.

Ready for relocation to Riyadh.

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
        "company": "Nearpay (SoftPOS & FinTech KSA)",
        "email":   "careers@nearpay.io",
        "domain":  "SOFTWARE",
        "role":    "Junior Software / Payments Systems Engineer",
        "region":  "Saudi Arabia",
        "subject": "Junior Software Engineer (Payments): Abdullah Bin Masaud – Nearpay (KSA / Remote)",
        "body": """Dear Nearpay Talent Team,

Nearpay's SoftPOS and contactless payment infrastructure developed in Saudi Arabia is revolutionizing card acceptance. I am applying for a Junior Software Engineer role.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026).

Why I Fit Nearpay:
- Low-Level Data Integrity: Engineered custom binary network protocols with CRC32 checksums, tested under concurrent client loads.
- API & Test Automation: Modular Flask REST endpoints covered by 25+ pytest test cases verifying latency and schema validation.
- Systems Fundamentals: Direct register-level firmware and hardware interface experience.

Available for Riyadh or remote.

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

    # ── DUBAI & UAE TECH ──
    {
        "company": "Talabat (Delivery Hero MENA) - Dubai",
        "email":   "careers@talabat.com",
        "domain":  "SOFTWARE",
        "role":    "Associate Backend Software Engineer",
        "region":  "Dubai / UAE",
        "subject": "Associate Backend Engineer Application: Abdullah Bin Masaud – COMSATS 2026 (Dubai)",
        "body": """Dear Talabat Talent Acquisition Team,

Talabat's on-demand delivery ecosystem serving millions across the Middle East requires software engineered for peak reliability. I am writing to apply for an Associate Backend Engineer role in Dubai.

I am graduating in Computer Engineering from COMSATS University Islamabad in 2026.

Technical Strengths:
- API Engineering: Designed and tested Flask REST endpoints with automated pytest coverage, latency checks, and error boundaries.
- Network Protocols: Custom TCP/IP multithreaded socket server with CRC32 packet integrity validation.
- Data Pipelines: Automated Python data verification with outlier detection and reporting.

Ready for relocation to Dubai.

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
        "company": "Careem (Super App MENA) - Dubai",
        "email":   "careers@careem.com",
        "domain":  "SOFTWARE",
        "role":    "Junior Software Engineer",
        "region":  "Dubai / UAE",
        "subject": "Junior Software Engineer Application: Abdullah Bin Masaud – COMSATS 2026 (Dubai / Remote)",
        "body": """Dear Careem Talent Team,

Careem's pioneering super-app platform connecting millions of captains and customers across the region represents world-class engineering. I am applying for a Junior Software Engineer position in Dubai or remote.

I am a final-year Computer Engineering candidate from COMSATS University Islamabad (graduating 2026).

Highlights:
- Concurrency & Network Systems: Custom multithreaded socket server with CRC32 packet verification, tested under 50 concurrent client threads.
- Modular APIs: Flask REST API with automated pytest test coverage.
- Edge AI & Computer Vision: Built VisionAid (YOLOv8) deployed on edge devices.

Available for Dubai relocation or remote work.

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
        "company": "Noon.com (E-Commerce Ecosystem) - Dubai & Riyadh",
        "email":   "noon@noon.com",
        "domain":  "AI",
        "role":    "Junior AI / Computer Vision Engineer",
        "region":  "Dubai / UAE & KSA",
        "subject": "Junior AI Engineer Application: Abdullah Bin Masaud – COMSATS 2026 (Dubai / Riyadh)",
        "body": """Dear Noon.com Talent Acquisition Team,

Noon's position as the homegrown digital marketplace of the Middle East requires advanced computer vision, catalog intelligence, and logistics optimization. I am applying for a Junior AI / Computer Vision Engineer role.

I am graduating in Computer Engineering from COMSATS University Islamabad in 2026.

Hands-on AI Highlights:
- VisionAid (FYP): Built an end-to-end edge AI assistive device with YOLOv8 running on Raspberry Pi 4.
- U-Net Segmentation: Medical image segmentation on MRI scans with 91%+ Dice accuracy.
- XGBoost Engine: Production machine learning pipeline with SHAP explainability and Flask REST API integration.

Ready for relocation to Dubai or Riyadh.

Profiles:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My AI CV is attached.

Best regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Hub71 (Tech Ecosystem) - Abu Dhabi",
        "email":   "info@hub71.com",
        "domain":  "SOFTWARE",
        "role":    "Technology & Software Engineering Graduate",
        "region":  "Dubai / UAE",
        "subject": "Software Engineering Graduate Application: Abdullah Bin Masaud – COMSATS 2026 (Abu Dhabi)",
        "body": """Dear Hub71 Talent & Community Team,

Hub71's flagship tech ecosystem in Abu Dhabi connecting global startups with regional growth is inspiring. I am applying to contribute my software engineering capabilities to Hub71 startups and technical initiatives.

I am graduating with a BS in Computer Engineering from COMSATS University Islamabad in 2026.

Technical Portfolio:
- Python & REST APIs: Clean, test-driven RESTful services built with Flask and tested with pytest.
- Systems & Network Concurrency: Socket-level multithreaded networking with CRC32 packet integrity validation.
- Edge AI: Real-time computer vision models (YOLOv8) deployed onto edge hardware.

Ready to relocate to Abu Dhabi.

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

    # ── PAKISTAN SOFTWARE HOUSES & TECH FIRMS ──
    {
        "company": "Avanza Solutions - Pakistan",
        "email":   "careers@avanzasolutions.com",
        "domain":  "SOFTWARE",
        "role":    "Associate Software Engineer (FinTech & Blockchain)",
        "region":  "Pakistan",
        "subject": "Associate Software Engineer Application: Abdullah Bin Masaud – COMSATS 2026",
        "body": """Dear Avanza Solutions Talent Acquisition Team,

Avanza's leadership in banking software, payment switches, and blockchain infrastructure across Pakistan and the Middle East requires dependable systems engineering. I am writing to apply for an Associate Software Engineer role.

I am a final-year Computer Engineering candidate at COMSATS University Islamabad (graduating 2026).

Why My Background Fits:
- Low-Level Protocol Rigor: Built custom multithreaded TCP/IP communication protocols with binary packet framing and CRC32 checksums.
- Robust API Engineering: Designed Flask REST endpoints with strict schema validation and 25+ automated pytest test cases.
- Data Validation: Created automated auditing tools for identifying missing or corrupted data.

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
        "company": "Autosoft Dynamics - Pakistan",
        "email":   "careers@autosoftdynamics.com",
        "domain":  "SOFTWARE",
        "role":    "Junior Software Engineer (Banking Platforms)",
        "region":  "Pakistan",
        "subject": "Junior Software Engineer Application: Abdullah Bin Masaud – COMSATS 2026",
        "body": """Dear Autosoft Dynamics Hiring Team,

Autosoft's core banking and financial automation software powering major financial institutions represents high-consequence engineering. I am applying for a Junior Software Engineer position.

I am graduating in Computer Engineering from COMSATS University Islamabad in 2026.

Relevant Strengths:
- Systems Reliability: Custom TCP/IP socket server with CRC32 packet integrity validation.
- API & Test Automation: Comprehensive pytest test suites validating API response codes, latency benchmarks, and concurrency.
- Data Quality Pipelines: Python data auditing pipeline with statistical outlier detection.

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
        "company": "TPS Worldwide - Pakistan",
        "email":   "careers@tpsworldwide.com",
        "domain":  "SOFTWARE",
        "role":    "Associate Software Engineer (Cards & Payments)",
        "region":  "Pakistan",
        "subject": "Associate Software Engineer Application: Abdullah Bin Masaud – COMSATS 2026",
        "body": """Dear TPS Worldwide Talent Team,

TPS Worldwide's cards, payments, and transaction switching solutions powering financial networks across 30+ countries require high-integrity systems engineering. I am applying for an Associate Software Engineer role.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026).

Technical Highlights:
- Network Concurrency: Multi-threaded socket communication with binary packet framing and CRC32 verification.
- Backend APIs: Production REST APIs with full pytest test automation and Swagger docs.
- Data Reliability: Custom data quality validation pipelines in Python.

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
        "company": "CureMD - HealthTech",
        "email":   "careers@curemd.com",
        "domain":  "SOFTWARE",
        "role":    "Software QA & Automation Engineer",
        "region":  "Pakistan",
        "subject": "Software QA & Automation Engineer Application: Abdullah Bin Masaud – COMSATS 2026",
        "body": """Dear CureMD Talent Acquisition Team,

CureMD's enterprise EHR, billing, and clinical software serving healthcare providers globally demands zero-defect quality standards. I am applying for a Software QA / Automation Engineer position.

I am graduating in Computer Engineering from COMSATS University Islamabad in 2026.

QA & Automation Strengths:
- Automated Testing: Built automated pytest test suites covering 25+ test cases for status codes, latency thresholds (<200ms), schema enforcement, and concurrent requests.
- Data Quality Auditing: Developed a standalone Python QA auditing engine implementing IQR statistical filtering and automated report generation.
- HealthTech Project: Built an AI medical image segmentation model with a 91%+ Dice similarity coefficient.

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
        "company": "Techlogix - Pakistan",
        "email":   "careers@techlogix.com",
        "domain":  "SOFTWARE",
        "role":    "Associate Software Engineer",
        "region":  "Pakistan",
        "subject": "Associate Software Engineer Application: Abdullah Bin Masaud – COMSATS 2026",
        "body": """Dear Techlogix Talent Team,

Techlogix's enterprise software consulting and digital transformation solutions across North America and the Middle East represent premier engineering. I am applying for an Associate Software Engineer role.

I am a final-year Computer Engineering candidate from COMSATS University Islamabad (graduating 2026).

Core Competencies:
- API Engineering: Modular Flask REST APIs with automated testing and structured JSON schemas.
- Concurrency & Reliability: Multi-client socket handling with CRC32 packet integrity validation.
- Clean Code Standards: 12 public GitHub repositories following unit testing and modular architecture.

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
        "company": "Tkxel - Pakistan",
        "email":   "careers@tkxel.com",
        "domain":  "SOFTWARE",
        "role":    "Associate Software Engineer",
        "region":  "Pakistan",
        "subject": "Associate Software Engineer Application: Abdullah Bin Masaud – COMSATS 2026",
        "body": """Dear Tkxel Recruitment Team,

Tkxel's custom software development services for global clients reflect high engineering productivity. I am writing to apply for an Associate Software Engineer position.

I am graduating in Computer Engineering from COMSATS University Islamabad in 2026.

Technical Portfolio:
- Python & REST APIs: Clean, test-driven RESTful services built with Flask and tested with pytest.
- Systems & Network Concurrency: Socket-level multithreaded networking with CRC32 packet integrity validation.
- Edge AI: Real-time computer vision models (YOLOv8) deployed onto edge hardware.

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
    {
        "company": "Confiz - Pakistan",
        "email":   "careers@confiz.com",
        "domain":  "AI",
        "role":    "Junior AI / Computer Vision Engineer",
        "region":  "Pakistan",
        "subject": "Junior AI Engineer Application: Abdullah Bin Masaud – COMSATS 2026",
        "body": """Dear Confiz Talent Team,

Confiz's retail AI, cloud solutions, and digital innovation for international clients represents cutting-edge engineering. I am applying for a Junior AI / Computer Vision Engineer position.

I am a final-year Computer Engineering candidate from COMSATS University Islamabad (graduating 2026).

AI & Deep Learning Portfolio:
1. VisionAid (FYP): Real-time assistive computer vision system (YOLOv8) deployed onto edge hardware (Raspberry Pi 4) with optimized inference latency.
2. Deep Learning Segmentation: U-Net architecture trained on medical MRI scans, achieving a 91%+ Dice similarity score.
3. Predictive Engineering: XGBoost-based customer risk engine with SHAP explainability and Flask REST deployment.

Profiles:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My AI CV is attached.

Best regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "NetSol Technologies - Pakistan",
        "email":   "careers@netsoltech.com",
        "domain":  "SOFTWARE",
        "role":    "Associate Software Engineer / Trainee",
        "region":  "Pakistan",
        "subject": "Associate Software Engineer Application: Abdullah Bin Masaud – COMSATS 2026",
        "body": """Dear NetSol Technologies Talent Acquisition Team,

NetSol's NFS Ascent platform powering global asset finance and leasing represents the highest standard of enterprise software engineering in Pakistan. I am writing to apply for an Associate Software Engineer role.

I am graduating in Computer Engineering from COMSATS University Islamabad in 2026.

Profile Highlights:
- Low-Level Data Integrity: Engineered custom binary network protocols with CRC32 checksums, tested under concurrent client loads.
- API & Test Automation: Modular Flask REST endpoints covered by 25+ pytest test cases verifying latency and schema validation.
- Systems Fundamentals: 12 public GitHub repositories demonstrating solid architectural standards.

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

    # ── GLOBAL REMOTE TECH COMPANIES ──
    {
        "company": "Buffer (100% Remote Global)",
        "email":   "jobs@buffer.com",
        "domain":  "SOFTWARE",
        "role":    "Software Engineer (Remote)",
        "region":  "Global Remote",
        "subject": "Software Engineer Application (Remote) – Abdullah Bin Masaud – Computer Engineering 2026",
        "body": """Dear Buffer Hiring Team,

Buffer's transparent, remote-first engineering culture and asynchronous workflow matches how I build software. I am applying for an entry-level software engineering position from Pakistan.

I am graduating with a BS in Computer Engineering from COMSATS University Islamabad in 2026.

Engineering Principles:
- Self-Driven Autonomy: Conceived, implemented, and documented 12 public GitHub projects independently.
- Clean APIs: Modular Flask REST APIs with automated pytest validation and clear Swagger docs.
- Network Protocols: Custom TCP/IP multithreaded socket server with CRC32 packet integrity validation.

Location: Pakistan (UTC+5)

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
        "company": "Zapier (100% Remote Global)",
        "email":   "jobs@zapier.com",
        "domain":  "SOFTWARE",
        "role":    "Software Engineer (Remote)",
        "region":  "Global Remote",
        "subject": "Software Engineer Application (Remote) – Abdullah Bin Masaud – Computer Engineering 2026",
        "body": """Dear Zapier Talent Team,

Zapier's mission of connecting web services and automating workflows at global scale requires deep API literacy. I am writing to apply for an entry-level software engineering role from Pakistan.

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

Warm regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Doist (100% Remote Global)",
        "email":   "jobs@doist.com",
        "domain":  "SOFTWARE",
        "role":    "Software Engineer (Remote)",
        "region":  "Global Remote",
        "subject": "Software Engineer Application (Remote) – Abdullah Bin Masaud – Computer Engineering 2026",
        "body": """Dear Doist Hiring Team,

Doist's dedication to asynchronous communication, thoughtful productivity (Todoist & Twist), and remote work excellence aligns with my engineering values. I am applying for a software engineering position from Pakistan.

I am graduating in Computer Engineering from COMSATS University Islamabad in 2026.

Engineering Foundation:
- Python & REST APIs: Clean, test-driven RESTful services built with Flask and tested with pytest.
- Systems & Network Concurrency: Socket-level multithreaded networking with CRC32 packet integrity validation.
- Anomaly & Risk Analytics: Built XGBoost predictive risk models with SHAP explainability.

Location: Pakistan (UTC+5)

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
        "company": "Toggl (100% Remote Global)",
        "email":   "jobs@toggl.com",
        "domain":  "SOFTWARE",
        "role":    "Software Engineer (Remote)",
        "region":  "Global Remote",
        "subject": "Software Engineer Application (Remote) – Abdullah Bin Masaud – Computer Engineering 2026",
        "body": """Dear Toggl Hiring Team,

Toggl's skills-first hiring approach and 100% remote-first engineering culture is refreshing. I am applying for an entry-level software engineering role from Pakistan.

I am a final-year Computer Engineering candidate from COMSATS University Islamabad (graduating 2026).

Practical Output:
- Systems Experience: Multithreaded TCP/IP socket server with custom packet serialization and CRC32 verification.
- Live Telemetry Streaming: Real-time sensor streaming dashboard built in Flask with WebSocket communication.
- Automated Testing: Production pytest test suites validating API latency and data payloads.

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
        "company": "DuckDuckGo (100% Remote Global)",
        "email":   "jobs@duckduckgo.com",
        "domain":  "SOFTWARE",
        "role":    "Software Engineer (Remote)",
        "region":  "Global Remote",
        "subject": "Software Engineer Application (Remote) – Abdullah Bin Masaud – Computer Engineering 2026",
        "body": """Dear DuckDuckGo Talent Team,

DuckDuckGo's leadership in user privacy, web search, and distributed engineering makes it a company I deeply admire. I am applying for an entry-level software engineering role from Pakistan.

I am graduating in Computer Engineering from COMSATS University Islamabad in 2026.

Why I Fit:
- Low-Level Systems: Deep understanding of TCP/IP, client-server models, and real-time socket communication.
- Automated CI/CD Testing: Built comprehensive pytest test suites validating API response codes, latency benchmarks, and concurrency.
- Autonomous Output: 12 complete, documented projects built and published independently on GitHub.

Timezone: UTC+5 (PKT)

Profiles:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b

My Software CV is attached.

Warm regards,
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
    print("  BATCH 8: 23 PRE-CHECKED MX TARGETS (SAUDI, UAE, REMOTE, PAKISTAN)")
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
    print(f"  BATCH 8 DISPATCH COMPLETE  |  Sent: {sent}  |  Failed: {failed}")
    print("=" * 85)

if __name__ == "__main__":
    main()
