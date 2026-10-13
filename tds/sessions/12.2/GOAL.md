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
