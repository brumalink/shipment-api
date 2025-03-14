# Shipment lifecycle

```mermaid
stateDiagram-v2
    [*] --> created
    created --> in_transit : first pickup scan
    in_transit --> delivered : delivery scan
    delivered --> [*]
```

| Status | Meaning |
|---|---|
| `created` | Booked, tracker assigned, not yet picked up |
| `in_transit` | Picked up; readings are evaluated continuously |
| `delivered` | Signed for by the consignee |
