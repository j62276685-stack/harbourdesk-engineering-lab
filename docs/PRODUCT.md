# HarbourDesk product context

HarbourDesk is a customer account product for a fictional Lagos click-and-collect shop. The customer portal brings existing reservations, payment details and stored credit into one place. Operations staff work with the corresponding payments, customer-import and notification contracts.

The local preview uses example accounts and provider records without a real external service. Order display names are presentation metadata; the source IDs, states, amounts and timestamps below remain authoritative.

Money is an integer number of minor units: NGN 125.00 is `12500`. Dates are UTC; a timestamp ending in Z has the same instant as an equivalent explicit offset. The application clock defaults to **6 October 2026, 09:00 UTC (10:00 Lagos)**. Tests must control the clock instead of depending on the day you run them.

## Accounts and example orders

| Account | ID | Password | Owns |
|---|---:|---|---|
| Ada | 1 | `practice-only` | `ord_active`, `ord_expired`, `ord_boundary`, `ord_before`, `ord_cancelled`, `ord_paid` |
| Ben | 2 | `practice-only` | `ord_ben` |

Use `ada@example.test` and `ben@example.test`. These passwords and webhook secrets are public synthetic fixtures. A wallet cache may disagree with the append-only ledger; diagnosing that is task 13. Task 11 adds reproducible bulk orders to the shared database for the before/after benchmark.

## Business contracts

- A customer may read or mutate only their own order. Unknown and unowned identifiers should both produce a 404 with `order_not_found`. Authentication is required for customer endpoints.
- An order is payable only while its status is `pending_payment` and the server time is strictly earlier than `expires_at`. Reject at the exact expiry instant. Rejected actions must leave order status, version and financial records unchanged.
- Search matches an ID substring without regard to case. Leading/trailing whitespace in a query is ignored. An all-whitespace query acts like an empty query and lists the caller's orders.
- Order pages use one-based page numbers, ID ascending order and an independent page size. An out-of-range page is empty. Invalid parameters produce 400.
- Successful provider events use a stable event ID. A duplicate must not create a second payment, second notification or extra state-version update. Amount and currency must match the intended order.
- A stale provider observation cannot silently undo a completed local payment. A settled payment for an already cancelled order needs an explicit reconciliation decision and an audit record; it must not automatically trigger fulfilment.
- The wallet ledger is authoritative for posted transactions. Existing entries must retain their original identifiers, references, values and timestamps. Any correction must record an explanation and be safe to repeat.

The application contains the task defects. The baseline tests verify a few working behaviors, not the full product. Work only on the contract named in your selected task.
