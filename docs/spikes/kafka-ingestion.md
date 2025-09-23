# Spike: Kafka for tracker readings

Date: September 2025 · Author: Jakub Lewandowski · Outcome: **not pursued**

## Question

Should the ingestion bridge publish readings to Kafka instead of calling the platform API directly?

## Findings

- Throughput is not a problem either way – we average ~40 messages/second.
- Kafka would give us replay of the reading stream, which is attractive for analytics.
- Operating a Kafka cluster ourselves is not worth it at our volume; a managed offering costs more than the
  rest of the platform infrastructure combined.

## Decision

Keep direct API ingestion. Revisit if volume grows 10× or if analytics needs a real-time stream.
Branch kept for reference.
