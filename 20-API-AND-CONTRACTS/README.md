# 20 Api And Contracts

## Purpose
Architecture, requirements, boundaries, data, security, testing, and operational notes for this PayrollNG area.

## Design principles
- Enforce tenant isolation and server-side authorization.
- Keep business rules independent of UI and infrastructure.
- Audit important changes and protect sensitive information.
- Record assumptions and open questions.
- Distinguish proposed, implemented, and tested capabilities.

## Documents
- [Api Overview](./api-overview.md)
- [Api Versioning](./api-versioning.md)
- [Authentication](./authentication.md)
- [Request Validation](./request-validation.md)
- [Error Contract](./error-contract.md)
- [Pagination And Filtering](./pagination-and-filtering.md)
- [Idempotency](./idempotency.md)
- [Rate Limiting](./rate-limiting.md)
- [Api Documentation](./api-documentation.md)
- [Hardware Device Api](./hardware-device-api.md)
- [Payment Provider Contracts](./payment-provider-contracts.md)
- [Tax Authority Contracts](./tax-authority-contracts.md)
- [Webhook Contracts](./webhook-contracts.md)

## Status
Proposed documentation baseline. It does not imply implementation or legal verification.
