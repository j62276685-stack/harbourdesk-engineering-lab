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
