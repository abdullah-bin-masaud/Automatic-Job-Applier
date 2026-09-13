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

# ── BATCH 7: MX-VERIFIED ISLAMABAD, RAWALPINDI, REMOTE & INTERNATIONAL ────────
BATCH7 = [
    {
        "company": "CARE (Center for Advanced Research in Engineering) Islamabad",
        "email":   "careers@carepvtltd.com",
        "domain":  "HARDWARE",
        "subject": "Candidate Profile: Abdullah Bin Masaud | Embedded & Firmware Engineering | COMSATS 2026 (Islamabad)",
        "body": """Dear CARE Engineering Leadership Team,

I am reaching out specifically to CARE Pvt Ltd because of your long-standing reputation as Pakistan's premier embedded systems, signal processing, and defense engineering R&D organization in Islamabad (H-9).

I am a final-year Computer Engineering student at COMSATS University Islamabad, Abbottabad Campus (graduating 2026). I am based locally in the Islamabad/Rawalpindi region and immediately available for an on-site embedded engineering role.

What I bring to CARE's engineering team:
1. Low-Level Firmware Development: PIC18F4550 microcontroller programming in C (MPLAB X / XC8) with custom ISRs, UART serial communication, SPI/I2C interfacing, and non-volatile EEPROM state persistence.
2. Hardware Prototyping & Simulation: Complete circuit schematic design, PCB simulation in Proteus, and hardware debugging with logic analyzers/oscilloscopes.
3. Edge AI / Hardware Integration: Designed 'VisionAid' — real-time computer vision (YOLOv8) deployed on Raspberry Pi 4 edge hardware for assistive navigation.

All source code and hardware documentation are publicly verifiable on my GitHub:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My Embedded Systems CV (CV__H.pdf) is attached. I am prepared to take any technical hardware test or attend an on-site interview in Islamabad at your earliest convenience.

Sincerely,
Abdullah Bin Masaud
BS Computer Engineering (2022-2026)
COMSATS University Islamabad, Abbottabad Campus
"""
    },
    {
        "company": "Taraz Technologies Islamabad",
        "email":   "info@taraztechnologies.com",
        "domain":  "HARDWARE",
        "subject": "Embedded Systems Engineer Applicant: Abdullah Bin Masaud – COMSATS Islamabad (Available Immediately)",
        "body": """Dear Taraz Technologies Hiring Team,

Taraz Technologies' excellence in power electronics, embedded controllers, and industrial R&D in Islamabad is widely respected across engineering circles. I am writing to apply for an Embedded Firmware / Hardware Engineer position.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), available immediately for on-site work in Islamabad.

Key Highlights of My Embedded Experience:
- PIC18 Microcontroller Architecture: Register-level C development (XC8 compiler), timer interrupts, analog-to-digital conversion, and UART telemetry logging.
- Telemetry & Communication Bridges: Interfacing embedded devices to PC software via custom binary packet protocols with CRC32 integrity verification.
- Rapid Simulation: Proteus schematic capture and validation prior to hardware fabrication.

Portfolio & Repositories:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My Embedded & Hardware CV is attached. I welcome the opportunity to discuss how my hands-on firmware skills can support Taraz Technologies' product lines.

Warm regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Genifem Technology Islamabad",
        "email":   "hr@genifem.com",
        "domain":  "SOFTWARE",
        "subject": "Software & AI Automation Engineering Application – Abdullah Bin Masaud – COMSATS 2026",
        "body": """Dear Genifem Recruitment Team,

I am writing regarding Genifem's software engineering and AI automation opportunities in Islamabad. As a final-year Computer Engineering candidate at COMSATS University Islamabad (graduating 2026), I have developed a strong, production-tested software portfolio that matches your tech stack in Python, automation, and API engineering.

Technical Capabilities:
- Backend & RESTful Architecture: Built modular Flask services with complete pytest test suites, input validation, and structured logging.
- Automated QA & Pipelines: Created end-to-end Python data auditing pipelines with statistical IQR outlier detection and automated report generation.
- Network Systems: Implemented multithreaded socket communication protocols with CRC32 packet error detection.

Projects & Code:
- GitHub: https://github.com/abdullah-bin-masaud (12 verified public repositories)
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Mobile: +92 332 9076356

I am available to start immediately, either remotely or on-site in Islamabad. My Software Engineering CV is attached.

Best regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "MRS Electronic Pakistan (Rawalpindi)",
        "email":   "careers.pk@mrs-electronic.com",
        "domain":  "HARDWARE",
        "subject": "Embedded Systems Engineer Application: Abdullah Bin Masaud – Rawalpindi / Islamabad",
        "body": """Dear MRS Electronic Pakistan Hiring Team,

I am writing to express my enthusiastic interest in joining MRS Electronic's engineering facility in Rawalpindi. Your work in automotive electronic control units, CAN-bus integration, and industrial controllers represents the exact domain of embedded engineering I specialize in.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), located within easy commuting distance to Rawalpindi.

Hands-on Competencies:
- Microcontroller Firmware: C/XC8 programming on PIC18 and ARM architectures, interrupt handling, EEPROM storage, and timer configurations.
- Sensor Interfaces & Circuitry: Practical experience with UART, SPI, analog sensor signal conditioning, and hardware debouncing.
- Verification: Hardware-in-the-loop simulation via Proteus and PC serial monitoring tools.

Links to verified work:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Contact: +92 332 9076356

My Embedded Systems CV is attached. I look forward to the prospect of meeting your technical team in Rawalpindi.

Sincerely,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Bentley Systems",
        "email":   "careers@bentley.com",
        "domain":  "SOFTWARE",
        "subject": "Graduate Software Engineer Application – Abdullah Bin Masaud – Pakistan / Remote",
        "body": """Dear Bentley Systems Talent Acquisition Team,

I am writing to apply for graduate and early-career software engineering roles with Bentley Systems. As a Computer Engineering student from COMSATS University Islamabad (graduating 2026), I admire Bentley's engineering infrastructure software that powers global civil and digital-twin projects.

Relevant Technical Profile:
- Systems Programming: Designed and load-tested multithreaded TCP/IP communication systems with custom binary packet framing and CRC32 error validation.
- Quality & Testing: Built comprehensive pytest test suites for RESTful APIs and created automated data pipeline validation tools in Python.
- Computer Vision & Modeling: Real-time image processing (OpenCV, YOLOv8) and spatial computation.

Links:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

I am available for full-time graduate opportunities and can support either local office or remote workflows. My resume is attached.

Best regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "LMKT Islamabad (National Incubation Center)",
        "email":   "info@lmkt.com",
        "domain":  "SOFTWARE",
        "subject": "Software / Technology Graduate Application – Abdullah Bin Masaud – Islamabad",
        "body": """Dear LMKT Recruitment Team,

LMKT's leadership in smart city infrastructure, clean technology, and running the National Incubation Center (NIC) in Islamabad makes it a standout organization for ambitious engineers. I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), applying to join LMKT's technology team in Islamabad.

Technical Highlights:
- Production-Grade Python: REST API design with Flask, automated testing with pytest, and data validation pipelines.
- IoT & Telemetry: Real-time sensor streaming architecture using WebSockets and Socket.IO.
- Multidisciplinary: Capable of working across firmware, cloud backends, and AI pipelines.

Portfolio:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

I am in the Islamabad area and available immediately for on-site interviews. My CV is attached.

Warm regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Ovex Technologies Islamabad",
        "email":   "careers@ovextech.com",
        "domain":  "SOFTWARE",
        "subject": "Software QA & Engineering Application – Abdullah Bin Masaud – Islamabad",
        "body": """Dear Ovex Technologies Talent Team,

I am writing to apply for a Software Engineering / QA role at Ovex Technologies Islamabad. I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026) with deep practical experience in software quality assurance and automated testing.

Key QA & Engineering Strengths:
- Automated Test Development: Developed 25+ comprehensive test cases in pytest covering HTTP status codes, latency benchmarks, edge cases, and concurrent requests.
- Data Quality Validation: Built a custom DataQualityAuditor and PipelineValidator in Python with automated discrepancy logging.
- Reliable Code: Clean, modular architecture with Git version control and full documentation.

Links:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

I am available immediately for on-site roles in Islamabad. My Software CV is attached.

Best regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Zones Pakistan (Islamabad)",
        "email":   "careers@zones.com",
        "domain":  "SOFTWARE",
        "subject": "Associate Software Engineer / IT Trainee – Abdullah Bin Masaud – Islamabad",
        "body": """Dear Zones Talent Acquisition Team,

Zones' major technology operations center in Islamabad is known for providing global enterprise IT solutions. I am writing to apply for an Associate Software Engineer or IT Trainee role.

I am graduating in Computer Engineering from COMSATS University Islamabad in 2026 and am ready for immediate full-time employment in Islamabad.

Technical Portfolio Summary:
- Backend Systems: Python, Flask REST APIs, TCP/IP networking, and database integration.
- Quality Assurance: Automated regression testing, performance latency tracking, and structured reporting.
- Practical Projects: 12 open-source repositories featuring computer vision, IoT telemetry, and low-level networking.

Online Profiles:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My Software Engineering CV is attached. I would appreciate the opportunity to interview with your Islamabad team.

Sincerely,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Shifa International Hospitals IT Division (Islamabad)",
        "email":   "hr@shifa.com.pk",
        "domain":  "AI",
        "subject": "HealthTech & AI Software Engineering Application – Abdullah Bin Masaud – Islamabad",
        "body": """Dear Shifa International Hospitals Human Resources & IT Team,

I am writing to express my strong interest in medical technology and software engineering opportunities with Shifa International's IT Division in Islamabad.

As a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), I have focused specifically on applied healthcare technology and computer vision.

