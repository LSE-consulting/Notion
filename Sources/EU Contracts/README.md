# EU TED (Tenders Electronic Daily)

The EU-wide public register of tender notices.

**Website:** https://ted.europa.eu/

## How it works

`EU_API_clean.ipynb` queries the TED search API for active notices in the target CPV categories, then uploads anything new to Notion.

## Filters

- **CPV codes:** the standard 27-code consultancy and research list
- **Notice type:** standard, social and competition-based tender notices. Award notices are excluded.
- **Language:** English only, checked against TED's own official-language field
- **Scope:** active notices only
- **Blocked keywords:** from `Sources/blocked_words.py`

## Files

| File | Purpose |
|---|---|
| `EU_API_clean.ipynb` | Fetches, filters and uploads |
| `EU_contract_titles.csv` | Every title already uploaded. Prevents duplicates. Do not delete. |
| `ted_api_output.json` | Raw response from the last run, kept for reference. Not read by anything. |

## Notes

- The notebook requests 10 pages of 50 results per run, so a maximum of 500 notices per run.
- Titles are matched for duplicates after trimming and lowercasing, so small formatting changes on TED's side will not cause a re-upload.
- The API key is written into the notebook rather than stored as a secret. It is a public TED key rather than a private credential, but it should be moved to GitHub secrets if this repository stays public.
