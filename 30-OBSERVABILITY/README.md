# 30 Observability

## Purpose
Architecture, requirements, boundaries, data, security, testing, and operational notes for this PayrollNG area.

## Design principles
- Enforce tenant isolation and server-side authorization.
- Keep business rules independent of UI and infrastructure.
- Audit important changes and protect sensitive information.
- Record assumptions and open questions.
- Distinguish proposed, implemented, and tested capabilities.

## Documents
- [Structured Logging](./structured-logging.md)
- [Distributed Tracing](./distributed-tracing.md)
- [Correlation Ids](./correlation-ids.md)
- [Audit Versus Operational Logs](./audit-versus-operational-logs.md)
- [Error Reporting](./error-reporting.md)
- [Log Retention](./log-retention.md)
- [Device Diagnostics](./device-diagnostics.md)
- [Integration Event Tracing](./integration-event-tracing.md)

## Status
Proposed documentation baseline. It does not imply implementation or legal verification.
