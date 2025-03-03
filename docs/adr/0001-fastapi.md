# ADR 0001: FastAPI + PostgreSQL for the shipment service

- Status: accepted
- Date: 2025-03-03
- Deciders: Marta Zielińska, Jakub Lewandowski, Aleksandra Nowak

## Context

The legacy route planner (Java, 2019) cannot be extended to handle tracker data. We need a new service that ingests
readings from ~2,000 trackers every 5 minutes and exposes an API for the dashboard and driver app.

## Decision

Python 3.12 with FastAPI, SQLAlchemy 2.0 and PostgreSQL 16.

## Consequences

- The team already knows Python (the data team uses it too, so detector logic can be shared).
- Automatic OpenAPI docs for the frontend and mobile teams.
- We need to be careful with CPU-heavy work in request handlers – excursion evaluation stays cheap by design.
