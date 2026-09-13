
import smtplib
import ssl
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path
import datetime

# ─── CONFIG ───────────────────────────────────────────────────────────────────
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

APPLICANT = {
    "name":       "Abdullah Bin Masaud",
    "phone":      "+92 332 9076356",
    "university": "COMSATS University Islamabad, Abbottabad Campus",
    "degree":     "BS Computer Engineering (2022-2026)",
    "github":     "https://github.com/abdullah-bin-masaud",
    "linkedin":   "https://linkedin.com/in/abdullah-bin-masaud-59677335b",
}

# ─── BATCH 2 – 15 NEW COMPANIES ───────────────────────────────────────────────
# (none of these were in batch 1)
BATCH2 = [
    # AI / ML
    {"company": "Folio3 AI",           "email": "careers@folio3.com",           "domain": "AI",       "role": "AI / Machine Learning Intern"},
    {"company": "Xord",                "email": "hr@xord.com",                   "domain": "AI",       "role": "AI / ML Engineering Intern"},
    {"company": "10Pearls",            "email": "careers@10pearls.com",          "domain": "AI",       "role": "AI/Data Science Intern"},
    {"company": "Confiz",              "email": "careers@confiz.com",            "domain": "AI",       "role": "AI / Computer Vision Intern"},

    # HARDWARE / EMBEDDED
    {"company": "Renzym Pvt Ltd",      "email": "info@renzym.com",              "domain": "HARDWARE", "role": "Embedded Systems Engineering Intern"},
    {"company": "RISETech",            "email": "hr@risetech.ai",               "domain": "HARDWARE", "role": "Embedded Software Engineering Intern"},
    {"company": "Beyond Intellect",    "email": "info@beyondintellect.com",      "domain": "HARDWARE", "role": "Embedded / PCB Design Intern"},
    {"company": "Pak Detector Tech",   "email": "careers@pakdetector.com",       "domain": "HARDWARE", "role": "Microcontroller / Firmware Intern"},

    # TELECOM
    {"company": "Jazz (Veon)",         "email": "careers@jazz.com.pk",          "domain": "TELECOM",  "role": "Telecom / Network Engineering Intern"},
    {"company": "Zong CMPak",          "email": "hr@zong.com.pk",               "domain": "TELECOM",  "role": "Telecom Engineering Intern"},
    {"company": "Telenor Pakistan",    "email": "recruitment@telenor.com.pk",   "domain": "TELECOM",  "role": "Network / Telecom Intern"},
    {"company": "PTCL",                "email": "hrd@ptcl.net.pk",              "domain": "TELECOM",  "role": "Telecom Engineering Intern"},

    # SOFTWARE / QA
    {"company": "NetSol Technologies", "email": "careers@netsoltech.com",       "domain": "SOFTWARE", "role": "Software Engineering Intern"},
    {"company": "VentureDive",         "email": "hr@venturedive.com",           "domain": "SOFTWARE", "role": "Software / QA Engineering Intern"},
    {"company": "Techlogix",           "email": "careers@techlogix.com",        "domain": "SOFTWARE", "role": "Software Engineering / QA Intern"},
]

