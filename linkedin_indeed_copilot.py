"""
LinkedIn & Indeed Application Pitch Generator.
Produces ready-to-paste screening answers and short pitch notes tailored to the matched domain.
"""
import os

CANDIDATE_NAME = os.getenv("SENDER_NAME", "Candidate")
CANDIDATE_GITHUB = os.getenv("SENDER_GITHUB", "https://github.com")

def generate_pitch(company_name: str, job_title: str, match_result: dict) -> dict:
    """Generates concise pitches suitable for LinkedIn Easy Apply notes and Indeed cover messages."""
    projects = match_result.get("github_projects", [])
    p1 = projects[0] if len(projects) > 0 else {"name": "Portfolio Project", "url": CANDIDATE_GITHUB}
    p2 = projects[1] if len(projects) > 1 else {"name": "Featured Repository", "url": CANDIDATE_GITHUB}

    pitch_note = (
        f"Hi {company_name} Hiring Team,\n\n"
        f"I am writing to express my interest in the {job_title} role, specializing in {match_result['domain_name']}. "
        f"I have built production-grade open-source systems including {p1['name']} ({p1['url']}) "
        f"and {p2['name']} ({p2['url']}). "
        f"I would welcome the opportunity to connect and discuss how my skills align with your goals!"
    )

    screening_answers = {
        "Years of relevant experience?": "1+ years (hands-on project and technical experience)",
        "Are you authorized to work in this location?": "Yes",
        "Notice period / Availability?": "Immediate",
        "Comfortable with on-site/hybrid?": "Yes, fully comfortable",
        "Portfolio / GitHub Profile URL": CANDIDATE_GITHUB,
        "Target CV to Upload": match_result.get("cv_file_name", "Resume.pdf")
    }

    return {
        "pitch_note": pitch_note,
        "screening_answers": screening_answers,
        "recommended_cv": match_result.get("cv_file_name", "Resume.pdf")
    }
