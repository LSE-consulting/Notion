# UK Contracts Finder

The UK government's register of public sector contract opportunities.

**Website:** https://www.contractsfinder.service.gov.uk

## How it works

This source runs in two steps, unlike the others.

1. `api_filtered_contracts.py` queries the Contracts Finder API for open notices in the target CPV categories, applies the shared blocklist, and writes the results to `output_data.json`.
2. `UK_notion_upload.ipynb` reads that file, then scrapes the live search results pages to collect the display fields the API does not return (value, location, client, description). It also opens each contract page to read its CPV codes, then uploads anything new to Notion.

Both steps are listed separately in the workflow file. If the first fails, the second has nothing to read and will produce no uploads.

## Filters

- **CPV codes:** the standard 27-code consultancy and research list, applied in step 1
- **Notice types:** Contract, Pipeline, Pre-procurement
- **Status:** Open only
- **Blocked keywords:** applied in both steps, from `Sources/blocked_words.py`

## Files

| File | Purpose |
|---|---|
| `api_filtered_contracts.py` | Step 1. Fetches and filters, writes `output_data.json`. |
| `output_data.json` | Handover file between the two steps. Overwritten each run. |
| `UK_notion_upload.ipynb` | Step 2. Scrapes display fields and uploads to Notion. |
| `contract_titles.csv` | Every title already uploaded. Prevents duplicates. Do not delete. |

## Notes

- The scrape loops through the first 49 pages of search results. If Contracts Finder ever returns more than that for our filters, later results would be missed.
- Two blocks of code in the notebook are commented out on purpose: one rebuilds `contract_titles.csv` from scratch if it is ever lost, the other removes duplicates from Notion. Neither runs automatically.
