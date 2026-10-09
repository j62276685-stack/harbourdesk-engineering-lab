from . import db

def reconcile(user_id):
    with db.connect() as conn:
        account = conn.execute("SELECT balance_minor FROM wallet_accounts WHERE user_id=?",(user_id,)).fetchone()
        ledger = conn.execute("SELECT COALESCE(SUM(delta_minor),0) FROM wallet_entries WHERE user_id=?",(user_id,)).fetchone()[0]
    return {"user_id":user_id,"cached_balance_minor":account[0],"ledger_balance_minor":ledger,"difference_minor":account[0]-ledger}
