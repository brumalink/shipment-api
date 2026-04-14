# Data model

```mermaid
erDiagram
    TENANT ||--o{ SHIPMENT : "owns"
    SHIPMENT ||--o{ CUSTODY_EVENT : "has"
    SHIPMENT }o--o| TRACKER : "monitored by"
    TRACKER ||--o{ SENSOR_READING : "reports"

    TENANT {
        string slug PK
        string name
        string data_region
    }
    SHIPMENT {
        string reference PK
        string tenant_slug FK
        string product_profile
        string origin
        string destination
        string status
        float min_temp_c
        float max_temp_c
    }
    SENSOR_READING {
        string tracker_id
        int sequence
        datetime recorded_at
        float temperature_c
    }
    CUSTODY_EVENT {
        datetime occurred_at
        string from_party
        string to_party
        string prev_hash
        string hash
    }
```

Temperature limits are copied onto the shipment at creation time, so later changes to a product profile
never alter the evaluation of historical shipments.

Since v2.0 every shipment belongs to a tenant. Brumalink's own consignments use the `brumalink` tenant.
Sensor readings are partitioned monthly and retained for 5 years (ADR 0004).
