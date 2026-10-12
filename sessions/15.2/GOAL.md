# 15.2 — Enforce and verify the bounded lifecycle transition contract

**Role:** Backend domain engineer

**Purpose:** Make order transitions predictable and enforceable.

**Stakeholder:** Fulfilment product owner and QA team.

## Task description

I am investigating the transition code that allows orders to move outside the agreed lifecycle. My goal is to provide the fulfilment and QA teams with a verified repair that enforces allowed transitions and preserves order history and version values when a request is rejected.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
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
