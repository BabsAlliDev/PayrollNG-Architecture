# Attendance Hardware Roadmap: Fingerprint First, RFID Later

## Version 1: fingerprint-first prototype
Select and test sensor/controller; build enrollment and verification; provide local event buffering and authenticated synchronization; validate events and audit device administration; document tested revisions and limitations.

## Version 2: RFID
Select reader/card technology after threat modelling; add card enrollment, assignment, revocation, and lost-card workflows; reuse device identity, event contracts, synchronization, and attendance policy; test cloning risks, replay, offline operation, and duplicate events.

Payroll and HR consume validated attendance records, not sensor-specific data. RFID remains planned until hardware and software tests demonstrate the integration.
