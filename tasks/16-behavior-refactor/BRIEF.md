# Task 16: Refactor a difficult module while preserving behavior

## Error or request

I am investigating a billing module that is difficult to maintain without risking pricing changes. My goal is to provide the maintainer with a simpler implementation and evidence that its established calculation order, rounding and outputs are preserved.

## Relevant files

[app/billing.py](../../app/billing.py); [inputs/billing-contract.md](inputs/billing-contract.md); [characterization-cases.json](inputs/characterization-cases.json).

- [billing-contract.md](inputs/billing-contract.md)
- [characterization-cases.json](inputs/characterization-cases.json)

## Reproduce or investigate

Open the [Task 16 workspace](../../workspaces/16-behavior-refactor.code-workspace). It uses the shared application and database. Read the inputs above. Run `./lab serve` for browser work or `./lab test` for tests.

Run `./lab probe 16`. Capture behavior for the supplied cases and additional threshold/rounding boundaries before changing code. Some legacy rules are awkward; this exercise preserves them.

## Completion criteria

1. Keep invoice_total as a compatible entry point and preserve outputs across the documented input domain.
2. Maintain the exact order of membership discount, coupon, courier fee, zero floor and tax rounding.
3. Show characterization checks around 10000 and 15000 thresholds, tiny values and tax-rounding ties.
4. Provide a clearer internal interface and remove unnecessary branching without adding a third-party framework.
5. Explain the design improvement and show a broader equivalence sample beyond the supplied examples.

## Deliverable

Focused refactor, characterization/equivalence evidence and design rationale. Changing product pricing is outside scope.

## Task sessions

Choose a session below for its scope, apps, outputs and checks.

- [16.1 — Capture a billing characterization contract at the boundaries](../../sessions/16.1/GOAL.md)
- [16.2 — Refactor one billing path against a frozen safety matrix](../../sessions/16.2/GOAL.md)
