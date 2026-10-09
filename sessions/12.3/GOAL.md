# 12.3 — Build canonical customer identities and alias coverage

**Role:** Data migration engineer

**Purpose:** Turn a messy import into auditable customer identities with a recovery path.

**Stakeholder:** Customer-data owner and release reviewer.

## Task description

Extend a frozen staging migration with deterministic canonical identities and aliases, then demonstrate the complete eight-row reconciliation and unique-email constraint.

## Final deliverable

- `customer-canonicalization.patch`
- `customer-coverage.csv`
- `customer-identity-checks.md`

## Quality checks

- [ ] Canonical emails are uniquely constrained.
- [ ] The earliest import/ID tie-break chooses survivors.
- [ ] The provided expected 3 identities, 2 aliases and 3 quarantine records reconcile to 8 sources.
- [ ] Repeated execution preserves the same mapping without losing originals.

**Apps:** Visual Studio Code, DB Browser for SQLite, GitHub Desktop.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

**Starting dependency:** Your frozen [12.2](../12.2/GOAL.md) staging code/database is required as the starting input.

## Workflow

1. Inspect the staging input and implement the survivor/alias mapping.
2. Run the migration and use DB Browser to verify constraints and per-source coverage.
3. Review the focused diff and export canonical/alias/quarantine counts with repeat-run evidence.
