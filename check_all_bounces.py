import imaplib
import email
import re

USERNAME = "abdullahmasaud10@gmail.com"
PASSWORD = "vzpvxrlhutflfyak"

mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(USERNAME, PASSWORD)

# Check All Mail
status, folders = mail.list()
all_mail_folder = '"[Gmail]/All Mail"'

mail.select(all_mail_folder)
status, messages = mail.search(None, '(SUBJECT "Delivery Status Notification")')
mail_ids = messages[0].split()

print(f"Total Delivery Status Notifications in All Mail: {len(mail_ids)}")

bounced = set()
for mid in mail_ids:
    status, data = mail.fetch(mid, '(RFC822)')
    msg = email.message_from_bytes(data[0][1])
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() in ["text/plain", "message/delivery-status"]:
                try:
                    body += part.get_payload(decode=True).decode(errors='ignore') + "\n"
                except Exception:
                    pass
    else:
        try:
            body = msg.get_payload(decode=True).decode(errors='ignore')
        except Exception:
            pass
    matches = re.findall(r'(?:to|for|Recipient: rfc822;)\s*([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)', body, re.IGNORECASE)
    for m in matches:
        if m.lower() != USERNAME.lower() and "google" not in m.lower():
            bounced.add(m.lower())

mail.close()
mail.logout()

print(f"Unique Bounced Addresses across entire account: {len(bounced)}")
for i, b in enumerate(sorted(bounced), 1):
    print(f"{i:02d}. {b}")
