# 09.1 — Design the bounded charge-retry decision table

**Role:** Integration software engineer

**Purpose:** Bound payment retries without increasing duplicate-charge risk.

**Stakeholder:** Payments integration reviewer.

## Task description

Choose the retry/stop outcome for the supplied status and duration scripts, calculate the deadline envelope, and deliver an implementable policy with an uncertainty warning.

## Final deliverable

- `retry-decision-table.ods`
- `retry-state-route.drawio`
- `retry-policy.pdf`

## Quality checks

- [ ] Eligible/permanent statuses match the supplied contract.
- [ ] Three calls and the eight-second envelope include request duration and waits.
- [ ] Retry-After validity/cap and stable idempotency identity are specified.
- [ ] Final timeout is not described as proof of no charge.

**Apps:** Visual Studio Code, LibreOffice, draw.io Desktop.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

## Workflow

1. Inspect provider call shape and scripted durations in VS Code.
2. In Calc build the eligibility, stable-key, attempt and wait-budget matrix.
3. Draw the stop/retry decision route and export the policy with timeout ambiguity.
