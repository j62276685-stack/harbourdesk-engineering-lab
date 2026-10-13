# 12.3 — Build canonical customer identities and alias coverage

**Role:** Data migration engineer

**Purpose:** Turn a messy import into auditable customer identities with a recovery path.

**Stakeholder:** Customer-data owner and release reviewer.

## Task description

I am investigating how staged customer records should map to canonical identities and aliases. My goal is to provide the customer-data owner with a verified migration that accounts for every source row and enforces the required unique-email constraint.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `customer-canonicalization.patch`
- `customer-coverage.csv`
- `customer-identity-checks.md`

## Quality checks

- [ ] Canonical emails are uniquely constrained.
- [ ] The earliest import/ID tie-break chooses survivors.
- [ ] The provided expected 3 identities, 2 aliases and 3 quarantine records reconcile to 8 sources.
- [ ] Repeated execution preserves the same mapping without losing originals.

**Apps:** Visual Studio Code, DB Browser for SQLite, GitHub Desktop.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

**Starting dependency:** Your frozen [12.2](../12.2/GOAL.md) staging code/database is required as the starting input.

## Workflow

1. Inspect the staging input and implement the survivor/alias mapping.
2. Run the migration and use DB Browser to verify constraints and per-source coverage.
3. Review the focused diff and export canonical/alias/quarantine counts with repeat-run evidence.

## Recording script

Open the [Task 12 workspace](../../workspaces/12-messy-migration.code-workspace) in VS Code. Run commands from its Application terminal; keep that terminal open. Follow the steps in order. Inputs and source: [task brief](../../tasks/12-messy-migration/BRIEF.md), [legacy-customers.csv](../../tasks/12-messy-migration/inputs/legacy-customers.csv), [legacy-customers.json](../../tasks/12-messy-migration/inputs/legacy-customers.json), [target-contract.md](../../tasks/12-messy-migration/inputs/target-contract.md), [migration.py](../../../app/migration.py), [schema.sql](../../../app/schema.sql), [db.py](../../../app/db.py).

1. **Set up the session and output folder.** Copy the report template only if a report does not already exist.

```sh
./tds/lab start 12 --session 12.3
mkdir -p tds/tasks/12-messy-migration/outcomes/12.3
cp -n tds/docs/REPORT-TEMPLATE.md tds/tasks/12-messy-migration/outcomes/12.3/report.md
git status --short
```

2. **Reproduce and capture the baseline.** Read the staged rows and survivor contract; preserve a disposable backup before applying canonicalization.

Run the baseline commands in the Application terminal:

```sh
./tds/lab probe 12
LAB_DB=tds/tasks/12-messy-migration/outcomes/12.3/work.sqlite3 ./tds/lab init
```

3. **Investigate and create the deliverable.** Complete app/migration.py and schema constraints for normalized canonical email, stable survivor, aliases, and source-row coverage. Keep raw rows and quarantine reasons; make a second run a no-op.

4. **Verify the result.** On the disposable database check three canonical, two aliases, three quarantine, and all eight source IDs accounted for; rerun and compare counts, then review the patch.

Run the verification commands on this session’s disposable database; use DB Browser to compare counts before and after the second migration:

```sh
LAB_DB=tds/tasks/12-messy-migration/outcomes/12.3/work.sqlite3 ./tds/lab migrate
LAB_DB=tds/tasks/12-messy-migration/outcomes/12.3/work.sqlite3 ./tds/lab migrate
./tds/lab test
```

Before committing this session’s code, export the reviewed change as the required patch:

```sh
git add -N -- tests
git diff HEAD --binary -- app/migration.py app/schema.sql tests > tds/tasks/12-messy-migration/outcomes/12.3/customer-canonicalization.patch
```

5. **Save and review the handoff.** Finish `report.md` in `tds/tasks/12-messy-migration/outcomes/12.3/`. Save or export `customer-coverage.csv`, `customer-identity-checks.md` to the same folder using the named apps. Reopen every output, check the quality boxes above, and confirm the folder contents:

```sh
ls -lh tds/tasks/12-messy-migration/outcomes/12.3
git status --short
```

Keep the short introduction and complete on-screen process within 15:00–45:59. Narrate what, where, and why; keep task content visible and do not show AI interaction during the recording.
