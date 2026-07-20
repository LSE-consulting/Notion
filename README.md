# Notion Upload — What This Does

This repo runs an automated pipeline that checks a set of public contract/tender
websites every weekday morning, picks out the ones relevant to us, and adds
them to the team's shared Notion database. It also does a daily tidy-up pass
that marks contracts as **Expired** once their closing date has passed.

You shouldn't need to touch any code to understand what's going on — this
doc explains it in plain English.

## The three websites it currently checks

Each website lives in its own folder under `Sources/`, so it's easy to see at
a glance what we're pulling from and to add more in future.

| Folder | Website | What it does |
|---|---|---|
| `Sources/UK Contracts` | [Contracts Finder](https://www.contractsfinder.service.gov.uk) (UK government) | Pulls open UK public-sector contracts matching our areas of work, then uploads new ones to Notion |
| `Sources/EU Contracts` | TED (Tenders Electronic Daily) | Pulls open EU tenders matching the same areas of work, then uploads new ones to Notion |
| `Sources/Find a Tender` | Find a Tender Service (UK, above-threshold contracts) | Same idea — searches, filters, and uploads new matches to Notion |

Each of these folders is self-contained: the notebook inside it, plus a
small CSV file that keeps track of what's already been uploaded (so we don't
create duplicates), plus a JSON file holding the raw data pulled from that
site's search. Adding a fourth, fifth, or sixth website later just means
adding a new folder in the same shape here.

## The other piece: keeping Notion tidy

| Folder | What it does |
|---|---|
| `Shared/Expired_Contracts_Update.ipynb` | Goes through the whole Notion database (not tied to one website) and flips any contract still marked "Open" to "Expired" once its closing date has passed |

This one lives outside `Sources/` because it works across all three
websites' entries at once, rather than belonging to just one of them.

## How and when it runs

Everything is automated through GitHub Actions (the `.github/workflows/schedule-notebooks.yml` file):

| When | What happens |
|---|---|
| Every weekday at 10:00 UTC | Runs all three website checks, then the expiry tidy-up, in order |
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
2. Put its notebook (and any CSV/JSON tracking files it needs) inside that folder.
3. Add one more step to the workflow file so GitHub Actions runs it on the same schedule.

The three existing folders in this repo are good templates to copy from.

## ⚠️ A security note — please read

While going through the files, I found that the **Notion access token** and
the **TED (EU tenders) API key** are written directly into several of the
notebooks, in plain text. That means anyone who can see this repo's code can
see those keys — and if this repo is public on GitHub (it was, at the time
this cleanup was done), they're currently exposed to the internet.

Whoever holds those keys should, as a priority:
- **Rotate/regenerate both keys** (the Notion integration token and the TED API key), since the current ones should be treated as compromised.
- Store the new ones as **GitHub Actions secrets** instead of in the notebook files, so they never appear in the code itself.
- If this repo doesn't need to be public, consider making it **private**.

I haven't changed any of the notebook code as part of this cleanup (as
requested), so the keys are still sitting in the files exactly as before —
this just flags it so it doesn't go unnoticed.

## One more thing I noticed (not changed)

`Sources/EU Contracts/ted_api_output.json` is a large (~21MB) file that
doesn't appear to be read by any of the code — it looks like a leftover data
dump from earlier testing. I've left it exactly where it was since it wasn't
part of what was asked, but it may be safe to delete if no one needs it, and
removing it would make the repo noticeably lighter to clone.

## What changed in this cleanup

To be transparent about exactly what was touched:

- **Moved** the three website folders under a new `Sources/` folder, and
  `Expired_Contracts_Update.ipynb` into a new `Shared/` folder — no file
  contents were changed, only their location.
- **Updated** `.github/workflows/schedule-notebooks.yml` so it points at the
  new file locations. This was the only file whose actual content changed.
- **Removed** a stray `.DS_Store` file (a harmless macOS system file that
  shouldn't have been tracked in git) and added a `.gitignore` so it doesn't
  come back.
- Did **not** touch any notebook or script logic.
