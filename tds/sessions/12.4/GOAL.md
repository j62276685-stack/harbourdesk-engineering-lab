# 12.4 — Exercise migration rollback and make a cutover recommendation

**Role:** Data migration engineer

**Purpose:** Turn a messy import into auditable customer identities with a recovery path.

**Stakeholder:** Customer-data owner and release reviewer.

## Task description

I am investigating whether the proposed customer migration can recover from an interruption. My goal is to provide the release reviewer with a tested rollback procedure and an evidence-based recommendation on whether the migration is ready for cutover.

## Final deliverable

- `report.md` — use the [report template](../../docs/REPORT-TEMPLATE.md).
- `migration-recovery-checks.ods`
- `migration-recovery-evidence.json`
- `migration-cutover-verdict.pdf`

## Quality checks

- [ ] A named interruption and an actual restore are demonstrated.
- [ ] Original schema/raw rows are recoverable and compared.
- [ ] A rerun has explicit outcomes and no unexplained loss/duplication.
- [ ] The cutover verdict is evidence-backed, including a hold decision if checks fail.

**Apps:** Visual Studio Code, DB Browser for SQLite, LibreOffice.

**Recording:** Aim for 30:00 including the intro; allowed length 15:00–45:59.

**Starting dependency:** A frozen [12.3](../12.3/GOAL.md) candidate migration and pre-migration disposable backup are required.

## Workflow

1. Inspect the frozen migration and choose one meaningful interruption/cutover boundary.
2. Execute the bounded failure/recovery drill and compare restored schema/rows with the original using DB Browser.
3. In LibreOffice complete the recovery evidence table and write the release recommendation with remaining risks.

## Recording script

Open the [Task 12 workspace](../../workspaces/12-messy-migration.code-workspace) in VS Code. Run commands from its Application terminal; keep that terminal open. Follow the steps in order. Inputs and source: [task brief](../../tasks/12-messy-migration/BRIEF.md), [legacy-customers.csv](../../tasks/12-messy-migration/inputs/legacy-customers.csv), [legacy-customers.json](../../tasks/12-messy-migration/inputs/legacy-customers.json), [target-contract.md](../../tasks/12-messy-migration/inputs/target-contract.md), [migration.py](../../../app/migration.py), [schema.sql](../../../app/schema.sql), [db.py](../../../app/db.py).

1. **Set up the session and output folder.** Copy the report template only if a report does not already exist.

```sh
./tds/lab start 12 --session 12.4
mkdir -p tds/tasks/12-messy-migration/outcomes/12.4
cp -n tds/docs/REPORT-TEMPLATE.md tds/tasks/12-messy-migration/outcomes/12.4/report.md
git status --short
```

2. **Reproduce and capture the baseline.** Freeze the candidate migration and copy a disposable pre-migration database before the drill. Choose a failure point after some work but before commit/cutover.

Run the baseline commands in the Application terminal:

```sh
./tds/lab probe 12
LAB_DB=tds/tasks/12-messy-migration/outcomes/12.4/pre-migration.sqlite3 ./tds/lab init
cp tds/tasks/12-messy-migration/outcomes/12.4/pre-migration.sqlite3 tds/tasks/12-messy-migration/outcomes/12.4/backup.sqlite3
```

3. **Investigate and create the deliverable.** Inject the failure in a test, then compare schema, row counts, and raw records before and after rollback in DB Browser. Restore the copied database and rerun the candidate only when the prior state is verified.

4. **Verify the result.** In Calc record backup, failure, rollback, restore, repeat-run, and release decision. Do not claim production cutover from this local drill.

Run the verification commands. Restore only the disposable database after the injected-failure test has proved rollback:

```sh
./tds/lab test
cp tds/tasks/12-messy-migration/outcomes/12.4/backup.sqlite3 tds/tasks/12-messy-migration/outcomes/12.4/restored.sqlite3
LAB_DB=tds/tasks/12-messy-migration/outcomes/12.4/restored.sqlite3 ./tds/lab migrate
```

5. **Save and review the handoff.** Finish `report.md` in `tds/tasks/12-messy-migration/outcomes/12.4/`. Save or export `migration-recovery-checks.ods`, `migration-recovery-evidence.json`, `migration-cutover-verdict.pdf` to the same folder using the named apps. Reopen every output, check the quality boxes above, and confirm the folder contents:

```sh
ls -lh tds/tasks/12-messy-migration/outcomes/12.4
git status --short
```

Keep the short introduction and complete on-screen process within 15:00–45:59. Narrate what, where, and why; keep task content visible and do not show AI interaction during the recording.
