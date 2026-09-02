# Council of Europe (eProc)

Calls for tenders published by the Council of Europe.

**Website:** https://eproc.coe.int/callfortenders-list

## How it works

`coe_notion_upload.ipynb` fetches all currently published calls for tenders from the eProc portal and uploads anything new to Notion.

## Filters

- **Status:** published tenders only
- **Language:** English and Spanish only, detected from the title
- **Deadline:** tenders past their deadline are skipped
- **Blocked keywords:** from `Sources/blocked_words.py`
- **No CPV or category filter**

## Files

| File | Purpose |
|---|---|
| `coe_notion_upload.ipynb` | Fetches, filters and uploads |
| `coe_contract_titles.csv` | Every title already uploaded. Prevents duplicates. Do not delete. |

## Notes

- **Why there is no category filter.** eProc tags its tenders with its own internal category scheme, and only around half carry a CPV code at all. Applying the standard 27-code CPV list matched just 1 of 25 live tenders in testing. This source publishes few enough opportunities, most of them broadly relevant, that filtering was judged not worth the loss.
- **The language filter is done here, not by the portal.** Setting the API to English only changes the display language, it does not filter tender content. French-only tenders were arriving labelled as English before this was corrected.
- **There is no description field on this source.** The `Description` field in Notion is built from the tender title plus its category labels. It is not free text from the tender itself.
- **The contract link is a constructed guess.** The URL pattern used has not been confirmed against the live site. Anyone relying on these links should verify one before assuming they all work.
- `Client` and `Employer Website` are set to the Council of Europe for every entry, since the portal serves a single institution and publishes no separate buyer field.
