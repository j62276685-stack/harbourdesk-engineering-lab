# 17.1 — Review the proposed refund conversion change

**Role:** Senior software engineer reviewing a change

**Purpose:** Assess whether a refund change preserves the published amount contract.

**Stakeholder:** Pull-request author and payments engineering lead.

## Task description

I am investigating whether a proposed refund conversion change preserves the published amount contract. My goal is to provide the pull-request author and payments engineering lead with a prioritized review, a minimal demonstration of any consequential defect and a justified approval recommendation.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `refund-review-findings.ods`
- `refund-pr-review.pdf`
- `refund-review-demonstration.md`

## Quality checks

- [ ] At least one consequential finding has an exact line, trigger and expected/actual result.
- [ ] The finding addresses the minor-unit contract and compatibility claim.
- [ ] Legitimate inputs and blocker versus optional feedback are distinguished.
- [ ] No real PR comment is posted or full replacement solution implemented.

**Apps:** Visual Studio Code, GitHub Desktop, LibreOffice.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

## Workflow

1. Compare the baseline/proposed revision in GitHub Desktop and inspect the candidate source in VS Code.
2. Run a minimal comparison plus legitimate inputs; record expected/actual values and severity in LibreOffice.
3. Export the source-linked review with the exact candidate lines and a reasoned decision.

## Recording script

Open the [Task 17 workspace](../../workspaces/17-flawed-pr-review.code-workspace) in VS Code. Run commands from its Application terminal; keep that terminal open. Follow the steps in order. Inputs and source: [task brief](../../tasks/17-flawed-pr-review/BRIEF.md), [pr-description.md](../../tasks/17-flawed-pr-review/inputs/pr-description.md), [proposed.patch](../../tasks/17-flawed-pr-review/inputs/proposed.patch), [refunds_candidate.py](../../tasks/17-flawed-pr-review/inputs/refunds_candidate.py), [review-cases.json](../../tasks/17-flawed-pr-review/inputs/review-cases.json), [refunds.py](../../../app/refunds.py).

1. **Set up the session and output folder.** Copy the report template only if a report does not already exist.

```sh
./tds/lab start 17 --session 17.1
mkdir -p tds/tasks/17-flawed-pr-review/outcomes/17.1
cp -n tds/docs/REPORT-TEMPLATE.md tds/tasks/17-flawed-pr-review/outcomes/17.1/report.md
git status --short
```

2. **Reproduce and capture the baseline.** After previous application changes are committed, create the local review branches once. In GitHub Desktop compare refund-baseline with proposed-refund; also read the candidate source and supplied cases in VS Code.

Run the baseline commands in the Application terminal:

```sh
./tds/lab setup-review
git diff refund-baseline..proposed-refund -- app/refunds.py
```

3. **Investigate and create the deliverable.** Run the supplied cases against both functions using the command below. In Calc record exact input, baseline result, proposed result, expected result, line, and severity. Test at least one valid integer and invalid boolean/float inputs; add the float case to the table manually if it is absent from the JSON fixture.

```sh
python3 - <<'PYDEMO'
import importlib.util, json
from app.refunds import refund_amount as baseline
path = 'tds/tasks/17-flawed-pr-review/inputs/refunds_candidate.py'
spec = importlib.util.spec_from_file_location('candidate', path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
cases = json.load(open('tds/tasks/17-flawed-pr-review/inputs/review-cases.json'))['inputs'] + [[12500, 12.5]]
for original, requested in cases:
    results = []
    for function in (baseline, module.refund_amount):
        try: results.append(function(original, requested))
        except Exception as error: results.append(type(error).__name__ + ': ' + str(error))
    print(repr((original, requested)), 'baseline=', results[0], 'proposed=', results[1])
PYDEMO
```

4. **Verify the result.** Give an approve or request-changes verdict based on consequential behavior. This is a local review artifact; do not post a live GitHub comment or edit the candidate branch.

5. **Save and review the handoff.** Finish `report.md` in `tds/tasks/17-flawed-pr-review/outcomes/17.1/`. Save or export `refund-review-findings.ods`, `refund-pr-review.pdf`, `refund-review-demonstration.md` to the same folder using the named apps. Reopen every output, check the quality boxes above, and confirm the folder contents:

```sh
ls -lh tds/tasks/17-flawed-pr-review/outcomes/17.1
git status --short
```

Keep the short introduction and complete on-screen process within 15:00–45:59. Narrate what, where, and why; keep task content visible and do not show AI interaction during the recording.
