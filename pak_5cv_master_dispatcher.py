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

# Complete 5 CV mapping
CV_MAP = {
    "AI":       CV_DIR / "CV__A.pdf",
    "HARDWARE": CV_DIR / "CV__H.pdf",
    "TELECOM":  CV_DIR / "CV__T.pdf",
    "SOFTWARE": CV_DIR / "CV__S.pdf",
    "BPO":      CV_DIR / "CV_E.pdf",   # Tailored for Medical Billing, Call Center, Operations, Support
}

# ─────────────────────────────────────────────────────────────────────────────
# 19 AUTHENTIC OPPORTUNITIES ACROSS IT, BPO, MEDICAL BILLING, CALL CENTER & OPS
# ─────────────────────────────────────────────────────────────────────────────
TARGETS = [
    # ── Medical Billing, Call Center, Customer Support & BPO (CV_E.pdf) ──
    {
        "company": "CareCloud / MTBC (Rawalpindi / Islamabad)",
        "email":   "careers@carecloud.com",
        "domain":  "BPO",
        "location": "Rawalpindi / Islamabad",
        "role":    "Medical Billing & Revenue Cycle Management (RCM) Trainee",
        "subject": "Job Application - Medical Billing & RCM Trainee - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Quick grasp of US healthcare billing workflows, patient demographic verification, CMS-1500 claims, and advanced Excel."
    },
    {
        "company": "Ibex Pakistan (Islamabad / Lahore)",
        "email":   "careers.pk@ibex.co",
        "domain":  "BPO",
        "location": "Islamabad / Lahore",
        "role":    "Customer Support Representative / International BPO Associate",
        "subject": "Job Application - Customer Support Representative - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Fluent professional English, active listening, technical troubleshooting, customer empathy, and 24/7 night shift availability."
    },
    {
        "company": "Mindbridge BPO (Lahore)",
        "email":   "info@mindbridge.net",
        "domain":  "BPO",
        "location": "Lahore",
        "role":    "Customer Support & Operations Associate",
        "subject": "Job Application - Customer Support & Operations Associate - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Inbound/outbound client support, CRM ticketing systems, multi-line telephone etiquette, and rotational shift flexibility."
    },
    {
        "company": "Quaid-e-Azam International Hospital (Rawalpindi / Islamabad)",
        "email":   "info@qih.com.pk",
        "domain":  "BPO",
        "location": "Rawalpindi / Islamabad",
        "role":    "Healthcare Operations & Patient Records Trainee",
        "subject": "Job Application - Healthcare Operations & Records Trainee - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Electronic records management, patient data auditing with 99%+ accuracy, high-speed typing (60+ WPM), and data integrity."
    },
    {
        "company": "Islamabad Diagnostic Centre HQ (Islamabad)",
        "email":   "info@idc.net.pk",
        "domain":  "BPO",
        "location": "Islamabad",
        "role":    "Operations & Clinical Data Support Officer",
        "subject": "Job Application - Operations & Data Support Officer - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Diagnostic record audits, clinical data validation, Excel data analysis, and professional client communication."
    },
    {
        "company": "Chughtai Lab Operations (National / Punjab)",
        "email":   "info@chughtailab.com",
        "domain":  "BPO",
        "location": "National / Punjab",
        "role":    "Operations & Customer Support Associate",
        "subject": "Job Application - Operations & Customer Support Associate - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Diagnostic report verification, customer inquiry management, high-speed data entry, and procedural accuracy."
    },
    {
        "company": "Allied Bank Operations (National)",
        "email":   "info@abl.com",
        "domain":  "BPO",
        "location": "National",
        "role":    "Management / Operations Trainee",
        "subject": "Job Application - Operations Trainee - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Quantitative analytical skills, systematic data record management, process documentation, and customer service excellence."
    },
    {
        "company": "BankIslami Customer Operations (National)",
        "email":   "info@bankislami.com.pk",
        "domain":  "BPO",
        "location": "National",
        "role":    "Customer Care & Operations Associate",
        "subject": "Job Application - Customer Care & Operations Associate - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Client relationship management, telephone etiquette, high problem-solving capacity, and procedural compliance."
    },
    {
        "company": "Al Baraka Bank Operations (National)",
        "email":   "info@albaraka.com.pk",
        "domain":  "BPO",
        "location": "National",
        "role":    "Operations & Service Support Officer",
        "subject": "Job Application - Operations & Service Support Officer - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Customer service, transaction verification, structured Excel reporting, and communication proficiency."
    },
    {
        "company": "Transworld Customer Support (Islamabad)",
        "email":   "info@tw1.com",
        "domain":  "BPO",
        "location": "Islamabad",
        "role":    "Technical Support / Helpdesk Associate",
        "subject": "Job Application - Technical Support Associate - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Technical troubleshooting, network customer diagnostics, client communication, and 24/7 rotational shift availability."
    },

    # ── IT & Software Engineering Targets (CV__S.pdf & CV__A.pdf) ──
    {
        "company": "Panacloud (Islamabad)",
        "email":   "info@panacloud.com",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "Junior Software Engineer",
        "subject": "Job Application - Junior Software Engineer - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Python backend development, modular Flask REST APIs with automated pytest test suites, and clean architecture."
    },
    {
        "company": "Disrupt.com (Islamabad)",
        "email":   "info@disrupt.com",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "Junior Software Engineer",
        "subject": "Job Application - Junior Software Engineer - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Backend API engineering, database design, and automated test-driven development."
    },
    {
        "company": "Cubix (Islamabad)",
        "email":   "info@cubix.co",
        "domain":  "AI",
        "location": "Islamabad",
        "role":    "Junior AI / Machine Learning Engineer",
        "subject": "Job Application - Junior AI Engineer - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Deep learning (U-Net MRI segmentation with 91%+ Dice score) and real-time computer vision with YOLOv8."
    },
    {
        "company": "Mindstorm Studios (Islamabad)",
        "email":   "info@mindstormstudios.com",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "Junior Software & Systems Developer",
        "subject": "Job Application - Junior Software Developer - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Low-level systems programming, multithreaded socket servers with CRC32 packet integrity, and algorithms."
    },
    {
        "company": "Webevis Technologies (Islamabad)",
        "email":   "info@webevis.com",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "Junior Software Engineer",
        "subject": "Job Application - Junior Software Engineer - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Full-stack Python backend development, REST APIs with authentication, and automated data quality validation."
    },
    {
        "company": "Aurora Solutions (Islamabad)",
        "email":   "info@aurorasolutions.io",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "Junior Software Engineer",
        "subject": "Job Application - Junior Software Engineer - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Modular Flask RESTful backends, 25+ pytest test cases, and clean object-oriented architecture."
    },
    {
        "company": "Elixir Technologies (Islamabad)",
        "email":   "info@elixirtech.com",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "Software Engineer Trainee",
        "subject": "Job Application - Software Engineer Trainee - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Backend services, statistical data verification pipelines, and network communication architectures."
    },
    {
        "company": "Mantaq Systems (Islamabad)",
        "email":   "info@mantaq.com",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "Junior Software Developer",
        "subject": "Job Application - Junior Software Developer - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Python backend development, database management, and automated testing."
    },
    {
        "company": "DevBatch (Islamabad)",
        "email":   "info@devbatch.com",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "Junior Software Engineer",
        "subject": "Job Application - Junior Software Engineer - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Flask REST API development with JWT authentication, CRUD endpoints, and Swagger documentation."
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
    print("  5-CV MASTER DISPATCHER: IT, BPO, MEDICAL BILLING, CALL CENTER & OPS")
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
            time.sleep(2)  # 2s polite delay
        except Exception as e:
            log_application(company, email, domain, role, f"FAILED: {e}")
            print(f"      Status  : [FAIL] {e}")
            failed += 1
            
    print("\n" + "=" * 80)
    print(f"  BATCH COMPLETED: {sent} Sent | {failed} Failed")
    print("=" * 80)

if __name__ == "__main__":
    main()
