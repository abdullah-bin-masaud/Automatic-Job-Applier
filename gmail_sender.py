"""
Secure SSL/TLS SMTP Email Dispatcher.
Supports sending emails with PDF attachments directly through authenticated SMTP servers.
"""
import smtplib
import ssl
import os
from email.message import EmailMessage
from pathlib import Path


def send_email_via_gmail(
    recipient_email: str,
    subject: str,
    body_text: str,
    attachment_pdf_path: str = None,
    sender_email: str = None,
    app_password: str = None
) -> dict:
    """
    Connects to Google SMTP servers (smtp.gmail.com:465) using SSL.
    Sends the email and places a copy in your Gmail Sent folder.
    """
    email_from = sender_email or os.environ.get("SENDER_EMAIL", "").strip()
    password = app_password or os.environ.get("GMAIL_APP_PASSWORD", "").strip()
    candidate_name = os.environ.get("SENDER_NAME", "Candidate").strip()

    if not email_from or not password:
        return {
            "success": False,
            "error": "CONFIG_REQUIRED",
            "message": "SENDER_EMAIL and GMAIL_APP_PASSWORD must be set in your .env file or environment."
        }

    msg = EmailMessage()
    msg["From"] = f"{candidate_name} <{email_from}>"
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.set_content(body_text)

    if attachment_pdf_path:
        pdf_file = Path(attachment_pdf_path)
        if pdf_file.exists():
            with open(pdf_file, "rb") as f:
                pdf_data = f.read()
            msg.add_attachment(
                pdf_data,
                maintype="application",
                subtype="pdf",
                filename=pdf_file.name
            )

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(email_from, password)
            server.send_message(msg)

        return {
            "success": True,
            "recipient": recipient_email,
            "subject": subject,
            "attached_file": str(attachment_pdf_path) if attachment_pdf_path else None,
            "message": "Email sent successfully via SMTP."
        }
    except smtplib.SMTPAuthenticationError as e:
        return {
            "success": False,
            "error": "AUTH_FAILED",
            "message": f"SMTP Authentication failed. Verify 2-Step Verification and App Password. Error: {e}"
        }
    except Exception as e:
        return {
            "success": False,
            "error": "SEND_FAILED",
            "message": str(e)
        }
