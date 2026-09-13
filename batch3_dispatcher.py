
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

# ── BATCH 3 — HIGH-CALLBACK / RECENTLY ACTIVE ──────────────────────────────
BATCH3 = [
    # ── RECENTLY ACTIVE LOCAL STARTUPS (fastest callbacks) ──
    {"company": "Genifem Technology",      "email": "hr@genifem.com",                  "domain": "SOFTWARE", "role": "Software / AI Automation Intern",         "why": "Recently posted on Rozee.pk Sep 2026"},
    {"company": "Signatics Pvt Ltd",       "email": "hr@signatics.com",                "domain": "HARDWARE", "role": "Embedded / Hardware Design Intern",        "why": "Active embedded hiring Islamabad"},
    {"company": "Zatnav",                  "email": "hr@zatnav.com",                   "domain": "HARDWARE", "role": "Embedded Systems Engineering Intern",      "why": "Recently advertised embedded roles"},
    {"company": "Cross Analytics",         "email": "info@crossanalytics.com.pk",      "domain": "HARDWARE", "role": "Embedded Systems Intern",                  "why": "Active Islamabad embedded internship"},
    {"company": "MRS Electronic Pakistan", "email": "careers.pk@mrs-electronic.com",   "domain": "HARDWARE", "role": "Electronics / Embedded Engineering Intern", "why": "Posted via LinkedIn recently"},
    {"company": "Xgrid",                   "email": "careers@xgrid.co",               "domain": "AI",       "role": "AI / Cloud Engineering Intern",            "why": "Active remote-friendly Lahore startup"},
    {"company": "Tkxel",                   "email": "careers@tkxel.com",              "domain": "SOFTWARE", "role": "Software Engineering Intern",              "why": "Active hiring, Lahore+remote"},
    {"company": "Turing",                  "email": "apply@turing.com",               "domain": "AI",       "role": "AI / ML Remote Engineering Intern",        "why": "Global remote platform, high acceptance"},
    {"company": "Kalsym Technologies",     "email": "hr@kalsym.com",                  "domain": "SOFTWARE", "role": "Software Engineering Intern",              "why": "Active Pakistan software house"},

    # ── MULTINATIONALS IN PAKISTAN (high prestige, structured programs) ──
    {"company": "Unilever Pakistan",       "email": "careers.pk@unilever.com",         "domain": "SOFTWARE", "role": "Technology / Digital Intern",              "why": "Structured early-careers program"},
    {"company": "Nestle Pakistan",         "email": "hr.pakistan@nestle.com",          "domain": "AI",       "role": "Digital / AI Intern",                      "why": "Structured internship program"},
    {"company": "Honeywell Pakistan",      "email": "careers@honeywell.com",           "domain": "HARDWARE", "role": "Engineering / Embedded Systems Intern",    "why": "Multinational embedded roles"},
    {"company": "Huawei Pakistan",         "email": "careers.pk@huawei.com",           "domain": "TELECOM",  "role": "Telecom / Network Engineering Intern",     "why": "Telecom giant, Pakistan office"},
    {"company": "Ericsson Pakistan",       "email": "recruitment.pk@ericsson.com",     "domain": "TELECOM",  "role": "Telecom Network Engineering Intern",       "why": "Major telecom infrastructure company"},
    {"company": "Nokia Pakistan",          "email": "careers.pk@nokia.com",            "domain": "TELECOM",  "role": "Network / Telecom Engineering Intern",     "why": "Global telecom, Pakistan active"},

    # ── DEFENCE / AEROSPACE / RESEARCH (unique edge) ──
    {"company": "NASTP Islamabad",         "email": "careers@nastp.gov.pk",            "domain": "HARDWARE", "role": "Embedded / AI Research Intern",            "why": "Active embedded + AI research hiring"},
    {"company": "NUST SEECS",              "email": "seecs@nust.edu.pk",              "domain": "AI",       "role": "AI Research / Lab Intern",                 "why": "Top research lab, CS/AI focus"},
    {"company": "PCSIR Islamabad",         "email": "info@pcsir.gov.pk",              "domain": "HARDWARE", "role": "Electronics Research Intern",              "why": "Government R&D, strong callback"},

    # ── INTERNATIONAL REMOTE (broadens reach) ──
    {"company": "Toptal (Network)",        "email": "apply@toptal.com",               "domain": "AI",       "role": "AI / ML Engineer (Remote)",                "why": "Global top-talent network"},
    {"company": "Andela",                  "email": "talent@andela.com",              "domain": "SOFTWARE", "role": "Software Engineer (Remote Emerging Market)", "why": "Hires remote devs from emerging markets"},
]

