# Shipment lifecycle

```mermaid
stateDiagram-v2
    [*] --> created
    created --> in_transit : first pickup scan
    in_transit --> quarantined : excursion detected
    quarantined --> in_transit : QA release
    quarantined --> rejected : QA reject
    in_transit --> delivered : delivery scan
    delivered --> [*]
    rejected --> [*]
```

| Status | Meaning |
|---|---|
| `created` | Booked, tracker assigned, not yet picked up |
| `in_transit` | Picked up; readings are evaluated continuously |
| `quarantined` | Excursion detected. The product must not be used until QA assesses it (SOP-TR-07) |
| `rejected` | QA rejected the product – return or destruction, deviation record required |
| `delivered` | Signed for by the consignee |

A shipment can be quarantined more than once. Every QA decision is recorded as a custody event.
