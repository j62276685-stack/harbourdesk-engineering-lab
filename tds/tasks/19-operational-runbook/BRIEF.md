# Task 19: Create an operational runbook for a recurring failure

## Error or request

I am investigating recurring notification failures that leave messages pending during provider outages. My goal is to provide the on-call engineer with a tested diagnosis and recovery runbook that restores queue progress without resending completed messages.

## Relevant files

[app/worker.py](../../../app/worker.py); [app/schema.sql](../../../app/schema.sql); [inputs/alert.txt](inputs/alert.txt); [operations-contract.md](inputs/operations-contract.md).

- [alert.txt](inputs/alert.txt)
- [operations-contract.md](inputs/operations-contract.md)

## Reproduce or investigate

Open the [Task 19 workspace](../../workspaces/19-operational-runbook.code-workspace). It uses the shared application and database. Read the inputs above. Run `./tds/lab serve` for browser work or `./tds/lab test` for tests.

Run `./tds/lab worker status`; then `./tds/lab worker control --mode transient --failures 3` and tick repeatedly. Use permanent and healthy modes for additional drills. The supplied alert is historical; current status is the authoritative drill observation.

## Completion criteria

1. Describe symptoms, bounded diagnosis and checks to distinguish provider outage from an empty queue or a malformed job.
2. Provide executable commands for diagnosis, controlled recovery and verification with expected interpretation.
3. Preserve pending payloads and attempts; do not resend sent messages or wipe the queue as recovery.
4. Exercise transient failure, sustained failure, recovery and an already-sent job; show before/after job IDs/statuses.
5. Define escalation/stopping conditions and a success check covering queue progress and duplicate prevention. Record limitations of the sandbox sender.

## Deliverable

outcomes/runbook.md and a drill transcript. Patch only if necessary to make a documented recovery step safe; explain any change.

## Task sessions

Choose a session below for its scope, apps, outputs and checks.

- [19.1 — Write a runbook for the bounded notification outage](../../sessions/19.1/GOAL.md)
- [19.2 — Exercise recovery and publish the runbook drill verdict](../../sessions/19.2/GOAL.md)
