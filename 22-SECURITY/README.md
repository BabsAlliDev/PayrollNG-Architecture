# 22 Security

## Purpose
Architecture, requirements, boundaries, data, security, testing, and operational notes for this PayrollNG area.

## Design principles
- Enforce tenant isolation and server-side authorization.
- Keep business rules independent of UI and infrastructure.
- Audit important changes and protect sensitive information.
- Record assumptions and open questions.
- Distinguish proposed, implemented, and tested capabilities.

## Documents
- [Security Overview](./security-overview.md)
- [Threat Model](./threat-model.md)
- [Password And Credential Policy](./password-and-credential-policy.md)
- [Tenant Authorization](./tenant-authorization.md)
- [Data Encryption](./data-encryption.md)
- [Secret Management](./secret-management.md)
- [Audit Logging](./audit-logging.md)
- [Secure File Handling](./secure-file-handling.md)
- [Rate Limiting](./rate-limiting.md)
- [Backup Security](./backup-security.md)
- [Incident Response](./incident-response.md)
- [Dependency Security](./dependency-security.md)
- [Device Credential Rotation](./device-credential-rotation.md)
- [Payment Security](./payment-security.md)

## Status
Proposed documentation baseline. It does not imply implementation or legal verification.
