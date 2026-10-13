# 12.2 — Implement reversible normalization and quarantine staging

**Role:** Data migration engineer

**Purpose:** Turn a messy import into auditable customer identities with a recovery path.

**Stakeholder:** Customer-data owner and release reviewer.

## Task description

I am investigating how to normalize the legacy customer import without losing source records or cutting over prematurely. My goal is to provide the customer-data owner with a rerunnable staging migration that preserves raw data and separates valid records from quarantined records.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `customer-staging.patch`
- `customer-staging-counts.csv`
- `customer-staging-checks.md`

## Quality checks

- [ ] Raw records retain original values and identifiers.
- [ ] Valid normalized and quarantine rows are classified by the target rule.
- [ ] The staging step is rerunnable without duplicate rows.
- [ ] The deliverable labels staging as staging and preserves the original customer table.

**Apps:** Visual Studio Code, DB Browser for SQLite, GitHub Desktop.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

**Starting dependency:** The supplied target contract suffices; the human-created [12.1](../12.1/GOAL.md) mapping may be supplied as design context.

## Workflow

1. Inspect the raw fixture/target contract and implement only the preservation/validation/staging step.
2. Apply it to a disposable DB and inspect each category in DB Browser.
3. Check rerun behavior and review the staged schema/source changes in GitHub Desktop.

## Recording script

Open the [Task 12 workspace](../../workspaces/12-messy-migration.code-workspace) in VS Code. Run commands from its Application terminal; keep that terminal open. Follow the steps in order. Inputs and source: [task brief](../../tasks/12-messy-migration/BRIEF.md), [legacy-customers.csv](../../tasks/12-messy-migration/inputs/legacy-customers.csv), [legacy-customers.json](../../tasks/12-messy-migration/inputs/legacy-customers.json), [target-contract.md](../../tasks/12-messy-migration/inputs/target-contract.md), [migration.py](../../../app/migration.py), [schema.sql](../../../app/schema.sql), [db.py](../../../app/db.py).

1. **Set up the session and output folder.** Copy the report template only if a report does not already exist.

```sh
./tds/lab start 12 --session 12.2
mkdir -p tds/tasks/12-messy-migration/outcomes/12.2
cp -n tds/docs/REPORT-TEMPLATE.md tds/tasks/12-messy-migration/outcomes/12.2/report.md
git status --short
```

2. **Reproduce and capture the baseline.** Record the eight source rows and create a fresh disposable database in this session’s output folder before any migration experiment.

Run the baseline commands in the Application terminal:

```sh
./tds/lab probe 12
LAB_DB=tds/tasks/12-messy-migration/outcomes/12.2/work.sqlite3 ./tds/lab init
```

3. **Investigate and create the deliverable.** In app/migration.py and app/schema.sql implement durable raw-row preservation, validation, and quarantine staging only. Do not canonicalize yet. Make rerun staging idempotent and keep writes transactionally grouped.

4. **Verify the result.** Run migration on the disposable database, inspect staged/raw/quarantine rows in DB Browser, rerun it, and export counts plus the source/schema patch.

Run the verification commands:

```sh
LAB_DB=tds/tasks/12-messy-migration/outcomes/12.2/work.sqlite3 ./tds/lab migrate
LAB_DB=tds/tasks/12-messy-migration/outcomes/12.2/work.sqlite3 ./tds/lab migrate
./tds/lab test
```

Before committing this session’s code, export the reviewed change as the required patch:

```sh
git add -N -- tests
git diff HEAD --binary -- app/migration.py app/schema.sql tests > tds/tasks/12-messy-migration/outcomes/12.2/customer-staging.patch
```

5. **Save and review the handoff.** Finish `report.md` in `tds/tasks/12-messy-migration/outcomes/12.2/`. Save or export `customer-staging-counts.csv`, `customer-staging-checks.md` to the same folder using the named apps. Reopen every output, check the quality boxes above, and confirm the folder contents:

```sh
ls -lh tds/tasks/12-messy-migration/outcomes/12.2
git status --short
```

Keep the short introduction and complete on-screen process within 15:00–45:59. Narrate what, where, and why; keep task content visible and do not show AI interaction during the recording.
