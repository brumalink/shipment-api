# System context

```mermaid
flowchart LR
    tracker["BL-T3 tracker<br/>(in container)"] -- "MQTT over LTE-M" --> broker["MQTT broker"]
    broker --> bridge["Ingestion bridge"]
    bridge -- "HTTPS, signed batches" --> platform["Shipment Platform"]
    platform --> db[("PostgreSQL")]
    platform --> dash["Ops dashboard<br/>(dispatchers)"]
    platform --> app["Driver app"]
    platform -- "e-mail" --> qa["QA duty officer"]
    platform -- "webhook" --> customer["Customer systems<br/>(pharmacies, wholesalers)"]
```

## Actors

- **Dispatchers** plan and monitor shipments in the ops dashboard.
- **Drivers** scan pickups and deliveries in the driver app; each scan becomes a custody event.
- **QA duty officer** is alerted on every excursion and releases or rejects quarantined shipments.
- **Customers** receive excursion webhooks and delivery confirmations.
