# 15.2 — Enforce and verify the bounded lifecycle transition contract

**Role:** Backend domain engineer

**Purpose:** Make order transitions predictable and enforceable.

**Stakeholder:** Fulfilment product owner and QA team.

## Task description

Implement the declared transition boundary and matrix checks, then provide persisted version/error evidence and a focused reviewed patch.

## Final deliverable

- `order-lifecycle.patch`
- `order-state-evidence.csv`
- `order-lifecycle-checks.md`

## Quality checks

- [ ] All known state pairs agree with the supplied contract.
- [ ] New accepted changes increment once; rejected/no-op requests do not.
- [ ] Unknown target, forbidden pair and ownership errors are distinct as specified.
- [ ] A legitimate flow and cancelled terminal state are checked.

**Apps:** Visual Studio Code, DB Browser for SQLite, GitHub Desktop.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

**Starting dependency:** The supplied lifecycle contract is sufficient; [15.1](../15.1/GOAL.md) may be included as a frozen visual specification.

## Workflow

1. Implement the declared transition table and focused matrix checks in VS Code.
2. Run legitimate/forbidden/no-op cases and inspect persisted version/status with DB Browser.
3. Review the diff in GitHub Desktop and export the transition checks and patch.
