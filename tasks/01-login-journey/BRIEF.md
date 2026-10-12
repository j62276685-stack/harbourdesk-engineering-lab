# Task 01: Diagnose a login failure limited to one browser journey

## Error or request

I am investigating a customer report that password sign-in works but signing in through our in-house Identity provider fails. My goal is to provide the engineering lead with an evidence-based diagnosis and a verified repair that restores the customer journey while retaining state validation.

## Relevant files

[app/auth.py](../../app/auth.py); [app/http.py](../../app/http.py); [web/index.html](../../web/index.html).

- [support-report.txt](inputs/support-report.txt)

## Reproduce or investigate

Open the [Task 01 workspace](../../workspaces/01-login-journey.code-workspace). It uses the shared application and database. Read the inputs above. Run `./lab serve` for browser work or `./lab test` for tests.

Run `./lab serve`. In a fresh browser open `http://localhost:8010`, verify password login, then clear localhost cookies and choose Harbour Identity. On the provider page at `127.0.0.1:8011`, click Continue as Ada. Preserve the network log and compare the successful and failing flows. `./lab probe 01` checks only the service callback.

## Completion criteria

1. Both password and provider browser journeys succeed using the original two hostnames.
2. Missing, incorrect and replayed state still fail; another session cannot use the state.
3. Record relevant request/response headers, redirect order and the observed browser/version. Explain which observation connects the failure to your fix.
4. Keep session cookies HttpOnly and retain state validation. Document how the local HTTP configuration relates to a hypothetical HTTPS deployment.

## Deliverable

A patch, browser reproduction record, callback boundary tests, and a short diagnosis. Do not replace the provider flow with password login or delete state checks.

## Task sessions

Choose a session below for its scope, apps, outputs and checks.

- [01.1 — Diagnose the provider sign-in journey](../../sessions/01.1/GOAL.md)
- [01.2 — Repair and verify the bounded sign-in failure](../../sessions/01.2/GOAL.md)
