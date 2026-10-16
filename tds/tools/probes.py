"""Observation tools, not acceptance tests. Most probes use disposable databases."""
import json
import os
import sqlite3
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from threading import Barrier
from unittest.mock import patch

def run(number, capture_directory=None):
    from app import auth, db, orders, payments, search, retries, wallet, worker, migration
    from app.billing import invoice_total
    from app.provider import ScriptedProvider, ProviderFailure
    if number in {3,14,17,18,20}:
        print(json.dumps({"status": "unavailable", "reason": "no_automated_diagnostic"}, indent=2))
        return
    if number==11:
        print(json.dumps({"status": "unavailable", "reason": "benchmark_required"}, indent=2))
        return
    with tempfile.TemporaryDirectory() as folder, patch.dict(os.environ,{"LAB_DB":str(Path(folder)/"probe.sqlite3"),"LAB_NOW":"2026-10-06T09:00:00Z","LAB_TICK":"0"}):
        db.initialize()
        if number==1:
            sid,state=auth.start_provider()
            result={"callback_with_cookie":auth.finish_provider(sid,state,"synthetic-ada")}
        elif number==2:
            result={}
            for identifier in ["ord_expired","ord_boundary","ord_before"]:
                try: result[identifier]=orders.pay(identifier,1)
                except orders.DomainError as exc: result[identifier]={"status":exc.status,"code":exc.code}
        elif number==4:
            result={"all_ids":[r["id"] for r in orders.list_orders(1)],"page_1":[r["id"] for r in orders.page_orders(1,1,2)],"page_2":[r["id"] for r in orders.page_orders(1,2,2)]}
        elif number==5:
            result={term:[r["id"] for r in search.search_orders(1,term)] for term in ["active"," ACTIVE "," active "]}
        elif number==6:
            result={}
            for label,amount,response in [("bad_input",0,{"status":200}),("provider_down",12500,{"status":503,"code":"unavailable"}),("decline",12500,{"status":402,"code":"card_declined"}),("success",12500,{"status":200,"payment_id":"p1"})]:
                provider=ScriptedProvider([response]); result[label]={"response":payments.charge(amount,provider),"provider_calls":len(provider.calls)}
        elif number==7:
            event={"id":"evt_race","order_id":"ord_active","amount_minor":12500,"currency":"NGN","type":"payment.succeeded"}
            barrier=Barrier(2)
            with ThreadPoolExecutor(max_workers=2) as executor:
                futures=[executor.submit(payments.handle_webhook,event,lambda:barrier.wait(timeout=5)) for _ in range(2)]
                deliveries=[]
                for future in futures:
                    try: deliveries.append(future.result(timeout=10))
                    except Exception as exc: deliveries.append({"exception":type(exc).__name__,"message":str(exc)})
            with db.connect() as conn:
                result={"deliveries":deliveries,"payment_rows":conn.execute("SELECT COUNT(*) FROM payments WHERE event_id=?",(event["id"],)).fetchone()[0],"notification_rows":conn.execute("SELECT COUNT(*) FROM notification_outbox WHERE event_id=?",(event["id"],)).fetchone()[0]}
                result["receipt_rows"]=conn.execute("SELECT COUNT(*) FROM webhook_receipts WHERE event_id=?",(event["id"],)).fetchone()[0]
                result["order_version"]=conn.execute("SELECT version FROM orders WHERE id=?",(event["order_id"],)).fetchone()[0]
            sequential=dict(event,id="evt_sequential",order_id="ord_before")
            result["sequential_deliveries"]=[payments.handle_webhook(sequential),payments.handle_webhook(sequential)]
            with db.connect() as conn:
                result["sequential_effects"]={
                    "payment_rows":conn.execute("SELECT COUNT(*) FROM payments WHERE event_id=?",(sequential["id"],)).fetchone()[0],
                    "notification_rows":conn.execute("SELECT COUNT(*) FROM notification_outbox WHERE event_id=?",(sequential["id"],)).fetchone()[0],
                    "receipt_rows":conn.execute("SELECT COUNT(*) FROM webhook_receipts WHERE event_id=?",(sequential["id"],)).fetchone()[0],
                    "order_version":conn.execute("SELECT version FROM orders WHERE id=?",(sequential["order_id"],)).fetchone()[0]}
        elif number==8:
            result={}
            for order_id,response in [("ord_cancelled",{"observation_id":"obs_801","status":"succeeded","observed_at":"2026-10-06T09:01:00Z","amount_minor":8400,"currency":"NGN"}),("ord_paid",{"observation_id":"obs_802","status":"failed","observed_at":"2026-10-06T08:44:00Z","amount_minor":9900,"currency":"NGN"})]:
                result[order_id]={"before":orders.get_order(order_id,1),"returned":payments.reconcile_provider(order_id,response),"after":orders.get_order(order_id,1)}
        elif number==9:
            provider=ScriptedProvider([{"status":400,"code":"invalid_request"},{"status":200,"payment_id":"p2"}]); sleeps=[]
            try: outcome=retries.charge_with_retry(provider,12500,"charge-001",sleeps.append)
            except ProviderFailure as exc: outcome={"status":exc.status,"code":exc.code}
            result={"outcome":outcome,"calls":provider.calls,"sleep_seconds":sleeps}
        elif number==10:
            from app.http import application
            result={}
            for uid in [1,2]:
                sid=auth.create_session(uid)
                status,_,body=application("GET","/api/orders/ord_ben",{"Cookie":auth.cookie(sid)})
                result[str(uid)]={"http_status":status,"body":body}
        elif number==12:
            with db.connect() as conn: before=[dict(r) for r in conn.execute("SELECT * FROM customers ORDER BY id")]
            try: migration.migrate(); outcome="completed"
            except Exception as exc: outcome=f"{type(exc).__name__}: {exc}"
            with db.connect() as conn: after=[dict(r) for r in conn.execute("SELECT * FROM customers ORDER BY id")]
            result={"migration":outcome,"before":before,"after":after}
        elif number==13:
            result=[wallet.reconcile(1),wallet.reconcile(2)]
        elif number==15:
            result={"before":orders.get_order("ord_paid",1),"transition":orders.transition("ord_paid",1,"pending_payment"),"after":orders.get_order("ord_paid",1)}
        elif number==16:
            result=[{"input":[amount,tier,coupon,delivery],"output":invoice_total(amount,tier,coupon,delivery)} for amount,tier,coupon,delivery in [(10000,"standard",None,"pickup"),(10000,"member","WELCOME","courier"),(16000,"standard",None,"courier"),(1,"member","WELCOME","pickup")]]
        elif number==19:
            worker.control("transient",2)
            result={"ticks":[worker.tick() for _ in range(3)],"jobs":worker.status()}
        else:
            raise SystemExit("Unknown task")
        if capture_directory:
            capture = Path(capture_directory)
            capture.mkdir(parents=True, exist_ok=False)
            with db.connect() as source, sqlite3.connect(str(capture/"observed.sqlite3")) as target:
                source.backup(target)
            (capture/"observation.json").write_text(json.dumps({
                "workstream":number,"clock":os.environ["LAB_NOW"],
                "database":"observed.sqlite3","database_scope":"temporary_copy","observation":result
            },indent=2)+"\n")
        print(json.dumps(result,indent=2))
