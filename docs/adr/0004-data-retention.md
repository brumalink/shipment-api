# ADR 0004: Retention of readings, custody events and source history

- Status: accepted
- Date: 2026-05-26
- Deciders: Piotr Kaczmarek (QA), Aleksandra Nowak, Marta Zielińska

## Context

EU GDP guidelines and our customer quality agreements require distribution records to be kept for at least 5 years.
Our 2026 NIS2 readiness review also flagged that source code and CI configuration of GDP-relevant systems had no
independent backup – GitHub itself was a single point of failure.

## Decision

| Data | Retention | Where |
|---|---|---|
| Sensor readings | 5 years | PostgreSQL, monthly partitions archived to object storage after 13 months |
| Custody events | 5 years after delivery | PostgreSQL |
| Source code, PRs, issues, releases of this repo | 5 years minimum | GitHub + independent daily backup (immutable, EU region) |

## Consequences

- Partitioning migration required (done in v2.2).
- Repository backups must include metadata (pull requests with reviews, issues, releases), not just git data – review
  evidence is part of the validated-system documentation.
- Restore test performed quarterly and recorded in `gdp-compliance-docs`.
