# Lifecycle contract
States: draft, pending_payment, paid, fulfilling, fulfilled, cancelled, refunded.
Allowed new-state transitions:
- draft → pending_payment or cancelled
- pending_payment → paid or cancelled
- paid → fulfilling or refunded
- fulfilling → fulfilled or refunded
- fulfilled → refunded
- cancelled → none
- refunded → none
Same-state requests are successful no-ops. Every other known pair is forbidden. Unknown targets are validation errors. Reject unauthorized access before disclosing state. No partial/refund amount modeling, shipping integration, inventory reservation or event delivery is required in this exercise.
