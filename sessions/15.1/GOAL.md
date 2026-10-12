# 15.1 — Model the seven-state order lifecycle for QA

**Role:** Backend domain engineer

**Purpose:** Make order transitions predictable and enforceable.

**Stakeholder:** Fulfilment product owner and QA team.

## Task description

I am investigating an order lifecycle that permits unclear or invalid state changes. My goal is to provide the fulfilment product owner and QA team with a state diagram and transition matrix defining allowed moves, repeated requests and error behavior.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `order-transition-matrix.ods`
- `order-lifecycle.drawio`
- `order-lifecycle-spec.pdf`

## Quality checks

- [ ] All seven states and every pair are classified.
- [ ] The diagram matches the permitted transitions.
- [ ] Same-state/version and error-code/ownership boundaries are explicit.
- [ ] Terminal states are represented correctly.

**Apps:** Visual Studio Code, LibreOffice, draw.io Desktop.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

## Workflow

1. Inspect the current transition source and supplied lifecycle contract.
2. Build the seven-by-seven allowed/forbidden/no-op matrix in Calc.
3. Draw the state diagram with terminal states and export the concise QA contract.
