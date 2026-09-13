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
    # --- More Punjab Universities ---
    {
        "company": "University of Engineering & Technology Lahore (UET Lahore)",
        "email":   "registrar@uet.edu.pk",
        "domain":  "HARDWARE",
        "location": "Lahore",
        "role":    "Lab Engineer - Electrical & Computer Engineering",
        "subject": "Job Application - Lab Engineer (ECE) - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Embedded systems labs, microcontroller firmware (C/C++), digital electronics, and hardware prototyping lab supervision."
    },
    {
        "company": "University of the Punjab Lahore",
        "email":   "registrar@pu.edu.pk",
        "domain":  "SOFTWARE",
        "location": "Lahore",
        "role":    "Lab Engineer / IT Systems Support",
        "subject": "Job Application - Lab Engineer (CS) - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Computer science programming labs, Python/C++ coursework, database fundamentals, and university IT infrastructure."
    },
    {
        "company": "University of Agriculture Faisalabad (UAF)",
        "email":   "registrar@uaf.edu.pk",
        "domain":  "SOFTWARE",
        "location": "Faisalabad",
        "role":    "IT Systems Support / Lab Engineer",
        "subject": "Job Application - IT Systems Support - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "University IT systems, Python programming support, database administration, and computing infrastructure maintenance."
    },
    {
        "company": "Hajvery University Lahore",
        "email":   "info@hup.edu.pk",
        "domain":  "HARDWARE",
        "location": "Lahore",
        "role":    "Lab Engineer - Computer Engineering",
        "subject": "Job Application - Lab Engineer (Computer Engineering) - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Embedded microcontroller labs, digital circuits, C programming, Proteus simulation, and lab experiment supervision."
    },
    {
        "company": "Islamia University Bahawalpur",
        "email":   "registrar@iub.edu.pk",
        "domain":  "SOFTWARE",
        "location": "Bahawalpur, Punjab",
        "role":    "Lab Engineer / IT Instructor Support",
        "subject": "Job Application - Lab Engineer (CS) - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Computer science lab instruction, Python programming, data structures, OS fundamentals, and IT lab administration."
    },
    # --- Construction / Infrastructure ---
    {
        "company": "Nespak (National Engineering Services Pakistan, Islamabad)",
        "email":   "info@nespak.com.pk",
        "domain":  "HARDWARE",
        "location": "Islamabad",
        "role":    "Graduate Engineer Trainee (Electronics / IT)",
        "subject": "Job Application - Graduate Engineer Trainee - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Civil/infrastructure instrumentation, embedded sensor systems, data acquisition, and engineering project documentation."
    },
    {
        "company": "FWO - Frontier Works Organization (Rawalpindi)",
        "email":   "info@fwo.com.pk",
        "domain":  "HARDWARE",
        "location": "Rawalpindi",
        "role":    "Graduate Trainee Engineer (Electronics / IT)",
        "subject": "Job Application - Graduate Trainee Engineer - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Electronics and instrumentation, embedded C programming, project monitoring systems, and hardware maintenance."
    },
    # --- Water / Utilities ---
    {
        "company": "WAPDA - Water & Power Development Authority (Lahore)",
        "email":   "info@wapda.gov.pk",
        "domain":  "HARDWARE",
        "location": "Lahore",
        "role":    "Graduate Engineer Trainee (Electronics / Instrumentation)",
        "subject": "Job Application - Graduate Engineer Trainee - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Power instrumentation, embedded monitoring systems, SCADA data logging, and engineering project data analysis."
    },
    {
        "company": "CDA - Capital Development Authority IT (Islamabad)",
        "email":   "info@cda.gov.pk",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "IT Systems Trainee / GIS Support",
        "subject": "Job Application - IT Systems Trainee - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Government IT systems, database administration, Python scripting, GIS mapping data, and urban infrastructure digitization."
    },
    # --- Automotive ---
    {
        "company": "Pak Suzuki Motor Company (Karachi)",
        "email":   "careers@paksuzuki.com.pk",
        "domain":  "HARDWARE",
        "location": "Karachi",
        "role":    "Graduate Engineer Trainee (Electronics / Embedded)",
        "subject": "Job Application - Graduate Engineer Trainee - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Automotive embedded systems, CAN bus protocols, microcontroller firmware, sensor telemetry, and ECU testing."
    },
    {
        "company": "Toyota Indus Motor (Karachi)",
        "email":   "careers@imc.com.pk",
        "domain":  "HARDWARE",
        "location": "Karachi",
        "role":    "Management Trainee Engineer",
        "subject": "Job Application - Management Trainee Engineer - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Automotive manufacturing electronics, embedded control systems, PLC automation, and quality control instrumentation."
    },
    # --- Textile Industry ---
    {
        "company": "Nishat Mills (Faisalabad / Lahore)",
        "email":   "hr@nishatmills.com",
        "domain":  "HARDWARE",
        "location": "Faisalabad",
        "role":    "IT / Automation Graduate Trainee",
        "subject": "Job Application - IT & Automation Trainee - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Industrial automation, PLC/SCADA systems, embedded process monitoring, and IT infrastructure support."
    },
    {
        "company": "Gul Ahmed Textile (Karachi)",
        "email":   "hr@gulahmed.com",
        "domain":  "HARDWARE",
        "location": "Karachi",
        "role":    "IT / Instrumentation Graduate Trainee",
        "subject": "Job Application - IT Graduate Trainee - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Textile manufacturing IT systems, embedded process controls, ERP data management, and production monitoring."
    },
    # --- R&D / Research Labs ---
    {
        "company": "NESCOM - National Engineering & Scientific Commission (Islamabad)",
        "email":   "admin@nescom.org.pk",
        "domain":  "HARDWARE",
        "location": "Islamabad",
        "role":    "Junior Research Engineer (Electronics / Embedded)",
        "subject": "Job Application - Junior Research Engineer - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Embedded firmware (C/C++), DSP fundamentals, sensor data acquisition, hardware prototyping, and FPGA development."
    },
    {
        "company": "PAEC - Pakistan Atomic Energy Commission (Islamabad)",
        "email":   "recruitment@paec.gov.pk",
        "domain":  "HARDWARE",
        "location": "Islamabad",
        "role":    "Junior Electronics Engineer",
        "subject": "Job Application - Junior Electronics Engineer - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Instrumentation and control systems, embedded sensor circuits, radiation monitoring hardware, and PCB design."
    },
    # --- More Software / AI Companies ---
    {
        "company": "Tkxel (Lahore / Islamabad)",
        "email":   "careers@tkxel.com",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "Junior Software Engineer",
        "subject": "Job Application - Junior Software Engineer - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Python/Node.js backend APIs, REST microservices, SQL database design, CI/CD pipelines, and automated testing."
    },
    {
        "company": "Northbay Solutions (Islamabad)",
        "email":   "info@northbay.com",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "Junior Developer / IT Engineer",
        "subject": "Job Application - Junior Developer - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Full-stack web development, Python/Flask APIs, PostgreSQL databases, and test-driven development practices."
    },
    {
        "company": "Centangle Interactive (Islamabad)",
        "email":   "info@centangle.com",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "Junior Software Developer",
        "subject": "Job Application - Junior Software Developer - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Django/Flask web development, REST API design, Python data pipelines, database migrations, and Git-based workflows."
    },
    {
        "company": "Sidat Hyder Morshed Associates (SHMA, Islamabad)",
        "email":   "info@sidathyder.com.pk",
        "domain":  "BPO",
        "location": "Islamabad",
        "role":    "IT / Data Management Trainee",
        "subject": "Job Application - IT Data Trainee - Abdullah Bin Masaud",
        "body_type": "BPO",
        "focus":   "IT audit processes, data management, Excel analytics, enterprise system support, and professional English reporting."
    },
    {
        "company": "Pakistan Railways IT Division (Lahore)",
        "email":   "pro@pakrail.gov.pk",
        "domain":  "SOFTWARE",
        "location": "Lahore",
        "role":    "IT Systems Graduate Trainee",
        "subject": "Job Application - IT Graduate Trainee - Abdullah Bin Masaud",
        "body_type": "TECH",
        "focus":   "Railway operations IT systems, database management, Python scripting, and government IT infrastructure support."
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
    print("  5-CV MASTER DISPATCHER - BATCH 8")
    print("  Punjab Unis | Infrastructure | Automotive | Textile | R&D | Software Houses")
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
    print(f"  BATCH 8 COMPLETED: {sent} Sent | {failed} Failed")
    print("=" * 80)

if __name__ == "__main__":
    main()
