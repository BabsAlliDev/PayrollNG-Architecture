# Future Payment Provider Integration

Status: Future capability; no direct bank, gateway, or NIBSS integration is assumed implemented.

Before selecting a provider, verify commercial/legal eligibility, official API documentation, authentication, sandbox, supported banks, limits, fees, settlement semantics, security, and operational support.

Proposed lifecycle: prepare batch → validate → approve → submit once with idempotency key → record provider reference → process callback/polling → reconcile → retain evidence.

Treat timeouts as unknown outcomes until reconciled; do not blindly retry a transfer that may already have succeeded. Verify callback authenticity and handle duplicate/out-of-order notifications. Keep manual CSV export as fallback until automation is proven.
