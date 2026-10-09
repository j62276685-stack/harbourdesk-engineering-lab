# Data dictionary and seed inventory

The executable schema is [app/schema.sql](../app/schema.sql); [app/db.py](../app/db.py) creates the synthetic initial rows. Tables live in your own workspace's `runtime/lab.sqlite3`. Use a new workspace or an explicit disposable `LAB_DB` for destructive experiments.

| Table | Key/important fields | Baseline seed | Purpose |
|---|---|---:|---|
| users | id; unique email; name | 2 | Ada and Ben |
| sessions | id; user_id; state; state_used | 0 | Created at login/provider start |
| orders | id; owner user_id; status; integer amount_minor; currency; expiry/creation; provider_status; version | 7 | Customer orders and boundary cases |
| payments | id; event_id; order_id; amount_minor; currency; created_at | 0 | Applied successful payment events |
| webhook_receipts | event_id; received_at | 0 | Processed-delivery bookkeeping |
| wallet_accounts | user_id; balance_minor | 2 | Cached posted balance |
| wallet_entries | id; user_id; delta_minor; source_ref; created_at; note | 4 | Authoritative posted ledger |
| wallet_audit | id; user_id; old_balance; new_balance; reason; created_at | 0 | Cache-reconciliation audit trail |
| customers | id; raw email/phone; external_ref; imported_at | 8 | Legacy import for migration |
| notification_outbox | id; event_id; user_id; channel; payload; status; attempts; available_at; last_error | 2 | Local notification drill |
| worker_state | singleton id=1; mode; failure_remaining | 1 | Controllable local dependency condition |

Orders use ID ordering for customer lists, and descending creation time with ID tie-break for the report query. `version` starts at zero for pending orders and one for the existing paid/cancelled records. It represents accepted changes; rejected/duplicate operations should not increment it where that is part of your task's contract.

The existing indexes/constraints reflect the existing implementation, not a finished design. For example, a unique receipt identifier alone does not establish transaction-wide correctness. Add or evolve tables/indexes where your brief permits, documenting how existing data is handled.

Legacy customer JSON preserves the difference between null and an empty string; the CSV is a convenient human-readable view. The database/JSON is authoritative when a CSV empty cell is ambiguous. Keep raw source records as well as normalized identities in the migration exercise.

All balances and order/payment amounts are integer minor units. There is no real external settlement data. In tasks 3 and 20, historical incident identifiers intentionally belong to supplied evidence rather than the interactive seed. Do not join them to unrelated seed records or infer historical deployment behavior from current source.
