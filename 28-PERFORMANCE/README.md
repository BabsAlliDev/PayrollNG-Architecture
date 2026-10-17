# 28 Performance

## Purpose
Architecture, requirements, boundaries, data, security, testing, and operational notes for this PayrollNG area.

## Design principles
- Enforce tenant isolation and server-side authorization.
- Keep business rules independent of UI and infrastructure.
- Audit important changes and protect sensitive information.
- Record assumptions and open questions.
- Distinguish proposed, implemented, and tested capabilities.

## Documents
- [Performance Objectives](./performance-objectives.md)
- [Database Performance](./database-performance.md)
- [Payroll Batch Performance](./payroll-batch-performance.md)
- [Caching Strategy](./caching-strategy.md)
- [Background Processing](./background-processing.md)
- [Load Testing](./load-testing.md)
- [Device Event Throughput](./device-event-throughput.md)
- [Bulk Reporting](./bulk-reporting.md)

## Status
Proposed documentation baseline. It does not imply implementation or legal verification.
