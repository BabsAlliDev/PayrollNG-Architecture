# Tax Engine Overview

Provide deterministic, testable tax calculations for a specific jurisdiction and tax period. Keep rules out of UI/controller code. Version rules with jurisdiction, source, approval status, effective dates, and tests. Preserve the rule version and breakdown used by finalized payroll.

Nigerian PAYE rules, thresholds, reliefs, employer obligations, and effective dates must be checked against current official legislation and tax-authority guidance before production. Have qualified tax/accounting professionals validate calculations and reporting.

Tax calculation is separate from return preparation, filing submission, tax payment, and authority acknowledgement. No rule set should be marked production-approved without source evidence, tests, reviewer, approval date, and effective date.
