# 08.1 — Decide how two contradictory provider observations should be reconciled

**Role:** Payments systems engineer

**Purpose:** Preserve trustworthy local state when provider evidence conflicts.

**Stakeholder:** Reconciliation operator and fulfilment lead.

## Task description

I am investigating provider observations that contradict local order state: a success for a cancelled order and an older failure for a paid order. My goal is to provide the reconciliation operator and fulfilment lead with a decision policy that preserves evidence and prevents accidental fulfilment.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
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
