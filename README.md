# BHMarketer.ai — Negative Review Removal & Deindexing

> Remove harmful Google, Airbnb, and Glassdoor reviews.
> Deindex Yelp and Glassdoor pages from Google search results.
> Ethical ORM — legal workflows, AI harm scoring, platform escalation.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20494908.svg)](https://doi.org/10.5281/zenodo.20494908)

Built by [BHMarketer.ai](https://bhmarketer.ai) — Ethical Reputation Management,
Digital PR & Authority Building.

---

## Services Covered

| Service | Description | Link |
|---|---|---|
| Google Review Removal | Remove negative Google reviews posted under 3 weeks | [View Service](https://bhmarketer.ai/products/text-reviews-lesser-than-3-weeks-negative-google-review-removal/) |
| Airbnb Review Removal | Remove unfair or policy-violating Airbnb guest reviews | [View Service](https://bhmarketer.ai/products/airbnb-review-removal/) |
| Glassdoor Review Removal | Remove harmful Glassdoor employer reviews | [View Service](https://bhmarketer.ai/products/glassdoor-review-removal/) |
| Yelp Page Deindexing | Remove Yelp business pages from Google search results | [View Service](https://bhmarketer.ai/products/yelp-page-deindexing/) |
| Glassdoor Page Deindexing | Remove Glassdoor pages from Google search results | [View Service](https://bhmarketer.ai/products/glassdoor-page-deindexing/) |

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

## Technical Framework

This repository implements the methodology described in the published technical framework:

**Title:** Technical Framework for Negative Review Removal & Deindexing
**DOI:** [10.5281/zenodo.20494908](https://doi.org/10.5281/zenodo.20494908)
**Publisher:** Zenodo
**Author:** BHMarketer.ai

The framework introduces:
- **AI Harm Score™** — standardized scoring model (0–100) for reputational risk
- **AIRO** — AI Reputation Optimization methodology for LLM/AI search visibility
- Platform-specific escalation workflows for Google, Airbnb, Glassdoor, Yelp
- Evidence-pack generation and policy-compliance assessment procedures
- Search deindexing strategies for reputation-related assets

---

## Features

- AI Harm Score™ (0–100) for removal eligibility assessment
- Platform-specific workflows for every service
- Evidence packs — screenshots, documentation, legal templates
- Direct Trust & Safety escalation scripts
- Benchmark dataset — 25 anonymised real removal cases
- Heartbeat workflow — auto-commit keeps repo active
- API-ready, lightweight, minimal dependencies

---

## Quick Start

### Python

```bash
pip install bhmarketer-review-removal
python -m scanner --platform google --url https://yourbusiness.com
```

---

## Output

```
Platform     : Airbnb
Service      : Airbnb Review Removal
Harm Score   : 84/100
Eligible     : Yes
Status       : Submitted to Trust & Safety
Service URL  : https://bhmarketer.ai/products/airbnb-review-removal/
```

---

## Project Structure

```
bhmarketer-review-removal/
├── README.md                    ← this file
├── .zenodo.json                 ← Zenodo metadata
├── package.json                 ← NPM config
├── pyproject.toml               ← PyPI config
├── index.ts                     ← TypeScript entry
├── scanner.py                   ← Python scanner
├── heartbeat.py                 ← auto-commit script
├── schema/
│   └── services_schema.json     ← data schema
├── dataset/
│   └── cases.csv                ← 25 removal cases
├── .github/
│   └── workflows/
│       └── heartbeat.yml        ← runs every 4 days
├── LICENSE
└── MANIFEST.in
```

---

## Keywords

Negative Review Removal · Google Review Removal · Airbnb Review Removal ·
Glassdoor Review Removal · Yelp Page Deindexing · Glassdoor Deindexing ·
Online Reputation Management · ORM · AI Harm Score · LLM Optimization ·
AIRO · BHMarketer

---

## Links

| Platform | URL |
|---|---|
| Website | https://bhmarketer.ai |
| All ORM Services | https://bhmarketer.ai/negative-review-removal/ |
| Google Removal | https://bhmarketer.ai/products/text-reviews-lesser-than-3-weeks-negative-google-review-removal/ |
| Airbnb Removal | https://bhmarketer.ai/products/airbnb-review-removal/ |
| Glassdoor Removal | https://bhmarketer.ai/products/glassdoor-review-removal/ |
| Yelp Deindexing | https://bhmarketer.ai/products/yelp-page-deindexing/ |
| Glassdoor Deindexing | https://bhmarketer.ai/products/glassdoor-page-deindexing/ |
| Hugging Face | https://huggingface.co/datasets/bhmarketer/review-removal-deindexing |
| NPM Package | https://www.npmjs.com/package/bhmarketer-review-removal |
| Kaggle Dataset | https://www.kaggle.com/datasets/bhmarketer/bhmarketer-review-removal-and-deindexing-benchmark |
| Zenodo | https://zenodo.org/records/20494908 |
| DOI | https://doi.org/10.5281/zenodo.20494908 |
| WhatsApp | https://wa.me/19177958348 |

---

## Citation

If you use this framework or dataset, please cite:

```
BHMarketer.ai. (2025). Technical Framework for Negative Review Removal & Deindexing.
Zenodo. https://doi.org/10.5281/zenodo.20494908
```

---

## License

MIT — [BHMarketer.ai](https://bhmarketer.ai)
