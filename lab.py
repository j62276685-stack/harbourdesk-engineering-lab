"""Run HarbourDesk and prepare independent task copies. No third-party packages."""
import argparse
import hashlib
import json
import os
import re
import shutil
import statistics
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
os.chdir(ROOT)
sys.path.insert(0, str(ROOT))
if sys.version_info < (3, 9):
    raise SystemExit("Python 3.9+ is required.")

def initialize_if_missing():
    from app import db
    if not db.database_path().exists():
        db.initialize()

def selected_number():
    path = ROOT / "exercise.json"
    if not path.exists():
        raise SystemExit("Choose a task with ./lab start NN, or supply its number to ./lab probe NN.")
    return json.loads(path.read_text())["number"]

def copy_task_document(source, target, task, destination, remove_sessions=False):
    text = source.read_text()
    if remove_sessions:
        text = text.split("\n## Task sessions", 1)[0].rstrip() + "\n"
    def relocate(match):
        label, link = match.groups()
        if link.startswith(("http:", "https:", "#")):
            return match.group(0)
        original = (source.parent / link).resolve()
        try:
            relative = original.relative_to(task / "inputs")
            mapped = destination / "evidence/inputs" / relative
        except ValueError:
            try:
                relative = original.relative_to(ROOT)
            except ValueError:
                return match.group(0)
            mapped = destination / relative
        if not mapped.exists() and original.is_file():
            return f"[{label}]({original})"
        return f"[{label}]({Path(os.path.relpath(mapped, target.parent)).as_posix()})"
    text = re.sub(r"\[([^\]]+)\]\(([^\)]+)\)", relocate, text)
    target.write_text(text)

