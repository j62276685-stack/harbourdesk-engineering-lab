# 09.2 — Implement retry eligibility and stable request identity

**Role:** Integration software engineer

**Purpose:** Bound payment retries without increasing duplicate-charge risk.

**Stakeholder:** Payments integration reviewer.

## Task description

Implement the permanent-failure stop, fixed operation key and attempt limit, then deliver the bounded first part of the retry policy with deterministic call-trace checks.

## Final deliverable

- `retry-identity.patch`
- `retry-call-audit.ods`
- `retry-identity-checks.md`

## Quality checks

- [ ] A permanent failure stops after one call.
- [ ] All attempts for one operation retain the same nonempty key.
- [ ] At most three calls occur.
- [ ] The delivered patch states that deadline/backoff integration is the next bounded piece, not falsely complete.

**Apps:** Visual Studio Code, GitHub Desktop, LibreOffice.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

**Starting dependency:** The provided retry contract supplies the rules; [09.1](../09.1/GOAL.md) may be included as a frozen design input.

## Workflow

1. Edit only retry eligibility, request identity and call-count behavior in VS Code.
2. Use fake provider scripts to inspect permanent failure, eventual success and exhausted calls.
3. Review the patch in GitHub Desktop and create a LibreOffice call/key audit table for the integration reviewer.
