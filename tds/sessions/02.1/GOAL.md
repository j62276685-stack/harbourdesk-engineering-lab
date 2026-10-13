# 02.1 — Audit expired-payment behavior at the boundary

**Role:** Backend software engineer

**Purpose:** Prevent payment attempts after an order reservation expires.

**Stakeholder:** Checkout product owner and QA engineer.

## Task description

I am investigating a report that expired orders still show a payment option and accept payment requests. My goal is to provide the checkout product owner and QA engineer with an evidence matrix showing the interface, API and database behavior at the expiry boundary.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `expiry-evidence.csv`
- `expiry-defect.md`
- `expiry-interface.png`

## Quality checks

- [ ] The three time cases are controlled explicitly.
- [ ] UI and server outcomes are recorded separately.
- [ ] Before/after persisted values support the mutation claim.
- [ ] The defect note specifies rejection at equality and legitimate unexpired behavior.

**Apps:** Firefox, Visual Studio Code, DB Browser for SQLite.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

## Workflow

1. Inspect the three order fixtures and server clock in DB Browser and the app.
2. Observe browser requests and the source predicate while comparing before/exactly-at/after expiry.
3. Record the outcome, before/after status and version, and exact acceptance boundary.

## Recording script

Open the [Task 02 workspace](../../workspaces/02-expired-action.code-workspace) in VS Code. Run commands from its Application terminal; keep that terminal open. Follow the steps in order. Inputs and source: [task brief](../../tasks/02-expired-action/BRIEF.md), [expiry-cases.json](../../tasks/02-expired-action/inputs/expiry-cases.json), [orders.py](../../../app/orders.py), [clock.py](../../../app/clock.py), [app.js](../../../web/app.js).

1. **Set up the session and output folder.** Copy the report template only if a report does not already exist.

```sh
./tds/lab start 02 --session 02.1
mkdir -p tds/tasks/02-expired-action/outcomes/02.1
cp -n tds/docs/REPORT-TEMPLATE.md tds/tasks/02-expired-action/outcomes/02.1/report.md
git status --short
```

2. **Reproduce and capture the baseline.** At the frozen 09:00 UTC clock, compare ord_expired, ord_boundary, and ord_before; they represent after, exactly at, and before expiry. Capture each order status and version before trying the UI and direct API action.

For browser work, start the app in a second terminal with the command below. Open http://localhost:8010 in Firefox; use the example Ada or Ben account and the displayed practice password. Keep the server terminal open and stop it with Control-C when finished.

```sh
./tds/lab serve
```

Run the baseline commands in the Application terminal:

```sh
./tds/lab probe 2
./tds/lab sql 'SELECT id,status,expires_at,version FROM orders WHERE id IN ("ord_expired","ord_boundary","ord_before") ORDER BY id'
```

3. **Investigate and create the deliverable.** In Firefox inspect the visible pay control and its Network request for each order. In VS Code compare app/orders.py eligibility with app/clock.py and the UI countdown in web/app.js. Record UI, HTTP, and database outcomes in separate CSV columns.

4. **Verify the result.** Confirm that equality is a rejection boundary and that refused actions do not change status or version. Save the Firefox evidence and defect note.

5. **Save and review the handoff.** Finish `report.md` in `tds/tasks/02-expired-action/outcomes/02.1/`. Save or export `expiry-evidence.csv`, `expiry-defect.md`, `expiry-interface.png` to the same folder using the named apps. Reopen every output, check the quality boxes above, and confirm the folder contents:

```sh
ls -lh tds/tasks/02-expired-action/outcomes/02.1
git status --short
```

Keep the short introduction and complete on-screen process within 15:00–45:59. Narrate what, where, and why; keep task content visible and do not show AI interaction during the recording.
