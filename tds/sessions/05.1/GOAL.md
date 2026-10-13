# 05.1 — Choose and deliver the smallest justified search repair

**Role:** Maintenance software engineer

**Purpose:** Repair pasted search terms while controlling change scope.

**Stakeholder:** Maintainer reviewing a small production-style patch.

## Task description

I am investigating a customer report that pasting a search term with surrounding spaces returns no orders. My goal is to provide the maintainer with the smallest verified repair and explain why it preserves search authorization and ordering.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `search-fix.patch`
- `search-options.ods`
- `search-maintainer-note.pdf`

## Quality checks

- [ ] Padded and unpadded queries give equivalent IDs.
- [ ] Empty/all-whitespace and case behavior follow the contract.
- [ ] The comparison explains a consequential tradeoff rather than merely counting lines.
- [ ] The selected patch is focused and legitimate ownership/no-match behavior is retained.

**Apps:** Visual Studio Code, Firefox, LibreOffice.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

## Workflow

1. Compare supplied padded/unpadded queries in Firefox and inspect the source path.
2. In LibreOffice create a small option/test matrix covering scope, contract risk and expected results.
3. Implement the chosen change in VS Code and verify whitespace, case, no-match and ownership results before exporting the handoff.

## Recording script

Open the [Task 05 workspace](../../workspaces/05-smallest-patch.code-workspace) in VS Code. Run commands from its Application terminal; keep that terminal open. Follow the steps in order. Inputs and source: [task brief](../../tasks/05-smallest-patch/BRIEF.md), [search-cases.json](../../tasks/05-smallest-patch/inputs/search-cases.json), [search.py](../../../app/search.py), [http.py](../../../app/http.py).

1. **Set up the session and output folder.** Copy the report template only if a report does not already exist.

```sh
./tds/lab start 05 --session 05.1
mkdir -p tds/tasks/05-smallest-patch/outcomes/05.1
cp -n tds/docs/REPORT-TEMPLATE.md tds/tasks/05-smallest-patch/outcomes/05.1/report.md
git status --short
```

2. **Reproduce and capture the baseline.** Run the search probe, then compare active, padded active, mixed case, blank, and no-match terms in Firefox using the supplied fixture.

For browser work, start the app in a second terminal with the command below. Open http://localhost:8010 in Firefox; use the example Ada or Ben account and the displayed practice password. Keep the server terminal open and stop it with Control-C when finished.

```sh
./tds/lab serve
```

Run the baseline commands in the Application terminal:

```sh
./tds/lab probe 5
```

3. **Investigate and create the deliverable.** In Calc compare normalizing once at the search boundary with changing each caller. Select the smaller contract-preserving change; trim the term in app/search.py while retaining case-insensitive matching, owned rows, and order.

4. **Verify the result.** Rerun the probe and tests. Check padded and unpadded IDs match, blank returns the caller’s owned list, and no-match plus Ben isolation remain correct.

Run the verification commands:

```sh
./tds/lab probe 5
./tds/lab test
```

Before committing this session’s code, export the reviewed change as the required patch:

```sh
git add -N -- tests
git diff HEAD --binary -- app/search.py tests > tds/tasks/05-smallest-patch/outcomes/05.1/search-fix.patch
```

5. **Save and review the handoff.** Finish `report.md` in `tds/tasks/05-smallest-patch/outcomes/05.1/`. Save or export `search-options.ods`, `search-maintainer-note.pdf` to the same folder using the named apps. Reopen every output, check the quality boxes above, and confirm the folder contents:

```sh
ls -lh tds/tasks/05-smallest-patch/outcomes/05.1
git status --short
```

Keep the short introduction and complete on-screen process within 15:00–45:59. Narrate what, where, and why; keep task content visible and do not show AI interaction during the recording.
