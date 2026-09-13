
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

# ─────────────────────────────────────────────────────────────────────────────
# BATCH 6 — VERIFIED EMAILS ONLY | ISB/RWP/REMOTE/INTERNATIONAL
# Each job has a 100% personalised body tailored to that exact company
# ─────────────────────────────────────────────────────────────────────────────
BATCH6 = [

    # ── ISLAMABAD — VERIFIED ─────────────────────────────────────────────────
    {
        "company": "Arbisoft (Fresh Grad Programme)",
        "email":   "freshgradhiring@arbisoft.com",
        "cv":      "AI",
        "subject": "Fresh Graduate Application – Abdullah Bin Masaud – Computer Engineering – COMSATS 2026",
        "body": """Dear Arbisoft Recruitment Team,

I am applying to Arbisoft's Fresh Graduate Hiring Programme — specifically the programme you run twice a year for BS graduates. I am a final-year Computer Engineering student at COMSATS University Islamabad, Abbottabad Campus (graduating 2026, CGPA: strong academic standing).

Why Arbisoft specifically?
I have followed your engineering blog and culture page. The fact that you build products used by millions globally — from education tech to FinTech — while maintaining one of Pakistan's best engineering cultures is exactly the environment I want to start my career in.

What I bring to the table:
→ VisionAid — my Final Year Project: real-time object-detection assistive device (YOLOv8 + Raspberry Pi 4) for visually impaired users. Featured-quality AI project.
→ AI Medical Image Segmentation — U-Net with 91%+ Dice score on brain tumour data
→ Customer Churn Engine — XGBoost + SHAP explainability, production-ready pipeline
→ Traffic & Pedestrian Counter — YOLOv8, deployed as a REST API

Every project is documented on GitHub: https://github.com/abdullah-bin-masaud
LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b

I am currently in Abbottabad and can relocate to Islamabad or Lahore immediately. I am also available for your online MCQ/coding assessment at any time.

My CV (AI/Computer Vision domain) is attached. I would be honoured to be part of Arbisoft's next cohort.

Sincerely,
Abdullah Bin Masaud
+92 332 9076356
COMSATS University Islamabad, Abbottabad | BS Computer Engineering (2022–2026)
"""
    },
    {
        "company": "Folio3 AI",
        "email":   "info@folio3.com",
        "cv":      "AI",
        "subject": "AI / ML Trainee Engineer Application – Abdullah Bin Masaud – COMSATS 2026",
        "body": """Dear Folio3 Hiring Team,

I am writing to apply for a Trainee/Associate AI Engineer position at Folio3's Islamabad office (Gulberg Green, Civic Center). Folio3's work in AI-powered enterprise solutions — from computer vision to predictive analytics — aligns perfectly with my final-year specialisation.

My most relevant project to Folio3's AI work:
→ VisionAid (FYP): YOLOv8-based real-time object detection for visually impaired users. This involved edge deployment on Raspberry Pi 4, custom dataset preparation, and real-time inference optimisation — production-level skills.
→ AI Medical Image Segmentation: U-Net trained on MRI data for tumour detection. Demonstrates deep learning beyond classification.
→ Customer Churn Predictive Engine: XGBoost + SHAP, including a REST API deployment layer (Flask).

GitHub (all projects live): https://github.com/abdullah-bin-masaud
LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b

I am based in Abbottabad and can join the Islamabad office immediately. I am available for any technical assessment or interview at your convenience.

My AI-focused CV is attached.

Respectfully,
Abdullah Bin Masaud
+92 332 9076356
COMSATS University Islamabad, Abbottabad | BS Computer Engineering (2022–2026)
"""
    },
    {
        "company": "Xgrid Islamabad",
        "email":   "careers@xgrid.co",
        "cv":      "AI",
        "subject": "AI/Cloud Engineering Internship Application – Abdullah Bin Masaud – COMSATS 2026",
        "body": """Dear Xgrid Talent Team,

I came across Xgrid's office at Gulberg Greens Islamabad and was immediately drawn to your focus on AI-driven cloud infrastructure. I am a final-year Computer Engineering student at COMSATS Islamabad (graduating 2026) applying for an internship on your engineering team.

Technical highlights most relevant to Xgrid:
→ Real-time telemetry streaming dashboard: Flask + SocketIO + OpenCV — backend architecture similar to cloud-native microservices
→ VisionAid: AI edge deployment on Raspberry Pi — resource-constrained inference, directly applicable to IoT/cloud AI at Xgrid
→ Flask REST API: production-grade with pytest suite, documented, and version-controlled

I am disciplined with Git, clean code practices, and documentation — I understand that at a company like Xgrid, code quality matters as much as functionality.

GitHub: https://github.com/abdullah-bin-masaud
LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b

I can join the Islamabad office immediately. CV attached.

Best regards,
Abdullah Bin Masaud | +92 332 9076356
COMSATS University Islamabad | BS Computer Engineering (2022–2026)
"""
    },
    {
        "company": "United Sol Islamabad",
        "email":   "career@unitedsol.net",
        "cv":      "SOFTWARE",
        "subject": "Software Engineering Intern Application – Abdullah Bin Masaud – COMSATS 2026",
        "body": """Dear United Sol HR Team,

I am Abdullah Bin Masaud, a final-year Computer Engineering student at COMSATS University Islamabad, Abbottabad (graduating 2026), applying for a software engineering internship at United Sol Islamabad.

My software engineering portfolio demonstrates production-level thinking:
→ Flask REST API: Full CRUD, authentication, pytest suite, Postman-tested, Swagger docs — ready for real project integration
→ Python Data QA Pipeline: Automated CSV validation, anomaly detection, HTML report generation — built like a production tool
→ TCP/IP Client-Server: Multithreaded architecture, custom binary packet protocol with CRC32 error detection, load tested with 50 concurrent threads

I take software quality seriously: every project on my GitHub has README documentation, requirements.txt, and clean folder structure.

GitHub: https://github.com/abdullah-bin-masaud
LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b

Available to start immediately in Islamabad. Software-engineering CV is attached.

Sincerely,
Abdullah Bin Masaud | +92 332 9076356
COMSATS University Islamabad | BS Computer Engineering (2022–2026)
"""
    },
    {
        "company": "Devomech Solutions Rawalpindi",
        "email":   "info@devomech.com",
        "cv":      "HARDWARE",
        "subject": "Embedded Systems Engineering Internship – Abdullah Bin Masaud – COMSATS 2026",
        "body": """Dear Devomech Solutions Team,

I have been following Devomech's robotics and embedded systems work from Rawalpindi — it is exactly the kind of hands-on engineering environment I want to start my career in. I am a final-year Computer Engineering student at COMSATS University Islamabad, Abbottabad (graduating 2026), applying for an embedded engineering internship.

My embedded systems projects:
→ PIC18F4550 Signal Communication Unit: Interrupt-driven firmware in C/XC8, UART communication, EEPROM data logging, custom packet protocol — every register manually configured, no abstraction layers
→ RFID Automated Attendance System: Real PCB logic, Proteus simulation, SPI + serial UART bridge
→ Sensor Control & Alert Circuits: Analog sensor interfacing, threshold-based alerting, hardware debouncing

I am comfortable reading datasheets, writing from scratch in C, and debugging with oscilloscopes. I want to work on real hardware — not just simulation.

GitHub: https://github.com/abdullah-bin-masaud
LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b

I can commute to Rawalpindi or relocate immediately. Hardware-focused CV is attached.

Respectfully,
Abdullah Bin Masaud | +92 332 9076356
COMSATS University Islamabad | BS Computer Engineering (2022–2026)
"""
    },
    {
        "company": "ZALYXIS AI (Remote Pakistan)",
        "email":   "contact@zalyxis.com",
        "cv":      "AI",
        "subject": "AI/ML Remote Internship Application – Abdullah Bin Masaud – COMSATS 2026",
        "body": """Dear ZALYXIS AI Team,

I am applying for your 3-month remote AI/ML internship programme. I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), and AI is my primary specialisation.

Projects directly relevant to your AI work:
→ VisionAid (FYP): YOLOv8-based real-time assistive system — from dataset annotation to edge deployment on Raspberry Pi 4, this was a complete end-to-end AI project
→ AI Medical Image Segmentation: U-Net architecture, trained on real MRI data, 91%+ Dice score
→ Traffic & Pedestrian Counter: YOLOv8 multi-class detection, wrapped as a REST API

I work autonomously and am fully set up for remote work (stable internet, dedicated workspace, Git-based workflow). I am available to start immediately and commit full-time for the internship duration.

GitHub: https://github.com/abdullah-bin-masaud
LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b

AI CV is attached. Happy to complete any technical assessment.

Best regards,
Abdullah Bin Masaud | +92 332 9076356
COMSATS University Islamabad | BS Computer Engineering (2022–2026)
"""
    },

    # ── REMOTE / INTERNATIONAL ────────────────────────────────────────────────
    {
        "company": "Remotebase Pakistan",
        "email":   "careers@remotebase.com",
        "cv":      "SOFTWARE",
        "subject": "Remote Software Engineer Application – Abdullah Bin Masaud – BS Computer Engineering 2026",
        "body": """Dear Remotebase Team,

Remotebase's mission — connecting top Pakistani talent with global tech companies — is exactly what I am looking for. I am a final-year Computer Engineering student at COMSATS Islamabad (graduating 2026), with a strong software engineering portfolio ready for international-standard remote work.

Why I am a strong Remotebase candidate:
→ Strong fundamentals: TCP/IP socket programming, REST API design, automated testing — not just framework usage
→ Clean code culture: every GitHub project has documentation, requirements, and consistent structure
→ Self-managed: I have independently built and documented 12 GitHub projects over the last 6 months

My strongest projects for remote software roles:
→ Flask REST API — production-ready with pytest, Swagger, and Postman collections
→ Python Data QA Pipeline — automated data validation with HTML reports
→ TCP/IP Client-Server — custom binary protocol, multithreaded, CRC32 verified

GitHub: https://github.com/abdullah-bin-masaud
LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b

Available full-time, immediately. Software CV attached.

Sincerely,
Abdullah Bin Masaud | +92 332 9076356
COMSATS University Islamabad | BS Computer Engineering (2022–2026)
"""
    },
    {
        "company": "Turing.com",
        "email":   "jobs@turing.com",
        "cv":      "AI",
        "subject": "AI Engineer Application (Pakistan Remote) – Abdullah Bin Masaud – COMSATS 2026",
        "body": """Dear Turing Talent Team,

I am applying to join the Turing network as a remote AI/ML engineer. I have a strong AI portfolio and am ready for the Turing technical vetting process.

My AI/ML skillset:
→ Computer Vision: YOLOv8 object detection, U-Net segmentation, real-time inference optimisation
→ ML Engineering: XGBoost, SHAP explainability, sklearn pipelines, model serialisation with joblib
→ Deployment: Flask REST API serving ML models, tested with pytest and Postman
→ Languages/Frameworks: Python (primary), NumPy, Pandas, OpenCV, PyTorch (learning), TensorFlow

FYP: VisionAid — assistive object detection system deployed on Raspberry Pi 4 for visually impaired users. This is the kind of real-world, constraint-driven AI engineering I am passionate about.

GitHub: https://github.com/abdullah-bin-masaud (12 public repositories)
LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b

I am ready to take the Turing vetting assessment immediately. AI CV is attached.

Best regards,
Abdullah Bin Masaud | +92 332 9076356
COMSATS University Islamabad | BS Computer Engineering (2022–2026)
"""
    },
    {
        "company": "Andela (Remote Emerging Markets)",
        "email":   "talent@andela.com",
        "cv":      "SOFTWARE",
        "subject": "Software Engineer Application – Pakistan – Abdullah Bin Masaud – 2026",
        "body": """Dear Andela Talent Team,

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026) applying to join the Andela talent network from Pakistan.

I understand Andela connects talented engineers from emerging markets with global technology companies. I believe I am exactly the profile you are looking for — strong fundamentals, real projects, and a demonstrated ability to work independently.

Technical highlights:
→ Flask REST API: Full-featured, pytest-covered, Swagger-documented — production-ready
→ TCP/IP Client-Server: Custom binary protocol, multithreaded server, error detection — strong CS fundamentals
→ AI Pipeline: YOLOv8 + U-Net + XGBoost — cross-domain ML engineering ability
→ Python Data QA: Automated validation and reporting system — data engineering skills

12 public GitHub repositories: https://github.com/abdullah-bin-masaud
LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b

Available immediately for remote work (PKT timezone, UTC+5). Software CV is attached.

Respectfully,
Abdullah Bin Masaud | +92 332 9076356
COMSATS University Islamabad | BS Computer Engineering (2022–2026)
"""
    },
    {
        "company": "Devsinc (Fresh Grad)",
        "email":   "jobs@devsinc.com",
        "cv":      "AI",
        "subject": "Fresh Graduate – AI/Software Engineer Application – Abdullah Bin Masaud – COMSATS 2026",
        "body": """Dear Devsinc Recruitment Team,

I am applying for Devsinc's Graduate & Early Career programme. I have followed Devsinc's growth into a global technology company with 500+ engineers, and I want to be part of that growth from the start of my career.

What sets me apart from other applicants:
1. REAL projects on GitHub — not university exercises. My VisionAid FYP is a working assistive technology system. My data QA pipeline is designed as a production tool.
2. Cross-domain engineering — I can work in AI/ML, backend APIs, and systems-level programming. Versatile from day one.
3. Documentation discipline — every GitHub repo has a README, architecture notes, and clean code. No spaghetti code.

Key projects:
→ VisionAid: YOLOv8 real-time assistive system on Raspberry Pi 4
→ AI Medical Image Segmentation: U-Net, 91%+ Dice score
→ Flask REST API: Production-grade with pytest and Swagger
→ TCP/IP Protocol: Multithreaded server with custom binary packet format

GitHub: https://github.com/abdullah-bin-masaud
LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b

I am ready for your technical assessment anytime. Can join Islamabad office or work remotely. CV attached.

Sincerely,
Abdullah Bin Masaud | +92 332 9076356
COMSATS University Islamabad | BS Computer Engineering (2022–2026)
"""
    },
    {
        "company": "Emumba Islamabad",
        "email":   "hr@emumba.com",
        "cv":      "SOFTWARE",
        "subject": "Software Engineering Intern Application – Abdullah Bin Masaud – COMSATS Islamabad 2026",
        "body": """Dear Emumba HR Team,

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026) applying for a software engineering internship at Emumba. I have been following Emumba's work — particularly your culture of engineering excellence and the high-calibre clients you serve.

My technical foundation is strong:
→ Flask REST API — designed with layered architecture, full test coverage, documented endpoints
→ TCP/IP Client-Server — implemented from scratch: socket programming, binary packet design, CRC32, multithreaded concurrency
→ Python Data QA Pipeline — production-grade automated validation tool

I care deeply about code quality. I don't just make it work — I make it maintainable. That matches Emumba's reputation.

GitHub: https://github.com/abdullah-bin-masaud
LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b

Based in Abbottabad, available to join Islamabad office immediately. Software CV attached.

Best regards,
Abdullah Bin Masaud | +92 332 9076356
COMSATS University Islamabad | BS Computer Engineering (2022–2026)
"""
    },
    {
        "company": "10Pearls Islamabad",
        "email":   "hr@10pearls.com",
        "cv":      "AI",
        "subject": "AI Engineering Intern Application – Abdullah Bin Masaud – COMSATS Islamabad 2026",
        "body": """Dear 10Pearls Recruitment Team,

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), writing to apply for an AI/Software Engineering internship at 10Pearls. Your company's reputation for building cutting-edge digital products across AI, cloud, and mobile makes it one of my top choices in Pakistan.

My most relevant AI work:
→ VisionAid: End-to-end AI assistive system — dataset preparation, model training (YOLOv8), edge optimisation, and real device deployment. This is production AI work, not a class project.
→ Medical Image Segmentation: U-Net — demonstrates deep learning beyond standard classification
→ Customer Churn Engine: Deployed as a Flask API with SHAP explainability for business stakeholders

I am eager to apply these skills in a professional environment and grow rapidly. My GitHub has 12 live projects: https://github.com/abdullah-bin-masaud
LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b

Available to join Islamabad office or work remotely. AI CV attached.

Sincerely,
Abdullah Bin Masaud | +92 332 9076356
COMSATS University Islamabad | BS Computer Engineering (2022–2026)
"""
    },
    {
        "company": "Nayatel Islamabad",
        "email":   "careers@nayatel.com",
        "cv":      "TELECOM",
        "subject": "Telecom/Network Engineering Internship – Abdullah Bin Masaud – COMSATS 2026",
        "body": """Dear Nayatel HR Team,

Nayatel is the gold standard of ISP/Telecom service in Islamabad — I have lived under your network and seen your infrastructure grow. I am a final-year Computer Engineering student at COMSATS Islamabad (graduating 2026), applying for a telecom/network engineering internship.

Why Nayatel specifically:
Your work spans fibre infrastructure, IPTV, and ISP operations — exactly the telecom domains I have studied and experimented with in my projects.

My telecom and networking background:
→ TCP/IP Client-Server: Multithreaded socket server with custom packet format, CRC32 error detection, load-tested with 50 concurrent clients — real network programming
→ UART-based PIC18 Communication: Serial data protocol design and hardware implementation
→ Telemetry Streaming: Real-time sensor data broadcast over Socket.IO — IoT networking pattern

I want to contribute to Nayatel's network operations or engineering team and grow in a company that builds real infrastructure for Pakistan.

GitHub: https://github.com/abdullah-bin-masaud
LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b

Available to join Islamabad immediately. Telecom CV attached.

Respectfully,
Abdullah Bin Masaud | +92 332 9076356
COMSATS University Islamabad | BS Computer Engineering (2022–2026)
"""
    },
    {
        "company": "Systems Limited Islamabad",
        "email":   "talent@systemsltd.com",
        "cv":      "SOFTWARE",
        "subject": "Graduate Trainee – Software Engineering – Abdullah Bin Masaud – COMSATS 2026",
        "body": """Dear Systems Limited Talent Acquisition Team,

Systems Limited is one of Pakistan's most respected IT companies with a track record of building world-class software for global clients. I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026), and I want to build my career at Systems Limited.

My software engineering profile is strong and practical:
→ Flask REST API: Complete backend API with CRUD operations, JWT authentication, pytest test suite, Swagger documentation — the kind of API that can go into production
→ TCP/IP Protocol System: Low-level network programming — understanding protocols at the byte level
→ Data QA Pipeline: Automated testing and validation — relevant to Systems Limited's QA and enterprise software work
→ 12 live GitHub projects: https://github.com/abdullah-bin-masaud

I am a hard worker who codes outside class hours — all my GitHub projects were self-initiated. That drive is what I will bring to Systems Limited every day.

LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b

Available for technical assessment and can join Islamabad office immediately. Software CV attached.

Sincerely,
Abdullah Bin Masaud | +92 332 9076356
COMSATS University Islamabad | BS Computer Engineering (2022–2026)
"""
    },
    {
        "company": "i2c Inc Rawalpindi",
        "email":   "careers@i2cinc.com",
        "cv":      "SOFTWARE",
        "subject": "Software Engineering Intern Application – Abdullah Bin Masaud – COMSATS 2026",
        "body": """Dear i2c Inc Recruiting Team,

i2c Inc is globally recognised as one of the most advanced fintech platform companies — and it operates from Rawalpindi, which is exactly where I want to build my career. I am a final-year Computer Engineering student at COMSATS Islamabad (graduating 2026), applying for a software engineering internship.

What makes me a strong fit for i2c's engineering culture:
→ I understand systems at a low level — I have built TCP/IP socket protocols from scratch, including binary packet formats, CRC32 checksums, and multithreaded handling. This kind of rigour matches i2c's payment platform requirements.
→ I can build APIs: Flask REST backend with full test coverage and documentation
→ I care about data correctness: My Python Data QA Pipeline is built around exactly that

GitHub: https://github.com/abdullah-bin-masaud
LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b

Can commute to Rawalpindi or work remotely. Available immediately. Software CV attached.

Respectfully,
Abdullah Bin Masaud | +92 332 9076356
COMSATS University Islamabad | BS Computer Engineering (2022–2026)
"""
    },
]

