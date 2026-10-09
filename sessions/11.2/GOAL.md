# 11.2 — Optimize one report query and prove result equivalence

**Role:** Database performance engineer

**Purpose:** Improve the recent-order report without changing its answers.

**Stakeholder:** Operations dashboard owner.

## Task description

Apply one justified query/index change, compare its plan and warmed performance with the frozen baseline, and deliver the schema change and equivalence evidence.

## Final deliverable

- `report-optimization.patch`
- `report-before-after.json`
- `report-equivalence.md`

## Quality checks

- [ ] The same ordered rows and digest are returned.
- [ ] Before/after plans and nine warmed samples use the same workload.
- [ ] Another user/status and an empty result are checked.
- [ ] Improvement or measurement limits and write/storage cost are explained.

**Apps:** Visual Studio Code, DB Browser for SQLite, GitHub Desktop.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

**Starting dependency:** A frozen [11.1](../11.1/GOAL.md) baseline report is required; do not claim a baseline generated during an unrecorded optimization as your recorded work.

## Workflow

1. Inspect the frozen workload/baseline and choose one query or index adjustment.
2. Apply it using DB Browser and edit the fresh/existing database schema path in VS Code.
3. Rerun the same measurements and ordered-result checks, then review/export the patch in GitHub Desktop.
