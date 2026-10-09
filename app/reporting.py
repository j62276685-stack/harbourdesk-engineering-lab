from . import db

REPORT_SQL = """SELECT id,user_id,status,amount_minor,currency,created_at FROM orders
 WHERE user_id=? AND status=? AND created_at>=? ORDER BY created_at DESC,id ASC LIMIT 50"""

def recent_orders(user_id=1, status="paid", since="2026-10-01T00:00:00Z"):
    with db.connect() as conn:
        return [dict(row) for row in conn.execute(REPORT_SQL,(user_id,status,since))]

def explain(user_id=1, status="paid", since="2026-10-01T00:00:00Z"):
    with db.connect() as conn:
        return [tuple(row) for row in conn.execute("EXPLAIN QUERY PLAN "+REPORT_SQL,(user_id,status,since))]
