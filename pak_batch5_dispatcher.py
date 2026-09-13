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
    "BPO":      CV_DIR / "CV_E.pdf",
}

TARGETS = [
    # --- KPK Companies ---
    {
        "company": "KPITB - KPK IT Board (Peshawar, KPK)",
        "email":   "info@kpitb.gov.pk",
        "domain":  "SOFTWARE",
        "location": "Peshawar, KPK",
        "role":    "IT Systems & Applications Trainee",
        "subject": "Job Application - IT Systems Trainee - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Government IT systems, Python automation, database administration, and digital services deployment."
    },
    {
        "company": "Gandhara University (Peshawar, KPK)",
        "email":   "info@gandhara.edu.pk",
        "domain":  "HARDWARE",
        "location": "Peshawar, KPK",
        "role":    "Lab Engineer - Computer & Electrical Engineering",
        "subject": "Job Application - Lab Engineer (CE/EE) - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Digital systems labs, embedded C programming, microcontroller fundamentals, and hardware lab supervision."
    },
    {
        "company": "Sarhad University of IT (Peshawar, KPK)",
        "email":   "info@suit.edu.pk",
        "domain":  "SOFTWARE",
        "location": "Peshawar, KPK",
        "role":    "Lab Engineer / IT Instructor Support",
        "subject": "Job Application - Lab Engineer (Computer Science) - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "CS lab instruction, Python and C programming, OOP concepts, and database fundamentals support."
    },
    {
        "company": "Abbottabad University of Science & Technology (AUST, KPK)",
        "email":   "info@aust.edu.pk",
        "domain":  "HARDWARE",
        "location": "Abbottabad, KPK",
        "role":    "Lab Engineer - Computer Engineering",
        "subject": "Job Application - Lab Engineer (CE) - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Embedded systems labs, microcontroller C/C++, Proteus simulation, and digital electronics demonstrations."
    },
    {
        "company": "Hazara University (Mansehra, KPK)",
        "email":   "info@hu.edu.pk",
        "domain":  "SOFTWARE",
        "location": "Mansehra, KPK",
        "role":    "Lab Engineer / Computer Science Support",
        "subject": "Job Application - Lab Engineer - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Programming lab instruction, Python/C coursework, data structures, and computing fundamentals."
    },
    # --- AI / Data Science Companies ---
    {
        "company": "Techverx (Lahore)",
        "email":   "careers@techverx.com",
        "domain":  "AI",
        "location": "Lahore",
        "role":    "Junior AI / Machine Learning Engineer",
        "subject": "Job Application - Junior AI/ML Engineer - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "YOLOv8 object detection, PyTorch/TensorFlow model training, real-time inference on Raspberry Pi edge hardware, and computer vision pipelines."
    },
    {
        "company": "Datatechvision (Islamabad)",
        "email":   "info@datatechvision.com",
        "domain":  "AI",
        "location": "Islamabad",
        "role":    "Data Science / AI Trainee",
        "subject": "Job Application - Data Science Trainee - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Statistical data analysis with NumPy/Pandas, ML model development, feature engineering, and real-time sensor data pipelines."
    },
    {
        "company": "Programmers Force (Lahore)",
        "email":   "careers@programmersforce.com",
        "domain":  "SOFTWARE",
        "location": "Lahore",
        "role":    "Junior Software Engineer (Python/Backend)",
        "subject": "Job Application - Junior Software Engineer - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Flask/Django REST APIs, PostgreSQL database schemas, Git version control, and 25+ automated pytest test coverage."
    },
    # --- Fintech / Banking Tech ---
    {
        "company": "1Link Pakistan (Karachi / Islamabad)",
        "email":   "info@1link.net.pk",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "IT / Systems Graduate Trainee",
        "subject": "Job Application - IT Graduate Trainee - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Payment switch systems, data transmission protocols, API integration, and financial IT infrastructure support."
    },
    {
        "company": "SadaPay (Islamabad)",
        "email":   "info@sadapay.com",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "Junior Backend / Systems Engineer",
        "subject": "Job Application - Junior Backend Engineer - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "RESTful API development, financial data pipelines, Python backend services, and automated API testing."
    },
    {
        "company": "Finja (Islamabad)",
        "email":   "hr@finja.pk",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "Junior Software Engineer (Fintech)",
        "subject": "Job Application - Junior Software Engineer - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Fintech platform development, Python/Node.js backend, database ORM, API integrations, and test-driven development."
    },
    # --- Education Tech / EdTech ---
    {
        "company": "Sabaq.pk EdTech (Islamabad)",
        "email":   "info@sabaq.pk",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "IT / Content Systems Support",
        "subject": "Job Application - IT Systems Support - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Educational technology platforms, Python backend, content management, and database query optimization."
    },
    {
        "company": "Taleemabad EdTech (Karachi / Remote)",
        "email":   "info@taleemabad.com",
        "domain":  "AI",
        "location": "Karachi",
        "role":    "AI / Machine Learning Content Engineer",
        "subject": "Job Application - AI Engineer - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Computer vision for educational content, Python AI/ML pipelines, NLP basics, and interactive model deployment."
    },
    # --- Accounting / Consulting ---
    {
        "company": "A.F. Ferguson & Co (KPMG Pakistan, Lahore / Islamabad)",
        "email":   "hr@afferguson.com",
        "domain":  "BPO",
        "location": "Islamabad",
        "role":    "IT Audit / Technology Risk Trainee",
        "subject": "Job Application - IT Audit Trainee - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "IT audit processes, data analytics in Excel, database verification, system compliance checks, and professional English reporting."
    },
    {
        "company": "Deloitte Pakistan (Islamabad / Karachi)",
        "email":   "careers.pk@deloitte.com",
        "domain":  "BPO",
        "location": "Islamabad",
        "role":    "Technology / IT Risk Trainee",
        "subject": "Job Application - Technology Risk Trainee - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Technology audit, Excel data modeling, IT risk assessment, business process documentation, and professional communication."
    },
    # --- More ISB/Pindi Tech ---
    {
        "company": "NetStar Technologies (Islamabad)",
        "email":   "info@netstar.pk",
        "domain":  "TELECOM",
        "location": "Islamabad",
        "role":    "Network / IT Support Engineer",
        "subject": "Job Application - Network IT Engineer - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "TCP/IP network configuration, LAN/WAN troubleshooting, Python socket programming, and NOC monitoring tools."
    },
    {
        "company": "Vinculum Pakistan (Islamabad)",
        "email":   "hr@vinculum.co",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "Junior Software / Backend Engineer",
        "subject": "Job Application - Junior Software Engineer - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "E-commerce platform APIs, Python/Flask backend, REST integration, database design, and CI/CD pipeline support."
    },
    {
        "company": "Finastra Pakistan (Islamabad)",
        "email":   "careers@finastra.com",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "Associate Software Developer",
        "subject": "Job Application - Associate Software Developer - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Fintech API integration, Java/Python backend, REST microservices, database schemas, and automated unit testing."
    },
    {
        "company": "Xgrid (Islamabad)",
        "email":   "careers@xgrid.co",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "Junior Cloud / Software Engineer",
        "subject": "Job Application - Junior Software Engineer - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Python scripting, cloud infrastructure automation, REST APIs, Docker basics, and test-driven backend development."
    },
    {
        "company": "CloudTech ISB (Islamabad)",
        "email":   "info@cloudtech.pk",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "Junior Cloud / DevOps Trainee",
        "subject": "Job Application - Junior Cloud Trainee - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Cloud services, Linux bash scripting, Python automation, container basics, and CI/CD pipeline fundamentals."
    },
]

