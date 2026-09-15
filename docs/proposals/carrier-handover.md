# Proposal: temperature continuity at carrier handover

Status: **ready for review**

## Problem

Since v2.0, 3PL partners hand consignments over to Brumalink (and back) at our hubs. Each carrier uses its own
tracker, so there is a moment when monitoring switches from one device to another. Today nothing checks that
this switch was seamless.

## Proposal

At each carrier handover, compare the **last reading of the outgoing tracker** with the **first reading of the
incoming tracker**:

- time gap must not exceed **15 minutes**,
- temperature difference must not exceed **2 °C**.

If either check fails, open a handover deviation and notify QA.

## Acceptance criteria

| Case | Outgoing | Incoming | Expected |
|---|---|---|---|
| Clean handover | 14:00, 5.0 °C | 14:06, 5.4 °C | OK |
| Monitoring gap | 14:00, 5.0 °C | 14:40, 5.1 °C | fail – gap of 40 min |
| Temperature jump | 14:00, 4.0 °C | 14:05, 7.5 °C | fail – jump of 3.5 °C |
| Clock skew | 14:00, 5.0 °C | 13:59, 5.0 °C | fail – incoming reading predates outgoing |

## Open points

- Should the 2 °C tolerance depend on the product profile? (QA to decide)
