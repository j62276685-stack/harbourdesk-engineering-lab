# 10.2 — Repair and verify order ownership enforcement

**Role:** Application security engineer

**Purpose:** Protect one customer’s orders from another authenticated customer.

**Stakeholder:** Security reviewer and account-service owner.

## Task description

I am investigating the order-service boundary that permits cross-user access. My goal is to provide the account-service owner with a verified ownership repair that rejects unauthorized reads and changes while preserving legitimate customer access.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `ownership-fix.patch`
- `ownership-http-checks.md`
- `ownership-state-evidence.csv`

## Quality checks

- [ ] Unowned and unknown orders use the same documented 404 response.
- [ ] The owner retains valid read and mutation behavior on fresh data.
- [ ] Unauthenticated requests fail independently.
- [ ] Rejected cross-user requests leave status and version unchanged.

**Apps:** Visual Studio Code, Firefox, DB Browser for SQLite.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

**Starting dependency:** The supplied access matrix is sufficient; [10.1](../10.1/GOAL.md) may be included as context.

## Workflow

1. Write focused session-based denied/allowed checks and implement the ownership repair.
2. Validate selected routes through Firefox request inspection.
3. Use DB Browser to verify rejected mutations left rows unchanged and export the source/test evidence.
