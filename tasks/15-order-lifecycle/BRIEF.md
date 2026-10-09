# Task 15: Model an order lifecycle

## Error or request

An order can currently move between states too freely. Model allowed transitions and reject invalid ones without changing order history on rejection.

## Relevant files

[app/orders.py](../../app/orders.py); [app/schema.sql](../../app/schema.sql); [inputs/lifecycle-contract.md](inputs/lifecycle-contract.md); [examples.json](inputs/examples.json).

- [examples.json](inputs/examples.json)
- [lifecycle-contract.md](inputs/lifecycle-contract.md)

## Reproduce or investigate

From the project root, run `./lab start 15`. Open the printed folder. Run `./lab serve` for browser work or `./lab test` for tests. Inputs are copied to `evidence/inputs/`.

Run `./lab probe 15`. Use the lifecycle contract to create a state diagram or transition table, then implement it at the service boundary and verify through HTTP.

## Completion criteria

1. Implement all allowed transitions in the supplied table and reject every other pair; terminal states have no outgoing transition.
2. Same-state requests are idempotent and do not change version.
3. Unknown target state yields 400, forbidden known transition yields 409, unowned/unknown order follows the 404 contract.
4. An accepted new state increments version once; rejection leaves it unchanged.
5. Test all pairs of the seven states, a legitimate customer flow, a cancelled terminal state and ownership.

## Deliverable

State table/diagram, implementation and transition-matrix tests. Provider conflict reconciliation is a separate task.

## Task sessions

Choose a session below for its scope, apps, outputs and checks.

- [15.1 — Model the seven-state order lifecycle for QA](../../sessions/15.1/GOAL.md)
- [15.2 — Enforce and verify the bounded lifecycle transition contract](../../sessions/15.2/GOAL.md)
