# Excursion notifications

When a shipment is quarantined:

1. **E-mail** to the QA duty officer: subject `[EXCURSION] <reference> peaked at <peak> C`.
2. **Webhook** to the customer, if configured:

```json
{ "event": "excursion", "shipment": "BL-2025-000123", "peak_c": 9.6 }
```

Webhook endpoints are configured per customer by the account manager.

## Retries

Customer endpoints are often unreliable. A failed webhook is retried **3 times with exponential backoff**
(after 1 s, 2 s and 4 s). After the last failure the account manager is notified.
