# 18.1 — Recover both sides’ intent from the delivery conflict

**Role:** Software integration engineer

**Purpose:** Combine delivery-price changes without losing either business requirement.

**Stakeholder:** Delivery product owner and release maintainer.

## Task description

Inspect the two local branch changes and tests, produce the combined delivery rule and acceptance matrix, and hand a bounded merge plan to the maintainer.

## Final deliverable

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
