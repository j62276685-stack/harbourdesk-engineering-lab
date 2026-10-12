# Task 14: Turn a notification request into precise requirements

## Error or request

I am investigating a product request to notify customers about order changes without sending unnecessary messages. My goal is to provide the product and implementation teams with precise notification rules and testable acceptance criteria.

## Relevant files

[inputs/stakeholder-notes.md](inputs/stakeholder-notes.md); [event-catalog.json](inputs/event-catalog.json); [preferences.json](inputs/preferences.json); [app/notification_policy.py](../../app/notification_policy.py).

- [event-catalog.json](inputs/event-catalog.json)
- [preferences.json](inputs/preferences.json)
- [stakeholder-notes.md](inputs/stakeholder-notes.md)

## Reproduce or investigate

Open the [Task 14 workspace](../../workspaces/14-notification-requirements.code-workspace). It uses the shared application and database. Read the inputs above. Run `./lab serve` for browser work or `./lab test` for tests.

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
