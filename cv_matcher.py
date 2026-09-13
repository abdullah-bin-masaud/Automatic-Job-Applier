"""
Semantic CV Matcher & Classifier Brain.
Analyzes job titles and descriptions to score against specialized CV profiles
and selects the optimal resume and showcase projects.
"""
from pathlib import Path
import re

RESUMES_DIR = Path(__file__).parent / "resumes"

DOMAIN_PROFILES = {
    "AI_ML_VISION": {
        "cv_file": "Resume_AI_Vision.pdf",
        "domain_name": "Artificial Intelligence & Computer Vision",
        "keywords": [
            "python", "yolo", "opencv", "computer vision", "machine learning", "deep learning",
            "pytorch", "tensorflow", "cnn", "u-net", "onnx", "segmentation", "object detection",
            "ai engineer", "data science", "nlp", "llm", "image processing", "scikit-learn"
        ],
        "github_projects": [
            {"name": "Vision AI Edge Assistant", "url": "https://github.com/your-username/vision-ai-edge", "desc": "Wearable edge AI navigation using YOLO and ONNX runtime"},
            {"name": "Medical Image Segmentation", "url": "https://github.com/your-username/medical-segmentation", "desc": "PyTorch U-Net for MRI lesion detection with Dice & IoU metrics"},
            {"name": "Real-Time Object & Flow Counter", "url": "https://github.com/your-username/object-counter", "desc": "OpenCV centroid tracker with bidirectional virtual tripwires"}
        ]
    },
    "TELECOM_NETWORKS": {
        "cv_file": "Resume_Telecom_Networks.pdf",
        "domain_name": "Telecommunications & Network Engineering",
        "keywords": [
            "telecom", "network", "tcp/ip", "socket", "routing", "switching", "wireshark",
            "protocols", "uart", "packet", "osi model", "cisco", "telemetry", "wireless",
            "lan", "wan", "ethernet", "latency", "dns", "dhcp", "bandwidth"
        ],
        "github_projects": [
            {"name": "TCP/IP Client-Server Network System", "url": "https://github.com/your-username/tcp-ip-client-server", "desc": "Multithreaded socket server with custom framing and CRC32 verification"},
            {"name": "Real-Time Telemetry Dashboard", "url": "https://github.com/your-username/telemetry-dashboard", "desc": "Low-latency MJPEG streaming and WebSocket telemetry cockpit"},
            {"name": "Hardware Telemetry Unit", "url": "https://github.com/your-username/hardware-telemetry", "desc": "Microcontroller pulse acquisition and UART serial telemetry logger"}
        ]
    },
    "EMBEDDED_HARDWARE": {
        "cv_file": "Resume_Embedded_Hardware.pdf",
        "domain_name": "Embedded Systems & Hardware Engineering",
        "keywords": [
            "embedded", "embedded c", "microcontroller", "pic18", "firmware", "proteus",
            "mplab", "hardware", "iot", "raspberry pi", "sensors", "eeprom", "interrupt",
            "schematic", "pcb", "spi", "i2c", "adc", "actuator", "c/c++"
        ],
        "github_projects": [
            {"name": "Automated IR Optical Attendance Gate", "url": "https://github.com/your-username/ir-attendance-gate", "desc": "Bi-directional optical IR beam door gate with EEPROM headcount logging"},
            {"name": "Microcontroller Signal Processing Unit", "url": "https://github.com/your-username/signal-processor", "desc": "Interrupt-driven pulse acquisition and non-volatile memory telemetry"},
            {"name": "Sensor Control & Alert Circuits", "url": "https://github.com/your-username/sensor-circuits", "desc": "Hardware sensor control circuits with hysteresis and audio-visual alerts"}
        ]
    },
    "SOFTWARE_QA": {
        "cv_file": "Resume_Software_QA.pdf",
        "domain_name": "Software Engineering & Quality Assurance (QA)",
        "keywords": [
            "qa", "quality assurance", "testing", "pytest", "test automation", "rest api",
            "flask", "validation", "sql", "mysql", "data validation", "regression",
            "sdlc", "bug", "jira", "unit test", "integration test", "backend", "developer"
        ],
        "github_projects": [
            {"name": "REST API Quality Validation Suite", "url": "https://github.com/your-username/rest-api-testing", "desc": "25+ pytest test cases verifying HTTP contracts, schemas, and SLA latency"},
            {"name": "Automated Data Validation & QA Pipeline", "url": "https://github.com/your-username/data-qa-pipeline", "desc": "Pandas data quality auditor with IQR outlier detection and ML regression checks"}
        ]
    }
}


def classify_job(job_title: str, job_description: str) -> dict:
    """Scores job title and description text against all domain profiles and returns the top match."""
    combined_text = (job_title + " " + job_description).lower()

    scores = {}
    matched_kw_map = {}

    for domain_key, profile in DOMAIN_PROFILES.items():
        score = 0
        matched = []
        for kw in profile["keywords"]:
            pattern = r"\b" + re.escape(kw) + r"\b"
            matches = len(re.findall(pattern, combined_text))
            if matches > 0:
                # Title matches carry 3x weight
                title_matches = len(re.findall(pattern, job_title.lower()))
                score += (title_matches * 3) + matches
                matched.append(kw)
        scores[domain_key] = score
        matched_kw_map[domain_key] = matched

    best_domain = max(scores, key=scores.get)
    if scores[best_domain] == 0:
        best_domain = "SOFTWARE_QA"

    profile = DOMAIN_PROFILES[best_domain]
    cv_path = RESUMES_DIR / profile["cv_file"]

    return {
        "domain_key": best_domain,
        "domain_name": profile["domain_name"],
        "cv_file_name": profile["cv_file"],
        "cv_full_path": str(cv_path),
        "score": scores[best_domain],
        "matched_keywords": matched_kw_map[best_domain],
        "github_projects": profile["github_projects"]
    }
