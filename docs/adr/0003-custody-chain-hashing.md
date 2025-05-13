# ADR 0003: Hash-chained custody events

- Status: accepted
- Date: 2025-05-06
- Deciders: Marta Zielińska, Piotr Kaczmarek (QA)

## Context

During a customer audit we had to prove that a custody record had not been edited after the fact. Database audit logs
were accepted, but the auditor recommended a tamper-evident mechanism at the application level.

## Decision

Each custody event stores `prev_hash` and `hash = sha256(prev_hash + canonical_json(event))`. The first event of a
shipment chains to a genesis value of 64 zeros.

## Consequences

- Any modification, deletion or reordering of past events is detectable (`verify_chain`).
- Events are append-only; corrections are recorded as new events referencing the corrected one.
- The hashing code is GDP-relevant: changes require QA sign-off (see CODEOWNERS).
