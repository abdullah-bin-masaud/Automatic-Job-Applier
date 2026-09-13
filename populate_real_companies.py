import csv
from pathlib import Path

csv_path = Path(r"C:\Users\Lenovo\Desktop\Projects\Automated-Job-Applier\jobs_to_apply.csv")

REAL_COMPANIES = [
    # 1. Embedded Systems & Hardware Engineering (CV__H)
    {
        "Company": "CARE (Center for Advanced Research in Engineering)",
        "Role": "Junior Embedded Firmware Engineer",
        "Channel": "Email",
        "Contact_or_URL": "careers@carepvtltd.com",
        "Job_Description": "Seeking fresh Computer/Electrical Engineering graduate for embedded C firmware development, PIC/ARM microcontrollers, UART/SPI serial protocols, Proteus simulation, and hardware-software integration in Islamabad."
    },
    {
        "Company": "MicroTech Industries",
        "Role": "Embedded Systems Trainee Engineer",
        "Channel": "Email",
        "Contact_or_URL": "careers@microtechx.com",
        "Job_Description": "Hiring fresh engineers for smart metering and IoT hardware. Hands-on experience with embedded C, microcontroller programming, sensor interfacing, and EEPROM logging required."
    },
    {
        "Company": "LMKT",
        "Role": "IoT & Hardware Solutions Associate",
        "Channel": "Email",
        "Contact_or_URL": "careers@lmkt.com",
        "Job_Description": "Opportunity for entry-level engineer in IoT device prototyping, microcontroller sensors, embedded controllers, and hardware telemetry systems in Islamabad."
    },

    # 2. Artificial Intelligence & Computer Vision (CV__A)
    {
        "Company": "Arbisoft",
        "Role": "Junior Computer Vision & AI Engineer",
        "Channel": "Email",
        "Contact_or_URL": "careers@arbisoft.com",
        "Job_Description": "Looking for entry-level AI Engineer with strong Python, OpenCV, YOLO object detection, PyTorch convolutional neural networks (CNNs), and ONNX runtime optimization for edge devices."
    },
    {
        "Company": "Devsinc",
        "Role": "Associate Machine Learning Engineer",
        "Channel": "Email",
        "Contact_or_URL": "jobs@devsinc.com",
        "Job_Description": "Hiring fresh graduates with solid Python foundations, computer vision, deep learning models, image segmentation, and data analysis using Scikit-Learn and Pandas."
    },
    {
        "Company": "Emumba",
        "Role": "AI / Deep Learning Trainee",
        "Channel": "Email",
        "Contact_or_URL": "careers@emumba.com",
        "Job_Description": "Seeking high-potential engineering graduates in Islamabad for computer vision, PyTorch model training, image processing with OpenCV, and machine learning pipelines."
    },
    {
        "Company": "10Pearls",
        "Role": "Junior AI & Data Engineer",
        "Channel": "Email",
        "Contact_or_URL": "careers@10pearls.com",
        "Job_Description": "Entry-level position for engineers skilled in Python, predictive modeling, machine learning classification, and data analytics pipelines."
    },

    # 3. Telecommunications & Network Engineering (CV__T)
    {
        "Company": "Nayatel",
        "Role": "Associate Network Operations (NOC) Engineer",
        "Channel": "Email",
        "Contact_or_URL": "hr@nayatel.com",
        "Job_Description": "Hiring fresh Computer/Telecom engineers in Islamabad for IP networking, TCP/IP protocol troubleshooting, routing and switching, network socket telemetry, and Wireshark packet analysis."
    },
    {
        "Company": "PTCL (Pakistan Telecommunication Company Ltd)",
        "Role": "Graduate Trainee Engineer - Networks",
        "Channel": "Email",
        "Contact_or_URL": "careers@ptcl.net.pk",
        "Job_Description": "National graduate trainee program for telecommunications, IP networking, core routing/switching infrastructure, TCP/IP protocol suite, and telecom operations in Islamabad."
    },
    {
        "Company": "Cybernet",
        "Role": "Junior IP Network Systems Engineer",
        "Channel": "Email",
        "Contact_or_URL": "careers@cyber.net.pk",
        "Job_Description": "Opportunity in enterprise IP infrastructure, network monitoring, TCP/IP socket troubleshooting, and hardware serial communication telemetry."
    },
    {
        "Company": "Jazz (VEON)",
        "Role": "Network Engineering Trainee",
        "Channel": "Email",
        "Contact_or_URL": "careers@jazz.com.pk",
        "Job_Description": "Hiring engineering graduates for mobile and enterprise network operations, packet transmission monitoring, and telecommunications infrastructure."
    },

    # 4. Software Engineering & Quality Assurance (CV__S)
    {
        "Company": "Systems Limited",
        "Role": "Associate Software QA & Automation Engineer",
        "Channel": "Email",
        "Contact_or_URL": "talent@systemsltd.com",
        "Job_Description": "Hiring fresh graduates for test automation, Python testing with pytest, REST API endpoint validation, SQL database queries, and regression testing."
    },
    {
        "Company": "Contour Software",
        "Role": "Trainee Software Quality Assurance Engineer",
        "Channel": "Email",
        "Contact_or_URL": "careers@contour-software.com",
        "Job_Description": "Entry-level QA position in Islamabad: automated API testing, regression test suite execution, bug lifecycle tracking, and data validation scripts."
    },
    {
        "Company": "VentureDive",
        "Role": "Junior Software Engineer - Backend & QA",
        "Channel": "Email",
        "Contact_or_URL": "careers@venturedive.com",
        "Job_Description": "Seeking fresh Computer Engineering graduate with Python programming, Flask/REST API development, automated testing, and relational database management."
    }
]

with open(csv_path, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["Company", "Role", "Channel", "Contact_or_URL", "Job_Description"])
    writer.writeheader()
    writer.writerows(REAL_COMPANIES)

print(f"[*] Populated {len(REAL_COMPANIES)} real Pakistani engineering companies into {csv_path}")
