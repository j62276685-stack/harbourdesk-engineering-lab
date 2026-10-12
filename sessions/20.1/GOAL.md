# 20.1 — Write a defensible disputed-charge memo

**Role:** Incident analyst with backend expertise

**Purpose:** Answer a disputed-charge question without overstating incomplete evidence.

**Stakeholder:** Operations manager and customer-support lead.

## Task description

I am investigating a report that a disputed order may have been paid twice. My goal is to provide the operations manager and support lead with the strongest conclusion the incomplete evidence supports and a concrete plan to distinguish the remaining explanations.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `disputed-charge-evidence.ods`
- `settlement-investigation.drawio`
- `disputed-charge-memo.pdf`

## Quality checks

- [ ] The conclusion is bounded by the actual supplied evidence.
- [ ] At least two explanations are consistent with the fragments.
- [ ] The next observation specifies source, identifiers, time range and distinguishing outcomes.
- [ ] Current starter behavior and missing fragment lines are not treated as historical settlement proof.

**Apps:** Visual Studio Code, LibreOffice, draw.io Desktop.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

## Workflow

1. Inspect only the supplied historical fragments in VS Code and identify their reliability limits.
2. Build a fact/hypothesis/evidence-gap table in LibreOffice.
3. Draw a two-hypothesis decision tree with discriminating observations and export the manager memo.
