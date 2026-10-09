PRAGMA foreign_keys = ON;
CREATE TABLE users(id INTEGER PRIMARY KEY, email TEXT NOT NULL UNIQUE, name TEXT NOT NULL);
CREATE TABLE sessions(id TEXT PRIMARY KEY, user_id INTEGER, state TEXT, state_used INTEGER NOT NULL DEFAULT 0);
CREATE TABLE orders(id TEXT PRIMARY KEY, user_id INTEGER NOT NULL REFERENCES users(id), status TEXT NOT NULL,
 amount_minor INTEGER NOT NULL, currency TEXT NOT NULL, expires_at TEXT NOT NULL, created_at TEXT NOT NULL,
 provider_status TEXT, version INTEGER NOT NULL DEFAULT 0);
CREATE TABLE payments(id INTEGER PRIMARY KEY, event_id TEXT NOT NULL, order_id TEXT NOT NULL REFERENCES orders(id),
 amount_minor INTEGER NOT NULL, currency TEXT NOT NULL, created_at TEXT NOT NULL);
CREATE TABLE webhook_receipts(event_id TEXT PRIMARY KEY, received_at TEXT NOT NULL);
CREATE TABLE wallet_accounts(user_id INTEGER PRIMARY KEY REFERENCES users(id), balance_minor INTEGER NOT NULL);
CREATE TABLE wallet_entries(id TEXT PRIMARY KEY, user_id INTEGER NOT NULL REFERENCES users(id),
 delta_minor INTEGER NOT NULL, source_ref TEXT NOT NULL, created_at TEXT NOT NULL, note TEXT NOT NULL);
CREATE TABLE wallet_audit(id INTEGER PRIMARY KEY, user_id INTEGER NOT NULL, old_balance INTEGER,
 new_balance INTEGER, reason TEXT NOT NULL, created_at TEXT NOT NULL);
CREATE TABLE customers(id TEXT PRIMARY KEY, email TEXT, phone TEXT, external_ref TEXT, imported_at TEXT NOT NULL);
CREATE TABLE notification_outbox(id INTEGER PRIMARY KEY, event_id TEXT NOT NULL, user_id INTEGER NOT NULL,
 channel TEXT NOT NULL, payload TEXT NOT NULL, status TEXT NOT NULL DEFAULT 'pending', attempts INTEGER NOT NULL DEFAULT 0,
 available_at TEXT NOT NULL, last_error TEXT);
CREATE TABLE worker_state(id INTEGER PRIMARY KEY CHECK(id=1), mode TEXT NOT NULL, failure_remaining INTEGER NOT NULL);
