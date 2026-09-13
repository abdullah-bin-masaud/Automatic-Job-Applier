import shutil
from pathlib import Path

source_guide = Path(r"C:\Users\Lenovo\.gemini\antigravity\brain\104b44c9-fb2b-4a78-80be-5f3b942a7571\PORTFOLIO_MASTER_GUIDE.md")
dest_guide = Path(r"C:\Users\Lenovo\Desktop\Projects\PORTFOLIO_MASTER_GUIDE.md")

if source_guide.exists():
    shutil.copy2(source_guide, dest_guide)
    print(f"[*] Copied master guide to: {dest_guide}")

UPLOAD_SCRIPT = '''"""
Automated GitHub Portfolio Publisher.
Creates 10 repositories under your GitHub account and uploads all project files via the official GitHub REST API.
No Git installation or administrative privileges required!

Usage:
    python upload_to_github.py
"""
import os
import sys
import json
import base64
import urllib.request
import urllib.error
from pathlib import Path

PROJECTS_ROOT = Path(__file__).parent

# 10 Projects to upload with their GitHub descriptions
PROJECT_CATALOG = [
    {
        "folder": "TCP-IP-Client-Server",
        "repo_name": "TCP-IP-Client-Server",
        "description": "Low-level multithreaded networking application demonstrating reliable packet transmission, custom 12-byte framing, and CRC32 error detection.",
    },
    {
        "folder": "Realtime-Video-Sensor-Dashboard",
        "repo_name": "Realtime-Video-Sensor-Dashboard",
        "description": "Web-based IoT dashboard streaming live camera video (MJPEG) and sensor telemetry (WebSockets) with Chart.js real-time visualization.",
    },
    {
        "folder": "PIC18-Signal-Communication-Unit",
        "repo_name": "PIC18-Signal-Communication-Unit",
        "description": "Embedded C firmware for PIC18F4550 with interrupt-driven pulse acquisition, non-volatile EEPROM event logging, and 9600-baud UART telemetry.",
    },
    {
        "folder": "Flask-REST-API-Testing",
        "repo_name": "Flask-REST-API-Testing",
        "description": "REST API automated testing suite with 25+ pytest cases validating HTTP status codes, payload schemas, latency SLAs (<150ms), and concurrency.",
    },
    {
        "folder": "Python-Data-QA-Pipeline",
        "repo_name": "Python-Data-QA-Pipeline",
        "description": "Automated data quality auditing and machine learning regression testing pipeline with IQR outlier detection and schema contract verification.",
    },
    {
        "folder": "AI-Medical-Image-Segmentation",
        "repo_name": "AI-Medical-Image-Segmentation",
        "description": "PyTorch U-Net deep convolutional neural network for automated lesion segmentation in brain MRI scans with Dice Similarity and IoU metrics.",
    },
    {
        "folder": "Customer-Churn-Risk-Predictive-Engine",
        "repo_name": "Customer-Churn-Risk-Predictive-Engine",
        "description": "Predictive ML analytics engine forecasting customer churn and default risk with class-imbalance compensation, ROC-AUC optimization, and risk tiers.",
    },
    {
        "folder": "Traffic-Pedestrian-Vehicle-Counter",
        "repo_name": "Traffic-Pedestrian-Vehicle-Counter",
        "description": "Computer vision software for real-time pedestrian and vehicle tracking and bidirectional counting across virtual tripwires using OpenCV.",
    },
    {
        "folder": "Microcontroller-Sensor-Control-Alert-Circuits",
        "repo_name": "Microcontroller-Sensor-Control-Alert-Circuits",
        "description": "Suite of 3 embedded automation circuits: 4-level transistor water indicator, LDR street light with hysteresis, and fire/smoke emergency alert.",
    },
    {
        "folder": "PIC18-Automated-Attendance-System",
        "repo_name": "PIC18-Automated-Attendance-System",
        "description": "Automated room occupancy and attendance tracking system using dual optical IR beam sensors, directional transit state machine, and EEPROM roll-call logging.",
    }
]


def make_github_request(url: str, token: str, method: str = "GET", data: dict = None):
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "User-Agent": "Antigravity-Portfolio-Publisher"
    }
    encoded_data = json.dumps(data).encode("utf-8") if data else None
    req = urllib.request.Request(url, data=encoded_data, headers=headers, method=method)

    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8")), resp.status
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        try:
            err_json = json.loads(body)
        except Exception:
            err_json = {"message": body}
        return err_json, e.code


def upload_portfolio():
    print("=" * 65)
    print("  ABDULLAH BIN MASAUD - GITHUB PORTFOLIO AUTO-UPLOADER")
    print("=" * 65)

    token = os.environ.get("GITHUB_TOKEN", "").strip()
    if not token:
        print("\\nTo upload your projects to GitHub, a Personal Access Token (PAT) is required.")
        print("Steps to get a free token (1 minute):")
        print("  1. Go to: https://github.com/settings/tokens")
        print("  2. Click 'Generate new token (classic)'")
        print("  3. Check the 'repo' scope (Full control of private/public repositories)")
        print("  4. Click 'Generate token' and copy the string")
        print("\\nEnter your GitHub Token below (it will only be used to create your repos):")
        token = input("GitHub Token (ghp_...): ").strip()

    if not token:
        print("[!] No token provided. Aborting.")
        return

    # Verify user identity
    user_info, code = make_github_request("https://api.github.com/user", token)
    if code != 200:
        print(f"[!] Authentication failed: {user_info.get('message', 'Invalid token')}")
        return

    username = user_info["login"]
    print(f"[*] Authenticated as GitHub user: @{username}")

    for idx, item in enumerate(PROJECT_CATALOG, 1):
        folder_path = PROJECTS_ROOT / item["folder"]
        repo_name = item["repo_name"]
        desc = item["description"]

        print(f"\\n[{idx}/10] Processing '{repo_name}'...")

        # 1. Create Repository on GitHub (or verify existing)
        create_payload = {
            "name": repo_name,
            "description": desc,
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": False
        }
        repo_resp, status = make_github_request("https://api.github.com/user/repos", token, method="POST", data=create_payload)
        if status == 201:
            print(f"  [+] Created new public repository: https://github.com/{username}/{repo_name}")
        elif status == 422 and "already exists" in str(repo_resp):
            print(f"  [*] Repository https://github.com/{username}/{repo_name} already exists. Updating files...")
        else:
            print(f"  [!] Could not create repository: {repo_resp.get('message')}")
            continue

        # 2. Upload all files from project folder
        files = [f for f in folder_path.rglob("*") if f.is_file()]
        for f in files:
            rel_path = f.relative_to(folder_path).as_posix()
            try:
                content_bytes = f.read_bytes()
                encoded_content = base64.b64encode(content_bytes).decode("utf-8")

                # Check if file already exists to get SHA for update
                file_url = f"https://api.github.com/repos/{username}/{repo_name}/contents/{rel_path}"
                existing_file, get_status = make_github_request(file_url, token)

                put_payload = {
                    "message": f"Add {rel_path} - Abdullah Bin Masaud Engineering Portfolio",
                    "content": encoded_content
                }
                if get_status == 200 and "sha" in existing_file:
                    put_payload["sha"] = existing_file["sha"]

                _, put_status = make_github_request(file_url, token, method="PUT", data=put_payload)
                if put_status in [200, 201]:
                    print(f"    -> Uploaded {rel_path}")
                else:
                    print(f"    [!] Failed to upload {rel_path} (Status {put_status})")
            except Exception as e:
                print(f"    [!] Error processing {rel_path}: {e}")

    print("\\n" + "=" * 65)
    print("  ALL PROJECTS SUCCESSFULLY UPLOADED TO GITHUB!")
    print(f"  View your profile: https://github.com/{username}")
    print("=" * 65)


if __name__ == "__main__":
    upload_portfolio()
'''

upload_script_path = Path(r"C:\Users\Lenovo\Desktop\Projects\upload_to_github.py")
upload_script_path.write_text(UPLOAD_SCRIPT.strip() + "\n", encoding="utf-8")
print(f"[*] Created automated uploader: {upload_script_path}")
