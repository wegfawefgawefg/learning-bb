# Race conditions

The check and update are separate, so concurrent requests observe stale state.
Run `solve.py`. The fixed route locks the invariant. Real systems use database
transactions, conditional updates, constraints, or idempotency keys.