# ─── EMAIL SENDER ──────────────────────────────────────────────────────────
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

def log_application(company, email, domain, status):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    TRACKER_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(TRACKER_PATH, "a", encoding="utf-8") as f:
        f.write(f"{timestamp},{company},{email},{domain},,{status}\n")

def main():
    print("=" * 70)
    print("  BATCH 6 — VERIFIED EMAILS | ISB/RWP/REMOTE/INTL | MAX-CALLBACK")
    print(f"  Targets: {len(BATCH6)} companies — each email 100% personalised")
    print("=" * 70)
    sent = failed = 0
    for i, job in enumerate(BATCH6, 1):
        company = job["company"]
        email   = job["email"]
        domain  = job["cv"]
        cv_path = CV_MAP[domain]
        print(f"\n[{i:02d}/{len(BATCH6)}] {company}")
        print(f"      To     : {email}")
        print(f"      CV     : {cv_path.name}  |  {domain}")
        try:
            send_email(email, job["subject"], job["body"], cv_path)
            log_application(company, email, domain, "SENT")
            print(f"      Status : [OK] SENT")
            sent += 1
        except Exception as e:
            log_application(company, email, domain, f"FAILED: {e}")
            print(f"      Status : [FAIL] {e}")
            failed += 1
    print("\n" + "=" * 70)
    print(f"  BATCH 6 COMPLETE  |  Sent: {sent}  |  Failed: {failed}")
    print(f"  Cumulative total: ~{83 + sent} applications sent")
    print("=" * 70)

if __name__ == "__main__":
    main()
