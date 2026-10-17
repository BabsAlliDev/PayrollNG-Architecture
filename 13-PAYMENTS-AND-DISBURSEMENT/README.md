# 13 Payments And Disbursement

## Purpose
Architecture, requirements, boundaries, data, security, testing, and operational notes for this PayrollNG area.

## Design principles
- Enforce tenant isolation and server-side authorization.
- Keep business rules independent of UI and infrastructure.
- Audit important changes and protect sensitive information.
- Record assumptions and open questions.
- Distinguish proposed, implemented, and tested capabilities.

## Documents
- [Payment Architecture](./payment-architecture.md)
- [Payment Batches](./payment-batches.md)
- [Bank Details And Validation](./bank-details-and-validation.md)
- [Csv Payment Export](./csv-payment-export.md)
- [Bank Export Formatters](./bank-export-formatters.md)
- [Payment Approval](./payment-approval.md)
- [Payment Instructions](./payment-instructions.md)
- [Payment Provider Abstraction](./payment-provider-abstraction.md)
- [Banking Api Integration](./banking-api-integration.md)
- [Payment Gateway Integration](./payment-gateway-integration.md)
- [Future Nibss Integration](./future-nibss-integration.md)
- [Payment Status And Webhooks](./payment-status-and-webhooks.md)
- [Payment Reconciliation](./payment-reconciliation.md)
- [Payment Failure And Retry](./payment-failure-and-retry.md)
- [Payment Idempotency](./payment-idempotency.md)
- [Payment Audit Trail](./payment-audit-trail.md)
- [Payment Ledger](./payment-ledger.md)
- [Refunds And Reversals](./refunds-and-reversals.md)
- [Disbursement Security](./disbursement-security.md)
- [Payment Provider Selection](./payment-provider-selection.md)

## Status
Proposed documentation baseline. It does not imply implementation or legal verification.
