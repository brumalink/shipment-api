# ADR 0004: Retention of readings, custody events and repository history

- Status: accepted
- Date: 2026-05-26
- Deciders: Piotr Kaczmarek (QA), Aleksandra Nowak, Marta Zielińska

## Context

EU GDP guidelines and our customer quality agreements require distribution records to be kept for at least 5 years.
Our 2026 NIS2 readiness review also flagged that the repositories documenting GDP-relevant systems had no
independent backup – the hosting platform itself was a single point of failure.

## Decision

| Data | Retention | Where |
|---|---|---|
| Sensor readings | 5 years | PostgreSQL, monthly partitions archived to object storage after 13 months |
| Custody events | 5 years after delivery | PostgreSQL |
| Repositories (history, pull requests, reviews, issues, releases, wiki) | 5 years minimum | Hosting platform + independent daily backup (immutable, EU region) |

## Consequences

- Repository backups must include metadata (pull requests with reviews, issues, releases, wiki), not just git
  history – review evidence is part of the validated-system documentation.
- A restore test is performed quarterly and recorded in `gdp-compliance-docs/validation/restore-tests/`.
