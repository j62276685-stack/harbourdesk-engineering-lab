# 18.2 — Resolve the delivery conflict and verify both parent changes

**Role:** Software integration engineer

**Purpose:** Combine delivery-price changes without losing either business requirement.

**Stakeholder:** Delivery product owner and release maintainer.

## Task description

Resolve the single delivery-pricing conflict, preserve both branch tests, and complete a local merge with a reviewed behavior/parentage record.

## Final deliverable

- `delivery-merge-results.ods`
- `delivery-merge-checks.md`
- `delivery-merged.patch`

## Quality checks

- [ ] Local below/at threshold and remote below/above cases are correct.
- [ ] Both sets of branch tests and the baseline suite pass.
- [ ] No conflict markers remain.
- [ ] The completed local merge has both branch tips as parents.

**Apps:** Visual Studio Code, GitHub Desktop, LibreOffice.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

**Starting dependency:** [18.1](../18.1/GOAL.md) is optional; the supplied branch-intent document defines the combined rule.

## Workflow

1. Resolve the bounded source conflict in VS Code against the supplied branch intent.
2. Run both branch tests and inspect the resolved change/merge completion in GitHub Desktop.
3. Complete the boundary/results matrix in LibreOffice and export the merge proof and decision note.
