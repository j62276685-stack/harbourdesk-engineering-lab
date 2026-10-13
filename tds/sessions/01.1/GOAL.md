# 01.1 — Diagnose the provider sign-in journey

**Role:** Backend software engineer

**Purpose:** Diagnose the reported provider sign-in failure and recommend a focused repair.

**Stakeholder:** Engineering lead and support lead.

## Task description

I am investigating a customer report that password sign-in works but signing in through our in-house Identity provider fails. My goal is to provide the engineering lead with an evidence-based diagnosis and a clear explanation of the affected customer journey.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `login-network-evidence.png`

## Quality checks

- [ ] Both journeys are observed on the original different hostnames.
- [ ] The diagnosis cites the callback request and matching database/source evidence.
- [ ] The proposed repair retains one-use state validation and distinguishes local HTTP from deployment configuration.
- [ ] The handoff separates observations from inference and gives a concrete next validation.

**Apps:** Firefox, Visual Studio Code, DB Browser for SQLite.

## Workflow

1. Read the [support ticket](../../tasks/01-login-journey/inputs/support-report.txt) in Visual Studio Code.
2. In Firefox, compare both sign-in journeys and inspect the redirects and callback request. Keep `localhost:8010` and `127.0.0.1:8011` unchanged.
3. Trace [app/auth.py](../../../app/auth.py) and [app/http.py](../../../app/http.py) in Visual Studio Code. Compare the matching session record in DB Browser for SQLite.
4. Complete `report.md` and capture the callback evidence. Reopen both outputs and check the criteria above.

Narrate what, where and why. Keep relevant content visible, limit window overlap to 25%, and avoid exposing personal information.

## Recording script

Open the [Task 01 workspace](../../workspaces/01-login-journey.code-workspace) in VS Code. Run commands from its Application terminal; keep that terminal open. Follow the steps in order. Inputs and source: [task brief](../../tasks/01-login-journey/BRIEF.md), [support-report.txt](../../tasks/01-login-journey/inputs/support-report.txt), [auth.py](../../../app/auth.py), [http.py](../../../app/http.py), [index.html](../../../web/index.html).

1. **Set up the session and output folder.** Copy the report template only if a report does not already exist.

```sh
./tds/lab start 01 --session 01.1
mkdir -p tds/tasks/01-login-journey/outcomes/01.1
cp -n tds/docs/REPORT-TEMPLATE.md tds/tasks/01-login-journey/outcomes/01.1/report.md
git status --short
```

2. **Reproduce and capture the baseline.** In Firefox, sign in as Ada with the local password, then sign out and clear the localhost cookie. Enable Preserve Log in Network, start Harbour Identity, and choose Continue as Ada. Compare the redirect, Set-Cookie, and callback Cookie headers; do not include raw token values in the screenshot.

For browser work, start the app in a second terminal with the command below. Open http://localhost:8010 in Firefox; use the example Ada or Ben account and the displayed practice password. Keep the server terminal open and stop it with Control-C when finished.

```sh
./tds/lab serve
```

Run the baseline commands in the Application terminal:

```sh
./tds/lab probe 1
./tds/lab sql 'SELECT user_id, state_used, state IS NOT NULL AS has_state FROM sessions ORDER BY rowid DESC LIMIT 5'
```

3. **Investigate and create the deliverable.** In VS Code trace the cookie policy and one-use state check in app/auth.py, then the start and callback routes in app/http.py. In DB Browser inspect the session state and state_used fields. Explain why a top-level return from the other hostname loses this cookie under the current policy.

4. **Verify the result.** Reopen the screenshot and report. Separate browser observation from the SameSite inference and propose a fix that retains HttpOnly and rejects missing, wrong, and replayed state.

5. **Save and review the handoff.** Finish `report.md` in `tds/tasks/01-login-journey/outcomes/01.1/`. Save or export `login-network-evidence.png` to the same folder using the named apps. Reopen every output, check the quality boxes above, and confirm the folder contents:

```sh
ls -lh tds/tasks/01-login-journey/outcomes/01.1
git status --short
```

Keep the short introduction and complete on-screen process within 15:00–45:59. Narrate what, where, and why; keep task content visible and do not show AI interaction during the recording.
