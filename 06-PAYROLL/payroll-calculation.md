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
