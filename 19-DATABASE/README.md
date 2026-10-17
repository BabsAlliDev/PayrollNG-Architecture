# 19 Database

## Purpose
Architecture, requirements, boundaries, data, security, testing, and operational notes for this PayrollNG area.

## Design principles
- Enforce tenant isolation and server-side authorization.
- Keep business rules independent of UI and infrastructure.
- Audit important changes and protect sensitive information.
- Record assumptions and open questions.
- Distinguish proposed, implemented, and tested capabilities.

## Documents
- [Database Overview](./database-overview.md)
- [Entity Relationship Model](./entity-relationship-model.md)
- [Tenant And Company Schema](./tenant-and-company-schema.md)
- [Employee Schema](./employee-schema.md)
- [Payroll Schema](./payroll-schema.md)
- [Tax Schema](./tax-schema.md)
- [Tax Filing Schema](./tax-filing-schema.md)
- [Attendance Schema](./attendance-schema.md)
- [Hardware Device Schema](./hardware-device-schema.md)
- [Leave Schema](./leave-schema.md)
- [Payments Schema](./payments-schema.md)
- [Subscriptions Schema](./subscriptions-schema.md)
- [Audit Schema](./audit-schema.md)
- [Indexes And Constraints](./indexes-and-constraints.md)
- [Migrations And Seeding](./migrations-and-seeding.md)
- [Data Retention](./data-retention.md)
- [Concurrency And Transactions](./concurrency-and-transactions.md)
- [Backup And Restore](./backup-and-restore.md)

## Status
Proposed documentation baseline. It does not imply implementation or legal verification.
