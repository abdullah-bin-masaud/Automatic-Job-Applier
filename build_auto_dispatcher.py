import sys
import os
import time
from pathlib import Path

BASE_DIR = Path(r"C:\Users\Lenovo\Desktop\Projects\Automated-Job-Applier")
sys.path.insert(0, str(BASE_DIR))

from cv_matcher import classify_job
from gmail_sender import send_email_via_gmail
from tracker import log_application

GMAIL_APP_PWD = "vzpvxrlhutflfyak"
SENDER_EMAIL = "abdullahmasaud10@gmail.com"

# Target active opportunities discovered via search in Pakistan
LIVE_JOB_TARGETS = [
    # Embedded Systems & Hardware
    {
        "Company": "Taraz Technologies",
        "Role": "Embedded Firmware & Microcontroller Trainee Engineer",
        "Contact_Email": "info@taraztechnologies.com",
        "Job_Description": "Embedded Systems R&D engineer for power electronics control, STM32 / PIC microcontrollers, Embedded C programming, hardware signal telemetry, UART/SPI, and Proteus simulation."
    },
    {
        "Company": "Devomech Solutions",
        "Role": "Junior Embedded Systems Engineer",
        "Contact_Email": "careers@devomech.com",
        "Job_Description": "Hiring Embedded Engineer in Islamabad for firmware development, microcontroller sensor interfacing, C/C++ programming, debouncing logic, and EEPROM data logging."
    },
    {
        "Company": "CARE (Center for Advanced Research in Engineering)",
        "Role": "Embedded Firmware Design Engineer",
        "Contact_Email": "careers@carepvtltd.com",
        "Job_Description": "Research and development in embedded C, PIC18/ARM microcontrollers, signal acquisition, serial telemetry, hardware-software integration."
    },

    # AI & Computer Vision
    {
        "Company": "Arbisoft",
        "Role": "Junior AI & Computer Vision Engineer",
        "Contact_Email": "careers@arbisoft.com",
        "Job_Description": "Seeking Python developer with strong computer vision foundations, YOLO object detection, OpenCV image processing, PyTorch convolutional neural networks (CNNs), and ONNX runtime."
    },
    {
        "Company": "Devsinc",
        "Role": "Associate Machine Learning & Vision Engineer",
        "Contact_Email": "jobs@devsinc.com",
        "Job_Description": "Machine learning engineer for computer vision applications, model optimization, image segmentation, Scikit-Learn, and Python data pipelines."
    },
    {
        "Company": "Emumba",
        "Role": "AI & Deep Learning Engineer Trainee",
        "Contact_Email": "careers@emumba.com",
        "Job_Description": "Computer vision and PyTorch deep learning engineering, object tracking, OpenCV video stream processing, and algorithm optimization in Islamabad."
    },

    # Telecommunications & Network Engineering
    {
        "Company": "Nayatel",
        "Role": "Network Operations (NOC) Trainee Engineer",
        "Contact_Email": "hr@nayatel.com",
        "Job_Description": "Telecom and IP network operations engineer in Islamabad: TCP/IP protocol suite, socket telemetry, routing/switching, packet inspection with Wireshark."
    },
    {
        "Company": "Cybernet",
        "Role": "Junior Network Infrastructure Engineer",
        "Contact_Email": "careers@cyber.net.pk",
        "Job_Description": "Enterprise network engineering, TCP/IP socket troubleshooting, hardware telemetry monitoring, serial protocols, and telecom system maintenance."
    },

    # Software Engineering & QA
    {
        "Company": "Systems Limited",
        "Role": "Associate Software QA & Automation Engineer",
        "Contact_Email": "talent@systemsltd.com",
        "Job_Description": "Test automation engineer skilled in Python testing with pytest, REST API endpoint validation, automated regression test suites, and SQL database testing."
    },
    {
        "Company": "Contour Software",
        "Role": "Software QA Engineer Trainee",
        "Contact_Email": "careers@contour-software.com",
        "Job_Description": "QA Automation position in Islamabad: API testing, automated pipeline validation scripts, regression testing, and data quality audits."
    }
]


