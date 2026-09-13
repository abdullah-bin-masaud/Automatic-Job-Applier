import os
from pathlib import Path

BASE_DIR = Path(r"C:\Users\Lenovo\Desktop\Projects\Automated-Job-Applier")
BASE_DIR.mkdir(parents=True, exist_ok=True)
(BASE_DIR / "drafts").mkdir(parents=True, exist_ok=True)

CV_MATCHER_PY = '''"""
Semantic CV Matcher & Classifier Brain.
Analyzes job titles and descriptions to score against your 4 specialized CVs
and selects the optimal resume and GitHub project portfolio links.
"""
from pathlib import Path

CV_DIR = Path(r"C:\\Users\\Lenovo\\Desktop\\CVV'S")

DOMAIN_PROFILES = {
    "AI_ML_VISION": {
        "cv_file": "CV__A.pdf",
        "domain_name": "Artificial Intelligence & Computer Vision",
        "keywords": [
            "python", "yolo", "opencv", "computer vision", "machine learning", "deep learning",
            "pytorch", "tensorflow", "cnn", "u-net", "onnx", "segmentation", "object detection",
            "ai engineer", "data science", "nlp", "llm", "image processing", "scikit-learn"
        ],
        "github_projects": [
            {"name": "VisionAid (FYP)", "url": "https://github.com/abdullah-bin-masaud/VisionAid", "desc": "Wearable edge AI navigation headset using YOLO and ONNX on Raspberry Pi 4B"},
            {"name": "AI Medical Image Segmentation", "url": "https://github.com/abdullah-bin-masaud/AI-Medical-Image-Segmentation", "desc": "PyTorch U-Net for brain MRI lesion detection with Dice & IoU metrics"},
            {"name": "Traffic & Pedestrian Analytics Counter", "url": "https://github.com/abdullah-bin-masaud/Traffic-Pedestrian-Vehicle-Counter", "desc": "Real-time OpenCV centroid tracker & tripwire line crossing analytics"}
        ]
    },
    "TELECOM_NETWORKS": {
        "cv_file": "CV__T.pdf",
        "domain_name": "Telecommunications & Network Engineering",
        "keywords": [
            "telecom", "network", "tcp/ip", "socket", "routing", "switching", "wireshark",
            "protocols", "uart", "packet", "osi model", "cisco", "telemetry", "wireless",
            "lan", "wan", "ethernet", "latency", "dns", "dhcp", "bandwidth"
        ],
        "github_projects": [
            {"name": "TCP/IP Client-Server Network System", "url": "https://github.com/abdullah-bin-masaud/TCP-IP-Client-Server", "desc": "Multithreaded socket server with custom 12-byte framing and CRC32 error detection"},
            {"name": "Real-Time Video Sensor Streaming Dashboard", "url": "https://github.com/abdullah-bin-masaud/Realtime-Video-Sensor-Dashboard", "desc": "Low-latency MJPEG video and WebSocket telemetry streaming cockpit"},
            {"name": "PIC18 Signal Communication Unit", "url": "https://github.com/abdullah-bin-masaud/PIC18-Signal-Communication-Unit", "desc": "Hardware pulse capture with EEPROM logging and 9600-baud UART telemetry"}
        ]
    },
    "EMBEDDED_HARDWARE": {
        "cv_file": "CV__H.pdf",
        "domain_name": "Embedded Systems & Hardware Engineering",
        "keywords": [
            "embedded", "embedded c", "microcontroller", "pic18", "firmware", "proteus",
            "mplab", "hardware", "iot", "raspberry pi", "sensors", "eeprom", "interrupt",
            "schematic", "pcb", "spi", "i2c", "adc", "actuator", "transistor", "c/c++"
        ],
        "github_projects": [
            {"name": "PIC18 Automated Attendance Gate", "url": "https://github.com/abdullah-bin-masaud/PIC18-Automated-Attendance-System", "desc": "Bi-directional optical IR beam door gate with EEPROM headcount logging"},
            {"name": "PIC18 Signal Communication Unit", "url": "https://github.com/abdullah-bin-masaud/PIC18-Signal-Communication-Unit", "desc": "Interrupt-driven pulse acquisition and non-volatile memory telemetry logging"},
            {"name": "Microcontroller Sensor Control & Alert Circuits", "url": "https://github.com/abdullah-bin-masaud/Microcontroller-Sensor-Control-Alert-Circuits", "desc": "Suite of 3 circuits: water level indicator, LDR street light with hysteresis, fire alert"}
        ]
    },
    "SOFTWARE_QA": {
        "cv_file": "CV__S.pdf",
        "domain_name": "Software Engineering & Quality Assurance (QA)",
        "keywords": [
            "qa", "quality assurance", "testing", "pytest", "test automation", "rest api",
            "flask", "validation", "sql", "mysql", "data validation", "regression",
            "sdlc", "bug", "jira", "unit test", "integration test", "backend", "developer"
        ],
        "github_projects": [
            {"name": "Flask REST API Quality Validation Suite", "url": "https://github.com/abdullah-bin-masaud/Flask-REST-API-Testing", "desc": "25+ pytest test cases verifying HTTP contracts, schemas, concurrency, and <150ms latency"},
            {"name": "Automated Data Validation & QA Pipeline", "url": "https://github.com/abdullah-bin-masaud/Python-Data-QA-Pipeline", "desc": "Pandas data quality auditor with IQR outlier detection and ML regression checks"},
            {"name": "Full-Stack Rent-a-Car Platform", "url": "https://github.com/abdullah-bin-masaud/BCE-Projects", "desc": "Relational MySQL database and PHP backend with session auth and validation"}
        ]
    }
}


def classify_job(job_title: str, job_description: str) -> dict:
    """
    Evaluates text against the 4 domain lexicons and returns the winning CV recommendation.
    """
    text = (job_title + " " + job_description).lower()
    scores = {}

    for domain_key, profile in DOMAIN_PROFILES.items():
        score = 0
        matched = []
        for kw in profile["keywords"]:
            if kw in text:
                score += (3 if kw in job_title.lower() else 1)
                matched.append(kw)
        scores[domain_key] = {"score": score, "matched": matched}

    winning_domain = max(scores.keys(), key=lambda k: scores[k]["score"])
    winner_profile = DOMAIN_PROFILES[winning_domain]
    winning_cv_path = CV_DIR / winner_profile["cv_file"]

    return {
        "domain_key": winning_domain,
        "domain_name": winner_profile["domain_name"],
        "cv_file_name": winner_profile["cv_file"],
        "cv_full_path": str(winning_cv_path),
        "score": scores[winning_domain]["score"],
        "matched_keywords": scores[winning_domain]["matched"],
        "github_projects": winner_profile["github_projects"],
        "all_scores": {k: v["score"] for k, v in scores.items()}
    }
'''

