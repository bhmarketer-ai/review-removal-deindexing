# BHMarketer.ai — Negative Review Removal & Deindexing

**BHMarketer.ai** is a leading provider of ethical online reputation management solutions.
This documentation covers the technical framework, scanner utilities, and workflows
for negative review removal and page deindexing.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20494908.svg)](https://doi.org/10.5281/zenodo.20494908)

---

## Project Overview

The **BHMarketer Review Removal & Deindexing** framework provides structured,
policy-compliant workflows for removing harmful reviews and deindexing pages
across Google, Airbnb, Glassdoor, and Yelp.

At its core, the framework introduces the **AI Harm Score™** — a standardized
scoring model (0–100) that quantifies reputational risk based on:

- Content visibility and platform authority
- Sentiment impact and search prominence
- Brand sensitivity and defamation risk
- Policy violation signals

---

## Services Covered

| Service | Description | Price | Link |
|---|---|---|---|
| Google Review Removal | Remove negative reviews posted under 3 weeks | Contact | [View](https://bhmarketer.ai/products/text-reviews-lesser-than-3-weeks-negative-google-review-removal/) |
| Airbnb Review Removal | Remove unfair or policy-violating guest reviews | $1,000 | [View](https://bhmarketer.ai/products/airbnb-review-removal/) |
| Glassdoor Review Removal | Remove harmful employer reviews | Contact | [View](https://bhmarketer.ai/products/glassdoor-review-removal/) |
| Yelp Page Deindexing | Remove Yelp pages from Google search | Contact | [View](https://bhmarketer.ai/products/yelp-page-deindexing/) |
| Glassdoor Page Deindexing | Remove Glassdoor pages from Google search | Contact | [View](https://bhmarketer.ai/products/glassdoor-page-deindexing/) |

---

## What's Included in Each Service

### Airbnb Review Removal — $1,000
- In-depth Airbnb policy violation audit
- Evidence pack with screenshots and documentation
- Direct escalation to Airbnb Trust & Safety
- Structured legal-style argument drafting
- Multiple follow-up appeals if needed
- Case tracking and status updates
- 1:1 consultation for complex review disputes

### Google Review Removal (under 3 weeks)
- Review eligibility check
- Policy violation identification
- Flag submission with documented evidence
- Follow-up escalation if not actioned
- Status tracking until resolved

### Glassdoor Review Removal
- Employer response strategy
- Policy violation documentation
- Direct platform escalation
- Legal defamation assessment where applicable

### Yelp & Glassdoor Page Deindexing
- Structured noindex / removal request
- Legal suppression documentation
- Google Search Console deindex filing
- Follow-up until confirmed removed from search

---

## Installation

### PyPI (Python)

```bash
pip install bhmarketer-review-removal
```

### NPM (Node.js)

```bash
npm install bhmarketer-review-removal
```

---

## Usage

### Python CLI

```bash
python -m scanner --platform google --url https://yourbusiness.com
python -m scanner --platform airbnb --url https://yourlisting.com
python -m scanner --platform glassdoor --url https://yourbusiness.com
python -m scanner --platform yelp --url https://yourbusiness.com
```

### Python — programmatic

```python
from scanner import scan, calculate_harm_score

# Score a review text
score = calculate_harm_score("This company is a complete fraud and scam")
print(f"Harm Score: {score}/100")

# Full scan
result = scan("airbnb", "https://yourlisting.com", "Unfair review text here")
print(result)
```

### Node.js / TypeScript

```typescript
import { scan, calculateHarmScore, SERVICES } from "bhmarketer-review-removal";

const score = calculateHarmScore("This company is a scam");
console.log(`Harm Score: ${score}/100`);

const result = scan("google", "Fake review claiming fraud");
console.log(result);
```

---

## Output

```
{
  "platform": "airbnb",
  "action": "review_removal",
  "service_name": "Airbnb Review Removal",
  "price": "$1,000",
  "harm_score": 84,
  "eligible": true,
  "status": "pending",
  "service_url": "https://bhmarketer.ai/products/airbnb-review-removal/"
}
```

---

## AI Harm Score™ Explained

The AI Harm Score™ rates a review from **0 to 100** based on four signal categories:

| Signal | Weight | Triggers |
|---|---|---|
| Defamatory content | 30 | fraud, scam, criminal, liar, cheat |
| Unverified claim | 20 | never visited, fake, paid review |
| Personal attack | 25 | direct insults targeting individuals |
| Policy violation | 25 | competitor mentions, spam, irrelevant |

**Scores 50+ = eligible for removal submission.**

---

## Technical Framework

This project implements the published framework:

> **Title:** Technical Framework for Negative Review Removal & Deindexing
> **DOI:** [10.5281/zenodo.20494908](https://doi.org/10.5281/zenodo.20494908)
> **Author:** BHMarketer.ai · **Publisher:** Zenodo

---

## Links

| Platform | URL |
|---|---|
| Website | https://bhmarketer.ai |
| All ORM Services | https://bhmarketer.ai/negative-review-removal/ |
| GitHub | https://github.com/bhmarketer-ai/review-removal-deindexing |
| Hugging Face | https://huggingface.co/datasets/bhmarketer/review-removal-deindexing |
| NPM | https://www.npmjs.com/package/bhmarketer-review-removal |
| Kaggle | https://www.kaggle.com/datasets/bhmarketer/bhmarketer-review-removal-and-deindexing-benchmark |
| Zenodo | https://zenodo.org/records/20494908 |
| WhatsApp | https://wa.me/19177958348 |

---

## License

MIT — [BHMarketer.ai](https://bhmarketer.ai)
