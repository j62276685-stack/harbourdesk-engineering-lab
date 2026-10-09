# Task 20: Answer a question the evidence cannot yet settle

## Error or request

A manager asks whether a disputed order was paid twice. The attached fragments are intentionally insufficient. Answer responsibly and design the next observation that would distinguish the plausible explanations.

## Relevant files

[inputs/manager-question.txt](inputs/manager-question.txt); [support-note.txt](inputs/support-note.txt); [app-fragment.jsonl](inputs/app-fragment.jsonl); [provider-summary.csv](inputs/provider-summary.csv); [evidence-limits.md](inputs/evidence-limits.md).

- [app-fragment.jsonl](inputs/app-fragment.jsonl)
- [evidence-limits.md](inputs/evidence-limits.md)
- [manager-question.txt](inputs/manager-question.txt)
- [provider-summary.csv](inputs/provider-summary.csv)
- [support-note.txt](inputs/support-note.txt)

## Reproduce or investigate

From the project root, run `./lab start 20`. Open the printed folder. Run `./lab serve` for browser work or `./lab test` for tests. Inputs are copied to `evidence/inputs/`.

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
