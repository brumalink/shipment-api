# Architecture overview

```
BL-T3 tracker --MQTT/LTE-M--> MQTT broker --> ingestion bridge --HTTPS--> shipment-api --> PostgreSQL
                                                                              |
                                                          ops-dashboard <-----+-----> driver-app
```

## Components

| Component | Responsibility |
|---|---|
| `app/api` | HTTP endpoints (FastAPI routers) |
| `app/models` | SQLAlchemy models |
| `app/schemas` | Request/response models (pydantic) |
| `app/services` | Business logic: excursion detection, alerts |

## Data

- **shipments** – one row per consignment, with the temperature limits copied from the product profile at creation time
  (so a later profile change never alters historical evaluation).
- **sensor_readings** – raw tracker readings, unique on `(tracker_id, sequence)`.

## Deployment

Container image built by CI, deployed to the `prod` environment by `infra-terraform`.
