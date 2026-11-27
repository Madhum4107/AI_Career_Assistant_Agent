"""Simple, transparent keyword-based resume skill detection.

This module intentionally does not claim semantic understanding or AI inference.
"""
from __future__ import annotations

import re
from collections.abc import Iterable

SKILLS = [
    "python", "java", "c++", "machine learning", "data analysis",
    "deep learning", "sql", "html", "css", "javascript", "react",
    "artificial intelligence", "natural language processing", "nlp",
]

ALIASES = {
    "ml": "machine learning",
    "ai": "artificial intelligence",
    "js": "javascript",
    "reactjs": "react",
    "sklearn": "scikit-learn",
}


def load_skills() -> list[str]:
    """Return the default skill vocabulary."""
    return list(SKILLS)


def _normalize(text: str) -> str:
    text = text.lower().replace("&", " and ")
    return re.sub(r"[^a-z0-9+#.]+", " ", text).strip()


def find_skills(text: str | Iterable[str], skills_db: Iterable[str]) -> list[str]:
    """Detect complete skill phrases; avoids substring false positives.

    Iterable inputs (such as the old token-list interface) are joined for
    backwards compatibility. Skills are returned in vocabulary order.
    """
    if not isinstance(text, str):
        text = " ".join(str(token) for token in text)
    normalized_text = f" {_normalize(text)} "
    found = []
    for skill in skills_db:
        canonical = ALIASES.get(skill.lower(), skill.lower())
        phrase = f" {_normalize(canonical)} "
        if phrase.strip() and phrase in normalized_text:
            found.append(canonical)
    # Deduplicate aliases without changing order.
    return list(dict.fromkeys(found))


def skill_score(found_skills: Iterable[str]) -> int:
    """Return detected skill count; this is not a resume quality score."""
    return len(set(found_skills))
