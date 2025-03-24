# Architecture overview

See the [system context diagram](diagrams/system-context.md) for the big picture.

## Building blocks

| Block | Responsibility |
|---|---|
| Ingestion bridge | Receives tracker messages from the MQTT broker, batches them and forwards to the platform |
| Shipment Platform API | Shipments, readings, excursions, custody chain |
| PostgreSQL | System of record |
| Ops dashboard / driver app | Clients of the API |

## Key decisions

- Platform stack – [ADR 0001](adr/0001-platform-stack.md)

## Environments

`dev` → `staging` → `prod`, see [deployment](deployment.md).
