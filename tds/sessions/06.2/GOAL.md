# 06.2 — Implement and verify one error-classification contract

**Role:** Payments integration engineer

**Purpose:** Give customers accurate failure messages and support usable error categories.

**Stakeholder:** Payments support lead and checkout team.

## Task description

I am investigating the payment code that maps different provider failures to the same misleading response. My goal is to provide the checkout team with a verified classification repair and HTTP evidence that each supported failure receives the correct status and message.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `error-mapping.patch`
- `error-response-evidence.md`
- `error-check-results.json`

## Quality checks

- [ ] Defined statuses, machine codes and safe messages agree with the contract.
- [ ] Invalid local values cause no provider call.
- [ ] Success data is preserved and unexpected errors remain dependency errors.
- [ ] The change adds no retries or actual remote charge.

**Apps:** Visual Studio Code, Firefox, GitHub Desktop.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

**Starting dependency:** [06.1](../06.1/GOAL.md) is optional; the supplied API error table is the authoritative starting contract.

## Workflow

1. Implement the bounded mapping and provider-call assertions in VS Code.
2. Use Firefox Network’s Edit and Resend on a synthetic local request to compare selected API responses.
3. Run focused tests, inspect the diff in GitHub Desktop and export a verification note.

## Recording script

Open the [Task 06 workspace](../../workspaces/06-error-classification.code-workspace) in VS Code. Run commands from its Application terminal; keep that terminal open. Follow the steps in order. Inputs and source: [task brief](../../tasks/06-error-classification/BRIEF.md), [provider-cases.json](../../tasks/06-error-classification/inputs/provider-cases.json), [payments.py](../../../app/payments.py), [provider.py](../../../app/provider.py), [API.md](../../../docs/API.md).

1. **Set up the session and output folder.** Copy the report template only if a report does not already exist.

```sh
./tds/lab start 06 --session 06.2
mkdir -p tds/tasks/06-error-classification/outcomes/06.2
cp -n tds/docs/REPORT-TEMPLATE.md tds/tasks/06-error-classification/outcomes/06.2/report.md
git status --short
```

2. **Reproduce and capture the baseline.** Run the provider probe before editing and note the current misclassification. Use the supplied stub cases; no external payment provider is involved.

For browser work, start the app in a second terminal with the command below. Open http://localhost:8010 in Firefox; use the example Ada or Ben account and the displayed practice password. Keep the server terminal open and stop it with Control-C when finished.

```sh
./tds/lab serve
```

Run the baseline commands in the Application terminal:

```sh
./tds/lab probe 6
```

3. **Investigate and create the deliverable.** In app/payments.py distinguish local validation from ProviderFailure status. Map decline, outage, timeout, and unexpected response to docs/API.md; preserve the success body and prevent provider calls for invalid integers, booleans, zero, and negatives.

4. **Verify the result.** Run focused cases and the suite. Use Firefox Network Edit and Resend on the local /api/charge request to capture representative HTTP responses, then review the patch in GitHub Desktop.

Run the verification commands:

```sh
./tds/lab probe 6
./tds/lab test
```

Before committing this session’s code, export the reviewed change as the required patch:

```sh
git add -N -- tests
git diff HEAD --binary -- app/payments.py tests > tds/tasks/06-error-classification/outcomes/06.2/error-mapping.patch
```

5. **Save and review the handoff.** Finish `report.md` in `tds/tasks/06-error-classification/outcomes/06.2/`. Save or export `error-response-evidence.md`, `error-check-results.json` to the same folder using the named apps. Reopen every output, check the quality boxes above, and confirm the folder contents:

```sh
ls -lh tds/tasks/06-error-classification/outcomes/06.2
git status --short
```

Keep the short introduction and complete on-screen process within 15:00–45:59. Narrate what, where, and why; keep task content visible and do not show AI interaction during the recording.
