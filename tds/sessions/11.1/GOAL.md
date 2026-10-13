# 11.1 — Measure the bounded report query baseline

**Role:** Database performance engineer

**Purpose:** Improve the recent-order report without changing its answers.

**Stakeholder:** Operations dashboard owner.

## Task description

I am investigating a report that the recent-order dashboard becomes slow as order volume grows. My goal is to provide the dashboard owner with a reproducible performance baseline, an explanation of the query plan and a focused optimization hypothesis.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `report-baseline.ods`
- `report-baseline.json`
- `report-performance-note.pdf`

## Quality checks

- [ ] Workload, row count, machine/runtime and parameters are explicit.
- [ ] Nine samples plus warm-up and median calculation are preserved.
- [ ] Plan and ordered-result identity are attached to the measurement.
- [ ] The hypothesis names a plan/work concern without inventing an observed speedup.

**Apps:** Visual Studio Code, DB Browser for SQLite, LibreOffice.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

## Workflow

1. Inspect the actual report SQL and seeded row count.
2. Collect nine warmed timing samples through the VS Code task menu and inspect EXPLAIN/query results in DB Browser.
3. In LibreOffice calculate the median and record result identity, plan evidence and a bounded hypothesis.
