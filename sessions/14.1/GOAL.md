# 14.1 — Specify notification events, recipients and channel rules

**Role:** Software requirements engineer

**Purpose:** Turn a vague notification request into implementable rules.

**Stakeholder:** Product manager, support lead and implementation team.

## Task description

Resolve a bounded set of stakeholder tensions into an event/recipient/channel matrix and routing diagram that the implementation team can use.

## Final deliverable

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
