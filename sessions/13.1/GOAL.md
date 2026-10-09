# 13.1 — Reconcile one wallet cache against its posted ledger

**Role:** Backend finance-systems engineer

**Purpose:** Reconcile the displayed wallet balance without rewriting financial history.

**Stakeholder:** Finance operations analyst.

## Task description

Independently calculate Ada’s posted balance, compare the cache and consistent control account, and produce an auditable correction recommendation.

## Final deliverable

- `wallet-reconciliation.ods`
- `wallet-authority.drawio`
- `wallet-correction-recommendation.pdf`

## Quality checks

- [ ] Arithmetic and source references are reproducible.
- [ ] Ben is checked as a consistent control.
- [ ] The recommendation does not invent a compensating financial transaction.
- [ ] The original ledger and necessary audit facts are specified.

**Apps:** DB Browser for SQLite, LibreOffice, draw.io Desktop.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

## Workflow

1. Inspect account/ledger values and source references in DB Browser.
2. Calculate the balance/difference in Calc and distinguish cached data from posted transactions.
3. Draw the ledger/cache/audit responsibility model and export the finance handoff.
