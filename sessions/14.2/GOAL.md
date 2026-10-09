# 14.2 — Turn notification policy into an acceptance specification

**Role:** Software requirements engineer

**Purpose:** Turn a vague notification request into implementable rules.

**Stakeholder:** Product manager, support lead and implementation team.

## Task description

Challenge a frozen notification policy with eight edge scenarios, tighten ambiguous rules and deliver a testable acceptance specification to QA.

## Final deliverable

- `notification-acceptance.ods`
- `notification-acceptance-flow.drawio`
- `notification-qa-spec.pdf`

## Quality checks

- [ ] Eight named scenario groups in the original brief are covered.
- [ ] Each expected outcome is grounded in a rule or explicit assumption.
- [ ] Duplicate/out-of-order behavior is testable.
- [ ] Unresolved product choices have an impact and concrete provisional default.

**Apps:** Visual Studio Code, LibreOffice, draw.io Desktop.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

**Starting dependency:** A frozen [14.1](../14.1/GOAL.md) policy is required, or use the supplied stakeholder notes as an intentionally incomplete draft policy and clearly mark that boundary.

## Workflow

1. Cross-check policy statements against the supplied event and preference examples.
2. Complete eight Given/When/Then cases in LibreOffice and identify missing or conflicting behavior.
3. Update the decision-flow diagram for the clarified rules and export the QA specification.
