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
# ISLAMABAD & RAWALPINDI 100% VERIFIED TARGETS (HIGH CALLBACK GUARANTEE)
# ─────────────────────────────────────────────────────────────────────────────
TARGETS = [
    {
        "company": "SkytechINN (NSTP, NUST H-12 Islamabad)",
        "email":   "info@skytechinn.com",
        "domain":  "AI",
        "role":    "AI-on-the-Edge & Embedded Vision Engineer Trainee",
        "subject": "Candidate: Abdullah Bin Masaud | Edge AI & Vision Systems (YOLOv8 + Raspberry Pi) | COMSATS 2026 (Islamabad)",
        "body": """Dear SkytechINN Engineering Team at NSTP,

I am writing specifically to apply for Edge AI, Computer Vision, and Embedded Engineering opportunities at SkytechINN's NSTP office (Office #1304, NUST H-12, Islamabad). 

Your work in intelligent surveillance, Edge AI, and robotics is a direct 1-to-1 match with my final year specialisation and hands-on portfolio.

Direct Technical Match:
1. VisionAid (My Final Year Project): Designed and implemented a real-time object detection and spatial guidance system for visually impaired users. Deployed optimized YOLOv8 models onto Raspberry Pi 4 edge hardware with real-time camera inference under strict memory and latency constraints.
2. Embedded & Microcontroller Systems: Direct register-level firmware development in C for PIC18/ARM microcontrollers, UART/SPI telemetry bridges, and Proteus hardware simulation.
3. Computer Vision Portfolio: U-Net medical image segmentation (91%+ Dice score) and YOLOv8 multi-class vehicle/pedestrian detection.

I am graduating in Computer Engineering from COMSATS University Islamabad in 2026. I am located in the local region and can visit your office at NSTP NUST immediately for an interview or technical evaluation.

Verified Portfolio & Code:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My AI & Edge Computing CV (CV__A.pdf) is attached. I look forward to hearing from you.

Warm regards,
Abdullah Bin Masaud
BS Computer Engineering (2022-2026)
COMSATS University Islamabad, Abbottabad Campus
"""
    },
    {
        "company": "Intelsense.ai (Islamabad)",
        "email":   "hr@intelsense.ai",
        "domain":  "AI",
        "role":    "Junior AI / Machine Learning Engineer",
        "subject": "Application: Junior AI Engineer (Fresh Graduate) – Abdullah Bin Masaud – COMSATS 2026 (Islamabad)",
        "body": """Dear Intelsense.ai Hiring Team,

I saw your call for fresh engineering graduates in Islamabad for AI and machine learning roles. As a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), I have focused my degree on applied deep learning, computer vision, and machine learning pipelines.

What I Have Built:
- VisionAid (FYP): Real-time assistive vision device using YOLOv8, deployed on edge hardware with audio feedback for visually impaired individuals.
- Deep Learning Segmentation: U-Net architecture trained on medical MRI datasets with a 91%+ Dice similarity score.
- Machine Learning Engineering: Production predictive engine with XGBoost, featuring SHAP explainability and Flask REST deployment.
- Clean Code Standards: 12 open-source repositories with strict modularity, unit tests, and documentation.

I am in the Islamabad area and available immediately for on-site interviews and technical assessments.

Online Repositories:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Mobile: +92 332 9076356

My AI CV is attached. I welcome the opportunity to discuss how I can contribute to Intelsense.ai's engineering projects.

Best regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "O'Cyber (Islamabad - PWD)",
        "email":   "career@ocyber.work",
        "domain":  "SOFTWARE",
        "role":    "SQA / Software Engineering Intern",
        "subject": "SQA Intern Application: Abdullah Bin Masaud – Computer Engineering (COMSATS 2026)",
        "body": """Dear O'Cyber Hiring Team,

I am applying for the SQA Intern position at O'Cyber (Islamabad - PWD). I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026) with deep, practical experience in automated quality assurance, regression testing, and API verification.

Direct QA & Software Testing Experience:
1. Automated API Testing Suite: Built an end-to-end pytest test suite with 25+ test cases validating HTTP status codes, latency thresholds (<200ms), schema enforcement, and concurrent multi-threaded requests.
2. Data Quality & Anomaly Detection: Developed a standalone Python QA auditing engine implementing IQR statistical filtering, missing data detection, and automated JSON/Markdown test reporting.
3. Network Validation: Implemented low-level TCP/IP socket testing with CRC32 packet integrity validation and error corruption simulation.

I am available to start immediately in Islamabad.

Portfolio:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Contact: +92 332 9076356

My Software Engineering & QA CV (CV__S.pdf) is attached.

Sincerely,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "CARE Pvt Ltd (Center for Advanced Research in Engineering, H-9 Islamabad)",
        "email":   "careers@carepvtltd.com",
        "domain":  "HARDWARE",
        "role":    "Embedded Firmware Design Engineer Trainee",
        "subject": "Candidate: Abdullah Bin Masaud | Embedded Firmware Engineer | COMSATS 2026 (Islamabad H-9)",
        "body": """Dear CARE Engineering Leadership Team,

CARE Pvt Ltd's standing as Pakistan's premier embedded systems, signal processing, and defense engineering R&D organization in Islamabad (H-9) is the reason I am reaching out to your team.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), based locally and ready for an immediate on-site embedded engineering role in Islamabad.

Embedded Systems Capabilities:
1. Low-Level Microcontroller Programming: Written production C code for PIC18F4550 using MPLAB X / XC8. Implemented interrupt service routines (ISRs), timer debouncing, UART transmission, SPI/I2C communication, and EEPROM state persistence.
2. Hardware Prototyping: Circuit design and component-level schematic simulation in Proteus prior to PCB layout.
3. Systems Architecture: Custom binary packet framing with CRC32 error detection, tested across serial and TCP/IP channels.

Every project has documented source code on GitHub:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My Hardware/Embedded CV is attached. I am prepared to sit for your technical engineering exam at your H-9 Islamabad facility at any time.

Sincerely,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Taraz Technologies (Islamabad)",
        "email":   "info@taraztechnologies.com",
        "domain":  "HARDWARE",
        "role":    "Embedded Firmware & Hardware Engineer Trainee",
        "subject": "Embedded Systems Engineer Application: Abdullah Bin Masaud – COMSATS Islamabad (Available Immediately)",
        "body": """Dear Taraz Technologies Hiring Team,

Taraz Technologies' excellence in embedded controllers, power electronic modules, and instrumentation in Islamabad is an ideal match for my technical background.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), available immediately for on-site work in Islamabad.

Hands-on Competencies:
- Microcontroller Firmware: Register-level C development on PIC18 (XC8), timer-driven state machines, ADC sampling, and UART telemetry.
- Telemetry & Interface Bridges: Interfacing hardware sensors to PC dashboards using custom binary protocols with CRC32 integrity validation.
- Circuit Simulation: Complete hardware validation using Proteus schematic capture.

Links & Repositories:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My Embedded Systems CV is attached. I welcome the opportunity to discuss how my firmware skills can support Taraz Technologies' product lines.

Best regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Devomech Solutions (Rawalpindi)",
        "email":   "info@devomech.com",
        "domain":  "HARDWARE",
        "role":    "Robotics & Embedded Systems Engineer Intern",
        "subject": "Embedded Systems & Robotics Engineer: Abdullah Bin Masaud – Rawalpindi (Available Immediately)",
        "body": """Dear Devomech Solutions Engineering Team,

I have followed Devomech's robotics, mechatronics, and custom hardware engineering projects in Rawalpindi with great enthusiasm.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), living within easy reach of Rawalpindi and available immediately.

Practical Hardware Highlights:
- PIC18F4550 Signal Unit: Interrupt-driven firmware in C, UART protocol, EEPROM data logging, and hardware debouncing.
- RFID-based Attendance System: Hardware-software bridge combining RFID reading with PC serial logging and Proteus simulation.
- Sensor Control & Alert Circuits: Multi-sensor analog thresholding and alarm circuitry.

I read datasheets with ease, write clean C code, and debug circuits methodically.

Profiles:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My Embedded Systems CV is attached. I look forward to meeting your engineering team in Rawalpindi.

Warm regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "MRS Electronic Pakistan (Rawalpindi)",
        "email":   "careers.pk@mrs-electronic.com",
        "domain":  "HARDWARE",
        "role":    "Automotive & Embedded Electronics Engineer Trainee",
        "subject": "Embedded Electronics Engineer: Abdullah Bin Masaud – Rawalpindi / Islamabad",
        "body": """Dear MRS Electronic Pakistan Hiring Team,

MRS Electronic's engineering facility in Rawalpindi is at the cutting edge of automotive electronics, CAN-bus integration, and programmable controllers. I am writing to apply for an Embedded Firmware Engineer Trainee role.

I am graduating with a BS in Computer Engineering from COMSATS University Islamabad in 2026, located in the twin cities area.

Core Skills:
- Embedded C: Register-level programming on PIC18 and ARM architectures, ISR design, timer configurations, and memory mapping.
- Communications: Serial UART, SPI, and custom binary packet encoding with CRC32 error detection.
- Circuitry: Analog signal conditioning, sensor integration, and Proteus simulation.

Public Code & Work:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My Embedded Systems CV is attached. I look forward to the chance to interview in Rawalpindi.

Sincerely,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Arbisoft (Islamabad Office, Blue Area)",
        "email":   "freshgradhiring@arbisoft.com",
        "domain":  "AI",
        "role":    "Fresh Graduate Software / AI Engineer",
        "subject": "Fresh Graduate Application: Abdullah Bin Masaud – Computer Engineering – COMSATS 2026 (Islamabad)",
        "body": """Dear Arbisoft Fresh Graduate Hiring Team,

I am writing to apply for Arbisoft's standardized Fresh Graduate Hiring cohort for your Islamabad office. I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026).

Why Arbisoft:
Arbisoft has established the gold standard for engineering culture in Pakistan. I want to contribute to high-impact products alongside engineers who prioritize clean architecture and computer science fundamentals.

What I Bring:
1. VisionAid (FYP): End-to-end computer vision assistive system (YOLOv8 + Raspberry Pi 4 edge deployment).
2. Deep Learning Segmentation: U-Net with 91%+ Dice similarity score on medical MRI datasets.
3. Production REST APIs: Modular Flask API with full pytest test automation, Swagger documentation, and Postman collections.
4. Systems Programming: Multithreaded TCP/IP socket server with binary packet framing and CRC32 error detection.

All 12 projects are publicly verifiable on GitHub:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Mobile: +92 332 9076356

I am available to take your online MCQ and coding assessment immediately, and can join the Islamabad office on day one. CV is attached.

Best regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Xgrid (Islamabad, Gulberg Greens)",
        "email":   "careers@xgrid.co",
        "domain":  "AI",
        "role":    "AI & Cloud Engineering Intern",
        "subject": "AI & Cloud Engineering Intern: Abdullah Bin Masaud – COMSATS 2026 (Gulberg Greens, Islamabad)",
        "body": """Dear Xgrid Talent Team,

I am writing to apply for an AI / Cloud Engineering internship at Xgrid's Islamabad facility (Gulberg Greens). Your focus on AI-driven cloud automation aligns perfectly with my engineering background.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026).

Relevant Experience:
- Edge AI & Resource Optimization: Built and deployed YOLOv8 models on Raspberry Pi 4 edge hardware for real-time computer vision inference.
- Microservices & Streaming: Built a live telemetry streaming dashboard using Flask, WebSockets/Socket.IO, and OpenCV.
- Automated Testing & Reliability: Production-grade pytest suites validating API endpoints, payload integrity, and response latency.

Profiles:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Mobile: +92 332 9076356

I can join your Islamabad office immediately. AI & Systems CV attached.

Warm regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "United Sol (Islamabad)",
        "email":   "career@unitedsol.net",
        "domain":  "SOFTWARE",
        "role":    "Software Engineering Intern",
        "subject": "Software Engineer Intern Application: Abdullah Bin Masaud – COMSATS 2026 (Islamabad)",
        "body": """Dear United Sol HR Team,

I am applying for a Software Engineering internship at United Sol Islamabad. As a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), I have developed a strong software portfolio covering Python, backend APIs, and data quality pipelines.

Engineering Portfolio:
- Modular Flask REST API: Complete with full pytest suite, structured JSON responses, and error handling.
- Automated Data QA Pipeline: Standalone Python validation tool with IQR outlier detection and report export.
- TCP/IP Protocol Engine: Custom multithreaded network protocol with CRC32 packet integrity validation.

I am based in the Islamabad area and can start immediately on-site.

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
        "company": "Nayatel (Islamabad HQ)",
        "email":   "careers@nayatel.com",
        "domain":  "TELECOM",
        "role":    "Network Operations (NOC) Trainee Engineer",
        "subject": "Network Engineer Trainee Application: Abdullah Bin Masaud – COMSATS 2026 (Islamabad HQ)",
        "body": """Dear Nayatel HR & Network Engineering Team,

Nayatel is the backbone of high-speed telecommunications in Islamabad and Rawalpindi. I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026) applying for a Network Operations / NOC Engineer Trainee role at Nayatel HQ in Islamabad.

Telecommunications & Networking Background:
- Socket Programming: Built a multithreaded TCP/IP client-server system in Python with custom binary packet framing and CRC32 error detection.
- Real-Time Streaming: Built live sensor telemetry broadcasting systems over WebSockets and Socket.IO.
- Hardware Communications: Low-level serial UART protocol implementation on PIC18 microcontrollers.

I live in the region, understand telecom infrastructure, and am eager to contribute to Nayatel's 24/7 network operations.

Links:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My Telecom & Network CV (CV__T.pdf) is attached.

Best regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "i2c Inc (Rawalpindi Tech Center)",
        "email":   "careers@i2cinc.com",
        "domain":  "SOFTWARE",
        "role":    "Associate Software Engineer / Intern",
        "subject": "Software Engineer Application: Abdullah Bin Masaud – COMSATS 2026 (Rawalpindi Tech Center)",
        "body": """Dear i2c Inc Talent Acquisition Team,

i2c Inc's global payment processing platform requires software built with deep architectural rigor. I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), applying for an Associate Software Engineer or Intern role at your Rawalpindi Technology Center.

Why My Profile Fits:
- Systems Fundamentals: Designed a custom multithreaded TCP/IP client-server protocol with CRC32 packet integrity validation, handling concurrent client threads without degradation.
- Production-Ready APIs: Developed Flask REST endpoints covered by 25+ pytest test cases verifying latency (<200ms), error conditions, and concurrency.
- Data Reliability: Created automated data quality pipelines with anomaly detection.

I can commute to your Rawalpindi facility with ease and am available immediately.

Links:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My Software Engineering CV is attached.

Respectfully,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "NASTP / NICAT (Rawalpindi, PAF Base Nur Khan)",
        "email":   "info@nastp.gov.pk",
        "domain":  "HARDWARE",
        "role":    "Aerospace & Embedded Systems Research Trainee",
        "subject": "Candidate: Abdullah Bin Masaud | Embedded Systems & Edge AI | COMSATS 2026 (Rawalpindi)",
        "body": """Dear NASTP Administration & Recruitment Directorate,

I am writing to express my interest in joining the research, development, and engineering divisions at NASTP Alpha, PAF Base Nur Khan, Rawalpindi.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), with hands-on competencies in embedded microcontroller firmware, edge AI computer vision, and communication systems.

