# 08.1 — Decide how two contradictory provider observations should be reconciled

**Role:** Payments systems engineer

**Purpose:** Preserve trustworthy local state when provider evidence conflicts.

**Stakeholder:** Reconciliation operator and fulfilment lead.

## Task description

Evaluate the cancelled/success and paid/older-failure cases, choose a policy with explicit authority boundaries, and deliver an operator decision table and state diagram.

## Final deliverable

- `reconciliation-policy.ods`
- `reconciliation-model.drawio`
- `reconciliation-decision.pdf`

## Quality checks

- [ ] An older failure cannot undo a paid order.
- [ ] Late success for a cancelled order does not automatically reopen fulfilment.
- [ ] Audit identity, money/currency validation and repeated-observation behavior are explicit.
- [ ] The policy distinguishes observation time from settlement evidence.

**Apps:** Visual Studio Code, LibreOffice, draw.io Desktop.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

## Workflow

1. Inspect the supplied local facts and provider observations in VS Code.
2. Build the evidence/decision/audit table in LibreOffice with stale, normal, repeated and invalid cases.
3. Draw the order-versus-payment decision model and export the operator guidance.
