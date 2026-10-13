# 09.2 — Implement retry eligibility and stable request identity

**Role:** Integration software engineer

**Purpose:** Bound payment retries without increasing duplicate-charge risk.

**Stakeholder:** Payments integration reviewer.

## Task description

I am investigating retry logic that repeats permanent failures and changes the identity of one payment operation. My goal is to provide the integration reviewer with a verified repair that stops ineligible retries, preserves one request key and enforces the attempt limit.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `retry-identity.patch`
- `retry-call-audit.ods`
- `retry-identity-checks.md`

## Quality checks

- [ ] A permanent failure stops after one call.
- [ ] All attempts for one operation retain the same nonempty key.
- [ ] At most three calls occur.
- [ ] The delivered patch states that deadline/backoff integration is the next bounded piece, not falsely complete.

**Apps:** Visual Studio Code, GitHub Desktop, LibreOffice.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

**Starting dependency:** The provided retry contract supplies the rules; [09.1](../09.1/GOAL.md) may be included as a frozen design input.

## Workflow

1. Edit only retry eligibility, request identity and call-count behavior in VS Code.
2. Use fake provider scripts to inspect permanent failure, eventual success and exhausted calls.
3. Review the patch in GitHub Desktop and create a LibreOffice call/key audit table for the integration reviewer.

## Recording script

Open the [Task 09 workspace](../../workspaces/09-retry-policy.code-workspace) in VS Code. Run commands from its Application terminal; keep that terminal open. Follow the steps in order. Inputs and source: [task brief](../../tasks/09-retry-policy/BRIEF.md), [provider-scripts.json](../../tasks/09-retry-policy/inputs/provider-scripts.json), [retry-contract.md](../../tasks/09-retry-policy/inputs/retry-contract.md), [retries.py](../../../app/retries.py), [provider.py](../../../app/provider.py).

1. **Set up the session and output folder.** Copy the report template only if a report does not already exist.

```sh
./tds/lab start 09 --session 09.2
mkdir -p tds/tasks/09-retry-policy/outcomes/09.2
cp -n tds/docs/REPORT-TEMPLATE.md tds/tasks/09-retry-policy/outcomes/09.2/report.md
git status --short
```

2. **Reproduce and capture the baseline.** Run the retry probe to capture current call keys and the response sequence.

Run the baseline commands in the Application terminal:

```sh
./tds/lab probe 9
```

3. **Investigate and create the deliverable.** In app/retries.py retry only status 0, 408, 429, 500, 502, 503, and 504; stop on other client or decline errors. Use the same idempotency key for every attempt, with at most three total calls. Add fake-provider tests for permanent failure, eventual success, and exhaustion.

4. **Verify the result.** Rerun the probe and suite; use ScriptedProvider.calls to fill the key/call audit in Calc. Review the focused patch in GitHub Desktop.

Run the verification commands:

```sh
./tds/lab probe 9
./tds/lab test
```

Before committing this session’s code, export the reviewed change as the required patch:

```sh
git add -N -- tests
git diff HEAD --binary -- app/retries.py tests > tds/tasks/09-retry-policy/outcomes/09.2/retry-identity.patch
```

5. **Save and review the handoff.** Finish `report.md` in `tds/tasks/09-retry-policy/outcomes/09.2/`. Save or export `retry-call-audit.ods`, `retry-identity-checks.md` to the same folder using the named apps. Reopen every output, check the quality boxes above, and confirm the folder contents:

```sh
ls -lh tds/tasks/09-retry-policy/outcomes/09.2
git status --short
```

Keep the short introduction and complete on-screen process within 15:00–45:59. Narrate what, where, and why; keep task content visible and do not show AI interaction during the recording.
