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
