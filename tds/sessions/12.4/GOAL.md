# 12.4 — Exercise migration rollback and make a cutover recommendation

**Role:** Data migration engineer

**Purpose:** Turn a messy import into auditable customer identities with a recovery path.

**Stakeholder:** Customer-data owner and release reviewer.

## Task description

I am investigating whether the proposed customer migration can recover from an interruption. My goal is to provide the release reviewer with a tested rollback procedure and an evidence-based recommendation on whether the migration is ready for cutover.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `migration-recovery-checks.ods`
- `migration-recovery-evidence.json`
- `migration-cutover-verdict.pdf`

## Quality checks

- [ ] A named interruption and an actual restore are demonstrated.
- [ ] Original schema/raw rows are recoverable and compared.
- [ ] A rerun has explicit outcomes and no unexplained loss/duplication.
- [ ] The cutover verdict is evidence-backed, including a hold decision if checks fail.

**Apps:** Visual Studio Code, DB Browser for SQLite, LibreOffice.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

**Starting dependency:** A frozen [12.3](../12.3/GOAL.md) candidate migration and pre-migration disposable backup are required.

## Workflow

1. Inspect the frozen migration and choose one meaningful interruption/cutover boundary.
2. Execute the bounded failure/recovery drill and compare restored schema/rows with the original using DB Browser.
3. In LibreOffice complete the recovery evidence table and write the release recommendation with remaining risks.
