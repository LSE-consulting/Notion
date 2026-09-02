# Find a Tender

The UK register for higher-value public sector contracts, above the Contracts Finder threshold.

**Website:** https://www.find-tender.service.gov.uk/

## How it works

`Find_tender_notion.ipynb` queries the Find a Tender API for notices updated in the last two days, keeps those matching the target CPV codes, and uploads anything new to Notion.

## Filters

- **CPV codes:** the standard 27-code consultancy and research list
- **Time window:** rolling two-day lookback on the notice's last-updated date
- **Notice type:** pre-award notices only. Award and contract notices are excluded.
- **Blocked keywords:** from `Sources/blocked_words.py`

## Files

| File | Purpose |
|---|---|
| `Find_tender_notion.ipynb` | Fetches, filters and uploads |
| `contract_titles.csv` | Every title already uploaded. Prevents duplicates. Do not delete. |

## Notes

- This source is the most frequent source of one-off failures. It returns `502` and `503` errors more often than the others. A single red cross here is routine.
- The notebook already handles that: it retries automatically, waits longer between attempts, and splits its time window into smaller slices if a request keeps failing. A step only fails once those retries are exhausted.
- The two-day window covers a normal weekend gap. A longer outage, such as three or more consecutive failed runs, can leave notices unseen even after the source recovers.
