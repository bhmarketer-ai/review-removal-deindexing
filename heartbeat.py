"""
BHMarketer.ai — Negative Review Removal & Deindexing
Heartbeat writer — GitHub Actions triggers this every 4 days
Appends a log entry to keep the repo active on all platforms
https://bhmarketer.ai/negative-review-removal/
"""

import json
import pathlib
from datetime import datetime, timezone

LOG = pathlib.Path("dataset/heartbeat_log.jsonl")

SERVICES = [
    {
        "name":  "Google Review Removal (under 3 weeks)",
        "price": "Contact",
        "url":   "https://bhmarketer.ai/products/text-reviews-lesser-than-3-weeks-negative-google-review-removal/",
    },
    {
        "name":  "Airbnb Review Removal",
        "price": "$1,000",
        "url":   "https://bhmarketer.ai/products/airbnb-review-removal/",
    },
    {
        "name":  "Glassdoor Review Removal",
        "price": "Contact",
        "url":   "https://bhmarketer.ai/products/glassdoor-review-removal/",
    },
    {
        "name":  "Yelp Page Deindexing",
        "price": "Contact",
        "url":   "https://bhmarketer.ai/products/yelp-page-deindexing/",
    },
    {
        "name":  "Glassdoor Page Deindexing",
        "price": "Contact",
        "url":   "https://bhmarketer.ai/products/glassdoor-page-deindexing/",
    },
]

LINKS = {
    "homepage":     "https://bhmarketer.ai/negative-review-removal/",
    "huggingface":  "https://huggingface.co/datasets/bhmarketer/review-removal-deindexing",
    "npm":          "https://www.npmjs.com/package/bhmarketer-review-removal",
    "kaggle":       "https://www.kaggle.com/datasets/bhmarketer/bhmarketer-review-removal-and-deindexing-benchmark",
    "zenodo":       "https://zenodo.org/records/20494908",
    "doi":          "https://doi.org/10.5281/zenodo.20494908",
}


def write_heartbeat():
    LOG.parent.mkdir(parents=True, exist_ok=True)
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "repo":      "bhmarketer-ai/review-removal-deindexing",
        "brand":     "BHMarketer.ai",
        "status":    "active",
        "services":  SERVICES,
        "links":     LINKS,
    }
    with LOG.open("a") as f:
        f.write(json.dumps(entry) + "\n")
    print(f"Heartbeat written: {entry['timestamp']}")
    for s in SERVICES:
        print(f"  {s['price']:>8}  {s['name']}")


if __name__ == "__main__":
    write_heartbeat()
