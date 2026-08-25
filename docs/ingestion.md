# Tracker reading ingestion

1. The BL-T3 tracker measures temperature and humidity every 5 minutes and publishes over MQTT (LTE-M).
2. The ingestion bridge subscribes to `tracker/+/readings`, batches up to 500 readings or 30 seconds.
3. The bridge signs the batch and calls `POST /readings` (see [API spec](../api/openapi.yaml), [example](../api/examples/reading-batch.json)).
4. The platform verifies the signature and stores each reading as received. Readings are never modified.

## Signature

Each batch carries an `X-Tracker-Signature` header: HMAC-SHA256 over the raw request body, hex encoded,
with a secret shared between the bridge and the platform. Batches with a missing or invalid signature are
rejected with `401`. Required since v2.3.1 (security review finding SR-2026-07).

## Duplicates

After losing coverage, a tracker re-sends its whole buffer when it reconnects. The same reading can
therefore arrive more than once. Readings are unique on `(tracker_id, sequence)`; duplicates are skipped
and counted in the response (`"duplicates": n`), never stored twice.

## Volumes

~2,000 trackers × 12 readings/hour ≈ 24,000 readings/hour.
