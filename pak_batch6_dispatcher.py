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
    # --- E-Commerce / Retail Tech ---
    {
        "company": "Daraz Pakistan (Lahore / Islamabad)",
        "email":   "pk.careers@daraz.pk",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "Associate Software / Operations Engineer",
        "subject": "Job Application - Associate Software Engineer - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "E-commerce platform APIs, Python/Django backend, microservices architecture, SQL/NoSQL databases, and automated test coverage."
    },
    {
        "company": "Yayvo.com (Islamabad)",
        "email":   "info@yayvo.com",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "Junior Developer / IT Operations Trainee",
        "subject": "Job Application - Junior IT Developer - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Backend Python development, database administration, REST API integrations, and e-commerce operations support."
    },
    # --- Logistics / Supply Chain ---
    {
        "company": "TCS Pakistan (Islamabad)",
        "email":   "hr@tcs.com.pk",
        "domain":  "BPO",
        "location": "Islamabad",
        "role":    "Operations & Dispatch Coordinator",
        "subject": "Job Application - Operations Coordinator - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Logistics operations, shipment tracking systems, Excel route-scheduling, customer communication, and data reporting."
    },
    {
        "company": "Leopards Courier (Islamabad)",
        "email":   "info@leopardscourier.com",
        "domain":  "BPO",
        "location": "Islamabad",
        "role":    "Operations & Customer Support Coordinator",
        "subject": "Job Application - Operations Coordinator - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Courier operations, track-and-trace systems, customer query resolution, and data management in Excel."
    },
    {
        "company": "Trax.pk (Islamabad / Lahore)",
        "email":   "info@trax.pk",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "Junior Software / IT Analyst",
        "subject": "Job Application - Junior IT Analyst - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Logistics tech platforms, Python backend, real-time tracking APIs, database query optimization, and system integration."
    },
    # --- Healthcare IT / Digital Health ---
    {
        "company": "Sehat Kahani (Karachi / Islamabad)",
        "email":   "info@sehatkahani.com",
        "domain":  "BPO",
        "location": "Islamabad",
        "role":    "Health Operations & Customer Support Associate",
        "subject": "Job Application - Health Operations Associate - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Telemedicine platform operations, patient scheduling, CRM data management, and professional English communication."
    },
    {
        "company": "Doctorida (Islamabad)",
        "email":   "info@doctorida.com",
        "domain":  "BPO",
        "location": "Islamabad",
        "role":    "Patient Services Coordinator",
        "subject": "Job Application - Patient Services Coordinator - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Healthcare service coordination, appointment management, patient communication, data entry, and Excel reporting."
    },
    {
        "company": "Shaukat Khanum Hospital IT Division (Lahore)",
        "email":   "info@shaukatkhanum.org.pk",
        "domain":  "BPO",
        "location": "Lahore",
        "role":    "IT Operations / Health Systems Support",
        "subject": "Job Application - IT Operations Support - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Hospital EHR/EMR systems, patient record management, IT helpdesk, and operational data reporting."
    },
    # --- Cybersecurity ---
    {
        "company": "Trillium Information Security (Islamabad)",
        "email":   "info@trilliumisec.com",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "Junior Security Analyst / Software Trainee",
        "subject": "Job Application - Junior Security Analyst - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Network security fundamentals, Python scripting for log analysis, OWASP basics, and software vulnerability testing."
    },
    {
        "company": "NETSOL Cybersecurity (Lahore)",
        "email":   "security@netsol.com",
        "domain":  "SOFTWARE",
        "location": "Lahore",
        "role":    "Junior IT Security Analyst",
        "subject": "Job Application - Junior IT Security Analyst - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Application security, automated security scanning, Python tooling for log analysis, and network threat monitoring."
    },
    # --- Real Estate / PropTech ---
    {
        "company": "Zameen.com (Lahore / Islamabad)",
        "email":   "hr@zameen.com",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "Junior Software / Data Engineer",
        "subject": "Job Application - Junior Software Engineer - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "PropTech platform backend, Python/Flask APIs, real estate data pipelines, SQL analytics, and API test automation."
    },
    {
        "company": "Graana.com (Islamabad)",
        "email":   "careers@graana.com",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "Junior Backend / Data Engineer",
        "subject": "Job Application - Junior Backend Engineer - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Real estate platform APIs, Python data pipelines, geospatial database queries, and automated backend testing."
    },
    # --- More KPK / Haripur ---
    {
        "company": "UET Haripur (Haripur, KPK)",
        "email":   "registrar@uetmardan.edu.pk",
        "domain":  "HARDWARE",
        "location": "Haripur, KPK",
        "role":    "Lab Engineer - Computer / Electrical Engineering",
        "subject": "Job Application - Lab Engineer (CE) - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Embedded systems lab management, microcontroller C programming, digital electronics, and Proteus simulation demonstrations."
    },
    {
        "company": "CECOS University (Peshawar, KPK)",
        "email":   "info@cecos.edu.pk",
        "domain":  "SOFTWARE",
        "location": "Peshawar, KPK",
        "role":    "Lab Engineer / IT Instructor Support",
        "subject": "Job Application - Lab Engineer (CS) - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "CS programming labs (Python/C), database systems, OOP coursework, and IT infrastructure support."
    },
    # --- Agriculture / Agri-Tech ---
    {
        "company": "Agritech Ltd Pakistan (Islamabad)",
        "email":   "info@agritech.net.pk",
        "domain":  "BPO",
        "location": "Islamabad",
        "role":    "Operations & Data Analyst Trainee",
        "subject": "Job Application - Operations Trainee - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Agricultural operations data entry, Excel modeling, stakeholder reporting, and professional English communication."
    },
    {
        "company": "CropIn Pakistan (Lahore / Islamabad)",
        "email":   "info@cropin.com",
        "domain":  "AI",
        "location": "Islamabad",
        "role":    "Data / AI Engineer Trainee",
        "subject": "Job Application - Data / AI Trainee - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Computer vision for crop analysis, satellite imagery processing, Python ML pipelines, and agricultural data modeling."
    },
    # --- Insurance Tech ---
    {
        "company": "Jubilee Insurance Pakistan (Karachi / Islamabad)",
        "email":   "hr@jubileeinsurance.com",
        "domain":  "BPO",
        "location": "Islamabad",
        "role":    "Operations / Claims Processing Trainee",
        "subject": "Job Application - Operations Trainee - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Insurance claims data processing, Excel-based reconciliation, customer service communication, and administrative reporting."
    },
    {
        "company": "EFU Insurance (Karachi / Islamabad)",
        "email":   "hr@efu.com.pk",
        "domain":  "BPO",
        "location": "Islamabad",
        "role":    "Operations & Data Management Trainee",
        "subject": "Job Application - Operations Trainee - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Insurance data management, Excel analytics, policy management systems, and professional English correspondence."
    },
    # --- Recruiting & HR Tech ---
    {
        "company": "Rozee.pk / Naukri.pk (Islamabad)",
        "email":   "hr@rozee.pk",
        "domain":  "BPO",
        "location": "Islamabad",
        "role":    "Operations / Customer Success Coordinator",
        "subject": "Job Application - Operations Coordinator - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "HR technology operations, client success management, data entry, job portal administration, and customer support."
    },
    {
        "company": "Job4u Pakistan (Islamabad)",
        "email":   "info@job4u.pk",
        "domain":  "BPO",
        "location": "Islamabad",
        "role":    "Operations & Client Support Coordinator",
        "subject": "Job Application - Operations Coordinator - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Recruitment operations, employer-candidate coordination, CRM data management, and professional English communication."
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
    print("  5-CV MASTER DISPATCHER - BATCH 6")
    print("  E-Commerce | Logistics | Health Tech | Security | PropTech | Insurance | HR Tech")
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
    print(f"  BATCH 6 COMPLETED: {sent} Sent | {failed} Failed")
    print("=" * 80)

if __name__ == "__main__":
    main()
