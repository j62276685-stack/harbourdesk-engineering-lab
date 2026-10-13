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

## Recording script

Open the [Task 04 workspace](../../workspaces/04-complaint-regression.code-workspace) in VS Code. Run commands from its Application terminal; keep that terminal open. Follow the steps in order. Inputs and source: [task brief](../../tasks/04-complaint-regression/BRIEF.md), [complaint.txt](../../tasks/04-complaint-regression/inputs/complaint.txt), [orders.py](../../../app/orders.py), [http.py](../../../app/http.py), [test_baseline.py](../../../tests/test_baseline.py).

1. **Set up the session and output folder.** Copy the report template only if a report does not already exist.

```sh
./tds/lab start 04 --session 04.1
mkdir -p tds/tasks/04-complaint-regression/outcomes/04.1
cp -n tds/docs/REPORT-TEMPLATE.md tds/tasks/04-complaint-regression/outcomes/04.1/report.md
git status --short
```

2. **Reproduce and capture the baseline.** Run the pagination probe and compare the full owned list with pages one and two in Firefox. Query seed rows so expected IDs come from the database, not the faulty endpoint.

For browser work, start the app in a second terminal with the command below. Open http://localhost:8010 in Firefox; use the example Ada or Ben account and the displayed practice password. Keep the server terminal open and stop it with Control-C when finished.

```sh
./tds/lab serve
```

Run the baseline commands in the Application terminal:

```sh
./tds/lab probe 4
./tds/lab sql 'SELECT id,user_id FROM orders ORDER BY id'
```

3. **Investigate and create the deliverable.** Add at least five owned rows to a regression fixture. Write a test that fails because app/orders.py starts page one at the second slice; change the offset to (page - 1) times page_size while retaining the existing validation and ownership filter.

4. **Verify the result.** Capture the failing test before the fix and a passing run after. Check size one, later pages, out-of-range page, invalid page, and Ben isolation; export the ordered ID evidence.

Run the verification commands:

```sh
./tds/lab probe 4
./tds/lab test
```

Before committing this session’s code, export the reviewed change as the required patch:

```sh
git add -N -- tests
git diff HEAD --binary -- app/orders.py tests > tds/tasks/04-complaint-regression/outcomes/04.1/pagination-regression.patch
```

5. **Save and review the handoff.** Finish `report.md` in `tds/tasks/04-complaint-regression/outcomes/04.1/`. Save or export `pagination-qa.md`, `page-order-evidence.csv` to the same folder using the named apps. Reopen every output, check the quality boxes above, and confirm the folder contents:

```sh
ls -lh tds/tasks/04-complaint-regression/outcomes/04.1
git status --short
```

Keep the short introduction and complete on-screen process within 15:00–45:59. Narrate what, where, and why; keep task content visible and do not show AI interaction during the recording.
