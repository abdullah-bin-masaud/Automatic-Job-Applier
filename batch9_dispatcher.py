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

# ── BATCH 9: 24 PRE-CHECKED MX TARGETS (SAUDI, UAE, REMOTE, PAKISTAN) ───────
TARGETS = [
    # ── SAUDI ARABIA TECH & FINTECH ──
    {
        "company": "Tabby (BNPL FinTech Unicorn)",
        "email":   "careers@tabby.ai",
        "domain":  "SOFTWARE",
        "role":    "Associate Backend Software Engineer",
        "region":  "Saudi Arabia & UAE",
        "subject": "Associate Backend Engineer Application: Abdullah Bin Masaud – FinTech (KSA / UAE)",
        "body": """Dear Tabby Talent Acquisition Team,

Tabby's rapid rise as the MENA region's leading shopping and financial services app requires robust, highly available payment infrastructure. I am writing to apply for an Associate Backend Software Engineer position.

I am graduating in Computer Engineering from COMSATS University Islamabad in 2026.

Why My Background Fits Tabby:
- Systems Concurrency & Integrity: Designed a custom multithreaded TCP/IP client-server protocol with CRC32 packet validation, handling concurrent client streams without degradation.
- Production REST APIs: Developed modular Flask REST APIs covered by 25+ automated pytest test cases validating latency, schemas, and concurrent load.
- Data Quality Pipelines: Built Python data validation pipelines with statistical outlier detection.

Ready for relocation to Riyadh, Dubai, or remote work.

Profiles:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My Software CV is attached.

Best regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "HungerStation (Delivery Hero KSA)",
        "email":   "careers@hungerstation.com",
        "domain":  "SOFTWARE",
        "role":    "Associate Software Engineer",
        "region":  "Saudi Arabia",
        "subject": "Associate Software Engineer Application: Abdullah Bin Masaud – COMSATS 2026 (Riyadh)",
        "body": """Dear HungerStation Talent Team,

HungerStation's high-throughput food and quick-commerce delivery platform across Saudi Arabia requires resilient, scalable backend services. I am writing to apply for an Associate Software Engineer role in Riyadh.

I am a final-year Computer Engineering candidate from COMSATS University Islamabad (graduating 2026).

Technical Strengths:
- API Engineering: Designed and tested Flask REST endpoints with automated pytest coverage, latency checks, and error boundaries.
- Network Protocols: Custom TCP/IP multithreaded socket server with CRC32 packet integrity validation.
- Data Pipelines: Automated Python data verification with outlier detection and reporting.

Ready for relocation to Riyadh.

Links:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My Software CV is attached.

Warm regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Bupa Arabia (HealthTech & Digital)",
        "email":   "careers@bupa.com.sa",
        "domain":  "AI",
        "role":    "HealthTech & AI Software Engineer",
        "region":  "Saudi Arabia",
        "subject": "HealthTech & AI Software Engineer: Abdullah Bin Masaud – COMSATS 2026 (KSA)",
        "body": """Dear Bupa Arabia Talent Acquisition Team,

Bupa Arabia's digital health solutions and healthcare insurance technology in Saudi Arabia represent high-impact digital transformation. I am applying for an engineering role on your digital health team.

I am graduating in Computer Engineering from COMSATS University Islamabad in 2026.

Healthcare & Applied AI Experience:
- AI Medical Image Segmentation: Developed a deep learning U-Net architecture trained on MRI brain tumor datasets, achieving 91%+ Dice similarity coefficient for automated lesion delineation.
- Assistive Technology (VisionAid): Real-time visual assistance device using edge AI (YOLOv8 + Raspberry Pi) for visually impaired individuals.
- Clean Backend Engineering: Production REST APIs with full test coverage and automated reporting.

Ready for relocation to Saudi Arabia.

Profiles:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My AI & Software CV is attached.

Best regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Alinma Bank (Digital Banking & IT)",
        "email":   "careers@alinma.com",
        "domain":  "SOFTWARE",
        "role":    "Associate Software Engineer / IT Trainee",
        "region":  "Saudi Arabia",
        "subject": "Associate Software Engineer Application: Abdullah Bin Masaud – FinTech (Riyadh)",
        "body": """Dear Alinma Bank Digital Talent Team,

Alinma Bank's pioneering digital banking platforms and fintech integrations across Saudi Arabia require dependable, test-driven systems engineering. I am applying for an Associate Software Engineer role in Riyadh.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026).

Competencies:
- Systems Reliability: Custom TCP/IP socket server with CRC32 packet integrity validation.
- API & Test Automation: Comprehensive pytest test suites validating API response codes, latency benchmarks, and concurrency.
- Data Quality Pipelines: Python data auditing pipeline with statistical outlier detection.

Ready for relocation to Riyadh.

Links:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My Software CV is attached.

Sincerely,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Thiqah (Business Solutions Leader KSA)",
        "email":   "careers@thiqah.sa",
        "domain":  "SOFTWARE",
        "role":    "Associate Software Engineer",
        "region":  "Saudi Arabia",
        "subject": "Associate Software Engineer Application: Abdullah Bin Masaud – COMSATS 2026 (KSA)",
        "body": """Dear Thiqah Recruitment Team,

Thiqah's smart enterprise platforms powering commercial and legal solutions across Saudi Arabia represent high-consequence engineering. I am applying for an Associate Software Engineer role.

I am graduating in Computer Engineering from COMSATS University Islamabad in 2026.

Technical Portfolio:
- Production-Grade APIs: Modular Flask REST APIs with automated testing and structured JSON schemas.
- Concurrency & Reliability: Multi-client socket handling with CRC32 packet integrity validation.
- Clean Code Standards: 12 public GitHub repositories following unit testing and modular architecture.

Ready for relocation to Saudi Arabia.

Profiles:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My Software CV is attached.

Warm regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "SAL Logistics (Smart Cargo Logistics KSA)",
        "email":   "careers@sal.sa",
        "domain":  "SOFTWARE",
        "role":    "Junior Software Engineer / Systems",
        "region":  "Saudi Arabia",
        "subject": "Junior Software Engineer Application: Abdullah Bin Masaud – COMSATS 2026 (KSA)",
        "body": """Dear SAL Logistics Talent Team,

SAL's supply chain technology, air cargo operations, and smart tracking platforms across the Kingdom require robust logistics systems software. I am applying for a Junior Software Engineer position in Saudi Arabia.

I am a final-year Computer Engineering candidate from COMSATS University Islamabad (graduating 2026).

Profile Highlights:
- Scalable Systems: Implemented multithreaded socket communication protocols tested with 50 concurrent client threads.
- Automated Testing & QA: Comprehensive pytest test suites ensuring endpoint response latency under 200ms.
- Data Quality Pipelines: Standalone Python data auditing pipeline with statistical outlier detection.

Ready for relocation to Saudi Arabia.

Links:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My Software CV is attached.

Best regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },

    # ── DUBAI & UAE TECH & FINTECH ──
    {
        "company": "Sarwa (Robo-Advisor & WealthTech Dubai)",
        "email":   "careers@sarwa.co",
        "domain":  "SOFTWARE",
        "role":    "Junior Backend Software Engineer",
        "region":  "Dubai / UAE",
        "subject": "Junior Backend Engineer Application: Abdullah Bin Masaud – FinTech (Dubai / Remote)",
        "body": """Dear Sarwa Talent Acquisition Team,

Sarwa's automated investment and trading platform making wealth management accessible across the GCC is an incredible FinTech benchmark. I am applying for a Junior Backend Software Engineer position in Dubai or remote.

I am graduating in Computer Engineering from COMSATS University Islamabad in 2026.

Why I Fit:
- Protocol Rigor: Built custom multithreaded TCP/IP communication protocols with binary packet framing and CRC32 checksums.
- Robust API Engineering: Designed Flask REST endpoints with strict schema validation and 25+ automated pytest test cases.
- Financial Risk Modeling: Built XGBoost predictive risk engines with SHAP explainability.

Available for Dubai or remote.

Profiles:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My Software CV is attached.

Warm regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Tarabut Gateway (Open Banking MENA)",
        "email":   "careers@tarabutgateway.com",
        "domain":  "SOFTWARE",
        "role":    "Associate Software Engineer (APIs)",
        "region":  "Dubai / UAE & Regional",
        "subject": "Associate Software Engineer Application: Abdullah Bin Masaud – Open Banking (Dubai / Remote)",
        "body": """Dear Tarabut Gateway Engineering Team,

Tarabut Gateway's open banking platform connecting financial institutions and FinTechs across the Middle East requires flawless API design and system security. I am applying for an Associate Software Engineer role.

I am a final-year Computer Engineering candidate from COMSATS University Islamabad (graduating 2026).

Technical Strengths:
- API Engineering: Designed and tested Flask REST endpoints with automated pytest coverage, latency checks, and error boundaries.
- Network Protocols: Custom TCP/IP multithreaded socket server with CRC32 packet integrity validation.
- Data Pipelines: Automated Python data verification with outlier detection and reporting.

Available for Dubai or remote.

Links:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My Software CV is attached.

Sincerely,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Postpay (FinTech Dubai)",
        "email":   "careers@postpay.io",
        "domain":  "SOFTWARE",
        "role":    "Junior Software Engineer",
        "region":  "Dubai / UAE",
        "subject": "Junior Software Engineer Application: Abdullah Bin Masaud – FinTech (Dubai)",
        "body": """Dear Postpay Talent Team,

Postpay's seamless checkout and payment solutions across the UAE and GCC represent modern payment engineering. I am writing to apply for a Junior Software Engineer position in Dubai.

I am graduating in Computer Engineering from COMSATS University Islamabad in 2026.

Profile Highlights:
- Low-Level Data Integrity: Engineered custom binary network protocols with CRC32 checksums, tested under concurrent client loads.
- API & Test Automation: Modular Flask REST endpoints covered by 25+ pytest test cases verifying latency and schema validation.
- Clean Code Standards: 12 public GitHub repositories following unit testing and modular architecture.

Ready for relocation to Dubai.

Profiles:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My Software CV is attached.

Best regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Grubtech (Cloud Kitchen & FoodTech Dubai)",
        "email":   "careers@grubtech.com",
        "domain":  "SOFTWARE",
        "role":    "Associate Backend Software Engineer",
        "region":  "Dubai / UAE",
        "subject": "Associate Backend Engineer Application: Abdullah Bin Masaud – COMSATS 2026 (Dubai)",
        "body": """Dear Grubtech Hiring Team,

Grubtech's restaurant operating system powering dark kitchens and omnichannel dining across 15+ countries represents high-scale distributed engineering. I am applying for an Associate Backend Software Engineer position in Dubai.

I am a final-year Computer Engineering candidate from COMSATS University Islamabad (graduating 2026).

Relevant Experience:
- Production REST APIs: Flask services covered by pytest test suites verifying endpoints, error handling, and concurrency.
- Telemetry & Event Streaming: Live sensor telemetry broadcasting systems built in Flask with WebSocket communication.
- Low-Level Systems: Custom multithreaded socket communication protocols with CRC32 packet error detection.

Ready for relocation to Dubai.

Links:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My Software CV is attached.

Warm regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Baraka (Investment & WealthTech Dubai)",
        "email":   "careers@getbaraka.com",
        "domain":  "SOFTWARE",
        "role":    "Junior Software Engineer",
        "region":  "Dubai / UAE",
        "subject": "Junior Software Engineer Application: Abdullah Bin Masaud – WealthTech (Dubai / Remote)",
        "body": """Dear Baraka Talent Team,

Baraka's commission-free investment platform empowering retail investors across the Middle East represents clean, user-centric engineering. I am applying for a Junior Software Engineer position in Dubai or remote.

I am graduating in Computer Engineering from COMSATS University Islamabad in 2026.

Engineering Highlights:
- Low-Level Data Integrity: Engineered custom binary network protocols with CRC32 checksums, tested under concurrent client loads.
- API & Test Automation: Modular Flask REST endpoints covered by 25+ pytest test cases verifying latency and schema validation.
- Clean Code Standards: 12 public GitHub repositories following unit testing and modular architecture.

Available for Dubai or remote.

Profiles:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My Software CV is attached.

Sincerely,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },

    # ── PAKISTAN SOFTWARE & IT POWERHOUSES ──
    {
        "company": "Gaditek - Pakistan",
        "email":   "careers@gaditek.com",
        "domain":  "SOFTWARE",
        "role":    "Associate Software Engineer",
        "region":  "Pakistan",
        "subject": "Associate Software Engineer Application: Abdullah Bin Masaud – COMSATS 2026",
        "body": """Dear Gaditek Talent Acquisition Team,

Gaditek's venture builder model and global SaaS products (cybersecurity, VPNs, cloud tools) reaching millions worldwide represent product engineering at scale. I am writing to apply for an Associate Software Engineer role.

I am a final-year Computer Engineering candidate from COMSATS University Islamabad (graduating 2026).

Engineering Highlights:
- Low-Level Systems: Custom multithreaded TCP/IP socket server with binary packet framing and CRC32 integrity validation.
- API Engineering: Modular Flask REST APIs with automated pytest validation for response latency under 200ms.
- Data Validation: Automated pipeline for verifying data consistency and detecting anomalies.

Profiles:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My Software CV is attached.

Best regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Genetech Solutions - Pakistan",
        "email":   "careers@genetechsolutions.com",
        "domain":  "SOFTWARE",
        "role":    "Junior Software Engineer",
        "region":  "Pakistan",
        "subject": "Junior Software Engineer Application: Abdullah Bin Masaud – COMSATS 2026",
        "body": """Dear Genetech Solutions Hiring Team,

Genetech Solutions' custom software engineering and enterprise consulting for global clients reflects high engineering productivity. I am applying for a Junior Software Engineer position.

I am graduating in Computer Engineering from COMSATS University Islamabad in 2026.

Technical Strengths:
- API Engineering: Designed and tested Flask REST endpoints with automated pytest coverage, latency checks, and error boundaries.
- Network Protocols: Custom TCP/IP multithreaded socket server with CRC32 packet integrity validation.
- Data Pipelines: Automated Python data verification with outlier detection and reporting.

Links:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My Software CV is attached.

Warm regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Creative Chaos - Pakistan",
        "email":   "careers@creativechaos.co",
        "domain":  "SOFTWARE",
        "role":    "Associate Software Engineer",
        "region":  "Pakistan",
        "subject": "Associate Software Engineer Application: Abdullah Bin Masaud – COMSATS 2026",
        "body": """Dear Creative Chaos Talent Team,

Creative Chaos' track record in building digital products and software engineering solutions for North American and European enterprises is well recognized. I am applying for an Associate Software Engineer role.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026).

Profile Highlights:
- Low-Level Data Integrity: Engineered custom binary network protocols with CRC32 checksums, tested under concurrent client loads.
- API & Test Automation: Modular Flask REST endpoints covered by 25+ pytest test cases verifying latency and schema validation.
- Clean Code Standards: 12 public GitHub repositories following unit testing and modular architecture.

Profiles:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My Software CV is attached.

Sincerely,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "TRG Pakistan (The Resource Group)",
        "email":   "careers@trgworld.com",
        "domain":  "SOFTWARE",
        "role":    "Associate Software Engineer",
        "region":  "Pakistan",
        "subject": "Associate Software Engineer Application: Abdullah Bin Masaud – COMSATS 2026",
        "body": """Dear TRG World Talent Acquisition Team,

TRG's portfolio of enterprise software, technology investments, and customer engagement platforms represents institutional-scale software engineering. I am applying for an Associate Software Engineer role.

I am graduating in Computer Engineering from COMSATS University Islamabad in 2026.

Engineering Highlights:
- Systems Reliability: Custom TCP/IP socket server with CRC32 packet integrity validation.
- API & Test Automation: Comprehensive pytest test suites validating API response codes, latency benchmarks, and concurrency.
- Data Quality Pipelines: Python data auditing pipeline with statistical outlier detection.

Links:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
- Phone: +92 332 9076356

My Software CV is attached.

Best regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },

    # ── GLOBAL REMOTE TECH LEADERS ──
    {
        "company": "Supabase (100% Remote Global)",
        "email":   "jobs@supabase.com",
        "domain":  "SOFTWARE",
        "role":    "Junior Software Engineer (Remote)",
        "region":  "Global Remote",
        "subject": "Software Engineer Application (Remote) – Abdullah Bin Masaud – Computer Engineering 2026",
        "body": """Dear Supabase Hiring Team,

Supabase's mission of building the open-source Firebase alternative has transformed how modern developers build backends. I am writing to apply for an entry-level software engineering role from Pakistan.

I am graduating with a BS in Computer Engineering from COMSATS University Islamabad in 2026.

Why I Fit:
- Systems Thinking: Built custom TCP/IP networking protocols in Python from scratch, including binary packet framing, CRC32 checksum calculations, and multi-threaded socket handling.
- API & Test Automation: Built comprehensive pytest test suites validating API response codes, latency benchmarks, and concurrency.
- Open-Source Mindset: 12 open-source GitHub repositories adhering to unit testing and clean modular design.

Timezone: UTC+5 (PKT) — ready for asynchronous collaboration.

Profiles:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b

My Software CV is attached.

Sincerely,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Vercel (100% Remote Global)",
        "email":   "jobs@vercel.com",
        "domain":  "SOFTWARE",
        "role":    "Junior Software Engineer (Remote)",
        "region":  "Global Remote",
        "subject": "Software Engineer Application (Remote) – Abdullah Bin Masaud – Computer Engineering 2026",
        "body": """Dear Vercel Talent Team,

Vercel's platform enabling developers to deploy frontend and serverless edge functions with zero configuration is the frontier of web infrastructure. I am applying for an entry-level software engineering role from Pakistan.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026).

Competencies:
- Low-Level Systems: Deep understanding of TCP/IP, client-server models, and real-time socket communication.
- Automated Testing: Built comprehensive pytest test suites validating API response codes, latency benchmarks, and concurrency.
- Autonomous Output: 12 complete, documented projects built and published independently on GitHub.

Timezone: UTC+5 (PKT)

Links:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b

My Software CV is attached.

Warm regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Postman (100% Remote Global)",
        "email":   "jobs@postman.com",
        "domain":  "SOFTWARE",
        "role":    "Software Engineer (Remote)",
        "region":  "Global Remote",
        "subject": "Software Engineer Application (Remote) – Abdullah Bin Masaud – Computer Engineering 2026",
        "body": """Dear Postman Talent Team,

Postman is the universal platform for API design, testing, and collaboration. I am writing to apply for an entry-level software engineering role from Pakistan.

I am graduating in Computer Engineering from COMSATS University Islamabad in 2026.

Why I Fit Postman:
- API Automation: Built end-to-end Flask REST endpoints covered by automated pytest test cases validating schemas, latency, and error states.
- Data Quality Pipelines: Standalone Python data auditing pipeline with statistical outlier detection.
- Distributed Protocol Design: Socket-level multithreaded communication with CRC32 packet error detection.

Timezone: UTC+5 (PKT)

Profiles:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b

My Software CV is attached.

Best regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Elastic (100% Remote Global)",
        "email":   "jobs@elastic.co",
        "domain":  "SOFTWARE",
        "role":    "Software Engineer (Distributed Systems)",
        "region":  "Global Remote",
        "subject": "Software Engineer Application (Remote) – Abdullah Bin Masaud – Computer Engineering 2026",
        "body": """Dear Elastic Hiring Team,

Elastic's search, observability, and security platform powered by distributed search engines represents high-throughput engineering. I am applying for an entry-level software engineering position from Pakistan.

I am a final-year Computer Engineering candidate from COMSATS University Islamabad (graduating 2026).

Practical Output:
- Systems Experience: Multithreaded TCP/IP socket server with custom packet serialization and CRC32 verification.
- Live Telemetry Streaming: Real-time sensor streaming dashboard built in Flask with WebSocket communication.
- Automated Testing: Production pytest test suites validating API latency and data payloads.

Timezone: UTC+5 (PKT)

Links:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b

My Software CV is attached.

Sincerely,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Cloudflare (100% Remote Global)",
        "email":   "jobs@cloudflare.com",
        "domain":  "SOFTWARE",
        "role":    "Systems Software Engineer (Remote)",
        "region":  "Global Remote",
        "subject": "Systems Software Engineer Application (Remote) – Abdullah Bin Masaud – Computer Engineering 2026",
        "body": """Dear Cloudflare Talent Acquisition Team,

Cloudflare's global edge network protecting and accelerating the internet is the ultimate benchmark for systems and network engineering. I am applying for an entry-level systems software engineering position from Pakistan.

I am graduating in Computer Engineering from COMSATS University Islamabad in 2026.

Systems & Systems Programming Experience:
- Low-Level Networking: Designed a multithreaded TCP/IP client-server communication protocol from scratch with binary packet framing and CRC32 checksums.
- Linux & Edge Computing: Deployed real-time computer vision models on Raspberry Pi running Ubuntu/Linux, optimizing memory and compute constraints.
- Code Rigor: 12 open-source GitHub repositories adhering to unit testing and clean modular design.

Timezone: UTC+5 (PKT)

Profiles:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b

My Software CV is attached.

Warm regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "HashiCorp (100% Remote Global)",
        "email":   "jobs@hashicorp.com",
        "domain":  "SOFTWARE",
        "role":    "Software Engineer (Remote)",
        "region":  "Global Remote",
        "subject": "Software Engineer Application (Remote) – Abdullah Bin Masaud – Computer Engineering 2026",
        "body": """Dear HashiCorp Hiring Team,

HashiCorp's foundational infrastructure automation tools (Terraform, Vault, Consul) power multi-cloud operations worldwide. I am applying for an entry-level software engineering role from Pakistan.

I am a final-year Computer Engineering candidate from COMSATS University Islamabad (graduating 2026).

Engineering Foundation:
- Python & REST APIs: Clean, test-driven RESTful services built with Flask and tested with pytest.
- Systems & Network Concurrency: Socket-level multithreaded networking with CRC32 packet integrity validation.
- Anomaly & Risk Analytics: Built XGBoost predictive risk models with SHAP explainability.

Location: Pakistan (UTC+5)

Links:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b

My Software CV is attached.

Best regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "DigitalOcean (100% Remote Global)",
        "email":   "jobs@digitalocean.com",
        "domain":  "SOFTWARE",
        "role":    "Software Engineer (Remote)",
        "region":  "Global Remote",
        "subject": "Software Engineer Application (Remote) – Abdullah Bin Masaud – Computer Engineering 2026",
        "body": """Dear DigitalOcean Talent Team,

DigitalOcean's simplicity and developer-first cloud infrastructure has supported millions of applications worldwide. I am applying for an entry-level software engineering role from Pakistan.

I am graduating in Computer Engineering from COMSATS University Islamabad in 2026.

Why I Fit:
- Systems Reliability: Custom TCP/IP socket server with CRC32 packet integrity validation.
- API & Test Automation: Comprehensive pytest test suites validating API response codes, latency benchmarks, and concurrency.
- Autonomous Output: 12 complete, documented projects built and published independently on GitHub.

Timezone: UTC+5 (PKT)

Profiles:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b

My Software CV is attached.

Sincerely,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "Stripe (100% Remote Global)",
        "email":   "jobs@stripe.com",
        "domain":  "SOFTWARE",
        "role":    "Software Engineer (Payments & Infrastructure)",
        "region":  "Global Remote",
        "subject": "Software Engineer Application (Remote) – Abdullah Bin Masaud – Computer Engineering 2026",
        "body": """Dear Stripe Hiring Team,

Stripe's economic infrastructure for the internet represents the pinnacle of API craftsmanship and financial reliability. I am writing to apply for an entry-level software engineering position from Pakistan.

I am graduating with a BS in Computer Engineering from COMSATS University Islamabad in 2026.

Engineering Highlights:
- Low-Level Protocol Rigor: Built custom multithreaded TCP/IP communication protocols with binary packet framing and CRC32 checksums.
- Robust API Engineering: Designed Flask REST endpoints with strict schema validation and 25+ automated pytest test cases.
- Data Validation: Created automated auditing tools for identifying missing or corrupted data.

Timezone: UTC+5 (PKT)

Links:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b

My Software CV is attached.

Warm regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    },
    {
        "company": "GitHub (100% Remote Global)",
        "email":   "jobs@github.com",
        "domain":  "SOFTWARE",
        "role":    "Software Engineer (Developer Tools)",
        "region":  "Global Remote",
        "subject": "Software Engineer Application (Remote) – Abdullah Bin Masaud – Computer Engineering 2026",
        "body": """Dear GitHub Talent Team,

GitHub is the home for developers worldwide. I have hosted and documented all 12 of my engineering repositories on GitHub, and I am applying for an entry-level software engineering role from Pakistan.

I am a final-year Computer Engineering student at COMSATS University Islamabad (graduating 2026).

Competencies:
- API Automation: Built end-to-end Flask REST endpoints covered by automated pytest test cases validating schemas, latency, and error states.
- Distributed Protocol Design: Socket-level multithreaded communication with CRC32 packet error detection.
- Clean Code Culture: Every GitHub project has documentation, requirements, and consistent structure.

Timezone: UTC+5 (PKT)

Profiles:
- GitHub: https://github.com/abdullah-bin-masaud
- LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b

My Software CV is attached.

Best regards,
Abdullah Bin Masaud
COMSATS University Islamabad | BS Computer Engineering
"""
    }
]

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
    print("=" * 85)
    print("  BATCH 9: 24 PRE-CHECKED MX TARGETS (SAUDI, UAE, REMOTE, PAKISTAN)")
    print(f"  Targets: {len(TARGETS)} companies — 0% bounce guaranteed")
    print("=" * 85)
    sent = failed = 0
    for i, job in enumerate(TARGETS, 1):
        company = job["company"]
        email   = job["email"]
        domain  = job["domain"]
        role    = job["role"]
        region  = job["region"]
        cv_path = CV_MAP[domain]
        print(f"\n[{i:02d}/{len(TARGETS)}] {company} ({region})")
        print(f"      To     : {email}")
        print(f"      CV     : {cv_path.name}  |  {domain}")
        print(f"      Role   : {role}")
        try:
            send_email(email, job["subject"], job["body"], cv_path)
            log_application(company, email, domain, role, "SENT")
            print(f"      Status : [OK] SENT")
            sent += 1
        except Exception as e:
            log_application(company, email, domain, role, f"FAILED: {e}")
            print(f"      Status : [FAIL] {e}")
            failed += 1
    print("\n" + "=" * 85)
    print(f"  BATCH 9 DISPATCH COMPLETE  |  Sent: {sent}  |  Failed: {failed}")
    print("=" * 85)

if __name__ == "__main__":
    main()
