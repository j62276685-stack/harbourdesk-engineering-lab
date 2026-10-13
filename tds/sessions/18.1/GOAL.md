# 18.1 — Recover both sides’ intent from the delivery conflict

**Role:** Software integration engineer

**Purpose:** Combine delivery-price changes without losing either business requirement.

**Stakeholder:** Delivery product owner and release maintainer.

## Task description

I am investigating a delivery-pricing conflict between free local delivery and a remote-region surcharge. My goal is to provide the product owner and release maintainer with the combined business rule, an acceptance matrix and a merge plan that preserves both changes.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `delivery-intent-matrix.ods`
- `delivery-merge-plan.pdf`
- `branch-evidence.md`

## Quality checks

- [ ] Both branches’ requirements and test contributions are identified.
- [ ] The threshold equality and remote high-subtotal case are specified.
- [ ] The plan explains why selecting either side wholesale would lose intent.
- [ ] The conflict remains an input; the deliverable is the completed review/plan.

**Apps:** Visual Studio Code, GitHub Desktop, LibreOffice.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

## Workflow

1. Inspect both branch histories/diffs in GitHub Desktop and the conflict/tests in VS Code.
2. Use LibreOffice to build the subtotal/region behavior matrix and combined requirement rationale.
3. Export a merge-intent handoff without resolving the source in this session.

## Recording script

Open the [Task 18 workspace](../../workspaces/18-merge-intent.code-workspace) in VS Code. Run commands from its Application terminal; keep that terminal open. Follow the steps in order. Inputs and source: [task brief](../../tasks/18-merge-intent/BRIEF.md), [branch-intent.md](../../tasks/18-merge-intent/inputs/branch-intent.md), [shipping.py](../../../app/shipping.py).

1. **Set up the session and output folder.** Copy the report template only if a report does not already exist.

```sh
./tds/lab start 18 --session 18.1
mkdir -p tds/tasks/18-merge-intent/outcomes/18.1
cp -n tds/docs/REPORT-TEMPLATE.md tds/tasks/18-merge-intent/outcomes/18.1/report.md
git status --short
```

2. **Reproduce and capture the baseline.** After previous work is committed, run setup-merge once. It leaves a real local conflict. Inspect git status and both branch versions in VS Code and GitHub Desktop.

Run the baseline commands in the Application terminal:

```sh
./tds/lab setup-merge
git status --short
git show free-delivery:app/shipping.py
git show remote-delivery:app/shipping.py
```

3. **Investigate and create the deliverable.** In Calc write the local/remote by below/at/above-threshold matrix: local below 25000 costs 1500, local at/above costs zero, remote always costs 3000. Identify which branch supplies each rule and which tests must survive.

4. **Verify the result.** Export the merge plan and branch evidence without resolving the conflict in this session.

5. **Save and review the handoff.** Finish `report.md` in `tds/tasks/18-merge-intent/outcomes/18.1/`. Save or export `delivery-intent-matrix.ods`, `delivery-merge-plan.pdf`, `branch-evidence.md` to the same folder using the named apps. Reopen every output, check the quality boxes above, and confirm the folder contents:

```sh
ls -lh tds/tasks/18-merge-intent/outcomes/18.1
git status --short
```

Keep the short introduction and complete on-screen process within 15:00–45:59. Narrate what, where, and why; keep task content visible and do not show AI interaction during the recording.
