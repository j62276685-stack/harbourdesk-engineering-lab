# 07.3 — Audit interrupted-delivery recovery on a candidate handler

**Role:** Backend payments engineer

**Purpose:** Keep duplicate deliveries from creating duplicate business effects.

**Stakeholder:** Payments engineering lead and operations.

## Task description

Design a bounded failure injection around a durable write, run it against the supplied or your candidate handler, and deliver a repeatability/rollback verdict.

## Final deliverable

- `webhook-recovery-cases.ods`
- `webhook-recovery-verdict.pdf`
- `webhook-interruption-evidence.json`

## Quality checks

- [ ] The exact interruption point and retry sequence are documented.
- [ ] Durable rows and order version are compared before/after retry.
- [ ] The verdict is supported whether the candidate passes or fails.
- [ ] No duplicate financial/outbox effect is silently accepted.

**Apps:** Visual Studio Code, DB Browser for SQLite, LibreOffice.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

**Starting dependency:** A frozen candidate handler is required. The original starter is a valid candidate for an audit; a human-created [07.2](../07.2/GOAL.md) patch is another option.

## Workflow

1. Select one interruption point and predict the observable invariants without claiming a remote charge result.
2. Run the controlled interruption/retry check in VS Code and inspect durable records with DB Browser.
3. Complete the recovery test table and export a QA verdict in LibreOffice, including a failure verdict if justified.
