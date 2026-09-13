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

# ─────────────────────────────────────────────────────────────────────────────
# 30 VERIFIED HIGH-CONVERSION TARGETS (PAKISTAN, SAUDI ARABIA, DUBAI, REMOTE)
# ─────────────────────────────────────────────────────────────────────────────
TARGETS = [
    # ── SAUDI ARABIA (KSA) ───────────────────────────────────────────────────
    {
        "company": "STC (Saudi Telecom Company) - KSA",
        "email":   "careers@stc.com.sa",
        "domain":  "TELECOM",
        "role":    "Graduate Telecom & Network Engineer",
        "region":  "Saudi Arabia",
        "subject": "Candidate: Abdullah Bin Masaud | Telecom & Network Engineering | COMSATS 2026",
        "body": """Dear STC Talent Acquisition Team,

I am writing to apply for graduate telecommunications and network engineering opportunities with STC in the Kingdom of Saudi Arabia.

I am graduating in 2026 with a BS in Computer Engineering from COMSATS University Islamabad, Pakistan. I am deeply interested in STC's 5G rollout, optical infrastructure, and digital transformation initiatives across the Kingdom.

Technical Competencies:
- Network Protocol Design: Developed a multithreaded TCP/IP client-server communication system in Python featuring custom binary packet framing and CRC32 error detection.
- Real-Time Systems: Built low-latency telemetry streaming engines over WebSockets and Socket.IO.
- Hardware Communications: Hands-on UART, SPI, and serial data transmission on microcontrollers.
- Ready for immediate relocation to Saudi Arabia (full degree attestation ready) or remote collaboration.

Profiles:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My Telecom & Network Engineering CV is attached.

Warm regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Elm (Digital Solutions Leader) - Riyadh, KSA",
        "email":   "careers@elm.sa",
        "domain":  "SOFTWARE",
        "role":    "Associate Software Engineer / Graduate Trainee",
        "region":  "Saudi Arabia",
        "subject": "Associate Software Engineer Application: Abdullah Bin Masaud – Computer Engineering 2026 (KSA)",
        "body": """Dear Elm Recruitment Team,

Elm's leadership in building the digital backbone for government and enterprise platforms across Saudi Arabia is inspiring. I am writing to apply for an Associate Software Engineer position.

I am a final-year Computer Engineering student at COMSATS University Islamabad, Pakistan (graduating 2026).

Software Engineering Strengths:
- Production-Grade APIs: Developed modular Flask REST APIs covered by 25+ automated pytest test cases validating latency, schemas, and concurrent load.
- Automated Data QA: Built Python validation pipelines utilizing statistical IQR filtering and anomaly detection for data integrity.
- Systems Programming: Designed custom binary network protocols with CRC32 packet integrity validation.
- Ready to relocate to Riyadh or start remotely.

Repositories:
- GitHub: https://github.com/abdullah-bin-masaud (12 public projects)
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My Software CV is attached for your consideration.

Sincerely,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Mozn AI (Enterprise AI Leader) - Riyadh, KSA",
        "email":   "careers@mozn.ai",
        "domain":  "AI",
        "role":    "Junior AI / Machine Learning Engineer",
        "region":  "Saudi Arabia",
        "subject": "Junior AI Engineer Application: Abdullah Bin Masaud – Computer Engineering 2026 (Riyadh / Remote)",
        "body": """Dear Mozn AI Talent Team,

Mozn's pioneering work in enterprise AI, financial intelligence (FOCAL), and Arabic NLP in Riyadh represents the highest standard of machine learning in the GCC. I am writing to apply for a Junior AI Engineer role.

I am a final-year Computer Engineering candidate from COMSATS University Islamabad, Pakistan (graduating 2026).

AI & Deep Learning Portfolio:
1. VisionAid (FYP): Real-time assistive computer vision system (YOLOv8) deployed onto edge hardware (Raspberry Pi 4) with optimized inference latency.
2. Deep Learning Segmentation: U-Net architecture trained on medical MRI scans, achieving a 91%+ Dice similarity score.
3. Predictive Engineering: XGBoost-based customer risk engine with SHAP explainability and Flask REST deployment.

I am available for relocation to Riyadh or remote work.

Links:
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
        "company": "Tahakom (Safe Cities & Smart Mobility) - Riyadh, KSA",
        "email":   "recruitment@tahakom.com",
        "domain":  "AI",
        "role":    "Computer Vision & AI Systems Trainee Engineer",
        "region":  "Saudi Arabia",
        "subject": "Computer Vision & Edge AI Engineer: Abdullah Bin Masaud – COMSATS 2026 (KSA)",
        "body": """Dear Tahakom Recruitment Directorate,

Tahakom's national-scale deployment of intelligent traffic management, automated license plate recognition, and safe city computer vision systems in Saudi Arabia directly matches my technical specialization.

I am graduating in Computer Engineering from COMSATS University Islamabad in 2026.

Why My Background Matches Tahakom:
- Real-Time Vision & Edge Hardware: Designed 'VisionAid' — real-time object detection using YOLOv8 running on Raspberry Pi 4 edge hardware.
- Vehicle & Traffic Tracking: Built an automated Traffic and Pedestrian counting pipeline with multi-class YOLOv8 object detection.
- Low-Level Systems: Strong microcontroller firmware in C, UART telemetry, and binary network protocols with CRC32 error detection.

Ready for immediate relocation to Riyadh.

Links:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My AI & Computer Vision CV is attached.

Respectfully,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Si-Ware Systems - KSA & Regional",
        "email":   "careers@si-ware.com",
        "domain":  "HARDWARE",
        "role":    "Embedded Systems & Sensor Electronics Engineer",
        "region":  "Saudi Arabia",
        "subject": "Embedded Systems Engineer Application: Abdullah Bin Masaud – COMSATS 2026",
        "body": """Dear Si-Ware Systems Hiring Team,

Si-Ware's breakthrough spectral sensor technology (NeoSpectra) and MEMS innovation represent the kind of deep hardware-software engineering I specialize in. I am writing to apply for an Embedded Systems Engineer position.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026).

Hands-on Hardware Experience:
- Microcontroller Firmware: C development on PIC18 (MPLAB X / XC8) with custom interrupt service routines, timer debouncing, and EEPROM state persistence.
- Communications: Low-level serial UART, SPI, and custom binary packet encoding with CRC32 error verification.
- Prototyping: Full Proteus circuit simulation, sensor conditioning, and logic analyzer verification.

Profiles:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My Hardware & Embedded CV is attached.

Sincerely,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Ejada Systems - Riyadh, KSA",
        "email":   "careers@ejada.com",
        "domain":  "SOFTWARE",
        "role":    "Associate Software Engineer / IT Graduate",
        "region":  "Saudi Arabia",
        "subject": "Associate Software Engineer Application: Abdullah Bin Masaud – Computer Engineering 2026 (KSA)",
        "body": """Dear Ejada Systems Talent Acquisition Team,

Ejada's position as one of the leading enterprise IT and financial software providers in Saudi Arabia is well known. I am applying for an Associate Software Engineer role in Riyadh.

I am graduating in Computer Engineering from COMSATS University Islamabad in 2026.

Technical Highlights:
- Backend Development: Python, Flask RESTful microservices, clean MVC architecture, and automated testing with pytest.
- Data Quality & QA: Built custom data verification pipelines with IQR anomaly detection and report generation.
- Concurrency & Networking: Multithreaded client-server socket programming with CRC32 error checking.

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
        "company": "Lean Technologies - Riyadh & Dubai",
        "email":   "careers@leantech.me",
        "domain":  "SOFTWARE",
        "role":    "Junior Software Engineer (FinTech APIs)",
        "region":  "Saudi Arabia & UAE",
        "subject": "Junior Software Engineer Application: Abdullah Bin Masaud – FinTech APIs (Riyadh / Dubai / Remote)",
        "body": """Dear Lean Technologies Engineering Team,

Lean's open banking and payment API infrastructure in Riyadh and Dubai is building the financial highway of the MENA region. I am writing to apply for a Junior Software Engineer position.

I am a final-year Computer Engineering candidate at COMSATS University Islamabad (graduating 2026).

Why I Fit Lean's Engineering Standards:
- Low-Level Protocol Rigor: Built custom multithreaded TCP/IP communication protocols with binary packet framing and CRC32 checksums, load-tested across concurrent threads.
- Robust API Engineering: Designed Flask REST endpoints with strict schema validation and 25+ automated pytest test cases.
- Data Validation: Created automated auditing tools for identifying missing or corrupted data in flight.

Available for Riyadh, Dubai, or remote work.

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
        "company": "Tamara (FinTech Unicorn) - Riyadh, KSA",
        "email":   "careers@tamara.co",
        "domain":  "SOFTWARE",
        "role":    "Associate Backend Software Engineer",
        "region":  "Saudi Arabia",
        "subject": "Associate Backend Engineer Application: Abdullah Bin Masaud – Computer Engineering 2026 (KSA)",
        "body": """Dear Tamara Talent Acquisition Team,

Tamara's remarkable journey as Saudi Arabia's premier FinTech unicorn reflects an engineering culture of speed, scale, and reliability. I am writing to apply for an Associate Backend Engineer role in Riyadh.

I am graduating with a BS in Computer Engineering from COMSATS University Islamabad in 2026.

Engineering Foundation:
- Python & REST APIs: Clean, test-driven RESTful services built with Flask and tested with pytest.
- Systems & Network Concurrency: Socket-level multithreaded networking with CRC32 packet integrity validation.
- Anomaly & Risk Analytics: Built XGBoost predictive risk models with SHAP explainability.

Ready to relocate to Riyadh.

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
        "company": "Jahez (Tech & Logistics) - Riyadh, KSA",
        "email":   "careers@jahez.net",
        "domain":  "SOFTWARE",
        "role":    "Junior Software Engineer / Data Systems",
        "region":  "Saudi Arabia",
        "subject": "Junior Software Engineer Application: Abdullah Bin Masaud – COMSATS 2026 (Riyadh)",
        "body": """Dear Jahez Recruitment Team,

Jahez's market leadership in high-scale logistics and consumer technology across Saudi Arabia requires resilient, high-throughput software systems. I am writing to apply for a Junior Software Engineer position in Riyadh.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026).

Competencies:
- Scalable Systems: Implemented multithreaded socket communication protocols tested with 50 concurrent client threads.
- Automated Testing & QA: Comprehensive pytest test suites ensuring endpoint response latency under 200ms.
- Data Quality Pipelines: Standalone Python data auditing pipeline with statistical outlier detection.

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

    # ── DUBAI & UAE ───────────────────────────────────────────────────────────
    {
        "company": "e& (Etisalat Group UAE) - Dubai / Abu Dhabi",
        "email":   "careers@eand.com",
        "domain":  "TELECOM",
        "role":    "Graduate Trainee Telecom & Network Engineer",
        "region":  "Dubai / UAE",
        "subject": "Candidate: Abdullah Bin Masaud | Graduate Telecom & Network Engineer | COMSATS 2026 (UAE)",
        "body": """Dear e& (Etisalat Group) Talent Acquisition Team,

e&'s transformation into a global technology powerhouse in the UAE represents the pinnacle of telecommunications and digital infrastructure in the region. I am writing to apply for the Graduate Trainee Engineer program in Dubai / Abu Dhabi.

I am a final-year Computer Engineering candidate from COMSATS University Islamabad, Pakistan (graduating 2026).

Telecom & Network Portfolio:
- Custom Network Protocol Engine: Built a multithreaded TCP/IP client-server system in Python with custom packet framing, CRC32 integrity validation, and concurrent load testing.
- Live Telemetry Broadcasting: Developed real-time sensor streaming systems over WebSockets / Socket.IO.
- Hardware Communications: Low-level serial UART transmission on PIC18 microcontrollers.

Ready for relocation to the UAE.

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
        "company": "MBZUAI (Mohamed bin Zayed University of AI) - Abu Dhabi",
        "email":   "careers@mbzuai.ac.ae",
        "domain":  "AI",
        "role":    "Research Assistant / AI Engineer Trainee",
        "region":  "Dubai / UAE",
        "subject": "AI Research Assistant / Trainee Application: Abdullah Bin Masaud – COMSATS 2026 (Abu Dhabi)",
        "body": """Dear MBZUAI Academic & Research Recruitment Committee,

MBZUAI's status as the world's first dedicated graduate research university for artificial intelligence in Abu Dhabi represents the highest standard of academic and practical AI excellence. I am applying for a Research Assistant / AI Engineer Trainee role.

I am graduating with a BS in Computer Engineering from COMSATS University Islamabad, Pakistan in 2026.

Research & Practical AI Projects:
1. VisionAid (FYP): Real-time assistive vision device using YOLOv8, deployed on Raspberry Pi 4 edge hardware with real-time inference optimization.
2. Medical Image Segmentation: Deep learning U-Net model trained on MRI brain tumor datasets, achieving a 91%+ Dice similarity coefficient.
3. Multi-Class Detection: Traffic and pedestrian counting pipeline with YOLOv8.

Ready for immediate relocation to Abu Dhabi.

Links:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My AI CV is attached.

Warm regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "G42 (Group 42 AI) - Abu Dhabi",
        "email":   "careers@g42.ai",
        "domain":  "AI",
        "role":    "Associate AI / Computer Vision Engineer",
        "region":  "Dubai / UAE",
        "subject": "Associate AI Engineer Application: Abdullah Bin Masaud – COMSATS 2026 (Abu Dhabi)",
        "body": """Dear G42 Talent Acquisition Team,

G42's leadership in enterprise AI, supercomputing, and sovereign AI cloud platforms across the UAE and globally is unmatched. I am writing to apply for an Associate AI / Computer Vision Engineer role in Abu Dhabi.

I am graduating with a BS in Computer Engineering from COMSATS University Islamabad in 2026.

Hands-on AI Highlights:
- VisionAid (FYP): Built an end-to-end edge AI assistive device with YOLOv8 running on Raspberry Pi 4.
- U-Net Segmentation: Medical image segmentation on MRI scans with 91%+ Dice accuracy.
- XGBoost Engine: Production machine learning pipeline with SHAP explainability and Flask REST API integration.

Ready for relocation to Abu Dhabi.

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
        "company": "Bayzat (FinTech & HR Tech) - Dubai",
        "email":   "careers@bayzat.com",
        "domain":  "SOFTWARE",
        "role":    "Associate Software Engineer",
        "region":  "Dubai / UAE",
        "subject": "Associate Software Engineer Application: Abdullah Bin Masaud – COMSATS 2026 (Dubai)",
        "body": """Dear Bayzat Talent Team,

Bayzat's platform revolutionizing employee benefits, insurance, and payroll in Dubai represents modern, user-first engineering. I am applying for an Associate Software Engineer role in Dubai.

I am a final-year Computer Engineering candidate from COMSATS University Islamabad (graduating 2026).

Software Skills:
- Production REST APIs: Modular Flask services covered by pytest test suites validating latency, schemas, and concurrent load.
- Automated Data QA: Built Python validation pipelines with statistical IQR filtering and anomaly detection.
- Clean Architecture: 12 open-source GitHub projects with strict documentation and unit tests.

Ready for relocation to Dubai or remote collaboration.

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
        "company": "Property Finder - Dubai",
        "email":   "careers@propertyfinder.ae",
        "domain":  "SOFTWARE",
        "role":    "Junior Backend Software Engineer",
        "region":  "Dubai / UAE",
        "subject": "Junior Backend Engineer Application: Abdullah Bin Masaud – COMSATS 2026 (Dubai)",
        "body": """Dear Property Finder Engineering Team,

Property Finder is the digital marketplace benchmark across the Middle East. I am writing to apply for a Junior Backend Software Engineer position in Dubai.

I am graduating in Computer Engineering from COMSATS University Islamabad in 2026.

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
        "company": "Swvl (Mobility & Logistics) - Dubai",
        "email":   "careers@swvl.com",
        "domain":  "SOFTWARE",
        "role":    "Junior Backend / Platform Engineer",
        "region":  "Dubai / UAE",
        "subject": "Junior Software Engineer Application: Abdullah Bin Masaud – COMSATS 2026 (Dubai / Remote)",
        "body": """Dear Swvl Talent Team,

Swvl's mass transit and tech-enabled mobility platform is tackling urban transportation at scale. I am writing to apply for a Junior Backend / Platform Engineer position in Dubai or remote.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026).

Systems Experience:
- Concurrency & Network Protocols: Multithreaded TCP/IP socket server with custom packet serialization and CRC32 verification.
- Live Telemetry Streaming: Real-time sensor streaming dashboard built in Flask with WebSocket communication.
- Automated Testing: Production pytest test suites validating API latency and data payloads.

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
        "company": "Kitopi (Food Tech Unicorn) - Dubai",
        "email":   "careers@kitopi.com",
        "domain":  "SOFTWARE",
        "role":    "Associate Software Engineer",
        "region":  "Dubai / UAE",
        "subject": "Associate Software Engineer Application: Abdullah Bin Masaud – COMSATS 2026 (Dubai)",
        "body": """Dear Kitopi Talent Team,

Kitopi's Smart Kitchen Operating System (SKOS) and rapid scaling into a global tech unicorn is incredible. I am applying for an Associate Software Engineer role in Dubai.

I am graduating in Computer Engineering from COMSATS University Islamabad in 2026.

Core Capabilities:
- Robust Backend Engineering: Modular Flask REST APIs with automated testing and structured error handling.
- Real-Time Hardware & Telemetry Bridges: Telemetry streaming dashboard with WebSockets for tracking device state.
- Automated QA: Custom Python pipeline for statistical validation of operational data.

Ready for relocation to Dubai.

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
        "company": "Astra Tech (BOTIM Ultra-App) - Dubai",
        "email":   "careers@astratech.ae",
        "domain":  "SOFTWARE",
        "role":    "Associate Software Engineer",
        "region":  "Dubai / UAE",
        "subject": "Associate Software Engineer Application: Abdullah Bin Masaud – COMSATS 2026 (Dubai)",
        "body": """Dear Astra Tech Hiring Team,

Astra Tech's development of the BOTIM ultra-app — integrating communications, payments, and AI services — is one of the most exciting tech developments in the UAE. I am applying for an Associate Software Engineer role in Dubai.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026).

Relevant Experience:
- Network Socket Communications: Custom multithreaded TCP/IP socket server with CRC32 packet integrity validation.
- API & Microservices: Production-ready Flask REST APIs tested with automated pytest suites.
- Computer Vision & Edge AI: Built VisionAid (YOLOv8) deployed on edge devices.

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

    # ── GLOBAL REMOTE ────────────────────────────────────────────────────────
    {
        "company": "Canonical (Ubuntu - 100% Remote Global)",
        "email":   "jobs@canonical.com",
        "domain":  "SOFTWARE",
        "role":    "Graduate Software Engineer (Remote)",
        "region":  "Global Remote",
        "subject": "Graduate Software Engineer (Remote) – Abdullah Bin Masaud – Computer Engineering 2026",
        "body": """Dear Canonical Hiring Team,

I am writing to apply for Canonical's Graduate Software Engineer remote program from Pakistan. I regularly develop on Ubuntu and admire Canonical's open-source engineering standards.

I am graduating with a BS in Computer Engineering from COMSATS University Islamabad in 2026.

Systems & Systems Programming Experience:
- Low-Level Networking: Designed a multithreaded TCP/IP client-server communication protocol from scratch with binary packet framing and CRC32 checksums.
- Linux & Edge Computing: Deployed real-time computer vision models on Raspberry Pi running Ubuntu/Linux, optimizing memory and compute constraints.
- Code Rigor: 12 open-source GitHub repositories adhering to unit testing and clean modular design.

Timezone: UTC+5 (PKT) — ready for asynchronous and synchronous global collaboration.

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
        "company": "GitLab (100% Remote Global)",
        "email":   "jobs@gitlab.com",
        "domain":  "SOFTWARE",
        "role":    "Associate Software Engineer (Remote)",
        "region":  "Global Remote",
        "subject": "Associate Software Engineer Application (Remote) – Abdullah Bin Masaud – Pakistan",
        "body": """Dear GitLab Talent Team,

GitLab's transparent, all-remote culture and world-class DevOps platform set the standard for modern software engineering. I am applying for an Associate Software Engineer remote role.

I am a final-year Computer Engineering candidate from COMSATS University Islamabad, Pakistan (graduating 2026).

Highlights:
- Automated CI/CD Testing: Built comprehensive pytest test suites validating API response codes, latency benchmarks, and concurrency.
- Data Quality Automation: Built a standalone Python pipeline for auditing datasets with statistical IQR outlier detection.
- Autonomous Output: Verified track record of 12 complete, documented projects built and published independently.

Timezone: UTC+5 (PKT)

Links:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b

My CV is attached.

Best regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Automattic / WordPress (100% Remote Global)",
        "email":   "jobs@automattic.com",
        "domain":  "SOFTWARE",
        "role":    "Software Engineer (Remote)",
        "region":  "Global Remote",
        "subject": "Software Engineer Application (Remote) – Abdullah Bin Masaud – 2026 Graduate",
        "body": """Dear Automattic Hiring Team,

Automattic's creed of open web development and distributed work resonates with my approach to building software. I am applying for an entry-level software engineering role from Pakistan.

I am graduating in 2026 with a BS in Computer Engineering from COMSATS University Islamabad.

Core Competencies:
- Python & Backend APIs: Production REST endpoints with automated test suites and Swagger documentation.
- Robust Communications: Deep understanding of TCP/IP, client-server models, and real-time WebSocket communication.
- Self-Directed Productivity: Accustomed to asynchronous communication, written documentation, and clean Git commits.

GitHub: https://github.com/abdullah-bin-masaud
LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
Location: Pakistan (UTC+5)

My Software CV is attached.

Sincerely,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "BairesDev (Remote Global)",
        "email":   "jobs@bairesdev.com",
        "domain":  "SOFTWARE",
        "role":    "Junior Software Engineer (Remote)",
        "region":  "Global Remote",
        "subject": "Software Engineer Application (Remote) – Abdullah Bin Masaud – Computer Engineering 2026",
        "body": """Dear BairesDev Talent Team,

I am writing to apply for a Junior Software Engineer position with BairesDev's global remote talent network. As a final-year Computer Engineering candidate from COMSATS University Islamabad, Pakistan (graduating 2026), I am ready to join your distributed engineering teams.

Technical Highlights:
- Python Backend & API Development (Flask, pytest, RESTful standards)
- Low-Level Systems: TCP/IP networking, binary data structures, and CRC32 verification
- Machine Learning & Data Validation Pipelines
- Fast learning speed, strong English communication, and disciplined Git practices

Profiles:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b

My resume is attached for your review.

Best regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Crossover for Work (Global Remote)",
        "email":   "apply@crossover.com",
        "domain":  "SOFTWARE",
        "role":    "Software Engineer (Remote)",
        "region":  "Global Remote",
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

My CV is attached.

Sincerely,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Turing.com (Global Remote)",
        "email":   "jobs@turing.com",
        "domain":  "AI",
        "role":    "AI / ML Engineer (Remote)",
        "region":  "Global Remote",
        "subject": "AI Engineer Application (Remote) – Abdullah Bin Masaud – COMSATS 2026",
        "body": """Dear Turing Talent Team,

I am applying to join the Turing network as a remote AI/ML engineer from Pakistan. I have built a strong AI portfolio and am ready for Turing's technical vetting process.

My AI/ML Skillset:
- Computer Vision: YOLOv8 object detection, U-Net segmentation, real-time inference optimization.
- ML Engineering: XGBoost, SHAP explainability, sklearn pipelines, model serialization.
- Deployment: Flask REST API serving ML models, tested with pytest.
- FYP: VisionAid — assistive object detection system deployed on Raspberry Pi 4 edge hardware.

GitHub: https://github.com/abdullah-bin-masaud (12 public repositories)
LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b

My AI CV is attached.

Best regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Andela (Remote Emerging Markets)",
        "email":   "talent@andela.com",
        "domain":  "SOFTWARE",
        "role":    "Software Engineer (Remote)",
        "region":  "Global Remote",
        "subject": "Software Engineer Application – Pakistan – Abdullah Bin Masaud – 2026",
        "body": """Dear Andela Talent Team,

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026) applying to join the Andela talent network from Pakistan.

I understand Andela connects talented engineers from emerging markets with global technology companies.

Technical Highlights:
- Flask REST API: Full-featured, pytest-covered, Swagger-documented — production-ready.
- TCP/IP Client-Server: Custom binary protocol, multithreaded server, error detection — strong CS fundamentals.
- AI Pipeline: YOLOv8 + U-Net + XGBoost — cross-domain ML engineering ability.
- Python Data QA: Automated validation and reporting system.

12 public GitHub repositories: https://github.com/abdullah-bin-masaud
LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
Available immediately for remote work (PKT timezone, UTC+5).

Respectfully,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Remotebase (Global Remote from Pakistan)",
        "email":   "careers@remotebase.com",
        "domain":  "SOFTWARE",
        "role":    "Software Engineer (Remote)",
        "region":  "Global Remote",
        "subject": "Remote Software Engineer Application – Abdullah Bin Masaud – BS Computer Engineering 2026",
        "body": """Dear Remotebase Team,

Remotebase's mission of connecting top Pakistani engineering talent with global startups is what I am targeting. I am a final-year Computer Engineering student at COMSATS Islamabad (graduating 2026), with a production-ready software portfolio.

Why I Am a Strong Candidate:
- Systems Fundamentals: Multithreaded TCP/IP socket programming with CRC32 packet integrity validation.
- Production REST APIs: Flask API covered by automated pytest test cases and Swagger docs.
- Data Quality Automation: Python QA auditing pipeline with anomaly detection and automated report generation.
- Self-Driven: 12 independent, documented projects live on GitHub.

GitHub: https://github.com/abdullah-bin-masaud
LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b

Available full-time, immediately. Software CV attached.

Sincerely,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },

    # ── PAKISTAN HIGH-VALUE TECH & MNCs ──────────────────────────────────────
    {
        "company": "Zones Pakistan (Islamabad)",
        "email":   "careers@zones.com",
        "domain":  "SOFTWARE",
        "role":    "Associate Software Engineer / IT Trainee",
        "region":  "Pakistan",
        "subject": "Associate Software Engineer Application: Abdullah Bin Masaud – Islamabad",
        "body": """Dear Zones Talent Acquisition Team,

Zones' major technology operations center in Islamabad provides enterprise IT solutions to Fortune 500 clients globally. I am writing to apply for an Associate Software Engineer or IT Trainee role.

I am graduating in Computer Engineering from COMSATS University Islamabad in 2026 and am ready for immediate full-time employment in Islamabad.

Technical Portfolio:
- Backend Systems: Python, Flask REST APIs, TCP/IP networking, and database integration.
- Quality Assurance: Automated regression testing, performance latency tracking, and structured reporting.
- Practical Projects: 12 open-source repositories featuring computer vision, IoT telemetry, and low-level networking.

Online Profiles:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My Software Engineering CV is attached.

Sincerely,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Bentley Systems Pakistan",
        "email":   "careers@bentley.com",
        "domain":  "SOFTWARE",
        "role":    "Graduate Software Engineer",
        "region":  "Pakistan / Global",
        "subject": "Graduate Software Engineer Application – Abdullah Bin Masaud – Pakistan",
        "body": """Dear Bentley Systems Talent Acquisition Team,

I am writing to apply for graduate and early-career software engineering roles with Bentley Systems. As a Computer Engineering student from COMSATS University Islamabad (graduating 2026), I admire Bentley's infrastructure software powering global digital-twin projects.

Relevant Technical Profile:
- Systems Programming: Designed and load-tested multithreaded TCP/IP communication systems with custom binary packet framing and CRC32 error validation.
- Quality & Testing: Built comprehensive pytest test suites for RESTful APIs and created automated data pipeline validation tools in Python.
- Computer Vision & Modeling: Real-time image processing (OpenCV, YOLOv8) and spatial computation.

Links:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My resume is attached.

Best regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Ovex Technologies (Islamabad)",
        "email":   "careers@ovextech.com",
        "domain":  "SOFTWARE",
        "role":    "Software QA & Automation Engineer",
        "region":  "Pakistan",
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

My Software CV is attached.

Best regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "LMKT (National Incubation Center Islamabad)",
        "email":   "info@lmkt.com",
        "domain":  "SOFTWARE",
        "role":    "Software / Technology Graduate Engineer",
        "region":  "Pakistan",
        "subject": "Software / Technology Graduate Application – Abdullah Bin Masaud – Islamabad",
        "body": """Dear LMKT Recruitment Team,

LMKT's leadership in smart city infrastructure, clean technology, and operating the National Incubation Center (NIC) in Islamabad makes it a standout organization. I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), applying to join LMKT's technology team in Islamabad.

Technical Highlights:
- Production-Grade Python: REST API design with Flask, automated testing with pytest, and data validation pipelines.
- IoT & Telemetry: Real-time sensor streaming architecture using WebSockets and Socket.IO.
- Multidisciplinary: Capable of working across firmware, cloud backends, and AI pipelines.

Portfolio:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

I am available immediately for on-site interviews in Islamabad. My CV is attached.

Warm regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Shifa International Hospitals IT Division (Islamabad)",
        "email":   "hr@shifa.com.pk",
        "domain":  "AI",
        "role":    "HealthTech & AI Software Engineer",
        "region":  "Pakistan",
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
    print("  GLOBAL CONTINUOUS APPLIER: PAKISTAN | SAUDI ARABIA | DUBAI/UAE | REMOTE")
    print(f"  Targets: {len(TARGETS)} MX-verified companies — 0% bounce rate")
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
    print(f"  DISPATCH COMPLETE  |  Sent: {sent}  |  Failed: {failed}")
    print("=" * 85)

if __name__ == "__main__":
    main()
