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
# 20 AUTHENTIC OPPORTUNITIES: PUNJAB, ISLAMABAD, PINDI & KPK
# ─────────────────────────────────────────────────────────────────────────────
TARGETS = [
    {
        "company": "PITB - Punjab Information Technology Board (Lahore)",
        "email":   "info@pitb.gov.pk",
        "domain":  "SOFTWARE",
        "location": "Lahore, Punjab",
        "role":    "Associate Software / IT Engineer",
        "subject": "Job Application - Associate Software Engineer - Abdullah Bin Masaud",
        "focus":   "Python backend development (Flask REST APIs with pytest), data pipelines, and public-sector software solutions."
    },
    {
        "company": "ITU - Information Technology University (Lahore)",
        "email":   "hr@itu.edu.pk",
        "domain":  "SOFTWARE",
        "location": "Lahore, Punjab",
        "role":    "Lab Engineer / Software Trainee",
        "subject": "Job Application - Lab Engineer (Computer Engineering) - Abdullah Bin Masaud",
        "focus":   "Academic laboratory instruction, software testing, algorithm design, and Python/C systems programming."
    },
    {
        "company": "Arbisoft (Lahore HQ)",
        "email":   "contact@arbisoft.com",
        "domain":  "AI",
        "location": "Lahore, Punjab",
        "role":    "Junior Software / AI Engineer",
        "subject": "Job Application - Junior Software / AI Engineer - Abdullah Bin Masaud",
        "focus":   "Computer vision with YOLOv8 (FYP on Raspberry Pi 4), deep learning (U-Net MRI segmentation), and Flask APIs."
    },
    {
        "company": "Contour Software (Lahore HQ)",
        "email":   "info@contour-software.com",
        "domain":  "SOFTWARE",
        "location": "Lahore, Punjab",
        "role":    "Junior Software Developer / QA Trainee",
        "subject": "Job Application - Junior Software Developer - Abdullah Bin Masaud",
        "focus":   "Modular API design, 25+ pytest automated test cases, and low-level multithreaded network socket systems."
    },
    {
        "company": "Transworld Associates (Islamabad HQ)",
        "email":   "careers@tw1.com",
        "domain":  "TELECOM",
        "location": "Islamabad",
        "role":    "Graduate Trainee Network Engineer",
        "subject": "Job Application - Graduate Trainee Network Engineer - Abdullah Bin Masaud",
        "focus":   "TCP/IP custom client-server socket programming with CRC32 packet framing, and telecom network infrastructure."
    },
    {
        "company": "COMSATS Internet Services (Islamabad HQ)",
        "email":   "hr@comsats.net.pk",
        "domain":  "TELECOM",
        "location": "Islamabad",
        "role":    "Trainee Network & Systems Engineer",
        "subject": "Job Application - Network & Systems Engineer - Abdullah Bin Masaud",
        "focus":   "Network operations, TCP/IP socket communications, live telemetry streaming, and routing protocols."
    },
    {
        "company": "PakWheels (Lahore HQ)",
        "email":   "info@pakwheels.com",
        "domain":  "SOFTWARE",
        "location": "Lahore, Punjab",
        "role":    "Junior Software Engineer",
        "subject": "Job Application - Junior Software Engineer - Abdullah Bin Masaud",
        "focus":   "Backend web engineering, REST APIs with authentication, automated test suites, and data validation."
    },
    {
        "company": "InvoZone (Lahore HQ)",
        "email":   "info@invozone.com",
        "domain":  "SOFTWARE",
        "location": "Lahore, Punjab",
        "role":    "Junior Software Engineer",
        "subject": "Job Application - Junior Software Engineer - Abdullah Bin Masaud",
        "focus":   "Agile backend development, Flask RESTful microservices, and automated testing with pytest."
    },
    {
        "company": "Meezan Bank IT Directorate (National)",
        "email":   "info@meezanbank.com",
        "domain":  "SOFTWARE",
        "location": "National / Punjab",
        "role":    "Trainee IT & Software Engineer",
        "subject": "Job Application - Trainee IT & Software Engineer - Abdullah Bin Masaud",
        "focus":   "Financial data validation pipelines, statistical IQR anomaly detection, and secure REST API services."
    },
    {
        "company": "AUST - Abbottabad University of Science & Technology (Abbottabad, KPK)",
        "email":   "info@aust.edu.pk",
        "domain":  "HARDWARE",
        "location": "Abbottabad, KPK",
        "role":    "Lab Engineer / Computer Engineering Trainee",
        "subject": "Job Application - Lab Engineer (Computer Engineering) - Abdullah Bin Masaud",
        "focus":   "Embedded microcontroller firmware in C (PIC18/XC8), circuit design in Proteus, and digital systems labs."
    },
    {
        "company": "NUML - National University of Modern Languages (Islamabad)",
        "email":   "info@numl.edu.pk",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "Lab Engineer / Computing Trainee",
        "subject": "Job Application - Lab Engineer (Computer Science) - Abdullah Bin Masaud",
        "focus":   "CS laboratory instruction, Python and C programming, object-oriented design, and database systems."
    },
    {
        "company": "Quaid-i-Azam University (Islamabad)",
        "email":   "info@qau.edu.pk",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "Lab Engineer / Computer Systems Trainee",
        "subject": "Job Application - Lab Engineer (Computer Systems) - Abdullah Bin Masaud",
        "focus":   "Computer systems laboratory instruction, network protocols, automated testing, and software verification."
    },
    {
        "company": "Foundation University (Rawalpindi)",
        "email":   "info@fui.edu.pk",
        "domain":  "HARDWARE",
        "location": "Rawalpindi",
        "role":    "Lab Engineer / Embedded & Computing Trainee",
        "subject": "Job Application - Lab Engineer (Computer Engineering) - Abdullah Bin Masaud",
        "focus":   "Microcontroller laboratory hardware, register-level C programming, circuit design, and Proteus simulation."
    },
    {
        "company": "Superior University (Lahore)",
        "email":   "info@superior.edu.pk",
        "domain":  "SOFTWARE",
        "location": "Lahore, Punjab",
        "role":    "Lab Engineer / Software Trainee",
        "subject": "Job Application - Lab Engineer (Computer Science) - Abdullah Bin Masaud",
        "focus":   "Software engineering instruction, full-stack application development, and student project supervision."
    },
    {
        "company": "UMT - University of Management & Technology (Lahore)",
        "email":   "info@umt.edu.pk",
        "domain":  "SOFTWARE",
        "location": "Lahore, Punjab",
        "role":    "Lab Engineer / Computing Trainee",
        "subject": "Job Application - Lab Engineer (Computing & IT) - Abdullah Bin Masaud",
        "focus":   "Computing laboratory guidance, Python backend architectures, and machine learning fundamentals."
    },
    {
        "company": "Riphah International University (Islamabad / Rawalpindi)",
        "email":   "info@riphah.edu.pk",
        "domain":  "HARDWARE",
        "location": "Islamabad / Rawalpindi",
        "role":    "Lab Engineer / Computer Engineering Trainee",
        "subject": "Job Application - Lab Engineer (Computer Engineering) - Abdullah Bin Masaud",
        "focus":   "Digital logic design, embedded systems laboratories, microcontroller programming, and circuit simulation."
    },
    {
        "company": "SZABIST (Islamabad)",
        "email":   "info@szabist-isb.edu.pk",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "Lab Engineer / Software Trainee",
        "subject": "Job Application - Lab Engineer (Computer Science) - Abdullah Bin Masaud",
        "focus":   "Software testing, algorithms, REST API implementation, and practical student project assistance."
    },
    {
        "company": "Iqra University (Islamabad)",
        "email":   "info@iqra.edu.pk",
        "domain":  "SOFTWARE",
        "location": "Islamabad",
        "role":    "Lab Engineer / Computing Trainee",
        "subject": "Job Application - Lab Engineer (Computer Science) - Abdullah Bin Masaud",
        "focus":   "Practical laboratory sessions in programming fundamentals, data structures, and computer networking."
    },
    {
        "company": "GC University (Lahore)",
        "email":   "info@gcu.edu.pk",
        "domain":  "SOFTWARE",
        "location": "Lahore, Punjab",
        "role":    "Lab Engineer / Computer Science Trainee",
        "subject": "Job Application - Lab Engineer (Computer Science) - Abdullah Bin Masaud",
        "focus":   "Computer science laboratory instruction, low-level socket programming, and automated software validation."
    },
    {
        "company": "GC University (Faisalabad)",
        "email":   "info@gcuf.edu.pk",
        "domain":  "SOFTWARE",
        "location": "Faisalabad, Punjab",
        "role":    "Lab Engineer / IT & Computing Trainee",
        "subject": "Job Application - Lab Engineer (Computer Science & IT) - Abdullah Bin Masaud",
        "focus":   "Information technology lab management, network setup, Python programming, and technical problem solving."
    }
]

def make_email_body(company, role, location, focus):
    return f"""Dear Hiring Team,

I am writing to apply for the {role} position at {company} ({location}).

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), based in the region and immediately available.

Key Qualifications:
- Degree: BS Computer Engineering (2022-2026), COMSATS University Islamabad
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
    print("  AUTHENTIC DISPATCHER: PUNJAB, ISLAMABAD, PINDI & KPK")
    print("  Simple Subjects | Concise Bodies | Mapped 4 CVs")
    print(f"  Targets: {len(TARGETS)} verified companies & institutions")
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
            time.sleep(2)  # respectful delay between sends
        except Exception as e:
            log_application(company, email, domain, role, f"FAILED: {e}")
            print(f"      Status  : [FAIL] {e}")
            failed += 1
            
    print("\n" + "=" * 80)
    print(f"  BATCH COMPLETED: {sent} Sent | {failed} Failed")
    print("=" * 80)

if __name__ == "__main__":
    main()
