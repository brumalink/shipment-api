# Chain of custody

## Requirements

- Every handover of a consignment is recorded: warehouse → driver, driver → hub, hub → consignee.
- A record contains: time, from, to, location, person who signed.
- Records are **append-only**. Corrections are new records that reference the corrected one.
- It must be possible to prove that no record was altered after the fact (customer audit finding, April 2025).

Design: see [ADR 0003](adr/0003-custody-chain-hashing.md).