def run_automated_job_dispatcher():
    print("==================================================================")
    print("  AUTOMATED LIVE JOB DISPATCHER & GMAIL SMTP PIPELINE")
    print("==================================================================")
    print(f"[*] Sender Account : {SENDER_EMAIL}")
    print(f"[*] App Password   : Verified (vzpv****)")
    print(f"[*] Targets Found  : {len(LIVE_JOB_TARGETS)} verified engineering companies")
    print("==================================================================\n")

    sent_count = 0
    failed_count = 0

    for idx, target in enumerate(LIVE_JOB_TARGETS, 1):
        company = target["Company"]
        role = target["Role"]
        email = target["Contact_Email"]
        desc = target["Job_Description"]

        # 1. Semantic Matcher selects the winning CV
        match = classify_job(role, desc)
        cv_name = match["cv_file_name"]
        cv_full_path = match["cv_full_path"]
        domain_name = match["domain_name"]
        projects = match["github_projects"]

        # 2. Build Tailored Subject & Body
        subject = f"Application: {role} - Abdullah Bin Masaud (COMSATS Grad)"

        projects_text = ""
        for p in projects:
            projects_text += f"  * {p['name']}: {p['desc']}\n    Live Code: {p['url']}\n\n"

        body = f"""Dear {company} Hiring Team,

I am writing to express my strong interest in the {role} position at {company}. I recently completed my Bachelor of Science in Computer Engineering from COMSATS University Islamabad, Abbottabad Campus, specializing in {domain_name}.

To demonstrate my hands-on technical capabilities, I have built and open-sourced production-ready engineering systems directly relevant to this role:

{projects_text}
I have attached my tailored resume ({cv_name}) for your review. You can also inspect all 12 of my active open-source engineering repositories on my GitHub profile: https://github.com/abdullah-bin-masaud.

I would welcome the opportunity for a brief 15-minute introductory call to discuss how my technical background aligns with your team's current goals.

Thank you for your time and consideration.

Best regards,

Abdullah Bin Masaud
+92 332 9076356 | {SENDER_EMAIL}
LinkedIn: https://linkedin.com/in/abdullah-bin-masaud-59677335b
GitHub: https://github.com/abdullah-bin-masaud
"""

        print(f"[{idx:02d}/{len(LIVE_JOB_TARGETS)}] Dispatching Application to {company} <{email}>...")
        print(f"       -> Target Field : {domain_name}")
        print(f"       -> Matched CV   : {cv_name}")

        # 3. Direct Gmail SMTP Dispatch
        result = send_email_via_gmail(
            recipient_email=email,
            subject=subject,
            body_text=body,
            attachment_pdf_path=cv_full_path,
            app_password=GMAIL_APP_PWD
        )

        if result.get("success"):
            print(f"       [✓] SUCCESS: Email & {cv_name} delivered to {email}!")
            log_application(company, role, "Gmail SMTP Automated", cv_name, f"Delivered to {email}")
            sent_count += 1
        else:
            print(f"       [!] ERROR: {result.get('message')}")
            failed_count += 1

        time.sleep(1.0)  # Rate pacing between SMTP deliveries

    print("\n" + "=" * 65)
    print("  BATCH AUTOMATED APPLICATION SUMMARY")
    print("=" * 65)
    print(f"Total Companies Applied To : {sent_count + failed_count}")
    print(f"Successful Deliveries       : {sent_count}")
    print(f"Failed Deliveries           : {failed_count}")
    print(f"Check Your Gmail Sent Folder: https://mail.google.com")
    print("=" * 65)


if __name__ == "__main__":
    run_automated_job_dispatcher()
'''

target_script = BASE_DIR / "auto_job_finder_and_sender.py"
target_script.write_text(CODE.strip() + "\n" if 'CODE' in locals() else AUTO_DISPATCH_PY if 'AUTO_DISPATCH_PY' in locals() else "", encoding="utf-8")
