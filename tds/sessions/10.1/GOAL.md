# 10.1 — Audit an authenticated cross-user access path

**Role:** Application security engineer

**Purpose:** Protect one customer’s orders from another authenticated customer.

**Stakeholder:** Security reviewer and account-service owner.

## Task description

I am investigating whether one authenticated customer can read or change another customer’s order. My goal is to provide the security reviewer and account-service owner with a source-linked access matrix and an evidence-based severity and repair recommendation.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `access-matrix.csv`
- `ownership-finding.md`
- `access-response-evidence.png`

## Quality checks

- [ ] Caller identity comes from the authenticated session.
- [ ] Read/pay/transition are compared on fresh copies.
- [ ] Unowned/unknown response leakage and persisted mutation effects are considered.
- [ ] The report includes legitimate access, not only a denied-case claim.

**Apps:** Firefox, Visual Studio Code, DB Browser for SQLite.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

## Workflow

1. Inspect session identity and the seeded ownership record in DB Browser.
2. Use two clean Firefox sessions and selected direct requests to compare allowed/denied behavior.
3. Trace the route/service ownership boundary in VS Code and write the access evidence and scoped recommendation.

## Recording script

Open the [Task 10 workspace](../../workspaces/10-cross-user-access.code-workspace) in VS Code. Run commands from its Application terminal; keep that terminal open. Follow the steps in order. Inputs and source: [task brief](../../tasks/10-cross-user-access/BRIEF.md), [access-matrix.csv](../../tasks/10-cross-user-access/inputs/access-matrix.csv), [orders.py](../../../app/orders.py), [http.py](../../../app/http.py).

1. **Set up the session and output folder.** Copy the report template only if a report does not already exist.

```sh
./tds/lab start 10 --session 10.1
mkdir -p tds/tasks/10-cross-user-access/outcomes/10.1
cp -n tds/docs/REPORT-TEMPLATE.md tds/tasks/10-cross-user-access/outcomes/10.1/report.md
git status --short
```

2. **Reproduce and capture the baseline.** Run the ownership probe, then inspect ord_ben and both user IDs in DB Browser. Use separate Firefox sessions for Ada and Ben so cookies do not mix.

For browser work, start the app in a second terminal with the command below. Open http://localhost:8010 in Firefox; use the example Ada or Ben account and the displayed practice password. Keep the server terminal open and stop it with Control-C when finished.

```sh
./tds/lab serve
```

Run the baseline commands in the Application terminal:

```sh
./tds/lab probe 10
./tds/lab sql 'SELECT id,user_id,status,version FROM orders WHERE id="ord_ben"'
```

3. **Investigate and create the deliverable.** In Firefox compare read, pay, and transition requests for ord_ben under each session; capture the denied response. Trace app/orders.py get_order and mutation predicates plus app/http.py session identity, and fill an access matrix with expected versus actual results.

4. **Verify the result.** Confirm the finding does not expose Ben’s order fields in a denied response. Record before/after status and version for any denied mutation.

5. **Save and review the handoff.** Finish `report.md` in `tds/tasks/10-cross-user-access/outcomes/10.1/`. Save or export `access-matrix.csv`, `ownership-finding.md`, `access-response-evidence.png` to the same folder using the named apps. Reopen every output, check the quality boxes above, and confirm the folder contents:

```sh
ls -lh tds/tasks/10-cross-user-access/outcomes/10.1
git status --short
```

Keep the short introduction and complete on-screen process within 15:00–45:59. Narrate what, where, and why; keep task content visible and do not show AI interaction during the recording.
