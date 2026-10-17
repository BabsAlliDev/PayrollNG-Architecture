# Architecture Overview

## Proposed architecture
Start with a modular monolith using Clean Architecture boundaries. This keeps deployment manageable while preserving modules that can be tested and evolved independently.

## Proposed technology stack
- Backend: C# / ASP.NET Core
- UI: Blazor
- Data access: Entity Framework Core
- Database: SQL Server
- Documentation: Markdown and Mermaid
- Testing: .NET unit and integration tests

Confirm exact versions, hosting, and providers before implementation.

## Layers
1. Presentation: Blazor pages and API endpoints.
2. Application: use cases and orchestration.
3. Domain: business rules, entities, and domain services.
4. Infrastructure: persistence, file storage, email, hardware, and external-provider adapters.

## Key boundaries
- Tenant is the customer/account boundary and may contain multiple companies.
- Super Admin is platform-level and separate from tenant users.
- Tax rules are versioned and effective-dated.
- Tax calculation, return preparation, filing, payment, and authority acknowledgement are separate states.
- Payment export is not payment settlement.
- Hardware and provider integrations use explicit interfaces.

Status: Proposed baseline, not proof of implementation.
