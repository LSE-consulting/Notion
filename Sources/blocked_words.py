# blocked_words.py
#
# Shared keyword blocklist used by every Notion scraper notebook in this repo
# to hard-exclude notices before upload (skipped entirely - never written to
# the unified Notion database).
#
# Same list, same matching logic, and same rationale as the sibling file of
# the same name in the OppsLink repo (scrapers/blocked_words.py) - kept
# identical across both repos on purpose, so a notice blocked from the job
# board is also blocked from the Notion database, and vice versa.
#
# Single source of truth: edit BLOCKED_KEYWORDS below and every notebook picks up
# the change on its next run. No per-notebook edits needed.
#
# Added 2026-08-09 per Javiera's feedback. Checked against BOTH title and
# description, case-insensitive, word-boundary aware (so "tour" won't match
# "tourism", but multi-word phrases like "waste disposal" still match with
# flexible whitespace).
#
# Per Javiera's call: "operational", "marketing", "tour", "logistics" and
# "construction" are matched as bare words to maximise coverage over precision.
# Expect some false positives on legitimate work that happens to use these
# words (e.g. "operational efficiency review", "marketing strategy",
# "tourism development", "logistics policy", "construction sector reform").
# Skipped notices are printed to console - spot-check those if false positives
# become a problem, and narrow the relevant term(s) to a phrase instead.

from __future__ import annotations

import html
import re
import unicodedata
from typing import List


def _norm_text(s) -> str:
    if s is None:
        return ""
    s = html.unescape(str(s))
    s = unicodedata.normalize("NFKC", s)
    s = s.lower().strip()
    s = re.sub(r"\s+", " ", s)
    if s in {"nan", "none", "null"}:
        return ""
    return s


BLOCKED_KEYWORDS: List[str] = [
    # --- Landscaping ---
    "landscaping",
    "landscape design",
    "landscape architecture",
    "grounds maintenance",
    "horticulture",
    "horticultural",
    "tree surgery",
    "arboriculture",
    "gardening",

    # --- Furniture / furnishing ---
    "furniture",
    "furnishing",
    "furnishings",
    "office fit-out",
    "upholstery",
    "upholstered",

    # --- Construction work (bare "construction" - max coverage, per Javiera) ---
    "construction",
    "construction work",
    "construction works",
    "construction services",
    "building works",
    "civil works",
    "groundworks",
    "refurbishment works",

    # --- Work suit ---
    "work suit",
    "work suits",
    "workwear",
    "overalls",
    "boilersuit",
    "boiler suit",
    "protective clothing",
    "coveralls",

    # --- Logistics (bare - max coverage, per Javiera) ---
    "logistics",

    # --- Operational (bare - max coverage, per Javiera) ---
    "operational",
    "operations",

    # --- Tour (bare - max coverage, per Javiera) ---
    "tour",
    "tours",
    "tour operator",
    "guided tour",
    "guided tours",
    "sightseeing",
    "excursion",

    # --- Marketing (bare - max coverage, per Javiera) ---
    "marketing",
    "advertising",
    "advertisement",
    "promotional campaign",

    # --- Sewage ---
    "sewage",
    "sewerage",
    "wastewater treatment",
    "effluent treatment",
    "sewer",
    "sewers",

    # --- Waste disposal ---
    "waste disposal",
    "waste collection",
    "refuse collection",
    "skip hire",
    "waste management",
]


def _keyword_hit(text: str, keyword: str) -> bool:
    # Multi-word phrases match with flexible whitespace; single words get
    # word-boundary matching so "tour" doesn't match inside "tourism".
    pattern = re.escape(keyword).replace(r"\ ", r"\s+")
    return re.search(rf"\b{pattern}\b", text) is not None


def is_blocked(title, description: str = "") -> bool:
    """
    True if the title or description matches any entry in BLOCKED_KEYWORDS.
    Pass the raw title/description - normalization happens inside.
    """
    text = f"{_norm_text(title)} {_norm_text(description)}"
    for kw in BLOCKED_KEYWORDS:
        if _keyword_hit(text, kw):
            return True
    return False


def blocked_keyword_hits(title, description: str = "") -> List[str]:
    """
    Same check as is_blocked(), but returns the list of matched keyword(s)
    instead of a bool - used for the console print so skipped notices can be
    spot-checked for false positives.
    """
    text = f"{_norm_text(title)} {_norm_text(description)}"
    return [kw for kw in BLOCKED_KEYWORDS if _keyword_hit(text, kw)]
