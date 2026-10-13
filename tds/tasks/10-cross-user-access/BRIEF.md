# Task 10: Find a cross-user authorization flaw

## Error or request

I am investigating whether an authenticated customer can access another customer’s order. My goal is to provide the security reviewer and account-service owner with evidence of the access boundary and a verified repair that preserves legitimate access.

## Relevant files

[app/orders.py](../../../app/orders.py); [app/http.py](../../../app/http.py); [inputs/access-matrix.csv](inputs/access-matrix.csv).

- [access-matrix.csv](inputs/access-matrix.csv)

## Reproduce or investigate

Open the [Task 10 workspace](../../workspaces/10-cross-user-access.code-workspace). It uses the shared application and database. Read the inputs above. Run `./tds/lab serve` for browser work or `./tds/lab test` for tests.

Run `./tds/lab probe 10`. Use authenticated requests to Ben’s `ord_ben` as Ada and Ben. Investigate read, pay and transition routes separately on fresh seed data so one operation does not conceal another.

## Completion criteria

1. Ada cannot read, pay or transition ord_ben; Ben retains each valid operation on a fresh DB.
2. Unknown and unowned identifiers use the same documented 404 shape without leaking order fields.
3. Unauthenticated requests fail and rejected mutations leave status/version untouched.
4. Tests use session identity, not a caller-supplied user_id field; check the reverse ownership direction too.

## Deliverable

Failing access test(s), ownership repair and allowed/denied HTTP checks. Use only the synthetic local accounts; no real service testing.

## Task sessions

Choose a session below for its scope, apps, outputs and checks.

- [10.1 — Audit an authenticated cross-user access path](../../sessions/10.1/GOAL.md)
- [10.2 — Repair and verify order ownership enforcement](../../sessions/10.2/GOAL.md)
