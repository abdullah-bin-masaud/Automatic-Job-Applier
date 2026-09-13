"""
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
