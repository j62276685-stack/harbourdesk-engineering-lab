# 17.1 — Review the proposed refund conversion change

**Role:** Senior software engineer reviewing a change

**Purpose:** Assess whether a refund change preserves the published amount contract.

**Stakeholder:** Pull-request author and payments engineering lead.

## Task description

I am investigating whether a proposed refund conversion change preserves the published amount contract. My goal is to provide the pull-request author and payments engineering lead with a prioritized review, a minimal demonstration of any consequential defect and a justified approval recommendation.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `refund-review-findings.ods`
- `refund-pr-review.pdf`
- `refund-review-demonstration.md`

## Quality checks

- [ ] At least one consequential finding has an exact line, trigger and expected/actual result.
- [ ] The finding addresses the minor-unit contract and compatibility claim.
- [ ] Legitimate inputs and blocker versus optional feedback are distinguished.
- [ ] No real PR comment is posted or full replacement solution implemented.

**Apps:** Visual Studio Code, GitHub Desktop, LibreOffice.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

## Workflow

1. Compare the baseline/proposed revision in GitHub Desktop and inspect the candidate source in VS Code.
2. Run a minimal comparison plus legitimate inputs; record expected/actual values and severity in LibreOffice.
3. Export the source-linked review with the exact candidate lines and a reasoned decision.
