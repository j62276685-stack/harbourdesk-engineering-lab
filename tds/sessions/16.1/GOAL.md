# 16.1 — Capture a billing characterization contract at the boundaries

**Role:** Software maintenance engineer

**Purpose:** Make billing code easier to maintain while preserving pricing behavior.

**Stakeholder:** Billing-module maintainer.

## Task description

I am investigating a billing module whose calculation order and rounding rules are difficult to follow. My goal is to provide the maintainer with executable characterization checks and a safety matrix that defines the pricing behavior a refactor must preserve.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
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

## Recording script

Open the [Task 16 workspace](../../workspaces/16-behavior-refactor.code-workspace) in VS Code. Run commands from its Application terminal; keep that terminal open. Follow the steps in order. Inputs and source: [task brief](../../tasks/16-behavior-refactor/BRIEF.md), [billing-contract.md](../../tasks/16-behavior-refactor/inputs/billing-contract.md), [characterization-cases.json](../../tasks/16-behavior-refactor/inputs/characterization-cases.json), [billing.py](../../../app/billing.py).

1. **Set up the session and output folder.** Copy the report template only if a report does not already exist.

```sh
./tds/lab start 16 --session 16.1
mkdir -p tds/tasks/16-behavior-refactor/outcomes/16.1
cp -n tds/docs/REPORT-TEMPLATE.md tds/tasks/16-behavior-refactor/outcomes/16.1/report.md
git status --short
```

2. **Reproduce and capture the baseline.** Run the billing probe and read the contract plus characterization-cases.json before editing app/billing.py.

Run the baseline commands in the Application terminal:

```sh
./tds/lab probe 16
```

3. **Investigate and create the deliverable.** In Calc independently compute boundaries around 10000 and 15000, small amounts, membership, coupon, courier, and tax rounding. Add tests that freeze the current invoice_total output and order of operations without changing pricing.

4. **Verify the result.** Run the suite, review only the new tests in GitHub Desktop, and save the frozen safety contract with observed values.

Run the verification commands:

```sh
./tds/lab test
```

Before committing this session’s code, export the reviewed change as the required patch:

```sh
git add -N -- tests
git diff HEAD --binary -- tests > tds/tasks/16-behavior-refactor/outcomes/16.1/billing-characterization.patch
```

5. **Save and review the handoff.** Finish `report.md` in `tds/tasks/16-behavior-refactor/outcomes/16.1/`. Save or export `billing-characterization.ods`, `billing-safety-contract.md` to the same folder using the named apps. Reopen every output, check the quality boxes above, and confirm the folder contents:

```sh
ls -lh tds/tasks/16-behavior-refactor/outcomes/16.1
git status --short
```

Keep the short introduction and complete on-screen process within 15:00–45:59. Narrate what, where, and why; keep task content visible and do not show AI interaction during the recording.
