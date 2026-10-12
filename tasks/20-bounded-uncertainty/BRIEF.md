# Task 20: Answer a question the evidence cannot yet settle

## Error or request

I am investigating a report that a disputed order may have been paid twice. My goal is to provide the operations manager and support lead with the strongest conclusion the incomplete evidence supports and a concrete plan to distinguish the remaining explanations.

## Relevant files

[inputs/manager-question.txt](inputs/manager-question.txt); [support-note.txt](inputs/support-note.txt); [app-fragment.jsonl](inputs/app-fragment.jsonl); [provider-summary.csv](inputs/provider-summary.csv); [evidence-limits.md](inputs/evidence-limits.md).

- [app-fragment.jsonl](inputs/app-fragment.jsonl)
- [evidence-limits.md](inputs/evidence-limits.md)
- [manager-question.txt](inputs/manager-question.txt)
- [provider-summary.csv](inputs/provider-summary.csv)
- [support-note.txt](inputs/support-note.txt)

## Reproduce or investigate

Open the [Task 20 workspace](../../workspaces/20-bounded-uncertainty.code-workspace). It uses the shared application and database. Read the inputs above. Run `./lab serve` for browser work or `./lab test` for tests.

Read only the supplied evidence as the historical incident record. The current starter code is an illustrative system, not proof of which code ran or which financial settlement occurred during that incident.

## Completion criteria

1. State the strongest bounded conclusion the evidence supports and do not give a fabricated definitive answer.
2. Describe at least two explanations consistent with the fragments and identify the missing discriminating fact.
3. Specify the exact data/source/time range/identifiers needed next and what outcomes would support or refute each explanation.
4. Separate request attempts, event deliveries, payment rows and actual settled charges.
5. Make every material claim traceable to a supplied source and describe evidence reliability/absence.

## Deliverable

outcomes/uncertainty-memo.md with supported facts, hypotheses, confidence and a concrete next-observation plan. No code change required.

## Task sessions

Choose a session below for its scope, apps, outputs and checks.

- [20.1 — Write a defensible disputed-charge memo](../../sessions/20.1/GOAL.md)
