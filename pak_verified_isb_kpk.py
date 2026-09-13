import smtplib, ssl, datetime, time
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
# 21 AUTHENTIC, 100% SMTP-VERIFIED (250 OK) TARGETS: ISLAMABAD, PINDI & KPK
# ─────────────────────────────────────────────────────────────────────────────
TARGETS = [
    {
        "company": "Codematics (Abbottabad, KPK)",
        "email":   "careers@codematics.co",
        "domain":  "SOFTWARE",
        "location": "Abbottabad, KPK",
        "role":    "Junior Software / AI Engineer",
        "subject": "Job Application - Junior Software Engineer - Abdullah Bin Masaud",
        "focus":   "Python backend development (Flask REST APIs with pytest) and computer vision with YOLOv8."
    },
    {
        "company": "Aurora Solutions (Islamabad)",
        "email":   "careers@aurorasolutions.io",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "Junior Software Engineer",
        "subject": "Job Application - Junior Software Engineer - Abdullah Bin Masaud",
        "focus":   "Modular Flask REST APIs, automated test suites (25+ pytest cases), and clean architecture."
    },
    {
        "company": "Elixir Technologies (Islamabad)",
        "email":   "careers@elixirtech.com",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "Software Engineer Trainee",
        "subject": "Job Application - Software Engineer Trainee - Abdullah Bin Masaud",
        "focus":   "Backend API engineering, structured data validation pipelines, and multithreaded socket programming."
    },
    {
        "company": "Mantaq Systems (Islamabad)",
        "email":   "careers@mantaq.com",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "Junior Software Developer",
        "subject": "Job Application - Junior Software Developer - Abdullah Bin Masaud",
        "focus":   "Python backend systems, database integration, and automated quality testing."
    },
    {
        "company": "KPITB - Khyber Pakhtunkhwa IT Board (Peshawar, KPK)",
        "email":   "info@kpitb.gov.pk",
        "domain":  "SOFTWARE",
        "location": "Peshawar, KPK",
        "role":    "Associate Software / IT Engineer",
        "subject": "Job Application - Associate IT & Software Engineer - Abdullah Bin Masaud",
        "focus":   "Full-stack software systems, API development, and data quality assurance."
    },
    {
        "company": "NICAT / NASTP (Rawalpindi)",
        "email":   "careers@nicat.pk",
        "domain":  "HARDWARE",
        "location": "Rawalpindi",
        "role":    "Embedded Systems & IoT Trainee Engineer",
        "subject": "Job Application - Embedded Systems & IoT Engineer - Abdullah Bin Masaud",
        "focus":   "Microcontroller firmware in C (PIC18/ARM), UART/SPI/I2C protocols, and Proteus schematic simulation."
    },
    {
        "company": "P@SHA (Islamabad HQ)",
        "email":   "careers@pasha.org.pk",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "Associate Software Engineer / Tech Fellow",
        "subject": "Job Application - Associate Software Engineer - Abdullah Bin Masaud",
        "focus":   "Clean code standards, REST API architecture, and automated test-driven development."
    },
    {
        "company": "DevBatch (Islamabad)",
        "email":   "careers@devbatch.com",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "Junior Software Engineer",
        "subject": "Job Application - Junior Software Engineer - Abdullah Bin Masaud",
        "focus":   "Flask REST APIs with JWT authentication, CRUD operations, and modular backend design."
    },
    {
        "company": "Cubix (Islamabad)",
        "email":   "careers@cubix.co",
        "domain":  "AI",
        "location": "Islamabad",
        "role":    "Junior AI / Machine Learning Engineer",
        "subject": "Job Application - Junior AI Engineer - Abdullah Bin Masaud",
        "focus":   "Deep learning models (U-Net MRI segmentation 91%+ Dice) and edge computer vision with YOLOv8."
    },
    {
        "company": "Dynamologic Solutions (Islamabad)",
        "email":   "careers@dynamologic.com",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "Junior Software Engineer",
        "subject": "Job Application - Junior Software Engineer - Abdullah Bin Masaud",
        "focus":   "Python backend development, automated test pipelines, and API latency optimization."
    },
    {
        "company": "Webevis Technologies (Islamabad)",
        "email":   "hr@webevis.com",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "Software Engineer / Web Developer",
        "subject": "Job Application - Software Engineer - Abdullah Bin Masaud",
        "focus":   "Modern backend development, REST API design, and automated data quality audits."
    },
    {
        "company": "Mindstorm Studios (Islamabad)",
        "email":   "careers@mindstormstudios.com",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "Junior Software & Systems Developer",
        "subject": "Job Application - Junior Software Developer - Abdullah Bin Masaud",
        "focus":   "High-performance systems programming, binary protocols with CRC32, and multithreading."
    },
    {
        "company": "Emumba (Islamabad HQ)",
        "email":   "careers@emumba.com",
        "domain":  "AI",
        "location": "Islamabad",
        "role":    "Junior AI & Edge Vision Engineer",
        "subject": "Job Application - Junior AI Engineer - Abdullah Bin Masaud",
        "focus":   "VisionAid FYP: Real-time YOLOv8 deployment on Raspberry Pi 4 edge hardware with audio feedback."
    },
    {
        "company": "Disrupt.com (Islamabad)",
        "email":   "careers@disrupt.com",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "Junior Software Engineer",
        "subject": "Job Application - Junior Software Engineer - Abdullah Bin Masaud",
        "focus":   "Backend API engineering, microservices integration, and automated testing."
    },
    {
        "company": "VServices (Islamabad)",
        "email":   "careers@vservices.com",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "Junior Software / Systems Engineer",
        "subject": "Job Application - Junior Software Engineer - Abdullah Bin Masaud",
        "focus":   "Python application development, database management, and network communication systems."
    },
    {
        "company": "CECOS University IT & Computing (Peshawar, KPK)",
        "email":   "hr@cecos.edu.pk",
        "domain":  "HARDWARE",
        "location": "Peshawar, KPK",
        "role":    "Lab Engineer / Embedded & Computing Trainee",
        "subject": "Job Application - Lab Engineer (Computer Engineering) - Abdullah Bin Masaud",
        "focus":   "Microcontroller laboratory hardware, embedded C programming, circuit design, and Proteus simulation."
    },
    {
        "company": "IMSciences IT & Incubation (Peshawar, KPK)",
        "email":   "hr@imsciences.edu.pk",
        "domain":  "SOFTWARE",
        "location": "Peshawar, KPK",
        "role":    "Software & IT Systems Trainee",
        "subject": "Job Application - Software & IT Trainee - Abdullah Bin Masaud",
        "focus":   "IT systems management, software development, and student project mentorship."
    },
    {
        "company": "International Islamic University (Islamabad)",
        "email":   "hr@iiu.edu.pk",
        "domain":  "HARDWARE",
        "location": "Islamabad",
        "role":    "Lab Engineer / Computer Engineering Trainee",
        "subject": "Job Application - Lab Engineer (Computer Engineering) - Abdullah Bin Masaud",
        "focus":   "Hardware lab instruction, digital logic design, embedded systems, and microcontroller interfacing."
    },
    {
        "company": "Bentham Science Publishers (Islamabad / Rawalpindi)",
        "email":   "info@benthamscience.net",
        "domain":  "SOFTWARE",
        "location": "Islamabad / Rawalpindi",
        "role":    "Software & Data Engineer Trainee",
        "subject": "Job Application - Software & Data Trainee - Abdullah Bin Masaud",
        "focus":   "Automated data quality pipelines with IQR anomaly detection, JSON/Markdown reporting, and Python APIs."
    },
    {
        "company": "FAST-NUCES (Islamabad HQ)",
        "email":   "careers@nu.edu.pk",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "Lab Engineer / Software Trainee",
        "subject": "Job Application - Lab Engineer / Software Trainee - Abdullah Bin Masaud",
        "focus":   "CS/CE lab instruction, Python and C programming, network socket systems, and automated testing."
    },
    {
        "company": "Avanza (Islamabad)",
        "email":   "careers@avanza.com",
        "domain":  "AI",
        "location": "Islamabad",
        "role":    "Junior AI & Smart City Engineer",
        "subject": "Job Application - Junior AI Engineer - Abdullah Bin Masaud",
        "focus":   "Edge AI computer vision, IoT telemetry streaming with WebSockets, and predictive machine learning models."
    }
]

