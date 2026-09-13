import smtplib, socket, subprocess

def get_mx_hosts(domain):
    out = subprocess.getoutput(f"nslookup -type=mx {domain}")
    hosts = []
    for line in out.splitlines():
        if "mail exchanger =" in line:
            parts = line.split("mail exchanger =")[1].strip().split()
            # usually format: [preference, hostname]
            host = parts[-1].rstrip(".")
            hosts.append(host)
    return hosts

def verify_recipient(email_address):
    domain = email_address.split("@")[1]
    hosts = get_mx_hosts(domain)
    if not hosts:
        return False, "No MX records found"
    
    for mx in hosts[:2]:  # try first 2 MX hosts
        try:
            s = smtplib.SMTP(mx, 25, timeout=5)
            s.helo("gmail.com")
            s.mail("abdullahmasaud10@gmail.com")
            code, resp = s.rcpt(email_address)
            s.quit()
            resp_str = resp.decode(errors="ignore") if isinstance(resp, bytes) else str(resp)
            if code == 250:
                return True, f"250 OK: {resp_str}"
            elif code in [550, 551, 552, 553, 554]:
                return False, f"{code} Rejected: {resp_str}"
            else:
                return None, f"{code} Indeterminate: {resp_str}"
        except Exception as e:
            pass
    return None, "Connection timeout or refused on MX"

test_emails = [
    "careers@sadapay.pk",       # Bounced previously
    "careers@devsinc.com",       # Bounced previously
    "careers@folio3.com",       # Delivered previously
    "hr@risetech.ai",           # Delivered previously
    "careers@confiz.com"        # Delivered previously
]

print("=== TESTING REAL-TIME SMTP RCPT VERIFICATION ===")
for em in test_emails:
    valid, reason = verify_recipient(em)
    status_tag = "VALID [250 OK]" if valid else ("REJECTED [BOUNCE PREVENTED]" if valid is False else "UNKNOWN")
    print(f"{em:<30} -> {status_tag} | {reason}")