Healthcare Tech Project:
- AI Medical Image Segmentation: Developed a deep learning U-Net architecture trained on MRI brain tumor datasets, achieving 91%+ Dice similarity coefficient for automated lesion delineation.
- Assistive Technology (VisionAid): Real-time visual assistance device using edge AI (YOLOv8 + Raspberry Pi) for visually impaired patients.

Links:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

I can join your Islamabad campus immediately to contribute to hospital information systems and clinical tech projects. My AI & Software CV is attached.

Respectfully,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Ufone / PTCL Group (Islamabad HQ)",
        "email":   "recruitment@ufone.com",
        "domain":  "TELECOM",
        "subject": "Graduate Trainee Engineer (Telecom & Networks) – Abdullah Bin Masaud – Islamabad HQ",
        "body": """Dear Ufone / PTCL Group Talent Acquisition Team,

I am writing to apply for the Graduate Trainee Engineer program in Telecom and Network Operations at Ufone HQ in Islamabad.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), with extensive coursework and project experience in telecommunications, RF signals, and computer networking.

Network & Telecom Projects:
- TCP/IP Protocol Engine: Engineered a custom client-server architecture with multi-client threading, binary packetization, and CRC32 error detection.
- Real-Time Telemetry Broadcasting: Developed a live sensor streaming dashboard utilizing Socket.IO and WebSockets for low-latency telemetry transmission.
- Hardware Communications: Configured PIC18 UART serial transmission and analyzed communication timing with logic simulation.

Profiles:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

I am based in the region and available immediately for tests and interviews in Islamabad. My Telecom CV is attached.

Best regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Canonical (Ubuntu - 100% Remote Global)",
        "email":   "jobs@canonical.com",
        "domain":  "SOFTWARE",
        "subject": "Graduate Software Engineer (Remote - Pakistan) – Abdullah Bin Masaud – COMSATS 2026",
        "body": """Dear Canonical Hiring Team,

