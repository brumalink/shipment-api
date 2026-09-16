# Proposal: signed excursion webhooks

Status: **draft**

## Problem

Customers asked how they can verify that an excursion webhook really comes from Brumalink.

## Proposal

Each webhook carries a header:

```
X-Brumalink-Signature: t=<unix timestamp>,v1=<hex HMAC-SHA256 of "<timestamp>.<body>">
```

- The secret is issued per customer and can be rotated in the customer portal.
- Receivers reject messages older than 5 minutes (replay protection).
- The scheme mirrors what common payment providers use, so customers can reuse existing verifiers.

## Rollout

1. Send the header to all customers (non-breaking).
2. Publish verification guide in the customer portal.
3. After 3 months, stop sending unsigned webhooks.
