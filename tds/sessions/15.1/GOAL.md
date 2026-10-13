# 15.1 — Model the seven-state order lifecycle for QA

**Role:** Backend domain engineer

**Purpose:** Make order transitions predictable and enforceable.

**Stakeholder:** Fulfilment product owner and QA team.

## Task description

I am investigating an order lifecycle that permits unclear or invalid state changes. My goal is to provide the fulfilment product owner and QA team with a state diagram and transition matrix defining allowed moves, repeated requests and error behavior.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `order-transition-matrix.ods`
- `order-lifecycle.drawio`
- `order-lifecycle-spec.pdf`

## Quality checks

- [ ] All seven states and every pair are classified.
- [ ] The diagram matches the permitted transitions.
- [ ] Same-state/version and error-code/ownership boundaries are explicit.
- [ ] Terminal states are represented correctly.

**Apps:** Visual Studio Code, LibreOffice, draw.io Desktop.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

## Workflow

1. Inspect the current transition source and supplied lifecycle contract.
2. Build the seven-by-seven allowed/forbidden/no-op matrix in Calc.
3. Draw the state diagram with terminal states and export the concise QA contract.

## Recording script

Open the [Task 15 workspace](../../workspaces/15-order-lifecycle.code-workspace) in VS Code. Run commands from its Application terminal; keep that terminal open. Follow the steps in order. Inputs and source: [task brief](../../tasks/15-order-lifecycle/BRIEF.md), [examples.json](../../tasks/15-order-lifecycle/inputs/examples.json), [lifecycle-contract.md](../../tasks/15-order-lifecycle/inputs/lifecycle-contract.md), [orders.py](../../../app/orders.py), [schema.sql](../../../app/schema.sql).

1. **Set up the session and output folder.** Copy the report template only if a report does not already exist.

```sh
./tds/lab start 15 --session 15.1
mkdir -p tds/tasks/15-order-lifecycle/outcomes/15.1
cp -n tds/docs/REPORT-TEMPLATE.md tds/tasks/15-order-lifecycle/outcomes/15.1/report.md
git status --short
```

2. **Reproduce and capture the baseline.** Run the lifecycle probe and read the seven-state contract and examples. Record current transition behavior before modeling.

Run the baseline commands in the Application terminal:

```sh
./tds/lab probe 15
```

3. **Investigate and create the deliverable.** In Calc fill all 49 source/target pairs: allowed change, same-state no-op, or forbidden. In draw.io mark allowed arrows and terminal cancelled/refunded states; note HTTP codes and version effects.

4. **Verify the result.** Cross-check every pair and export a QA contract that distinguishes unknown targets, forbidden known transitions, and ownership.

5. **Save and review the handoff.** Finish `report.md` in `tds/tasks/15-order-lifecycle/outcomes/15.1/`. Save or export `order-transition-matrix.ods`, `order-lifecycle.drawio`, `order-lifecycle-spec.pdf` to the same folder using the named apps. Reopen every output, check the quality boxes above, and confirm the folder contents:

```sh
ls -lh tds/tasks/15-order-lifecycle/outcomes/15.1
git status --short
```

Keep the short introduction and complete on-screen process within 15:00–45:59. Narrate what, where, and why; keep task content visible and do not show AI interaction during the recording.
