from pathlib import Path

ROOT = Path.cwd()

# Every major PayrollNG architecture documentation module.
SECTIONS = {
    "00-OVERVIEW": """
    product-vision scope-and-objectives system-requirements
    stakeholders-and-roles glossary assumptions-and-constraints
    product-capabilities release-scope
    """,
    "01-SYSTEM-ARCHITECTURE": """
    architecture-overview architectural-principles clean-architecture
    modular-monolith technology-stack system-context quality-attributes
    module-boundaries background-processing
    """,
    "02-IDENTITY-AND-ACCESS": """
    authentication authorization roles-and-permissions super-admin
    tenant-admin hr-user payroll-user finance-user employee-self-service
    session-management account-recovery multi-factor-authentication
    """,
    "03-MULTI-TENANCY": """
    tenant-model tenant-provisioning tenant-isolation tenant-configuration
    tenant-lifecycle tenant-data-access cross-tenant-support
    tenant-deletion-and-retention
    """,
    "04-ORGANIZATION": """
    company-management branch-management department-management
    section-and-unit-management organization-hierarchy
    company-specific-settings multiple-companies-per-tenant
    """,
    "05-EMPLOYEE-MANAGEMENT": """
    employee-lifecycle employee-profiles employment-records
    job-and-position-management employee-documents employee-benefits
    employee-import-and-export employee-offboarding employee-data-access
    """,
    "06-PAYROLL": """
    payroll-overview payroll-calendar pay-components earnings-and-allowances
    deductions overtime bonus-management loan-management payroll-calculation
    payroll-review payroll-approval payroll-finalization
    payroll-reversal-and-adjustment payroll-history weekly-and-monthly-payroll
    payroll-validation payroll-reconciliation payroll-locking-and-period-close
    """,
    "07-TAX-ENGINE": """
    tax-engine-overview nigerian-paye tax-rule-versioning
    effective-dated-rules taxable-income tax-exemptions
    tax-calculation-workflow tax-validation-and-testing
    tax-liability-ledger tax-adjustments multi-jurisdiction-tax-design
    """,
    "08-TAX-FILING-AND-STATUTORY-REPORTING": """
    tax-filing-overview employer-tax-obligations paye-return-preparation
    employee-tax-schedules statutory-report-generation tax-filing-calendar
    tax-payment-records filing-approval-workflow filing-evidence-and-receipts
    tax-authority-integration tax-filing-reconciliation
    filing-amendments-and-corrections filing-audit-trail future-electronic-filing
    """,
    "09-ATTENDANCE": """
    attendance-overview clock-in-and-clock-out attendance-records
    work-schedules shifts lateness-and-absence overtime-attendance
    attendance-corrections attendance-import attendance-approval
    attendance-policy attendance-to-payroll
    """,
    "10-HARDWARE-INTEGRATION": """
    hardware-architecture hardware-requirements hardware-bill-of-materials
    hardware-component-selection hardware-block-diagram electrical-design
    power-management microcontroller-firmware-architecture
    fingerprint-sensor-integration rfid-reader-integration
    display-and-user-interface real-time-clock local-storage-and-offline-mode
    wifi-and-networking cloud-api-integration device-authentication
    attendance-event-protocol device-enrollment-and-registration
    offline-sync-and-retry firmware-update-strategy hardware-security
    device-health-monitoring pcb-design enclosure-design hardware-assembly
    hardware-testing hardware-troubleshooting hardware-cost-estimation
    hardware-prototype-roadmap manufacturing-and-quality-control
    """,
    "11-BIOMETRICS-AND-RFID": """
    biometric-architecture fingerprint-enrollment fingerprint-verification
    biometric-template-protection rfid-attendance-architecture
    rfid-card-enrollment rfid-card-revocation rfid-event-validation
    fingerprint-vs-rfid attendance-device-abstraction
    future-multi-factor-attendance biometric-privacy-and-retention
    """,
    "12-LEAVE": """
    leave-types leave-policies leave-balances leave-application
    leave-approval leave-calendar leave-accrual-and-carryover leave-to-payroll
    """,
    "13-PAYMENTS-AND-DISBURSEMENT": """
    payment-architecture payment-batches bank-details-and-validation
    csv-payment-export bank-export-formatters payment-approval
    payment-instructions payment-provider-abstraction banking-api-integration
    payment-gateway-integration future-nibss-integration
    payment-status-and-webhooks payment-reconciliation payment-failure-and-retry
    payment-idempotency payment-audit-trail payment-ledger refunds-and-reversals
    disbursement-security payment-provider-selection
    """,
    "14-PAYSLIPS": """
    payslip-generation payslip-data-model payslip-pdf-rendering
    payslip-delivery payslip-access-control payslip-corrections
    """,
    "15-REPORTING-AND-ANALYTICS": """
    reporting-architecture payroll-reports employee-reports attendance-reports
    tax-reports payment-reports statutory-reports financial-exports
    report-permissions management-dashboards data-export-controls
    """,
    "16-NOTIFICATIONS": """
    notification-architecture in-app-notifications email-notifications
    sms-notifications notification-templates notification-preferences
    notification-retries delivery-status
    """,
    "17-SUBSCRIPTIONS-AND-BILLING": """
    subscription-model plans-and-entitlements subscription-lifecycle
    billing-records usage-limits subscription-enforcement invoices-and-receipts
    renewals-and-cancellations future-recurring-billing-provider
    """,
    "18-SUPPORT": """
    support-tickets ticket-lifecycle support-agent-access support-audit-trail
    customer-feedback support-escalation
    """,
    "19-DATABASE": """
    database-overview entity-relationship-model tenant-and-company-schema
    employee-schema payroll-schema tax-schema tax-filing-schema
    attendance-schema hardware-device-schema leave-schema payments-schema
    subscriptions-schema audit-schema indexes-and-constraints
    migrations-and-seeding data-retention concurrency-and-transactions
    backup-and-restore
    """,
    "20-API-AND-CONTRACTS": """
    api-overview api-versioning authentication request-validation error-contract
    pagination-and-filtering idempotency rate-limiting api-documentation
    hardware-device-api payment-provider-contracts tax-authority-contracts
    webhook-contracts
    """,
    "21-FRONTEND": """
    frontend-overview application-shell navigation-and-routing design-system
    forms-and-validation state-management accessibility responsive-design
    employee-portal admin-console payroll-review-interface
    hardware-management-interface
    """,
    "22-SECURITY": """
    security-overview threat-model password-and-credential-policy
    tenant-authorization data-encryption secret-management audit-logging
    secure-file-handling rate-limiting backup-security incident-response
    dependency-security device-credential-rotation payment-security
    """,
    "23-DATA-PRIVACY-AND-COMPLIANCE": """
    privacy-overview personal-data-inventory data-minimization
    employee-data-access retention-and-deletion data-subject-requests
    privacy-impact-assessment nigeria-data-protection biometric-data-protection
    financial-data-protection tax-compliance-responsibilities legal-review-register
    """,
    "24-INTEGRATIONS": """
    integration-architecture email-provider sms-provider fingerprint-devices
    rfid-devices banking-interfaces payment-providers tax-authorities
    government-services external-apis webhooks integration-failure-handling
    provider-selection-and-certification
    """,
    "25-INFRASTRUCTURE": """
    infrastructure-overview application-hosting sql-server-hosting file-storage
    networking-and-firewalls environment-configuration scaling-strategy
    hardware-device-connectivity
    """,
    "26-DEPLOYMENT-AND-RELEASES": """
    deployment-overview local-development development-environment
    staging-environment production-environment database-migrations
    release-process rollback-procedure environment-variables
    firmware-release-process hardware-provisioning
    """,
    "27-MONITORING-AND-RELIABILITY": """
    health-checks application-metrics infrastructure-metrics alerting
    availability-objectives capacity-planning device-health-monitoring
    integration-monitoring payment-failure-monitoring tax-filing-deadline-alerts
    """,
    "28-PERFORMANCE": """
    performance-objectives database-performance payroll-batch-performance
    caching-strategy background-processing load-testing
    device-event-throughput bulk-reporting
    """,
    "29-TESTING-AND-QUALITY": """
    testing-strategy unit-tests integration-tests api-tests
    tenant-isolation-tests payroll-calculation-tests tax-engine-tests
    tax-filing-tests payment-export-tests payment-provider-sandbox-tests
    hardware-in-the-loop-tests rfid-tests fingerprint-device-tests security-tests
    end-to-end-tests performance-tests test-data-management regression-testing
    """,
    "30-OBSERVABILITY": """
    structured-logging distributed-tracing correlation-ids
    audit-versus-operational-logs error-reporting log-retention
    device-diagnostics integration-event-tracing
    """,
    "31-BUSINESS-FLOWS": """
    tenant-onboarding company-onboarding employee-onboarding payroll-run
    payroll-approval payment-export future-payment-disbursement
    tax-return-preparation future-tax-electronic-filing employee-leave
    employee-offboarding subscription-change support-ticket-resolution
    fingerprint-attendance-event rfid-attendance-event
    device-enrollment-and-revocation
    """,
    "32-DATA-FLOWS": """
    employee-data-flow attendance-data-flow payroll-data-flow
    tax-calculation-data-flow tax-filing-data-flow payment-export-data-flow
    future-payment-provider-data-flow notification-data-flow hardware-sync-data-flow
    """,
    "33-DIAGRAMS": """
    system-context-diagram container-diagram module-dependency-diagram
    deployment-diagram tenant-data-isolation-diagram payroll-sequence-diagram
    payroll-state-machine employee-lifecycle-diagram database-erd
    payment-export-sequence future-payment-disbursement-sequence
    tax-filing-sequence hardware-device-architecture
    fingerprint-attendance-sequence rfid-attendance-sequence
    offline-device-sync-sequence
    """,
    "34-ARCHITECTURE-DECISIONS": """
    ADR-001-modular-monolith ADR-002-clean-architecture ADR-003-tenant-boundary
    ADR-004-super-admin-separation ADR-005-sql-server ADR-006-csv-payment-export
    ADR-007-fingerprint-first ADR-008-versioned-tax-rules
    ADR-009-hardware-abstraction ADR-010-rfid-future-support
    ADR-011-tax-filing-phases ADR-012-payment-provider-abstraction
    """,
    "35-DEVELOPMENT-STANDARDS": """
    coding-conventions naming-conventions branching-strategy commit-messages
    pull-request-process code-review documentation-standards
    dependency-management configuration-and-secrets definition-of-done
    """,
    "36-OPERATIONS-AND-CONTINUITY": """
    backup-and-restore disaster-recovery incident-management maintenance
    data-migration operational-runbooks access-reviews tax-deadline-operations
    payment-incident-runbook hardware-replacement-and-recovery
    """,
    "37-ROADMAP-AND-FUTURE-CAPABILITIES": """
    release-phases mvp-scope post-mvp-capabilities known-limitations
    technical-debt-register future-microservices-assessment
    fingerprint-v1-rfid-v2 future-payment-processing future-tax-filing
    future-multi-country-tax future-hardware-productization
    """,
}