# ─── EMAIL BODY TEMPLATES ─────────────────────────────────────────────────────
BODY_TEMPLATES = {
    "AI": """Dear Hiring Team,

I am Abdullah Bin Masaud, a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), writing to apply for the {role} position at {company}.

My focus areas include Computer Vision, Machine Learning, and AI systems. Key projects:
  - VisionAid: Real-time object detection system for visually impaired users (YOLO + Raspberry Pi)
  - AI Medical Image Segmentation: U-Net based tumor detection
  - Traffic & Pedestrian Counter: YOLOv8 multi-class detection pipeline
  - Customer Churn Predictive Engine: XGBoost + SHAP explanations

GitHub: {github}
LinkedIn: {linkedin}

I am eager to contribute to {company}'s AI/ML initiatives. My CV is attached for your review.

Best regards,
{name}
{phone}
{university} | {degree}""",

    "HARDWARE": """Dear Hiring Team,

I am Abdullah Bin Masaud, a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), writing to apply for the {role} position at {company}.

My embedded systems expertise includes PIC18 firmware (C/XC8), UART, SPI, I2C protocols, Proteus simulation, PCB design fundamentals, and real-time sensor integration. Key projects:
  - PIC18F4550 Signal Communication Unit (UART + EEPROM logging)
  - Microcontroller Sensor Control & Alert Circuits
  - PIC18 Automated RFID Attendance System
  - Realtime Video-Sensor Dashboard (hardware-software bridge)

GitHub: {github}
LinkedIn: {linkedin}

I am highly motivated to bring my embedded systems skills to {company}. My CV is attached.

Best regards,
{name}
{phone}
{university} | {degree}""",

    "TELECOM": """Dear Hiring Team,

I am Abdullah Bin Masaud, a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), writing to apply for the {role} position at {company}.

My telecommunications and networking background covers TCP/IP socket programming, network protocol analysis, signal processing, and RF communications fundamentals. Key projects:
  - Custom TCP/IP Client-Server with CRC32 error detection
  - Realtime Video + Sensor Telemetry Streaming Dashboard
  - PIC18 Signal Communication Unit (UART-based)

GitHub: {github}
LinkedIn: {linkedin}

I would be thrilled to contribute to {company}'s network and telecom operations. My CV is attached.

Best regards,
{name}
{phone}
{university} | {degree}""",

    "SOFTWARE": """Dear Hiring Team,

I am Abdullah Bin Masaud, a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), writing to apply for the {role} position at {company}.

My software engineering and QA background includes REST API development (Flask), automated test pipelines, data quality validation, and agile practices. Key projects:
  - Flask REST API with comprehensive pytest test suite
  - Python Data QA Pipeline (automated data validation)
  - TCP/IP Client-Server with error detection

GitHub: {github}
LinkedIn: {linkedin}

I am eager to support {company}'s software engineering and quality goals. My CV is attached.

Best regards,
{name}
{phone}
{university} | {degree}""",
}

# ─── SEND ONE EMAIL ───────────────────────────────────────────────────────────
def send_email(to_email, subject, body_text, cv_path):
    msg = MIMEMultipart()
    msg["From"]    = SENDER_EMAIL
    msg["To"]      = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body_text, "plain"))

    # Attach CV
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
    return True

# ─── LOG TO TRACKER ───────────────────────────────────────────────────────────
def log_application(company, email, domain, role, status):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"{timestamp},{company},{email},{domain},{role},{status}\n"
    TRACKER_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(TRACKER_PATH, "a", encoding="utf-8") as f:
        f.write(line)

# ─── MAIN ─────────────────────────────────────────────────────────────────────
def main():
    print("=" * 60)
    print("  BATCH 2 - AUTO JOB APPLICATION DISPATCHER")
    print(f"  Sending {len(BATCH2)} applications...")
    print("=" * 60)

    sent = 0
    failed = 0

    for i, job in enumerate(BATCH2, 1):
        company = job["company"]
        email   = job["email"]
        domain  = job["domain"]
        role    = job["role"]
        cv_path = CV_MAP[domain]

        subject = f"Application for {role} - Abdullah Bin Masaud - BS Computer Engineering (COMSATS)"
        body    = BODY_TEMPLATES[domain].format(
            company=company, role=role,
            name=APPLICANT["name"], phone=APPLICANT["phone"],
            university=APPLICANT["university"], degree=APPLICANT["degree"],
            github=APPLICANT["github"], linkedin=APPLICANT["linkedin"],
        )

        print(f"\n[{i:02d}/{len(BATCH2)}] {company}")
        print(f"      To      : {email}")
        print(f"      CV      : {cv_path.name}")
        print(f"      Domain  : {domain}")

        try:
            send_email(email, subject, body, cv_path)
            log_application(company, email, domain, role, "SENT")
            print(f"      Status  : [OK] SENT")
            sent += 1
        except Exception as e:
            log_application(company, email, domain, role, f"FAILED: {e}")
            print(f"      Status  : [FAIL] {e}")
            failed += 1

    print("\n" + "=" * 60)
    print(f"  BATCH 2 COMPLETE  |  Sent: {sent}  |  Failed: {failed}")
    print(f"  Logged to: {TRACKER_PATH}")
    print("=" * 60)

if __name__ == "__main__":
    main()
