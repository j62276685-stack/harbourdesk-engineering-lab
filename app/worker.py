import json
from . import db, clock

def control(mode="healthy", failures=0):
    if mode not in {"healthy","transient","permanent"}:
        raise ValueError("Mode must be healthy, transient or permanent")
    with db.connect() as conn:
        conn.execute("UPDATE worker_state SET mode=?,failure_remaining=? WHERE id=1",(mode,failures))

def tick():
    with db.connect() as conn:
        row = conn.execute("SELECT * FROM notification_outbox WHERE status='pending' ORDER BY id LIMIT 1").fetchone()
        if not row:
            return {"result":"idle"}
        state = conn.execute("SELECT * FROM worker_state WHERE id=1").fetchone()
        conn.execute("UPDATE notification_outbox SET attempts=attempts+1 WHERE id=?",(row["id"],))
        if state["mode"] == "permanent" or state["failure_remaining"] > 0:
            conn.execute("UPDATE worker_state SET failure_remaining=MAX(0,failure_remaining-1) WHERE id=1")
            conn.execute("UPDATE notification_outbox SET last_error='provider_unavailable' WHERE id=?",(row["id"],))
            return {"result":"failed","job_id":row["id"]}
        conn.execute("UPDATE notification_outbox SET status='sent',last_error=NULL WHERE id=?",(row["id"],))
        return {"result":"sent","job_id":row["id"]}

def status():
    with db.connect() as conn:
        return [dict(row) for row in conn.execute("SELECT * FROM notification_outbox ORDER BY id")]

def requeue(job_id):
    with db.connect() as conn:
        conn.execute("UPDATE notification_outbox SET status='pending',last_error=NULL WHERE id=? AND status!='sent'",(job_id,))
