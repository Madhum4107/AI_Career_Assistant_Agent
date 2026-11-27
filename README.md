# Resume Skill Analyzer

A small command-line **keyword-matching** demo that extracts supported skill phrases from resume text and suggests a role based on overlap with a transparent skills list.

## What it does

- Counts whitespace-separated words
- Detects supported skill phrases using exact phrase boundaries (so `java` does not match `javascript`)
- Supports a few aliases (for example, `ML` → `machine learning`)
- Suggests a role using simple skill overlap

## What it does not do

This is not a trained AI/NLP model, ATS simulator, resume-quality scorer, job-market predictor, or hiring recommendation system. The skills list is finite and results depend on wording. The role suggestion is a toy heuristic and must not be used for career decisions.

## Run

Requires Python 3.9+; no third-party packages.

```bash
python main.py
```

Run tests:

```bash
python -m unittest discover -v
```

## Files

- `add.py` — word count and basic text cleaning helpers
- `analyzer.py` — supported skills, phrase matching, counting
- `predictor.py` — rule-based role suggestion
- `main.py` — demonstration entry point
- `test_analyzer.py` — regression tests

## Author

Madhumitha M · B.E. CSE (AI & ML), 2028

[GitHub](https://github.com/Madhum4107) · [LinkedIn](https://www.linkedin.com/in/madhumitha4107/)
