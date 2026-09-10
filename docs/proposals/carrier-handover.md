# Proposal: temperature continuity at carrier handover

Status: **draft**

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
