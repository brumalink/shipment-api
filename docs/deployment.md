# Deployment

| Environment | Purpose | Data |
|---|---|---|
| `dev` | Integration of feature branches | Synthetic |
| `staging` | Release candidates, customer UAT | Anonymised copy of prod (weekly) |
| `prod` | Live consignments | Real |

- The platform runs as a container behind a managed load balancer.
- Promotion `staging` → `prod` requires approval by the DevOps team and, for GDP-relevant changes, by QA.
- Infrastructure is described in the `infra-docs` repository.
