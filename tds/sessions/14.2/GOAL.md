# 14.2 — Turn notification policy into an acceptance specification

**Role:** Software requirements engineer

**Purpose:** Turn a vague notification request into implementable rules.

**Stakeholder:** Product manager, support lead and implementation team.

## Task description

I am investigating ambiguities in the proposed order-notification policy using eight edge scenarios. My goal is to provide QA and the implementation team with a testable acceptance specification that makes each notification decision explicit.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `notification-acceptance.ods`
- `notification-acceptance-flow.drawio`
- `notification-qa-spec.pdf`

## Quality checks

- [ ] Eight named scenario groups in the original brief are covered.
- [ ] Each expected outcome is grounded in a rule or explicit assumption.
- [ ] Duplicate/out-of-order behavior is testable.
- [ ] Unresolved product choices have an impact and concrete provisional default.

**Apps:** Visual Studio Code, LibreOffice, draw.io Desktop.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

**Starting dependency:** A frozen [14.1](../14.1/GOAL.md) policy is required, or use the supplied stakeholder notes as an intentionally incomplete draft policy and clearly mark that boundary.

## Workflow

1. Cross-check policy statements against the supplied event and preference examples.
2. Complete eight Given/When/Then cases in LibreOffice and identify missing or conflicting behavior.
3. Update the decision-flow diagram for the clarified rules and export the QA specification.

## Recording script

Open the [Task 14 workspace](../../workspaces/14-notification-requirements.code-workspace) in VS Code. Run commands from its Application terminal; keep that terminal open. Follow the steps in order. Inputs and source: [task brief](../../tasks/14-notification-requirements/BRIEF.md), [event-catalog.json](../../tasks/14-notification-requirements/inputs/event-catalog.json), [preferences.json](../../tasks/14-notification-requirements/inputs/preferences.json), [stakeholder-notes.md](../../tasks/14-notification-requirements/inputs/stakeholder-notes.md), [notification_policy.py](../../../app/notification_policy.py).

1. **Set up the session and output folder.** Copy the report template only if a report does not already exist.

```sh
./tds/lab start 14 --session 14.2
mkdir -p tds/tasks/14-notification-requirements/outcomes/14.2
cp -n tds/docs/REPORT-TEMPLATE.md tds/tasks/14-notification-requirements/outcomes/14.2/report.md
git status --short
```

2. **Reproduce and capture the baseline.** Use the frozen notification rule table or the supplied notes; check the event and preference examples before drafting tests.

3. **Investigate and create the deliverable.** In Calc write at least eight Given/When/Then cases for paid, cancelled, refund, fulfilment, duplicate, opt-out, quiet hours, and missing contact. Add expected recipient/channel/payload and whether delivery is suppressed. Update the decision diagram.

4. **Verify the result.** Ensure each case has an observable result and that unknown policy choices are stated rather than silently invented. Export the QA specification.

5. **Save and review the handoff.** Finish `report.md` in `tds/tasks/14-notification-requirements/outcomes/14.2/`. Save or export `notification-acceptance.ods`, `notification-acceptance-flow.drawio`, `notification-qa-spec.pdf` to the same folder using the named apps. Reopen every output, check the quality boxes above, and confirm the folder contents:

```sh
ls -lh tds/tasks/14-notification-requirements/outcomes/14.2
git status --short
```

Keep the short introduction and complete on-screen process within 15:00–45:59. Narrate what, where, and why; keep task content visible and do not show AI interaction during the recording.
