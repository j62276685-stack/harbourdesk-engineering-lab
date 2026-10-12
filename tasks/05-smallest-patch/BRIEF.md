# Task 05: Find the smallest patch for a reproducible bug

## Error or request

I am investigating a customer report that pasting a search term with surrounding spaces returns no orders. My goal is to provide the maintainer with the smallest verified repair and explain why it preserves search authorization and ordering.

## Relevant files

[app/search.py](../../app/search.py); [app/http.py](../../app/http.py); [inputs/search-cases.json](inputs/search-cases.json).

- [search-cases.json](inputs/search-cases.json)

## Reproduce or investigate

Open the [Task 05 workspace](../../workspaces/05-smallest-patch.code-workspace). It uses the shared application and database. Read the inputs above. Run `./lab serve` for browser work or `./lab test` for tests.

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
