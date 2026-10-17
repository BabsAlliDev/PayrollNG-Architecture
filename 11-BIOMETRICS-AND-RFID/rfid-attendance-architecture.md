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
