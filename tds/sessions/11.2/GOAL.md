# 11.2 — Optimize one report query and prove result equivalence

**Role:** Database performance engineer

**Purpose:** Improve the recent-order report without changing its answers.

**Stakeholder:** Operations dashboard owner.

## Task description

I am investigating the query and indexing choices behind the slow recent-order report. My goal is to provide the dashboard owner with a measured optimization and evidence that it returns the same results as the recorded baseline.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
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

## Recording script

Open the [Task 11 workspace](../../workspaces/11-slow-query.code-workspace) in VS Code. Run commands from its Application terminal; keep that terminal open. Follow the steps in order. Inputs and source: [task brief](../../tasks/11-slow-query/BRIEF.md), [report-contract.md](../../tasks/11-slow-query/inputs/report-contract.md), [reporting.py](../../../app/reporting.py), [schema.sql](../../../app/schema.sql).

1. **Set up the session and output folder.** Copy the report template only if a report does not already exist.

```sh
./tds/lab start 11 --session 11.2
mkdir -p tds/tasks/11-slow-query/outcomes/11.2
cp -n tds/docs/REPORT-TEMPLATE.md tds/tasks/11-slow-query/outcomes/11.2/report.md
git status --short
```

2. **Reproduce and capture the baseline.** Open the saved baseline JSON and use the same database, hardware, query parameters, and warmed nine-run method. Record the original digest before editing.

Run the baseline commands in the Application terminal:

```sh
cp tds/tasks/11-slow-query/outcomes/11.1/report-baseline.json tds/tasks/11-slow-query/outcomes/11.2/report-before.json
```

3. **Investigate and create the deliverable.** Make one justified index or SQL change in app/schema.sql or app/reporting.py. If testing an index in DB Browser first, apply the same change to fresh-database initialization so the repair persists.

4. **Verify the result.** Run nine samples again, compare median, plan, count, and exact result digest. Revert or explain any row/order difference; report write/storage cost and measurement limits.

Run the verification commands. The combined JSON keeps both nine-sample records and their plans for comparison:

```sh
./tds/lab benchmark --runs 9 > tds/tasks/11-slow-query/outcomes/11.2/report-after.json
python3 -c 'import json,sys; print(json.dumps({"before":json.load(open(sys.argv[1])),"after":json.load(open(sys.argv[2]))},indent=2))' tds/tasks/11-slow-query/outcomes/11.2/report-before.json tds/tasks/11-slow-query/outcomes/11.2/report-after.json > tds/tasks/11-slow-query/outcomes/11.2/report-before-after.json
./tds/lab test
```

Before committing this session’s code, export the reviewed change as the required patch:

```sh
git add -N -- tests
git diff HEAD --binary -- app/reporting.py app/schema.sql tests > tds/tasks/11-slow-query/outcomes/11.2/report-optimization.patch
```

5. **Save and review the handoff.** Finish `report.md` in `tds/tasks/11-slow-query/outcomes/11.2/`. Save or export `report-before-after.json`, `report-equivalence.md` to the same folder using the named apps. Reopen every output, check the quality boxes above, and confirm the folder contents:

```sh
ls -lh tds/tasks/11-slow-query/outcomes/11.2
git status --short
```

Keep the short introduction and complete on-screen process within 15:00–45:59. Narrate what, where, and why; keep task content visible and do not show AI interaction during the recording.
