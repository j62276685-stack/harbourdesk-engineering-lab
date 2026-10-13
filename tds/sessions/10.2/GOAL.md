# 10.2 — Repair and verify order ownership enforcement

**Role:** Application security engineer

**Purpose:** Protect one customer’s orders from another authenticated customer.

**Stakeholder:** Security reviewer and account-service owner.

## Task description

I am investigating the order-service boundary that permits cross-user access. My goal is to provide the account-service owner with a verified ownership repair that rejects unauthorized reads and changes while preserving legitimate customer access.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `ownership-fix.patch`
- `ownership-http-checks.md`
- `ownership-state-evidence.csv`

## Quality checks

- [ ] Unowned and unknown orders use the same documented 404 response.
- [ ] The owner retains valid read and mutation behavior on fresh data.
- [ ] Unauthenticated requests fail independently.
- [ ] Rejected cross-user requests leave status and version unchanged.

**Apps:** Visual Studio Code, Firefox, DB Browser for SQLite.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

**Starting dependency:** The supplied access matrix is sufficient; [10.1](../10.1/GOAL.md) may be included as context.

## Workflow

1. Write focused session-based denied/allowed checks and implement the ownership repair.
2. Validate selected routes through Firefox request inspection.
3. Use DB Browser to verify rejected mutations left rows unchanged and export the source/test evidence.

## Recording script

Open the [Task 10 workspace](../../workspaces/10-cross-user-access.code-workspace) in VS Code. Run commands from its Application terminal; keep that terminal open. Follow the steps in order. Inputs and source: [task brief](../../tasks/10-cross-user-access/BRIEF.md), [access-matrix.csv](../../tasks/10-cross-user-access/inputs/access-matrix.csv), [orders.py](../../../app/orders.py), [http.py](../../../app/http.py).

1. **Set up the session and output folder.** Copy the report template only if a report does not already exist.

```sh
./tds/lab start 10 --session 10.2
mkdir -p tds/tasks/10-cross-user-access/outcomes/10.2
cp -n tds/docs/REPORT-TEMPLATE.md tds/tasks/10-cross-user-access/outcomes/10.2/report.md
git status --short
```

2. **Reproduce and capture the baseline.** Capture Ada and Ben baseline requests on fresh seed data and record ord_ben status/version before a rejected mutation.

For browser work, start the app in a second terminal with the command below. Open http://localhost:8010 in Firefox; use the example Ada or Ben account and the displayed practice password. Keep the server terminal open and stop it with Control-C when finished.

```sh
./tds/lab serve
```

Run the baseline commands in the Application terminal:

```sh
./tds/lab probe 10
```

3. **Investigate and create the deliverable.** In app/orders.py scope reads and all update predicates to the authenticated user ID; let app/http.py continue deriving identity from the session, not request data. Add tests for both ownership directions, unknown IDs, unauthenticated calls, and unchanged rejected rows.

4. **Verify the result.** Run the probe and suite, then repeat the Firefox requests. In DB Browser verify denied pay/transition left the target row unchanged; export the patch and HTTP results.

Run the verification commands:

```sh
./tds/lab probe 10
./tds/lab test
```

Before committing this session’s code, export the reviewed change as the required patch:

```sh
git add -N -- tests
git diff HEAD --binary -- app/orders.py app/http.py tests > tds/tasks/10-cross-user-access/outcomes/10.2/ownership-fix.patch
```

5. **Save and review the handoff.** Finish `report.md` in `tds/tasks/10-cross-user-access/outcomes/10.2/`. Save or export `ownership-http-checks.md`, `ownership-state-evidence.csv` to the same folder using the named apps. Reopen every output, check the quality boxes above, and confirm the folder contents:

```sh
ls -lh tds/tasks/10-cross-user-access/outcomes/10.2
git status --short
```

Keep the short introduction and complete on-screen process within 15:00–45:59. Narrate what, where, and why; keep task content visible and do not show AI interaction during the recording.
