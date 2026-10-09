# API and fixture contracts

All POST bodies are JSON. Successful customer requests require an `hd_session` cookie obtained by a synthetic login. Content types and status codes can be observed in browser developer tools or tested through `app.http.application`.

| Method | Endpoint | Input/response |
|---|---|---|
| GET | `/health` | `status`, `service`, `clock` |
| POST | `/auth/login` | `{email,password}` → `user_id` and Set-Cookie |
| GET | `/auth/start` | Redirect to the synthetic identity provider |
| GET | `/auth/callback?state=...&code=...` | Validate one-use state and return to the app |
| GET | `/api/me` | `user_id`, `name`, `email`, `server_now` |
| POST | `/auth/logout` | Revokes the current session and expires its cookie; other sessions remain |
| GET | `/api/wallet` | `balance_minor`, `currency`, `entries` for the current account; read-only cached balance and posted ledger |
| GET | `/api/orders` | `{orders,server_now}` |
| GET | `/api/orders?page=1&page_size=2` | First page, default size two |
| GET | `/api/orders/{id}` | One owned order |
| GET | `/api/search?q=active` | `{orders}` for the authenticated customer |
| POST | `/api/orders/{id}/pay` | Empty body; paid result or domain error |
| POST | `/api/orders/{id}/transition` | `{target}`; transition result |
| POST | `/api/charge` | `{amount_minor,provider_response?}`; local stub only |
| POST | `/webhooks/payments` | Event plus `X-Lab-Webhook-Secret: synthetic-webhook-secret` |

An order has `id`, `user_id`, `status`, `amount_minor`, `currency`, `expires_at`, `created_at`, `provider_status`, `version`. Times may arrive in equivalent timezone offsets. `version` increments on a real accepted state change, not on rejected or duplicate requests.

Webhook fixture: `{"id":"evt_001","type":"payment.succeeded","order_id":"ord_active","amount_minor":12500,"currency":"NGN"}`. This is a shared-secret simulation, not a real signature standard. Validation at the HTTP edge is working baseline behavior; task 7 concerns business effects and transaction boundaries.

Provider scripts are JSON with `responses`, consumed in order. Success: `{status:200,payment_id:"pay_demo"}`. Failure: `{status:503,code:"unavailable",retry_after:2,elapsed_seconds:0.2}`. Status `0` means a simulated transport timeout. The stub logs each call's amount and idempotency key. Its optional `on_call(seconds)` callback lets your fake clock account for simulated request duration. Never wait on a real remote provider to test these cases.

Error classification required in task 6:

| Cause | HTTP | Code | Customer message |
|---|---:|---|---|
| Bad local amount (non-integer, boolean, zero or negative) | 400 | `invalid_amount` | Enter a valid amount. |
| Provider says card declined (402) | 402 | `payment_declined` | Payment was declined. Use another payment method. |
| Provider outage (500/502/503/504) | 503 | `provider_unavailable` | Payment service is temporarily unavailable. Try again later. |
| Provider transport timeout (0) | 504 | `provider_timeout` | Payment service timed out. Check payment status before trying again. |
| Successful response | 200 | Provider success body | Preserve success data. |

Unexpected provider errors must remain a dependency classification, such as 502 `provider_error`; do not describe them as bad customer input or leak raw upstream messages. Do not retry or create payment rows in the classification task.

## Product presentation routes

GET / serves the branded customer portal. The local identity service renders its own Harbour Identity page, retaining the cross-site callback flow. A failed callback still returns HTTP 401: HTML clients receive a branded retry page; JSON/API clients retain login_state_missing_or_invalid. This presentation change does not fix the sign-in cookie/state exercise.

Wallet reads do not calculate a replacement cache value, create audit rows or mutate the ledger. CSV exports are client-side representations of actual selected results. Numeric minor-unit fields, including negative ledger entries, remain numeric. Potential spreadsheet-formula text is escaped. No export implies a live financial statement or settlement proof.
