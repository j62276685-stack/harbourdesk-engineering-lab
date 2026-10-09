# 13.2 — Implement a repeat-safe audited wallet cache correction

**Role:** Backend finance-systems engineer

**Purpose:** Reconcile the displayed wallet balance without rewriting financial history.

**Stakeholder:** Finance operations analyst.

## Task description

Repair only a confirmed cached-balance discrepancy, preserve the ledger, and demonstrate an atomic audit/correction plus safe repetition.

## Final deliverable

- `wallet-cache-repair.patch`
- `wallet-audit-evidence.csv`
- `wallet-repair-checks.md`

## Quality checks

- [ ] Corrected cache equals posted ledger sum.
- [ ] Original ledger fields are unchanged.
- [ ] One atomic audit/correction records old/new amount and reason.
- [ ] Repeat, consistent account, unknown account and controlled rollback are verified.

**Apps:** Visual Studio Code, DB Browser for SQLite, GitHub Desktop.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

**Starting dependency:** The supplied reconciliation policy defines the boundary; [13.1](../13.1/GOAL.md) is optional context.

## Workflow

1. Implement the bounded repair and domain cases in VS Code.
2. Run the correction/repeat/control checks and inspect ledger/cache/audit rows in DB Browser.
3. Review the code diff and export before/after extracts with interruption/rollback evidence.
