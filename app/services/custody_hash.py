"""Tamper-evident hash chain for custody events (ADR 0003).

hash_n = sha256(hash_{n-1} + canonical_json(event_n)), starting from GENESIS.
Changing, removing or reordering any past event breaks every hash after it.
"""

import hashlib
import json

GENESIS = "0" * 64


def event_hash(prev_hash: str, event: dict) -> str:
    payload = json.dumps(event, sort_keys=True, separators=(",", ":"), default=str)
    return hashlib.sha256((prev_hash + payload).encode()).hexdigest()


def build_chain(events: list[dict]) -> list[str]:
    hashes: list[str] = []
    prev = GENESIS
    for event in events:
        prev = event_hash(prev, event)
        hashes.append(prev)
    return hashes


def verify_chain(events: list[dict], hashes: list[str]) -> int | None:
    """Return the index of the first event whose hash doesn't match, or None if the chain is intact."""
    if len(events) != len(hashes):
        return min(len(events), len(hashes))
    prev = GENESIS
    for i, (event, stored) in enumerate(zip(events, hashes, strict=True)):
        prev = event_hash(prev, event)
        if prev != stored:
            return i
    return None
