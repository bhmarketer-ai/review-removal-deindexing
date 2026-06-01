# Configuration file for the Sphinx documentation builder.
# BHMarketer.ai — Negative Review Removal & Deindexing

project   = "BHMarketer Review Removal"
author    = "BHMarketer.ai"
copyright = "2025, BHMarketer.ai"
release   = "1.0.0"

# Extensions
extensions = [
    "myst_parser",
]

# File types
source_suffix = [".md"]

# Theme
html_theme = "sphinx_rtd_theme"

html_theme_options = {
    "display_version": True,
}

# GitHub edit link
html_context = {
    "display_github":  True,
    "github_user":     "bhmarketer-ai",
    "github_repo":     "review-removal-deindexing",
    "github_version":  "main",
    "conf_py_path":    "/docs/",
}

# Entry point
master_doc = "index"
