# 07 Tax Engine

## Purpose
Architecture, requirements, boundaries, data, security, testing, and operational notes for this PayrollNG area.

## Design principles
- Enforce tenant isolation and server-side authorization.
- Keep business rules independent of UI and infrastructure.
- Audit important changes and protect sensitive information.
- Record assumptions and open questions.
- Distinguish proposed, implemented, and tested capabilities.

## Documents
- [Tax Engine Overview](./tax-engine-overview.md)
- [Nigerian Paye](./nigerian-paye.md)
- [Tax Rule Versioning](./tax-rule-versioning.md)
- [Effective Dated Rules](./effective-dated-rules.md)
- [Taxable Income](./taxable-income.md)
- [Tax Exemptions](./tax-exemptions.md)
- [Tax Calculation Workflow](./tax-calculation-workflow.md)
- [Tax Validation And Testing](./tax-validation-and-testing.md)
- [Tax Liability Ledger](./tax-liability-ledger.md)
- [Tax Adjustments](./tax-adjustments.md)
- [Multi Jurisdiction Tax Design](./multi-jurisdiction-tax-design.md)

## Status
Proposed documentation baseline. It does not imply implementation or legal verification.
