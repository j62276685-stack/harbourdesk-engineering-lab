# 07.2 — Repair the atomic webhook effect boundary

**Role:** Backend payments engineer

**Purpose:** Keep duplicate deliveries from creating duplicate business effects.

**Stakeholder:** Payments engineering lead and operations.

## Task description

Implement one durable event-application boundary for matching success events and verify sequential/concurrent delivery before handing over the change.

## Final deliverable

- `webhook-atomicity.patch`
- `webhook-effect-checks.md`
- `webhook-durable-evidence.csv`

## Quality checks

- [ ] An identical event produces one business effect under sequential/concurrent delivery.
- [ ] All deliveries acknowledge once the event is durably applied.
- [ ] Distinct orders/events still apply independently.
- [ ] Rejected input creates no success receipt/effect.

**Apps:** Visual Studio Code, DB Browser for SQLite, GitHub Desktop.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

**Starting dependency:** [07.1](../07.1/GOAL.md) is useful context; the supplied delivery contract defines the invariant independently.

## Workflow

1. Edit the handler/schema narrowly in VS Code using the stated invariant.
2. Run focused replay/concurrency checks; use DB Browser to compare committed side-effect rows.
3. Review the diff in GitHub Desktop, record the validation limits and export the patch.
