import smtplib, ssl, datetime, subprocess, time
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
# 30 FRESH PAKISTAN IT OPPORTUNITIES (IT, CS, AI, SE, CE, EE, TELECOM)
# ALL 100% MX-VERIFIED & NOT YET IN TRACKER
# ─────────────────────────────────────────────────────────────────────────────
TARGETS = [
    # ── 1. Contour Software ──
    {
        "company": "Contour Software (Constellation Software Pakistan)",
        "email":   "careers@contour-software.com",
        "domain":  "SOFTWARE",
        "discipline": "SE / CS / SQA",
        "role":    "Associate Software Engineer / SQA Trainee",
        "subject": "Associate Software Engineer Application: Abdullah Bin Masaud – Computer Engineering (COMSATS 2026)",
        "body": """Dear Contour Software Recruitment Team,

Contour Software's standing as Constellation Software's delivery center in Pakistan — building mission-critical vertical market software across finance, healthcare, and enterprise systems — demands rigorous engineering discipline.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026) with deep practical experience in software architecture, test automation, and low-level systems.

Direct Project Proof:
1. Production REST APIs: Developed modular Flask REST services with JWT authentication, structured CRUD endpoints, and 25+ automated pytest test cases validating HTTP status codes, latency benchmarks (<200ms), and payload validation.
2. Automated Data QA Pipeline: Built an end-to-end Python data auditing engine featuring statistical IQR outlier detection, missing-value assertions, and automated JSON/Markdown test reporting.
3. Network Protocols & Concurrency: Built a multithreaded TCP/IP client-server protocol from scratch with binary packet framing and CRC32 checksum error detection, load-tested against 50 concurrent client connections.
4. Computer Vision (FYP): Built VisionAid, deploying YOLOv8 object detection on Raspberry Pi 4 edge hardware for real-time assistive guidance.

I am immediately available and open to on-site roles in Lahore, Islamabad, or hybrid setups.

Portfolio:
- GitHub: https://github.com/abdullah-bin-masaud (12 public repositories)
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Mobile: +92 332 9076356

My Software Engineering CV is attached. I welcome any coding assessment or technical interview.

Sincerely,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },

    # ── 2. 10Pearls ──
    {
        "company": "10Pearls Pakistan (Islamabad / Lahore / Karachi)",
        "email":   "info@10pearls.com",
        "domain":  "AI",
        "discipline": "AI / SE / CS",
        "role":    "Junior AI & Software Engineer",
        "subject": "Junior AI & Software Engineer Application: Abdullah Bin Masaud | COMSATS 2026",
        "body": """Dear 10Pearls Talent Acquisition Team,

10Pearls' leadership in building innovative digital products, AI transformation platforms, and cloud solutions makes it an organization where my skills in computer vision and full-stack software development can create immediate value.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026) with demonstrable open-source projects across artificial intelligence, edge computing, and backend development.

Technical Highlights:
- VisionAid (FYP): Designed and deployed a real-time assistive guidance system using YOLOv8 running on Raspberry Pi 4 edge hardware with optimized inference latency and audio cues.
- Deep Learning & Medical Imaging: Trained a U-Net convolutional neural network on medical MRI scans, achieving a 91%+ Dice similarity score for brain tumor segmentation.
- Production ML Pipeline: Engineered an XGBoost predictive engine with SHAP explainability, deployed as a containerized Flask REST API.
- Live Video Streaming Dashboard: Built an interactive telemetry and video streaming platform using Flask, WebSockets (Socket.IO), and OpenCV.

I am available immediately and open to joining your Islamabad, Lahore, or Karachi development hubs.

Profiles:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My AI & Software CV is attached.

Best regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },

    # ── 3. Cowlar Design Studio ──
    {
        "company": "Cowlar Design Studio (Islamabad / Lahore)",
        "email":   "careers@cowlar.com",
        "domain":  "HARDWARE",
        "discipline": "CE / EE / IoT",
        "role":    "Embedded Systems & IoT Hardware Engineer",
        "subject": "Embedded Firmware & IoT Engineer: Abdullah Bin Masaud – COMSATS 2026 (Islamabad)",
        "body": """Dear Cowlar Engineering Team,

Cowlar's pioneering work in IoT connected hardware, smart sensors, and edge-intelligence products represents the exact intersection of embedded systems, circuit design, and edge computing that I specialize in.

I am graduating in Computer Engineering from COMSATS University Islamabad in 2026, located in the Islamabad region and available immediately.

Hands-on Hardware & Firmware Capabilities:
1. Microcontroller Firmware: Written register-level C code for PIC18F4550 using MPLAB X and XC8. Implemented interrupt service routines (ISRs), hardware debouncing, UART telemetry, SPI, I2C, and EEPROM state persistence.
2. Edge AI Deployment: Deployed YOLOv8 real-time object detection models directly onto Raspberry Pi 4 edge hardware (VisionAid FYP), handling camera pipeline and hardware compute limits.
3. Real-Time Telemetry Bridges: Developed live telemetry systems streaming real-time sensor measurements over WebSockets to interactive browser dashboards.
4. Circuit Validation: Complete component-level schematic design and circuit simulation in Proteus prior to hardware fabrication.

I am enthusiastic about Cowlar's IoT mission and would be thrilled to attend a technical interview at your office.

GitHub: https://github.com/abdullah-bin-masaud
LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
Phone: +92 332 9076356

My Embedded Systems & Hardware CV is attached.

Warm regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },

    # ── 4. Systems Limited ──
    {
        "company": "Systems Limited (Lahore / Islamabad / Karachi)",
        "email":   "careers@systemsltd.com",
        "domain":  "SOFTWARE",
        "discipline": "SE / CS / IT",
        "role":    "Trainee Software Engineer / Associate Consultant",
        "subject": "Trainee Software Engineer Application: Abdullah Bin Masaud – COMSATS 2026 (CE Graduate)",
        "body": """Dear Systems Limited Graduate Recruitment Directorate,

As Pakistan's premier global technology innovator and digital consultancy, Systems Limited provides the ideal environment for high-performing engineering graduates who value clean code, scalable architecture, and continuous learning.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026) with a track record of practical software systems engineering.

Why My Foundation Aligns with Systems Limited:
- Backend Architecture: Built modular Flask REST APIs featuring JWT authentication, comprehensive input validation, and 25+ automated pytest unit and integration test cases.
- Data Quality & Engineering: Created an automated Python data auditing tool featuring statistical IQR outlier filtering, schema assertions, and JSON/Markdown reporting.
- Systems Concurrency: Designed a multithreaded TCP/IP socket server with binary packet framing and CRC32 checksum error validation, load-tested against 50 concurrent client connections.
- Edge AI & Computer Vision: Built VisionAid on Raspberry Pi 4 edge hardware (YOLOv8) and a Traffic Counter REST API.

I am available immediately and open to joining in Lahore, Islamabad, or Karachi.

Links:
- GitHub: https://github.com/abdullah-bin-masaud (12 public repositories)
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My Software Engineering CV is attached.

Respectfully,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },

    # ── 5. SadaPay ──
    {
        "company": "SadaPay (Islamabad HQ)",
        "email":   "careers@sadapay.pk",
        "domain":  "SOFTWARE",
        "discipline": "SE / CS / Fintech",
        "role":    "Junior Software Engineer — Backend / Core Systems",
        "subject": "Junior Backend Engineer Application: Abdullah Bin Masaud – COMSATS 2026 (Islamabad)",
        "body": """Dear SadaPay Engineering Team,

SadaPay's user-first financial platform and modern engineering culture are reshaping Pakistan's banking sector. I am applying for a Junior Software Engineer (Backend / Core Systems) role at your Islamabad HQ.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), based in the Islamabad area and immediately available.

Relevant Engineering Experience:
1. Resilient API Design: Built Flask REST APIs with JWT authentication, transactional integrity, 25+ pytest test cases covering edge cases, and response latency benchmarking (<200ms).
2. Wire-Level Systems Understanding: Built a multithreaded TCP/IP socket protocol with binary packet framing and CRC32 checksums, validating data integrity across concurrent client streams.
3. Data Anomaly Detection: Developed a standalone Python data validation engine using statistical IQR anomaly detection — the exact discipline required for transaction auditing.
4. Predictive ML: Built an XGBoost customer churn model with SHAP explainability and Flask REST API deployment.

I would welcome the opportunity to complete any coding evaluation or technical assessment.

GitHub: https://github.com/abdullah-bin-masaud
LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
Phone: +92 332 9076356

My Software Engineering CV is attached.

Sincerely,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },

    # ── 6. Abhi FinTech ──
    {
        "company": "Abhi (FinTech — Financial Wellness Platform)",
        "email":   "careers@abhi.com.pk",
        "domain":  "SOFTWARE",
        "discipline": "SE / CS / Fintech",
        "role":    "Junior Software Engineer",
        "subject": "Junior Software Engineer Application: Abdullah Bin Masaud – COMSATS 2026 (Fintech / Backend)",
        "body": """Dear Abhi Engineering Leadership,

Abhi's pioneering earned wage access and credit underwriting infrastructure are creating profound financial empowerment across Pakistan. I am writing to apply for a Junior Software Engineer position.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), available immediately.

Technical Qualifications:
- Backend Systems: Built modular Flask REST APIs with JWT authentication, role-based access control, Swagger documentation, and automated pytest suites.
- Data Quality & Risk Modeling: Developed an XGBoost predictive model with SHAP feature explainability, and created automated Python data quality pipelines utilizing IQR statistical anomaly detection.
- Scalable Concurrency: Engineered a custom multithreaded TCP/IP socket server with binary packet framing and CRC32 error validation, stress-tested with 50 simultaneous clients.
- Full Availability: Can onboard immediately for Islamabad or remote roles.

Portfolio:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My Software CV is attached.

Best regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },

    # ── 7. Mettis Global ──
    {
        "company": "Mettis Global (Islamabad — Capital Markets & FinTech)",
        "email":   "info@mettisglobal.com",
        "domain":  "SOFTWARE",
        "discipline": "SE / CS / Data",
        "role":    "Junior Software / Financial Data Engineer",
        "subject": "Software Engineer Application: Abdullah Bin Masaud – Data & Systems | COMSATS 2026 (Islamabad)",
        "body": """Dear Mettis Global Technology Team,

Mettis Global's authoritative market intelligence and real-time financial data feeds require software built with absolute precision, high throughput, and data integrity.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), located in the Islamabad region and ready to start immediately.

Why My Background Fits Mettis Global:
- Financial Data QA Pipeline: Built an automated Python data validation tool implementing statistical IQR outlier detection, schema type validation, and automated report generation.
- Predictive Modeling: Implemented an XGBoost machine learning engine with SHAP feature importance analysis and REST API deployment.
- High-Performance Networking: Built a multithreaded TCP/IP binary communication system with CRC32 packet integrity validation.
- Real-Time Streaming: Built a live telemetry streaming dashboard using Flask and Socket.IO for low-latency metric broadcasting.

Available immediately in Islamabad.

GitHub: https://github.com/abdullah-bin-masaud
LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
Phone: +92 332 9076356

My Software Engineering CV is attached.

Warm regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },

    # ── 8. Inbox Business Technologies ──
    {
        "company": "Inbox Business Technologies (Karachi / Islamabad)",
        "email":   "hr@inboxbiz.com",
        "domain":  "SOFTWARE",
        "discipline": "SE / IT / Networks",
        "role":    "Associate Systems / Software Engineer",
        "subject": "Associate Software Engineer Application: Abdullah Bin Masaud – COMSATS 2026",
        "body": """Dear Inbox Business Technologies HR Team,

Inbox Business Technologies' position as a major provider of enterprise IT infrastructure, managed services, and mission-critical networks across Pakistan aligns directly with my computer engineering training.

I am graduating in Computer Engineering from COMSATS University Islamabad in 2026, with an engineering skillset covering backend software, computer networks, and embedded systems.

Engineering Highlights:
- Low-Level Networking: Developed a multithreaded TCP/IP client-server protocol with custom binary packet framing and CRC32 checksum error detection, validated with 50 concurrent client connections.
- Backend APIs: Built modular Flask REST APIs with JWT authentication, CRUD operations, 25+ pytest test cases, and Swagger API documentation.
- Automated Auditing: Built an automated Python data auditing tool featuring statistical outlier detection (IQR) and anomaly logging.
- Embedded & Telecom: Written register-level C firmware for microcontrollers and configured UART serial communication protocols.

Available immediately across Pakistan.

GitHub: https://github.com/abdullah-bin-masaud
LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
Phone: +92 332 9076356

My Software CV is attached.

Sincerely,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },

    # ── 9. Genetech Solutions ──
    {
        "company": "Genetech Solutions (Karachi)",
        "email":   "hr@genetechsolutions.com",
        "domain":  "SOFTWARE",
        "discipline": "SE / IT / Web",
        "role":    "Junior Software Engineer",
        "subject": "Junior Software Engineer Application: Abdullah Bin Masaud – COMSATS 2026",
        "body": """Dear Genetech Solutions Recruitment Team,

Genetech Solutions' sustained track record of delivering enterprise-grade digital platforms and custom software for international and local clients represents the kind of disciplined engineering environment I seek.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), open to both on-site roles in Karachi and remote engineering positions.

Relevant Engineering Work:
- Modular Backend Development: Built Flask REST APIs with JWT authentication, clean error handling, Swagger documentation, and automated pytest test suites (25+ tests).
- Automated Data Validation: Implemented a Python QA auditing tool featuring statistical IQR outlier detection and anomaly reporting.
- Systems Concurrency: Designed a multithreaded TCP/IP socket server with binary packet framing and CRC32 checksum verification.
- Computer Vision: Built YOLOv8 edge deployment on Raspberry Pi 4 (VisionAid FYP).

GitHub: https://github.com/abdullah-bin-masaud
LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
Phone: +92 332 9076356

My Software CV is attached.

Best regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },

    # ── 10. Creative Chaos ──
    {
        "company": "Creative Chaos (Karachi / US — Product Engineering)",
        "email":   "hr@creativechaos.com",
        "domain":  "SOFTWARE",
        "discipline": "SE / AI / Product",
        "role":    "Junior Software / AI Engineer",
        "subject": "Junior Software Engineer Application: Abdullah Bin Masaud – COMSATS 2026 (Backend & AI)",
        "body": """Dear Creative Chaos Talent Acquisition Team,

Creative Chaos' reputation for building globally acclaimed digital products across fintech, healthcare, and enterprise tech requires developers who combine clean engineering with product intuition.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), available immediately for remote or on-site work.

Public GitHub Highlights:
1. VisionAid (FYP): Built a real-time assistive guidance system using YOLOv8 deployed on Raspberry Pi 4 edge hardware with audio feedback cues.
2. Medical AI Segmentation: Trained U-Net convolutional neural network on MRI scans, achieving 91%+ Dice similarity score.
3. Backend Architecture: Flask REST API with JWT authentication, full CRUD, 25+ pytest test cases, and Swagger documentation.
4. Predictive ML: Production XGBoost customer churn engine with SHAP explainability.

I welcome any coding challenge or technical interview.

GitHub: https://github.com/abdullah-bin-masaud
LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
Phone: +92 332 9076356

My Software & AI CV is attached.

Warm regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },

    # ── 11. TRG Pakistan ──
    {
        "company": "TRG Pakistan (The Resource Group)",
        "email":   "hr@trg.com.pk",
        "domain":  "SOFTWARE",
        "discipline": "SE / CS / Analytics",
        "role":    "Junior Software / Analytics Engineer",
        "subject": "Software Engineer Application: Abdullah Bin Masaud – Analytics & Backend | COMSATS 2026",
        "body": """Dear TRG Pakistan HR Team,

TRG's pioneering enterprise technology and customer experience platforms operating on a global scale make it one of Pakistan's most significant tech groups. I am applying for a Junior Software / Analytics Engineer position.

I am graduating in Computer Engineering from COMSATS University Islamabad in 2026.

Key Competencies:
- Analytics & ML Engineering: Built an XGBoost predictive engine with SHAP feature explainability, deployed via Flask REST API.
- Automated QA & Auditing: Designed a Python data auditing engine utilizing statistical IQR outlier detection and automated report generation.
- Backend Architecture: Built modular Flask services with JWT authentication and 25+ automated pytest test cases validating latency and schema compliance.
- Network Concurrency: Multithreaded TCP/IP socket server with binary packet framing and CRC32 error detection.

Available immediately and open to Karachi or remote positions.

GitHub: https://github.com/abdullah-bin-masaud
LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
Phone: +92 332 9076356

My Software CV is attached.

Sincerely,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },

    # ── 12. NetSol Technologies ──
    {
        "company": "NetSol Technologies (Lahore HQ)",
        "email":   "hr@netsoltech.com",
        "domain":  "SOFTWARE",
        "discipline": "SE / CS / Enterprise",
        "role":    "Graduate Trainee Software Engineer",
        "subject": "Graduate Trainee Software Engineer Application: Abdullah Bin Masaud – COMSATS 2026",
        "body": """Dear NetSol Technologies Graduate Recruitment Team,

NetSol's leadership as Pakistan's pioneer in global enterprise finance and asset leasing software platforms represents a benchmark in software engineering reliability. I am writing to apply for the Graduate Trainee Software Engineer program.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026).

Why I Am Prepared for NetSol's Standards:
- Production Backend Systems: Built modular Flask REST APIs with JWT authentication, comprehensive input validation, and 25+ automated pytest unit and integration test cases.
- Data Integrity & Validation: Developed an automated Python data auditing tool featuring statistical outlier detection (IQR) and automated anomaly reporting.
- Network Protocols: Designed a multithreaded TCP/IP socket server with binary packet framing and CRC32 checksum error detection, validated with 50 concurrent client connections.
- Clean Architecture: 12 open-source GitHub repositories following clean code standards and comprehensive documentation.

Available for on-site work in Lahore, Islamabad, or remote.

GitHub: https://github.com/abdullah-bin-masaud
LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
Phone: +92 332 9076356

My Software Engineering CV is attached.

Respectfully,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },

    # ── 13. Tintash ──
    {
        "company": "Tintash (Lahore / Remote — Product Engineering Studio)",
        "email":   "hr@tintash.com",
        "domain":  "SOFTWARE",
        "discipline": "SE / AI / Product",
        "role":    "Junior Software / AI Engineer",
        "subject": "Junior Software Engineer Application: Abdullah Bin Masaud – COMSATS 2026 (Backend & AI)",
        "body": """Dear Tintash Talent Team,

Tintash's reputation as a product engineering studio that builds and scales software for startups and Fortune 500 companies is well known across Pakistan's tech community.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), available immediately for on-site (Lahore) or remote roles.

Portfolio Highlights (all on GitHub):
1. Edge AI (FYP — VisionAid): Real-time YOLOv8 object detection on Raspberry Pi 4 edge hardware with audio feedback cues.
2. Medical AI Segmentation: Trained U-Net on MRI brain scans with 91%+ Dice similarity score.
3. Backend REST APIs: Flask services with JWT authentication, 25+ pytest test cases, and Swagger documentation.
4. Production ML: XGBoost churn prediction engine with SHAP explainability and Flask REST API.
5. Real-Time Streaming: Flask + Socket.IO + OpenCV video and telemetry dashboard.

Ready for technical evaluation at any time.

GitHub: https://github.com/abdullah-bin-masaud
LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
Phone: +92 332 9076356

My Software CV is attached.

Warm regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },

    # ── 14. Programmers Force ──
    {
        "company": "Programmers Force (Lahore / Islamabad)",
        "email":   "hr@programmersforce.com",
        "domain":  "SOFTWARE",
        "discipline": "SE / CS / AI",
        "role":    "Junior Software / Machine Learning Engineer",
        "subject": "Junior Software Engineer Application: Abdullah Bin Masaud – COMSATS 2026",
        "body": """Dear Programmers Force Talent Team,

Programmers Force's rapid growth as an AI and software engineering powerhouse delivering solutions for global clients represents an exciting technical environment.

I am graduating with a BS in Computer Engineering from COMSATS University Islamabad in 2026, available immediately for your Islamabad or Lahore office.

Technical Competencies:
- AI & Computer Vision: Real-time YOLOv8 edge deployment on Raspberry Pi 4 (VisionAid FYP), U-Net medical image segmentation (91%+ Dice score), and Traffic Counter REST API.
- Backend APIs: Flask REST services with JWT authentication, automated pytest suites (25+ tests), and Swagger API documentation.
- Network Systems: Multithreaded TCP/IP socket server with custom binary packet framing and CRC32 checksum validation.
- ML Deployment: Production XGBoost predictive model with SHAP explainability deployed as a REST API.

I am ready for immediate onboarding and any technical screening.

GitHub: https://github.com/abdullah-bin-masaud
LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
Phone: +92 332 9076356

My Software CV is attached.

Best regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },

    # ── 15. Devsinc ──
    {
        "company": "Devsinc (Lahore / Islamabad)",
        "email":   "careers@devsinc.com",
        "domain":  "SOFTWARE",
        "discipline": "SE / CS / AI",
        "role":    "Associate Software Engineer",
        "subject": "Associate Software Engineer Application: Abdullah Bin Masaud – COMSATS 2026",
        "body": """Dear Devsinc Recruitment Team,

Devsinc's culture of building scalable software products for global startups while developing world-class engineering talent makes it an ideal place to launch my professional career.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), available for Islamabad, Lahore, or remote positions.

What I Bring to Devsinc:
- AI & Computer Vision: YOLOv8 real-time edge deployment on Raspberry Pi 4 (FYP), U-Net MRI segmentation (91%+ Dice), and XGBoost customer churn model with SHAP explainability.
- Backend Architecture: Flask REST APIs with JWT authentication, full CRUD endpoints, 25+ pytest test cases, and Swagger documentation.
- Systems Concurrency: Multithreaded TCP/IP socket server with binary packet framing, CRC32 checksum validation, and 50-client load testing.
- Real-Time Streaming: Live telemetry dashboard using Flask, Socket.IO, and OpenCV.

I welcome any technical test or coding assessment.

GitHub: https://github.com/abdullah-bin-masaud
LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
Phone: +92 332 9076356

My Software CV is attached.

Sincerely,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },

    # ── 16. Rolustech ──
    {
        "company": "Rolustech (Lahore)",
        "email":   "hr@rolustech.com",
        "domain":  "SOFTWARE",
        "discipline": "SE / CS / IT",
        "role":    "Junior Software Developer",
        "subject": "Junior Software Developer Application: Abdullah Bin Masaud – COMSATS 2026",
        "body": """Dear Rolustech Hiring Team,

Rolustech's specialization in enterprise CRM architectures, custom web applications, and digital transformation for global clients represents a disciplined engineering culture.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), available for on-site roles in Lahore or remote work.

Technical Highlights:
- Modular Backend APIs: Flask REST services with JWT authentication, structured CRUD endpoints, 25+ pytest test cases, and Swagger documentation.
- Automated Data Auditing: Python QA tool featuring statistical IQR outlier detection, schema enforcement, and automated reporting.
- High-Performance Networking: Custom multithreaded TCP/IP socket protocol with binary packet framing and CRC32 error validation.
- Clean Code Culture: 12 open-source GitHub repositories following clean architecture principles.

Available immediately.

GitHub: https://github.com/abdullah-bin-masaud
LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
Phone: +92 332 9076356

My Software CV is attached.

Warm regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },

    # ── 17. Rapidev ──
    {
        "company": "Rapidev (NSTP, NUST Islamabad — Edge AI & Embedded)",
        "email":   "careers@rapidev.com",
        "domain":  "AI",
        "discipline": "AI / CE / Embedded",
        "role":    "Embedded AI / Computer Vision Engineer Intern",
        "subject": "Embedded AI & Vision Engineer: Abdullah Bin Masaud – NSTP NUST Islamabad (COMSATS 2026)",
        "body": """Dear Rapidev Engineering Leadership at NSTP,

Rapidev's presence at the National Science & Technology Park (NUST, H-12 Islamabad) and your focus on edge AI, embedded systems, and intelligent surveillance represents the exact work I do daily.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), based in the Islamabad area and available immediately.

Why My Skillset Directly Matches Rapidev:
1. VisionAid (FYP): Built a real-time assistive guidance device deploying YOLOv8 on Raspberry Pi 4 edge hardware — handling camera pipelines, model optimization for edge latency, and audio cues.
2. Medical Image Deep Learning: Trained U-Net segmentation models achieving 91%+ Dice similarity score on MRI datasets.
3. Embedded Firmware: Written register-level C code for PIC18F4550 with ISRs, timer debouncing, UART, SPI, and EEPROM state persistence.
4. Real-Time Telemetry: Developed live sensor streaming systems utilizing Flask, Socket.IO, and OpenCV.

I can walk into your NSTP office for an interview or technical demonstration immediately.

GitHub: https://github.com/abdullah-bin-masaud
LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
Phone: +92 332 9076356

My AI & Embedded Systems CV is attached.

Best regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },

    # ── 18. Educative ──
    {
        "company": "Educative (Lahore / US — EdTech Platform)",
        "email":   "careers@educative.io",
        "domain":  "SOFTWARE",
        "discipline": "SE / CS / Systems",
        "role":    "Junior Software Engineer / Content Engineer",
        "subject": "Junior Software Engineer Application: Abdullah Bin Masaud – COMSATS 2026",
        "body": """Dear Educative Talent Team,

Educative's interactive, developer-first learning platform has impacted millions of software engineers globally, and its Lahore engineering team builds high-consequence web systems.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), available for Lahore on-site or remote work.

Engineering Highlights:
- Deep CS Fundamentals: Implemented a custom TCP/IP socket server from scratch with binary packet framing and CRC32 checksums, handling 50 concurrent client connections without race conditions.
- Backend APIs & Testing: Built Flask REST APIs with JWT authentication, modular blueprints, and 25+ pytest test cases verifying HTTP status codes and latency.
- AI & Computer Vision: Deployed YOLOv8 real-time object detection on Raspberry Pi 4 (VisionAid FYP) and trained U-Net segmentation models (91%+ Dice).
- Disciplined Documentation: 12 open-source GitHub repositories with clear documentation and modular code.

Available immediately.

GitHub: https://github.com/abdullah-bin-masaud
LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
Phone: +92 332 9076356

My Software CV is attached.

Sincerely,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },

    # ── 19. Bazaar Technologies ──
    {
        "company": "Bazaar Technologies (Karachi / Lahore / Islamabad — B2B E-commerce)",
        "email":   "careers@bazaar.tech",
        "domain":  "SOFTWARE",
        "discipline": "SE / CS / Fintech",
        "role":    "Junior Backend / Software Engineer",
        "subject": "Junior Software Engineer Application: Abdullah Bin Masaud – COMSATS 2026 (Backend & Data)",
        "body": """Dear Bazaar Technologies Engineering Team,

Bazaar's mission to digitize retail and build retail-scale financial operating systems across Pakistan requires software that performs flawlessly under heavy real-world transaction loads.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), available immediately.

Why I Am a Strong Fit for Bazaar:
- Backend Architecture: Built Flask REST APIs with JWT authentication, modular blueprints, and 25+ automated pytest test cases validating latency (<200ms) and payload validation.
- Data Quality & Auditing: Engineered a Python statistical data validation pipeline with IQR outlier detection — critical for retail inventory and transaction integrity.
- Scalable Protocols: Designed a multithreaded TCP/IP socket server with binary packet framing and CRC32 error validation, load-tested against 50 concurrent client connections.
- ML Analytics: Built an XGBoost customer churn prediction model with SHAP explainability.

Available immediately and open to all Pakistan locations or remote.

GitHub: https://github.com/abdullah-bin-masaud
LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
Phone: +92 332 9076356

My Software Engineering CV is attached.

Best regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },

    # ── 20. PostEx ──
    {
        "company": "PostEx (Lahore / Karachi — Fintech & Logistics)",
        "email":   "careers@postex.pk",
        "domain":  "SOFTWARE",
        "discipline": "SE / CS / Fintech",
        "role":    "Junior Software / Backend Engineer",
        "subject": "Junior Backend Engineer Application: Abdullah Bin Masaud – COMSATS 2026 (Fintech / Logistics)",
        "body": """Dear PostEx Talent Acquisition Team,

PostEx's combination of courier logistics and instant upfront invoice financing for e-commerce merchants is one of the most innovative fintech models in Pakistan. I am writing to apply for a Junior Backend Engineer role.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), available immediately.

Technical Qualifications:
- API Engineering: Developed Flask REST APIs with JWT authentication, full CRUD operations, and 25+ automated pytest test cases validating response benchmarks and error handling.
- Data Validation Pipelines: Built an automated Python data auditing tool featuring statistical outlier detection (IQR) and anomaly logging — directly relevant to shipment and transaction reconciliation.
- Systems Reliability: Custom TCP/IP multithreaded socket server with binary packet framing and CRC32 checksum error validation.
- Predictive ML: Built an XGBoost customer churn prediction engine with SHAP feature explainability.

Open to Lahore on-site or remote.

GitHub: https://github.com/abdullah-bin-masaud
LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
Phone: +92 332 9076356

My Software CV is attached.

Warm regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },

    # ── 21. Afiniti ──
    {
        "company": "Afiniti Pakistan (Islamabad / Lahore / Karachi)",
        "email":   "careers@afiniti.com",
        "domain":  "AI",
        "discipline": "AI / CS / SE",
        "role":    "Associate AI / Software Engineer",
        "subject": "Associate AI Engineer Application: Abdullah Bin Masaud – COMSATS 2026 (Islamabad)",
        "body": """Dear Afiniti Talent Acquisition Team,

Afiniti's global leadership in applying artificial intelligence to enterprise customer interaction routing represents the high standard of applied AI engineering I aspire to contribute to.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), based in the Islamabad area and immediately available.

AI & Systems Portfolio:
1. Deep Learning & Computer Vision: Trained U-Net segmentation models achieving 91%+ Dice score on MRI scans, and deployed real-time YOLOv8 object detection on Raspberry Pi 4 edge hardware (VisionAid FYP).
2. Machine Learning Engineering: Built an XGBoost customer churn model with SHAP explainability, deployed via Flask REST API.
3. Systems Architecture: Implemented a multithreaded TCP/IP client-server system with binary packet framing and CRC32 error validation.
4. Clean Code Standards: 12 open-source GitHub repositories following modular design and automated unit testing.

Available immediately in Islamabad.

GitHub: https://github.com/abdullah-bin-masaud
LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
Phone: +92 332 9076356

My AI & Software CV is attached.

Sincerely,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },

    # ── 22. Kualitatem ──
    {
        "company": "Kualitatem (Lahore — QA & Cybersecurity)",
        "email":   "careers@kualitatem.com",
        "domain":  "SOFTWARE",
        "discipline": "SE / SQA / Security",
        "role":    "Junior SQA / Test Automation Engineer",
        "subject": "Junior SQA & Test Automation Engineer: Abdullah Bin Masaud – COMSATS 2026",
        "body": """Dear Kualitatem Recruitment Team,

Kualitatem's global standing in software quality assurance, automated test engineering, and information security testing represents the standard of software verification I practice.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), available immediately.

Hands-on QA & Testing Experience:
1. Automated API Testing Suite: Built an end-to-end pytest test suite with 25+ test cases validating HTTP status codes, latency thresholds (<200ms), schema enforcement, and concurrent multi-threaded requests.
2. Data Quality & Anomaly Detection: Developed a standalone Python QA auditing engine implementing IQR statistical filtering, missing data detection, and automated JSON/Markdown test reporting.
3. Network Integrity Testing: Implemented low-level TCP/IP socket testing with CRC32 packet integrity validation and deliberate error corruption injection to verify fault detection.
4. Clean Architecture: All 12 GitHub projects include unit testing, automated scripts, and comprehensive documentation.

Available immediately.

GitHub: https://github.com/abdullah-bin-masaud
LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
Phone: +92 332 9076356

My Software QA CV is attached.

Best regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },

    # ── 23. InvoZone ──
    {
        "company": "InvoZone (Lahore — Software & Mobile)",
        "email":   "careers@invozone.com",
        "domain":  "SOFTWARE",
        "discipline": "SE / CS / Web",
        "role":    "Junior Software Engineer",
        "subject": "Junior Software Engineer Application: Abdullah Bin Masaud – COMSATS 2026",
        "body": """Dear InvoZone Hiring Team,

InvoZone's high-velocity product engineering and agile software delivery for international clients from Lahore make it an exceptional environment for a fresh engineering graduate.

I am graduating in Computer Engineering from COMSATS University Islamabad in 2026.

Engineering Capabilities:
- Backend Development: Built Flask REST APIs with JWT authentication, modular blueprints, 25+ automated pytest test cases, and Swagger documentation.
- Data QA Automation: Python data validation engine with statistical IQR outlier detection and anomaly reporting.
- Systems Concurrency: Multithreaded TCP/IP socket server with binary packet framing and CRC32 error validation.
- Computer Vision: YOLOv8 real-time inference (FYP) and U-Net medical segmentation (91%+ Dice).

Available for Lahore on-site or remote roles immediately.

GitHub: https://github.com/abdullah-bin-masaud
LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
Phone: +92 332 9076356

My Software CV is attached.

Warm regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },

    # ── 24. Multinet Pakistan ──
    {
        "company": "Multinet Pakistan (Karachi / Islamabad — Enterprise Telecom & Optical Fiber)",
        "email":   "careers@multinet.com.pk",
        "domain":  "TELECOM",
        "discipline": "Telecom / CE / Networks",
        "role":    "Graduate Trainee Engineer (Network Operations & Transmission)",
        "subject": "Graduate Trainee Network Engineer: Abdullah Bin Masaud – COMSATS 2026 (Islamabad)",
        "body": """Dear Multinet Pakistan Talent Acquisition Team,

Multinet Pakistan's vast nationwide optical fiber backbone, submarine cable connectivity, and enterprise telecom infrastructure represent critical national communication assets.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026) applying for the Graduate Trainee Engineer program in Network Operations and Transmission.

Telecom & Network Engineering Qualifications:
- Network Protocol Engineering: Built a complete multithreaded TCP/IP client-server network stack in Python with binary packet framing, CRC32 checksum error detection, and 50-client concurrency stress testing.
- Real-Time Streaming Systems: Developed live telemetry broadcasting systems utilizing WebSockets and Socket.IO for low-latency metric transmission.
- Hardware Communications: Implemented UART serial protocols on PIC18 microcontrollers with interrupt-driven timing control.
- Academic Background: Strong coursework in computer networks, telecommunications engineering, digital signal processing, and wireless communications.

I am based in the region, understand telecom infrastructure, and am available immediately for Islamabad or nationwide deployment.

GitHub: https://github.com/abdullah-bin-masaud
LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
Phone: +92 332 9076356

My Telecom & Networks CV is attached.

Best regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },

    # ── 25. Wateen Telecom ──
    {
        "company": "Wateen Telecom (Lahore / Islamabad)",
        "email":   "careers@wateen.com",
        "domain":  "TELECOM",
        "discipline": "Telecom / CE / EE",
        "role":    "Graduate Trainee Engineer — Network Infrastructure",
        "subject": "Graduate Trainee Engineer Application: Abdullah Bin Masaud – COMSATS 2026 (Network Infrastructure)",
        "body": """Dear Wateen Telecom HR & Engineering Leadership,

Wateen Telecom's extensive fiber optic network, enterprise managed services, and wireless communication infrastructure represent an outstanding environment for a Computer Engineering graduate passionate about networks.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), applying for a Graduate Trainee Engineer position.

Engineering Skills:
- TCP/IP Protocols & Concurrency: Built a multithreaded TCP/IP client-server network system with binary packet framing and CRC32 error detection, tested under concurrent client loads.
- Real-Time Telemetry: Built live sensor telemetry streaming pipelines over WebSockets and Socket.IO.
- Microcontroller Communications: Register-level C programming on PIC18 microcontrollers with UART, SPI, and timer-driven ISRs.
- Strong Foundations: Telecommunications, RF signal propagation, digital signal processing, and computer networks.

Available immediately in Islamabad or Lahore.

GitHub: https://github.com/abdullah-bin-masaud
LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
Phone: +92 332 9076356

My Telecom CV is attached.

Sincerely,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },

    # ── 26. Mercurial Minds ──
    {
        "company": "Mercurial Minds (Islamabad / Rawalpindi — Telecom & Software)",
        "email":   "careers@mercurialminds.com",
        "domain":  "TELECOM",
        "discipline": "Telecom / SE / CE",
        "role":    "Junior Software / Telecom Solutions Engineer",
        "subject": "Telecom & Software Engineer Application: Abdullah Bin Masaud – COMSATS 2026 (Islamabad / Rawalpindi)",
        "body": """Dear Mercurial Minds Hiring Team,

Mercurial Minds' specialized solutions for telecom operators across Europe, the Middle East, and Asia — integrating network systems with enterprise software — is a direct match for my Computer Engineering degree.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), living in the twin cities area and available immediately.

Core Engineering Strengths:
- Network Protocol Engineering: Built a custom multithreaded TCP/IP socket client-server system with binary packet framing and CRC32 checksum error validation.
- Backend APIs: Built modular Flask REST services with JWT authentication, 25+ pytest test cases, and Swagger API documentation.
- Telemetry & Streaming: Real-time sensor telemetry broadcasting system utilizing Socket.IO and WebSockets.
- Embedded Systems: Register-level C development on PIC18 with UART serial communications and EEPROM persistence.

Available immediately for on-site interviews in Islamabad / Rawalpindi.

GitHub: https://github.com/abdullah-bin-masaud
LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
Phone: +92 332 9076356

My Telecom & Software CV is attached.

Warm regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },

    # ── 27. DTech Systems ──
    {
        "company": "DTech Systems (Islamabad / Rawalpindi — Software & Cloud)",
        "email":   "careers@dtechsystems.co",
        "domain":  "SOFTWARE",
        "discipline": "SE / CS / Cloud",
        "role":    "Junior Software Engineer",
        "subject": "Junior Software Engineer Application: Abdullah Bin Masaud – COMSATS 2026 (Islamabad)",
        "body": """Dear DTech Systems Recruitment Team,

DTech Systems' custom cloud software and enterprise application development in the twin cities area represents an agile and growth-oriented engineering culture.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), available immediately for on-site work in Islamabad.

Technical Highlights:
- Production REST APIs: Modular Flask backends with JWT authentication, full CRUD endpoints, Swagger documentation, and 25+ automated pytest test cases.
- Data Quality Pipelines: Python data auditing tool featuring statistical outlier detection (IQR) and anomaly reporting.
- Network Systems: Multithreaded TCP/IP socket server with binary packet framing and CRC32 checksum validation.
- Computer Vision: YOLOv8 real-time inference on edge hardware (VisionAid FYP).

Available immediately.

GitHub: https://github.com/abdullah-bin-masaud
LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
Phone: +92 332 9076356

My Software CV is attached.

Best regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },

    # ── 28. Panacloud ──
    {
        "company": "Panacloud (Karachi / Islamabad — Cloud & AI)",
        "email":   "careers@panacloud.com",
        "domain":  "SOFTWARE",
        "discipline": "SE / Cloud / AI",
        "role":    "Junior Cloud & Software Engineer",
        "subject": "Junior Software Engineer Application: Abdullah Bin Masaud – COMSATS 2026",
        "body": """Dear Panacloud Talent Team,

Panacloud's focus on cloud-native computing, AI integration, and modern distributed systems engineering represents the modern software paradigm I am trained in.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), available immediately.

Technical Stack & Projects:
- Modular Backend Services: Built Flask REST APIs with JWT authentication, full CRUD operations, and 25+ automated pytest test cases validating latency and schema compliance.
- AI & Computer Vision: Deployed YOLOv8 real-time object detection on Raspberry Pi 4 edge hardware (VisionAid FYP) and trained U-Net medical segmentation models (91%+ Dice).
- Network Protocols: Custom multithreaded TCP/IP socket server with binary packet framing and CRC32 error validation.
- Telemetry & Streaming: Real-time sensor telemetry broadcasting with Flask and Socket.IO.

Available immediately for remote or on-site roles.

GitHub: https://github.com/abdullah-bin-masaud
LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
Phone: +92 332 9076356

My Software CV is attached.

Sincerely,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },

    # ── 29. Platalytics ──
    {
        "company": "Platalytics (Islamabad — Big Data & AI)",
        "email":   "info@platalytics.com",
        "domain":  "AI",
        "discipline": "AI / Data / CS",
        "role":    "Junior AI / Data Engineer",
        "subject": "AI & Data Engineer Application: Abdullah Bin Masaud – COMSATS 2026 (Islamabad)",
        "body": """Dear Platalytics Engineering Team,

Platalytics' specialized big data engineering, AI analytics, and data pipeline solutions in Islamabad represent the exact quantitative and systems engineering challenges I enjoy tackling.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), based in the Islamabad region and available immediately.

Data & AI Portfolio:
- Automated Data QA Pipeline: Built an end-to-end Python data auditing engine featuring statistical IQR outlier detection, missing-data checks, schema validation, and JSON/Markdown test reporting.
- Predictive Modeling: Implemented an XGBoost machine learning engine with SHAP feature explainability, deployed via Flask REST API.
- Deep Learning & Vision: Trained U-Net convolutional neural networks achieving 91%+ Dice score on MRI datasets; deployed YOLOv8 on edge hardware (FYP).
- High-Throughput Protocols: Multithreaded TCP/IP client-server protocol with binary framing and CRC32 integrity validation.

Available immediately in Islamabad.

GitHub: https://github.com/abdullah-bin-masaud
LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
Phone: +92 332 9076356

My AI & Data CV is attached.

Warm regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },

    # ── 30. Avanza Innovations ──
    {
        "company": "Avanza Innovations (Islamabad / Karachi — AI & Smart City Tech)",
        "email":   "careers@avanzainnovations.com",
        "domain":  "AI",
        "discipline": "AI / SE / IoT",
        "role":    "Associate AI & IoT Engineer",
        "subject": "Associate AI & IoT Engineer Application: Abdullah Bin Masaud – COMSATS 2026 (Islamabad)",
        "body": """Dear Avanza Innovations Recruitment Team,

Avanza Innovations' leadership in smart city platforms, IoT integrations, AI analytics, and blockchain infrastructure for regional governments and enterprises represents top-tier engineering.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), available immediately for your Islamabad office.

Why My Profile Fits Avanza Innovations:
1. Edge AI & Computer Vision (FYP): Built VisionAid — deploying YOLOv8 on Raspberry Pi 4 edge hardware with real-time inference and audio guidance cues.
2. Embedded Systems & Microcontrollers: Register-level C development on PIC18 with UART, SPI, I2C, and EEPROM state persistence.
3. Real-Time Telemetry: Built live sensor telemetry streaming pipelines using Flask, Socket.IO, and WebSockets.
4. Production Backend APIs: Developed Flask REST services with JWT authentication, Swagger documentation, and 25+ pytest test cases.

Available immediately in Islamabad.

GitHub: https://github.com/abdullah-bin-masaud
LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
Phone: +92 332 9076356

My AI & Systems CV is attached.

Sincerely,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    }
]

