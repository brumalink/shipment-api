# ADR 0001: Platform stack

- Status: accepted
- Date: 2025-03-03
- Deciders: Marta Zielińska, Jakub Lewandowski, Aleksandra Nowak

## Context

The legacy route planner (2019) cannot be extended to handle tracker data. We need a new platform that ingests
readings from ~2,000 trackers every 5 minutes and exposes an API for the dashboard and driver app.

## Decision

A single API service backed by PostgreSQL, deployed as a container. The API is designed contract-first:
[`api/openapi.yaml`](../../api/openapi.yaml) is the source of truth for all clients.

## Consequences

- Frontend and mobile teams can work in parallel against the specification.
- One database simplifies GDP evidence (single system of record).
- Heavy analytics stay out of the platform (see `cold-chain-reports`).
