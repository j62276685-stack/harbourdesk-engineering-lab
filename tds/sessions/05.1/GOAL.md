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