def make_email_body(company, role, location, focus, body_type):
    if body_type == "BPO":
        return f"""Dear Hiring Team,

I am writing to apply for the {role} position at {company} ({location}).

I am a Computer Engineering graduate from COMSATS University Islamabad (Graduated August 2026), immediately available for full-time onboarding.

Summary of Qualifications:
- Degree: BS Computer Engineering (Aug 2022 - Aug 2026), COMSATS University Islamabad
- Core Strengths: {focus}
- Communication: Fluent professional verbal and written English, active listening, and conflict resolution skills.
- Technical & Data Skills: Advanced MS Excel (VLOOKUP, formulas, data cleanup), CRM databases, and high-speed typing (60+ WPM with 99% accuracy).
- Shift Availability: 100% available for rotational shifts, day/night shifts, US/UK timezones, and immediate joining.

Profiles:
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356
- Email: abdullahmasaud10@gmail.com

My resume is attached for your review. I would welcome the opportunity for an interview or assessment.

Thank you for your time and consideration.

Best regards,
Abdullah Bin Masaud
BS Computer Engineering | COMSATS University Islamabad
"""
    else:
        return f"""Dear Hiring Team,

I am writing to apply for the {role} position at {company} ({location}).

I am a Computer Engineering graduate from COMSATS University Islamabad (Graduated August 2026), immediately available for full-time onboarding.

Key Technical Qualifications:
- Degree: BS Computer Engineering (Aug 2022 - Aug 2026), COMSATS University Islamabad
- Technical Focus: {focus}
- Final Year Project: VisionAid - Real-time assistive guidance device using YOLOv8 deployed on Raspberry Pi 4 edge hardware with audio feedback cues.
- Open Source Work: 12 public engineering repositories on GitHub covering AI, network socket protocols, and embedded systems.

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
    print("  5-CV MASTER DISPATCHER - BATCH 5")
    print("  KPK | AI/Data | Fintech | EdTech | Consulting | ISB Tech Houses")
    print(f"  Targets: {len(TARGETS)} companies & institutions")
    print("=" * 80)

    sent = 0
    failed = 0

    for i, job in enumerate(TARGETS, 1):
        company   = job["company"]
        email     = job["email"]
        domain    = job["domain"]
        location  = job["location"]
        role      = job["role"]
        subject   = job["subject"]
        focus     = job["focus"]
        body_type = job["body_type"]
        cv_path   = CV_MAP[domain]
        body      = make_email_body(company, role, location, focus, body_type)

        print(f"\n[{i:02d}/{len(TARGETS)}] {company}")
        print(f"      To      : {email}")
        print(f"      CV      : {cv_path.name} ({domain})")
        print(f"      Subject : {subject}")

        try:
            send_email(email, subject, body, cv_path)
            log_application(company, email, domain, role, "SENT")
            print("      Status  : [OK] DELIVERED")
            sent += 1
            time.sleep(3)
        except Exception as e:
            log_application(company, email, domain, role, f"FAILED: {e}")
            print(f"      Status  : [FAIL] {e}")
            failed += 1

    print("\n" + "=" * 80)
    print(f"  BATCH 5 COMPLETED: {sent} Sent | {failed} Failed")
    print("=" * 80)

if __name__ == "__main__":
    main()
