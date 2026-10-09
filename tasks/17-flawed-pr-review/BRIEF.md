# Task 17: Review a plausible but flawed pull request

## Error or request

Review a proposed “support major-unit refund input” PR. Decide whether it preserves the refund API contract and identify any consequential defect with a concrete trigger.

## Relevant files

[app/refunds.py](../../app/refunds.py); [inputs/pr-description.md](inputs/pr-description.md); proposed.patch; [refunds_candidate.py](inputs/refunds_candidate.py); [review-cases.json](inputs/review-cases.json).

- [pr-description.md](inputs/pr-description.md)
- [proposed.patch](inputs/proposed.patch)
- [refunds_candidate.py](inputs/refunds_candidate.py)
- [review-cases.json](inputs/review-cases.json)

## Reproduce or investigate

From the project root, run `./lab start 17`. Open the printed folder. Run `./lab serve` for browser work or `./lab test` for tests. Inputs are copied to `evidence/inputs/`.

Read the baseline, proposed source and diff without applying the PR to your workspace. You can import the candidate module from its file path into a disposable test to compare behavior. This is a local review artifact, not a live GitHub PR.

For the branch comparison in session 17.1, run `./lab setup-review` in a fresh task workspace; it creates the supplied local candidate and baseline branches.

## Completion criteria

1. Identify actionable defects with exact proposed-file lines, a minimal input and observed/expected result.
2. Connect each finding to the integer-minor-unit refund contract and the PR’s stated compatibility claim.
3. Distinguish blockers from optional style feedback and avoid unsupported hypothetical defects.
4. Provide at least one executable demonstration and legitimate-case checks, then give a reasoned approve/request-changes recommendation.

## Deliverable

outcomes/pr-review.md and demonstration tests/output. Do not implement a full revised PR or post comments externally.

## Task sessions

Choose a session below for its scope, apps, outputs and checks.

- [17.1 — Review the proposed refund conversion change](../../sessions/17.1/GOAL.md)
