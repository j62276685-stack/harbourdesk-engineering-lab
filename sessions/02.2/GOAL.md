# 02.2 — Enforce and verify expiry in one checkout path

**Role:** Backend software engineer

**Purpose:** Prevent payment attempts after an order reservation expires.

**Stakeholder:** Checkout product owner and QA engineer.

## Task description

Enforce the server deadline and corresponding button state, test a small fixed-clock boundary set, and deliver a checkout patch for review.

## Final deliverable

- `expiry-fix.patch`
- `expiry-checks.md`
- `rejected-order-observation.csv`

## Quality checks

- [ ] One second before is allowed; equality and one second after are rejected.
- [ ] Expired UI actions are unavailable and change at the visible deadline.
- [ ] Rejected API actions leave persisted state unchanged.
- [ ] One equivalent offset timestamp and a normal active order are checked.

**Apps:** Visual Studio Code, Firefox, DB Browser for SQLite.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

**Starting dependency:** [02.1](../02.1/GOAL.md) is optional context; all time fixtures and the contract are supplied.

## Workflow

1. Edit the bounded eligibility/UI behavior in VS Code.
2. Use Firefox to verify action state and a direct request; run a focused boundary test through the task menu.
3. Use DB Browser to confirm rejected requests did not change status/version, then export the patch and check results.
