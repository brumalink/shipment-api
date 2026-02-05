# Tenants (3PL partners)

From v2.0, logistics partners can run their own consignments on the platform.

- A tenant has a **slug** (lowercase letters, digits, dashes; 4–32 characters), a name and a data region.
- Supported data regions: `eu-central`, `eu-north`.
- Every shipment belongs to exactly one tenant. Brumalink's own shipments use the `brumalink` tenant.

## Data isolation requirements

| # | Requirement | Verified by |
|---|---|---|
| T1 | A tenant's users see only that tenant's shipments, readings and custody events | UAT test set TEN-01 |
| T2 | Tenant data is stored only in the tenant's data region | Infrastructure review |
| T3 | Exports and webhooks never contain another tenant's data | UAT test set TEN-02 |
| T4 | Brumalink QA can see all tenants (read-only) for GDP oversight | Access review |

Validation record: `VAL-002` in `gdp-compliance-docs`.
