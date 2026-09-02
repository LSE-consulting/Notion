# UNGM (UN Global Marketplace)

Procurement notices published by UN agencies.

**Website:** https://www.ungm.org/Public/Notice

## How it works

`ungm_notion_upload.ipynb` searches UNGM for recent active notices in the target service categories, opens each notice page to read its description, and uploads anything new to Notion.

## Filters

- **Opportunity type:** Request for EOI, Request for proposal, Request for quotation, Request for pre-qualification
- **Status:** active opportunities only
- **Service categories:** environmental services, management and business services, economics and statistics, education and training, public order and security, politics and civic affairs
- **Time window:** notices published in the last four days
- **Language:** English only, detected from the title and description rather than trusted from UNGM's tagging
- **Blocked keywords:** from `Sources/blocked_words.py`

## Files

| File | Purpose |
|---|---|
| `ungm_notion_upload.ipynb` | Fetches, filters and uploads |
| `ungm_contract_titles.csv` | Every title already uploaded. Prevents duplicates. Do not delete. |

## Notes

- The four-day window matters. Without it, the filters match over 1,700 currently open notices, most of them long-running calls that have already been uploaded. Four days covers the Friday to Monday gap, and the CSV catches any overlap.
- The category filter uses UNGM's own internal database row numbers, not the published UNSPSC codes those categories correspond to. Substituting real UNSPSC codes returns zero results without any error. Do not change that list without testing.
- Fields UNGM does not publish, and which are therefore left blank or marked unavailable in Notion: contract value, CPV codes, employer website.
- This source returns `500` errors more often than most. A single red cross is routine.