Technical Experience:
1. Edge AI Deployment: Developed VisionAid — real-time object detection using YOLOv8 running on edge hardware (Raspberry Pi 4) with low-latency audio guidance.
2. Microcontroller Firmware: C/XC8 development on PIC18 microcontrollers with UART communication, timer interrupts, and EEPROM non-volatile logging.
3. Protocol Design: Custom binary packet framing with CRC32 error detection and multithreaded socket handling.

I am based in the twin cities and available immediately for tests and interviews in Rawalpindi.

Repositories:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My Embedded Systems CV is attached.

Warm regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Velosi Integrity & Safety (Islamabad)",
        "email":   "careers@velosiaims.com",
        "domain":  "SOFTWARE",
        "role":    "Engineering Software & Technology Trainee",
        "subject": "Engineering Software Trainee Application: Abdullah Bin Masaud – COMSATS 2026 (Islamabad)",
        "body": """Dear Velosi Integrity & Safety Recruitment Team,

I am writing to apply for engineering software and technology opportunities at Velosi's Islamabad office.

As a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), I have developed strong skills in software quality assurance, engineering data validation pipelines, and embedded monitoring systems.

Engineering Highlights:
- Automated Data Auditing: Built Python-based pipeline validators for checking engineering datasets, calculating statistical outliers (IQR), and logging anomalies.
- Full-Stack Telemetry Dashboard: Built a real-time sensor monitoring dashboard in Flask and WebSockets for tracking temperature, load, and alert thresholds.
- Disciplined Coding: All 12 projects on GitHub follow clean architecture and unit test standards.

I am available to join your Islamabad office immediately.

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
        "company": "Ufone / PTCL Group (Islamabad HQ)",
        "email":   "recruitment@ufone.com",
        "domain":  "TELECOM",
        "role":    "Graduate Trainee Engineer (Telecom & Network Infrastructure)",
        "subject": "Graduate Trainee Engineer Application: Abdullah Bin Masaud – COMSATS 2026 (Islamabad HQ)",
        "body": """Dear Ufone / PTCL Group Talent Acquisition Team,

I am writing to apply for the Graduate Trainee Engineer program in Telecom and Network Operations at Ufone HQ in Islamabad.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), with coursework and hands-on laboratory experience in telecommunications, RF signals, and computer networking.

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
    print("=" * 80)
    print("  ISLAMABAD & RAWALPINDI PRIORITY DISPATCHER — 100% VERIFIED TARGETS")
    print(f"  Targets: {len(TARGETS)} companies in Islamabad / Rawalpindi")
    print("=" * 80)
    sent = failed = 0
    for i, job in enumerate(TARGETS, 1):
        company = job["company"]
        email   = job["email"]
        domain  = job["domain"]
        role    = job["role"]
        cv_path = CV_MAP[domain]
        print(f"\n[{i:02d}/{len(TARGETS)}] {company}")
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
    print("\n" + "=" * 80)
    print(f"  ISB/RWP DISPATCH COMPLETE  |  Sent: {sent}  |  Failed: {failed}")
    print("=" * 80)

if __name__ == "__main__":
    main()
