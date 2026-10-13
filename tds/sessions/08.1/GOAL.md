# 08.1 — Decide how two contradictory provider observations should be reconciled

**Role:** Payments systems engineer

**Purpose:** Preserve trustworthy local state when provider evidence conflicts.

**Stakeholder:** Reconciliation operator and fulfilment lead.

## Task description

I am investigating provider observations that contradict local order state: a success for a cancelled order and an older failure for a paid order. My goal is to provide the reconciliation operator and fulfilment lead with a decision policy that preserves evidence and prevents accidental fulfilment.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `reconciliation-policy.ods`
- `reconciliation-model.drawio`
- `reconciliation-decision.pdf`

## Quality checks

- [ ] An older failure cannot undo a paid order.
- [ ] Late success for a cancelled order does not automatically reopen fulfilment.
- [ ] Audit identity, money/currency validation and repeated-observation behavior are explicit.
- [ ] The policy distinguishes observation time from settlement evidence.

**Apps:** Visual Studio Code, LibreOffice, draw.io Desktop.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

## Workflow

1. Inspect the supplied local facts and provider observations in VS Code.
2. Build the evidence/decision/audit table in LibreOffice with stale, normal, repeated and invalid cases.
3. Draw the order-versus-payment decision model and export the operator guidance.

## Recording script

Open the [Task 08 workspace](../../workspaces/08-provider-reconciliation.code-workspace) in VS Code. Run commands from its Application terminal; keep that terminal open. Follow the steps in order. Inputs and source: [task brief](../../tasks/08-provider-reconciliation/BRIEF.md), [observations.json](../../tasks/08-provider-reconciliation/inputs/observations.json), [policy-context.md](../../tasks/08-provider-reconciliation/inputs/policy-context.md), [payments.py](../../../app/payments.py), [schema.sql](../../../app/schema.sql).

1. **Set up the session and output folder.** Copy the report template only if a report does not already exist.

```sh
./tds/lab start 08 --session 08.1
mkdir -p tds/tasks/08-provider-reconciliation/outcomes/08.1
cp -n tds/docs/REPORT-TEMPLATE.md tds/tasks/08-provider-reconciliation/outcomes/08.1/report.md
git status --short
```

2. **Reproduce and capture the baseline.** Run the reconciliation probe and inspect observations.json beside the local order rows. Keep provider observation time and local order state as distinct evidence.

Run the baseline commands in the Application terminal:

```sh
./tds/lab probe 8
./tds/lab sql 'SELECT id,status,provider_status,version FROM orders WHERE id IN ("ord_cancelled","ord_paid") ORDER BY id'
```

3. **Investigate and create the deliverable.** In Calc make decisions for success on cancelled, older failure on paid, normal pending success, replay, amount/currency mismatch, and unknown order. Preserve a review/refund path for cancelled success and prevent an old failure from downgrading paid. Draw the order/payment/audit boundaries.

4. **Verify the result.** Check every policy row against the supplied context; export operator guidance with what is recorded, what changes state, and what requires human review.

5. **Save and review the handoff.** Finish `report.md` in `tds/tasks/08-provider-reconciliation/outcomes/08.1/`. Save or export `reconciliation-policy.ods`, `reconciliation-model.drawio`, `reconciliation-decision.pdf` to the same folder using the named apps. Reopen every output, check the quality boxes above, and confirm the folder contents:

```sh
ls -lh tds/tasks/08-provider-reconciliation/outcomes/08.1
git status --short
```

Keep the short introduction and complete on-screen process within 15:00–45:59. Narrate what, where, and why; keep task content visible and do not show AI interaction during the recording.
