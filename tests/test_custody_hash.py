from app.services.custody_hash import GENESIS, build_chain, event_hash, verify_chain

EVENTS = [
    {"occurred_at": "2025-05-02T06:10:00+02:00", "from": "WAW-HUB-1", "to": "driver:TW-114", "location": "WAW"},
    {"occurred_at": "2025-05-02T09:45:00+02:00", "from": "driver:TW-114", "to": "POZ-HUB-1", "location": "POZ"},
    {"occurred_at": "2025-05-02T13:20:00+02:00", "from": "POZ-HUB-1", "to": "Apteka Centralna", "location": "POZ"},
]


def test_first_hash_is_chained_to_genesis():
    assert build_chain(EVENTS)[0] == event_hash(GENESIS, EVENTS[0])


def test_intact_chain_verifies():
    assert verify_chain(EVENTS, build_chain(EVENTS)) is None


def test_modified_event_is_detected():
    hashes = build_chain(EVENTS)
    tampered = [dict(e) for e in EVENTS]
    tampered[1]["to"] = "POZ-HUB-2"
    assert verify_chain(tampered, hashes) == 1


def test_removed_event_is_detected():
    hashes = build_chain(EVENTS)
    assert verify_chain(EVENTS[:1] + EVENTS[2:], hashes[:1] + hashes[2:]) == 1


def test_key_order_does_not_matter():
    reordered = [dict(reversed(list(e.items()))) for e in EVENTS]
    assert build_chain(reordered) == build_chain(EVENTS)
