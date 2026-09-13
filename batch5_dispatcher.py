
import smtplib, ssl, datetime
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

APPLICANT = {
    "name":       "Abdullah Bin Masaud",
    "phone":      "+92 332 9076356",
    "university": "COMSATS University Islamabad, Abbottabad Campus",
    "degree":     "BS Computer Engineering (2022-2026)",
    "github":     "https://github.com/abdullah-bin-masaud",
    "linkedin":   "https://linkedin.com/in/abdullah-bin-masaud-59677335b",
}

# ── BATCH 5 — UAE/GULF + NSTP STARTUPS + MORE TOP COMPANIES ─────────────────
BATCH5 = [
    # ── UAE / GULF ──
    {"company": "Accenture Middle East",  "email": "careers@accenture.com",          "domain": "AI",       "role": "AI / Software Engineering Graduate (UAE)"},
    {"company": "Microsoft Gulf",         "email": "careers@microsoft.com",           "domain": "AI",       "role": "AI / Software Engineer Intern (Gulf)"},
    {"company": "IBM MEA",                "email": "careers@ibm.com",                 "domain": "SOFTWARE", "role": "Software Engineering Graduate Intern (MEA)"},
    {"company": "MBZUAI Abu Dhabi",       "email": "admissions@mbzuai.ac.ae",         "domain": "AI",       "role": "AI Research Internship (Abu Dhabi)"},
    {"company": "G42 Abu Dhabi",          "email": "talent@g42.ai",                   "domain": "AI",       "role": "AI / Machine Learning Engineer Intern"},
    {"company": "Careem (Dubai)",         "email": "careers@careem.com",              "domain": "SOFTWARE", "role": "Software Engineering Intern (Remote-friendly)"},
    {"company": "Noon.com",               "email": "talent@noon.com",                 "domain": "AI",       "role": "AI / Data Engineering Intern (UAE)"},

    # ── NSTP ISLAMABAD STARTUPS ──
    {"company": "Rapidev (NSTP)",         "email": "hr@rapidev.com",                  "domain": "SOFTWARE", "role": "Software Engineering Intern"},
    {"company": "Telerelation (NSTP)",    "email": "info@telerelation.com",           "domain": "TELECOM",  "role": "Telecom / VoIP Engineering Intern"},
    {"company": "Victreat (NSTP)",        "email": "hr@victreat.com",                 "domain": "AI",       "role": "AI / Healthtech Engineering Intern"},
    {"company": "NSTP Info",              "email": "info@nstp.pk",                    "domain": "SOFTWARE", "role": "Software / AI Engineering Intern"},

    # ── MORE HIGH-VALUE PAKISTAN ──
    {"company": "Meezan Bank (IT Div)",   "email": "hr@meezanbank.com",               "domain": "SOFTWARE", "role": "IT / Software Engineering Intern"},
    {"company": "HBL (Digital)",          "email": "careers@hbl.com",                 "domain": "SOFTWARE", "role": "Digital / Software Technology Intern"},
    {"company": "i2c Inc",                "email": "careers@i2cinc.com",              "domain": "SOFTWARE", "role": "Software Engineering Intern (Fintech)"},
    {"company": "Enablers",               "email": "hr@enablers.org",                 "domain": "SOFTWARE", "role": "Technology / Software Intern"},
    {"company": "Abacus Consulting",      "email": "careers@abacus.com.pk",           "domain": "SOFTWARE", "role": "Software / IT Consulting Intern"},
    {"company": "TPS Pakistan",           "email": "careers@tpspk.com",              "domain": "SOFTWARE", "role": "Software / Payments Engineering Intern"},
    {"company": "MTBC Pakistan",          "email": "careers@mtbc.com",               "domain": "SOFTWARE", "role": "Software Engineering Intern"},
    {"company": "Netsol Fintech",         "email": "fintech.careers@netsoltech.com",  "domain": "SOFTWARE", "role": "Fintech Software Engineering Intern"},
    {"company": "PakWheels",              "email": "careers@pakwheels.com",           "domain": "AI",       "role": "AI / Software Engineering Intern"},
]