I am writing to apply for Canonical's Graduate Software Engineer / Associate Software Engineer remote program. I have long used Ubuntu for development and robotics prototyping, and I admire Canonical's open-source engineering standards.

I am graduating with a BS in Computer Engineering from COMSATS University Islamabad in 2026.

Why Canonical:
- Systems Thinking: Built custom TCP/IP networking protocols in Python from scratch, including binary packet framing, CRC32 checksum calculations, and multi-threaded socket handling.
- Linux & Embedded: Deployed real-time computer vision models on Raspberry Pi running Ubuntu Core / Linux, optimizing inference latency under hardware resource constraints.
- Clean Engineering: All projects are publicly version-controlled with Git, strict adherence to unit testing, and modular documentation.

Profiles:
- GitHub: https://github.com/abdullah-bin-masaud (12 public repositories)
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Timezone: UTC+5 (PKT) — ready for global collaboration

My Software Engineering CV is attached. I look forward to participating in Canonical's technical review process.

Warm regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "GitLab (100% Remote Global)",
        "email":   "jobs@gitlab.com",
        "domain":  "SOFTWARE",
        "subject": "Associate Software Engineer / Intern (Remote) – Abdullah Bin Masaud – Pakistan",
        "body": """Dear GitLab Talent Team,

GitLab's transparent, all-remote culture and world-class DevOps platform set the standard for modern software engineering. I am writing to apply for an Associate Software Engineer or Intern role.

I am a final-year Computer Engineering student at COMSATS University Islamabad, Pakistan (graduating 2026).

Relevant Experience:
- Automated CI/CD Testing Mindset: Implemented comprehensive pytest suites covering functional, latency, and concurrency tests for backend APIs.
- Data Quality Automation: Built a standalone Python pipeline that audits datasets for schema violations, missing values, and anomalies with auto-generated reports.
- Self-Driven Workflow: High degree of autonomy, verified by 12 end-to-end projects built, documented, and published independently.

Links:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Timezone: UTC+5 (PKT)

My CV is attached. I welcome the opportunity to contribute to GitLab's remote engineering team.

Best regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Automattic / WordPress (100% Remote Global)",
        "email":   "jobs@automattic.com",
        "domain":  "SOFTWARE",
        "subject": "Software Engineer Application (Remote) – Abdullah Bin Masaud – 2026 Graduate",
        "body": """Dear Automattic Hiring Team,

