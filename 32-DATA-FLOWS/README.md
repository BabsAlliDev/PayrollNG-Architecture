# 32 Data Flows

## Purpose
Architecture, requirements, boundaries, data, security, testing, and operational notes for this PayrollNG area.

## Design principles
- Enforce tenant isolation and server-side authorization.
- Keep business rules independent of UI and infrastructure.
- Audit important changes and protect sensitive information.
- Record assumptions and open questions.
- Distinguish proposed, implemented, and tested capabilities.

## Documents
- [Employee Data Flow](./employee-data-flow.md)
- [Attendance Data Flow](./attendance-data-flow.md)
- [Payroll Data Flow](./payroll-data-flow.md)
- [Tax Calculation Data Flow](./tax-calculation-data-flow.md)
- [Tax Filing Data Flow](./tax-filing-data-flow.md)
- [Payment Export Data Flow](./payment-export-data-flow.md)
- [Future Payment Provider Data Flow](./future-payment-provider-data-flow.md)
- [Notification Data Flow](./notification-data-flow.md)
- [Hardware Sync Data Flow](./hardware-sync-data-flow.md)

## Status
Proposed documentation baseline. It does not imply implementation or legal verification.
