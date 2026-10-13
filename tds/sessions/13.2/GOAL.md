# 13.2 — Implement a repeat-safe audited wallet cache correction

**Role:** Backend finance-systems engineer

**Purpose:** Reconcile the displayed wallet balance without rewriting financial history.

**Stakeholder:** Finance operations analyst.

## Task description

I am investigating the confirmed discrepancy between the wallet cache and posted transaction history. My goal is to provide finance operations with a repeat-safe correction that updates the cache atomically, records the change and preserves the original ledger.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `wallet-cache-repair.patch`
- `wallet-audit-evidence.csv`
- `wallet-repair-checks.md`

## Quality checks

- [ ] Corrected cache equals posted ledger sum.
- [ ] Original ledger fields are unchanged.
- [ ] One atomic audit/correction records old/new amount and reason.
- [ ] Repeat, consistent account, unknown account and controlled rollback are verified.

**Apps:** Visual Studio Code, DB Browser for SQLite, GitHub Desktop.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

**Starting dependency:** The supplied reconciliation policy defines the boundary; [13.1](../13.1/GOAL.md) is optional context.

## Workflow

1. Implement the bounded repair and domain cases in VS Code.
2. Run the correction/repeat/control checks and inspect ledger/cache/audit rows in DB Browser.
3. Review the code diff and export before/after extracts with interruption/rollback evidence.

## Recording script

Open the [Task 13 workspace](../../workspaces/13-wallet-reconciliation.code-workspace) in VS Code. Run commands from its Application terminal; keep that terminal open. Follow the steps in order. Inputs and source: [task brief](../../tasks/13-wallet-reconciliation/BRIEF.md), [reconciliation-policy.md](../../tasks/13-wallet-reconciliation/inputs/reconciliation-policy.md), [wallet-statement.csv](../../tasks/13-wallet-reconciliation/inputs/wallet-statement.csv), [wallet.py](../../../app/wallet.py), [schema.sql](../../../app/schema.sql).

1. **Set up the session and output folder.** Copy the report template only if a report does not already exist.

```sh
./tds/lab start 13 --session 13.2
mkdir -p tds/tasks/13-wallet-reconciliation/outcomes/13.2
cp -n tds/docs/REPORT-TEMPLATE.md tds/tasks/13-wallet-reconciliation/outcomes/13.2/report.md
git status --short
```

2. **Reproduce and capture the baseline.** Capture account, ledger, and audit state before editing. Keep a disposable copy for interruption testing.

Run the baseline commands in the Application terminal:

```sh
./tds/lab probe 13
```

3. **Investigate and create the deliverable.** In app/wallet.py add a transaction that checks the posted sum, repairs only a differing cache, and writes one reasoned audit record in the same transaction. Treat unknown users as errors and leave ledger entries unchanged.

4. **Verify the result.** Run correction, repeat, Ben control, unknown-user, and injected-rollback tests. In DB Browser compare ledger, cache, and audit rows; review the patch.

Run the verification commands:

```sh
./tds/lab test
```

Before committing this session’s code, export the reviewed change as the required patch:

```sh
git add -N -- tests
git diff HEAD --binary -- app/wallet.py app/schema.sql tests > tds/tasks/13-wallet-reconciliation/outcomes/13.2/wallet-cache-repair.patch
```

5. **Save and review the handoff.** Finish `report.md` in `tds/tasks/13-wallet-reconciliation/outcomes/13.2/`. Save or export `wallet-audit-evidence.csv`, `wallet-repair-checks.md` to the same folder using the named apps. Reopen every output, check the quality boxes above, and confirm the folder contents:

```sh
ls -lh tds/tasks/13-wallet-reconciliation/outcomes/13.2
git status --short
```

Keep the short introduction and complete on-screen process within 15:00–45:59. Narrate what, where, and why; keep task content visible and do not show AI interaction during the recording.
