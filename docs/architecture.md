# Architecture overview

See the [system context diagram](diagrams/system-context.md) for the big picture and the
[data model](diagrams/data-model.md) for entities.

## Building blocks

| Block | Responsibility |
|---|---|
| Ingestion bridge | Receives tracker messages from the MQTT broker, batches and signs them, forwards to the platform |
| Shipment Platform API | Shipments, readings, excursions, custody chain, tenants |
| PostgreSQL | System of record |
| Ops dashboard / driver app | Clients of the API |

## Key decisions

| ADR | Decision |
|---|---|
| [0001](adr/0001-platform-stack.md) | Platform stack |
| [0002](adr/0002-excursion-rules.md) | Excursion rules per product profile |
| [0003](adr/0003-custody-chain-hashing.md) | Hash-chained custody events |
| [0004](adr/0004-data-retention.md) | Retention of readings, custody events and repository history |

## GDP audit trail

Good Distribution Practice requires that we can demonstrate, for every consignment, that the product stayed
within its labelled storage conditions and who had custody at any point. The evidence consists of:

1. **Raw readings** – never updated, only inserted.
2. **Excursion evaluations** – reproducible from raw readings with the rules valid on the shipment date
   ([excursion rules](excursion-rules.md) and their history in this repository).
3. **Custody chain** – tamper evident via hash chaining ([custody chain](custody-chain.md)).
4. **Design history** – this repository, its tags and its pull request reviews are part of the
   validated-system documentation. The version of any rule in force on a given date must be retrievable,
   which is why the repository is backed up daily to independent storage.

## Environments

`dev` → `staging` → `prod`, see [deployment](deployment.md).
