# 16.2 — Refactor one billing path against a frozen safety matrix

**Role:** Software maintenance engineer

**Purpose:** Make billing code easier to maintain while preserving pricing behavior.

**Stakeholder:** Billing-module maintainer.

## Task description

I am investigating how to simplify the billing module without changing established invoice totals. My goal is to provide the maintainer with a focused refactor and evidence of compatibility against the recorded characterization checks and input sample.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `billing-refactor.patch`
- `billing-equivalence.ods`
- `billing-refactor-rationale.md`

## Quality checks

- [ ] The public entry point remains compatible.
- [ ] The calculation order and frozen outputs are unchanged.
- [ ] Equivalence includes a broader sample and threshold/rounding cases.
- [ ] The rationale identifies a maintenance improvement with no unrelated pricing change.

**Apps:** Visual Studio Code, GitHub Desktop, LibreOffice.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

**Starting dependency:** Frozen baseline outputs/checks from [16.1](../16.1/GOAL.md) are required. Do not characterize only the already-refactored code.

## Workflow

1. Choose one internal responsibility boundary and refactor it in VS Code.
2. Run the frozen cases and broader sample; compare outputs and calculations in LibreOffice.
3. Review the diff and interface contract in GitHub Desktop, then export the patch and design note.
