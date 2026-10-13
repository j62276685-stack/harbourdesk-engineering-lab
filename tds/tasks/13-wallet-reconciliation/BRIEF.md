# Task 13: Reconcile a wallet balance with transaction history

## Error or request

I am investigating a customer dispute about a wallet balance that differs from its posted transaction history. My goal is to provide finance operations with an evidence-based reconciliation and an audited, repeat-safe correction that preserves the ledger.

## Relevant files

[app/wallet.py](../../../app/wallet.py); [app/schema.sql](../../../app/schema.sql); [inputs/wallet-statement.csv](inputs/wallet-statement.csv); [reconciliation-policy.md](inputs/reconciliation-policy.md).

- [reconciliation-policy.md](inputs/reconciliation-policy.md)
- [wallet-statement.csv](inputs/wallet-statement.csv)

## Reproduce or investigate

Open the [Task 13 workspace](../../workspaces/13-wallet-reconciliation.code-workspace). It uses the shared application and database. Read the inputs above. Run `./tds/lab serve` for browser work or `./tds/lab test` for tests.

Run `./tds/lab probe 13`, query wallet_accounts and wallet_entries, and compare the supplied statement. Preserve the initial extracts. Ben provides a consistent control case.

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
