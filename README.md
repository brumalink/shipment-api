# Brumalink Shipment API

Source of truth for every temperature-controlled consignment handled by Brumalink:
shipments, tracker readings, temperature excursions and the chain of custody.

In production since **July 2025**.

## What it does

- **Shipments** – create and track consignments with a product temperature profile (`2-8C`, `15-25C`, `frozen`).
- **Readings ingestion** – BL-T3 trackers report temperature/humidity every 5 minutes over MQTT → ingestion bridge → `POST /readings`.
- **Excursion detection** – readings outside the product profile raise an excursion and put the shipment in `quarantined` until QA releases it.
- **Chain of custody** – every handover is recorded as a hash-chained event (tamper evident, required for GDP audits).
- **Route planning** – multi-leg routes through Brumalink cold-storage hubs.

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

## Documentation

- [Architecture overview](docs/architecture.md)
- [Architecture decision records](docs/adr/)

## Ownership

Backend team (`@brumalink/backend`). Changes to custody-chain code also require review by QA & Compliance.
