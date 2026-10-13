# 16.2 — Refactor one billing path against a frozen safety matrix

**Role:** Software maintenance engineer

**Purpose:** Make billing code easier to maintain while preserving pricing behavior.

**Stakeholder:** Billing-module maintainer.

## Task description

I am investigating how to simplify the billing module without changing established invoice totals. My goal is to provide the maintainer with a focused refactor and evidence of compatibility against the recorded characterization checks and input sample.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `billing-refactor.patch`
- `billing-equivalence.ods`
- `billing-refactor-rationale.md`

## Quality checks

- [ ] The public entry point remains compatible.
- [ ] The calculation order and frozen outputs are unchanged.
- [ ] Equivalence includes a broader sample and threshold/rounding cases.
- [ ] The rationale identifies a maintenance improvement with no unrelated pricing change.

**Apps:** Visual Studio Code, GitHub Desktop, LibreOffice.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

**Starting dependency:** Frozen baseline outputs/checks from [16.1](../16.1/GOAL.md) are required. Do not characterize only the already-refactored code.

## Workflow

1. Choose one internal responsibility boundary and refactor it in VS Code.
2. Run the frozen cases and broader sample; compare outputs and calculations in LibreOffice.
3. Review the diff and interface contract in GitHub Desktop, then export the patch and design note.

## Recording script

Open the [Task 16 workspace](../../workspaces/16-behavior-refactor.code-workspace) in VS Code. Run commands from its Application terminal; keep that terminal open. Follow the steps in order. Inputs and source: [task brief](../../tasks/16-behavior-refactor/BRIEF.md), [billing-contract.md](../../tasks/16-behavior-refactor/inputs/billing-contract.md), [characterization-cases.json](../../tasks/16-behavior-refactor/inputs/characterization-cases.json), [billing.py](../../../app/billing.py).

1. **Set up the session and output folder.** Copy the report template only if a report does not already exist.

```sh
./tds/lab start 16 --session 16.2
mkdir -p tds/tasks/16-behavior-refactor/outcomes/16.2
cp -n tds/docs/REPORT-TEMPLATE.md tds/tasks/16-behavior-refactor/outcomes/16.2/report.md
git status --short
```

2. **Reproduce and capture the baseline.** Start from the frozen characterization matrix and run it on the unchanged billing function.

Run the baseline commands in the Application terminal:

```sh
./tds/lab probe 16
```

3. **Investigate and create the deliverable.** Refactor one internal responsibility in app/billing.py while keeping invoice_total and the exact membership, coupon, courier, zero-floor, and tax order. Do not simplify away an awkward legacy rule without evidence.

4. **Verify the result.** Run the frozen tests and a broader deterministic sample. In Calc compare old/new outputs and explain the readability improvement; review the focused diff.

Run the verification commands:

```sh
./tds/lab test
```

Before committing this session’s code, export the reviewed change as the required patch:

```sh
git add -N -- tests
git diff HEAD --binary -- app/billing.py tests > tds/tasks/16-behavior-refactor/outcomes/16.2/billing-refactor.patch
```

5. **Save and review the handoff.** Finish `report.md` in `tds/tasks/16-behavior-refactor/outcomes/16.2/`. Save or export `billing-equivalence.ods`, `billing-refactor-rationale.md` to the same folder using the named apps. Reopen every output, check the quality boxes above, and confirm the folder contents:

```sh
ls -lh tds/tasks/16-behavior-refactor/outcomes/16.2
git status --short
```

Keep the short introduction and complete on-screen process within 15:00–45:59. Narrate what, where, and why; keep task content visible and do not show AI interaction during the recording.
