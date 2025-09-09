# Architecture overview

```
BL-T3 tracker --MQTT/LTE-M--> MQTT broker --> ingestion bridge --HTTPS (HMAC)--> shipment-api --> PostgreSQL
                                                                                    |
                                                                ops-dashboard <-----+-----> driver-app
```

## Components

| Component | Responsibility |
|---|---|
| `app/api` | HTTP endpoints (FastAPI routers) |
| `app/models` | SQLAlchemy models |
| `app/schemas` | Request/response models (pydantic) |
| `app/services` | Business logic: excursion detection, alerts, custody hash chain |
| `app/routing` | Multi-leg route planning through cold-storage hubs |

## Data

- **shipments** – one row per consignment, with the temperature limits copied from the product profile at creation time
  (so a later profile change never alters historical evaluation).
- **sensor_readings** – raw tracker readings, unique on `(tracker_id, sequence)`. Retained for 5 years (ADR 0004).
- **custody_events** – append-only, hash-chained handovers (ADR 0003).
- **tenants** – 3PL partners using the platform (since v2.0).

## GDP audit trail

Good Distribution Practice requires that we can demonstrate, for every consignment, that the product stayed within
its labelled storage conditions and who had custody at any point. The evidence consists of:

1. Raw readings – never updated, only inserted.
2. Excursion evaluations – reproducible from raw readings with the detector version recorded in the release notes.
3. Custody chain – tamper evident via hash chaining; `GET /shipments/{ref}/custody` reports `intact: false` if any event was altered.
4. **Source code history** – the exact detector logic in force on any date must be retrievable. This repository, its tags
   and its pull request history are part of the validated-system documentation and are backed up daily.

## Deployment

Container image built by CI, deployed to `staging` and then `prod` by `infra-terraform`.
