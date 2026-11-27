# Resume Skill Analyzer

A beginner-friendly Python prototype that scans text for skills from a small reference list, calculates a simple score, and maps the score to a broad career-level label.

> **Current scope:** keyword-based analysis with fixed rules. It does not use an LLM, understand resume context, or make validated career predictions.

## Features

- Maintains a small reference skill list
- Detects skill keywords in supplied text
- Counts detected skills
- Produces a simple rule-based score
- Maps the score to a coarse role-level suggestion

## Workflow

```text
Resume text → Keyword matching → Skill count → Rule score → Label
```

## Tech stack

Python

## Run locally

```bash
git clone https://github.com/Madhum4107/AI_Career_Assistant_Agent.git
cd AI_Career_Assistant_Agent
python main.py
```

No external package installation is required for the current core prototype (Python standard library only).

## Project files

- `main.py` — entry point and input/output flow
- `analyzer.py` — keyword detection and scoring logic
- `predictor.py` — score-to-label mapping
- `add.py` — small practice/helper script

## Limitations

- Keyword matching may miss synonyms and can match terms without understanding context.
- The score is an arbitrary rule, not a validated assessment.
- Suggested labels are illustrative only and should not be treated as career or hiring advice.
- The repository name includes “Agent,” but the current implementation is not an autonomous AI agent.

## Roadmap

- Resume file parsing (PDF/DOCX) with clear privacy controls
- Job-description matching and explainable gap analysis
- Skill evidence and project links
- Tests, structured output, and a usable interface
- Optional LLM features only with explicit user configuration

## Author

**Madhumitha M**

[GitHub](https://github.com/Madhum4107) · [LinkedIn](https://www.linkedin.com/in/madhumitha4107/)
