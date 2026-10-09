# 06.1 — Specify a customer-safe provider error taxonomy

**Role:** Payments integration engineer

**Purpose:** Give customers accurate failure messages and support usable error categories.

**Stakeholder:** Payments support lead and checkout team.

## Task description

Use the supplied response fixtures to distinguish customer validation, declines and dependency failures, then deliver a classification table and routing diagram to the checkout team.

## Final deliverable

- `error-taxonomy.ods`
- `error-routing.drawio`
- `error-contract.pdf`

## Quality checks

- [ ] Bad local values and upstream failures are distinct.
- [ ] Outage, decline, timeout, unexpected response and success are covered.
- [ ] Raw upstream diagnostic text is not proposed as customer copy.
- [ ] Each classification follows API.md or explicitly records an unresolved choice.

**Apps:** Visual Studio Code, LibreOffice, draw.io Desktop.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

## Workflow

1. Observe the fixture cases with the VS Code task runner and inspect the current mapping.
2. Complete a classification table in Calc with HTTP code, machine code, safe message and source of responsibility.
3. Draw the decision route with basic shapes and export a short implementation handoff.
