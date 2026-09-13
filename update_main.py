from pathlib import Path

BASE_DIR = Path(r"C:\Users\Lenovo\Desktop\Projects\Automated-Job-Applier")

MAIN_CLI_PY = '''"""
Automated Job Hunting Cockpit — Interactive CLI.
Run: py main.py
"""
import sys
import os
import csv
from pathlib import Path

PROJECT_DIR = Path(__file__).parent
sys.path.insert(0, str(PROJECT_DIR))

from cv_matcher import classify_job
from email_generator import generate_email_draft
from linkedin_indeed_copilot import generate_pitch
from tracker import log_application
from gmail_sender import send_email_via_gmail

DEFAULT_APP_PWD = "vzpvxrlhutflfyak"


def menu():
    print("=" * 65)
    print("  ABDULLAH BIN MASAUD - AUTOMATED JOB APPLICATION ENGINE")
    print("=" * 65)
    print("1. [Interactive] Analyze a Job & Auto-Pick Winning CV")
    print("2. [Direct Email Engine] Auto-Send Applications to Verified Companies")
    print("3. [Draft Generator] Create .eml Draft Files in drafts/ Folder")
    print("4. [LinkedIn / Indeed] Generate 1-Click Pitch & Answers for a Job Post")
    print("5. [Tracker] View All Applied Jobs History")
    print("6. Exit")
    print("=" * 65)

    choice = input("Select an option (1-6): ").strip()
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


def process_direct_gmail_send():
    csv_path = PROJECT_DIR / "jobs_to_apply.csv"
    if not csv_path.exists():
        print(f"[!] {csv_path} not found.")
        return

    pwd = os.environ.get("GMAIL_APP_PASSWORD", DEFAULT_APP_PWD).strip()

    print("\\n" + "=" * 65)
    print("  AUTOMATED DIRECT GMAIL DISPATCH")
    print("=" * 65)
    print(f"[*] Authenticated Sender: abdullahmasaud10@gmail.com")

    with open(csv_path, mode="r", encoding="utf-8") as f:
        reader = list(csv.DictReader(f))
        print(f"[*] Loaded {len(reader)} target companies from jobs_to_apply.csv\\n")

        for idx, row in enumerate(reader, 1):
            company = row["Company"]
            role = row["Role"]
            channel = row["Channel"]
            contact = row["Contact_or_URL"]
            desc = row["Job_Description"]

            res = classify_job(role, desc)

            if channel.lower() == "email" and "@" in contact:
                subject = f"Application: {role} - Abdullah Bin Masaud (COMSATS Grad)"
                projects_text = ""
                for p in res["github_projects"]:
                    projects_text += f"  * {p['name']}: {p['desc']}\\n    Live Code: {p['url']}\\n\\n"

                body = f"""Dear {company} Hiring Team,

I am writing to express my strong interest in the {role} role at {company}. I recently completed my Bachelor of Science in Computer Engineering from COMSATS University Islamabad, Abbottabad Campus, specializing in {res['domain_name']}.

To demonstrate my hands-on technical capabilities, I have built and open-sourced production-ready projects directly relevant to this position:

{projects_text}
I have attached my tailored resume ({res['cv_file_name']}) for your consideration. You can also view all 12 of my active engineering repositories on my GitHub: https://github.com/abdullah-bin-masaud.

I would welcome the opportunity for a brief 15-minute conversation to discuss how my technical skills can contribute to {company}.

Thank you for your time and consideration.

Best regards,

Abdullah Bin Masaud
+92 332 9076356 | abdullahmasaud10@gmail.com
LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
GitHub: https://github.com/abdullah-bin-masaud
"""
                cv_full_path = res["cv_full_path"]
                print(f"[{idx}/{len(reader)}] Sending application for '{role}' at {company} to <{contact}>...")
                print(f"      -> Attached: {res['cv_file_name']}")

                result = send_email_via_gmail(contact, subject, body, cv_full_path, pwd)
                if result.get("success"):
                    print(f"      [✓] SENT SUCCESSFULLY! (Check your Gmail Sent folder)")
                    log_application(company, role, "Email (Gmail Direct)", res["cv_file_name"], "Sent via Gmail SMTP")
                else:
                    print(f"      [!] Error sending: {result.get('message')}")
                    log_application(company, role, "Email (Failed)", res["cv_file_name"], f"Error: {result.get('message')}")

            else:
                log_application(company, role, channel, res["cv_file_name"], f"Prepared for {channel}")
                print(f"[{idx}/{len(reader)}] [{res['cv_file_name']}] Prepared {channel} target for {company} ({role})")

    print("\\n" + "=" * 65)
    print("  ALL APPLICATIONS PROCESSED & SENT!")
    print("  Check your Gmail Sent folder: https://mail.google.com")
    print("=" * 65)


def process_draft_batch():
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

            res = classify_job(role, desc)

            if channel.lower() == "email":
                draft_path = generate_email_draft(company, role, contact, res, drafts_dir)
                log_application(company, role, "Email", res["cv_file_name"], f"Draft created: {draft_path.name}")
                print(f"[+] [{res['cv_file_name']}] Generated Draft for {company} ({role}) -> {draft_path.name}")
                count += 1

    print(f"\\n[*] Batch draft processing finished. Draft files created in: {drafts_dir}")


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
            process_direct_gmail_send()
        elif c == "3":
            process_draft_batch()
        elif c == "4":
            generate_copilot_pitch()
        elif c == "5":
            view_tracker()
        elif c == "6":
            print("[*] Exiting. Good luck with your applications!")
            break
        else:
            print("[!] Invalid option. Choose 1-6.")
        input("\\nPress Enter to continue...")
'''

target_main = BASE_DIR / "main.py"
target_main.write_text(MAIN_CLI_PY.strip() + "\n", encoding="utf-8")
print(f"Updated main.py at {target_main}")
