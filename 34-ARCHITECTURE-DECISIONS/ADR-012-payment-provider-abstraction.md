# ADR-012: Abstract Future Payment Providers

- Status: Proposed
- Decision: Keep CSV export initially; add provider integration after a concrete provider and requirements are verified.
- Consequences: Keep provider-specific logic outside payroll domain code. Model idempotency, payment states, reconciliation, and audit explicitly.
- Review trigger: Provider selection and successful sandbox proof of concept.
