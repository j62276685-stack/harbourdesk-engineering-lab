# 02.2 — Enforce and verify expiry in one checkout path

**Role:** Backend software engineer

**Purpose:** Prevent payment attempts after an order reservation expires.

**Stakeholder:** Checkout product owner and QA engineer.

## Task description

I am investigating the checkout path that allows customers to pay after an order expires. My goal is to provide the checkout team with a verified repair that enforces the server deadline and disables the payment option at the correct time.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `expiry-fix.patch`
- `expiry-checks.md`
- `rejected-order-observation.csv`

## Quality checks

- [ ] One second before is allowed; equality and one second after are rejected.
- [ ] Expired UI actions are unavailable and change at the visible deadline.
- [ ] Rejected API actions leave persisted state unchanged.
- [ ] One equivalent offset timestamp and a normal active order are checked.

**Apps:** Visual Studio Code, Firefox, DB Browser for SQLite.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

**Starting dependency:** [02.1](../02.1/GOAL.md) is optional context; all time fixtures and the contract are supplied.

## Workflow

1. Edit the bounded eligibility/UI behavior in VS Code.
2. Use Firefox to verify action state and a direct request; run a focused boundary test through the task menu.
3. Use DB Browser to confirm rejected requests did not change status/version, then export the patch and check results.

## Recording script

Open the [Task 02 workspace](../../workspaces/02-expired-action.code-workspace) in VS Code. Run commands from its Application terminal; keep that terminal open. Follow the steps in order. Inputs and source: [task brief](../../tasks/02-expired-action/BRIEF.md), [expiry-cases.json](../../tasks/02-expired-action/inputs/expiry-cases.json), [orders.py](../../../app/orders.py), [clock.py](../../../app/clock.py), [app.js](../../../web/app.js).

1. **Set up the session and output folder.** Copy the report template only if a report does not already exist.

```sh
./tds/lab start 02 --session 02.2
mkdir -p tds/tasks/02-expired-action/outcomes/02.2
cp -n tds/docs/REPORT-TEMPLATE.md tds/tasks/02-expired-action/outcomes/02.2/report.md
git status --short
```

2. **Reproduce and capture the baseline.** Capture the three fixture rows and run the disposable probe before editing. In Firefox confirm which pay controls and requests currently disagree with the deadline.

For browser work, start the app in a second terminal with the command below. Open http://localhost:8010 in Firefox; use the example Ada or Ben account and the displayed practice password. Keep the server terminal open and stop it with Control-C when finished.

```sh
./tds/lab serve
```

Run the baseline commands in the Application terminal:

```sh
./tds/lab probe 2
```

3. **Investigate and create the deliverable.** Make app/orders.py reject payment when server time is at or after expires_at, using timezone-aware comparison. In web/app.js make the pay control change at the visible deadline, while leaving the server as the authority. Add before/equal/after and offset-timestamp tests.

4. **Verify the result.** Rerun the probe and tests. In Firefox check the boundary and a normal active order; in DB Browser confirm rejected requests leave status and version unchanged.

Run the verification commands:

```sh
./tds/lab probe 2
./tds/lab test
./tds/lab sql 'SELECT id,status,version FROM orders WHERE id IN ("ord_expired","ord_boundary","ord_before") ORDER BY id'
```

Before committing this session’s code, export the reviewed change as the required patch:

```sh
git add -N -- tests
git diff HEAD --binary -- app/orders.py app/clock.py web/app.js tests > tds/tasks/02-expired-action/outcomes/02.2/expiry-fix.patch
```

5. **Save and review the handoff.** Finish `report.md` in `tds/tasks/02-expired-action/outcomes/02.2/`. Save or export `expiry-checks.md`, `rejected-order-observation.csv` to the same folder using the named apps. Reopen every output, check the quality boxes above, and confirm the folder contents:

```sh
ls -lh tds/tasks/02-expired-action/outcomes/02.2
git status --short
```

Keep the short introduction and complete on-screen process within 15:00–45:59. Narrate what, where, and why; keep task content visible and do not show AI interaction during the recording.
