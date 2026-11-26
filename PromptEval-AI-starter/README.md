# PromptEval AI

A small evaluation dashboard for comparing current and new LLM support-assistant responses across a fixed CSV test set.

## Run locally (Windows)

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Place `questions.csv` in `data/`, or upload it in the sidebar. Required columns: `question`, `answer_current`, `answer_new`. Optional: `id`, `topic`.

## What it evaluates

The application calculates transparent, rule-based **proxies** for:
- Relevance: meaningful term overlap between question and answer.
- Completeness: answer detail and presence of action-oriented words.
- Clarity: approximate sentence-length signal.
- Professional tone: polite/supportive language signal.

The proxy score is normalized to 0–100 across those four dimensions. It is **not a factual accuracy score**. The supplied dataset has no verified reference answers or policy documents, so factual accuracy must be checked by a human or against an approved knowledge base. Do not present these heuristics as a true semantic or factual judge.

## Recommendation logic

- Ship: new proxy score improves by at least 2 points and no per-question proxy regressions are detected.
- Do not ship: new proxy score falls by more than 2 points, or more than 25% of questions regress.
- Ship with conditions: mixed / inconclusive evidence; review flagged cases and verify factual accuracy.

These are example decision thresholds and should be calibrated with the product team.

## Design note: making this an automated check

1. Maintain a versioned golden dataset of real customer questions and approved expected policies / reference answers.
2. Version every prompt and record the prompt hash, model name, model version, parameters, and evaluation date.
3. Run the same fixed dataset against old and new prompt versions using a consistent rubric.
4. Combine automated checks and a blinded LLM-as-a-judge; validate judge scores against human reviewers.
5. Detect regressions by topic and by individual question, with special handling for safety- and policy-critical cases.
6. Integrate evaluation into CI/CD; block deployment when quality, regression, or critical-policy thresholds fail, and retain historical reports.

## Limitations / next steps

- Text heuristics are explainable but can be gamed and do not establish factual correctness.
- Add approved policy retrieval and factuality checks.
- Add human review for low-confidence and critical cases.
- Run repeated / blinded judge evaluations and monitor evaluator consistency.
