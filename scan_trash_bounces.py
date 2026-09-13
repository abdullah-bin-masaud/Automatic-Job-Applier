import imaplib, email, re

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('abdullahmasaud10@gmail.com', 'vzpvxrlhutflfyak')

status, folders = mail.list()
trash_folder = None
for f in folders:
    f_str = f.decode('utf-8', errors='ignore')
    if '[Gmail]/Trash' in f_str or '[Gmail]/Bin' in f_str:
        # Extract folder name
        parts = f_str.split(' "/" ')
        if len(parts) > 1:
            trash_folder = parts[1].strip('"')
        break

print('Trash folder name:', trash_folder)
if not trash_folder:
    trash_folder = '[Gmail]/Trash'

try:
    mail.select(f'"{trash_folder}"')
except Exception:
    mail.select(trash_folder)

status, messages = mail.search(None, 'ALL')
mids = messages[0].split()
print(f'Total messages in Trash: {len(mids)}')

bounces = set()
for mid in mids:
    status, data = mail.fetch(mid, '(RFC822)')
    if not data or not data[0]:
        continue
    raw = data[0][1]
    msg = email.message_from_bytes(raw)
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
        
        matches = re.findall(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)', body)
        for m in matches:
            m_low = m.lower().rstrip('.')
            if 'google' not in m_low and 'abdullahmasaud' not in m_low and not m_low.endswith('.png') and not m_low.endswith('.jpg'):
                bounces.add(m_low)

print(f'\nIdentified {len(bounces)} distinct addresses from bounce reports:')
for b in sorted(bounces):
    print('  *', b)
