# 18.2 — Resolve the delivery conflict and verify both parent changes

**Role:** Software integration engineer

**Purpose:** Combine delivery-price changes without losing either business requirement.

**Stakeholder:** Delivery product owner and release maintainer.

## Task description

I am investigating how to resolve the delivery-pricing conflict without losing either branch’s requirements. My goal is to provide the release maintainer with a completed local merge, passing checks for both pricing rules and a clear record of the resolution.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `delivery-merge-results.ods`
- `delivery-merge-checks.md`
- `delivery-merged.patch`

## Quality checks

- [ ] Local below/at threshold and remote below/above cases are correct.
- [ ] Both sets of branch tests and the baseline suite pass.
- [ ] No conflict markers remain.
- [ ] The completed local merge has both branch tips as parents.

**Apps:** Visual Studio Code, GitHub Desktop, LibreOffice.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

**Starting dependency:** [18.1](../18.1/GOAL.md) is optional; the supplied branch-intent document defines the combined rule.

## Workflow

1. Resolve the bounded source conflict in VS Code against the supplied branch intent.
2. Run both branch tests and inspect the resolved change/merge completion in GitHub Desktop.
3. Complete the boundary/results matrix in LibreOffice and export the merge proof and decision note.

## Recording script

Open the [Task 18 workspace](../../workspaces/18-merge-intent.code-workspace) in VS Code. Run commands from its Application terminal; keep that terminal open. Follow the steps in order. Inputs and source: [task brief](../../tasks/18-merge-intent/BRIEF.md), [branch-intent.md](../../tasks/18-merge-intent/inputs/branch-intent.md), [shipping.py](../../../app/shipping.py).

1. **Set up the session and output folder.** Copy the report template only if a report does not already exist.

```sh
./tds/lab start 18 --session 18.2
mkdir -p tds/tasks/18-merge-intent/outcomes/18.2
cp -n tds/docs/REPORT-TEMPLATE.md tds/tasks/18-merge-intent/outcomes/18.2/report.md
git status --short
```

2. **Reproduce and capture the baseline.** Continue the conflict prepared in 18.1. If starting independently, commit earlier application changes and run `./tds/lab setup-merge` once before these commands. Inspect both branch tips and generated tests.

Run the baseline commands in the Application terminal:

```sh
git status --short
git show free-delivery:app/shipping.py
git show remote-delivery:app/shipping.py
```

3. **Investigate and create the deliverable.** Resolve app/shipping.py so remote always costs 3000; local below 25000 costs 1500 and local at/above costs zero. Remove conflict markers and keep both test files. Add combined boundary checks if needed.

4. **Verify the result.** Run both branch tests and the full suite, then stage the resolved source and complete the merge commit. Check that the final commit has two parents and export a first-parent diff.

Run the verification commands:

```sh
python3 -m unittest discover -s tests -p "test_*delivery.py" -v
./tds/lab test
git add app/shipping.py tests/test_local_delivery.py tests/test_remote_delivery.py
git commit -m "Combine local threshold and remote delivery rules"
git rev-list --parents -n 1 HEAD
```

After the merge commit, export the reviewed first-parent change as the required patch:

```sh
git diff --binary HEAD^1 HEAD -- app/shipping.py tests > tds/tasks/18-merge-intent/outcomes/18.2/delivery-merged.patch
```

5. **Save and review the handoff.** Finish `report.md` in `tds/tasks/18-merge-intent/outcomes/18.2/`. Save or export `delivery-merge-results.ods`, `delivery-merge-checks.md` to the same folder using the named apps. Reopen every output, check the quality boxes above, and confirm the folder contents:

```sh
ls -lh tds/tasks/18-merge-intent/outcomes/18.2
git status --short
```

Keep the short introduction and complete on-screen process within 15:00–45:59. Narrate what, where, and why; keep task content visible and do not show AI interaction during the recording.
