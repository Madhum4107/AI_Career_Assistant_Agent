import unittest

from analyzer import find_skills, load_skills, skill_score


class SkillDetectionTests(unittest.TestCase):
    def test_detects_multiword_and_aliases(self):
        skills = find_skills("Experienced in ML, data analysis, and ReactJS.", load_skills())
        self.assertEqual(skills, ["machine learning", "data analysis", "react"])

    def test_avoids_substring_false_positive(self):
        self.assertNotIn("java", find_skills("I use javascript daily.", load_skills()))

    def test_token_list_compatibility(self):
        self.assertEqual(find_skills(["python", "sql"], load_skills()), ["python", "sql"])

    def test_deduplicates_and_count(self):
        skills = find_skills("Python python and SQL sql", load_skills())
        self.assertEqual(skills, ["python", "sql"])
        self.assertEqual(skill_score(skills), 2)

    def test_empty_text(self):
        self.assertEqual(find_skills("", load_skills()), [])


if __name__ == "__main__":
    unittest.main()
