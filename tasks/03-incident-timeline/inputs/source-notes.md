# Source reliability
- Proxy clock is one second ahead of service UTC according to the 07:55 health check. Its timestamps include the Lagos offset; service/provider times are UTC.
- Proxy lines are response completion times. Provider starts and service processing logs describe different phases, so do not force them to be equal.
- [service.jsonl](service.jsonl) is a selected fragment, not all instance logs. Missing 08:03:20–08:04:30 UTC.
- Provider CSV describes delivery attempts, not distinct charges or financial settlements.
- Metrics are per-minute aggregates. Counts do not identify individual customers.
- Incident order/payment IDs are historical synthetic IDs and are not in the interactive starter database.
