# 20.1 — Write a defensible disputed-charge memo

**Role:** Incident analyst with backend expertise

**Purpose:** Answer a disputed-charge question without overstating incomplete evidence.

**Stakeholder:** Operations manager and customer-support lead.

## Task description

I am investigating a report that a disputed order may have been paid twice. My goal is to provide the operations manager and support lead with the strongest conclusion the incomplete evidence supports and a concrete plan to distinguish the remaining explanations.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `disputed-charge-evidence.ods`
- `settlement-investigation.drawio`
- `disputed-charge-memo.pdf`

## Quality checks

- [ ] The conclusion is bounded by the actual supplied evidence.
- [ ] At least two explanations are consistent with the fragments.
- [ ] The next observation specifies source, identifiers, time range and distinguishing outcomes.
- [ ] Current starter behavior and missing fragment lines are not treated as historical settlement proof.

**Apps:** Visual Studio Code, LibreOffice, draw.io Desktop.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

## Workflow

1. Inspect only the supplied historical fragments in VS Code and identify their reliability limits.
2. Build a fact/hypothesis/evidence-gap table in LibreOffice.
3. Draw a two-hypothesis decision tree with discriminating observations and export the manager memo.

## Recording script

Open the [Task 20 workspace](../../workspaces/20-bounded-uncertainty.code-workspace) in VS Code. Run commands from its Application terminal; keep that terminal open. Follow the steps in order. Inputs and source: [task brief](../../tasks/20-bounded-uncertainty/BRIEF.md), [app-fragment.jsonl](../../tasks/20-bounded-uncertainty/inputs/app-fragment.jsonl), [evidence-limits.md](../../tasks/20-bounded-uncertainty/inputs/evidence-limits.md), [manager-question.txt](../../tasks/20-bounded-uncertainty/inputs/manager-question.txt), [provider-summary.csv](../../tasks/20-bounded-uncertainty/inputs/provider-summary.csv), [support-note.txt](../../tasks/20-bounded-uncertainty/inputs/support-note.txt).

1. **Set up the session and output folder.** Copy the report template only if a report does not already exist.

```sh
./tds/lab start 20 --session 20.1
mkdir -p tds/tasks/20-bounded-uncertainty/outcomes/20.1
cp -n tds/docs/REPORT-TEMPLATE.md tds/tasks/20-bounded-uncertainty/outcomes/20.1/report.md
git status --short
```

2. **Reproduce and capture the baseline.** Open only the supplied historical fragments and evidence-limits note. Do not use the current interactive app as evidence of the historical settlement.

3. **Investigate and create the deliverable.** In Calc separate request attempts, delivery attempts, local payment rows, and confirmed settled charges. Give two explanations consistent with the fragments; in draw.io show the exact missing observation that would distinguish them.

4. **Verify the result.** Write the strongest supported conclusion and a read-only next-data request with source, identifiers, and time range. Export the memo without a fabricated yes/no settlement answer.

5. **Save and review the handoff.** Finish `report.md` in `tds/tasks/20-bounded-uncertainty/outcomes/20.1/`. Save or export `disputed-charge-evidence.ods`, `settlement-investigation.drawio`, `disputed-charge-memo.pdf` to the same folder using the named apps. Reopen every output, check the quality boxes above, and confirm the folder contents:

```sh
ls -lh tds/tasks/20-bounded-uncertainty/outcomes/20.1
git status --short
```

Keep the short introduction and complete on-screen process within 15:00–45:59. Narrate what, where, and why; keep task content visible and do not show AI interaction during the recording.
