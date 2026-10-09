import os
import sqlite3
from pathlib import Path

def database_path():
    return Path(os.environ.get("LAB_DB", "runtime/lab.sqlite3"))

def connect(path=None):
    conn = sqlite3.connect(path or database_path(), timeout=5)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys=ON")
    conn.execute("PRAGMA busy_timeout=5000")
    return conn

def initialize(path=None):
    path = Path(path or database_path())
    if path.exists():
        raise FileExistsError(f"Database already exists: {path}. Preserve it or choose LAB_DB for a fresh copy.")
    path.parent.mkdir(parents=True, exist_ok=True)
    with connect(path) as conn:
        conn.execute("PRAGMA journal_mode=WAL")
        conn.executescript(Path(__file__).with_name("schema.sql").read_text())
        conn.executemany("INSERT INTO users VALUES(?,?,?)", [(1,"ada@example.test","Ada"),(2,"ben@example.test","Ben")])
        conn.executemany("INSERT INTO orders VALUES(?,?,?,?,?,?,?,?,?)", [
            ("ord_active",1,"pending_payment",12500,"NGN","2026-10-06T09:10:00Z","2026-10-06T08:55:00Z",None,0),
            ("ord_expired",1,"pending_payment",8400,"NGN","2026-10-06T08:59:59Z","2026-10-06T08:40:00Z",None,0),
            ("ord_boundary",1,"pending_payment",8400,"NGN","2026-10-06T09:00:00Z","2026-10-06T08:40:00Z",None,0),
            ("ord_before",1,"pending_payment",8400,"NGN","2026-10-06T09:00:01Z","2026-10-06T08:40:00Z",None,0),
            ("ord_ben",2,"pending_payment",22000,"NGN","2026-10-06T09:20:00Z","2026-10-06T08:56:00Z",None,0),
            ("ord_cancelled",1,"cancelled",8400,"NGN","2026-10-06T09:10:00Z","2026-10-06T08:45:00Z",None,1),
            ("ord_paid",1,"paid",9900,"NGN","2026-10-06T09:10:00Z","2026-10-06T08:45:00Z","succeeded",1),
        ])
        conn.executemany("INSERT INTO wallet_accounts VALUES(?,?)", [(1,17200),(2,5000)])
        conn.executemany("INSERT INTO wallet_entries VALUES(?,?,?,?,?,?)", [
            ("le_001",1,20000,"opening:1","2026-10-05T09:00:00Z","Opening credit"),
            ("le_002",1,-3000,"purchase:101","2026-10-05T10:00:00Z","Purchase"),
            ("le_003",1,1200,"refund:101","2026-10-05T11:00:00Z","Partial refund"),
            ("le_004",2,5000,"opening:2","2026-10-05T09:00:00Z","Opening credit"),
        ])
        conn.executemany("INSERT INTO customers VALUES(?,?,?,?,?)", [
            ("c01"," Ada@Example.test ","+234800000001","crm-01","2026-10-01T09:00:00Z"),
            ("c02","ada@example.test","0800000001","crm-02","2026-10-02T09:00:00Z"),
            ("c03","BEN@example.test",None,"crm-03","2026-10-01T09:00:00Z"),
            ("c04",None,"+234800000004","crm-04","2026-10-01T09:00:00Z"),
            ("c05","","+234800000005","crm-05","2026-10-01T09:00:00Z"),
            ("c06","not-an-email","+234800000006","crm-06","2026-10-01T09:00:00Z"),
            ("c07"," ada@example.test ",None,"crm-07","2026-10-03T09:00:00Z"),
            ("c08","chidi@example.test","+234800000008","crm-08","2026-10-01T09:00:00Z"),
        ])
        conn.executemany("INSERT INTO notification_outbox(event_id,user_id,channel,payload,available_at) VALUES(?,?,?,?,?)", [
            ("notice-1",1,"email",'{"order_id":"ord_paid"}',"2026-10-06T08:40:00Z"),
            ("notice-2",2,"email",'{"order_id":"ord_ben"}',"2026-10-06T08:41:00Z"),
        ])
        conn.execute("INSERT INTO worker_state VALUES(1,'healthy',0)")
    return path
