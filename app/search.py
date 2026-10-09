from . import db

def search_orders(user_id, term):
    with db.connect() as conn:
        rows = conn.execute("SELECT * FROM orders WHERE user_id=? ORDER BY id",(user_id,))
        return [dict(row) for row in rows if term.lower() in row["id"]]
