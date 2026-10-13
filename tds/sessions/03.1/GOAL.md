# 03.1 — Reconstruct one incident and its evidence limits

**Role:** Site reliability engineer

**Purpose:** Give operations an evidence-backed account of a receipt incident.

**Stakeholder:** Incident commander and customer-support lead.

## Task description

I am investigating a morning incident in which customers received duplicate receipts. My goal is to provide the incident commander and support lead with a source-linked timeline and a clear explanation of what the evidence establishes and what remains uncertain.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `incident-evidence.ods`
- `incident-timeline.drawio`
- `incident-summary.pdf`

## Quality checks

- [ ] Each material event has a source row/line and normalized UTC time.
- [ ] Minute aggregates are not treated as individual events.
- [ ] Facts, inference and missing evidence are visibly differentiated.
- [ ] The summary does not equate repeated event delivery with duplicate settlement.

**Apps:** Visual Studio Code, LibreOffice, draw.io Desktop.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

## Workflow

1. Inspect raw records and source reliability notes in VS Code.
2. Build a bounded evidence/timestamp table in LibreOffice Calc; normalize timezone and clock differences.
3. Draw the incident sequence with basic shapes, then export a one-page summary with unresolved questions.

## Recording script

Open the [Task 03 workspace](../../workspaces/03-incident-timeline.code-workspace) in VS Code. Run commands from its Application terminal; keep that terminal open. Follow the steps in order. Inputs and source: [task brief](../../tasks/03-incident-timeline/BRIEF.md), [deploy.txt](../../tasks/03-incident-timeline/inputs/deploy.txt), [metrics.csv](../../tasks/03-incident-timeline/inputs/metrics.csv), [provider.csv](../../tasks/03-incident-timeline/inputs/provider.csv), [proxy.log](../../tasks/03-incident-timeline/inputs/proxy.log), [service.jsonl](../../tasks/03-incident-timeline/inputs/service.jsonl), [source-notes.md](../../tasks/03-incident-timeline/inputs/source-notes.md), [support.txt](../../tasks/03-incident-timeline/inputs/support.txt).

1. **Set up the session and output folder.** Copy the report template only if a report does not already exist.

```sh
./tds/lab start 03 --session 03.1
mkdir -p tds/tasks/03-incident-timeline/outcomes/03.1
cp -n tds/docs/REPORT-TEMPLATE.md tds/tasks/03-incident-timeline/outcomes/03.1/report.md
git status --short
```

2. **Reproduce and capture the baseline.** Open all seven supplied incident sources in VS Code. Note their source row or line and original timestamp; read source-notes.md before converting any times.

3. **Investigate and create the deliverable.** In Calc build columns for original time, UTC time, source location, event ID, observation, inference, and uncertainty. Adjust the proxy clock using the health-check offset; treat metrics as minute buckets. In draw.io map the sequence and mark the missing log interval.

4. **Verify the result.** Check every material timeline row against its source. Export the one-page summary without claiming that delivery attempts prove multiple settlements.

5. **Save and review the handoff.** Finish `report.md` in `tds/tasks/03-incident-timeline/outcomes/03.1/`. Save or export `incident-evidence.ods`, `incident-timeline.drawio`, `incident-summary.pdf` to the same folder using the named apps. Reopen every output, check the quality boxes above, and confirm the folder contents:

```sh
ls -lh tds/tasks/03-incident-timeline/outcomes/03.1
git status --short
```

Keep the short introduction and complete on-screen process within 15:00–45:59. Narrate what, where, and why; keep task content visible and do not show AI interaction during the recording.
