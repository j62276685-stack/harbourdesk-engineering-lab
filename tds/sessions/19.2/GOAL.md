# 19.2 — Exercise recovery and publish the runbook drill verdict

**Role:** Site reliability engineer

**Purpose:** Make a recurring notification failure diagnosable and recoverable.

**Stakeholder:** On-call engineer.

## Task description

I am investigating whether the notification runbook handles transient outages, sustained failures and recovery safely. My goal is to provide the on-call engineer with a tested drill verdict showing queue progress, sent-message protection and clear escalation conditions.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `notification-drill.ods`
- `notification-drill-verdict.pdf`
- `notification-drill-evidence.json`

## Quality checks

- [ ] Transient failure, sustained failure and recovery are observed.
- [ ] Job IDs, attempts, payload and status are compared before/after.
- [ ] An already-sent job is not resent by recovery.
- [ ] The updated handoff names a stop/escalation condition and a real queue-progress success check.

**Apps:** Visual Studio Code, DB Browser for SQLite, LibreOffice.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

**Starting dependency:** Use your frozen [19.1](../19.1/GOAL.md) runbook, or label the supplied operations contract as the draft runbook being validated.

## Workflow

1. Use DB Browser’s row editor to select the local worker failure mode and inspect job payload/status.
2. Use VS Code’s task menu to tick the worker and capture the failure/recovery sequence.
3. Update the frozen runbook and drill table in LibreOffice, including the sustained-failure stopping decision.

## Recording script

Open the [Task 19 workspace](../../workspaces/19-operational-runbook.code-workspace) in VS Code. Run commands from its Application terminal; keep that terminal open. Follow the steps in order. Inputs and source: [task brief](../../tasks/19-operational-runbook/BRIEF.md), [alert.txt](../../tasks/19-operational-runbook/inputs/alert.txt), [operations-contract.md](../../tasks/19-operational-runbook/inputs/operations-contract.md), [worker.py](../../../app/worker.py), [schema.sql](../../../app/schema.sql).

1. **Set up the session and output folder.** Copy the report template only if a report does not already exist.

```sh
./tds/lab start 19 --session 19.2
mkdir -p tds/tasks/19-operational-runbook/outcomes/19.2
cp -n tds/docs/REPORT-TEMPLATE.md tds/tasks/19-operational-runbook/outcomes/19.2/report.md
git status --short
```

2. **Reproduce and capture the baseline.** Capture initial worker status and job IDs. In DB Browser inspect worker_state and notification_outbox; use the CLI controls rather than changing payloads by hand.

Run the baseline commands in the Application terminal:

```sh
./tds/lab worker status
./tds/lab worker control --mode transient --failures 2
./tds/lab worker tick
./tds/lab worker tick
./tds/lab worker control --mode healthy
./tds/lab worker tick
./tds/lab worker status
```

3. **Investigate and create the deliverable.** Set transient mode for two failures, tick and record each result, then restore healthy and tick again. Try permanent mode only with an explicit stop count; check an already-sent job is not resent. Fill the Calc drill table.

4. **Verify the result.** Capture final status and compare attempts, status, and last_error. Export a verdict that states the sandbox sender cannot prove downstream email delivery.

Run the verification commands:

```sh
./tds/lab record worker-status
```

5. **Save and review the handoff.** Finish `report.md` in `tds/tasks/19-operational-runbook/outcomes/19.2/`. Save or export `notification-drill.ods`, `notification-drill-verdict.pdf`, `notification-drill-evidence.json` to the same folder using the named apps. Reopen every output, check the quality boxes above, and confirm the folder contents:

```sh
ls -lh tds/tasks/19-operational-runbook/outcomes/19.2
git status --short
```

Keep the short introduction and complete on-screen process within 15:00–45:59. Narrate what, where, and why; keep task content visible and do not show AI interaction during the recording.
