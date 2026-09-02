# Shared

Notebooks that work across the whole Notion database rather than one website.

## `Expired_Contracts_Update.ipynb`

Finds every contract still marked **Open** whose closing date has already passed, and changes its status to **Expired**.

Runs once at the end of every pipeline run, after all eight sources. It does not fetch anything from the web and does not add or delete records, it only changes the status field on records that already exist.

If contracts are still showing as Open past their closing date, check the **Execute Expired Contract Update Notebook** step in the most recent run.
