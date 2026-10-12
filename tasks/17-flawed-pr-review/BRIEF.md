# Task 17: Review a plausible but flawed pull request

## Error or request

I am investigating whether a proposed refund conversion change preserves the published amount contract. My goal is to provide the pull-request author and payments engineering lead with a prioritized review, a minimal demonstration of any consequential defect and a justified approval recommendation.

## Relevant files

[app/refunds.py](../../app/refunds.py); [inputs/pr-description.md](inputs/pr-description.md); proposed.patch; [refunds_candidate.py](inputs/refunds_candidate.py); [review-cases.json](inputs/review-cases.json).

- [pr-description.md](inputs/pr-description.md)
- [proposed.patch](inputs/proposed.patch)
- [refunds_candidate.py](inputs/refunds_candidate.py)
- [review-cases.json](inputs/review-cases.json)

## Reproduce or investigate

Open the [Task 17 workspace](../../workspaces/17-flawed-pr-review.code-workspace). It uses the shared application and database. Read the inputs above. Run `./lab serve` for browser work or `./lab test` for tests.

Read the baseline, proposed source and diff without applying the PR to your workspace. You can import the candidate module from its file path into a disposable test to compare behavior. This is a local review artifact, not a live GitHub PR.

For the branch comparison in session 17.1, run `./lab setup-review` after committing your earlier fixes; it creates review branches without changing the shared application.

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
