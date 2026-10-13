# Task 07: Implement duplicate-safe webhook handling

## Error or request

I am investigating whether repeated, concurrent or interrupted payment-event deliveries create duplicate business effects. My goal is to provide the payments engineering lead with a verified processing boundary that applies each successful event once and recovers safely.

## Relevant files

[app/payments.py](../../../app/payments.py); [app/schema.sql](../../../app/schema.sql); [app/db.py](../../../app/db.py); [app/http.py](../../../app/http.py); [inputs/event.json](inputs/event.json); [delivery-contract.md](inputs/delivery-contract.md).

- [delivery-contract.md](inputs/delivery-contract.md)
- [event.json](inputs/event.json)

## Reproduce or investigate

Open the [Task 07 workspace](../../workspaces/07-duplicate-webhook.code-workspace). It uses the shared application and database. Read the inputs above. Run `./tds/lab serve` for browser work or `./tds/lab test` for tests.

Run `./tds/lab probe 07`. It schedules two handlers at the same lookup barrier on a disposable DB. Repeat a sequential delivery and inspect payments, webhook_receipts, order version and notification_outbox. Add your own deterministic concurrency and failure-injection tests.

## Completion criteria

1. Sequential and concurrent identical events create one payment row, one notification and one accepted order update; all successful deliveries acknowledge safely.
2. A failure between the business write and the receipt acknowledgement can be retried without duplicate effects or lost work.
3. A rejected amount/currency does not create a successful receipt or business side effect.
4. Distinct event IDs for distinct orders each apply once; preserve HTTP input validation and explain the idempotency boundary.
5. Demonstrate transaction rollback and a deterministic race without relying only on sleep.

## Deliverable

Handler/schema changes as needed, concurrency and interruption tests, plus the invariant and transaction rationale. SQLite is the intended sandbox database.

## Task sessions

Choose a session below for its scope, apps, outputs and checks.

- [07.1 — Investigate a deterministic duplicate-delivery race](../../sessions/07.1/GOAL.md)
- [07.2 — Repair the atomic webhook effect boundary](../../sessions/07.2/GOAL.md)
- [07.3 — Audit interrupted-delivery recovery on a candidate handler](../../sessions/07.3/GOAL.md)
