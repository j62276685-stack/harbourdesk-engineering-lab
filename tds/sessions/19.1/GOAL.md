# 19.1 — Write a runbook for the bounded notification outage

**Role:** Site reliability engineer

**Purpose:** Make a recurring notification failure diagnosable and recoverable.

**Stakeholder:** On-call engineer.

## Task description

I am investigating a recurring notification outage that leaves messages pending in the queue. My goal is to provide the on-call engineer with a practical diagnosis and recovery runbook that defines safe actions, stopping conditions and checks for restored queue progress.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `notification-runbook.pdf`
- `notification-runbook.odt`
- `runbook-command-checks.md`

## Quality checks

- [ ] Diagnosis distinguishes empty queue, upstream outage and suspect payload.
- [ ] Recovery preserves pending payloads and does not resend sent jobs.
- [ ] Commands, expected interpretation, stop/escalation and success checks are executable.
- [ ] The sandbox sent status is not claimed to prove real email delivery.

**Apps:** Visual Studio Code, DB Browser for SQLite, LibreOffice.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

## Workflow

1. Inspect alert/source/controls in VS Code and queue/state fields in DB Browser.
2. In LibreOffice draft diagnosis steps, safe recovery controls and interpretation of each result.
3. Check the runbook against a short healthy/transient observation and export the document for the on-call engineer.

## Recording script

Open the [Task 19 workspace](../../workspaces/19-operational-runbook.code-workspace) in VS Code. Run commands from its Application terminal; keep that terminal open. Follow the steps in order. Inputs and source: [task brief](../../tasks/19-operational-runbook/BRIEF.md), [alert.txt](../../tasks/19-operational-runbook/inputs/alert.txt), [operations-contract.md](../../tasks/19-operational-runbook/inputs/operations-contract.md), [worker.py](../../../app/worker.py), [schema.sql](../../../app/schema.sql).

1. **Set up the session and output folder.** Copy the report template only if a report does not already exist.

```sh
./tds/lab start 19 --session 19.1
mkdir -p tds/tasks/19-operational-runbook/outcomes/19.1
cp -n tds/docs/REPORT-TEMPLATE.md tds/tasks/19-operational-runbook/outcomes/19.1/report.md
git status --short
```

2. **Reproduce and capture the baseline.** Read the alert, operations contract, app/worker.py, and current queue rows. Run status before changing worker mode.

Run the baseline commands in the Application terminal:

```sh
./tds/lab worker status
./tds/lab sql 'SELECT id,status,attempts,last_error FROM notification_outbox ORDER BY id'
./tds/lab sql 'SELECT mode,failure_remaining FROM worker_state WHERE id=1'
```

3. **Investigate and create the deliverable.** In LibreOffice draft an on-call sequence: check queue, identify transient versus sustained failure, cap attempted recovery, restore healthy mode, tick one job, and verify no sent job is replayed. Include exact interpretation of each command result.

4. **Verify the result.** Run a short disposable probe or controlled healthy/transient observation. Export the ODT and PDF and make the command-check note explicit.

5. **Save and review the handoff.** Finish `report.md` in `tds/tasks/19-operational-runbook/outcomes/19.1/`. Save or export `notification-runbook.pdf`, `notification-runbook.odt`, `runbook-command-checks.md` to the same folder using the named apps. Reopen every output, check the quality boxes above, and confirm the folder contents:

```sh
ls -lh tds/tasks/19-operational-runbook/outcomes/19.1
git status --short
```

Keep the short introduction and complete on-screen process within 15:00–45:59. Narrate what, where, and why; keep task content visible and do not show AI interaction during the recording.
