# 01.1 — Diagnose the provider sign-in journey

**Role:** Backend software engineer

**Purpose:** Diagnose the reported provider sign-in failure and recommend a focused repair.

**Stakeholder:** Engineering lead and support lead.

## Task description

Investigate ticket HD-1101: password sign-in works, but Harbour Identity sign-in fails. Identify where the journey breaks, support the diagnosis with browser, source-code and database evidence, and recommend a focused repair for the engineering and support leads.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

## Final deliverable

- `login-diagnosis.md`
- `login-network-evidence.png`
- `session-observation.csv`

## Quality checks

- [ ] Both journeys are observed on the original different hostnames.
- [ ] The diagnosis cites the callback request and matching database/source evidence.
- [ ] The proposed repair retains one-use state validation and distinguishes local HTTP from deployment configuration.
- [ ] The handoff separates observations from inference and gives a concrete next validation.

**Apps:** Firefox, Visual Studio Code, DB Browser for SQLite.

## Workflow

1. Read the [support ticket](../../tasks/01-login-journey/inputs/support-report.txt) in Visual Studio Code.
2. In Firefox, compare both sign-in journeys and inspect the redirects and callback request. Keep `localhost:8010` and `127.0.0.1:8011` unchanged.
3. Trace [app/auth.py](../../app/auth.py) and [app/http.py](../../app/http.py) in Visual Studio Code. Compare the matching session record in DB Browser for SQLite.
4. Write the diagnosis, capture the callback evidence, and export the session observations. Reopen all three outputs and check the criteria above.

Narrate what, where and why. Keep relevant content visible, limit window overlap to 25%, and avoid exposing personal information.
