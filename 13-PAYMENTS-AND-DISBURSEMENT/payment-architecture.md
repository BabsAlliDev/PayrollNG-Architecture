# Payments and Disbursement Architecture

## Initial scope
Generate validated downloadable CSV salary-payment files for manual bank upload.

## Future scope
Provider/bank APIs, payment initiation, status callbacks, reconciliation, and controlled disbursement, subject to provider selection and verification.

Model distinct states: payroll approved → batch prepared → instruction exported/submitted → provider processing → confirmed/failed/unknown → reconciled. A CSV export is not a bank transfer, and a submitted request is not necessarily a successful payment.

Controls: validate bank details and totals; enforce approval; use idempotency keys; persist provider references and state transitions; verify callbacks; handle duplicates/out-of-order events; reconcile outcomes; protect bank data; audit preparation, approval, submission, retries, and reconciliation.

Do not claim a bank or NIBSS API integration exists until official access and requirements are verified.