BODY_TEMPLATES = {
    "AI": """Dear Hiring Team,

I am Abdullah Bin Masaud, a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), writing to apply for the {role} position at {company}.

I specialize in AI, Computer Vision, and Machine Learning. My project portfolio includes:
- VisionAid: Real-time assistive object detection system (YOLOv8 + Raspberry Pi 4)
- AI Medical Image Segmentation: U-Net tumor detection with 91%+ accuracy
- Traffic & Pedestrian Vehicle Counter: Multi-class YOLOv8 production pipeline
- Customer Churn Engine: XGBoost + SHAP for explainable predictions

All live on GitHub: {github}
LinkedIn: {linkedin}

I am immediately available for internship or graduate roles, on-site or remote. Please find my tailored CV attached.

Best regards,
{name}
{phone} | {university} | {degree}""",

    "HARDWARE": """Dear Hiring Team,

I am Abdullah Bin Masaud, a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), applying for the {role} position at {company}.

My embedded systems and hardware engineering portfolio:
- PIC18F4550 firmware (C/XC8): UART, SPI, I2C, EEPROM, interrupt-driven ISRs
- RFID Automated Attendance System (Proteus simulation + real PCB logic)
- Microcontroller Sensor Control & Alert Circuits (hands-on build)
- Real-time hardware-to-dashboard telemetry bridge (Flask + SocketIO)

GitHub: {github} | LinkedIn: {linkedin}

Immediately available. Tailored CV (Embedded/Hardware) is attached.

Best regards,
{name}
{phone} | {university} | {degree}""",

    "TELECOM": """Dear Hiring Team,

I am Abdullah Bin Masaud, a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), applying for the {role} position at {company}.

My telecom and networking engineering background:
- Custom TCP/IP socket protocol (multithreaded server + CRC32 error detection)
- Real-time telemetry streaming over Socket.IO (MQTT-style architecture)
- PIC18 UART serial communication protocol design and testing
- Signal processing and RF fundamentals (coursework + lab-verified)

GitHub: {github} | LinkedIn: {linkedin}

Immediately available. Telecom-focused CV is attached.

Best regards,
{name}
{phone} | {university} | {degree}""",

    "SOFTWARE": """Dear Hiring Team,

I am Abdullah Bin Masaud, a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), applying for the {role} position at {company}.

My software engineering and QA portfolio:
- Flask REST API: Full CRUD endpoints with pytest test suite and Swagger docs
- Python Data QA Pipeline: Automated validation, anomaly detection, HTML reports
- TCP/IP Client-Server: CRC32 error detection + concurrent load testing (50 threads)
- All projects: publicly documented on GitHub with clean code and READMEs

GitHub: {github} | LinkedIn: {linkedin}

Immediately available on-site or remote. Software-focused CV is attached.

Best regards,
{name}
{phone} | {university} | {degree}""",
}

def send_email(to_email, subject, body_text, cv_path):
    msg = MIMEMultipart()
    msg["From"]    = SENDER_EMAIL
    msg["To"]      = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body_text, "plain"))
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
    print("=" * 65)
    print("  BATCH 5 -- UAE/GULF + NSTP STARTUPS + BANKING TECH + MORE")
    print(f"  Targets: {len(BATCH5)} companies")
    print("=" * 65)
    sent = failed = 0
    for i, job in enumerate(BATCH5, 1):
        company, email, domain, role = job["company"], job["email"], job["domain"], job["role"]
        cv_path = CV_MAP[domain]
        subject = f"Application for {role} - Abdullah Bin Masaud - BS Computer Engineering (COMSATS 2026)"
        body = BODY_TEMPLATES[domain].format(
            company=company, role=role,
            name=APPLICANT["name"], phone=APPLICANT["phone"],
            university=APPLICANT["university"], degree=APPLICANT["degree"],
            github=APPLICANT["github"], linkedin=APPLICANT["linkedin"],
        )
        print(f"\n[{i:02d}/{len(BATCH5)}] {company}")
        print(f"      To     : {email}")
        print(f"      CV     : {cv_path.name}  |  {domain}")
        try:
            send_email(email, subject, body, cv_path)
            log_application(company, email, domain, role, "SENT")
            print(f"      Status : [OK] SENT")
            sent += 1
        except Exception as e:
            log_application(company, email, domain, role, f"FAILED: {e}")
            print(f"      Status : [FAIL] {e}")
            failed += 1
    print("\n" + "=" * 65)
    print(f"  BATCH 5 COMPLETE  |  Sent: {sent}  |  Failed: {failed}")
    print(f"  Running total: ~{63 + sent} total applications sent today")
    print("=" * 65)

if __name__ == "__main__":
    main()
