import csv, imaplib, email, re

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('abdullahmasaud10@gmail.com', 'vzpvxrlhutflfyak')

all_bounced = set()

for folder in ['INBOX', '[Gmail]/Trash', '[Gmail]/Spam']:
    try:
        mail.select(f'"{folder}"')
        status, messages = mail.search(None, 'ALL')
        mids = messages[0].split()
        for mid in mids:
            status, data = mail.fetch(mid, '(RFC822)')
            if not data or not data[0]:
                continue
            msg = email.message_from_bytes(data[0][1])
            sender = msg.get('From', '')
            subject = msg.get('Subject', '')
            if 'mailer-daemon' in sender.lower() or 'delivery status' in subject.lower() or 'undelivered' in subject.lower() or 'failure' in subject.lower():
                body = ''
                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_type() in ['text/plain', 'message/delivery-status']:
                            payload = part.get_payload(decode=True)
                            if payload:
                                body += payload.decode(errors='ignore') + '\n'
                else:
                    payload = msg.get_payload(decode=True)
                    if payload:
                        body = payload.decode(errors='ignore')
                for m in re.findall(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)', body):
                    low = m.lower().rstrip('.')
                    if 'google' not in low and 'abdullahmasaud' not in low and not low.endswith('.png') and not low.endswith('.jpg'):
                        all_bounced.add(low)
    except Exception as e:
        print('Folder err:', folder, e)

mail.close()
mail.logout()

print(f"Total distinct bounced addresses identified: {len(all_bounced)}")

# Read tracker
tracker_entries = []
tracker_emails = set()
with open(r'C:\Users\Lenovo\Desktop\Projects\Automated-Job-Applier\applied_tracker.csv', 'r', encoding='utf-8') as f:
    for row in csv.reader(f):
        if len(row) > 2:
            em = row[2].strip().lower()
            comp = row[1].strip()
            role = row[4].strip() if len(row) > 4 else ''
            tracker_entries.append((comp, em, role))
            tracker_emails.add(em)

unique_delivered = {}
unique_bounced = {}

for comp, em, role in tracker_entries:
    # Check if exact email or base email bounced
    is_bounced = em in all_bounced or any(em in b for b in all_bounced)
    if is_bounced:
        if em not in unique_bounced:
            unique_bounced[em] = (comp, role)
    else:
        if em not in unique_delivered:
            unique_delivered[em] = (comp, role)

print("\n" + "=" * 75)
print("             ACCURATE COLD APPLICATION AUDIT")
print("=" * 75)
print(f"Total tracked email applications logged : {len(tracker_entries)}")
print(f"Total unique email addresses targeted   : {len(tracker_emails)}")
print(f"CONFIRMED BOUNCED (Address Not Found)   : {len(unique_bounced)} ({len(unique_bounced)/len(tracker_emails)*100:.1f}%)")
print(f"CONFIRMED DELIVERED (Alive Inboxes)     : {len(unique_delivered)} ({len(unique_delivered)/len(tracker_emails)*100:.1f}%)")
print("=" * 75)

print(f"\nSample of Confirmed BOUNCED Addresses ({len(unique_bounced)} total):")
for i, (em, (comp, role)) in enumerate(list(unique_bounced.items())[:20], 1):
    print(f"  [X] {i:02d}. {em:<35} | {comp}")

print(f"\nSample of Confirmed DELIVERED Inboxes ({len(unique_delivered)} total):")
for i, (em, (comp, role)) in enumerate(list(unique_delivered.items())[:25], 1):
    print(f"  [OK] {i:02d}. {em:<35} | {comp}")
