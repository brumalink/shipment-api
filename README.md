# Brumalink Shipment Platform

> **Fictional company.** Brumalink is a fictional company used for demonstration purposes. All company names, people, customers and data in this repository are invented. Any resemblance to real entities is coincidental.
>
> **AI-generated content.** This repository was created with the help of AI and contains documentation only.

Design documentation for the platform that tracks every temperature-controlled consignment
handled by Brumalink: shipments, tracker readings, temperature excursions and the chain of custody.

Status: **in production since July 2025** (v1.0).

## What the platform does

| Capability | Documentation |
|---|---|
| Shipments with a product temperature profile (`2-8C`, `15-25C`, `frozen`) | [API spec](api/openapi.yaml), [lifecycle](docs/shipment-lifecycle.md) |
| Ingestion of tracker readings (every 5 minutes, MQTT → HTTPS) | [ingestion](docs/ingestion.md) |
| Temperature excursion detection and quarantine | [excursion rules](docs/excursion-rules.md) |
| Excursion alerts to QA and customers | [notifications](docs/notifications.md) |
| Tamper-evident chain of custody | [custody chain](docs/custody-chain.md) |
| Multi-leg routes through cold-storage hubs | [route planning](docs/routing/route-planning.md) |

Start with the [architecture overview](docs/architecture.md).

## Contents

- [`docs/`](docs/) – architecture, diagrams, decision records (ADR), glossary
- [`api/`](api/) – API specification (OpenAPI) and example payloads

## Ownership

Backend team. Changes to excursion rules and custody-chain documents also require QA & Compliance review.
