"""
Automated Job Hunting Cockpit — Interactive CLI.
Run: python main.py
"""
import sys
import os
import csv
from pathlib import Path

# Load environment variables if python-dotenv is available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

PROJECT_DIR = Path(__file__).parent
sys.path.insert(0, str(PROJECT_DIR))

from cv_matcher import classify_job
from email_generator import generate_email_draft
from linkedin_indeed_copilot import generate_pitch
from tracker import log_application
from gmail_sender import send_email_via_gmail


def menu():
    print("=" * 65)
    print("      AUTOMATED MULTI-CHANNEL JOB APPLICATION COCKPIT")
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
    print("\n--- PASTE JOB DETAILS ---")
    title = input("Job Title: ").strip()
    print("Enter Job Description keywords (e.g. Embedded C, Microcontroller OR YOLO, PyTorch, QA):")
    desc = input("Job Description / Keywords: ").strip()

    res = classify_job(title, desc)
    print("\n" + "=" * 55)
    print(f"  RECOMMENDED CV  : {res['cv_file_name']}")
    print(f"  TARGET DOMAIN   : {res['domain_name']}")
    print(f"  MATCH SCORE     : {res['score']} points")
    print(f"  MATCHED KEYWORDS: {', '.join(res['matched_keywords']) if res['matched_keywords'] else 'Default domain assigned'}")
    print("=" * 55)
    print("Recommended GitHub Repos to Feature:")
    for p in res["github_projects"]:
        print(f"  * {p['name']}: {p['url']}")


def process_direct_gmail_send():
    csv_path = PROJECT_DIR / "jobs_to_apply.csv"
    if not csv_path.exists():
        print(f"[!] {csv_path} not found. Please create one based on jobs_to_apply.example.csv.")
        return

    sender_email = os.getenv("SENDER_EMAIL")
    app_pwd = os.getenv("GMAIL_APP_PASSWORD")

    if not sender_email or not app_pwd:
        print("[!] SENDER_EMAIL and GMAIL_APP_PASSWORD must be configured in your .env file.")
        return

    print(f"[*] Dispatching applications using sender: {sender_email}")
    confirm = input("Confirm direct send? (y/N): ").strip().lower()
    if confirm != "y":
        print("[*] Aborted.")
        return

    with open(csv_path, mode="r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        count = 0
        for row in reader:
            company = row.get("Company", "").strip()
            role = row.get("Role", "").strip()
            channel = row.get("Channel", "").strip()
            contact = row.get("Contact_or_URL", "").strip()
            desc = row.get("Job_Description", "").strip()

            if channel.lower() == "email" and "@" in contact:
                res = classify_job(role, desc)
                subject = f"Application: {role} - {os.getenv('SENDER_NAME', 'Candidate')}"
                body = f"Dear {company} Hiring Team,\n\nI am applying for the {role} position.\n"
                result = send_email_via_gmail(contact, subject, body, res["cv_full_path"], sender_email, app_pwd)
                status = "Sent" if result.get("success") else f"Failed: {result.get('error')}"
                log_application(company, role, "Direct Email", res["cv_file_name"], status)
                print(f"[+] [{status}] {company} - {role}")
                count += 1

    print(f"[*] Finished processing. Dispatched {count} applications.")


def process_draft_batch():
    csv_path = PROJECT_DIR / "jobs_to_apply.csv"
    if not csv_path.exists():
        print(f"[!] {csv_path} not found. Using jobs_to_apply.example.csv instead.")
        csv_path = PROJECT_DIR / "jobs_to_apply.example.csv"

    drafts_dir = PROJECT_DIR / "drafts"
    drafts_dir.mkdir(parents=True, exist_ok=True)

    with open(csv_path, mode="r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        count = 0
        for row in reader:
            company = row.get("Company", "").strip()
            role = row.get("Role", "").strip()
            channel = row.get("Channel", "").strip()
            contact = row.get("Contact_or_URL", "").strip()
            desc = row.get("Job_Description", "").strip()

            if channel.lower() == "email" and "@" in contact:
                res = classify_job(role, desc)
                draft_path = generate_email_draft(company, role, contact, res, drafts_dir)
                log_application(company, role, "Email Draft", res["cv_file_name"], f"Draft: {draft_path.name}")
                print(f"[+] Generated draft for {company} ({role}) -> {draft_path.name}")
                count += 1

    print(f"\n[*] Batch draft generation complete. Files created in: {drafts_dir}")


def generate_copilot_pitch():
    company = input("Company Name: ").strip()
    role = input("Job Title: ").strip()
    desc = input("Job Description / Keywords: ").strip()

    res = classify_job(role, desc)
    pitch_data = generate_pitch(company, role, res)

    print("\n" + "=" * 55)
    print(f"  1. ATTACH THIS RESUME FILE:")
    print(f"     -> {res['cv_full_path']}")
    print("\n  2. COPY & PASTE THIS SHORT NOTE:")
    print("-" * 55)
    print(pitch_data["pitch_note"])
    print("-" * 55)
    print("\n  3. STANDARD SCREENING ANSWERS:")
    for q, a in pitch_data["screening_answers"].items():
        print(f"     * {q} -> {a}")
    print("=" * 55)

    log_application(company, role, "LinkedIn/Indeed", res["cv_file_name"], "Copilot pitch generated")


def view_tracker():
    tracker_file = PROJECT_DIR / "applied_tracker.csv"
    if not tracker_file.exists():
        print("[*] No applied jobs logged yet.")
        return

    print("\n" + "=" * 65)
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
            print("[*] Exiting.")
            break
        else:
            print("[!] Invalid option. Choose 1-6.")
        input("\nPress Enter to continue...")
