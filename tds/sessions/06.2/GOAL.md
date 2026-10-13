# 06.2 — Implement and verify one error-classification contract

**Role:** Payments integration engineer

**Purpose:** Give customers accurate failure messages and support usable error categories.

**Stakeholder:** Payments support lead and checkout team.

## Task description

I am investigating the payment code that maps different provider failures to the same misleading response. My goal is to provide the checkout team with a verified classification repair and HTTP evidence that each supported failure receives the correct status and message.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `error-mapping.patch`
- `error-response-evidence.md`
- `error-check-results.json`

## Quality checks

- [ ] Defined statuses, machine codes and safe messages agree with the contract.
- [ ] Invalid local values cause no provider call.
- [ ] Success data is preserved and unexpected errors remain dependency errors.
- [ ] The change adds no retries or actual remote charge.

**Apps:** Visual Studio Code, Firefox, GitHub Desktop.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

**Starting dependency:** [06.1](../06.1/GOAL.md) is optional; the supplied API error table is the authoritative starting contract.

## Workflow

1. Implement the bounded mapping and provider-call assertions in VS Code.
2. Use Firefox Network’s Edit and Resend on a synthetic local request to compare selected API responses.
3. Run focused tests, inspect the diff in GitHub Desktop and export a verification note.
