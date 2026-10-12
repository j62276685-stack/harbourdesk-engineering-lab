# 02.1 — Audit expired-payment behavior at the boundary

**Role:** Backend software engineer

**Purpose:** Prevent payment attempts after an order reservation expires.

**Stakeholder:** Checkout product owner and QA engineer.

## Task description

I am investigating a report that expired orders still show a payment option and accept payment requests. My goal is to provide the checkout product owner and QA engineer with an evidence matrix showing the interface, API and database behavior at the expiry boundary.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `expiry-evidence.csv`
- `expiry-defect.md`
- `expiry-interface.png`

## Quality checks

- [ ] The three time cases are controlled explicitly.
- [ ] UI and server outcomes are recorded separately.
- [ ] Before/after persisted values support the mutation claim.
- [ ] The defect note specifies rejection at equality and legitimate unexpired behavior.

**Apps:** Firefox, Visual Studio Code, DB Browser for SQLite.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

## Workflow

1. Inspect the three order fixtures and server clock in DB Browser and the app.
2. Observe browser requests and the source predicate while comparing before/exactly-at/after expiry.
3. Record the outcome, before/after status and version, and exact acceptance boundary.
