"""Run a small example of keyword-based resume skill analysis."""
from analyzer import load_skills, find_skills, skill_score

SAMPLE_RESUME = """
I know Python, JavaScript, Machine Learning and SQL.
I have worked on AI and Data Analysis projects.
"""


def analyze_resume(text: str) -> dict:
    skills = find_skills(text, load_skills())
    return {"word_count": len(text.split()), "skills": skills, "skill_count": skill_score(skills)}


def main() -> None:
    result = analyze_resume(SAMPLE_RESUME)
    print("\\n=== Resume Skill Analyzer (keyword demo) ===")
    print(f"Words: {result['word_count']}")
    print(f"Skills detected ({result['skill_count']}): {', '.join(result['skills']) or 'None'}")
    print("\\nThis prototype only detects keywords. It does not score resume quality or predict a job role.")
    print("Replace SAMPLE_RESUME with your own text in analyze_resume(text) to test another sample.")


if __name__ == "__main__":
    main()
