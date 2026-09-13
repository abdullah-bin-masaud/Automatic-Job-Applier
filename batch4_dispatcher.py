
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

# ── BATCH 4 — FINTECH, HEALTHTECH, STARTUPS, MORE HOUSES ────────────────────
BATCH4 = [
    # ── FINTECH ──
    {"company": "Finja",              "email": "careers@finja.pk",             "domain": "SOFTWARE", "role": "Software Engineering Intern (Fintech)"},
    {"company": "Ailaaj",             "email": "careers@ailaaj.com",           "domain": "AI",       "role": "AI / Data Engineering Intern (Healthtech)"},
    {"company": "Dukan.pk",           "email": "hr@dukan.pk",                  "domain": "SOFTWARE", "role": "Software Engineering Intern"},
    {"company": "NayaPay",            "email": "careers@nayapay.com",          "domain": "SOFTWARE", "role": "Software / Backend Engineering Intern"},
    {"company": "Tez Financial",      "email": "careers@tezfinancial.com",     "domain": "SOFTWARE", "role": "Software Engineering Intern"},
    {"company": "SadaPay",            "email": "jobs@sadapay.com",             "domain": "SOFTWARE", "role": "Software Engineering Intern"},

    # ── MORE SOFTWARE HOUSES ──
    {"company": "PureLogics",         "email": "hr@purelogics.net",            "domain": "SOFTWARE", "role": "Software / QA Engineering Intern"},
    {"company": "Ciklum Pakistan",    "email": "careers@ciklum.com",           "domain": "SOFTWARE", "role": "Software Engineering Intern"},
    {"company": "Motive (KeepTruckin)","email":"engineering@motive.com",       "domain": "AI",       "role": "AI / ML Engineering Intern (Remote)"},
    {"company": "Keen",               "email": "hr@keen.com.pk",               "domain": "AI",       "role": "AI Engineering Intern"},
    {"company": "Incumbent",          "email": "careers@incumbent.com.pk",     "domain": "SOFTWARE", "role": "Software Engineering Intern"},
    {"company": "e4 Technologies",    "email": "hr@e4technologies.pk",         "domain": "HARDWARE", "role": "IoT / Embedded Systems Intern"},

    # ── R&D / LABS ──
    {"company": "ITU Lahore",         "email": "careers@itu.edu.pk",           "domain": "AI",       "role": "AI Research Intern"},
    {"company": "LUMS CS Dept",       "email": "research@lums.edu.pk",         "domain": "AI",       "role": "AI / ML Research Intern"},
    {"company": "COMSATS Research",   "email": "research@comsats.edu.pk",      "domain": "AI",       "role": "AI / Computer Vision Research Intern"},

    # ── INTERNATIONAL REMOTE ──
    {"company": "Deel (Remote)",      "email": "apply@deel.com",               "domain": "SOFTWARE", "role": "Software Engineering Intern (Remote)"},
    {"company": "Remotebase",         "email": "apply@remotebase.com",         "domain": "SOFTWARE", "role": "Software Engineer (Remote-Pakistan)"},
    {"company": "Invisible Tech",     "email": "apply@inv.tech",               "domain": "AI",       "role": "AI Operations Engineer (Remote)"},
]

BODY_TEMPLATES = {
    "AI": """Dear Hiring Team,

I am Abdullah Bin Masaud, a final-year Computer Engineering student at COMSATS University Islamabad, Abbottabad Campus (graduating 2026). I am writing to apply for the {role} position at {company}.

I specialize in AI, Machine Learning, and Computer Vision with the following portfolio:
- VisionAid — real-time object detection for visually impaired users (YOLOv8 + Raspberry Pi)
- AI Medical Image Segmentation — U-Net tumor detection model
- Traffic & Pedestrian Vehicle Counter — YOLOv8 multi-class production pipeline
- Customer Churn Predictive Engine — XGBoost + SHAP interpretability

GitHub  : {github}
LinkedIn: {linkedin}

I am available immediately, on-site or remote. My CV is attached.

Sincerely,
{name} | {phone}
{university} | {degree}""",

    "HARDWARE": """Dear Hiring Team,

I am Abdullah Bin Masaud, a final-year Computer Engineering student at COMSATS University Islamabad, Abbottabad Campus (graduating 2026). I am applying for the {role} position at {company}.

My embedded & IoT engineering expertise:
- PIC18F4550 firmware (C/XC8) with UART, SPI, I2C, EEPROM, interrupt-driven ISRs
- RFID-based automated attendance system with Proteus simulation
- Microcontroller sensor control & alert circuits (real hardware)
- Real-time hardware-to-cloud telemetry bridge using Flask + SocketIO

GitHub  : {github}
LinkedIn: {linkedin}

My CV (tailored for embedded/hardware roles) is attached. I am available immediately.

Sincerely,
{name} | {phone}
{university} | {degree}""",

    "TELECOM": """Dear Hiring Team,

I am Abdullah Bin Masaud, a final-year Computer Engineering student at COMSATS University Islamabad, Abbottabad Campus (graduating 2026). I am applying for the {role} position at {company}.

My telecom & networking background:
- Custom TCP/IP socket server (multithreaded, CRC32 error detection, load testing)
- Real-time sensor telemetry streaming (Socket.IO / MQTT-style)
- UART-based serial communication protocol design on PIC18
- Signal processing and RF fundamentals (coursework + hands-on lab)

GitHub  : {github}
LinkedIn: {linkedin}

CV attached. Available immediately.

Sincerely,
{name} | {phone}
{university} | {degree}""",

    "SOFTWARE": """Dear Hiring Team,

I am Abdullah Bin Masaud, a final-year Computer Engineering student at COMSATS University Islamabad, Abbottabad Campus (graduating 2026). I am writing to apply for the {role} position at {company}.

My software engineering & QA portfolio:
- Flask REST API with full pytest test suite and API documentation
- Python Data QA Pipeline — automated validation, anomaly detection, reporting
- TCP/IP client-server with CRC32 error detection and load testing
- All projects publicly available and documented on GitHub

GitHub  : {github}
LinkedIn: {linkedin}

I am immediately available for internship (on-site or remote). CV attached.

Sincerely,
{name} | {phone}
{university} | {degree}""",
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
    return True

def log_application(company, email, domain, role, status):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    TRACKER_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(TRACKER_PATH, "a", encoding="utf-8") as f:
        f.write(f"{timestamp},{company},{email},{domain},{role},{status}\n")

def main():
    print("=" * 65)
    print("  BATCH 4 — FINTECH / HEALTHTECH / STARTUPS / INTERNATIONAL")
    print(f"  Targets: {len(BATCH4)} companies")
    print("=" * 65)
    sent = failed = 0
    for i, job in enumerate(BATCH4, 1):
        company, email, domain, role = job["company"], job["email"], job["domain"], job["role"]
        cv_path = CV_MAP[domain]
        subject = f"Application for {role} - Abdullah Bin Masaud - BS Computer Engineering (COMSATS 2026)"
        body = BODY_TEMPLATES[domain].format(
            company=company, role=role,
            name=APPLICANT["name"], phone=APPLICANT["phone"],
            university=APPLICANT["university"], degree=APPLICANT["degree"],
            github=APPLICANT["github"], linkedin=APPLICANT["linkedin"],
        )
        print(f"\n[{i:02d}/{len(BATCH4)}] {company}")
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
    print(f"  BATCH 4 COMPLETE  |  Sent: {sent}  |  Failed: {failed}")
    print(f"  Running total: ~{45 + sent} total applications sent")
    print("=" * 65)

if __name__ == "__main__":
    main()
