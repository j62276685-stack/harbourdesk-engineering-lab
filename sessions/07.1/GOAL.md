# 07.1 — Investigate a deterministic duplicate-delivery race

**Role:** Backend payments engineer

**Purpose:** Keep duplicate deliveries from creating duplicate business effects.

**Stakeholder:** Payments engineering lead and operations.

## Task description

I am investigating whether simultaneous deliveries of the same payment event create duplicate business effects. My goal is to provide the payments engineering lead with reproducible race evidence and a clear account of the transaction boundary needed to prevent duplication.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `webhook-invariants.ods`
- `webhook-race-review.pdf`
- `webhook-race-observation.json`

## Quality checks

- [ ] The scheduling is deterministic rather than a sleep guess.
- [ ] Payment, notification, receipt and order-version effects are all accounted for.
- [ ] The recommendation explains the durable business boundary.
- [ ] Sequential replay is compared with concurrent delivery.

**Apps:** Visual Studio Code, DB Browser for SQLite, LibreOffice.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

## Workflow

1. Run the race observation from VS Code and inspect the handler’s durable steps.
2. Use DB Browser to inspect payments, receipt, version and outbox counts in a captured disposable copy.
3. Build the effect/invariant table and write a concise transaction-boundary recommendation in LibreOffice.
