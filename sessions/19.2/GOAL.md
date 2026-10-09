# 19.2 — Exercise recovery and publish the runbook drill verdict

**Role:** Site reliability engineer

**Purpose:** Make a recurring notification failure diagnosable and recoverable.

**Stakeholder:** On-call engineer.

## Task description

Run a bounded transient/sustained outage drill against the local queue, test recovery and sent-job safety, and publish a verified on-call handoff.

## Final deliverable

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
