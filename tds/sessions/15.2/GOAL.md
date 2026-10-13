# 15.2 — Enforce and verify the bounded lifecycle transition contract

**Role:** Backend domain engineer

**Purpose:** Make order transitions predictable and enforceable.

**Stakeholder:** Fulfilment product owner and QA team.

## Task description

I am investigating the transition code that allows orders to move outside the agreed lifecycle. My goal is to provide the fulfilment and QA teams with a verified repair that enforces allowed transitions and preserves order history and version values when a request is rejected.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `order-lifecycle.patch`
- `order-state-evidence.csv`
- `order-lifecycle-checks.md`

## Quality checks

- [ ] All known state pairs agree with the supplied contract.
- [ ] New accepted changes increment once; rejected/no-op requests do not.
- [ ] Unknown target, forbidden pair and ownership errors are distinct as specified.
- [ ] A legitimate flow and cancelled terminal state are checked.

**Apps:** Visual Studio Code, DB Browser for SQLite, GitHub Desktop.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

**Starting dependency:** The supplied lifecycle contract is sufficient; [15.1](../15.1/GOAL.md) may be included as a frozen visual specification.

## Workflow

1. Implement the declared transition table and focused matrix checks in VS Code.
2. Run legitimate/forbidden/no-op cases and inspect persisted version/status with DB Browser.
3. Review the diff in GitHub Desktop and export the transition checks and patch.

## Recording script

Open the [Task 15 workspace](../../workspaces/15-order-lifecycle.code-workspace) in VS Code. Run commands from its Application terminal; keep that terminal open. Follow the steps in order. Inputs and source: [task brief](../../tasks/15-order-lifecycle/BRIEF.md), [examples.json](../../tasks/15-order-lifecycle/inputs/examples.json), [lifecycle-contract.md](../../tasks/15-order-lifecycle/inputs/lifecycle-contract.md), [orders.py](../../../app/orders.py), [schema.sql](../../../app/schema.sql).

1. **Set up the session and output folder.** Copy the report template only if a report does not already exist.

```sh
./tds/lab start 15 --session 15.2
mkdir -p tds/tasks/15-order-lifecycle/outcomes/15.2
cp -n tds/docs/REPORT-TEMPLATE.md tds/tasks/15-order-lifecycle/outcomes/15.2/report.md
git status --short
```

2. **Reproduce and capture the baseline.** Run the lifecycle probe and record order status/version before a forbidden and same-state request.

Run the baseline commands in the Application terminal:

```sh
./tds/lab probe 15
```

3. **Investigate and create the deliverable.** In app/orders.py enforce the supplied transition table at the service boundary. Same-state calls return without a version bump; known forbidden pairs return 409, unknown targets 400, and unowned/unknown IDs 404. Add a seven-by-seven matrix test.

4. **Verify the result.** Run the probe and suite. In DB Browser verify accepted changes increment once while forbidden and no-op requests do not mutate rows; review the patch.

Run the verification commands:

```sh
./tds/lab probe 15
./tds/lab test
```

Before committing this session’s code, export the reviewed change as the required patch:

```sh
git add -N -- tests
git diff HEAD --binary -- app/orders.py tests > tds/tasks/15-order-lifecycle/outcomes/15.2/order-lifecycle.patch
```

5. **Save and review the handoff.** Finish `report.md` in `tds/tasks/15-order-lifecycle/outcomes/15.2/`. Save or export `order-state-evidence.csv`, `order-lifecycle-checks.md` to the same folder using the named apps. Reopen every output, check the quality boxes above, and confirm the folder contents:

```sh
ls -lh tds/tasks/15-order-lifecycle/outcomes/15.2
git status --short
```

Keep the short introduction and complete on-screen process within 15:00–45:59. Narrate what, where, and why; keep task content visible and do not show AI interaction during the recording.
