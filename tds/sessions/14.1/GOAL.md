# 14.1 — Specify notification events, recipients and channel rules

**Role:** Software requirements engineer

**Purpose:** Turn a vague notification request into implementable rules.

**Stakeholder:** Product manager, support lead and implementation team.

## Task description

I am investigating a product request to notify customers about order changes without sending unnecessary messages. My goal is to provide the product manager, support lead and implementation team with clear event, recipient and channel rules that resolve the supplied stakeholder conflicts.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `notification-rules.ods`
- `notification-routing.drawio`
- `notification-rules.pdf`

## Quality checks

- [ ] Paid/cancelled/fulfilled/refunded and operator conflict events are covered.
- [ ] Required transactional messages and optional marketing are distinguished.
- [ ] Missing contact information and timezone/quiet hours have explicit behavior.
- [ ] The matrix states dedupe identity, retention assumption and privacy boundary.

**Apps:** Visual Studio Code, LibreOffice, draw.io Desktop.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

## Workflow

1. Inspect the supplied events/preferences and stakeholder notes in VS Code.
2. Build the channel/recipient/consent/quiet-hour matrix in Calc, labelling provisional choices.
3. Draw routing and deduplication boundaries, then export the requirements handoff.

## Recording script

Open the [Task 14 workspace](../../workspaces/14-notification-requirements.code-workspace) in VS Code. Run commands from its Application terminal; keep that terminal open. Follow the steps in order. Inputs and source: [task brief](../../tasks/14-notification-requirements/BRIEF.md), [event-catalog.json](../../tasks/14-notification-requirements/inputs/event-catalog.json), [preferences.json](../../tasks/14-notification-requirements/inputs/preferences.json), [stakeholder-notes.md](../../tasks/14-notification-requirements/inputs/stakeholder-notes.md), [notification_policy.py](../../../app/notification_policy.py).

1. **Set up the session and output folder.** Copy the report template only if a report does not already exist.

```sh
./tds/lab start 14 --session 14.1
mkdir -p tds/tasks/14-notification-requirements/outcomes/14.1
cp -n tds/docs/REPORT-TEMPLATE.md tds/tasks/14-notification-requirements/outcomes/14.1/report.md
git status --short
```

2. **Reproduce and capture the baseline.** Open the stakeholder notes, event catalog, preferences, and current notification policy. Mark each explicit rule versus an assumption.

3. **Investigate and create the deliverable.** In Calc map event, recipient, transactional/optional type, channel, opt-out, quiet hours with timezone, missing contact, timing, and deduplication key. In draw.io show routing and the boundary before a delivery request.

4. **Verify the result.** Review every input example against the matrix. Export the rules and list unresolved product choices with a provisional default where justified.

5. **Save and review the handoff.** Finish `report.md` in `tds/tasks/14-notification-requirements/outcomes/14.1/`. Save or export `notification-rules.ods`, `notification-routing.drawio`, `notification-rules.pdf` to the same folder using the named apps. Reopen every output, check the quality boxes above, and confirm the folder contents:

```sh
ls -lh tds/tasks/14-notification-requirements/outcomes/14.1
git status --short
```

Keep the short introduction and complete on-screen process within 15:00–45:59. Narrate what, where, and why; keep task content visible and do not show AI interaction during the recording.
