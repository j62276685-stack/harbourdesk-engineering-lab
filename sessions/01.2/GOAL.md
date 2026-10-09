# 01.2 — Repair and verify the bounded sign-in failure

**Role:** Backend software engineer

**Purpose:** Restore reliable sign-in for the shop support team.

**Stakeholder:** Support lead and customers unable to sign in.

## Task description

Make a focused session/callback repair, validate normal and invalid-state paths, and deliver a reviewed source patch with browser evidence.

## Final deliverable

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
