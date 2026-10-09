# 09.3 — Integrate deadline and Retry-After handling

**Role:** Integration software engineer

**Purpose:** Bound payment retries without increasing duplicate-charge risk.

**Stakeholder:** Payments integration reviewer.

## Task description

Add wait-budget and rate-limit handling to a frozen eligible-retry implementation, then verify the stop decisions using a fake clock and publish a timing audit.

## Final deliverable

- `retry-budget.patch`
- `retry-timing-audit.ods`
- `retry-budget-verdict.md`

## Quality checks

- [ ] Waits and simulated request durations count toward the eight-second budget.
- [ ] No next call begins after exhaustion or a wait exceeding the budget.
- [ ] 429 delay parsing and the four-second cap follow the contract.
- [ ] Timing evidence is fake-clock based and includes the final outcome.

**Apps:** Visual Studio Code, GitHub Desktop, LibreOffice.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

**Starting dependency:** A frozen eligibility/key implementation is required; use your [09.2](../09.2/GOAL.md) result. This is a separate Idea with that code as its starting input.

## Workflow

1. Inspect the supplied/human-created eligibility candidate and implement bounded waits/deadline checks.
2. Run malformed Retry-After, capped delay, exhausted budget and eventual-success scenarios using a fake clock.
3. Review the source diff in GitHub Desktop and recalculate the timing table in LibreOffice.