def start(number, destination=None, session_id=None):
    if (ROOT / "exercise.json").exists():
        raise SystemExit("Create task copies from the project's top-level directory.")
    task = next(iter(sorted((ROOT / "tasks").glob(f"{number:02d}-*"))), None)
    if not task:
        raise SystemExit("Choose a task from 1 to 20.")
    goal = ROOT / "sessions" / str(session_id) / "GOAL.md" if session_id else task / "BRIEF.md"
    if session_id and (not goal.is_file() or not session_id.startswith(f"{number:02d}.")):
        raise SystemExit("The session must exist and belong to the chosen task, for example 01.1.")
    label = f"{session_id}-{task.name[3:]}" if session_id else task.name
    dest = Path(destination).expanduser().resolve() if destination else ROOT / "workspaces" / label
    if dest.exists():
        raise SystemExit(f"Destination already exists: {dest}. Use --destination for another copy.")
    dest.mkdir(parents=True)
    for name in ("app", "web", "tests", "tools", "docs", ".vscode"):
        shutil.copytree(ROOT / name, dest / name, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    for name in ("lab", "lab.py", ".gitignore"):
        shutil.copy2(ROOT / name, dest / name)
    shutil.copytree(task / "inputs", dest / "evidence/inputs")
    for source in (task / "inputs").glob("*.md"):
        copy_task_document(source, dest / "evidence/inputs" / source.name, task, dest)
    copy_task_document(task / "BRIEF.md", dest / "evidence/PROBLEM.md", task, dest, True)
    copy_task_document(goal, dest / "TASK.md", task, dest, not session_id)
    (dest / "exercise.json").write_text(json.dumps({"number": number, "session": session_id, "clock": "2026-10-06T09:00:00Z"}, indent=2) + "\n")
    (dest / "outcomes").mkdir()
    result = subprocess.run([sys.executable, str(dest / "lab.py"), "init"], cwd=dest)
    if result.returncode:
        raise SystemExit(result.returncode)
    git("init", "-b", "exercise", cwd=dest)
    git("config", "user.name", "HarbourDesk", cwd=dest)
    git("config", "user.email", "practice@example.test", cwd=dest)
    git("add", ".", cwd=dest)
    git("commit", "-m", "Task starting source", cwd=dest)
    (dest / "runtime/baseline-revision.txt").write_text(git("rev-parse", "HEAD", cwd=dest).stdout.strip() + "\n")
    print(f"Ready: {dest}\nOpen TASK.md, then run ./lab serve or use Terminal > Run Task in VS Code.")

def git_executable():
    explicit = os.environ.get("LAB_GIT")
    if explicit:
        return explicit
    system = shutil.which("git")
    if system:
        try:
            if subprocess.run([system,"--version"],capture_output=True,timeout=5).returncode == 0:
                return system
        except (OSError,subprocess.TimeoutExpired):
            pass
    bundled = Path.home()/".cache/codex-runtimes/codex-primary-runtime/dependencies/bin/fallback/git"
    return str(bundled) if bundled.exists() else (system or "git")

def git(*args, cwd=ROOT, check=True):
    return subprocess.run([git_executable(),*args],cwd=cwd,check=check,text=True,capture_output=True)

def setup_review():
    if json.loads((ROOT/"exercise.json").read_text())["number"] != 17:
        raise SystemExit("This command prepares the supplied task 17 candidate only.")
    if git("status","--porcelain","--","app","web","tests").stdout.strip():
        raise SystemExit("Use a fresh, clean workspace for the review candidate.")
    git("branch","refund-baseline")
    git("checkout","-b","proposed-refund")
    shutil.copy2(ROOT/"evidence/inputs/refunds_candidate.py",ROOT/"app/refunds.py")
    git("add","app/refunds.py")
    git("commit","-m","Propose support-form refund conversion")
    print("Local refund-baseline and proposed-refund revisions are ready for review. No review finding was supplied.")

def setup_merge():
    if json.loads((ROOT/"exercise.json").read_text())["number"] != 18:
        raise SystemExit("This command is for task 18 only.")
    if git("status","--porcelain","--","app","web","tests").stdout.strip():
        raise SystemExit("Workspace has changes. Preserve/commit them before preparing the merge; use a fresh task 18 workspace if needed.")
    base=git("rev-parse","HEAD").stdout.strip()
    git("checkout","-b","free-delivery")
    (ROOT/"app/shipping.py").write_text('def quote(subtotal_minor, region="local"):\n    return 0 if subtotal_minor >= 25000 else 1500\n')
    (ROOT/"tests/test_local_delivery.py").write_text('import unittest\nfrom app.shipping import quote\n\nclass LocalDeliveryTests(unittest.TestCase):\n    def test_local_threshold(self):\n        self.assertEqual(quote(24999),1500)\n        self.assertEqual(quote(25000),0)\n')
    git("add","app/shipping.py","tests/test_local_delivery.py")
    git("commit","-m","Waive local delivery at the qualifying subtotal")
    git("checkout","-b","remote-delivery",base)
    (ROOT/"app/shipping.py").write_text('def quote(subtotal_minor, region="local"):\n    return 3000 if region == "remote" else 1500\n')
    (ROOT/"tests/test_remote_delivery.py").write_text('import unittest\nfrom app.shipping import quote\n\nclass RemoteDeliveryTests(unittest.TestCase):\n    def test_remote_fee(self):\n        self.assertEqual(quote(10000,"remote"),3000)\n        self.assertEqual(quote(50000,"remote"),3000)\n')
    git("add","app/shipping.py","tests/test_remote_delivery.py")
    git("commit","-m","Charge remote delivery consistently")
    git("checkout","free-delivery")
    merge=git("merge","remote-delivery",check=False)
    print(merge.stdout+merge.stderr)
    if merge.returncode != 1 or not (ROOT/".git/MERGE_HEAD").exists():
        raise SystemExit("Expected a merge conflict but did not get one. Inspect git status.")
    print("Conflict ready in app/shipping.py. Resolve it, run both branch tests, then complete the merge.")

def seed_large(count):
    from app import db
    with db.connect() as conn:
        existing = conn.execute("SELECT COUNT(*) FROM orders WHERE id LIKE 'bench_%'").fetchone()[0]
        if existing:
            raise SystemExit(f"Benchmark data already present ({existing} rows). Use a fresh workspace/database for another size.")
        batch = []
        for i in range(count):
            batch.append((f"bench_{i:07d}",1 if i%5==0 else 2,"paid" if i%7==0 else "pending_payment",100+i%100000,"NGN",
                          "2026-12-01T00:00:00Z",f"2026-10-{1+i%6:02d}T{i%24:02d}:{i%60:02d}:{i%60:02d}Z",None,0))
        conn.executemany("INSERT INTO orders VALUES(?,?,?,?,?,?,?,?,?)",batch)
    print(f"Inserted {count} reproducible benchmark orders.")

def benchmark(runs):
    from app import db, reporting
    reporting.recent_orders()
    times=[]
    for _ in range(runs):
        before=time.perf_counter()
        rows=reporting.recent_orders()
        times.append((time.perf_counter()-before)*1000)
    encoded=json.dumps(rows,sort_keys=True,separators=(",",":")).encode()
    with db.connect() as conn:
        total=conn.execute("SELECT COUNT(*) FROM orders").fetchone()[0]
    print(json.dumps({"rows_in_database":total,"result_count":len(rows),"result_sha256":hashlib.sha256(encoded).hexdigest(),
                      "runs":runs,"median_ms":statistics.median(times),"samples_ms":times,"query_plan":reporting.explain()},indent=2))

def main():
    parser = argparse.ArgumentParser(description="HarbourDesk application and task tools")
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("list", "init", "test", "setup-review", "setup-merge", "migrate"):
        commands.add_parser(name)
    p = commands.add_parser("start")
    p.add_argument("number", type=int); p.add_argument("--session"); p.add_argument("--destination")
    for name in ("serve", "preview"):
        p = commands.add_parser(name)
        p.add_argument("--port", type=int, default=8010); p.add_argument("--provider-port", type=int, default=8011)
    p = commands.add_parser("probe"); p.add_argument("number", type=int, nargs="?")
    p = commands.add_parser("sql"); p.add_argument("statement")
    p = commands.add_parser("seed-large"); p.add_argument("--rows", type=int, default=150000)
    p = commands.add_parser("benchmark"); p.add_argument("--runs", type=int, default=9)
    p = commands.add_parser("worker")
    p.add_argument("action", choices=["status", "tick", "control", "requeue"])
    p.add_argument("--mode", default="healthy"); p.add_argument("--failures", type=int, default=0); p.add_argument("--job", type=int)
    p = commands.add_parser("record")
    p.add_argument("action", choices=["tests", "probe", "benchmark", "worker-status", "worker-tick", "worker-requeue", "database", "diff"])
    p.add_argument("--job", type=int)
    args = parser.parse_args()
    if args.command == "list":
        print((ROOT / "tasks/INDEX.md").read_text() if (ROOT / "tasks/INDEX.md").exists() else (ROOT / "TASK.md").read_text())
        return
    if args.command == "start":
        start(args.number, args.destination, args.session); return
    from app import db
    if args.command == "init":
        print(f"Initialized {db.initialize()}")
    elif args.command in {"serve", "preview"}:
        from urllib.request import urlopen
        try:
            with urlopen(f"http://localhost:{args.port}/health", timeout=1) as response:
                if json.load(response).get("service") == "HarbourDesk":
                    print(f"HarbourDesk is already running at http://localhost:{args.port}")
                    return
        except (OSError, ValueError):
            pass
        initialize_if_missing()
        from app.http import serve
        serve(args.port, args.provider_port)
    elif args.command == "test":
        raise SystemExit(subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"], cwd=ROOT).returncode)
    elif args.command == "probe":
        from tools.probes import run
        number = args.number if args.number is not None else selected_number()
        if not 1 <= number <= 20:
            raise SystemExit("Choose a task from 1 to 20.")
        run(number)
    elif args.command == "record":
        selected_number()
        initialize_if_missing()
        from tools.recording import run
        raise SystemExit(run(args.action, ROOT, args.job))
    elif args.command == "setup-review": setup_review()
    elif args.command == "setup-merge": setup_merge()
    else:
        initialize_if_missing()
        if args.command == "sql":
            with db.connect() as conn:
                cursor = conn.execute(args.statement)
                print(json.dumps([dict(row) for row in cursor.fetchall()], indent=2) if cursor.description else f"Affected rows: {cursor.rowcount}")
        elif args.command == "seed-large":
            if args.rows < 1: raise SystemExit("Rows must be positive.")
            seed_large(args.rows)
        elif args.command == "benchmark":
            if args.runs < 3: raise SystemExit("Use at least three runs.")
            benchmark(args.runs)
        elif args.command == "migrate":
            from app.migration import migrate
            migrate(); print("Migration completed; verify the rows against the task contract.")
        elif args.command == "worker":
            from app import worker
            if args.action == "status": result = worker.status()
            elif args.action == "tick": result = worker.tick()
            elif args.action == "control": result = worker.control(args.mode, args.failures)
            else:
                if args.job is None: raise SystemExit("Supply --job for requeue.")
                result = worker.requeue(args.job)
            print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
