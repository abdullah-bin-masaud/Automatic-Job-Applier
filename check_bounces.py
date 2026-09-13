import imaplib
import email
from email.header import decode_header
import re

USERNAME = "abdullahmasaud10@gmail.com"
PASSWORD = "vzpvxrlhutflfyak"

try:
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(USERNAME, PASSWORD)
    mail.select("INBOX")

    # Search for bounce messages from mailer-daemon
    status, messages = mail.search(None, '(FROM "mailer-daemon@googlemail.com")')
    mail_ids = messages[0].split()

    print(f"Total bounce notifications found in Inbox: {len(mail_ids)}")

    bounced_emails = set()
    
    # Process each bounce email
    for mid in mail_ids[-100:]:  # check the last 100
        status, data = mail.fetch(mid, '(RFC822)')
        raw_email = data[0][1]
        msg = email.message_from_bytes(raw_email)
        
        # Look for the failed recipient in headers or body
        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                if content_type in ["text/plain", "message/delivery-status"]:
                    try:
                        body += part.get_payload(decode=True).decode(errors='ignore') + "\n"
                    except Exception:
                        pass
        else:
            try:
                body = msg.get_payload(decode=True).decode(errors='ignore')
            except Exception:
                pass
        
        # Regex search for the failed email address
        # Typically looks like: "Your message wasn't delivered to abc@xyz.com" or "Final-Recipient: rfc822; abc@xyz.com"
        matches = re.findall(r'(?:to|for|Recipient: rfc822;)\s*([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)', body, re.IGNORECASE)
        for m in matches:
            if m.lower() != USERNAME.lower() and "google" not in m.lower():
                bounced_emails.add(m.lower())

    mail.close()
    mail.logout()

    print(f"\nUnique bounced destination addresses identified ({len(bounced_emails)}):")
    for idx, em in enumerate(sorted(bounced_emails), 1):
        print(f"{idx:02d}. {em}")

except Exception as e:
    print(f"IMAP check error: {e}")
