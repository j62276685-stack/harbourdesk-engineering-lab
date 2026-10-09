# HarbourDesk

A local customer portal for a fictional shop: orders, payment details, wallet history, and collection guidance. Python 3.9+ runs the application without additional packages. Git is needed to create independent task copies and for the review/merge tasks.

## Run the application

Double-click **HarbourDesk.command**, or open this folder in a terminal and run:

```sh
./lab serve
```

Open **http://localhost:8010** in Firefox. The local identity provider runs at **http://127.0.0.1:8011**. Stop the application with Control-C. The launcher creates the database on first use and preserves it on later launches.

| Account | Email | Password |
|---|---|---|
| Ada | ada@example.test | practice-only |
| Ben | ben@example.test | practice-only |

The database is `runtime/lab.sqlite3`. The default clock is fixed at 2026-10-06 09:00 UTC so the task cases stay reproducible. `LAB_NOW` sets another time; `LAB_TICK=1` advances it. `LAB_DB` selects a different database.

## Choose a task

Read the [task list](tasks/INDEX.md). Each task folder contains the **reported error or request**, relevant code, reproduction steps, required inputs and completion criteria. The linked session descriptions specify the scope, apps, outputs and checks. [Task 1.1](sessions/01.1/GOAL.md) contains the revised description.

For an independent task copy:

```sh
./lab start 01 --session 01.1
```

Open the printed folder and read `TASK.md` and `evidence/PROBLEM.md`. Work on its application files; save your deliverables in `outcomes/`. Existing task folders are never overwritten; use `--destination /absolute/path` for another attempt. Stop the running application before launching a task copy on the same ports.

## Files and checks

| Location | Purpose |
|---|---|
| `app/` | Python application, SQLite schema and seed data |
| `web/` | Customer portal and identity-provider interface |
| `tests/` | Existing behavior checks |
| `tasks/` | Twenty reported problems and their input files |
| `sessions/` | Thirty-nine task descriptions |
| `docs/` | Product rules, API and data dictionary needed for the tasks |
| `tools/`, [lab](lab), [lab.py](lab.py) | Launch, task preparation and evidence tools |

Run `./lab test` for the existing tests. Use VS Code’s **Terminal → Run Task** menu for launch, tests, and evidence capture. Capture actions require a selected task workspace and save files under `outcomes/evidence/`.

Task helpers: `./lab probe NN`; `./lab seed-large --rows 150000` and `./lab benchmark` for task 11; `./lab setup-review` for task 17; `./lab setup-merge` for task 18; and `./lab worker status|tick|control|requeue` for task 19. Worker control accepts `--mode healthy|transient|permanent --failures N`; requeue accepts `--job ID`.

The application retains the intentional errors described in the tasks. Passing existing tests does not establish that those errors have been repaired. The [product rules](docs/PRODUCT.md), [API](docs/API.md) and [data dictionary](docs/DATA-MODEL.md) define the expected behavior. All accounts and records are fictional, with no live payments or messages. Inputs were AI-generated before recording. Recording Ideas still need Odin approval before Studio creates their tasks.
