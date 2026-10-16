"""Capture observations for manual review; no acceptance verdicts or code repairs."""
import datetime
import hashlib
import json
import os
import sqlite3
import subprocess
import sys
from pathlib import Path

def run(action, root, job=None):
    stamp=datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    from lab import task_context, task_directory
    metadata=task_context()
    output=task_directory(metadata["number"])/"outcomes"
    if metadata.get("session"): output=output/metadata["session"]
    folder=output/"evidence"/(stamp+"-"+action)
    folder.mkdir(parents=True,exist_ok=False)
    revision=subprocess.run([__import__("lab").git_executable(),"rev-parse","HEAD"],cwd=root,text=True,capture_output=True)
    (folder/"capture.json").write_text(json.dumps({"action":action,"session":metadata.get("session"),
        "workstream":metadata["number"],"captured_utc":stamp,"clock":os.environ.get("LAB_NOW",metadata["clock"]),
        "source_revision":revision.stdout.strip(),"source_modified":bool(__import__("lab").git("status","--porcelain","--","app","web","tests").stdout.strip()),
        "database_scope":"temporary_copy" if action=="probe" else "application_runtime"},indent=2)+"\n")
    if action=="probe":
        from tools.probes import run as probe
        probe(metadata["number"],folder/"probe")
        return 0
    if action=="database":
        from app import db
        with db.connect() as source, sqlite3.connect(str(folder/"runtime-copy.sqlite3")) as target:
            source.backup(target)
        print("Saved a consistent current database copy for inspection/export.")
        return 0
    if action=="diff":
        from lab import git
        baseline_key=metadata.get("session") or str(metadata["number"]).zfill(2)
        baseline=root/"tds/runtime/task-baselines"/(baseline_key+".txt")
        if not baseline.exists():
            raise SystemExit("Source baseline is not configured.")
        # Comparing the initial revision to the working tree includes committed edits as well as current tracked edits.
        result=git("diff","--binary",baseline.read_text().strip(),"--","app","web","tests")
        (folder/"source-changes.patch").write_text(result.stdout)
        (folder/"git-status.txt").write_text(git("status","--short").stdout)
        (folder/"source-history.txt").write_text(git("log","--oneline","--all","--decorate").stdout)
        untracked=git("ls-files","--others","--exclude-standard","--","app","web","tests").stdout.splitlines()
        if untracked:
            (folder/"untracked-source-files.txt").write_text("\n".join(untracked)+"\n")
            print("Untracked source files are listed in untracked-source-files.txt; the patch includes tracked changes only.")
        print("Saved source diff, status and history.")
        return 0
    commands={"tests":["test"],"benchmark":["benchmark","--runs","9"],
              "worker-status":["worker","status"],"worker-tick":["worker","tick"]}
    if action=="worker-requeue":
        if job is None: raise SystemExit("A job ID is required (--job).")
        commands[action]=["worker","requeue","--job",str(job)]
    result=subprocess.run([sys.executable,str(root/"tds/lab.py"),*commands[action]],cwd=root,text=True,capture_output=True)
    (folder/"stdout.txt").write_text(result.stdout)
    (folder/"stderr.txt").write_text(result.stderr)
    (folder/"result.json").write_text(json.dumps({"exit_code":result.returncode,
        "stdout_sha256":hashlib.sha256(result.stdout.encode()).hexdigest()},indent=2)+"\n")
    if action in {"benchmark","worker-status","worker-tick","worker-requeue"} and result.returncode==0:
        (folder/"observation.json").write_text(json.dumps(json.loads(result.stdout),indent=2)+"\n")
    print(result.stdout+result.stderr)
    print("Saved capture: "+str(folder))
    return result.returncode
