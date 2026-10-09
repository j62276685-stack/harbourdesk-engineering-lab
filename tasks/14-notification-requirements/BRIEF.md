# Task 14: Turn a notification request into precise requirements

## Error or request

Product asks: “Notify people when orders change, but don’t spam them.” Produce a specification that engineers and QA can implement and evaluate. Conflicting stakeholder preferences are provided.

## Relevant files

[inputs/stakeholder-notes.md](inputs/stakeholder-notes.md); [event-catalog.json](inputs/event-catalog.json); [preferences.json](inputs/preferences.json); [app/notification_policy.py](../../app/notification_policy.py).

- [event-catalog.json](inputs/event-catalog.json)
- [preferences.json](inputs/preferences.json)
- [stakeholder-notes.md](inputs/stakeholder-notes.md)

## Reproduce or investigate

From the project root, run `./lab start 14`. Open the printed folder. Run `./lab serve` for browser work or `./lab test` for tests. Inputs are copied to `evidence/inputs/`.

Read the notes and examples. Identify decisions required from product, then select explicit provisional defaults where the notes allow them. Do not contact stakeholders or build delivery integration.

## Completion criteria

1. Define triggering events, recipients, channels, preference/consent behavior, payload privacy and timing.
2. Specify duplicate and out-of-order handling with a deduplication identity and retention window.
3. Separate required/transactional messages from optional marketing and address quiet hours with a timezone.
4. Provide at least eight Given/When/Then acceptance examples covering paid, cancelled, refund, fulfilment, duplicates, opt-out, quiet hours and missing contact data.
5. List unresolved choices, their effect and a concrete default/assumption so an implementation can proceed when reasonable.

## Deliverable

outcomes/notification-spec.md with an event/recipient/channel table, acceptance scenarios and decision log. A completed coding solution is not required.

## Task sessions

Choose a session below for its scope, apps, outputs and checks.

- [14.1 — Specify notification events, recipients and channel rules](../../sessions/14.1/GOAL.md)
- [14.2 — Turn notification policy into an acceptance specification](../../sessions/14.2/GOAL.md)
