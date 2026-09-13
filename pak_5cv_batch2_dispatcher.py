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
    {
        "company": "Oladoc Healthcare Operations (Lahore / Islamabad)",
        "email":   "info@oladoc.com",
        "domain":  "BPO",
        "location": "Lahore / Islamabad",
        "role":    "Healthcare Operations & Customer Support Associate",
        "subject": "Job Application - Operations & Customer Support - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Healthcare patient support, doctor booking operations, multi-line telephone communication, and advanced Excel reporting."
    },
    {
        "company": "Marham.pk Healthcare Operations (Lahore / Islamabad)",
        "email":   "info@marham.pk",
        "domain":  "BPO",
        "location": "Lahore / Islamabad",
        "role":    "Patient Services & Operations Associate",
        "subject": "Job Application - Patient Services & Operations - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Customer care, patient coordination, appointment management, active listening, and high-speed typing (60+ WPM)."
    },
    {
        "company": "Fatima Group (Lahore, Punjab)",
        "email":   "info@fatima-group.com",
        "domain":  "BPO",
        "location": "Lahore, Punjab",
        "role":    "Operations & Management Trainee",
        "subject": "Job Application - Operations Trainee - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Corporate operations, data auditing pipelines, quantitative problem-solving, and professional correspondence."
    },
    {
        "company": "SNGPL - Sui Northern Gas Pipelines (Lahore, Punjab)",
        "email":   "info@sngpl.com.pk",
        "domain":  "HARDWARE",
        "location": "Lahore, Punjab",
        "role":    "Graduate Engineer Trainee (Operations & Instrumentation)",
        "subject": "Job Application - Graduate Engineer Trainee - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Embedded microcontroller systems, sensor telemetry data streaming, and hardware circuit validation in Proteus."
    },
    {
        "company": "Interloop Holdings (Faisalabad, Punjab)",
        "email":   "info@interloop.com.pk",
        "domain":  "HARDWARE",
        "location": "Faisalabad, Punjab",
        "role":    "Industrial Automation & IT Associate",
        "subject": "Job Application - Industrial Automation Associate - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Microcontroller firmware in C (PIC18), digital electronics, industrial telemetry, and sensor integration."
    },
    {
        "company": "Ministry of IT & Telecom - MoITT (Islamabad HQ)",
        "email":   "info@moitt.gov.pk",
        "domain":  "TELECOM",
        "location": "Islamabad",
        "role":    "IT & Telecom Operations Associate",
        "subject": "Job Application - IT & Telecom Associate - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Computer communication networks, TCP/IP socket programming with CRC32 packet framing, and telecom systems."
    },
    {
        "company": "Telenor Customer Operations (Islamabad HQ)",
        "email":   "customercare@telenor.com.pk",
        "domain":  "BPO",
        "location": "Islamabad",
        "role":    "Customer Support Specialist",
        "subject": "Job Application - Customer Support Specialist - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Customer service excellence, technical troubleshooting, conflict resolution, and 24/7 rotational shift flexibility."
    },
    {
        "company": "FAST-NUCES Info (Islamabad HQ)",
        "email":   "info@nu.edu.pk",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "Lab Engineer / Computing Trainee",
        "subject": "Job Application - Lab Engineer (Computer Science) - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Computer science laboratory instruction, Python and C systems programming, and automated testing with pytest."
    },
    {
        "company": "COMSATS Wah Campus (Wah Cantt, Punjab)",
        "email":   "info@ciitwah.edu.pk",
        "domain":  "HARDWARE",
        "location": "Wah Cantt, Punjab",
        "role":    "Lab Engineer / Computer Engineering Trainee",
        "subject": "Job Application - Lab Engineer (Computer Engineering) - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Microcontroller laboratories, register-level C programming, embedded systems, and Proteus simulation."
    },
    {
        "company": "UET Peshawar (Peshawar, KPK)",
        "email":   "registrar@uetpeshawar.edu.pk",
        "domain":  "HARDWARE",
        "location": "Peshawar, KPK",
        "role":    "Lab Engineer / Electrical & Computer Trainee",
        "subject": "Job Application - Lab Engineer (Computer Engineering) - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Digital systems, embedded C programming, sensor interfacing, and engineering laboratory demonstrations."
    },
    {
        "company": "STEP Education / IT (Lahore, Punjab)",
        "email":   "info@step.edu.pk",
        "domain":  "SOFTWARE",
        "location": "Lahore, Punjab",
        "role":    "IT Systems & Operations Trainee",
        "subject": "Job Application - IT Systems & Operations - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Software application support, database records, Python programming, and technical problem-solving."
    },
    {
        "company": "Timeline Digital (Islamabad)",
        "email":   "contact@timelinedigi.com",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "Junior Software / Backend Developer",
        "subject": "Job Application - Junior Software Developer - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Flask REST API development with JWT authentication, CRUD endpoints, and 25+ automated pytest test cases."
    },
    {
        "company": "O'Cyber (Islamabad)",
        "email":   "info@ocyber.work",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "Software QA & Verification Trainee",
        "subject": "Job Application - Software QA Trainee - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Automated API testing suites (pytest), statistical data validation pipelines with IQR outlier detection, and reporting."
    }
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
    print("  5-CV MASTER DISPATCHER - BATCH 2")
    print("  Status: Computer Engineering Graduate (August 2026)")
    print(f"  Targets: {len(TARGETS)} verified companies & institutions")
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
        
        print(f"\n[{i:02d}/{len(TARGETS)}] {company} ({location})")
        print(f"      To      : {email}")
        print(f"      CV      : {cv_path.name} ({domain})")
        print(f"      Subject : {subject}")
        
        try:
            send_email(email, subject, body, cv_path)
            log_application(company, email, domain, role, "SENT")
            print("      Status  : [OK] DELIVERED")
            sent += 1
            time.sleep(2)
        except Exception as e:
            log_application(company, email, domain, role, f"FAILED: {e}")
            print(f"      Status  : [FAIL] {e}")
            failed += 1
            
    print("\n" + "=" * 80)
    print(f"  BATCH COMPLETED: {sent} Sent | {failed} Failed")
    print("=" * 80)

if __name__ == "__main__":
    main()
