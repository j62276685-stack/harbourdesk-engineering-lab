# 08.2 — Implement the two-case reconciliation policy with an audit trail

**Role:** Payments systems engineer

**Purpose:** Preserve trustworthy local state when provider evidence conflicts.

**Stakeholder:** Reconciliation operator and fulfilment lead.

## Task description

I am investigating how the application applies provider observations that conflict with completed or cancelled orders. My goal is to provide the reconciliation operator with a verified repair that follows the agreed policy, retains an audit trail and avoids unintended fulfilment.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `provider-reconciliation.patch`
- `reconciliation-audit.csv`
- `reconciliation-verification.md`

## Quality checks

- [ ] The two conflicting cases preserve the selected safeguards.
- [ ] A normal matching success and an invalid money/currency observation are checked.
- [ ] Stable observation identity prevents a repeated financial/audit effect.
- [ ] The audit retains the received evidence and selected reason.

**Apps:** Visual Studio Code, DB Browser for SQLite, GitHub Desktop.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

**Starting dependency:** Use the supplied safeguards plus a frozen [08.1](../08.1/GOAL.md) policy, or write the bounded policy as part of this session’s first review.

## Workflow

1. Use the stated policy to edit the relevant handler/audit storage in VS Code.
2. Run the two conflict cases, a normal success and a replay; inspect order/audit records in DB Browser.
3. Review the diff and explain any state-model choice in the verification note.
