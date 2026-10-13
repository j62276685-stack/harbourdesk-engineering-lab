# 14.1 — Specify notification events, recipients and channel rules

**Role:** Software requirements engineer

**Purpose:** Turn a vague notification request into implementable rules.

**Stakeholder:** Product manager, support lead and implementation team.

## Task description

I am investigating a product request to notify customers about order changes without sending unnecessary messages. My goal is to provide the product manager, support lead and implementation team with clear event, recipient and channel rules that resolve the supplied stakeholder conflicts.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `notification-rules.ods`
- `notification-routing.drawio`
- `notification-rules.pdf`

## Quality checks

- [ ] Paid/cancelled/fulfilled/refunded and operator conflict events are covered.
- [ ] Required transactional messages and optional marketing are distinguished.
- [ ] Missing contact information and timezone/quiet hours have explicit behavior.
- [ ] The matrix states dedupe identity, retention assumption and privacy boundary.

**Apps:** Visual Studio Code, LibreOffice, draw.io Desktop.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

## Workflow

1. Inspect the supplied events/preferences and stakeholder notes in VS Code.
2. Build the channel/recipient/consent/quiet-hour matrix in Calc, labelling provisional choices.
3. Draw routing and deduplication boundaries, then export the requirements handoff.
