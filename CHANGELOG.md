# Changelog

All notable changes to this project are documented in this file.

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
