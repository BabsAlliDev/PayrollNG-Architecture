# 17 Subscriptions And Billing

## Purpose
Architecture, requirements, boundaries, data, security, testing, and operational notes for this PayrollNG area.

## Design principles
- Enforce tenant isolation and server-side authorization.
- Keep business rules independent of UI and infrastructure.
- Audit important changes and protect sensitive information.
- Record assumptions and open questions.
- Distinguish proposed, implemented, and tested capabilities.

## Documents
- [Subscription Model](./subscription-model.md)
- [Plans And Entitlements](./plans-and-entitlements.md)
- [Subscription Lifecycle](./subscription-lifecycle.md)
- [Billing Records](./billing-records.md)
- [Usage Limits](./usage-limits.md)
- [Subscription Enforcement](./subscription-enforcement.md)
- [Invoices And Receipts](./invoices-and-receipts.md)
- [Renewals And Cancellations](./renewals-and-cancellations.md)
- [Future Recurring Billing Provider](./future-recurring-billing-provider.md)

## Status
Proposed documentation baseline. It does not imply implementation or legal verification.
