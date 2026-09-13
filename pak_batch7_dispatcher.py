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
    # --- Rawalpindi / Pindi Companies ---
    {
        "company": "Benazir Bhutto Hospital Rawalpindi",
        "email":   "info@bbhrawalpindi.com",
        "domain":  "BPO",
        "location": "Rawalpindi",
        "role":    "Health Records & Operations Coordinator",
        "subject": "Job Application - Health Records Coordinator - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Patient records management, medical billing data entry, hospital operations support, and professional English communication."
    },
    {
        "company": "Holy Family Hospital Rawalpindi",
        "email":   "info@hfh.com.pk",
        "domain":  "BPO",
        "location": "Rawalpindi",
        "role":    "IT Operations & Admin Coordinator",
        "subject": "Job Application - IT Operations Coordinator - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Hospital IT systems, patient data coordination, records management, and administrative operations support."
    },
    {
        "company": "Roots International Schools (Islamabad / Rawalpindi)",
        "email":   "careers@rootsschools.com",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "IT Systems & Operations Trainee",
        "subject": "Job Application - IT Systems Trainee - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "School ERP systems, IT infrastructure support, Python scripting, and student data management systems."
    },
    {
        "company": "The City School (Islamabad / Rawalpindi)",
        "email":   "hr@thecityschool.edu.pk",
        "domain":  "BPO",
        "location": "Islamabad",
        "role":    "IT Support / Operations Coordinator",
        "subject": "Job Application - IT Operations Coordinator - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "School administration, student records management, IT helpdesk support, and professional English communication."
    },
    # --- Solar / Clean Energy ---
    {
        "company": "Reon Energy Pakistan (Islamabad / Lahore)",
        "email":   "info@reonenergy.com",
        "domain":  "HARDWARE",
        "location": "Islamabad",
        "role":    "Junior Electronics / Embedded Engineer",
        "subject": "Job Application - Junior Embedded Engineer - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Solar inverter monitoring systems, embedded sensor telemetry, PV data logging firmware, and IoT edge computing."
    },
    {
        "company": "Zorays Solar Pakistan (Islamabad)",
        "email":   "info@zorayssolar.com",
        "domain":  "HARDWARE",
        "location": "Islamabad",
        "role":    "Junior Electrical / Electronics Engineer",
        "subject": "Job Application - Junior Electronics Engineer - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Solar PV system design, inverter electronics, embedded monitoring boards, and energy data acquisition pipelines."
    },
    {
        "company": "Beacon Energy (Islamabad)",
        "email":   "info@beaconenergy.com.pk",
        "domain":  "HARDWARE",
        "location": "Islamabad",
        "role":    "Graduate Engineer Trainee (Electronics / Embedded)",
        "subject": "Job Application - Graduate Engineer Trainee - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Power electronics, embedded systems monitoring, solar SCADA integration, and sensor-based energy analytics."
    },
    # --- Gaming / Game Dev ---
    {
        "company": "Caramel Tech (Lahore)",
        "email":   "hr@carameltech.com",
        "domain":  "SOFTWARE",
        "location": "Lahore",
        "role":    "Junior Game Developer / Software Engineer",
        "subject": "Job Application - Junior Software Engineer - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "C/C++ programming, object-oriented design, game engine APIs, and Python scripting for automation pipelines."
    },
    {
        "company": "Gameloft Pakistan (Lahore)",
        "email":   "careers@gameloft.com",
        "domain":  "SOFTWARE",
        "location": "Lahore",
        "role":    "Junior Developer (Mobile/Backend)",
        "subject": "Job Application - Junior Developer - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "C++ systems programming, REST API integration, automated unit testing, version control (Git), and agile workflows."
    },
    # --- Food Tech / FMCG ---
    {
        "company": "Foodpanda Pakistan (Islamabad / Lahore)",
        "email":   "pk.careers@foodpanda.com",
        "domain":  "BPO",
        "location": "Islamabad",
        "role":    "Operations & Customer Support Specialist",
        "subject": "Job Application - Operations Specialist - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Food delivery operations, merchant/rider coordination, customer query resolution, data reporting, and shift flexibility."
    },
    {
        "company": "Bykea Pakistan (Karachi / Islamabad)",
        "email":   "hr@bykea.com",
        "domain":  "BPO",
        "location": "Islamabad",
        "role":    "Customer Support & Operations Coordinator",
        "subject": "Job Application - Customer Support Coordinator - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Ride-hailing/logistics operations, live chat & call support, CRM data entry, complaint resolution, and shift flexibility."
    },
    # --- Pharma / Bio ---
    {
        "company": "Getz Pharma Pakistan (Karachi / Islamabad)",
        "email":   "hr@getzpharma.com",
        "domain":  "BPO",
        "location": "Islamabad",
        "role":    "IT / Operations Graduate Trainee",
        "subject": "Job Application - Operations Trainee - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Pharmaceutical operations support, ERP data entry, Excel analytics, inventory records management, and English correspondence."
    },
    {
        "company": "Ferozsons Laboratories (Rawalpindi)",
        "email":   "hr@ferozsons.com.pk",
        "domain":  "BPO",
        "location": "Rawalpindi",
        "role":    "Operations Management Trainee",
        "subject": "Job Application - Operations Management Trainee - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Pharma supply chain operations, data reconciliation in Excel, professional communication, and process documentation."
    },
    # --- More IT Startups ISB ---
    {
        "company": "Afiniti Pakistan (Islamabad)",
        "email":   "careers@afiniti.com",
        "domain":  "AI",
        "location": "Islamabad",
        "role":    "Junior AI / Data Engineer",
        "subject": "Job Application - Junior AI Engineer - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "AI behavioral analytics, Python ML pipelines, real-time inference systems, and large-scale statistical data processing."
    },
    {
        "company": "Aion Digital (Islamabad)",
        "email":   "info@aiondigital.com",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "Junior Backend / FinTech Engineer",
        "subject": "Job Application - Junior Backend Engineer - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Digital banking APIs, Python Flask microservices, REST integrations, database design, and automated test pipelines."
    },
    {
        "company": "Nepra Technologies (Islamabad)",
        "email":   "info@nepra.com.pk",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "IT Systems Trainee",
        "subject": "Job Application - IT Systems Trainee - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Regulatory IT systems, database management, Python scripting, and IT infrastructure documentation."
    },
    # --- NGO / Development Sector ---
    {
        "company": "United Nations UNDP Pakistan (Islamabad)",
        "email":   "registry.pk@undp.org",
        "domain":  "BPO",
        "location": "Islamabad",
        "role":    "IT / Operations Support Associate",
        "subject": "Job Application - IT Operations Support - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Development sector operations, data management, Excel reporting, and professional English communication in a multicultural setting."
    },
    {
        "company": "USAID Pakistan (Islamabad)",
        "email":   "islamabadusaid@usaid.gov",
        "domain":  "BPO",
        "location": "Islamabad",
        "role":    "IT / Operations Assistant",
        "subject": "Job Application - IT Operations Assistant - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "International development operations, IT systems support, database administration, and professional English reporting."
    },
    {
        "company": "British Council Pakistan (Islamabad)",
        "email":   "information@britishcouncil.org.pk",
        "domain":  "BPO",
        "location": "Islamabad",
        "role":    "Operations / Digital Services Coordinator",
        "subject": "Job Application - Operations Coordinator - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Cultural program operations, digital content management, customer service, data entry, and professional English communication."
    },
    {
        "company": "LUMS - Lahore University of Management Sciences",
        "email":   "hr@lums.edu.pk",
        "domain":  "SOFTWARE",
        "location": "Lahore",
        "role":    "Lab Engineer / IT Systems Support",
        "subject": "Job Application - Lab Engineer / IT Systems Support - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "University IT infrastructure, Python programming support, Linux server administration, and computing lab management."
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
    print("  5-CV MASTER DISPATCHER - BATCH 7")
    print("  Pindi | Solar/Energy | Gaming | Food Tech | Pharma | NGO | LUMS")
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
    print(f"  BATCH 7 COMPLETED: {sent} Sent | {failed} Failed")
    print("=" * 80)

if __name__ == "__main__":
    main()
