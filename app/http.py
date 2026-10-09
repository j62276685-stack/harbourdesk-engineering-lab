import html
import json
import os
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlencode, urlparse
from . import auth, clock, db, orders, payments, search
from .provider import ScriptedProvider

def application(method, target, headers=None, body=b"", provider_port=8011):
    headers = {k.lower():v for k,v in (headers or {}).items()}
    url = urlparse(target)
    query = parse_qs(url.query)
    path = url.path
    extra = {}
    if path in {"/","/static/app.js","/static/style.css","/favicon.svg"} and method == "GET":
        name = {"/":"index.html","/static/app.js":"app.js","/static/style.css":"style.css","/favicon.svg":"favicon.svg"}[path]
        mime = {"index.html":"text/html","app.js":"text/javascript","style.css":"text/css","favicon.svg":"image/svg+xml"}[name]
        return 200,{"Content-Type":mime+"; charset=utf-8"},Path(__file__).parent.parent.joinpath("web",name).read_bytes()
    if path == "/health" and method == "GET":
        return 200,extra,{"status":"ok","service":"HarbourDesk","clock":clock.now().isoformat()}
    if path == "/auth/start" and method == "GET":
        sid, state = auth.start_provider()
        params = urlencode({"state":state})
        return 302,{"Set-Cookie":auth.cookie(sid),"Location":f"http://127.0.0.1:{provider_port}/authorize?{params}"},b""
    if path == "/auth/callback" and method == "GET":
        success = auth.finish_provider(auth.session_id(headers.get("cookie")),query.get("state",[""])[0],query.get("code",[""])[0])
        if success:
            return 302,{"Location":"/"},b""
        if "text/html" in headers.get("accept",""):
            return 401,{"Content-Type":"text/html; charset=utf-8"},Path(__file__).parent.parent.joinpath("web/auth-error.html").read_bytes()
        return 401,extra,{"code":"login_state_missing_or_invalid"}
    try:
        data = json.loads(body or b"{}") if method in {"POST","PATCH"} else {}
    except (ValueError,UnicodeError):
        return 400,extra,{"code":"invalid_json"}
    if not isinstance(data,dict):
        return 400,extra,{"code":"invalid_request"}
    if path == "/auth/login" and method == "POST":
        identities = {"ada@example.test":1,"ben@example.test":2}
        if data.get("email") not in identities or data.get("password") != "practice-only":
            return 401,extra,{"code":"invalid_credentials"}
        sid = auth.create_session(identities[data["email"]])
        return 200,{"Set-Cookie":auth.cookie(sid)},{"user_id":identities[data["email"]]}
    if path == "/webhooks/payments" and method == "POST":
        if headers.get("x-lab-webhook-secret") != "synthetic-webhook-secret":
            return 401,extra,{"code":"invalid_webhook_secret"}
        required = {"id","order_id","amount_minor","currency","type"}
        if not isinstance(data,dict) or not required.issubset(data) or data["type"] != "payment.succeeded":
            return 400,extra,{"code":"invalid_event"}
        with db.connect() as conn:
            order = conn.execute("SELECT * FROM orders WHERE id=?",(data["order_id"],)).fetchone()
        if not order or data["amount_minor"] != order["amount_minor"] or data["currency"] != order["currency"]:
            return 422,extra,{"code":"event_order_mismatch"}
        return 200,extra,payments.handle_webhook(data)
    user_id = auth.current_user(headers.get("cookie"))
    if not user_id:
        return 401,extra,{"code":"authentication_required"}
    if path == "/auth/logout" and method == "POST":
        with db.connect() as conn:
            conn.execute("DELETE FROM sessions WHERE id=?",(auth.session_id(headers.get("cookie")),))
        return 200,{"Set-Cookie":"hd_session=; Path=/; HttpOnly; SameSite=Strict; Max-Age=0"},{"signed_out":True}
    try:
        if path == "/api/me" and method == "GET":
            with db.connect() as conn:
                profile=conn.execute("SELECT name,email FROM users WHERE id=?",(user_id,)).fetchone()
            return 200,extra,{"user_id":user_id,"name":profile["name"],"email":profile["email"],"server_now":clock.now().isoformat()}
        if path == "/api/wallet" and method == "GET":
            with db.connect() as conn:
                account=conn.execute("SELECT balance_minor FROM wallet_accounts WHERE user_id=?",(user_id,)).fetchone()
                entries=[dict(row) for row in conn.execute("SELECT * FROM wallet_entries WHERE user_id=? ORDER BY created_at DESC,id DESC",(user_id,))]
            return 200,extra,{"balance_minor":account["balance_minor"],"currency":"NGN","entries":entries}
        if path == "/api/orders" and method == "GET":
            result = orders.list_orders(user_id)
            if "page" in query:
                result = orders.page_orders(user_id,int(query["page"][0]),int(query.get("page_size",["2"])[0]))
            return 200,extra,{"orders":result,"server_now":clock.now().isoformat()}
        if path == "/api/search" and method == "GET":
            return 200,extra,{"orders":search.search_orders(user_id,query.get("q",[""])[0])}
        if path == "/api/charge" and method == "POST":
            stub = ScriptedProvider([data.get("provider_response",{"status":200,"payment_id":"pay_demo"})])
            code,result = payments.charge(data.get("amount_minor"),stub)
            return code,extra,result
        if path.startswith("/api/orders/"):
            segments = path.strip("/").split("/")
            order_id = segments[2]
            if len(segments)==3 and method=="GET":
                return 200,extra,orders.get_order(order_id,user_id)
            if len(segments)==4 and method=="POST" and segments[3]=="pay":
                return 200,extra,orders.pay(order_id,user_id)
            if len(segments)==4 and method=="POST" and segments[3]=="transition":
                return 200,extra,orders.transition(order_id,user_id,data.get("target"))
    except orders.DomainError as exc:
        return exc.status,extra,{"code":exc.code}
    except (ValueError,TypeError):
        return 400,extra,{"code":"invalid_request"}
    return 404,extra,{"code":"route_not_found"}

