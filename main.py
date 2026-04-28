from add import process_resume, clean_text, extract_words
from analyzer import load_skills, find_skills, skill_score
from predictor import predict_job_role

resume = """
I know Python, JavaScript, Machine Learning and SQL.
I have worked on AI and Data Analysis projects.
"""

def main():

    # Step 1
    result = process_resume(resume)

    # Step 2
    clean = clean_text(resume)
    words = extract_words(clean)

    # Step 3
    skills_db = load_skills()
    found_skills = find_skills(words, skills_db)

    # Step 4
    score = skill_score(found_skills)

    # Step 5
    role = predict_job_role(score)

    # OUTPUT
    print("\n==============================")
    print("   AI CAREER ASSISTANT")
    print("==============================")

    print("\nResume Words:", result["word_count"])
    print("Basic Score:", result["score"])

    print("\nSkills Found:", found_skills)
    print("Skill Score:", score)

    print("\nPredicted Job Role:", role)

    print("==============================\n")


if __name__ == "__main__":
    main()