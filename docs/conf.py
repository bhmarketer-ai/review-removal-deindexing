# docs/conf.py
# BHMarketer.ai — Review Removal & Deindexing — ReadTheDocs config

project   = "BHMarketer Review Removal & Deindexing"
author    = "BHMarketer.ai"
copyright = "2025, BHMarketer.ai"
release   = "1.0.0"

extensions = [
    "myst_parser",
]

source_suffix = {
    ".md": "markdown",
}

html_theme   = "sphinx_rtd_theme"
html_title   = "BHMarketer Review Removal & Deindexing"

html_theme_options = {
    "display_version":      True,
    "prev_next_buttons_location": "bottom",
    "style_external_links": True,
}

html_context = {
    "display_github":      True,
    "github_user":         "bhmarketer-ai",
    "github_repo":         "review-removal-deindexing",
    "github_version":      "main",
    "conf_py_path":        "/docs/",
}

master_doc = "index"
