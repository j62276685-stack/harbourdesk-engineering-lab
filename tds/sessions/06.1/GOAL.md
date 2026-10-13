# 06.1 — Specify a customer-safe provider error taxonomy

**Role:** Payments integration engineer

**Purpose:** Give customers accurate failure messages and support usable error categories.

**Stakeholder:** Payments support lead and checkout team.

## Task description

I am investigating why payment-provider failures are presented to customers as invalid amounts. My goal is to provide the payments support lead and checkout team with a clear classification table that distinguishes validation errors, declines, outages and timeouts.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `error-taxonomy.ods`
- `error-routing.drawio`
- `error-contract.pdf`

## Quality checks

- [ ] Bad local values and upstream failures are distinct.
- [ ] Outage, decline, timeout, unexpected response and success are covered.
- [ ] Raw upstream diagnostic text is not proposed as customer copy.
- [ ] Each classification follows API.md or explicitly records an unresolved choice.

**Apps:** Visual Studio Code, LibreOffice, draw.io Desktop.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

## Workflow

1. Observe the fixture cases with the VS Code task runner and inspect the current mapping.
2. Complete a classification table in Calc with HTTP code, machine code, safe message and source of responsibility.
3. Draw the decision route with basic shapes and export a short implementation handoff.

## Recording script

Open the [Task 06 workspace](../../workspaces/06-error-classification.code-workspace) in VS Code. Run commands from its Application terminal; keep that terminal open. Follow the steps in order. Inputs and source: [task brief](../../tasks/06-error-classification/BRIEF.md), [provider-cases.json](../../tasks/06-error-classification/inputs/provider-cases.json), [payments.py](../../../app/payments.py), [provider.py](../../../app/provider.py), [API.md](../../../docs/API.md).

1. **Set up the session and output folder.** Copy the report template only if a report does not already exist.

```sh
./tds/lab start 06 --session 06.1
mkdir -p tds/tasks/06-error-classification/outcomes/06.1
cp -n tds/docs/REPORT-TEMPLATE.md tds/tasks/06-error-classification/outcomes/06.1/report.md
git status --short
```

2. **Reproduce and capture the baseline.** Run the provider probe and read the public error table in docs/API.md beside provider-cases.json. Record actual status, machine code, safe message, and whether the stub was called.

Run the baseline commands in the Application terminal:

```sh
./tds/lab probe 6
```

3. **Investigate and create the deliverable.** In Calc create rows for invalid local amount, decline, outage, timeout, unexpected response, and success. Assign the contract’s HTTP and machine codes; mark customer-safe messages separately from raw upstream diagnostics. In draw.io show validation before the provider call.

4. **Verify the result.** Cross-check every row with the API contract. Export a short implementation handoff that records any unresolved category explicitly.

5. **Save and review the handoff.** Finish `report.md` in `tds/tasks/06-error-classification/outcomes/06.1/`. Save or export `error-taxonomy.ods`, `error-routing.drawio`, `error-contract.pdf` to the same folder using the named apps. Reopen every output, check the quality boxes above, and confirm the folder contents:

```sh
ls -lh tds/tasks/06-error-classification/outcomes/06.1
git status --short
```

Keep the short introduction and complete on-screen process within 15:00–45:59. Narrate what, where, and why; keep task content visible and do not show AI interaction during the recording.
