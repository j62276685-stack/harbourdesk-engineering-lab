# Task 05: Find the smallest patch for a reproducible bug

## Error or request

Pasting a valid search term with spaces returns no order, although typing it manually works. Find the smallest justified repair without changing search authorization or ordering.

## Relevant files

[app/search.py](../../app/search.py); [app/http.py](../../app/http.py); [inputs/search-cases.json](inputs/search-cases.json).

- [search-cases.json](inputs/search-cases.json)

## Reproduce or investigate

From the project root, run `./lab start 05`. Open the printed folder. Run `./lab serve` for browser work or `./lab test` for tests. Inputs are copied to `evidence/inputs/`.

Run `./lab probe 05`. Compare the supplied terms against PRODUCT.md. Keep the change limited to the search behavior unless evidence demonstrates another required change.

## Completion criteria

1. Padded, unpadded and differently cased terms return identical IDs.
2. An empty or all-whitespace term lists the caller’s own orders in the original order.
3. No-match and Ben’s isolated results retain their existing behavior.
4. Explain why each changed line is necessary; avoid renaming unrelated APIs, adding dependencies or rewriting the request router.

## Deliverable

A minimal patch and focused verification. Report changed lines and why a larger alternative was unnecessary.

## Task sessions

Choose a session below for its scope, apps, outputs and checks.

- [05.1 — Choose and deliver the smallest justified search repair](../../sessions/05.1/GOAL.md)
