# 04.1 — Turn the pagination complaint into a regression repair

**Role:** Software quality engineer

**Purpose:** Turn an ambiguous pagination complaint into a verified regression repair.

**Stakeholder:** Customer-account product owner.

## Task description

Define the expected first-page result from the contract, write a deterministic failing regression, make a focused repair and provide before/after QA evidence.

## Final deliverable

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
