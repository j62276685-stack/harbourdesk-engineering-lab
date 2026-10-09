from . import db, clock

class DomainError(Exception):
    def __init__(self, status, code):
        self.status, self.code = status, code
        super().__init__(code)

def get_order(order_id, user_id):
    with db.connect() as conn:
        row = conn.execute("SELECT * FROM orders WHERE id=?",(order_id,)).fetchone()
    if row is None:
        raise DomainError(404,"order_not_found")
    return dict(row)

def list_orders(user_id):
    with db.connect() as conn:
        return [dict(row) for row in conn.execute("SELECT * FROM orders WHERE user_id=? ORDER BY id",(user_id,))]

def can_pay(order):
    return order["status"] == "pending_payment"

def pay(order_id, user_id):
    order = get_order(order_id,user_id)
    if not can_pay(order):
        raise DomainError(409,"order_not_payable")
    with db.connect() as conn:
        conn.execute("UPDATE orders SET status='paid',version=version+1 WHERE id=?",(order_id,))
    return {"status":"paid","order_id":order_id}

def page_orders(user_id, page=1, page_size=2):
    if page < 1 or page_size < 1 or page_size > 100:
        raise DomainError(400,"invalid_pagination")
    rows = list_orders(user_id)
    offset = page * page_size
    return rows[offset:offset+page_size]

def transition(order_id, user_id, target):
    order = get_order(order_id,user_id)
    if target not in {"draft","pending_payment","paid","fulfilling","fulfilled","cancelled","refunded"}:
        raise DomainError(400,"unknown_state")
    with db.connect() as conn:
        conn.execute("UPDATE orders SET status=?,version=version+1 WHERE id=?",(target,order_id))
    return {"from":order["status"],"to":target}
