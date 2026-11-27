"""Transparent keyword-based resume skill extraction (not an AI/NLP model)."""
import re
from collections.abc import Iterable

SKILLS = [
    "python", "java", "c++", "machine learning", "data analysis",
    "deep learning", "sql", "html", "css", "javascript", "react",
    "artificial intelligence", "nlp", "pandas", "numpy", "scikit-learn",
    "tensorflow", "pytorch", "excel", "power bi", "tableau", "fastapi",
    "streamlit", "git", "docker",
]

ALIASES = {
    "ml": "machine learning",
    "ai": "artificial intelligence",
    "js": "javascript",
    "sklearn": "scikit-learn",
    "powerbi": "power bi",
}


def load_skills() -> list[str]:
    """Return canonical supported skill phrases."""
    return list(SKILLS)


def normalize_text(text: str) -> str:
    """Normalize case and punctuation while preserving skill phrase boundaries."""
    text = text.lower().replace("c++", "c plus plus")
    return re.sub(r"[^a-z0-9]+", " ", text).strip()


def find_skills(text: str, skills_db: Iterable[str] | None = None) -> list[str]:
    """Find exact phrase matches; avoid false matches such as 'java' in 'javascript'."""
    if not isinstance(text, str) or not text.strip():
        return []
    candidates = skills_db if skills_db is not None else load_skills()
    normalized = normalize_text(text)
    found = []
    for raw_skill in candidates:
        canonical = ALIASES.get(raw_skill.lower().strip(), raw_skill.lower().strip())
        phrase = normalize_text(canonical)
        if phrase and re.search(rf"(?<!\w){re.escape(phrase)}(?!\w)", normalized):
            found.append(canonical)
    return sorted(set(found))


def skill_score(found_skills: Iterable[str], skills_db: Iterable[str] | None = None) -> int:
    """Return the number of supported skills found; not a resume quality score."""
    found = set(found_skills)
    universe = set(skills_db if skills_db is not None else load_skills())
    return len(found & universe)
