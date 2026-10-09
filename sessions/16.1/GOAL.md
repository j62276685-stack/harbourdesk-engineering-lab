# 16.1 — Capture a billing characterization contract at the boundaries

**Role:** Software maintenance engineer

**Purpose:** Make billing code easier to maintain while preserving pricing behavior.

**Stakeholder:** Billing-module maintainer.

## Task description

Characterize the legacy billing order and selected threshold/rounding cases, then deliver a refactor safety matrix with executable checks.

## Final deliverable

- `billing-characterization.patch`
- `billing-characterization.ods`
- `billing-safety-contract.md`

## Quality checks

- [ ] Discount/coupon/delivery/zero-floor/tax order is explicit.
- [ ] 10000/15000 and tiny/rounding cases are included.
- [ ] Checks preserve observed legacy behavior rather than introducing new pricing.
- [ ] The test-only diff and input/output evidence are traceable.

**Apps:** Visual Studio Code, GitHub Desktop, LibreOffice.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

## Workflow

1. Inspect the baseline billing source and supplied input cases in VS Code.
2. Generate selected observations, independently check threshold/rounding calculations in LibreOffice, and write focused characterization checks.
3. Use GitHub Desktop to review only the new safety checks and save the characterization contract.
