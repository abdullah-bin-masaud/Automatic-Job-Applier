import smtplib
import ssl
import os
import mimetypes
from email.message import EmailMessage
from pathlib import Path

SENDER_EMAIL = "abdullahmasaud10@gmail.com"


def send_email_via_gmail(
    recipient_email: str,
    subject: str,
    body_text: str,
    attachment_pdf_path: str = None,
    app_password: str = None
) -> dict:
    """
    Connects to Google SMTP servers (smtp.gmail.com:465) using SSL.
    Sends the email and automatically places a copy in your Gmail 'Sent' folder.
    """
    password = app_password or os.environ.get("GMAIL_APP_PASSWORD", "").strip()
    if not password:
        return {
            "success": False,
            "error": "GMAIL_APP_PASSWORD_REQUIRED",
            "message": "A 16-character Gmail App Password is required to send emails directly through Google's servers."
        }

    msg = EmailMessage()
    msg["From"] = f"Abdullah Bin Masaud <{SENDER_EMAIL}>"
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.set_content(body_text)

    # Attach PDF if provided
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

    # Send through Google's official secure SMTP server
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(SENDER_EMAIL, password)
            server.send_message(msg)

        return {
            "success": True,
            "recipient": recipient_email,
            "subject": subject,
            "attached_file": str(attachment_pdf_path) if attachment_pdf_path else None,
            "message": "Email sent successfully! It is now visible in your Gmail 'Sent' folder."
        }
    except smtplib.SMTPAuthenticationError as e:
        return {
            "success": False,
            "error": "AUTH_FAILED",
            "message": f"Gmail Authentication failed. Ensure 2-Step Verification is ON and you are using a 16-character App Password. Error: {e}"
        }
    except Exception as e:
        return {
            "success": False,
            "error": "SEND_FAILED",
            "message": str(e)
        }


if __name__ == "__main__":
    import sys
    print("=" * 60)
    print("  GMAIL SMTP DIRECT SENDER TEST")
    print("=" * 60)

    # Allow testing from command line
    pwd = input("Enter your 16-character Gmail App Password: ").strip().replace(" ", "")
    if pwd:
        test_subject = "Test: Automated Job Application Engine Proof"
        test_body = (
            "Hi Abdullah,\n\n"
            "This is a verified automated test from your Python Job Application Engine.\n"
            "Because this email was sent through Google's official SMTP server (smtp.gmail.com),\n"
            "it is automatically saved in your 'Sent' folder as proof of automated delivery!\n\n"
            "Candidate: Abdullah Bin Masaud\n"
            "University: COMSATS University Islamabad\n"
            "GitHub Portfolio: https://github.com/abdullah-bin-masaud\n"
        )
        test_cv = r"C:\Users\Lenovo\Desktop\CVV'S\CV__A.pdf"
        print(f"[*] Sending test email to {SENDER_EMAIL} with {test_cv} attached...")
        result = send_email_via_gmail(SENDER_EMAIL, test_subject, test_body, test_cv, pwd)
        print("\nResult:", result)
    else:
        print("[!] No password provided.")
