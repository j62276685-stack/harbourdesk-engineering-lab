# 01.2 — Repair and verify the bounded sign-in failure

**Role:** Backend software engineer

**Purpose:** Restore reliable sign-in for the shop support team.

**Stakeholder:** Support lead and customers unable to sign in.

## Task description

I am investigating the sign-in failure that prevents customers from returning successfully from our in-house Identity provider. My goal is to provide the engineering lead with a verified repair that restores sign-in while retaining one-use state validation.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `login-fix.patch`
- `login-verification.md`
- `provider-success.png`

## Quality checks

- [ ] Both legitimate journeys now work.
- [ ] Missing, incorrect and replayed state remain rejected.
- [ ] The diff contains only the justified session/callback change.
- [ ] Evidence supports the claimed browser result and names the browser version.

**Apps:** Visual Studio Code, Firefox, GitHub Desktop.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

**Starting dependency:** [01.1](../01.1/GOAL.md) diagnosis is useful context; the supplied ticket and original source are sufficient if this is attempted independently.

## Workflow

1. Use the known complaint and policy to select the smallest safe code change.
2. Test normal password/provider journeys in Firefox and run focused state checks from VS Code’s task menu.
3. Review the entire diff in GitHub Desktop and save the patch and verification note.

## Recording script

Open the [Task 01 workspace](../../workspaces/01-login-journey.code-workspace) in VS Code. Run commands from its Application terminal; keep that terminal open. Follow the steps in order. Inputs and source: [task brief](../../tasks/01-login-journey/BRIEF.md), [support-report.txt](../../tasks/01-login-journey/inputs/support-report.txt), [auth.py](../../../app/auth.py), [http.py](../../../app/http.py), [index.html](../../../web/index.html).

1. **Set up the session and output folder.** Copy the report template only if a report does not already exist.

```sh
./tds/lab start 01 --session 01.2
mkdir -p tds/tasks/01-login-journey/outcomes/01.2
cp -n tds/docs/REPORT-TEMPLATE.md tds/tasks/01-login-journey/outcomes/01.2/report.md
git status --short
```

2. **Reproduce and capture the baseline.** Reproduce the failing provider journey and a working password journey in Firefox. Record the browser version and callback status before editing.

For browser work, start the app in a second terminal with the command below. Open http://localhost:8010 in Firefox; use the example Ada or Ben account and the displayed practice password. Keep the server terminal open and stop it with Control-C when finished.

```sh
./tds/lab serve
```

Run the baseline commands in the Application terminal:

```sh
./tds/lab probe 1
```

3. **Investigate and create the deliverable.** Change the local callback cookie policy in app/auth.py to permit this top-level cross-site return while keeping HttpOnly and one-use state validation. Add tests for missing, wrong, reused, and cross-session state; avoid broad router changes.

4. **Verify the result.** Run the state checks and full suite, then repeat both Firefox journeys. Review the entire change in GitHub Desktop and record the two-hostname result in login-verification.md.

Run the verification commands:

```sh
./tds/lab test
```

Before committing this session’s code, export the reviewed change as the required patch:

```sh
git add -N -- tests
git diff HEAD --binary -- app/auth.py app/http.py tests > tds/tasks/01-login-journey/outcomes/01.2/login-fix.patch
```

5. **Save and review the handoff.** Finish `report.md` in `tds/tasks/01-login-journey/outcomes/01.2/`. Save or export `login-verification.md`, `provider-success.png` to the same folder using the named apps. Reopen every output, check the quality boxes above, and confirm the folder contents:

```sh
ls -lh tds/tasks/01-login-journey/outcomes/01.2
git status --short
```

Keep the short introduction and complete on-screen process within 15:00–45:59. Narrate what, where, and why; keep task content visible and do not show AI interaction during the recording.
