# Tracker reading ingestion

1. The BL-T3 tracker measures temperature and humidity every 5 minutes and publishes over MQTT (LTE-M).
2. The ingestion bridge subscribes to `tracker/+/readings`, batches up to 500 readings or 30 seconds.
3. The bridge calls `POST /readings` (see [API spec](../api/openapi.yaml), [example](../api/examples/reading-batch.json)).
4. The platform stores each reading as received. Readings are never modified.

## Duplicates

After losing coverage, a tracker re-sends its whole buffer when it reconnects. The same reading can
therefore arrive more than once. Readings are unique on `(tracker_id, sequence)`; duplicates are skipped
and counted in the response (`"duplicates": n`), never stored twice.

## Volumes

~2,000 trackers × 12 readings/hour ≈ 24,000 readings/hour.
