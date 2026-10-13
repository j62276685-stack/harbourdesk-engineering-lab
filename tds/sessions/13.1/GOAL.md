# 13.1 — Reconcile one wallet cache against its posted ledger

**Role:** Backend finance-systems engineer

**Purpose:** Reconcile the displayed wallet balance without rewriting financial history.

**Stakeholder:** Finance operations analyst.

## Task description

I am investigating a customer dispute about Ada’s displayed wallet balance. My goal is to provide finance operations with an independently calculated ledger balance, a comparison against the cached balance and an auditable correction recommendation.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `wallet-reconciliation.ods`
- `wallet-authority.drawio`
- `wallet-correction-recommendation.pdf`

## Quality checks

- [ ] Arithmetic and source references are reproducible.
- [ ] Ben is checked as a consistent control.
- [ ] The recommendation does not invent a compensating financial transaction.
- [ ] The original ledger and necessary audit facts are specified.

**Apps:** DB Browser for SQLite, LibreOffice, draw.io Desktop.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

## Workflow

1. Inspect account/ledger values and source references in DB Browser.
2. Calculate the balance/difference in Calc and distinguish cached data from posted transactions.
3. Draw the ledger/cache/audit responsibility model and export the finance handoff.

## Recording script

Open the [Task 13 workspace](../../workspaces/13-wallet-reconciliation.code-workspace) in VS Code. Run commands from its Application terminal; keep that terminal open. Follow the steps in order. Inputs and source: [task brief](../../tasks/13-wallet-reconciliation/BRIEF.md), [reconciliation-policy.md](../../tasks/13-wallet-reconciliation/inputs/reconciliation-policy.md), [wallet-statement.csv](../../tasks/13-wallet-reconciliation/inputs/wallet-statement.csv), [wallet.py](../../../app/wallet.py), [schema.sql](../../../app/schema.sql).

1. **Set up the session and output folder.** Copy the report template only if a report does not already exist.

```sh
./tds/lab start 13 --session 13.1
mkdir -p tds/tasks/13-wallet-reconciliation/outcomes/13.1
cp -n tds/docs/REPORT-TEMPLATE.md tds/tasks/13-wallet-reconciliation/outcomes/13.1/report.md
git status --short
```

2. **Reproduce and capture the baseline.** Run the wallet probe and inspect wallet_accounts, wallet_entries, and the supplied statement in DB Browser. Preserve the original ledger and cached balance figures.

Run the baseline commands in the Application terminal:

```sh
./tds/lab probe 13
./tds/lab sql 'SELECT user_id,SUM(delta_minor) AS ledger_minor FROM wallet_entries GROUP BY user_id ORDER BY user_id'
./tds/lab sql 'SELECT user_id,balance_minor FROM wallet_accounts ORDER BY user_id'
```

3. **Investigate and create the deliverable.** In Calc sum posted delta_minor by user from zero, compare with cache, and include Ben as the consistent control. Draw the ledger as authority, cache as derived state, and audit as the correction record.

4. **Verify the result.** Check arithmetic and source IDs. Recommend a cache correction only; no fabricated payment or refund entry.

5. **Save and review the handoff.** Finish `report.md` in `tds/tasks/13-wallet-reconciliation/outcomes/13.1/`. Save or export `wallet-reconciliation.ods`, `wallet-authority.drawio`, `wallet-correction-recommendation.pdf` to the same folder using the named apps. Reopen every output, check the quality boxes above, and confirm the folder contents:

```sh
ls -lh tds/tasks/13-wallet-reconciliation/outcomes/13.1
git status --short
```

Keep the short introduction and complete on-screen process within 15:00–45:59. Narrate what, where, and why; keep task content visible and do not show AI interaction during the recording.
