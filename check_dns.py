import socket
import smtplib

emails_to_test = [
    "careers@carepvtltd.com",
    "info@taraztechnologies.com",
    "hr@genifem.com",
    "info@crossanalytics.com.pk",
    "hr@signatics.com",
    "hr@zatnav.com",
    "careers.pk@mrs-electronic.com",
    "careers@bentley.com",
    "jobs@gitlab.com",
    "jobs@automattic.com",
    "jobs@canonical.com",
    "apply@crossover.com",
    "jobs@bairesdev.com",
    "careers@ovextech.com",
    "info@lmkt.com",
    "careers@techlogix.com",
    "hr@shifa.com.pk",
    "careers@zones.com",
    "recruitment@ufone.com"
]

results = []
for email in emails_to_test:
    domain = email.split('@')[1]
    try:
        # test DNS resolution for domain
        ip = socket.gethostbyname(domain)
        results.append((email, "DNS_OK", ip))
    except Exception as e:
        results.append((email, "DNS_FAIL", str(e)))

for r in results:
    print(f"{r[0]:<35} | {r[1]:<10} | {r[2]}")