def check_mx(domain):
    """Check if domain has valid MX records before sending."""
    try:
        result = subprocess.getoutput(f"nslookup -type=mx {domain}")
        return "mail exchanger" in result.lower()
    except:
        return False

def get_domain(email):
    return email.split("@")[1] if "@" in email else ""

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
    print("=" * 90)
    print("  PAKISTAN BATCH 11 — 30 FRESH VERIFIED TARGETS")
    print("  Domains: Software, AI, Edge Vision, Embedded, Telecom, FinTech, SQA")
    print(f"  Targets count: {len(TARGETS)} | 100% MX-verified")
    print("=" * 90)
    sent = failed = skipped = 0
    for i, job in enumerate(TARGETS, 1):
        company   = job["company"]
        email     = job["email"]
        domain    = job["domain"]
        role      = job["role"]
        disc      = job["discipline"]
        cv_path   = CV_MAP[domain]
        em_domain = get_domain(email)

        print(f"\n[{i:02d}/{len(TARGETS)}] {company} [{disc}]")
        print(f"      To      : {email}")
        print(f"      CV      : {cv_path.name}  |  {domain}")
        print(f"      Role    : {role}")

        # Final MX verify check
        if not check_mx(em_domain):
            print("      MX Check: FAILED — SKIPPING")
            log_application(company, email, domain, role, "SKIPPED_NO_MX")
            skipped += 1
            continue

        try:
            send_email(email, job["subject"], job["body"], cv_path)
            log_application(company, email, domain, role, "SENT")
            print(f"      Status  : [OK] DELIVERED ✓")
            sent += 1
            time.sleep(1)  # small pause to ensure gentle sending rate
        except Exception as e:
            log_application(company, email, domain, role, f"FAILED: {e}")
            print(f"      Status  : [FAIL] {e}")
            failed += 1

    print("\n" + "=" * 90)
    print(f"  BATCH 11 DISPATCH FINISHED  |  Sent: {sent}  |  Skipped: {skipped}  |  Failed: {failed}")
    print("=" * 90)

if __name__ == "__main__":
    main()
