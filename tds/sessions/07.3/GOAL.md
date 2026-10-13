# 07.3 — Audit interrupted-delivery recovery on a candidate handler

**Role:** Backend payments engineer

**Purpose:** Keep duplicate deliveries from creating duplicate business effects.

**Stakeholder:** Payments engineering lead and operations.

## Task description

I am investigating whether an interrupted webhook handler can recover safely when the provider redelivers the event. My goal is to provide the payments engineering lead with a failure-injection verdict showing whether durable effects are rolled back or completed without duplication.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `webhook-recovery-cases.ods`
- `webhook-recovery-verdict.pdf`
- `webhook-interruption-evidence.json`

## Quality checks

- [ ] The exact interruption point and retry sequence are documented.
- [ ] Durable rows and order version are compared before/after retry.
- [ ] The verdict is supported whether the candidate passes or fails.
- [ ] No duplicate financial/outbox effect is silently accepted.

**Apps:** Visual Studio Code, DB Browser for SQLite, LibreOffice.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

**Starting dependency:** A frozen candidate handler is required. The original starter is a valid candidate for an audit; a human-created [07.2](../07.2/GOAL.md) patch is another option.

## Workflow

1. Select one interruption point and predict the observable invariants without claiming a remote charge result.
2. Run the controlled interruption/retry check in VS Code and inspect durable records with DB Browser.
3. Complete the recovery test table and export a QA verdict in LibreOffice, including a failure verdict if justified.

## Recording script

Open the [Task 07 workspace](../../workspaces/07-duplicate-webhook.code-workspace) in VS Code. Run commands from its Application terminal; keep that terminal open. Follow the steps in order. Inputs and source: [task brief](../../tasks/07-duplicate-webhook/BRIEF.md), [delivery-contract.md](../../tasks/07-duplicate-webhook/inputs/delivery-contract.md), [event.json](../../tasks/07-duplicate-webhook/inputs/event.json), [payments.py](../../../app/payments.py), [schema.sql](../../../app/schema.sql), [db.py](../../../app/db.py), [http.py](../../../app/http.py).

1. **Set up the session and output folder.** Copy the report template only if a report does not already exist.

```sh
./tds/lab start 07 --session 07.3
mkdir -p tds/tasks/07-duplicate-webhook/outcomes/07.3
cp -n tds/docs/REPORT-TEMPLATE.md tds/tasks/07-duplicate-webhook/outcomes/07.3/report.md
git status --short
```

2. **Reproduce and capture the baseline.** Freeze the candidate handler and choose one interruption point between durable operations. State the predicted row counts before running the test.

Run the baseline commands in the Application terminal:

```sh
./tds/lab record probe
```

3. **Investigate and create the deliverable.** Add a controlled exception at that point in a disposable test, deliver the same event again, and inspect the printed evidence folder’s probe/observed.sqlite3 in DB Browser. In Calc record before-interruption, after-interruption, and after-retry counts for all four business effects.

4. **Verify the result.** Run the test suite and give a pass or fail verdict from the durable rows. Do not infer any real remote charge from this local exercise.

Run the verification commands:

```sh
./tds/lab test
```

5. **Save and review the handoff.** Finish `report.md` in `tds/tasks/07-duplicate-webhook/outcomes/07.3/`. Save or export `webhook-recovery-cases.ods`, `webhook-recovery-verdict.pdf`, `webhook-interruption-evidence.json` to the same folder using the named apps. Reopen every output, check the quality boxes above, and confirm the folder contents:

```sh
ls -lh tds/tasks/07-duplicate-webhook/outcomes/07.3
git status --short
```

Keep the short introduction and complete on-screen process within 15:00–45:59. Narrate what, where, and why; keep task content visible and do not show AI interaction during the recording.
