# Task 02: Fix an expired action that remains available

## Error or request

I am investigating a report that expired orders still display a payment option and accept payment requests. My goal is to provide the checkout team with a verified repair that enforces expiry in both the interface and the service.

## Relevant files

[app/orders.py](../../../app/orders.py); [app/http.py](../../../app/http.py); [app/clock.py](../../../app/clock.py); [web/app.js](../../../web/app.js).

- [expiry-cases.json](inputs/expiry-cases.json)

## Reproduce or investigate

Open the [Task 02 workspace](../../workspaces/02-expired-action.code-workspace). It uses the shared application and database. Read the inputs above. Run `./tds/lab serve` for browser work or `./tds/lab test` for tests.

Run `./tds/lab probe 02`. Use Ada in `./tds/lab serve` and compare `ord_expired`, `ord_boundary` and `ord_before`. Inspect the HTTP response and order version before/after an attempt. Use explicit `LAB_NOW` values or an injected test clock.

## Completion criteria

1. One second before expiry is allowed, exactly at expiry and one second after are rejected.
2. A direct API request rejects an expired order independently of the button; choose a clear 409 domain error.
3. Rejected requests leave status, version and financial rows unchanged.
4. The UI disables or removes the action for expired and non-payable orders and updates as the visible countdown crosses expiry.
5. Check equivalent offset timestamps and an ordinary unexpired order.

## Deliverable

A patch, UI evidence and deterministic server/API boundary tests. Scope is expiry; general payment-provider integration is excluded.

## Task sessions

Choose a session below for its scope, apps, outputs and checks.

- [02.1 — Audit expired-payment behavior at the boundary](../../sessions/02.1/GOAL.md)
- [02.2 — Enforce and verify expiry in one checkout path](../../sessions/02.2/GOAL.md)
