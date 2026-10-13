# 12.1 — Audit the eight-row legacy import and define cutover counts

**Role:** Data migration engineer

**Purpose:** Turn a messy import into auditable customer identities with a recovery path.

**Stakeholder:** Customer-data owner and release reviewer.

## Task description

I am investigating a legacy customer import containing inconsistent formats, duplicate identities, missing values and invalid records. My goal is to provide the customer-data owner with a deterministic identity mapping and quarantine plan that accounts for all eight source rows.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `customer-migration-ledger.ods`
- `customer-target-model.drawio`
- `customer-migration-design.pdf`

## Quality checks

- [ ] All eight raw source rows are accounted for.
- [ ] Normalization and survivor/tie-break rules are applied explicitly.
- [ ] Null, blank and invalid values have distinct recorded reasons.
- [ ] Identity count is distinguished from source-row coverage.

**Apps:** DB Browser for SQLite, LibreOffice, draw.io Desktop.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

## Workflow

1. Inspect raw null/blank/padded records and schema in DB Browser.
2. Build the source-to-identity/quarantine ledger and reconciliation counts in Calc.
3. Draw the target source/canonical/alias/quarantine relationships and export the design note.

## Recording script

Open the [Task 12 workspace](../../workspaces/12-messy-migration.code-workspace) in VS Code. Run commands from its Application terminal; keep that terminal open. Follow the steps in order. Inputs and source: [task brief](../../tasks/12-messy-migration/BRIEF.md), [legacy-customers.csv](../../tasks/12-messy-migration/inputs/legacy-customers.csv), [legacy-customers.json](../../tasks/12-messy-migration/inputs/legacy-customers.json), [target-contract.md](../../tasks/12-messy-migration/inputs/target-contract.md), [migration.py](../../../app/migration.py), [schema.sql](../../../app/schema.sql), [db.py](../../../app/db.py).

1. **Set up the session and output folder.** Copy the report template only if a report does not already exist.

```sh
./tds/lab start 12 --session 12.1
mkdir -p tds/tasks/12-messy-migration/outcomes/12.1
cp -n tds/docs/REPORT-TEMPLATE.md tds/tasks/12-messy-migration/outcomes/12.1/report.md
git status --short
```

2. **Reproduce and capture the baseline.** Read the JSON fixture to distinguish null from blank; use DB Browser to inspect the eight raw rows and current uniqueness behavior. Run the disposable migration probe.

Run the baseline commands in the Application terminal:

```sh
./tds/lab probe 12
```

3. **Investigate and create the deliverable.** In Calc make one row per source ID with raw email, normalized email or quarantine reason, canonical survivor, and alias mapping. Apply the supplied earliest imported_at then lowest ID survivor rule. Draw raw/canonical/alias/quarantine tables.

4. **Verify the result.** Reconcile five valid rows into three canonical identities and two aliases, plus three quarantined rows. Export the design and cutover counts without altering the shared DB.

5. **Save and review the handoff.** Finish `report.md` in `tds/tasks/12-messy-migration/outcomes/12.1/`. Save or export `customer-migration-ledger.ods`, `customer-target-model.drawio`, `customer-migration-design.pdf` to the same folder using the named apps. Reopen every output, check the quality boxes above, and confirm the folder contents:

```sh
ls -lh tds/tasks/12-messy-migration/outcomes/12.1
git status --short
```

Keep the short introduction and complete on-screen process within 15:00–45:59. Narrate what, where, and why; keep task content visible and do not show AI interaction during the recording.
