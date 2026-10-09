"""Account boundary checks for the customer portal; domain defects remain exercises."""
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from app import auth, db
from app.http import application

class AccountPreviewTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.env=patch.dict(os.environ,{"LAB_DB":str(Path(self.temp.name)/"account.sqlite3")})
        self.env.start()
        db.initialize()
    def tearDown(self):
        self.env.stop()
        self.temp.cleanup()
    def test_wallet_requires_login_and_separates_customers(self):
        self.assertEqual(application("GET","/api/wallet")[0],401)
        for uid,name,email,balance in [(1,"Ada","ada@example.test",17200),(2,"Ben","ben@example.test",5000)]:
            headers={"Cookie":auth.cookie(auth.create_session(uid))}
            status,_,profile=application("GET","/api/me",headers)
            self.assertEqual((status,profile["user_id"],profile["name"],profile["email"]),(200,uid,name,email))
            status,_,wallet=application("GET","/api/wallet",headers)
            self.assertEqual(status,200)
            self.assertEqual(wallet["balance_minor"],balance)
            self.assertTrue(wallet["entries"])
            self.assertTrue(all(entry["user_id"]==uid for entry in wallet["entries"]))
        # Reading the portal must not reconcile or rewrite the posted/cache data.
        with db.connect() as conn:
            self.assertEqual(conn.execute("SELECT balance_minor FROM wallet_accounts WHERE user_id=1").fetchone()[0],17200)
            self.assertEqual(conn.execute("SELECT COUNT(*) FROM wallet_audit").fetchone()[0],0)
    def test_logout_revokes_only_current_session(self):
        first,other=auth.create_session(1),auth.create_session(2)
        status,headers,result=application("POST","/auth/logout",{"Cookie":auth.cookie(first)})
        self.assertEqual(status,200)
        self.assertTrue(result["signed_out"])
        self.assertIn("Max-Age=0",headers["Set-Cookie"])
        self.assertIsNone(auth.current_user(auth.cookie(first)))
        self.assertEqual(auth.current_user(auth.cookie(other)),2)
        self.assertEqual(application("GET","/api/me",{"Cookie":auth.cookie(first)})[0],401)
    def test_failed_callback_preserves_http_error_for_html_and_api(self):
        target="/auth/callback?state=wrong&code=synthetic-ada"
        status,headers,payload=application("GET",target,{"Accept":"text/html"})
        self.assertEqual(status,401)
        self.assertIn("text/html",headers["Content-Type"])
        self.assertIn(b"Back to sign in",payload)
        status,_,payload=application("GET",target,{"Accept":"application/json"})
        self.assertEqual(status,401)
        self.assertEqual(payload["code"],"login_state_missing_or_invalid")

if __name__=="__main__": unittest.main()
