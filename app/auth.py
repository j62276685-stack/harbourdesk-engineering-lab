import secrets
from http.cookies import SimpleCookie
from . import db

COOKIE_POLICY = "Path=/; HttpOnly; SameSite=Strict"

def session_id(cookie_header):
    cookies = SimpleCookie()
    try:
        cookies.load(cookie_header or "")
    except Exception:
        return None
    return cookies["hd_session"].value if "hd_session" in cookies else None

def create_session(user_id=None):
    sid = secrets.token_urlsafe(24)
    with db.connect() as conn:
        conn.execute("INSERT INTO sessions(id,user_id) VALUES(?,?)", (sid,user_id))
    return sid

def cookie(sid):
    return f"hd_session={sid}; {COOKIE_POLICY}"

def start_provider():
    sid, state = create_session(), secrets.token_urlsafe(24)
    with db.connect() as conn:
        conn.execute("UPDATE sessions SET state=? WHERE id=?",(state,sid))
    return sid, state

def finish_provider(sid, state, code):
    with db.connect() as conn:
        row = conn.execute("SELECT * FROM sessions WHERE id=?",(sid,)).fetchone()
        if not row or not state or row["state"] != state or row["state_used"] or code != "synthetic-ada":
            return False
        conn.execute("UPDATE sessions SET user_id=1,state_used=1 WHERE id=?",(sid,))
    return True

def current_user(cookie_header):
    with db.connect() as conn:
        row = conn.execute("SELECT user_id FROM sessions WHERE id=?",(session_id(cookie_header),)).fetchone()
    return row["user_id"] if row else None
