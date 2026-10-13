# Task 12: Design a migration for messy existing data

## Error or request

I am investigating a legacy customer import containing inconsistent formats, duplicates and invalid records. My goal is to provide the customer-data owner with a verified migration that preserves source records, creates canonical identities, quarantines invalid data and supports rollback.

## Relevant files

[app/migration.py](../../../app/migration.py); [app/schema.sql](../../../app/schema.sql); [app/db.py](../../../app/db.py); [inputs/target-contract.md](inputs/target-contract.md); [legacy-customers.csv](inputs/legacy-customers.csv); [legacy-customers.json](inputs/legacy-customers.json). The JSON preserves null versus an empty string.

- [legacy-customers.csv](inputs/legacy-customers.csv)
- [legacy-customers.json](inputs/legacy-customers.json)
- [target-contract.md](inputs/target-contract.md)

## Reproduce or investigate

Open the [Task 12 workspace](../../workspaces/12-messy-migration.code-workspace). It uses the shared application and database. Read the inputs above. Run `./tds/lab serve` for browser work or `./tds/lab test` for tests.

Run `./tds/lab probe 12` on disposable data and inspect the raw eight-row fixture. Use a fresh LAB_DB copy for each destructive experiment. The target contract defines canonicalization, quarantine and count reconciliation.

## Completion criteria

1. Normalize valid email by trim/lowercase and merge according to the deterministic survivor rule; uniquely constrain canonical emails.
2. Preserve original raw rows and map every valid source row to its canonical record; quarantine every invalid/null/blank row with a reason.
3. Reconcile all eight inputs: three canonical identities, two merged aliases, three quarantine records; source-row coverage remains eight.
4. A second run is safe and does not duplicate, lose or silently alter records.
5. Demonstrate recovery from a failure mid-migration and restore a disposable database to its original schema/data. State backup/recovery steps and the point at which cutover is safe.

## Deliverable

Migration, reconciliation report, meaningful checks and recovery demonstration. Implement locally; no production rollout is requested.

## Task sessions

Choose a session below for its scope, apps, outputs and checks.

- [12.1 — Audit the eight-row legacy import and define cutover counts](../../sessions/12.1/GOAL.md)
- [12.2 — Implement reversible normalization and quarantine staging](../../sessions/12.2/GOAL.md)
- [12.3 — Build canonical customer identities and alias coverage](../../sessions/12.3/GOAL.md)
- [12.4 — Exercise migration rollback and make a cutover recommendation](../../sessions/12.4/GOAL.md)