# Curated documents for important product and architecture decisions.
SPECIAL = {
"01-SYSTEM-ARCHITECTURE/architecture-overview.md": """
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
""",
"03-MULTI-TENANCY/tenant-model.md": """
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
""",
"06-PAYROLL/payroll-calculation.md": """
# Payroll Calculation

## Proposed workflow
1. Select tenant, company, period, and weekly/monthly frequency.
2. Snapshot eligible employees and inputs.
3. Validate employment, compensation, attendance, and required records.
4. Calculate configured earnings and allowances.
5. Calculate deductions and statutory items using approved, effective-dated rules.
6. Calculate net pay and reconcile totals.
7. Submit for review and approval.
8. Finalize an auditable payroll snapshot.
9. Generate payslips and permitted payment instructions/exports.

## Invariants
Identical inputs and rule versions should produce deterministic results. Finalized payroll must not be silently overwritten. Corrections use controlled adjustments/reversals. Duplicate submissions must not create duplicate runs or payments. Weekly/monthly periods need explicit boundaries and overlap protection.

Payroll staff prepare and review; Finance is the proposed default final approver. Test rounding, hires/exits, unpaid leave, overtime, bonuses, corrections, rule changes, concurrency, and idempotency.
""",
"07-TAX-ENGINE/tax-engine-overview.md": """
# Tax Engine Overview

Provide deterministic, testable tax calculations for a specific jurisdiction and tax period. Keep rules out of UI/controller code. Version rules with jurisdiction, source, approval status, effective dates, and tests. Preserve the rule version and breakdown used by finalized payroll.

Nigerian PAYE rules, thresholds, reliefs, employer obligations, and effective dates must be checked against current official legislation and tax-authority guidance before production. Have qualified tax/accounting professionals validate calculations and reporting.

Tax calculation is separate from return preparation, filing submission, tax payment, and authority acknowledgement. No rule set should be marked production-approved without source evidence, tests, reviewer, approval date, and effective date.
""",
"08-TAX-FILING-AND-STATUTORY-REPORTING/tax-filing-overview.md": """
# Tax Filing and Statutory Reporting

## Product direction
PayrollNG may evolve from calculating payroll tax and preparing reports into assisting employers with return preparation, payment tracking, electronic submission, and reconciliation. These are separate capabilities.

## Phased delivery
1. Calculate tax using approved, effective-dated rules.
2. Generate reviewable tax schedules and return-ready reports.
3. Track obligations, deadlines, approvals, submitted documents, payment references, and evidence.
4. Add electronic filing only after official interfaces, permissions, credentials, legal requirements, and testing arrangements are verified.
5. Reconcile liabilities, payments, receipts, assessments, and amendments.

Track jurisdiction, employer, tax period, return type, due date, rule version, liability, approver, submission status, reference, receipt, payment status, amendments, and audit events as applicable.

A generated report is not a filed return. A payment reference is not proof of payment. Do not assume an authority offers an API. Verify current official Nigerian federal and state requirements with qualified professionals.
""",
"10-HARDWARE-INTEGRATION/hardware-architecture.md": """
# Hardware Integration Architecture

## Current focus
PayrollNG is developing a fingerprint-first attendance hardware prototype. Record actual selected components, board revisions, firmware versions, and test evidence as they become known. Do not invent finalized specifications.

## Logical components
- Microcontroller and firmware
- Fingerprint sensor and enrollment flow
- Display and operator feedback
- Real-time clock
- Local event storage for offline use
- Wi-Fi/network interface
- Device identity and credentials
- HTTPS API client and synchronization queue
- Health and diagnostics reporting

## Reliability
Design for power loss, network outage, clock drift, repeated events, retries, storage limits, credential revocation, device replacement, and firmware update failure. Events should have stable identifiers and be idempotent.

## Security and privacy
Do not store raw fingerprint images by default. Prefer sensor-side matching or protected templates after review. Protect credentials, use TLS, support revocation, restrict enrollment, and audit administration.

## RFID
RFID is planned for a later version, not claimed as implemented. Use a device/event abstraction so RFID can be added without rewriting payroll logic.
""",
"11-BIOMETRICS-AND-RFID/rfid-attendance-architecture.md": """
# RFID Attendance Architecture

Status: Planned future capability. The first hardware direction is fingerprint-first.

## Intended flow
1. An authorized administrator registers a card/token and assigns it to an employee.
2. A reader produces a credential reference.
3. The device creates an event with event ID, device ID, timestamp, and credential reference.
4. The backend authenticates the device and validates assignment, format, replay, and duplicate status.
5. Attendance policy accepts, flags, or rejects the event.
6. Authorized staff review exceptions and corrections.

A card UID alone may be clonable and must not automatically be treated as strong identity proof. Select card technology after threat modelling. Include card assignment/revocation, lost-card handling, audit history, replay/clone tests, and offline behavior. Payroll should consume validated attendance records independently of reader type.
""",
"13-PAYMENTS-AND-DISBURSEMENT/payment-architecture.md": """
# Payments and Disbursement Architecture

## Initial scope
Generate validated downloadable CSV salary-payment files for manual bank upload.

## Future scope
Provider/bank APIs, payment initiation, status callbacks, reconciliation, and controlled disbursement, subject to provider selection and verification.

Model distinct states: payroll approved → batch prepared → instruction exported/submitted → provider processing → confirmed/failed/unknown → reconciled. A CSV export is not a bank transfer, and a submitted request is not necessarily a successful payment.

Controls: validate bank details and totals; enforce approval; use idempotency keys; persist provider references and state transitions; verify callbacks; handle duplicates/out-of-order events; reconcile outcomes; protect bank data; audit preparation, approval, submission, retries, and reconciliation.

Do not claim a bank or NIBSS API integration exists until official access and requirements are verified.
""",
"13-PAYMENTS-AND-DISBURSEMENT/future-payment-provider-integration.md": """
# Future Payment Provider Integration

Status: Future capability; no direct bank, gateway, or NIBSS integration is assumed implemented.

Before selecting a provider, verify commercial/legal eligibility, official API documentation, authentication, sandbox, supported banks, limits, fees, settlement semantics, security, and operational support.

Proposed lifecycle: prepare batch → validate → approve → submit once with idempotency key → record provider reference → process callback/polling → reconcile → retain evidence.

Treat timeouts as unknown outcomes until reconciled; do not blindly retry a transfer that may already have succeeded. Verify callback authenticity and handle duplicate/out-of-order notifications. Keep manual CSV export as fallback until automation is proven.
""",
"37-ROADMAP-AND-FUTURE-CAPABILITIES/fingerprint-v1-rfid-v2.md": """
# Attendance Hardware Roadmap: Fingerprint First, RFID Later

## Version 1: fingerprint-first prototype
Select and test sensor/controller; build enrollment and verification; provide local event buffering and authenticated synchronization; validate events and audit device administration; document tested revisions and limitations.

## Version 2: RFID
Select reader/card technology after threat modelling; add card enrollment, assignment, revocation, and lost-card workflows; reuse device identity, event contracts, synchronization, and attendance policy; test cloning risks, replay, offline operation, and duplicate events.

Payroll and HR consume validated attendance records, not sensor-specific data. RFID remains planned until hardware and software tests demonstrate the integration.
""",
"37-ROADMAP-AND-FUTURE-CAPABILITIES/future-payment-processing.md": """
# Future Payment Processing

1. Validated downloadable CSV export.
2. Export tracking and manual reconciliation.
3. Provider evaluation and sandbox prototype.
4. Approved payment initiation with idempotency and dual control.
5. Callback/status handling and reconciliation.
6. Production rollout only after provider, security, finance, legal, and operational approval.

Never imply payment settled because a file was generated or a request submitted. Preserve manual processing as a fallback until automated processing is verified.
""",
"37-ROADMAP-AND-FUTURE-CAPABILITIES/future-tax-filing.md": """
# Future Tax Filing

1. Reliable payroll tax calculation with approved, versioned rules.
2. Generate tax schedules and return-ready reports.
3. Track tax periods, deadlines, review, approval, and manual filing evidence.
4. Evaluate electronic filing with the relevant tax authority or approved provider.
5. Implement submission, authority acknowledgement, amendments, and reconciliation if official interfaces and permissions support them.

Do not assume a public API exists. Verify current official processes, formats, access requirements, deadlines, and legal obligations. Keep filing preparation distinct from submission and accepted filing status.
""",
"34-ARCHITECTURE-DECISIONS/ADR-006-csv-payment-export.md": """
# ADR-006: Begin with Manual CSV Payment Export

- Status: Proposed
- Context: Direct banking provider requirements are not yet verified.
- Decision: Begin with validated downloadable CSV files for manual bank upload.
- Consequences: Export is not proof of payment. Model export, submission, settlement, and reconciliation separately.
- Review trigger: Provider, contract, API, sandbox, and security requirements are verified.
""",
"34-ARCHITECTURE-DECISIONS/ADR-007-fingerprint-first.md": """
# ADR-007: Fingerprint-First Hardware Prototype

- Status: Proposed
- Context: Attendance hardware is under development; final sensor/controller choices must be verified.
- Decision: Prioritize fingerprint for the first version and isolate device details behind adapters.
- Consequences: Avoid raw fingerprint-image storage by default. Test hardware and review privacy/security before deployment.
- Review trigger: Prototype evidence requires a change.
""",
"34-ARCHITECTURE-DECISIONS/ADR-010-rfid-future-support.md": """
# ADR-010: Keep RFID as a Future Attendance Option

- Status: Proposed
- Decision: Design reusable device/event contracts but do not claim RFID is implemented until hardware and software are tested.
- Consequences: Review credential security, revocation, cloning, replay, and offline behavior.
- Review trigger: Version 2 planning and reader/card selection.
""",
"34-ARCHITECTURE-DECISIONS/ADR-011-tax-filing-phases.md": """
# ADR-011: Phase Tax Filing Separately from Tax Calculation

- Status: Proposed
- Decision: Validate calculation first, add return preparation next, then consider electronic filing only after official requirements and access are verified.
- Consequences: A generated schedule is not a filed return; filing status requires evidence or a verified authority response.
- Review trigger: Official interfaces or legal obligations change.
""",
"34-ARCHITECTURE-DECISIONS/ADR-012-payment-provider-abstraction.md": """
# ADR-012: Abstract Future Payment Providers

- Status: Proposed
- Decision: Keep CSV export initially; add provider integration after a concrete provider and requirements are verified.
- Consequences: Keep provider-specific logic outside payroll domain code. Model idempotency, payment states, reconciliation, and audit explicitly.
- Review trigger: Provider selection and successful sandbox proof of concept.
""",
}

