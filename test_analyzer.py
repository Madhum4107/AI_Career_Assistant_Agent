import unittest
from analyzer import find_skills, skill_score, normalize_text
from main import analyze_resume
from predictor import predict_job_role


class ResumeAnalyzerTests(unittest.TestCase):
    def test_exact_match_prevents_substring_false_positive(self):
        self.assertEqual(find_skills("JavaScript developer"), ["javascript"])
        self.assertNotIn("java", find_skills("JavaScript developer"))

    def test_phrase_matching_and_alias(self):
        found = find_skills("Experienced in ML, Power BI and C++.")
        self.assertIn("machine learning", found)
        self.assertIn("power bi", found)
        self.assertIn("c++", found)

    def test_empty_input(self):
        self.assertEqual(find_skills(""), [])
        self.assertEqual(predict_job_role([]), "Explore beginner roles")

    def test_role_suggestion_uses_skills(self):
        self.assertEqual(predict_job_role(["sql", "excel", "power bi"]), "Data Analyst")

    def test_score_is_supported_skill_count(self):
        self.assertEqual(skill_score(["python", "unsupported"]), 1)

    def test_sample_analysis_shape(self):
        result = analyze_resume("Python and SQL")
        self.assertEqual(result["word_count"], 3)
        self.assertIn("python", result["skills"])
        self.assertGreaterEqual(result["skill_count"], 1)


if __name__ == "__main__":
    unittest.main()
