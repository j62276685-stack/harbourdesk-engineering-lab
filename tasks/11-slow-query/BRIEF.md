# Task 11: Optimize one slow database query

## Error or request

The recent-paid-orders dashboard grows slow as orders accumulate. Measure the baseline, make a justified query/index change and show equivalent results.

## Relevant files

[app/reporting.py](../../app/reporting.py); [app/schema.sql](../../app/schema.sql); [inputs/report-contract.md](inputs/report-contract.md).

- [report-contract.md](inputs/report-contract.md)

## Reproduce or investigate

From the project root, run `./lab start 11`. Open the printed folder. Run `./lab serve` for browser work or `./lab test` for tests. Inputs are copied to `evidence/inputs/`.

Run `./lab seed-large --rows 150000` once in this workspace, then `./lab benchmark --runs 9`. Save the digest, plan and timing samples. Compare on the same DB/hardware, warm-up and workload after your change.

## Completion criteria

1. Return identical ordered rows and the same result digest for the supplied workload, including ties.
2. Record before/after query plans, row counts, median latency and at least nine samples each.
3. Show a material improvement (target at least 2× on the seeded workload), or explain measurement noise and provide plan/work evidence if hardware obscures timing.
4. Justify index column order or query changes and mention write/storage cost; check another user/status combination and an empty result.
5. Show how the schema change applies to both a new DB and an existing DB.

## Deliverable

Query/index patch, repeatable migration or SQL, measurement report and equivalence checks. Do not reduce rows, change filters or hardcode results.

## Task sessions

Choose a session below for its scope, apps, outputs and checks.

- [11.1 — Measure the bounded report query baseline](../../sessions/11.1/GOAL.md)
- [11.2 — Optimize one report query and prove result equivalence](../../sessions/11.2/GOAL.md)
