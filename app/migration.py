from . import db

def migrate():
    with db.connect() as conn:
        conn.execute("CREATE UNIQUE INDEX customers_email_unique ON customers(email)")
