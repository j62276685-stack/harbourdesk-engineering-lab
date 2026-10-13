# 08.2 — Implement the two-case reconciliation policy with an audit trail

**Role:** Payments systems engineer

**Purpose:** Preserve trustworthy local state when provider evidence conflicts.

**Stakeholder:** Reconciliation operator and fulfilment lead.

## Task description

I am investigating how the application applies provider observations that conflict with completed or cancelled orders. My goal is to provide the reconciliation operator with a verified repair that follows the agreed policy, retains an audit trail and avoids unintended fulfilment.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `provider-reconciliation.patch`
- `reconciliation-audit.csv`
- `reconciliation-verification.md`

## Quality checks

- [ ] The two conflicting cases preserve the selected safeguards.
- [ ] A normal matching success and an invalid money/currency observation are checked.
- [ ] Stable observation identity prevents a repeated financial/audit effect.
- [ ] The audit retains the received evidence and selected reason.

**Apps:** Visual Studio Code, DB Browser for SQLite, GitHub Desktop.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

**Starting dependency:** Use the supplied safeguards plus a frozen [08.1](../08.1/GOAL.md) policy, or write the bounded policy as part of this session’s first review.

## Workflow

1. Use the stated policy to edit the relevant handler/audit storage in VS Code.
2. Run the two conflict cases, a normal success and a replay; inspect order/audit records in DB Browser.
3. Review the diff and explain any state-model choice in the verification note.

## Recording script

Open the [Task 08 workspace](../../workspaces/08-provider-reconciliation.code-workspace) in VS Code. Run commands from its Application terminal; keep that terminal open. Follow the steps in order. Inputs and source: [task brief](../../tasks/08-provider-reconciliation/BRIEF.md), [observations.json](../../tasks/08-provider-reconciliation/inputs/observations.json), [policy-context.md](../../tasks/08-provider-reconciliation/inputs/policy-context.md), [payments.py](../../../app/payments.py), [schema.sql](../../../app/schema.sql).

1. **Set up the session and output folder.** Copy the report template only if a report does not already exist.

```sh
./tds/lab start 08 --session 08.2
mkdir -p tds/tasks/08-provider-reconciliation/outcomes/08.2
cp -n tds/docs/REPORT-TEMPLATE.md tds/tasks/08-provider-reconciliation/outcomes/08.2/report.md
git status --short
```

2. **Reproduce and capture the baseline.** Run the two contradiction cases before editing and record the original order versions.

Run the baseline commands in the Application terminal:

```sh
./tds/lab probe 8
```

3. **Investigate and create the deliverable.** In app/payments.py apply the documented policy: preserve cancelled order state while recording success for review, ignore stale failure for paid, validate observation fields, and deduplicate by observation_id. Add durable audit storage in app/schema.sql and tests for replay and normal success.

4. **Verify the result.** Rerun the probe and suite. In DB Browser export order and audit rows for both contradictions and a replay; review the diff and explain state-model choices.

Run the verification commands:

```sh
./tds/lab probe 8
./tds/lab test
```

Before committing this session’s code, export the reviewed change as the required patch:

```sh
git add -N -- tests
git diff HEAD --binary -- app/payments.py app/schema.sql tests > tds/tasks/08-provider-reconciliation/outcomes/08.2/provider-reconciliation.patch
```

5. **Save and review the handoff.** Finish `report.md` in `tds/tasks/08-provider-reconciliation/outcomes/08.2/`. Save or export `reconciliation-audit.csv`, `reconciliation-verification.md` to the same folder using the named apps. Reopen every output, check the quality boxes above, and confirm the folder contents:

```sh
ls -lh tds/tasks/08-provider-reconciliation/outcomes/08.2
git status --short
```

Keep the short introduction and complete on-screen process within 15:00–45:59. Narrate what, where, and why; keep task content visible and do not show AI interaction during the recording.
