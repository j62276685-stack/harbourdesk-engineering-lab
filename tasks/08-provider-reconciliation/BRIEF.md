# Task 08: Handle a provider response that contradicts local state

## Error or request

A delayed success arrives for a cancelled order, and an older failure response arrives for a locally paid order. Define a reconciliation rule that preserves evidence and avoids accidental fulfilment.

## Relevant files

[app/payments.py](../../app/payments.py); [app/schema.sql](../../app/schema.sql); [inputs/observations.json](inputs/observations.json); [policy-context.md](inputs/policy-context.md).

- [observations.json](inputs/observations.json)
- [policy-context.md](inputs/policy-context.md)

## Reproduce or investigate

From the project root, run `./lab start 08`. Open the printed folder. Run `./lab serve` for browser work or `./lab test` for tests. Inputs are copied to `evidence/inputs/`.

Run `./lab probe 08`. Review each supplied provider observation and the local seed. Design and document the reconciliation decision before changing code. You may add an audit table and distinguish payment state from order fulfilment state.

## Completion criteria

1. An older failure cannot downgrade an already paid order.
2. Success for a cancelled order is recorded for review/refund reconciliation without reopening or fulfilling it.
3. Pending/failed observations, invalid amount/currency and unknown orders have explicit outcomes and preserve evidence.
4. Repeated identical observations do not create duplicate financial/audit effects; stable observation_id is supplied in the fixture.
5. Test your documented policy with normal success, stale evidence and conflicting evidence. Make no claim that the provider or local DB is always authoritative for every field.

## Deliverable

A decision table, reconciliation implementation, audit evidence and tests. More than one state model is acceptable if the policy is explicit and meets the safeguards.

## Task sessions

Choose a session below for its scope, apps, outputs and checks.

- [08.1 — Decide how two contradictory provider observations should be reconciled](../../sessions/08.1/GOAL.md)
- [08.2 — Implement the two-case reconciliation policy with an audit trail](../../sessions/08.2/GOAL.md)
