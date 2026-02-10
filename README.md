# Brumalink Shipment API

Source of truth for every temperature-controlled consignment handled by Brumalink:
shipments, tracker readings, temperature excursions and the chain of custody.

In production since **July 2025**. Multi-tenant since **v2.0** (February 2026) – 3PL partners
run their own consignments on the platform, with data isolated per tenant.

## What it does

- **Shipments** – create and track consignments with a product temperature profile (`2-8C`, `15-25C`, `frozen`).
- **Readings ingestion** – BL-T3 trackers report temperature/humidity every 5 minutes over MQTT → ingestion bridge → `POST /readings`. Payloads are HMAC-signed by the tracker.
- **Excursion detection** – readings outside the product profile raise an excursion and put the shipment in `quarantined` until QA releases it. Short door-open spikes are tolerated per SOP-TR-07.
- **Chain of custody** – every handover is recorded as a hash-chained event (tamper evident, required for GDP audits).
- **Route planning** – multi-leg routes through Brumalink cold-storage hubs.
- **Tenants** – 3PL partners with their own data region.

## Local development

```bash
docker compose up -d db
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API docs: http://localhost:8000/docs

## Tests

```bash
pytest
```

## Configuration

All settings use the `BRUMALINK_` prefix, e.g. `BRUMALINK_DATABASE_URL`, `BRUMALINK_TRACKER_SHARED_SECRET`.
See [`app/config.py`](app/config.py).

## Documentation

- [Architecture overview](docs/architecture.md)
- [Architecture decision records](docs/adr/)
- [Security policy](SECURITY.md)

## Ownership

Backend team (`@brumalink/backend`). Changes to custody-chain code also require review by QA & Compliance
(`@brumalink/qa-compliance`), see [CODEOWNERS](.github/CODEOWNERS).
