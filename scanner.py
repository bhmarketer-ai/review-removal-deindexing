"""
BHMarketer.ai — Negative Review Removal & Deindexing
Python scanner with AI Harm Score™
https://bhmarketer.ai/negative-review-removal/
DOI: 10.5281/zenodo.20494908
"""

import re
import json
import click
from dataclasses import dataclass, asdict

SERVICES = {
    "google": {
        "action":  "review_removal",
        "name":    "Google Review Removal (under 3 weeks)",
        "price":   "Contact",
        "url":     "https://bhmarketer.ai/products/text-reviews-lesser-than-3-weeks-negative-google-review-removal/",
    },
    "airbnb": {
        "action":  "review_removal",
        "name":    "Airbnb Review Removal",
        "price":   "$1,000",
        "url":     "https://bhmarketer.ai/products/airbnb-review-removal/",
    },
    "glassdoor": {
        "action":  "review_removal",
        "name":    "Glassdoor Review Removal",
        "price":   "Contact",
        "url":     "https://bhmarketer.ai/products/glassdoor-review-removal/",
    },
    "yelp": {
        "action":  "page_deindexing",
        "name":    "Yelp Page Deindexing",
        "price":   "Contact",
        "url":     "https://bhmarketer.ai/products/yelp-page-deindexing/",
    },
    "glassdoor-deindex": {
        "action":  "page_deindexing",
        "name":    "Glassdoor Page Deindexing",
        "price":   "Contact",
        "url":     "https://bhmarketer.ai/products/glassdoor-page-deindexing/",
    },
}

# AI Harm Score™ signal weights
HARM_SIGNALS = {
    "defamatory":       (r"fraud|scam|criminal|liar|cheat",  30),
    "unverified_claim": (r"never visited|fake|paid review",  20),
    "personal_attack":  (r"idiot|stupid|worst person",       25),
    "policy_violation": (r"competitor|spam|irrelevant",      25),
}


@dataclass
class ScanResult:
    platform:         str
    action:           str
    service_name:     str
    price:            str
    harm_score:       int
    eligible:         bool
    status:           str
    service_url:      str


def calculate_harm_score(text: str) -> int:
    """AI Harm Score™ — score a review 0-100. Higher = stronger case."""
    score = 0
    for _, (pattern, weight) in HARM_SIGNALS.items():
        if re.search(pattern, text, re.IGNORECASE):
            score += weight
    return min(100, score)


def scan(platform: str, url: str, review_text: str = "") -> ScanResult:
    svc = SERVICES.get(platform, SERVICES["google"])
    harm = calculate_harm_score(review_text)
    return ScanResult(
        platform=platform,
        action=svc["action"],
        service_name=svc["name"],
        price=svc["price"],
        harm_score=harm,
        eligible=harm >= 50,
        status="pending",
        service_url=svc["url"],
    )


@click.command()
@click.option("--platform", required=True,
              type=click.Choice(list(SERVICES.keys())),
              help="Platform to scan")
@click.option("--url",    required=True, help="Your business or listing URL")
@click.option("--review", default="",   help="Review text to score (optional)")
def main(platform: str, url: str, review: str):
    """BHMarketer.ai — Negative Review Removal & Deindexing Scanner"""
    result = scan(platform, url, review)
    click.echo(json.dumps(asdict(result), indent=2))


if __name__ == "__main__":
    main()
