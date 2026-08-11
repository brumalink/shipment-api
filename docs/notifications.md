# Excursion notifications

When a shipment is quarantined:

1. **E-mail** to the QA duty officer: subject `[EXCURSION] <reference> peaked at <peak> C`.
2. **Webhook** to the customer, if configured:

```json
{ "event": "excursion", "shipment": "BL-2025-000123", "started_at": "2026-08-03T10:15:00+02:00", "peak_c": 9.6 }
```

Webhook endpoints are configured per customer by the account manager.

## One alert per excursion

Trackers re-send buffered readings after reconnecting, which used to re-trigger the same excursion and page
the QA officer twice (incident INC-2026-031). Since v2.3.0 alerts are sent **once per excursion**, identified
by shipment reference and excursion start time.

## Retries

Customer endpoints are often unreliable. A failed webhook is retried **3 times with exponential backoff**
(after 1 s, 2 s and 4 s). After the last failure the account manager is notified.
