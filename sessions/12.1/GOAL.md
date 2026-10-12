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
