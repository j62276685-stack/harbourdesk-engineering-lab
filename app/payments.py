import json
from . import db, clock
from .provider import ProviderFailure

def charge(amount_minor, provider, idempotency_key="demo-charge"):
    try:
        if not isinstance(amount_minor,int) or isinstance(amount_minor,bool) or amount_minor <= 0:
            raise ValueError("amount_minor must be a positive integer")
        return 200, provider.charge(amount_minor,idempotency_key)
    except (ValueError,ProviderFailure):
        return 400, {"code":"invalid_amount","message":"Enter a valid amount."}

def handle_webhook(event, after_lookup=None):
    with db.connect() as conn:
        seen = conn.execute("SELECT 1 FROM webhook_receipts WHERE event_id=?",(event["id"],)).fetchone()
    if seen:
        return {"duplicate":True}
    if after_lookup:
        after_lookup()
    with db.connect() as conn:
        conn.execute("INSERT INTO payments(event_id,order_id,amount_minor,currency,created_at) VALUES(?,?,?,?,?)",
                     (event["id"],event["order_id"],event["amount_minor"],event["currency"],clock.now().isoformat()))
        conn.execute("UPDATE orders SET status='paid',provider_status='succeeded',version=version+1 WHERE id=?",(event["order_id"],))
        conn.execute("INSERT INTO notification_outbox(event_id,user_id,channel,payload,available_at) SELECT ?,user_id,'email',?,? FROM orders WHERE id=?",
                     (event["id"],json.dumps({"order_id":event["order_id"]}),clock.now().isoformat(),event["order_id"]))
    with db.connect() as conn:
        conn.execute("INSERT OR IGNORE INTO webhook_receipts VALUES(?,?)",(event["id"],clock.now().isoformat()))
    return {"duplicate":False}

def reconcile_provider(order_id, response):
    mapping = {"succeeded":"paid","failed":"pending_payment","pending":"pending_payment"}
    with db.connect() as conn:
        conn.execute("UPDATE orders SET status=?,provider_status=?,version=version+1 WHERE id=?",
                     (mapping[response["status"]],response["status"],order_id))
    return {"status":mapping[response["status"]]}
