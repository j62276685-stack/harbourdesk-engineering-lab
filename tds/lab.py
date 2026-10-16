"""One HarbourDesk application with task-specific workspace views."""
import argparse
import hashlib
import json
import os
import shutil
import statistics
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TDS_ROOT = ROOT / "tds"
os.chdir(ROOT)
sys.path.insert(0, str(ROOT))
if sys.version_info < (3, 9):
    raise SystemExit("Python 3.9+ is required.")

def initialize_if_missing():
    from app import db
    if not db.database_path().exists():
        db.initialize()

def task_directory(number):
    directory = next(iter(sorted((TDS_ROOT / "tasks").glob(f"{number:02d}-*"))), None)
    if directory is None:
        raise SystemExit("Choose a task from 1 to 20.")
    return directory

def task_context():
    selected = TDS_ROOT / "runtime/current-task.json"
    saved = json.loads(selected.read_text()) if selected.exists() else {}
    override = os.environ.get("HD_TASK")
    try:
        number = int(override) if override else int(saved["number"])
    except (ValueError, KeyError):
        raise SystemExit("Choose a task with ./tds/lab start NN, or open its workspace.")
    task_directory(number)
    session = saved.get("session") if saved.get("number") == number else None
    return {"number": number, "session": session, "clock": "2026-10-06T09:00:00Z"}

def selected_number():
    return task_context()["number"]

def start(number, session_id=None):
    task = task_directory(number)
    goal = TDS_ROOT / "sessions" / str(session_id) / "GOAL.md" if session_id else task / "BRIEF.md"
    if session_id and (not goal.is_file() or not session_id.startswith(f"{number:02d}.")):
        raise SystemExit("The session must belong to the task, for example 01.1.")
    runtime = TDS_ROOT / "runtime"
    runtime.mkdir(exist_ok=True)
    metadata = {"number": number, "session": session_id, "clock": "2026-10-06T09:00:00Z"}
    (runtime / "current-task.json").write_text(json.dumps(metadata, indent=2) + "\n")
    baselines = runtime / "task-baselines"
    baselines.mkdir(exist_ok=True)
    baseline = baselines / f"{session_id or f'{number:02d}'}.txt"
    if not baseline.exists():
        result = git("rev-parse", "HEAD", check=False)
        if result.returncode == 0:
            baseline.write_text(result.stdout.strip() + "\n")
    print(f"Workspace: {TDS_ROOT / 'workspaces' / (task.name + '.code-workspace')}\nRead: {goal}\nShared application: {ROOT}\nDatabase: {ROOT / 'runtime/lab.sqlite3'}")


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
    if selected_number() != 17:
        raise SystemExit("Select task 17 first: ./tds/lab start 17")
    if git("status", "--porcelain", "--", "app", "web", "tests").stdout.strip():
        raise SystemExit("Commit your application changes before preparing the review branches.")
    for branch in ("refund-baseline", "proposed-refund"):
        if git("show-ref", "--verify", f"refs/heads/{branch}", check=False).returncode == 0:
            raise SystemExit(f"Branch {branch} already exists; use it for the review.")
    # Build a candidate Git revision without checking out or replacing the shared application.
    import tempfile
    base = git("rev-parse", "HEAD").stdout.strip()
    candidate = task_directory(17) / "inputs/refunds_candidate.py"
    blob = git("hash-object", "-w", str(candidate)).stdout.strip()
    with tempfile.TemporaryDirectory() as temporary:
        environment = dict(os.environ, GIT_INDEX_FILE=str(Path(temporary) / "index"))
        def index_git(*arguments):
            return subprocess.run([git_executable(), *arguments], cwd=ROOT, env=environment, check=True, text=True, capture_output=True).stdout.strip()
        index_git("read-tree", base)
        index_git("update-index", "--add", "--cacheinfo", f"100644,{blob},app/refunds.py")
        candidate_tree = index_git("write-tree")
        commit = index_git("commit-tree", candidate_tree, "-p", base, "-m", "Propose support-form refund conversion")
    git("branch", "refund-baseline", base)
    git("branch", "proposed-refund", commit)
    print("Review refund-baseline and proposed-refund in GitHub Desktop. The shared application and current branch are unchanged.")

def setup_merge():
    if selected_number() != 18:
        raise SystemExit("This command is for task 18 only.")
    if git("status","--porcelain","--","app","web","tests").stdout.strip():
        raise SystemExit("Commit your application changes before preparing the delivery merge.")
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
            raise SystemExit(f"Benchmark data already present ({existing} rows). Keep this dataset for the before/after comparison.")
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
    p.add_argument("number", type=int); p.add_argument("--session")
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
        print((TDS_ROOT / "tasks/INDEX.md").read_text() if (TDS_ROOT / "tasks/INDEX.md").exists() else (ROOT / "README.md").read_text())
        return
    if args.command == "start":
        start(args.number, args.session); return
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
            migrate(); print("Migration completed.")
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
