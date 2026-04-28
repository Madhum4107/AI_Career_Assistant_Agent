def load_skills():
    return [
        "python", "java", "c++", "machine learning",
        "data analysis", "deep learning", "sql",
        "html", "css", "javascript", "react",
        "ai", "nlp"
    ]


def find_skills(words, skills_db):
    found = set()

    for word in words:
        for skill in skills_db:
            if skill in word:
                found.add(skill)

    return list(found)


def skill_score(found_skills):
    n = len(found_skills)

    if n <= 2:
        return 3
    elif n <= 5:
        return 6
    else:
        return 9