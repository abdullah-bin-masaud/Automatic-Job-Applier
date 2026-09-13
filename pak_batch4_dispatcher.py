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
    # --- More Software Houses / IT ---
    {
        "company": "Techlogix (Lahore / Islamabad)",
        "email":   "careers@techlogix.com",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "Junior Software Engineer",
        "subject": "Job Application - Junior Software Engineer - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Flask REST APIs, Python data pipelines, SQL database design, and automated testing with pytest (25+ test cases)."
    },
    {
        "company": "Netsol Technologies (Lahore)",
        "email":   "hr@netsol.com",
        "domain":  "SOFTWARE",
        "location": "Lahore",
        "role":    "Associate Software Developer",
        "subject": "Job Application - Associate Software Developer - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Object-oriented design, RESTful APIs, SQL/NoSQL databases, version control (Git), and SDLC methodologies."
    },
    {
        "company": "TRG Pakistan (Lahore / Islamabad)",
        "email":   "careers@trg.com.pk",
        "domain":  "BPO",
        "location": "Islamabad",
        "role":    "IT Operations / BPO Trainee",
        "subject": "Job Application - IT Operations Trainee - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "BPO operations management, data entry, CRM systems, professional client communication, and shift flexibility."
    },
    {
        "company": "Zones IT Solutions Pakistan (Islamabad)",
        "email":   "info@zones.com",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "IT Solutions / Systems Trainee",
        "subject": "Job Application - IT Solutions Trainee - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "IT infrastructure, Python scripting, network troubleshooting, and customer technical support documentation."
    },
    {
        "company": "Logiciel Services (Islamabad)",
        "email":   "info@logicielservices.com",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "Junior Developer / IT Analyst",
        "subject": "Job Application - Junior Developer - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Full-stack Python/Flask development, REST APIs, relational databases, and agile sprint-based delivery."
    },
    # --- Government IT / Public Sector ---
    {
        "company": "NADRA - National Database Registration Authority (Islamabad)",
        "email":   "info@nadra.gov.pk",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "IT / Software Graduate Trainee",
        "subject": "Job Application - IT Graduate Trainee - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Large-scale database systems, Python scripting, data integrity pipelines, and identity management system support."
    },
    {
        "company": "FBR - Federal Board of Revenue IT (Islamabad)",
        "email":   "helpdesk@fbr.gov.pk",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "IT Support / Systems Trainee",
        "subject": "Job Application - IT Systems Trainee - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "IT helpdesk, ERP system support, database administration, and computer network troubleshooting."
    },
    # --- Hospitals / Health ---
    {
        "company": "PIMS - Pakistan Institute of Medical Sciences (Islamabad)",
        "email":   "info@pims.gov.pk",
        "domain":  "BPO",
        "location": "Islamabad",
        "role":    "Health Information Management / Admin Trainee",
        "subject": "Job Application - Health Information Trainee - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Healthcare records management, medical billing data entry, patient coordination, and hospital administration support."
    },
    {
        "company": "KRL Hospital Islamabad",
        "email":   "info@krlhospital.com.pk",
        "domain":  "BPO",
        "location": "Islamabad",
        "role":    "Admin / Operations Coordinator",
        "subject": "Job Application - Admin & Operations Coordinator - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Hospital front-desk operations, patient record management, medical billing coordination, and Excel reporting."
    },
    {
        "company": "Shifa International Hospital (Islamabad)",
        "email":   "hr@shifa.com.pk",
        "domain":  "BPO",
        "location": "Islamabad",
        "role":    "IT Support / Operations Trainee",
        "subject": "Job Application - IT Operations Trainee - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Hospital ERP support, patient data coordination, clinical operations tracking, and professional English communication."
    },
    # --- Industrial / Manufacturing ---
    {
        "company": "Engro Corporation (Karachi / Lahore)",
        "email":   "careers@engro.com",
        "domain":  "HARDWARE",
        "location": "Lahore",
        "role":    "Graduate Engineer Trainee (Instrumentation / IT)",
        "subject": "Job Application - Graduate Engineer Trainee - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Industrial automation, sensor telemetry, embedded SCADA monitoring, and process instrumentation data pipelines."
    },
    {
        "company": "Fauji Fertilizer Company (Rawalpindi, Punjab)",
        "email":   "career@ffc.com.pk",
        "domain":  "HARDWARE",
        "location": "Rawalpindi",
        "role":    "Management Trainee Engineer (Electronics/IT)",
        "subject": "Job Application - Management Trainee Engineer - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Embedded sensor systems, PLC/instrumentation, digital electronics, and industrial process data monitoring."
    },
    {
        "company": "Pakistan Cables (Karachi)",
        "email":   "hr@pakistancables.com",
        "domain":  "HARDWARE",
        "location": "Karachi",
        "role":    "Graduate Trainee Engineer",
        "subject": "Job Application - Graduate Trainee Engineer - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Electrical manufacturing systems, embedded control electronics, quality control instrumentation, and hardware testing."
    },
    # --- Telecom / ISP ---
    {
        "company": "Mobilink / Jazz (Islamabad)",
        "email":   "hr@jazz.com.pk",
        "domain":  "TELECOM",
        "location": "Islamabad",
        "role":    "Network / IT Graduate Trainee",
        "subject": "Job Application - Network Graduate Trainee - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "TCP/IP network architecture, GSM/LTE system fundamentals, NOC operations, and real-time network telemetry."
    },
    {
        "company": "Zong CM-Pak (Islamabad)",
        "email":   "hr@zong.com.pk",
        "domain":  "TELECOM",
        "location": "Islamabad",
        "role":    "IT / Network Operations Graduate Trainee",
        "subject": "Job Application - IT Graduate Trainee - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Telecommunications network protocols, Python scripting for network automation, and NOC monitoring tools."
    },
    # --- NGO / Research / Social Sector ---
    {
        "company": "Aga Khan University Hospital (Karachi / Islamabad)",
        "email":   "hr@aku.edu",
        "domain":  "BPO",
        "location": "Islamabad",
        "role":    "IT Systems / Operations Support",
        "subject": "Job Application - IT Operations Support - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Hospital information systems, EHR data entry, healthcare operations coordination, and professional English communication."
    },
    {
        "company": "Islamabad Stock Exchange / PSX (Islamabad)",
        "email":   "info@psx.com.pk",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "IT / Data Systems Trainee",
        "subject": "Job Application - IT Data Systems Trainee - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Financial data processing pipelines, real-time database systems, Python analytics, and data integrity validation."
    },
    # --- Media / Broadcast ---
    {
        "company": "ARY Digital Network (Islamabad / Karachi)",
        "email":   "hr@ary.tv",
        "domain":  "BPO",
        "location": "Islamabad",
        "role":    "Operations / Digital Media Support Trainee",
        "subject": "Job Application - Operations Support Trainee - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Media operations coordination, digital content management, shift operations, and professional English communication."
    },
    {
        "company": "Geo News (Karachi / Islamabad)",
        "email":   "info@geo.tv",
        "domain":  "BPO",
        "location": "Islamabad",
        "role":    "Digital Operations / IT Support Trainee",
        "subject": "Job Application - Digital Operations Trainee - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Digital broadcast operations, content management systems, IT helpdesk support, and professional communication."
    },
    {
        "company": "Express News / Express Media Group (Islamabad)",
        "email":   "careers@expressnews.tv",
        "domain":  "BPO",
        "location": "Islamabad",
        "role":    "IT Operations Coordinator",
        "subject": "Job Application - IT Operations Coordinator - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Newsroom operations, digital media workflows, IT helpdesk, and data management with advanced Excel skills."
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
    print("  5-CV MASTER DISPATCHER - BATCH 4")
    print("  Software Houses | Gov IT | Hospitals | Industrial | Telecom | Media")
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
    print(f"  BATCH 4 COMPLETED: {sent} Sent | {failed} Failed")
    print("=" * 80)

if __name__ == "__main__":
    main()
