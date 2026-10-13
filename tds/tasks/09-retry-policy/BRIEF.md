# Task 09: Design a retry policy for one integration

## Error or request

I am investigating payment retry behavior that can repeat permanent failures or increase duplicate-charge risk. My goal is to provide the integration reviewer with a verified policy that preserves request identity and bounds attempts, waits and total duration.

## Relevant files

[app/retries.py](../../../app/retries.py); [app/provider.py](../../../app/provider.py); [inputs/retry-contract.md](inputs/retry-contract.md); [provider-scripts.json](inputs/provider-scripts.json).

- [provider-scripts.json](inputs/provider-scripts.json)
- [retry-contract.md](inputs/retry-contract.md)

## Reproduce or investigate

Open the [Task 09 workspace](../../workspaces/09-retry-policy.code-workspace). It uses the shared application and database. Read the inputs above. Run `./tds/lab serve` for browser work or `./tds/lab test` for tests.

Run `./tds/lab probe 09`. Use `ScriptedProvider.calls`, an injected sleep recorder, and its optional on_call callback for simulated request duration. Inject a monotonic clock if needed; do not use real waiting in tests.

## Completion criteria

1. Retry only transport timeout 0, 408, 429, 500, 502, 503, 504. Other client/decline/auth responses stop immediately.
2. At most three calls including the first; delays are 1s then 2s unless a valid 429 Retry-After asks for a longer delay, capped at 4s.
3. An eight-second total budget includes request durations and waits; do not start another call once exhausted or when its wait would exceed the budget.
4. All attempts for one operation use the same nonempty idempotency key. Do not retry a charge without a stable key.
5. Cover eventual success, immediate permanent failure, exhausted attempts, deadline exhaustion and malformed Retry-After. State the final outcome and ambiguity of a timed-out charge.

## Deliverable

Decision table, bounded implementation and fake-clock tests. You may extend the function with keyword-only clock/budget parameters while preserving ordinary callers.

## Task sessions

Choose a session below for its scope, apps, outputs and checks.

- [09.1 — Design the bounded charge-retry decision table](../../sessions/09.1/GOAL.md)
- [09.2 — Implement retry eligibility and stable request identity](../../sessions/09.2/GOAL.md)
- [09.3 — Integrate deadline and Retry-After handling](../../sessions/09.3/GOAL.md)
