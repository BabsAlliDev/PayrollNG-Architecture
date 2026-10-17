# PayrollNG — System Architecture

**Tagline:** Payroll made simple

This repository contains the architecture and technical documentation baseline for PayrollNG, a proposed payroll and workforce-management platform.

## Proposed stack
- C# / ASP.NET Core
- Blazor
- Entity Framework Core
- SQL Server
- Markdown and Mermaid
- .NET unit and integration tests

## Capabilities
- Tenant, company, employee and HR management
- Weekly/monthly payroll, review, approval and payslips
- Configurable/versioned Nigerian tax calculations
- Tax return preparation and future electronic filing
- Fingerprint-first attendance hardware and planned future RFID
- Leave, reports, notifications, subscriptions, support and audit
- Initial CSV salary-payment exports and future automated disbursement

## Key decisions
1. Start as a modular monolith with Clean Architecture boundaries.
2. Tenant is the customer/account boundary; a tenant may own multiple companies.
3. Super Admin is platform-level and separate from tenant users.
4. Version statutory tax rules and preserve versions used by finalized payroll.
5. Separate tax calculation, return preparation, submission, acknowledgement and tax payment.
6. Separate payment exports, instructions, settlement and reconciliation.
7. Develop fingerprint attendance first; RFID is a planned future capability.
8. Keep hardware and external providers behind explicit interfaces.

## Status
Documentation baseline only. Documents are proposals until reviewed and approved; they do not prove a feature has been implemented, tested, certified, or legally validated. Verify tax, payment, provider, and hardware requirements before production.
