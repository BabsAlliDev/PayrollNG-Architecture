# 34 Architecture Decisions

## Purpose
Architecture, requirements, boundaries, data, security, testing, and operational notes for this PayrollNG area.

## Design principles
- Enforce tenant isolation and server-side authorization.
- Keep business rules independent of UI and infrastructure.
- Audit important changes and protect sensitive information.
- Record assumptions and open questions.
- Distinguish proposed, implemented, and tested capabilities.

## Documents
- [Adr 001 Modular Monolith](./ADR-001-modular-monolith.md)
- [Adr 002 Clean Architecture](./ADR-002-clean-architecture.md)
- [Adr 003 Tenant Boundary](./ADR-003-tenant-boundary.md)
- [Adr 004 Super Admin Separation](./ADR-004-super-admin-separation.md)
- [Adr 005 Sql Server](./ADR-005-sql-server.md)
- [Adr 006 Csv Payment Export](./ADR-006-csv-payment-export.md)
- [Adr 007 Fingerprint First](./ADR-007-fingerprint-first.md)
- [Adr 008 Versioned Tax Rules](./ADR-008-versioned-tax-rules.md)
- [Adr 009 Hardware Abstraction](./ADR-009-hardware-abstraction.md)
- [Adr 010 Rfid Future Support](./ADR-010-rfid-future-support.md)
- [Adr 011 Tax Filing Phases](./ADR-011-tax-filing-phases.md)
- [Adr 012 Payment Provider Abstraction](./ADR-012-payment-provider-abstraction.md)

## Status
Proposed documentation baseline. It does not imply implementation or legal verification.