def serve(port=8010, provider_port=8011):
    if not db.database_path().exists():
        db.initialize()
    class Handler(BaseHTTPRequestHandler):
        def respond(self):
            try:
                length = int(self.headers.get("Content-Length","0"))
                if length > 65536:
                    self.send_error(413)
                    return
                status,headers,payload = application(self.command,self.path,dict(self.headers),self.rfile.read(length),provider_port)
                if isinstance(payload,(dict,list)):
                    payload = json.dumps(payload).encode()
                    headers["Content-Type"] = "application/json"
                self.send_response(status)
                for name,value in headers.items():
                    self.send_header(name,value)
                self.send_header("Content-Length",str(len(payload)))
                self.end_headers()
                self.wfile.write(payload)
            except Exception:
                self.send_error(500,"Lab handler failure; inspect terminal traceback")
                import traceback
                traceback.print_exc()
        do_GET = respond
        do_POST = respond
        do_PATCH = respond
    class IdentityProvider(BaseHTTPRequestHandler):
        def do_GET(self):
            query = parse_qs(urlparse(self.path).query)
            state = query.get("state",[""])[0]
            callback = f"http://localhost:{port}/auth/callback?"+urlencode({"state":state,"code":"synthetic-ada"})
            template=Path(__file__).parent.parent.joinpath("web/identity.html").read_text()
            page=template.replace("{{CALLBACK}}",html.escape(callback)).encode()
            self.send_response(200)
            self.send_header("Content-Type","text/html; charset=utf-8")
            self.send_header("Content-Length",str(len(page)))
            self.end_headers()
            self.wfile.write(page)
    provider = ThreadingHTTPServer(("127.0.0.1",provider_port),IdentityProvider)
    server = ThreadingHTTPServer(("127.0.0.1",port),Handler)
    threading.Thread(target=provider.serve_forever,daemon=True).start()
    print(f"App: http://localhost:{port} | Identity: http://127.0.0.1:{provider_port}",flush=True)
    print(f"Clock frozen at {clock.now().isoformat()}; Ctrl-C stops both servers.",flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
        provider.shutdown()
        provider.server_close()
