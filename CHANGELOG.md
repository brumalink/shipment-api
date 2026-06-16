# Changelog

All notable changes to this project are documented in this file.

## [v2.2.0] - 2026-06-16

- ADR 0004: retention of readings, custody events and source history
- Filter shipments by status, origin and destination

## [v2.1.0] - 2026-04-21

- Run container as non-root user (SR-2026-03)
- Bump dependencies
- Retry customer webhooks with exponential backoff

## [v2.0.0] - 2026-02-10

- Add Tenant model with slug validation
- Add tenant admin endpoints
- Add tenant slug validation tests
- Release 2.0 - multi-tenant platform for 3PL partners

## [v1.2.0] - 2025-10-21

- Document GDP audit trail in architecture overview
- Bump dependencies
- Tolerate short door-open spikes in excursion detection (SOP-TR-07)

## [v1.1.0] - 2025-08-19

- Fix duplicate readings stored after tracker reconnect
- CI: test on Python 3.12 and 3.13
- Add pagination to shipment listing

## [v1.0.0] - 2025-07-01

- Port route planning from legacy-route-planner
- Add route planner tests
- Update README for production go-live

## [v0.2.0] - 2025-06-10

- Bump FastAPI, uvicorn and SQLAlchemy
- Add custody event model
- Hash-chain custody events for tamper evidence
- Expose custody chain endpoint
- Add tests for custody hash chain
- Excursion rules per product profile (2-8C, 15-25C, frozen)
- Add excursion listing endpoint and wire custody router
- Add excursion alerts via e-mail and customer webhook
- Add security policy

## [v0.1.0] - 2025-04-15

- Initial project skeleton
- Add settings management via pydantic-settings
- Add SQLAlchemy engine, session and declarative base
- Add Shipment model with temperature limits
- Add shipment request/response schemas
- Add CRUD endpoints for shipments
- Add Dockerfile and docker-compose for local development
- Add CI workflow running pytest
- Move health check to its own router and report version
- Add pull request template and CODEOWNERS
- Add SensorReading model
- Add batch ingestion endpoint for tracker readings
- Add temperature excursion detector (fixed 2-8C limits)
- Add Dependabot configuration
- Write architecture overview
