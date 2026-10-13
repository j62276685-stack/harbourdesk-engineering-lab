# Delivery assumptions
Events may arrive more than once or in parallel on independent database connections. The provider repeats the same event ID for the same operation and retries after a timeout. A process may exit after a committed business write but before a success response. Distinct order payments have distinct event IDs. Acknowledgement should be a successful result once the effect is known to have committed.

In this task only successful matching events are business inputs; HTTP validation rejects incorrect amount/currency/type. Investigate both a delivery race and interruption between durable steps. No particular SQL pattern or locking mechanism is prescribed. The probe's after_lookup hook is an optional scheduling aid, not part of the public provider protocol.
