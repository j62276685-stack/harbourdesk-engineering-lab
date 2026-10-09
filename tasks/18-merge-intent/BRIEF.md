# Task 18: Resolve a merge conflict where both changes matter

## Error or request

Two delivery-pricing changes conflict: free local delivery at a threshold and a remote-region surcharge. Resolve the merge so both business requirements survive.

## Relevant files

[app/shipping.py](../../app/shipping.py); [inputs/branch-intent.md](inputs/branch-intent.md); generated tests/test_local_delivery.py; tests/test_remote_delivery.py.

- [branch-intent.md](inputs/branch-intent.md)

## Reproduce or investigate

From the project root, run `./lab start 18`. Open the printed folder. Run `./lab serve` for browser work or `./lab test` for tests. Inputs are copied to `evidence/inputs/`.

Run `./lab setup-merge` in the pristine task 18 workspace. It creates local branches free-delivery and remote-delivery and leaves a real Git conflict. Inspect both branch changes and the generated tests. Git must be installed for this task.

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
