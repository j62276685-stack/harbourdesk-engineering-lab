# 04.1 — Turn the pagination complaint into a regression repair

**Role:** Software quality engineer

**Purpose:** Turn an ambiguous pagination complaint into a verified regression repair.

**Stakeholder:** Customer-account product owner.

## Task description

I am investigating a customer report that the first page of orders skips records and later pages look incorrect. My goal is to provide the account product owner with a deterministic regression test, a focused pagination repair and evidence that the expected records now appear.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `pagination-regression.patch`
- `pagination-qa.md`
- `page-order-evidence.csv`

## Quality checks

- [ ] The new regression demonstrably fails before and passes after.
- [ ] Page concatenation has no gap or duplicated ID.
- [ ] Page one, size one and an out-of-range page are checked.
- [ ] The verified list excludes the other customer’s records.

**Apps:** Visual Studio Code, Firefox, DB Browser for SQLite.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

## Workflow

1. Compare the full order list with page-one/page-two responses in Firefox and seed records in DB Browser.
2. Write the smallest meaningful regression and repair in VS Code, with at least five owned rows.
3. Use the task menu to rerun the test and confirm the final concatenated page IDs against database ordering.
