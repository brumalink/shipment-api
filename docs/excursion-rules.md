# Temperature excursion rules

Version 2 – valid from 2025-05-20. See [ADR 0002](adr/0002-excursion-rules.md).

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

## Consequence

Any excursion puts the shipment in `quarantined` status and alerts the QA duty officer.

## Example (`2-8C`)

| Time | °C | |
|---|---|---|
| 08:00 | 5.0 | |
| 08:05 | 8.4 | excursion starts |
| 08:10 | 9.6 | peak |
| 08:15 | 8.9 | excursion ends |
| 08:20 | 6.0 | |
