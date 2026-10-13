# 18.1 — Recover both sides’ intent from the delivery conflict

**Role:** Software integration engineer

**Purpose:** Combine delivery-price changes without losing either business requirement.

**Stakeholder:** Delivery product owner and release maintainer.

## Task description

I am investigating a delivery-pricing conflict between free local delivery and a remote-region surcharge. My goal is to provide the product owner and release maintainer with the combined business rule, an acceptance matrix and a merge plan that preserves both changes.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `delivery-intent-matrix.ods`
- `delivery-merge-plan.pdf`
- `branch-evidence.md`

## Quality checks

- [ ] Both branches’ requirements and test contributions are identified.
- [ ] The threshold equality and remote high-subtotal case are specified.
- [ ] The plan explains why selecting either side wholesale would lose intent.
- [ ] The conflict remains an input; the deliverable is the completed review/plan.

**Apps:** Visual Studio Code, GitHub Desktop, LibreOffice.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

## Workflow

1. Inspect both branch histories/diffs in GitHub Desktop and the conflict/tests in VS Code.
2. Use LibreOffice to build the subtotal/region behavior matrix and combined requirement rationale.
3. Export a merge-intent handoff without resolving the source in this session.