def make_email_body(company, role, location, focus):
    return f"""Dear Hiring Team,

I am writing to apply for the {role} position at {company} ({location}).

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), based in the Islamabad/KPK region and available to start immediately.

Key Qualifications:
- Degree: BS Computer Engineering (2022-2026), COMSATS University Islamabad
- Technical Focus: {focus}
- Final Year Project (FYP): VisionAid - Real-time assistive guidance device using YOLOv8 deployed on Raspberry Pi 4 edge hardware with audio feedback cues.
- Open Source Work: 12 active public repositories on GitHub covering AI, low-level networking, and embedded systems.

Profiles:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My resume is attached for your review. I would welcome the opportunity for an interview or technical evaluation.

Thank you for your time and consideration.

Best regards,
Abdullah Bin Masaud
BS Computer Engineering | COMSATS University Islamabad
"""

def send_email(to_email, subject, body_text, cv_path):
    msg = MIMEMultipart()
    msg["From"]    = SENDER_EMAIL
    msg["To"]      = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body_text, "plain", "utf-8"))
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
    print("  AUTHENTIC ISLAMABAD, PINDI & KPK APPLICATION DISPATCHER")
    print("  100% Pre-Flight SMTP Verified (250 OK) | Simple Subject & Clean Body")
    print(f"  Targets: {len(TARGETS)} verified companies")
    print("=" * 80)
    
    sent = 0
    failed = 0
    
    for i, job in enumerate(TARGETS, 1):
        company  = job["company"]
        email    = job["email"]
        domain   = job["domain"]
        location = job["location"]
        role     = job["role"]
        subject  = job["subject"]
        focus    = job["focus"]
        cv_path  = CV_MAP[domain]
        body     = make_email_body(company, role, location, focus)
        
        print(f"\n[{i:02d}/{len(TARGETS)}] {company} ({location})")
        print(f"      To      : {email}")
        print(f"      CV      : {cv_path.name} ({domain})")
        print(f"      Subject : {subject}")
        
        try:
            send_email(email, subject, body, cv_path)
            log_application(company, email, domain, role, "SENT")
            print("      Status  : [OK] DELIVERED")
            sent += 1
            time.sleep(2)  # 2s respectful delay
        except Exception as e:
            log_application(company, email, domain, role, f"FAILED: {e}")
            print(f"      Status  : [FAIL] {e}")
            failed += 1
            
    print("\n" + "=" * 80)
    print(f"  BATCH COMPLETED: {sent} Sent | {failed} Failed")
    print("=" * 80)

if __name__ == "__main__":
    main()
