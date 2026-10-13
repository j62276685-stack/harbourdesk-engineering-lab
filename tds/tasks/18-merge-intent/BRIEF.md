# Task 18: Resolve a merge conflict where both changes matter

## Error or request

I am investigating conflicting delivery-pricing changes for free local delivery and a remote-region surcharge. My goal is to provide the release maintainer with a completed merge that preserves both business rules and passes both branches’ checks.

## Relevant files

[app/shipping.py](../../../app/shipping.py); [inputs/branch-intent.md](inputs/branch-intent.md); generated tests/test_local_delivery.py; tests/test_remote_delivery.py.

- [branch-intent.md](inputs/branch-intent.md)

## Reproduce or investigate

Open the [Task 18 workspace](../../workspaces/18-merge-intent.code-workspace). It uses the shared application and database. Read the inputs above. Run `./tds/lab serve` for browser work or `./tds/lab test` for tests.

Run `./tds/lab setup-merge` after committing your earlier fixes. It creates local branches free-delivery and remote-delivery and leaves a real Git conflict. Inspect both branch changes and the generated tests. Git must be installed for this task.

## Completion criteria

1. Local subtotal below 25000 pays 1500; local subtotal at/above 25000 pays zero.
2. Remote delivery pays 3000 at all subtotals, including values qualifying for free local delivery.
3. Both branch test files survive and pass with the baseline suite. Add boundary/combination checks where useful.
4. No conflict markers remain and the completed merge commit has both branch tips as parents.
5. Explain the combined business intent and how your resolution differs from blindly selecting a side.

## Deliverable

Resolved source, passing checks, a completed local merge commit and short decision record. No push or remote branch is required.

## Task sessions

Choose a session below for its scope, apps, outputs and checks.

- [18.1 — Recover both sides’ intent from the delivery conflict](../../sessions/18.1/GOAL.md)
- [18.2 — Resolve the delivery conflict and verify both parent changes](../../sessions/18.2/GOAL.md)