ROOT_README = """# PayrollNG — System Architecture

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
"""

def title(slug):
    return " ".join(word.capitalize() for word in slug.replace("_", "-").split("-"))

def write_missing(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(content.rstrip() + "\n", encoding="utf-8")
        return 1
    return 0

def main():
    created = 0

    for folder, raw_docs in SECTIONS.items():
        docs = raw_docs.split()
        folder_title = title(folder)
        links = "\n".join(
            f"- [{title(doc)}](./{doc}.md)" for doc in docs
        )

        readme = f"""# {folder_title}

## Purpose
Architecture, requirements, boundaries, data, security, testing, and operational notes for this PayrollNG area.

## Design principles
- Enforce tenant isolation and server-side authorization.
- Keep business rules independent of UI and infrastructure.
- Audit important changes and protect sensitive information.
- Record assumptions and open questions.
- Distinguish proposed, implemented, and tested capabilities.

## Documents
{links}

## Status
Proposed documentation baseline. It does not imply implementation or legal verification.
"""
        created += write_missing(ROOT / folder / "README.md", readme)

        for doc in docs:
            body = f"""# {title(doc)}

## 1. Purpose
Define the proposed requirements and architecture for {title(doc)} in the PayrollNG {folder_title} area.

## 2. Scope and requirements
- Define actors, business outcomes, preconditions, validation rules, and state transitions.
- Define module ownership, interfaces, data, authorization, and tenant scope.
- Document success, failure, retry, duplicate-request, and recovery behavior.
- Identify audit evidence, retention, and reporting requirements.
- Separate planned capabilities from implemented and tested behavior.

## 3. Proposed design
Describe use cases, domain rules, persistence, interfaces, background work, and external dependencies. Keep hardware, banking, tax-authority, email, and other providers behind adapters. Do not assume an API or device has been selected until verified.

## 4. Security and privacy
Apply least privilege and server-side authorization. Validate record ownership. Avoid logging credentials, tokens, full bank details, or raw biometric data. Define retention and deletion requirements. Audit privileged changes.

## 5. Failure handling
Document validation errors, permission failures, timeouts, unavailable dependencies, retries, duplicate events, and recovery procedures. Use idempotency when repetition could create duplicate business effects.

## 6. Testing and acceptance
Cover unit and integration tests, authorization, tenant isolation, boundary cases, failures, retries, and duplicate events. Use provider sandbox or hardware-in-the-loop testing where relevant.

## 7. Open questions
Record product-owner decisions and requirements needing authoritative tax, legal, provider, or hardware verification.

## 8. Implementation status
**Status: Documentation baseline / proposed design.** Update after design approval and again when implementation and tests are verified.
"""
            created += write_missing(ROOT / folder / f"{doc}.md", body)

    # Replace generic starters with detailed documents for critical areas.
    for relative, body in SPECIAL.items():
        target = ROOT / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(body.strip() + "\n", encoding="utf-8")
        created += 1

    # Root README and index are deliberately kept synchronized with this generator.
    (ROOT / "README.md").write_text(ROOT_README.strip() + "\n", encoding="utf-8")

    index = "# PayrollNG Architecture Module Index\n\n"
    for folder in SECTIONS:
        index += f"- [{title(folder)}](./{folder}/README.md)\n"
    (ROOT / "ARCHITECTURE-INDEX.md").write_text(index, encoding="utf-8")

    write_missing(
        ROOT / ".gitignore",
        ".DS_Store\nThumbs.db\n.vscode/\n.idea/\n*.tmp\n*.bak\n*.log\n__pycache__/\n"
    )

    markdown_count = sum(
        1 for path in ROOT.rglob("*.md") if ".git" not in path.parts
    )

    print("\nPayrollNG architecture documentation generated successfully.")
    print(f"Modules: {len(SECTIONS)}")
    print(f"New files created: {created}")
    print(f"Markdown files present: {markdown_count}")
    print(f"Repository: {ROOT}")
    print("\nExisting topic files were preserved.")
    print("Root README and architecture index were refreshed.")
    print("Review proposed designs and legal/integration requirements before production.")

if __name__ == "__main__":
    main()
