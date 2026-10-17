# Tenant Model

A tenant represents a PayrollNG customer/account. One tenant may own multiple companies; a company is not the tenant boundary.

## Proposed hierarchy
Tenant → Company → Branch → Department → Section → Unit → Employee

Not every organization needs every level.

## Isolation controls
- Resolve tenant context from authenticated identity and trusted server-side membership.
- Never trust a client-supplied TenantId as proof of authorization.
- Scope every tenant-owned query, command, export, file, cache key, and background job.
- Test cross-tenant denial at repository, application, API, and export boundaries.
- Audit tenant membership changes and privileged support access.

Super Admin is a platform identity, not a normal company payroll approver. Exceptional support access must be least-privilege and audited.