EMAIL_GENERATOR_PY = '''"""
Tailored Email Application Generator.
Generates personalized outreach emails and creates ready-to-send .eml draft files
complete with attached matching CV and clickable GitHub project showcases.
"""
from pathlib import Path
from email.message import EmailMessage
import mimetypes

CANDIDATE_NAME = "Abdullah Bin Masaud"
CANDIDATE_PHONE = "+92 332 9076356"
CANDIDATE_EMAIL = "abdullahmasaud10@gmail.com"
CANDIDATE_LINKEDIN = "https://linkedin.com/in/abdullah-bin-masaud-59677335b"
CANDIDATE_GITHUB = "https://github.com/abdullah-bin-masaud"


def generate_email_draft(company_name: str, job_title: str, recipient_email: str, match_result: dict, output_dir: Path) -> Path:
    """Generates an RFC-822 .eml draft file with tailored body and attached CV."""
    msg = EmailMessage()
    msg["From"] = f"{CANDIDATE_NAME} <{CANDIDATE_EMAIL}>"
    msg["To"] = recipient_email
    msg["Subject"] = f"Application: {job_title} - {CANDIDATE_NAME} (COMSATS Grad)"

    domain_name = match_result["domain_name"]
    projects = match_result["github_projects"]

    projects_bullet_text = ""
    for p in projects:
        projects_bullet_text += f"  * {p['name']}: {p['desc']}\\n    Live Repository: {p['url']}\\n\\n"

    body = f"""Dear {company_name} Hiring Team,

I am writing to express my strong interest in the {job_title} role at {company_name}. I recently completed my Bachelor of Science in Computer Engineering from COMSATS University Islamabad, Abbottabad Campus, specializing in {domain_name}.

To demonstrate my hands-on technical capabilities, I have built and open-sourced production-ready projects directly relevant to this position:

{projects_bullet_text}
I have attached my tailored resume ({match_result['cv_file_name']}) for your consideration. You can also view all 12 of my active engineering repositories on my GitHub: {CANDIDATE_GITHUB}.

I would welcome the opportunity for a brief 15-minute conversation to discuss how my technical skills can contribute to {company_name}.

Thank you for your time and consideration.

Best regards,

{CANDIDATE_NAME}
{CANDIDATE_PHONE} | {CANDIDATE_EMAIL}
LinkedIn: {CANDIDATE_LINKEDIN}
GitHub: {CANDIDATE_GITHUB}
"""
    msg.set_content(body)

    # Attach the winning CV PDF
    cv_path = Path(match_result["cv_full_path"])
    if cv_path.exists():
        with open(cv_path, "rb") as f:
            pdf_data = f.read()
        msg.add_attachment(pdf_data, maintype="application", subtype="pdf", filename=match_result["cv_file_name"])

    # Save as .eml file
    safe_company = "".join(c for c in company_name if c.isalnum() or c in " _-").strip()
    eml_path = output_dir / f"Application_{safe_company}_{match_result['cv_file_name'].replace('.pdf', '')}.eml"
    with open(eml_path, "wb") as f:
        f.write(msg.as_bytes())

    return eml_path
'''

