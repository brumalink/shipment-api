# Temperature excursion rules

Version 3 – valid from 2025-10-21. See [ADR 0002](adr/0002-excursion-rules.md) and SOP-TR-07 in `gdp-compliance-docs`.

## Product profiles

| Profile | Range | Typical products |
|---|---|---|
| `2-8C` | 2 to 8 °C | vaccines, insulin, biologics |
| `15-25C` | 15 to 25 °C | controlled room temperature medicines |
| `frozen` | -25 to -15 °C | frozen plasma, some diagnostics |

The limits are copied onto the shipment when it is created.

## Rule

An **excursion** is a continuous run of readings outside the shipment's range. It starts at the first reading
outside the range and ends at the last reading outside the range. The **peak** is the reading with the largest
deviation from the range.

### Short spikes (new in version 3)

Opening the container door during loading causes short temperature spikes that do not affect product quality.
Per SOP-TR-07 a run is **ignored** when both are true:

- it lasts **less than 10 minutes**, and
- its peak deviates from the range by **less than 5 °C**.

A short but severe spike (deviation of 5 °C or more) is always an excursion.

## Consequence

Any excursion puts the shipment in `quarantined` status and alerts the QA duty officer.

## Examples (`2-8C`, one reading every 5 minutes)

| Readings (°C) | Result |
|---|---|
| 5.0, 8.4, 9.6, 8.9, 8.5, 6.0 | excursion – 15 minutes above 8 °C, peak 9.6 |
| 5.0, 9.0, 8.7, 6.0 | ignored – 5 minutes, +1 °C (door opened) |
| 5.0, 14.0, 13.5, 6.0 | excursion – only 5 minutes, but +6 °C |

## Why the history of this document matters

Shipments are evaluated with the rule version valid on the shipment date. During audits we must show which
version applied – the git history and tags of this repository are the evidence.
