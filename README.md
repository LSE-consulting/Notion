# Notion Upload — What This Does

This repo runs an automated pipeline that checks a set of public contract/tender
websites every weekday morning, picks out the ones relevant to us, and adds
them to the team's shared Notion database. It also does a daily tidy-up pass
that marks contracts as **Expired** once their closing date has passed.

You shouldn't need to touch any code to understand what's going on — this
doc explains it in plain English.

## The websites it currently checks

Each website lives in its own folder under `Sources/`, so it's easy to see at
a glance what we're pulling from and to add more in future.

| Folder | Website | What it does |
|---|---|---|
| `Sources/UK Contracts` | [Contracts Finder](https://www.contractsfinder.service.gov.uk) (UK government) | Pulls open UK public-sector contracts matching our areas of work, then uploads new ones to Notion |
| `Sources/EU Contracts` | [TED](https://ted.europa.eu/) (Tenders Electronic Daily) | Pulls open EU tenders matching the same areas of work, then uploads new ones to Notion |
| `Sources/Find a Tender` | [Find a Tender Service](https://www.find-tender.service.gov.uk/) (UK, above-threshold contracts) | Same idea — searches, filters, and uploads new matches to Notion |
| `Sources/EU Commission` | [EU Funding & Tenders Portal](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-tenders) (Calls for Tenders) | Pulls live calls for tenders direct from EU institutions, then uploads new matches to Notion |
| `Sources/UNGM` | [UN Global Marketplace](https://www.ungm.org/) | Pulls UN agency procurement notices, then uploads new matches to Notion |
| `Sources/World Bank` | [World Bank Business Opportunities](https://projects.worldbank.org/en/projects-operations/opportunities) | Pulls open Consultant Services opportunities, then uploads new matches to Notion |

Each of these folders is self-contained: the notebook inside it, plus a
small CSV file that keeps track of what's already been uploaded (so we don't
create duplicates). UK Contracts is a little different from the rest — it
also has a separate fetch script (`api_filtered_contracts.py`) and a JSON
file that caches the raw data that script pulls before the notebook uploads
it. The other five folders don't need this extra step; their notebooks fetch
and upload in one go. Adding a new website later just means adding a new
folder in whichever of these two shapes fits best.

## The other piece: keeping Notion tidy

| Folder | What it does |
|---|---|
| `Shared/Expired_Contracts_Update.ipynb` | Goes through the whole Notion database (not tied to one website) and flips any contract still marked "Open" to "Expired" once its closing date has passed |

This one lives outside `Sources/` because it works across every website's
entries at once, rather than belonging to just one of them.

## How and when it runs

Everything is automated through GitHub Actions (the `.github/workflows/schedule-notebooks.yml` file):

| When | What happens |
|---|---|
| Every weekday at 10:00 UTC | Runs all six website checks, then the expiry tidy-up, in order |
| Anytime, on demand | A team member with repo access can trigger the same run manually from the "Actions" tab on GitHub ("Run workflow" button) |

It does **not** run on weekends. If Monday morning's Notion board looks the
same as Friday afternoon's, that's expected — nothing runs Saturday or
Sunday.

At the end of a run, if any of the tracking CSV/JSON files changed, the
automation commits those changes back to this repo itself — that's why
you'll see commits like "Updated files after automated run" in the history
even though no person made them.

## Adding a new website in future

Since each website already has its own self-contained folder under
`Sources/`, adding one more should follow the same pattern:

1. Create a new folder under `Sources/` for the new website.
2. Put its notebook (and a CSV tracking file, self-created on first run) inside
   that folder.
3. Add one more step to the workflow file so GitHub Actions runs it on the same schedule.

The existing folders in this repo are good templates to copy from — `Sources/World Bank`
is the most recently added and a good starting point.