LINKEDIN_INDEED_COPILOT_PY = '''"""
LinkedIn & Indeed Application Pitch Generator.
Produces ready-to-paste screening answers and short pitch notes tailored to the matched domain.
"""
def generate_pitch(company_name: str, job_title: str, match_result: dict) -> dict:
    """Generates concise pitches suitable for LinkedIn Easy Apply notes and Indeed cover messages."""
    projects = match_result["github_projects"]
    p1 = projects[0]
    p2 = projects[1]

    pitch_note = (
        f"Hi {company_name} Team,\\n\\n"
        f"I am a Computer Engineering graduate from COMSATS specializing in {match_result['domain_name']}. "
        f"I have built production-grade open-source systems including {p1['name']} ({p1['url']}) "
        f"and {p2['name']} ({p2['url']}). "
        f"I have attached my specialized {match_result['cv_file_name']} and would love to connect!"
    )

    screening_answers = {
        "Years of relevant experience?": "1 year (hands-on project and internship experience)",
        "Are you authorized to work in this location?": "Yes",
        "Notice period / Availability?": "Immediate",
        "Comfortable with on-site/hybrid?": "Yes, fully comfortable",
        "Portfolio / GitHub Profile URL": "https://github.com/abdullah-bin-masaud",
        "Target CV to Upload": match_result["cv_file_name"]
    }

    return {
        "pitch_note": pitch_note,
        "screening_answers": screening_answers,
        "recommended_cv": match_result["cv_file_name"]
    }
'''

TRACKER_PY = '''"""
Application Tracker: Logs every job analyzed and applied to applied_tracker.csv.
"""
import csv
import time
from pathlib import Path

TRACKER_FILE = Path(__file__).parent / "applied_tracker.csv"


def log_application(company: str, role: str, channel: str, cv_used: str, notes: str = "Applied"):
    file_exists = TRACKER_FILE.exists()
    date_str = time.strftime("%Y-%m-%d %H:%M:%S")

    with open(TRACKER_FILE, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Date", "Company", "Role", "Channel", "CV_Used", "Status_Notes"])
        writer.writerow([date_str, company, role, channel, cv_used, notes])
'''

