import sys, csv
from pathlib import Path

sys.path.insert(0, r"C:\Users\Lenovo\Desktop\Projects\Automated-Job-Applier")
from cv_matcher import classify_job
from email_generator import generate_email_draft

csv_path = Path(r"C:\Users\Lenovo\Desktop\Projects\Automated-Job-Applier\jobs_to_apply.csv")
drafts_dir = Path(r"C:\Users\Lenovo\Desktop\Projects\Automated-Job-Applier\drafts")

with open(csv_path, "r", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        match = classify_job(row["Role"], row["Job_Description"])
        draft = generate_email_draft(row["Company"], row["Role"], row["Contact_or_URL"], match, drafts_dir)
        kb = draft.stat().st_size // 1024
        print(f"Generated: {draft.name} | CV: {match['cv_file_name']} ({kb} KB)")
