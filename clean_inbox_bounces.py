import imaplib

mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login("abdullahmasaud10@gmail.com", "vzpvxrlhutflfyak")
mail.select("INBOX")

# Search all mailer-daemon emails
typ, data = mail.search(None, 'FROM', 'mailer-daemon@googlemail.com')
mids = data[0].split()
print(f"Found {len(mids)} Mailer-Daemon bounce messages in Inbox.")

for mid in mids:
    mail.store(mid, "+FLAGS", "\\Deleted")

mail.expunge()
mail.close()
mail.logout()
print("Inbox successfully cleaned. All bounce notifications moved to Trash.")
