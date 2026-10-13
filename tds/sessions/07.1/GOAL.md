# 07.1 — Investigate a deterministic duplicate-delivery race

**Role:** Backend payments engineer

**Purpose:** Keep duplicate deliveries from creating duplicate business effects.

**Stakeholder:** Payments engineering lead and operations.

## Task description

I am investigating whether simultaneous deliveries of the same payment event create duplicate business effects. My goal is to provide the payments engineering lead with reproducible race evidence and a clear account of the transaction boundary needed to prevent duplication.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `webhook-invariants.ods`
- `webhook-race-review.pdf`
- `webhook-race-observation.json`

## Quality checks

- [ ] The scheduling is deterministic rather than a sleep guess.
- [ ] Payment, notification, receipt and order-version effects are all accounted for.
- [ ] The recommendation explains the durable business boundary.
- [ ] Sequential replay is compared with concurrent delivery.

**Apps:** Visual Studio Code, DB Browser for SQLite, LibreOffice.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

## Workflow

1. Run the race observation from VS Code and inspect the handler’s durable steps.
2. Use DB Browser to inspect payments, receipt, version and outbox counts in a captured disposable copy.
3. Build the effect/invariant table and write a concise transaction-boundary recommendation in LibreOffice.

## Recording script

Open the [Task 07 workspace](../../workspaces/07-duplicate-webhook.code-workspace) in VS Code. Run commands from its Application terminal; keep that terminal open. Follow the steps in order. Inputs and source: [task brief](../../tasks/07-duplicate-webhook/BRIEF.md), [delivery-contract.md](../../tasks/07-duplicate-webhook/inputs/delivery-contract.md), [event.json](../../tasks/07-duplicate-webhook/inputs/event.json), [payments.py](../../../app/payments.py), [schema.sql](../../../app/schema.sql), [db.py](../../../app/db.py), [http.py](../../../app/http.py).

1. **Set up the session and output folder.** Copy the report template only if a report does not already exist.

```sh
./tds/lab start 07 --session 07.1
mkdir -p tds/tasks/07-duplicate-webhook/outcomes/07.1
cp -n tds/docs/REPORT-TEMPLATE.md tds/tasks/07-duplicate-webhook/outcomes/07.1/report.md
git status --short
```

2. **Reproduce and capture the baseline.** Select the session and capture the deterministic race probe; use the printed evidence folder rather than the shared live database for the race rows.

Run the baseline commands in the Application terminal:

```sh
./tds/lab record probe
```

3. **Investigate and create the deliverable.** In VS Code trace the receipt lookup, payment/order/outbox write, and receipt insertion in app/payments.py. In DB Browser open the printed evidence folder’s probe/observed.sqlite3 and count event rows, receipts, notifications, and order version. Copy probe/observation.json from that folder to webhook-race-observation.json in this session’s outcome folder. Contrast concurrent delivery with sequential replay.

4. **Verify the result.** Use Calc to state the expected one-effect invariant and the observed violation. Explain why the lookup and all durable writes need one transaction boundary.

5. **Save and review the handoff.** Finish `report.md` in `tds/tasks/07-duplicate-webhook/outcomes/07.1/`. Save or export `webhook-invariants.ods`, `webhook-race-review.pdf`, `webhook-race-observation.json` to the same folder using the named apps. Reopen every output, check the quality boxes above, and confirm the folder contents:

```sh
ls -lh tds/tasks/07-duplicate-webhook/outcomes/07.1
git status --short
```

Keep the short introduction and complete on-screen process within 15:00–45:59. Narrate what, where, and why; keep task content visible and do not show AI interaction during the recording.
