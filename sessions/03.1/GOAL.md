# 03.1 — Reconstruct one incident and its evidence limits

**Role:** Site reliability engineer

**Purpose:** Give operations an evidence-backed account of a receipt incident.

**Stakeholder:** Incident commander and customer-support lead.

## Task description

Normalize the supplied incident fragments into a source-linked timeline, draw the event sequence and provide an operations conclusion that distinguishes facts from missing evidence.

## Final deliverable

- `incident-evidence.ods`
- `incident-timeline.drawio`
- `incident-summary.pdf`

## Quality checks

- [ ] Each material event has a source row/line and normalized UTC time.
- [ ] Minute aggregates are not treated as individual events.
- [ ] Facts, inference and missing evidence are visibly differentiated.
- [ ] The summary does not equate repeated event delivery with duplicate settlement.

**Apps:** Visual Studio Code, LibreOffice, draw.io Desktop.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

## Workflow

1. Inspect raw records and source reliability notes in VS Code.
2. Build a bounded evidence/timestamp table in LibreOffice Calc; normalize timezone and clock differences.
3. Draw the incident sequence with basic shapes, then export a one-page summary with unresolved questions.
