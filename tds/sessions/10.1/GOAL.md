# 10.1 — Audit an authenticated cross-user access path

**Role:** Application security engineer

**Purpose:** Protect one customer’s orders from another authenticated customer.

**Stakeholder:** Security reviewer and account-service owner.

## Task description

I am investigating whether one authenticated customer can read or change another customer’s order. My goal is to provide the security reviewer and account-service owner with a source-linked access matrix and an evidence-based severity and repair recommendation.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `access-matrix.csv`
- `ownership-finding.md`
- `access-response-evidence.png`

## Quality checks

- [ ] Caller identity comes from the authenticated session.
- [ ] Read/pay/transition are compared on fresh copies.
- [ ] Unowned/unknown response leakage and persisted mutation effects are considered.
- [ ] The report includes legitimate access, not only a denied-case claim.

**Apps:** Firefox, Visual Studio Code, DB Browser for SQLite.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

## Workflow

1. Inspect session identity and the seeded ownership record in DB Browser.
2. Use two clean Firefox sessions and selected direct requests to compare allowed/denied behavior.
3. Trace the route/service ownership boundary in VS Code and write the access evidence and scoped recommendation.
