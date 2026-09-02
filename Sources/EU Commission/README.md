# EU Commission (Funding and Tenders Portal)

Calls for tenders issued directly by European Commission institutions and agencies.

**Website:** https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-tenders

## How it works

`eu_commission_notion_upload.ipynb` queries the portal's search API for live calls for tenders, keeps those matching the target CPV codes, and uploads anything new to Notion.

## Filters

- **Procedure type:** Open procedure, Call for expression of interest (both variants), Planned negotiation procedure, Accelerated open procedure
- **Status:** Forthcoming and Open. Closed calls are excluded.
- **Language:** English
- **CPV codes:** the standard consultancy and research list, matched after fetching rather than by the API
- **Blocked keywords:** from `Sources/blocked_words.py`

## Files

| File | Purpose |
|---|---|
| `eu_commission_notion_upload.ipynb` | Fetches, filters and uploads |
| `eu_commission_contract_titles.csv` | Every title already uploaded. Prevents duplicates. Do not delete. |

## Notes

- The portal identifies procedure types and statuses by numeric code rather than by name. Those codes are listed with comments in the notebook. They were confirmed by inspecting the live site, so if the portal changes them, results will silently drop to zero rather than error.
- Buyer names are read from the lead contracting authority field. The portal's own `caName` field is unreliable and is deliberately not used.
- Where a closing date is missing, the notebook falls back to the publication date plus two months.