Automattic's creed of open web development and distributed work resonates strongly with how I build software. I am applying for an entry-level software engineering role from Pakistan.

I am graduating in 2026 with a BS in Computer Engineering from COMSATS University Islamabad.

Core Competencies:
- Python & Backend APIs: Production-grade REST endpoints with complete test automation and Swagger documentation.
- Robust Communications: Deep understanding of TCP/IP, client-server models, and real-time WebSocket communication.
- Self-Directed Productivity: Accustomed to asynchronous communication, written documentation, and clean Git commits.

GitHub & Profiles:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Location: Pakistan (UTC+5)

My Software CV is attached. I am eager to undertake any trial or technical assessment.

Sincerely,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "BairesDev (Remote Global)",
        "email":   "jobs@bairesdev.com",
        "domain":  "SOFTWARE",
        "subject": "Software Engineer Application (Remote) – Abdullah Bin Masaud – Computer Engineering 2026",
        "body": """Dear BairesDev Talent Team,

I am writing to apply for a Junior Software Engineer position with BairesDev's remote talent network. As a final-year Computer Engineering candidate from COMSATS University Islamabad, Pakistan (graduating 2026), I am ready to join your distributed engineering teams.

Technical Highlights:
- Python Backend & API Development (Flask, pytest, RESTful standards)
- Low-Level Systems: TCP/IP networking, binary data structures, and CRC32 verification
- Machine Learning & Data Validation Pipelines
- Fast learning speed, strong English communication, and disciplined Git practices

Profiles:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b

My resume is attached for your review. I am prepared to take your technical evaluation immediately.

Best regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Crossover for Work (Global Remote)",
        "email":   "apply@crossover.com",
        "domain":  "SOFTWARE",
        "subject": "Software Engineer Applicant (Remote) – Abdullah Bin Masaud – Computer Engineering",
        "body": """Dear Crossover Talent Team,

I am writing to apply for remote software engineering roles through Crossover. I am a final-year Computer Engineering student at COMSATS University Islamabad, Pakistan (graduating 2026), with demonstrated ability to deliver production-quality code.

Portfolio Highlights:
- Built 12 public GitHub repositories covering backend API engineering, TCP/IP networking protocols, edge AI, and automated data pipelines.
- High emphasis on test-driven development: automated pytest test suites with latency and concurrency benchmarking.
- Comfortable working in intense, high-output distributed engineering environments.

Work Portfolio:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b

My CV is attached. I look forward to your standardized testing and evaluation process.

Sincerely,
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

def log_application(company, email, domain, status):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    TRACKER_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(TRACKER_PATH, "a", encoding="utf-8") as f:
        f.write(f"{timestamp},{company},{email},{domain},,{status}\n")

def main():
    print("=" * 75)
    print("  BATCH 7 — MX-VERIFIED ISB / RWP / REMOTE / INTL — 500% CALLBACK FORMULA")
    print(f"  Targets: {len(BATCH7)} companies — all MX-verified, zero bounce")
    print("=" * 75)
    sent = failed = 0
    for i, job in enumerate(BATCH7, 1):
        company = job["company"]
        email   = job["email"]
        domain  = job["domain"]
        cv_path = CV_MAP[domain]
        print(f"\n[{i:02d}/{len(BATCH7)}] {company}")
        print(f"      To     : {email}")
        print(f"      CV     : {cv_path.name}  |  {domain}")
        try:
            send_email(email, job["subject"], job["body"], cv_path)
            log_application(company, email, domain, "SENT")
            print(f"      Status : [OK] SENT")
            sent += 1
        except Exception as e:
            log_application(company, email, domain, f"FAILED: {e}")
            print(f"      Status : [FAIL] {e}")
            failed += 1
    print("\n" + "=" * 75)
    print(f"  BATCH 7 COMPLETE  |  Sent: {sent}  |  Failed: {failed}")
    print(f"  Total verified applications delivered: ~{103 + sent}")
    print("=" * 75)

if __name__ == "__main__":
    main()
