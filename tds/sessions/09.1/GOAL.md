# 09.1 — Design the bounded charge-retry decision table

**Role:** Integration software engineer

**Purpose:** Bound payment retries without increasing duplicate-charge risk.

**Stakeholder:** Payments integration reviewer.

## Task description

I am investigating payment retries that can continue unnecessarily or use changing request keys. My goal is to provide the integration reviewer with an implementable retry policy that defines eligible failures, stable request identity and a bounded time budget.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `retry-decision-table.ods`
- `retry-state-route.drawio`
- `retry-policy.pdf`

## Quality checks

- [ ] Eligible/permanent statuses match the supplied contract.
- [ ] Three calls and the eight-second envelope include request duration and waits.
- [ ] Retry-After validity/cap and stable idempotency identity are specified.
- [ ] Final timeout is not described as proof of no charge.

**Apps:** Visual Studio Code, LibreOffice, draw.io Desktop.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

## Workflow

1. Inspect provider call shape and scripted durations in VS Code.
2. In Calc build the eligibility, stable-key, attempt and wait-budget matrix.
3. Draw the stop/retry decision route and export the policy with timeout ambiguity.

## Recording script

Open the [Task 09 workspace](../../workspaces/09-retry-policy.code-workspace) in VS Code. Run commands from its Application terminal; keep that terminal open. Follow the steps in order. Inputs and source: [task brief](../../tasks/09-retry-policy/BRIEF.md), [provider-scripts.json](../../tasks/09-retry-policy/inputs/provider-scripts.json), [retry-contract.md](../../tasks/09-retry-policy/inputs/retry-contract.md), [retries.py](../../../app/retries.py), [provider.py](../../../app/provider.py).

1. **Set up the session and output folder.** Copy the report template only if a report does not already exist.

```sh
./tds/lab start 09 --session 09.1
mkdir -p tds/tasks/09-retry-policy/outcomes/09.1
cp -n tds/docs/REPORT-TEMPLATE.md tds/tasks/09-retry-policy/outcomes/09.1/report.md
git status --short
```

2. **Reproduce and capture the baseline.** Run the retry probe and read the retry contract and scripted provider durations. Observe the current attempt keys and waits.

Run the baseline commands in the Application terminal:

```sh
./tds/lab probe 9
```

3. **Investigate and create the deliverable.** In Calc build rows for eligible statuses, permanent decline, malformed Retry-After, attempt limit, stable key, and the eight-second budget including call duration. Draw the stop/retry/status-check route; a timeout leaves charge outcome uncertain.

4. **Verify the result.** Check the table against the contract and export a policy with the exact stop conditions and bounded timing examples.

5. **Save and review the handoff.** Finish `report.md` in `tds/tasks/09-retry-policy/outcomes/09.1/`. Save or export `retry-decision-table.ods`, `retry-state-route.drawio`, `retry-policy.pdf` to the same folder using the named apps. Reopen every output, check the quality boxes above, and confirm the folder contents:

```sh
ls -lh tds/tasks/09-retry-policy/outcomes/09.1
git status --short
```

Keep the short introduction and complete on-screen process within 15:00–45:59. Narrate what, where, and why; keep task content visible and do not show AI interaction during the recording.
