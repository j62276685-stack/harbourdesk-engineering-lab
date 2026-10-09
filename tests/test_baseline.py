import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from app import auth, db, orders, payments, search, wallet
from app.billing import invoice_total
from app.http import application
from app.provider import ScriptedProvider
from app.refunds import refund_amount

class BaselineTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.env = patch.dict(os.environ,{"LAB_DB":str(Path(self.temp.name)/"test.sqlite3"),"LAB_NOW":"2026-10-06T09:00:00Z","LAB_TICK":"0"})
        self.env.start()
        db.initialize()
    def tearDown(self):
        self.env.stop()
        self.temp.cleanup()
    def test_seed_ownership_listing(self):
        self.assertTrue(all(o["user_id"] == 1 for o in orders.list_orders(1)))
        self.assertEqual([o["id"] for o in orders.list_orders(2)],["ord_ben"])
    def test_valid_local_login(self):
        status,headers,data = application("POST","/auth/login",body=json.dumps({"email":"ada@example.test","password":"practice-only"}).encode())
        self.assertEqual(status,200)
        self.assertEqual(auth.current_user(headers["Set-Cookie"]),1)
    def test_callback_checks_state_and_replay(self):
        sid,state = auth.start_provider()
        self.assertFalse(auth.finish_provider(sid,"wrong-state","synthetic-ada"))
        self.assertTrue(auth.finish_provider(sid,state,"synthetic-ada"))
        self.assertFalse(auth.finish_provider(sid,state,"synthetic-ada"))
    def test_authenticated_routes_and_bad_json(self):
        self.assertEqual(application("GET","/api/orders")[0],401)
        self.assertEqual(application("POST","/auth/login",body=b"{")[0],400)
        self.assertEqual(application("POST","/auth/login",body=b"[]")[0],400)
    def test_active_payment(self):
        self.assertEqual(orders.pay("ord_active",1)["status"],"paid")
    def test_already_paid_not_payable(self):
        with self.assertRaises(orders.DomainError): orders.pay("ord_paid",1)
    def test_simple_search(self):
        self.assertEqual(search.search_orders(1,"active")[0]["id"],"ord_active")
    def test_valid_provider_charge(self):
        code,data = payments.charge(12500,ScriptedProvider([{"status":200,"payment_id":"p1"}]))
        self.assertEqual((code,data["payment_id"]),(200,"p1"))
    def test_sequential_webhook_replay(self):
        event={"id":"evt_test","order_id":"ord_active","amount_minor":12500,"currency":"NGN","type":"payment.succeeded"}
        self.assertFalse(payments.handle_webhook(event)["duplicate"])
        self.assertTrue(payments.handle_webhook(event)["duplicate"])
        with db.connect() as conn: self.assertEqual(conn.execute("SELECT COUNT(*) FROM payments").fetchone()[0],1)
    def test_ben_wallet_consistent(self):
        self.assertEqual(wallet.reconcile(2)["difference_minor"],0)
    def test_billing_preserved_examples(self):
        self.assertEqual(invoice_total(10000),10750)
        self.assertEqual(invoice_total(10000,"member","WELCOME","courier"),11288)
        self.assertEqual(invoice_total(16000,"standard",None,"courier"),17200)
    def test_refund_contract(self):
        self.assertEqual(refund_amount(12500,5000),5000)
        for bad in [0,-1,12501,1.5,True]:
            with self.assertRaises(ValueError): refund_amount(12500,bad)

if __name__ == "__main__": unittest.main()
