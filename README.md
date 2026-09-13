# Automatic Job Applier & Multi-Channel Outreach Engine

An intelligent, modular automated job application and outreach engine designed to streamline job hunting across direct email, LinkedIn, and Indeed. 

The system semantically classifies incoming job postings, scores requirements against candidate domain profiles (AI/Vision, Telecom/Networks, Embedded Systems, Software QA/Backend), automatically selects the best matching CV, and generates customized email outreach (or `.eml` drafts) with clickable project showcases and attached resumes.

---

## Architecture & Workflow

```text
               ┌───────────────────────────────┐
               │    Job Title & Description    │
               └──────────────┬────────────────┘
                              │
                              ▼
               ┌───────────────────────────────┐
               │         cv_matcher.py         │
               │  - Tokenizes job keywords     │
               │  - Scores domain profiles     │
               │  - Selects matching resume    │
               │  - Pairs relevant portfolio   │
               └──────────────┬────────────────┘
                              │
              ┌───────────────┴───────────────┐
              ▼                               ▼
   ┌────────────────────┐          ┌────────────────────┐
   │    Email Engine    │          │  Copilot Assistant │
   │ - EML Draft Maker  │          │ - LinkedIn pitches │
   │ - Direct SMTP Send │          │ - Screening answers│
   └──────────┬─────────┘          └──────────┬─────────┘
              │                               │
              └───────────────┬───────────────┘
                              ▼
               ┌───────────────────────────────┐
               │          tracker.py           │
               │  Logs history to CSV tracker  │
               └───────────────────────────────┘
```

---

## Core Features

- **Semantic Domain Matching**: Automatically scores job requirements across customizable domains:
  - **AI & Computer Vision**: PyTorch, OpenCV, YOLO, CNNs, Deep Learning, ONNX.
  - **Telecommunications & Networks**: TCP/IP, Sockets, Packet Routing, Wireshark, Protocols.
  - **Embedded Systems & Firmware**: C/C++, PIC18/ARM Microcontrollers, UART/SPI, Sensors.
  - **Software Engineering & QA**: REST API testing, Pytest, SQL, Data Validation.
- **Dynamic Project Portfolio Pairing**: Automatically embeds relevant GitHub repositories and achievements into cover pitches based on the detected domain.
- **Draft Generator (`.eml`)**: Creates standards-compliant `.eml` email files with your tailored cover letter and attached PDF resume—ready to review in Outlook, Thunderbird, or Apple Mail before sending.
- **Automated SMTP Mailer**: Secure SSL/TLS direct email dispatcher with support for Gmail App Passwords and custom SMTP relays.
- **LinkedIn & Indeed Copilot**: Generates one-click cover notes and answers to standard applicant screening questions.
- **Application Audit Tracker**: Persistently logs dates, target companies, roles, contact channels, and CV versions used into a clean CSV audit log.

---

## Project Structure

```text
Automatic-Job-Applier/
├── main.py                     # Interactive CLI cockpit orchestrating all modes
├── cv_matcher.py               # Keyword classification engine and domain scoring brain
├── email_generator.py          # E-mail template generator and .eml draft builder
├── gmail_sender.py             # Secure SSL SMTP delivery module with attachments
├── linkedin_indeed_copilot.py  # Quick pitch generator & screening Q&A copilot
├── tracker.py                  # CSV-based application audit and history logger
├── jobs_to_apply.example.csv   # Sample job input queue template
├── .env.example                # Environment configuration template
├── requirements.txt            # Minimal Python dependencies
└── README.md                   # Full documentation & setup guide
```

---

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/abdullah-bin-masaud/Automatic-Job-Applier.git
cd Automatic-Job-Applier
```

### 2. Install Dependencies
This project uses the Python standard library with optional extensions:
```bash
pip install -r requirements.txt
```

### 3. Configure Environment
Copy the example environment file and configure your credentials:
```bash
cp .env.example .env
```
Fill in your sender details in `.env`:
```env
SENDER_EMAIL=your_email@example.com
SENDER_NAME=Your Name
GMAIL_APP_PASSWORD=your_16_character_app_password
```

### 4. Setup Resumes and Job Queue
1. Place your specialized resume PDFs in a directory (e.g. `resumes/`) and configure the paths in `cv_matcher.py`.
2. Populate `jobs_to_apply.csv` (using `jobs_to_apply.example.csv` as a reference) with companies and job descriptions you want to target.

---

## Usage

Launch the interactive cockpit:
```bash
python main.py
```

### Interactive Menu Options:
1. **Analyze a Job & Auto-Pick Winning CV**: Paste any job description to view keyword matches, match scores, and recommended portfolio links.
2. **Direct Email Engine**: Automatically send tailored applications with attached CVs to companies listed in `jobs_to_apply.csv`.
3. **Draft Generator**: Batch-produce offline `.eml` drafts with attached resumes for manual inspection.
4. **LinkedIn / Indeed Pitch**: Generate tailored pitch messages and screening answers for job portals.
5. **Tracker**: View comprehensive historical application logs.

---

## License

MIT License - open for personal and commercial adaptation.