SAMPLE_JOBS_CSV = '''Company,Role,Channel,Contact_or_URL,Job_Description
Siemens,Embedded Firmware Engineer Trainee,Email,careers@siemens.com,"Seeking Junior Embedded Engineer with C/C++ programming for microcontroller firmware, interrupt handling, Proteus simulation, and UART/SPI communication."
Nayatel,Network Operations NOC Engineer,Email,jobs@nayatel.com,"Hiring fresh engineering graduate for IP networking, TCP/IP protocol troubleshooting, routing and switching, network monitoring, and socket telemetry."
Arbisoft,Junior Machine Learning & Computer Vision Engineer,LinkedIn,https://www.linkedin.com/jobs/view/12345,"Looking for Computer Vision engineer skilled in Python, YOLO object detection, OpenCV image processing, PyTorch CNNs, and ONNX deployment."
Systems Limited,Associate Software QA Automation Engineer,Indeed,https://pk.indeed.com/viewjob?jk=67890,"Graduate Software QA Engineer to design test automation with Python, pytest, REST API endpoint validation, and regression testing."
'''

MAIN_CLI_PY = '''"""
Automated Job Hunting Cockpit — Interactive CLI.
Run: py main.py
"""
import sys
from pathlib import Path
import csv

PROJECT_DIR = Path(__file__).parent
sys.path.insert(0, str(PROJECT_DIR))

from cv_matcher import classify_job
from email_generator import generate_email_draft
from linkedin_indeed_copilot import generate_pitch
from tracker import log_application


def menu():
    print("=" * 65)
    print("  ABDULLAH BIN MASAUD - AUTOMATED JOB APPLICATION ENGINE")
    print("=" * 65)
    print("1. [Interactive] Analyze a Job & Auto-Pick Winning CV")
    print("2. [Email Engine] Process Sample Jobs & Generate Ready-to-Send Drafts")
    print("3. [LinkedIn / Indeed] Generate 1-Click Pitch & Answers for a Job Post")
    print("4. [Tracker] View All Applied Jobs History")
    print("5. Exit")
    print("=" * 65)

    choice = input("Select an option (1-5): ").strip()
    return choice


def analyze_interactive():
    print("\\n--- PASTE JOB DETAILS ---")
    title = input("Job Title: ").strip()
    print("Enter Job Description keywords (e.g. Embedded C, PIC, Microcontroller OR YOLO, PyTorch):")
    desc = input("Job Description / Keywords: ").strip()

    res = classify_job(title, desc)
    print("\\n" + "=" * 55)
    print(f"  RECOMMENDED CV  : {res['cv_file_name']}")
    print(f"  TARGET DOMAIN   : {res['domain_name']}")
    print(f"  MATCH SCORE     : {res['score']} points")
    print(f"  MATCHED KEYWORDS: {', '.join(res['matched_keywords'])}")
    print("=" * 55)
    print("Recommended GitHub Repos to Feature:")
    for p in res["github_projects"]:
        print(f"  * {p['name']}: {p['url']}")


def process_email_batch():
    csv_path = PROJECT_DIR / "jobs_to_apply.csv"
    if not csv_path.exists():
        print(f"[!] {csv_path} not found.")
        return

    drafts_dir = PROJECT_DIR / "drafts"
    with open(csv_path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        count = 0
        for row in reader:
            company = row["Company"]
            role = row["Role"]
            channel = row["Channel"]
            contact = row["Contact_or_URL"]
            desc = row["Job_Description"]

            # Classify
            res = classify_job(role, desc)

            if channel.lower() == "email":
                draft_path = generate_email_draft(company, role, contact, res, drafts_dir)
                log_application(company, role, "Email", res["cv_file_name"], f"Draft created: {draft_path.name}")
                print(f"[+] [{res['cv_file_name']}] Generated Email Draft for {company} ({role}) -> {draft_path.name}")
                count += 1
            else:
                log_application(company, role, channel, res["cv_file_name"], f"Prepared for {channel}")
                print(f"[+] [{res['cv_file_name']}] Prepared {channel} target for {company} ({role})")

    print(f"\\n[*] Batch processing finished. Email draft files created in: {drafts_dir}")
    print("    Double-click any .eml file to open directly in your email client (Outlook/Thunderbird) and hit Send!")


def generate_copilot_pitch():
    company = input("Company Name: ").strip()
    role = input("Job Title: ").strip()
    desc = input("Job Description / Keywords: ").strip()

    res = classify_job(role, desc)
    pitch_data = generate_pitch(company, role, res)

    print("\\n" + "=" * 55)
    print(f"  1. ATTACH THIS RESUME FILE:")
    print(f"     -> {res['cv_full_path']}")
    print("\\n  2. COPY & PASTE THIS SHORT NOTE:")
    print("-" * 55)
    print(pitch_data["pitch_note"])
    print("-" * 55)
    print("\\n  3. STANDARD SCREENING ANSWERS:")
    for q, a in pitch_data["screening_answers"].items():
        print(f"     * {q} -> {a}")
    print("=" * 55)

    log_application(company, role, "LinkedIn/Indeed", res["cv_file_name"], "Copilot pitch generated")


def view_tracker():
    tracker_file = PROJECT_DIR / "applied_tracker.csv"
    if not tracker_file.exists():
        print("[*] No applied jobs logged yet.")
        return

    print("\\n" + "=" * 65)
    print("  APPLICATION TRACKING HISTORY")
    print("=" * 65)
    with open(tracker_file, mode="r", encoding="utf-8") as f:
        for line in f:
            print(line.strip())


if __name__ == "__main__":
    while True:
        c = menu()
        if c == "1":
            analyze_interactive()
        elif c == "2":
            process_email_batch()
        elif c == "3":
            generate_copilot_pitch()
        elif c == "4":
            view_tracker()
        elif c == "5":
            print("[*] Exiting. Good luck with your applications!")
            break
        else:
            print("[!] Invalid option. Choose 1-5.")
        input("\\nPress Enter to continue...")
'''

