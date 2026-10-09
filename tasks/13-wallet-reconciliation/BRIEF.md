# Task 13: Reconcile a wallet balance with transaction history

## Error or request

Ada’s displayed wallet balance is disputed. Reconcile the cached balance with posted entries, decide what is authoritative, and implement an audited correction that can be safely repeated.

## Relevant files

[app/wallet.py](../../app/wallet.py); [app/schema.sql](../../app/schema.sql); [inputs/wallet-statement.csv](inputs/wallet-statement.csv); [reconciliation-policy.md](inputs/reconciliation-policy.md).

- [reconciliation-policy.md](inputs/reconciliation-policy.md)
- [wallet-statement.csv](inputs/wallet-statement.csv)

## Reproduce or investigate

From the project root, run `./lab start 13`. Open the printed folder. Run `./lab serve` for browser work or `./lab test` for tests. Inputs are copied to `evidence/inputs/`.

Run `./lab probe 13`, query wallet_accounts and wallet_entries, and compare the supplied statement. Preserve the initial extracts. Ben provides a consistent control case.

## Completion criteria

1. Identify the discrepancy with arithmetic and source references; distinguish cache correction from inventing a new financial transaction.
2. After correction the cache equals the sum of posted ledger entries for the affected account.
3. Retain all existing entries byte-for-byte at the field level; create an audit record with old/new amounts, time and reason.
4. Repeated repair does not add another corrective effect/audit record for the same resolved discrepancy.
5. Test the consistent account, repeated execution, unknown account and an interruption/rollback scenario.

## Deliverable

Diagnosis, audited correction, verification extracts and tests. No real currency movement is involved.

## Task sessions

Choose a session below for its scope, apps, outputs and checks.

- [13.1 — Reconcile one wallet cache against its posted ledger](../../sessions/13.1/GOAL.md)
- [13.2 — Implement a repeat-safe audited wallet cache correction](../../sessions/13.2/GOAL.md)
