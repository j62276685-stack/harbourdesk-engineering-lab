# Task 06: Investigate a misleading error message

## Error or request

A dependency outage is shown to the customer as an invalid amount. Distinguish local validation failures, declined payments, upstream outages and transport timeouts.

## Relevant files

[app/payments.py](../../app/payments.py); [app/provider.py](../../app/provider.py); [app/http.py](../../app/http.py); [docs/API.md](../../docs/API.md); [inputs/provider-cases.json](inputs/provider-cases.json).

- [provider-cases.json](inputs/provider-cases.json)

## Reproduce or investigate

From the project root, run `./lab start 06`. Open the printed folder. Run `./lab serve` for browser work or `./lab test` for tests. Inputs are copied to `evidence/inputs/`.

Run `./lab probe 06`, then run the additional cases in the supplied JSON through `ScriptedProvider`. Use the classification table in API.md as the public contract.

## Completion criteria

1. Return the documented status, machine code and customer message for each defined failure category.
2. Bad local amounts do not call the provider; check booleans and non-integer values as well as zero/negative amounts.
3. Successful data is preserved. An unexpected upstream response is still a dependency failure.
4. Tests demonstrate that raw upstream diagnostic text is not exposed to the customer.

## Deliverable

Classification patch, tests and a mapping table. Do not introduce retries or actual payment processing.

## Task sessions

Choose a session below for its scope, apps, outputs and checks.

- [06.1 — Specify a customer-safe provider error taxonomy](../../sessions/06.1/GOAL.md)
- [06.2 — Implement and verify one error-classification contract](../../sessions/06.2/GOAL.md)
