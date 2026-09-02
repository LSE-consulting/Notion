# IDB (Inter-American Development Bank)

Consultancy procurement notices from the IDB's open data platform.

**Website:** https://data.iadb.org/dataset/project-procurement-bidding-notices-and-notification-of-contract-awards

## How it works

`idb_notion_upload.ipynb` queries the IDB's open procurement dataset for recent consultancy notices and uploads anything new to Notion.

## Filters

- **Notice type:** General Procurement Notice and Expression of Interest
- **Title keywords:** Consultancy, Consultant, Consulting, Advisory, Consultoría, Consultora, Consultoria
- **Language:** English or Spanish only, detected from the notice title
- **Time window:** notices published in the last four days
- **Deadline:** already-expired notices are skipped
- **Blocked keywords:** from `Sources/blocked_words.py`

## Files

| File | Purpose |
|---|---|
| `idb_notion_upload.ipynb` | Fetches, filters and uploads |
| `idb_contract_titles.csv` | Every title already uploaded. Prevents duplicates. Do not delete. |

## Notes

- **Deadlines from this source are unreliable.** The dataset regularly returns dates that fall before the publication date, and placeholder values such as `2001-01-01`. The notebook only trusts a deadline if it falls after the publication date, otherwise it uses the publication date plus two months. Closing dates on IDB entries in Notion should be treated as indicative and checked against the original notice.
- This is the only source that accepts Spanish as well as English.
- Fields the dataset does not publish, and which are therefore left blank or marked unavailable in Notion: contract value, CPV codes, client, employer website.
- Notice type values in the source data have inconsistent trailing spaces, so the notebook matches on the start of the value rather than the whole thing.