README_MD = '''# Automated Job Application Engine

An intelligent, multi-channel job hunting engine tailored for **Abdullah Bin Masaud**. It automatically analyzes job postings across Email, LinkedIn, and Indeed, scores them against your 4 specialized CVs, and produces tailored outreach with attached resumes and matching GitHub repositories.

## How It Works
```
[ Job Title & Description ]
            │
            ▼
   [ cv_matcher.py ] ───> Analyzes keyword density across 4 domains
            │
            ├─> High AI/Vision    ──> Picks CV__A.pdf + links VisionAid & Medical U-Net
            ├─> High Telecom      ──> Picks CV__T.pdf + links TCP/IP Server & Video Cockpit
            ├─> High Embedded     ──> Picks CV__H.pdf + links PIC18 Signal & Attendance Gate
            └─> High QA/Testing   ──> Picks CV__S.pdf + links REST API Testing & QA Pipeline
            │
            ▼
[ Channel Dispatcher ]
    ├── Email Engine     ──> Creates ready-to-send .eml drafts with CV attached
    ├── LinkedIn/Indeed  ──> Generates 1-click tailored pitch notes & screening answers
    └── Tracker          ──> Logs date, company, role, channel, and CV used to CSV
```

## Quickstart

### 1. Launch the Engine
```bash
cd C:\\Users\\Lenovo\\Desktop\\Projects\\Automated-Job-Applier
py main.py
```

### 2. Available Options
1. **Analyze a Job Post:** Paste any job title and description $\\rightarrow$ tells you the winning CV to upload.
2. **Process Email Batch:** Reads `jobs_to_apply.csv` and creates ready-to-send `.eml` draft files in `drafts/` with your CV attached.
3. **LinkedIn / Indeed Pitch:** Generates customized short cover notes and answers to screening questions.
4. **View Tracker:** Shows historical record of every job applied to.
'''

files = {
    "cv_matcher.py": CV_MATCHER_PY,
    "email_generator.py": EMAIL_GENERATOR_PY,
    "linkedin_indeed_copilot.py": LINKEDIN_INDEED_COPILOT_PY,
    "tracker.py": TRACKER_PY,
    "jobs_to_apply.csv": SAMPLE_JOBS_CSV.strip() + "\n",
    "main.py": MAIN_CLI_PY,
    "README.md": README_MD,
}

for rel, code in files.items():
    p = BASE_DIR / rel
    p.write_text(code.strip() + "\n", encoding="utf-8")
    print(f"Created {p}")

print("Automated-Job-Applier engine successfully built!")
