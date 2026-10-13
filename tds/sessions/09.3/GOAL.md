# 09.3 — Integrate deadline and Retry-After handling

**Role:** Integration software engineer

**Purpose:** Bound payment retries without increasing duplicate-charge risk.

**Stakeholder:** Payments integration reviewer.

## Task description

I am investigating whether eligible payment retries respect the total deadline and provider rate-limit instructions. My goal is to provide the integration reviewer with a verified timing implementation and a fake-clock audit of its wait and stop decisions.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `retry-budget.patch`
- `retry-timing-audit.ods`
- `retry-budget-verdict.md`

## Quality checks

- [ ] Waits and simulated request durations count toward the eight-second budget.
- [ ] No next call begins after exhaustion or a wait exceeding the budget.
- [ ] 429 delay parsing and the four-second cap follow the contract.
- [ ] Timing evidence is fake-clock based and includes the final outcome.

**Apps:** Visual Studio Code, GitHub Desktop, LibreOffice.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

**Starting dependency:** A frozen eligibility/key implementation is required; use your [09.2](../09.2/GOAL.md) result. This is a separate Idea with that code as its starting input.

## Workflow

1. Inspect the supplied/human-created eligibility candidate and implement bounded waits/deadline checks.
2. Run malformed Retry-After, capped delay, exhausted budget and eventual-success scenarios using a fake clock.
3. Review the source diff in GitHub Desktop and recalculate the timing table in LibreOffice.

## Recording script

Open the [Task 09 workspace](../../workspaces/09-retry-policy.code-workspace) in VS Code. Run commands from its Application terminal; keep that terminal open. Follow the steps in order. Inputs and source: [task brief](../../tasks/09-retry-policy/BRIEF.md), [provider-scripts.json](../../tasks/09-retry-policy/inputs/provider-scripts.json), [retry-contract.md](../../tasks/09-retry-policy/inputs/retry-contract.md), [retries.py](../../../app/retries.py), [provider.py](../../../app/provider.py).

1. **Set up the session and output folder.** Copy the report template only if a report does not already exist.

```sh
./tds/lab start 09 --session 09.3
mkdir -p tds/tasks/09-retry-policy/outcomes/09.3
cp -n tds/docs/REPORT-TEMPLATE.md tds/tasks/09-retry-policy/outcomes/09.3/report.md
git status --short
```

2. **Reproduce and capture the baseline.** Start from the frozen eligibility candidate or the supplied retry contract; record its call sequence before adding timing.

Run the baseline commands in the Application terminal:

```sh
./tds/lab probe 9
```

3. **Investigate and create the deliverable.** Inject a fake monotonic clock and sleep callback into app/retries.py. Count request durations and waits in the eight-second budget; use 1 and 2 seconds normally, or valid nonnegative 429 Retry-After capped at four seconds. Do not begin a call if its preceding wait exceeds the budget.

4. **Verify the result.** Test malformed/negative Retry-After, capped delay, exhausted time, and eventual success without real sleeping. Compare the timing table in Calc and review the patch.

Run the verification commands:

```sh
./tds/lab test
```

Before committing this session’s code, export the reviewed change as the required patch:

```sh
git add -N -- tests
git diff HEAD --binary -- app/retries.py tests > tds/tasks/09-retry-policy/outcomes/09.3/retry-budget.patch
```

5. **Save and review the handoff.** Finish `report.md` in `tds/tasks/09-retry-policy/outcomes/09.3/`. Save or export `retry-timing-audit.ods`, `retry-budget-verdict.md` to the same folder using the named apps. Reopen every output, check the quality boxes above, and confirm the folder contents:

```sh
ls -lh tds/tasks/09-retry-policy/outcomes/09.3
git status --short
```

Keep the short introduction and complete on-screen process within 15:00–45:59. Narrate what, where, and why; keep task content visible and do not show AI interaction during the recording.
