import smtplib
import ssl
from pathlib import Path

# Test target emails to verify which ones exist and accept mail
test_list = [
    ("SkytechINN (NSTP Islamabad)", "info@skytechinn.com"),
    ("Intelsense.ai (Islamabad)", "hr@intelsense.ai"),
    ("O'Cyber (Islamabad)", "career@ocyber.work"),
    ("Velosi Integrity (Islamabad)", "careers@velosiaims.com"),
    ("United Sol (Islamabad)", "career@unitedsol.net"),
    ("Kulsum Hospital IT (Islamabad)", "hr@kih.com.pk"),
    ("PSTD Accelerate (Pakistan)", "hr@pstd.com.pk"),
    ("Devomech Solutions (Rawalpindi)", "info@devomech.com"),
    ("CARE Pvt Ltd (Islamabad)", "careers@carepvtltd.com"),
    ("Taraz Technologies (Islamabad)", "info@taraztechnologies.com"),
    ("MRS Electronic (Rawalpindi)", "careers.pk@mrs-electronic.com"),
    ("ZALYXIS AI (Remote)", "contact@zalyxis.com"),
    ("Remotebase (Remote)", "careers@remotebase.com"),
    ("Turing.com (Remote)", "jobs@turing.com"),
    ("NASTP Info (Rawalpindi)", "info@nastp.gov.pk"),
]

print(f"Total candidate destinations: {len(test_list)}")
for name, email in test_list:
    domain = email.split('@')[1]
    print(f"Candidate: {name:<35} | Email: {email}")
