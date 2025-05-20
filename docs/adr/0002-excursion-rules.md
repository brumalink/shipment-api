# ADR 0002: Temperature excursion rules per product profile

- Status: accepted
- Date: 2025-05-20
- Deciders: Marta Zielińska, Piotr Kaczmarek (QA)

## Context

Initially every shipment was evaluated against 2–8 °C. Customers now ship controlled-room-temperature and frozen products.

## Decision

Each shipment carries a product profile: `2-8C`, `15-25C` or `frozen` (-25 to -15 °C). The limits are copied onto the
shipment at creation time. An excursion is any continuous run of readings outside the limits.

## Consequences

- Changing a profile's limits does not change the evaluation of existing shipments (required for audit reproducibility).
- New profiles require a change request approved by QA and an update of the validation record in `gdp-compliance-docs`.
