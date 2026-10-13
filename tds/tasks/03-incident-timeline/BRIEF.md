# Task 03: Reconstruct an incident from scattered evidence

## Error or request

I am investigating a morning incident in which customers received duplicate receipts. My goal is to provide the incident commander and support lead with a source-linked timeline and a clear explanation of what the evidence establishes and what remains uncertain.

## Relevant files

[inputs/proxy.log](inputs/proxy.log); [service.jsonl](inputs/service.jsonl); [provider.csv](inputs/provider.csv); [deploy.txt](inputs/deploy.txt); [metrics.csv](inputs/metrics.csv); [support.txt](inputs/support.txt); [source-notes.md](inputs/source-notes.md).

- [deploy.txt](inputs/deploy.txt)
- [metrics.csv](inputs/metrics.csv)
- [provider.csv](inputs/provider.csv)
- [proxy.log](inputs/proxy.log)
- [service.jsonl](inputs/service.jsonl)
- [source-notes.md](inputs/source-notes.md)
- [support.txt](inputs/support.txt)

## Reproduce or investigate

Open the [Task 03 workspace](../../workspaces/03-incident-timeline.code-workspace). It uses the shared application and database. Read the inputs above. Run `./tds/lab serve` for browser work or `./tds/lab test` for tests.

Read all source files. Normalize times to UTC while retaining original timestamps and source locations. Metrics are minute buckets, not individual events. The source notes describe clock differences and missing intervals.

## Completion criteria

1. Provide a ordered timeline with source filename and line or row for each material event.
2. Separate direct observations, inferences, hypotheses and unknowns.
3. Bound the incident window, account for duplicate identifiers, and explain which deployment facts establish correlation only.
4. Explain what cannot be counted or attributed from these fragments and request a concrete missing observation.

## Deliverable

outcomes/timeline.md, an evidence table, likely explanation(s) with confidence, and an investigation follow-up. No code change is required.

## Task sessions

Choose a session below for its scope, apps, outputs and checks.

- [03.1 — Reconstruct one incident and its evidence limits](../../sessions/03.1/GOAL.md)