BODY_TEMPLATES = {
    "AI": """Dear Hiring Team,

I am Abdullah Bin Masaud, a final-year Computer Engineering student at COMSATS University Islamabad, Abbottabad Campus (graduating 2026), writing to express my strong interest in the {role} position at {company}.

My core focus areas are Artificial Intelligence, Machine Learning, and Computer Vision. I have hands-on experience with:
- Real-time object detection (YOLOv8) — VisionAid project for visually impaired users
- Medical image segmentation (U-Net) for tumor detection
- Traffic & Pedestrian counter with multi-class classification
- Customer Churn prediction engine (XGBoost + SHAP)

All projects are publicly available on my GitHub:
GitHub  : {github}
LinkedIn: {linkedin}

I am available immediately for an internship, either on-site or remote. My CV is attached for your consideration.

Thank you for your time, and I look forward to the opportunity to contribute to {company}.

Sincerely,
{name}
{phone}
{university} | {degree}""",

    "HARDWARE": """Dear Hiring Team,

I am Abdullah Bin Masaud, a final-year Computer Engineering student at COMSATS University Islamabad, Abbottabad Campus (graduating 2026), writing to apply for the {role} position at {company}.

My embedded systems and hardware engineering experience includes:
- PIC18F4550 firmware in C/XC8 (UART, EEPROM, interrupts)
- RFID-based automated attendance system (Proteus-simulated)
- Microcontroller sensor control & alert circuits
- Real-time hardware-software telemetry bridge (Flask + sensors)

GitHub  : {github}
LinkedIn: {linkedin}

I am ready to contribute to {company}'s engineering team immediately. My tailored CV is attached.

Sincerely,
{name}
{phone}
{university} | {degree}""",

    "TELECOM": """Dear Hiring Team,

I am Abdullah Bin Masaud, a final-year Computer Engineering student at COMSATS University Islamabad, Abbottabad Campus (graduating 2026), applying for the {role} position at {company}.

My telecommunications and networking background includes:
- Custom TCP/IP socket programming (multithreaded server, CRC32 error detection)
- Real-time sensor telemetry streaming (MQTT-style over Flask-SocketIO)
- Signal processing and RF fundamentals (coursework + lab)
- PIC18 UART-based serial communication protocol design

GitHub  : {github}
LinkedIn: {linkedin}

I am highly motivated to join {company}'s network engineering team. My CV is attached.

Sincerely,
{name}
{phone}
{university} | {degree}""",

    "SOFTWARE": """Dear Hiring Team,

I am Abdullah Bin Masaud, a final-year Computer Engineering student at COMSATS University Islamabad, Abbottabad Campus (graduating 2026), applying for the {role} position at {company}.

My software engineering and QA background includes:
- REST API development with Flask + comprehensive pytest suite
- Automated data quality validation pipeline in Python
- Full-stack TCP/IP client-server system with error detection
- CI/CD-ready project structures (GitHub public repositories)

GitHub  : {github}
LinkedIn: {linkedin}

I am eager to bring my skills to {company}. My CV is attached for your review.

Sincerely,
{name}
{phone}
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
    print("  BATCH 3 — HIGH CALLBACK / RECENTLY ACTIVE COMPANIES")
    print(f"  Targets: {len(BATCH3)} companies")
    print("=" * 65)
    sent = failed = 0
    for i, job in enumerate(BATCH3, 1):
        company, email, domain, role = job["company"], job["email"], job["domain"], job["role"]
        cv_path = CV_MAP[domain]
        subject = f"Application for {role} - Abdullah Bin Masaud - BS Computer Engineering (COMSATS 2026)"
        body = BODY_TEMPLATES[domain].format(
            company=company, role=role,
            name=APPLICANT["name"], phone=APPLICANT["phone"],
            university=APPLICANT["university"], degree=APPLICANT["degree"],
            github=APPLICANT["github"], linkedin=APPLICANT["linkedin"],
        )
        print(f"\n[{i:02d}/{len(BATCH3)}] {company}")
        print(f"      To     : {email}")
        print(f"      CV     : {cv_path.name}  |  {domain}")
        print(f"      Reason : {job['why']}")
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
    print(f"  BATCH 3 COMPLETE  |  Sent: {sent}  |  Failed: {failed}")
    print(f"  Running total: ~{25 + sent} applications sent")
    print("=" * 65)

if __name__ == "__main__":
    main()
