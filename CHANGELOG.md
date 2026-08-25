# Changelog

All notable changes to this project are documented in this file.

## [v2.3.1] - 2026-08-25

- Ingestion: require HMAC signature on tracker batches

## [v2.3.0] - 2026-08-11

- Docs checks: pin actions by SHA, read-only token, timeouts
- Notifications: one alert per excursion (INC-2026-031)

## [v2.2.0] - 2026-06-16

- ADR 0004: retention of readings, custody events and repository history
- Specify shipment filters by status, origin and destination

## [v2.1.0] - 2026-04-21

- Deployment: unprivileged containers (SR-2026-03)
- Add tenants to data model diagram
- Notifications: retry webhooks with exponential backoff

## [v2.0.0] - 2026-02-10

- Describe multi-tenant model
- Specify tenant endpoints
- Add tenant data isolation requirements
- Release 2.0 - multi-tenant platform for 3PL partners

## [v1.2.0] - 2025-10-21

- Document GDP audit trail in architecture overview
- Excursion rules v3: tolerate short door-open spikes (SOP-TR-07)

## [v1.1.0] - 2025-08-19

- Ingestion: document duplicate handling after reconnect
- Docs checks: fail on committed secrets and large files
- Specify pagination for shipment listing

## [v1.0.0] - 2025-07-01

- Document route planning rules
- Add cold-storage hub list
- Update README for production go-live

## [v0.2.0] - 2025-06-10

- Add quarantine and rejection to shipment lifecycle
- Describe chain of custody requirements
- ADR 0003: hash-chained custody events
- Add custody chain example response
- Add custody verification procedure for auditors
- Excursion rules per product profile (2-8C, 15-25C, frozen)
- Specify excursion and custody chain endpoints
- Document excursion alert notifications
- Add security policy

## [v0.1.0] - 2025-04-15

- Initial documentation structure
- Add system context diagram
- Draft data model
- Specify shipment resource in OpenAPI
- Add example shipment payload
- Document shipment lifecycle
- Document deployment environments
- Add documentation checks workflow
- Add architecture overview
- Add pull request template and CODEOWNERS
- Describe tracker reading ingestion
- Specify readings batch endpoint
- Define temperature excursion rules (fixed 2-8C)
- Add Dependabot configuration for workflow actions
- Add excursion alert sequence diagram
