"""Command-line demo for the keyword-based resume skill analyzer."""
from add import process_resume
from analyzer import find_skills, load_skills, skill_score
from predictor import predict_job_role

SAMPLE_RESUME = """
Python, SQL, Pandas, NumPy, machine learning, data analysis,
scikit-learn, Streamlit, FastAPI, Git, and React.
"""


def analyze_resume(resume_text: str) -> dict:
    skills = find_skills(resume_text, load_skills())
    count = skill_score(skills)
    return {
        "word_count": process_resume(resume_text)["word_count"],
        "skills": skills,
        "skill_count": count,
        "suggested_role": predict_job_role(skills),
    }


def main() -> None:
    result = analyze_resume(SAMPLE_RESUME)
    print("RESUME SKILL ANALYZER (keyword-based demo)")
    print("-" * 44)
    print(f"Word count: {result['word_count']}")
    print(f"Supported skills detected: {result['skill_count']}")
    print("Skills:", ", ".join(result["skills"]) or "None")
    print("Suggested role based on detected keywords:", result["suggested_role"])
    print("Note: This is a keyword demo, not a resume quality or hiring prediction.")


if __name__ == "__main__":
    main()
