# 26 Deployment And Releases

## Purpose
Architecture, requirements, boundaries, data, security, testing, and operational notes for this PayrollNG area.

## Design principles
- Enforce tenant isolation and server-side authorization.
- Keep business rules independent of UI and infrastructure.
- Audit important changes and protect sensitive information.
- Record assumptions and open questions.
- Distinguish proposed, implemented, and tested capabilities.

## Documents
- [Deployment Overview](./deployment-overview.md)
- [Local Development](./local-development.md)
- [Development Environment](./development-environment.md)
- [Staging Environment](./staging-environment.md)
- [Production Environment](./production-environment.md)
- [Database Migrations](./database-migrations.md)
- [Release Process](./release-process.md)
- [Rollback Procedure](./rollback-procedure.md)
- [Environment Variables](./environment-variables.md)
- [Firmware Release Process](./firmware-release-process.md)
- [Hardware Provisioning](./hardware-provisioning.md)

## Status
Proposed documentation baseline. It does not imply implementation or legal verification.
