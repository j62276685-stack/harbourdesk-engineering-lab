# Task materials

This folder contains the task [index](tasks/INDEX.md), [session goals](sessions), inputs, workspaces, report [template](docs/REPORT-TEMPLATE.md), and recording tools. All workspaces edit the same [HarbourDesk application](../README.md) and use its shared database.

1. Read the brief and session goal from the [task index](tasks/INDEX.md) on your guide computer, then open the linked workspace on your development computer. VS Code shows only HarbourDesk; briefs, goals, inputs, and recording tools stay in `tds` and are excluded from Explorer and Search.
2. Before recording, select the session on the development computer with `./tds/lab start 01 --session 01.1` from the project directory. This prepares the recording metadata and source baseline. Session selection belongs to this guide, so it is not listed among the application’s VS Code commands.
3. Use **Terminal → Run Task → Start application** or **Run tests** as needed. Investigate the issue, and save the required deliverables in the task's `outcomes/` folder.
4. Run the relevant checks and review your changes before moving to the next task.

The task CLI is `./tds/lab` from the project directory. For example: `./tds/lab serve`, `./tds/lab test`, or `./tds/lab record database`. Run `./tds/lab list` for the task list.

## Interpreting diagnostics

Probe output contains observations only, without coaching or next steps. An observation is not an acceptance verdict. Probes run against a temporary database; recorded probes save that database as `observed.sqlite3` and identify its scope in `observation.json`.

- The login probe checks a callback with a supplied cookie. It cannot simulate browser cookie policy. Use `./tds/lab serve` and a real browser to investigate the cross-site journey.
- The notification probe uses a temporary queue. Use `./tds/lab worker` for the runbook drill against the application database.
- Document and Git investigations return `no_automated_diagnostic`; use their briefs and supplied evidence.
- The reporting probe returns `benchmark_required`. Run `./tds/lab seed-large --rows 150000`, then `./tds/lab benchmark`, and retain the query plan, result digest, and measurements.

Get each Idea approved in Odin before recording its Studio task. Inputs are fictional and were prepared before recording.
