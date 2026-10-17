# 33 Diagrams

## Purpose
Architecture, requirements, boundaries, data, security, testing, and operational notes for this PayrollNG area.

## Design principles
- Enforce tenant isolation and server-side authorization.
- Keep business rules independent of UI and infrastructure.
- Audit important changes and protect sensitive information.
- Record assumptions and open questions.
- Distinguish proposed, implemented, and tested capabilities.

## Documents
- [System Context Diagram](./system-context-diagram.md)
- [Container Diagram](./container-diagram.md)
- [Module Dependency Diagram](./module-dependency-diagram.md)
- [Deployment Diagram](./deployment-diagram.md)
- [Tenant Data Isolation Diagram](./tenant-data-isolation-diagram.md)
- [Payroll Sequence Diagram](./payroll-sequence-diagram.md)
- [Payroll State Machine](./payroll-state-machine.md)
- [Employee Lifecycle Diagram](./employee-lifecycle-diagram.md)
- [Database Erd](./database-erd.md)
- [Payment Export Sequence](./payment-export-sequence.md)
- [Future Payment Disbursement Sequence](./future-payment-disbursement-sequence.md)
- [Tax Filing Sequence](./tax-filing-sequence.md)
- [Hardware Device Architecture](./hardware-device-architecture.md)
- [Fingerprint Attendance Sequence](./fingerprint-attendance-sequence.md)
- [Rfid Attendance Sequence](./rfid-attendance-sequence.md)
- [Offline Device Sync Sequence](./offline-device-sync-sequence.md)

## Status
Proposed documentation baseline. It does not imply implementation or legal verification.
