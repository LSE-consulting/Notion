# World Bank Business Opportunities

Consultant Services opportunities from World Bank-funded projects.

**Website:** https://projects.worldbank.org/en/projects-operations/opportunities

## How it works

`worldbank_notion_upload.ipynb` queries the World Bank procurement notices API for currently open Consultant Services opportunities and uploads anything new to Notion.

## Filters

- **Procurement type:** Consultant Services only
- **Sector:** an include-list of around 52 sectors, covering everything except Health Facilities and Construction, Housing Construction, ICT Infrastructure, Irrigation and Drainage, Other Water Supply/Sanitation/Waste Management, and Waste Management
- **Deadline:** currently open opportunities only
- **Language:** English only, checked against the API's own language field
- **Blocked keywords:** from `Sources/blocked_words.py`

## Files

| File | Purpose |
|---|---|
| `worldbank_notion_upload.ipynb` | Fetches, filters and uploads |
| `world_bank_contract_titles.csv` | Every title already uploaded. Prevents duplicates. Do not delete. |

## Notes

- The World Bank uses its own sector taxonomy rather than CPV codes, and the filtering is done by the API rather than in the notebook. The `CPV Codes` field in Notion is set to "Not Applicable" so it does not look like a gap in the scrape.
- The API sits behind bot protection. The notebook sends browser-style headers to avoid being blocked. If this source starts failing consistently with `403`, that protection has tightened and the request needs revisiting.
- Sector names in the include-list must match the World Bank's spelling exactly, including some with irregular spacing. Correcting them would silently drop those sectors.
