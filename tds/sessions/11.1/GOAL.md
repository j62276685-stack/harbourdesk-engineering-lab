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

## Recording script

Open the [Task 11 workspace](../../workspaces/11-slow-query.code-workspace) in VS Code. Run commands from its Application terminal; keep that terminal open. Follow the steps in order. Inputs and source: [task brief](../../tasks/11-slow-query/BRIEF.md), [report-contract.md](../../tasks/11-slow-query/inputs/report-contract.md), [reporting.py](../../../app/reporting.py), [schema.sql](../../../app/schema.sql).

1. **Set up the session and output folder.** Copy the report template only if a report does not already exist.

```sh
./tds/lab start 11 --session 11.1
mkdir -p tds/tasks/11-slow-query/outcomes/11.1
cp -n tds/docs/REPORT-TEMPLATE.md tds/tasks/11-slow-query/outcomes/11.1/report.md
git status --short
```

2. **Reproduce and capture the baseline.** Seed the benchmark dataset once, then capture nine warmed samples to the baseline JSON file. Keep this database for session 11.2.

Run the baseline commands in the Application terminal:

```sh
./tds/lab seed-large --rows 150000
./tds/lab benchmark --runs 9 > tds/tasks/11-slow-query/outcomes/11.1/report-baseline.json
```

3. **Investigate and create the deliverable.** In VS Code read app/reporting.py and the report contract. In DB Browser inspect EXPLAIN QUERY PLAN and row count. In Calc enter every sample, median, ordered-result hash, and plan; state one bounded index/query hypothesis.

4. **Verify the result.** Check the JSON has nine samples and a result digest. Export a performance note that does not claim a speedup before a comparable second run.

5. **Save and review the handoff.** Finish `report.md` in `tds/tasks/11-slow-query/outcomes/11.1/`. Save or export `report-baseline.ods`, `report-baseline.json`, `report-performance-note.pdf` to the same folder using the named apps. Reopen every output, check the quality boxes above, and confirm the folder contents:

```sh
ls -lh tds/tasks/11-slow-query/outcomes/11.1
git status --short
```

Keep the short introduction and complete on-screen process within 15:00–45:59. Narrate what, where, and why; keep task content visible and do not show AI interaction during the recording.
