# HarbourDesk

One application containing the task errors. Work through them in order; each fix carries forward. All task workspaces edit the same code and use the same database.

## Run

Double-click [HarbourDesk.command](HarbourDesk.command), or run `./lab serve` from this folder. Open **http://localhost:8010** in Firefox. The identity provider runs at **http://127.0.0.1:8011**. Stop with Control-C and restart after changing Python code.

Python 3.9+ is required. Git is used for changes, review and merge tasks. No extra packages are needed.

| Account | Email | Password |
|---|---|---|
| Ada | ada@example.test | practice-only |
| Ben | ben@example.test | practice-only |

The shared database is `runtime/lab.sqlite3`. It is created once and kept between tasks. The clock defaults to 2026-10-06 09:00 UTC; `LAB_NOW` changes it and `LAB_TICK=1` advances it. Use a separate `LAB_DB` only for disposable experiments.

## Work through the tasks

1. Open a workspace from the [task list](tasks/INDEX.md) in VS Code.
2. Read its problem brief and session description. Start with [Task 1.1](sessions/01.1/GOAL.md).
3. Use **Terminal → Run Task → Select session** to choose the recording session. The command-line equivalent is `./lab start 01 --session 01.1`.
4. Inspect and fix the files under **Application**. Save outputs in the task's `outcomes/` folder; captures go there automatically.
5. Verify the fix and commit it in GitHub Desktop before moving to the next task.

The workspace folders are views of this project. Selecting a task keeps the current code, database and earlier fixes.

## Checks and task tools

Run `./lab test` or use the task menu for tests and evidence capture. Probes use disposable data to inspect your current code. Database captures and worker controls use the shared runtime database.

- Task 11: `./lab seed-large --rows 150000`, then `./lab benchmark`.
- Task 17: select task 17, then `./lab setup-review`; compare its review branches without changing the application.
- Task 18: select task 18, commit earlier work, then `./lab setup-merge`; resolve the conflict in the shared application.
- Task 19: use `./lab worker status`, `tick`, `control --mode transient --failures 2`, or `requeue --job ID`.

Read the [product rules](docs/PRODUCT.md), [API](docs/API.md) and [data dictionary](docs/DATA-MODEL.md) when needed. Existing tests cover working behavior; each task supplies checks for its error. Accounts and records are fictional. Inputs were AI-generated before recording. Get each Idea approved in Odin before recording its Studio task.
