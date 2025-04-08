# Temperature excursion rules

Version 1 – valid from 2025-04-08.

## Rule

All shipments are evaluated against **2–8 °C**.

An **excursion** is a continuous run of readings outside 2–8 °C. It starts at the first reading outside
the range and ends at the last reading outside the range. The **peak** is the reading furthest from the range.

## Consequence

Any excursion puts the shipment in `quarantined` status and alerts the QA duty officer.

## Example

| Time | °C | |
|---|---|---|
| 08:00 | 5.0 | |
| 08:05 | 8.4 | excursion starts |
| 08:10 | 9.6 | peak |
| 08:15 | 8.9 | excursion ends |
| 08:20 | 6.0 | |
