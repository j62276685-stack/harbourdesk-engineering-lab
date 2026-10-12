# Task 04: Write a regression test from a vague complaint

## Error or request

I am investigating a customer report that the first page of orders skips records and later pages look incorrect. My goal is to provide the account product owner with a deterministic regression test, a focused pagination repair and evidence that the expected records now appear.

## Relevant files

[app/orders.py](../../app/orders.py); [app/http.py](../../app/http.py); [tests/test_baseline.py](../../tests/test_baseline.py); [inputs/complaint.txt](inputs/complaint.txt).

- [complaint.txt](inputs/complaint.txt)

## Reproduce or investigate

Open the [Task 04 workspace](../../workspaces/04-complaint-regression.code-workspace). It uses the shared application and database. Read the inputs above. Run `./lab serve` for browser work or `./lab test` for tests.

Run `./lab probe 04`, inspect Ada’s ordered IDs with `./lab sql`, and compare `/api/orders` with pages of size two. Establish a precise expected result from PRODUCT.md before writing your test.

## Completion criteria

1. Create your own test which fails on the original source and passes with the patch; preserve both outputs.
2. With at least five owned records, concatenated successive pages match the full ordered list without gaps or duplicate IDs.
3. Page one begins at the first ordered item; a page beyond the final item is empty.
4. Size one, alternate page sizes and invalid page numbers behave consistently; Ben’s records are excluded.

## Deliverable

Your new regression test, focused repair, clarified bug statement and before/after test evidence. Existing probes are observations, not the regression test deliverable.

## Task sessions

Choose a session below for its scope, apps, outputs and checks.

- [04.1 — Turn the pagination complaint into a regression repair](../../sessions/04.1/GOAL.md)
