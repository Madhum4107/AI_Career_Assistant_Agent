# Resume Skill Analyzer

A small Python prototype that detects skill keywords in resume text using transparent phrase matching.

> **Scope:** This is a keyword-matching exercise—not an AI agent, semantic resume evaluator, hiring predictor, or validated resume score.

## What it does
- Detects skill terms from a small vocabulary.
- Supports multi-word terms (for example, `machine learning` and `data analysis`).
- Avoids simple substring false positives (such as matching `java` inside `javascript`).
- Returns a reproducible skill list and count.

## Run
Requires Python 3.10+; no third-party dependencies.

```bash
python main.py
python -m unittest discover -v
```

## Use the function
```python
from analyzer import find_skills, load_skills

resume_text = "I use Python, SQL and machine learning."
print(find_skills(resume_text, load_skills()))
```

## Limitations
- No PDF/DOCX parsing or LLM.
- No semantic understanding, context validation, synonym inference beyond a few aliases, or career prediction.
- Keyword presence is not proof of proficiency.

## Project files
- `main.py`: sample command-line demo
- `analyzer.py`: matching and counting utilities
- `test_analyzer.py`: unit tests

**Madhumitha M** · [GitHub](https://github.com/Madhum4107) · [LinkedIn](https://www.linkedin.com/in/madhumitha4107/)
