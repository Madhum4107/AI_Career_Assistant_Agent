"""Simple rule-based role suggestion from detected resume skill keywords."""
from collections.abc import Iterable

ROLE_SKILLS = {
    "Data Analyst": {"sql", "excel", "power bi", "tableau", "data analysis"},
    "Data Scientist": {"python", "machine learning", "pandas", "numpy", "scikit-learn", "statistics"},
    "ML Engineer": {"python", "machine learning", "tensorflow", "pytorch", "docker", "fastapi"},
    "Frontend Developer": {"html", "css", "javascript", "react"},
    "Backend Developer": {"python", "java", "fastapi", "sql", "docker"},
}


def predict_job_role(found_skills: Iterable[str]) -> str:
    """Suggest the role with the most overlapping skills; deterministic tie break."""
    skills = {str(skill).lower().strip() for skill in found_skills}
    if not skills:
        return "Explore beginner roles"
    scores = [(role, len(skills & required)) for role, required in ROLE_SKILLS.items()]
    scores.sort(key=lambda item: (-item[1], item[0]))
    if scores[0][1] == 0:
        return "Explore beginner roles"
    return scores[0][0]
