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
    # --- BPO / Call Centers ---
    {
        "company": "Ibex Pakistan (Islamabad)",
        "email":   "hr@ibex.co",
        "domain":  "BPO",
        "location": "Islamabad",
        "role":    "Customer Experience Specialist",
        "subject": "Job Application - Customer Experience Specialist - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Multi-channel customer support (voice, chat, email), conflict resolution, quality monitoring, and shift flexibility."
    },
    {
        "company": "Mindbridge Pvt Ltd (Lahore)",
        "email":   "careers@mindbridge.com.pk",
        "domain":  "BPO",
        "location": "Lahore",
        "role":    "BPO Operations Trainee",
        "subject": "Job Application - BPO Operations Trainee - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Outbound/inbound call operations, CRM data entry, KPI tracking, and professional communication in English."
    },
    {
        "company": "Emenac Inc (Lahore / Remote)",
        "email":   "hr@emenac.com",
        "domain":  "BPO",
        "location": "Lahore",
        "role":    "Call Center Agent / Customer Support",
        "subject": "Job Application - Customer Support Agent - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "US/UK timezone customer service, active listening, complaint resolution, and high-speed typing (60+ WPM)."
    },
    {
        "company": "Callify Pakistan (Islamabad)",
        "email":   "info@callify.pk",
        "domain":  "BPO",
        "location": "Islamabad",
        "role":    "Call Center Representative",
        "subject": "Job Application - Call Center Representative - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Inbound/outbound call handling, customer query resolution, CRM data management, and shift flexibility."
    },
    {
        "company": "Midas Safety (Lahore, Punjab)",
        "email":   "hr@midassafety.com",
        "domain":  "BPO",
        "location": "Lahore, Punjab",
        "role":    "Operations & Customer Support Coordinator",
        "subject": "Job Application - Operations Coordinator - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Operations coordination, professional English communication, data reporting, and office administration skills."
    },
    # --- Medical Billing / Health Tech ---
    {
        "company": "eHealthSource Pakistan (Islamabad)",
        "email":   "info@ehealthsource.com",
        "domain":  "BPO",
        "location": "Islamabad",
        "role":    "Medical Billing & RCM Associate",
        "subject": "Job Application - Medical Billing Associate - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Healthcare Revenue Cycle Management (RCM), insurance claim processing, ICD-10 coding, ERA/EOB reconciliation, and MS Excel data pipelines."
    },
    {
        "company": "MedVoice (Lahore, Punjab)",
        "email":   "careers@medvoice.com",
        "domain":  "BPO",
        "location": "Lahore, Punjab",
        "role":    "Medical Billing & Coding Trainee",
        "subject": "Job Application - Medical Billing Trainee - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Medical billing workflows, CPT/ICD-10 coding, claim submission and denial management, and CRM documentation."
    },
    # --- Banks / Financial ---
    {
        "company": "MCB Bank Limited (Lahore HQ)",
        "email":   "careers@mcb.com.pk",
        "domain":  "BPO",
        "location": "Lahore",
        "role":    "Management Trainee Officer (MTO)",
        "subject": "Job Application - Management Trainee Officer - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Banking operations, customer relationship management, data analysis in Excel, and professional English communication."
    },
    {
        "company": "Bank of Punjab (Lahore, Punjab)",
        "email":   "hr@bop.com.pk",
        "domain":  "BPO",
        "location": "Lahore, Punjab",
        "role":    "Management Trainee Officer (MTO)",
        "subject": "Job Application - Management Trainee Officer - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Branch banking operations, financial data entry, customer service, and quantitative problem-solving."
    },
    {
        "company": "Silk Bank Pakistan (Karachi / Lahore)",
        "email":   "careers@silkbank.com.pk",
        "domain":  "BPO",
        "location": "Lahore",
        "role":    "Operations / Customer Service Trainee",
        "subject": "Job Application - Operations Trainee - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "Retail banking services, customer query handling, cash management support, and electronic data reporting."
    },
    # --- Universities (Lab Engineer) ---
    {
        "company": "Air University Islamabad",
        "email":   "registrar@mail.au.edu.pk",
        "domain":  "HARDWARE",
        "location": "Islamabad",
        "role":    "Lab Engineer - Computer Engineering",
        "subject": "Job Application - Lab Engineer (Computer Engineering) - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Embedded systems labs, microcontroller C programming (PIC18/STM32), Proteus simulations, and digital electronics demonstrations."
    },
    {
        "company": "Bahria University Islamabad",
        "email":   "registrar@bahria.edu.pk",
        "domain":  "HARDWARE",
        "location": "Islamabad",
        "role":    "Lab Engineer - Electrical & Computer Engineering",
        "subject": "Job Application - Lab Engineer (ECE) - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Digital systems, FPGA/VHDL, sensor interfacing, embedded firmware, and engineering experiment supervision."
    },
    {
        "company": "PAF-KIET (Karachi)",
        "email":   "info@pafkiet.edu.pk",
        "domain":  "HARDWARE",
        "location": "Karachi",
        "role":    "Lab Engineer - Computer & Electrical Engineering",
        "subject": "Job Application - Lab Engineer - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Microcontroller programming, embedded systems lab instruction, PCB design, and C/C++ coursework support."
    },
    # --- Utility / Energy / Industrial ---
    {
        "company": "IESCO - Islamabad Electric Supply Company",
        "email":   "info@iesco.com.pk",
        "domain":  "HARDWARE",
        "location": "Islamabad",
        "role":    "Graduate Engineer Trainee (Electrical / Electronics)",
        "subject": "Job Application - Graduate Engineer Trainee - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Power distribution systems, embedded control panels, sensor instrumentation, and engineering data monitoring."
    },
    {
        "company": "PESCO - Peshawar Electric Supply Company (KPK)",
        "email":   "info@pesco.gov.pk",
        "domain":  "HARDWARE",
        "location": "Peshawar, KPK",
        "role":    "Graduate Engineer Trainee",
        "subject": "Job Application - Graduate Engineer Trainee - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Electrical distribution engineering, SCADA & PLC systems, embedded sensor monitoring, and power quality analysis."
    },
    {
        "company": "K-Electric (Karachi)",
        "email":   "careers@ke.com.pk",
        "domain":  "HARDWARE",
        "location": "Karachi",
        "role":    "Graduate Engineer Trainee",
        "subject": "Job Application - Graduate Engineer Trainee - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Embedded SCADA & instrumentation, power distribution electronics, microcontroller monitoring systems, and CAD-based design."
    },
    # --- Defense / Public Sector ---
    {
        "company": "SUPARCO - Space & Upper Atmosphere Research Commission (Islamabad)",
        "email":   "info@suparco.gov.pk",
        "domain":  "HARDWARE",
        "location": "Islamabad",
        "role":    "Junior Aerospace Electronics / Embedded Systems Engineer",
        "subject": "Job Application - Junior Embedded Systems Engineer - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Embedded firmware (C/C++), real-time telemetry data streaming, sensor integration on Raspberry Pi/ARM, and PCB validation."
    },
    {
        "company": "HIT - Heavy Industries Taxila (Taxila, Punjab)",
        "email":   "info@hit.com.pk",
        "domain":  "HARDWARE",
        "location": "Taxila, Punjab",
        "role":    "Junior Design / Electronics Engineer",
        "subject": "Job Application - Junior Electronics Engineer - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Electronic circuit design, microcontroller firmware, PCB schematic capture, embedded C, and hardware prototyping."
    },
    # --- Telecom ---
    {
        "company": "Jazz (Islamabad HQ)",
        "email":   "careers@jazz.com.pk",
        "domain":  "TELECOM",
        "location": "Islamabad",
        "role":    "Network Operations / IT Graduate Trainee",
        "subject": "Job Application - Network Operations Graduate Trainee - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "TCP/IP network protocols, packet analysis, network monitoring, and computer communication systems programming."
    },
    {
        "company": "PTCL (Islamabad HQ)",
        "email":   "careers@ptcl.net.pk",
        "domain":  "TELECOM",
        "location": "Islamabad",
        "role":    "IT / Network Graduate Trainee",
        "subject": "Job Application - IT & Network Graduate Trainee - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Telecommunications network infrastructure, TCP/IP socket programming, NOC operations, and technical troubleshooting."
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
    print("  5-CV MASTER DISPATCHER - BATCH 3")
    print("  BPO | Medical Billing | Banks | Universities | Utility | Defense | Telecom")
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
    print(f"  BATCH 3 COMPLETED: {sent} Sent | {failed} Failed")
    print("=" * 80)

if __name__ == "__main__":
    main()
