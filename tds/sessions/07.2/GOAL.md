# 07.2 — Repair the atomic webhook effect boundary

**Role:** Backend payments engineer

**Purpose:** Keep duplicate deliveries from creating duplicate business effects.

**Stakeholder:** Payments engineering lead and operations.

## Task description

I am investigating the webhook processing path that can apply a successful payment event more than once. My goal is to provide the payments engineering lead with a verified atomic repair that preserves one payment effect under sequential and concurrent delivery.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `webhook-atomicity.patch`
- `webhook-effect-checks.md`
- `webhook-durable-evidence.csv`

## Quality checks

- [ ] An identical event produces one business effect under sequential/concurrent delivery.
- [ ] All deliveries acknowledge once the event is durably applied.
- [ ] Distinct orders/events still apply independently.
- [ ] Rejected input creates no success receipt/effect.

**Apps:** Visual Studio Code, DB Browser for SQLite, GitHub Desktop.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

**Starting dependency:** [07.1](../07.1/GOAL.md) is useful context; the supplied delivery contract defines the invariant independently.

## Workflow

1. Edit the handler/schema narrowly in VS Code using the stated invariant.
2. Run focused replay/concurrency checks; use DB Browser to compare committed side-effect rows.
3. Review the diff in GitHub Desktop, record the validation limits and export the patch.

## Recording script

Open the [Task 07 workspace](../../workspaces/07-duplicate-webhook.code-workspace) in VS Code. Run commands from its Application terminal; keep that terminal open. Follow the steps in order. Inputs and source: [task brief](../../tasks/07-duplicate-webhook/BRIEF.md), [delivery-contract.md](../../tasks/07-duplicate-webhook/inputs/delivery-contract.md), [event.json](../../tasks/07-duplicate-webhook/inputs/event.json), [payments.py](../../../app/payments.py), [schema.sql](../../../app/schema.sql), [db.py](../../../app/db.py), [http.py](../../../app/http.py).

1. **Set up the session and output folder.** Copy the report template only if a report does not already exist.

```sh
./tds/lab start 07 --session 07.2
mkdir -p tds/tasks/07-duplicate-webhook/outcomes/07.2
cp -n tds/docs/REPORT-TEMPLATE.md tds/tasks/07-duplicate-webhook/outcomes/07.2/report.md
git status --short
```

2. **Reproduce and capture the baseline.** Capture the original race and read the delivery contract. Keep the probe database separate from the shared runtime database.

Run the baseline commands in the Application terminal:

```sh
./tds/lab record probe
```

3. **Investigate and create the deliverable.** In app/payments.py make duplicate detection, receipt claim, payment insert, order update, and outbox insert one atomic transaction. Preserve HTTP-edge amount/currency validation and acknowledgements for already applied events; add deterministic concurrent and sequential tests.

4. **Verify the result.** Repeat the race capture and tests. In DB Browser open the printed evidence folder’s probe/observed.sqlite3 and verify one payment, receipt, outbox row, and version increment; test a distinct event and a rejected payload, then review the patch.

Run the verification commands:

```sh
./tds/lab record probe
./tds/lab test
```

Before committing this session’s code, export the reviewed change as the required patch:

```sh
git add -N -- tests
git diff HEAD --binary -- app/payments.py app/schema.sql tests > tds/tasks/07-duplicate-webhook/outcomes/07.2/webhook-atomicity.patch
```

5. **Save and review the handoff.** Finish `report.md` in `tds/tasks/07-duplicate-webhook/outcomes/07.2/`. Save or export `webhook-effect-checks.md`, `webhook-durable-evidence.csv` to the same folder using the named apps. Reopen every output, check the quality boxes above, and confirm the folder contents:

```sh
ls -lh tds/tasks/07-duplicate-webhook/outcomes/07.2
git status --short
```

Keep the short introduction and complete on-screen process within 15:00–45:59. Narrate what, where, and why; keep task content visible and do not show AI interaction during the recording.
