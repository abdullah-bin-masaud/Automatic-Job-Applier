"""
Tailored Email Application Generator.
Generates personalized outreach emails and creates ready-to-send .eml draft files
complete with attached matching CV and clickable GitHub project showcases.
"""
import os
from pathlib import Path
from email.message import EmailMessage

CANDIDATE_NAME = os.getenv("SENDER_NAME", "Candidate")
CANDIDATE_PHONE = os.getenv("SENDER_PHONE", "")
CANDIDATE_EMAIL = os.getenv("SENDER_EMAIL", "candidate@example.com")
CANDIDATE_LINKEDIN = os.getenv("SENDER_LINKEDIN", "https://linkedin.com")
CANDIDATE_GITHUB = os.getenv("SENDER_GITHUB", "https://github.com")


def generate_email_draft(company_name: str, job_title: str, recipient_email: str, match_result: dict, output_dir: Path) -> Path:
    """Generates an RFC-822 .eml draft file with tailored body and attached CV."""
    msg = EmailMessage()
    msg["From"] = f"{CANDIDATE_NAME} <{CANDIDATE_EMAIL}>"
    msg["To"] = recipient_email
    msg["Subject"] = f"Application: {job_title} - {CANDIDATE_NAME}"

    domain_name = match_result["domain_name"]
    projects = match_result.get("github_projects", [])

    projects_bullet_text = ""
    for p in projects:
        projects_bullet_text += f"  * {p['name']}: {p['desc']}\n    Live Repository: {p['url']}\n\n"

    body = f"""Dear {company_name} Hiring Team,

I am writing to express my strong interest in the {job_title} role at {company_name}, specializing in {domain_name}.

To demonstrate my hands-on technical capabilities, I have built and open-sourced production-ready projects directly relevant to this position:

{projects_bullet_text}I have attached my tailored resume ({match_result['cv_file_name']}) for your consideration. You can also review my open-source code and engineering repositories on GitHub: {CANDIDATE_GITHUB}.

I would welcome the opportunity for a brief conversation to discuss how my technical background can contribute to your team at {company_name}.

Thank you for your time and consideration.

Best regards,

{CANDIDATE_NAME}
{CANDIDATE_PHONE} | {CANDIDATE_EMAIL}
LinkedIn: {CANDIDATE_LINKEDIN}
GitHub: {CANDIDATE_GITHUB}
"""
    msg.set_content(body)

    # Attach the winning CV PDF if it exists
    cv_path = Path(match_result.get("cv_full_path", ""))
    if cv_path.exists():
        with open(cv_path, "rb") as f:
            pdf_data = f.read()
        msg.add_attachment(pdf_data, maintype="application", subtype="pdf", filename=match_result["cv_file_name"])

    output_dir.mkdir(parents=True, exist_ok=True)
    safe_company = "".join(c for c in company_name if c.isalnum() or c in " _-").strip()
    eml_path = output_dir / f"Application_{safe_company}_{match_result['cv_file_name'].replace('.pdf', '')}.eml"
    with open(eml_path, "wb") as f:
        f.write(msg.as_bytes())

    return eml_path
