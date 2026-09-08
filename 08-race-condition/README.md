# Race conditions

The check and update are separate, so concurrent requests observe stale state.
Run `solve.py`. The fixed route locks the invariant. Real systems use database
transactions, conditional updates, constraints, or idempotency keys.

## Why an attacker cares

Concurrency matters when several individually valid operations violate a global
invariant: redeem once, withdraw at most the balance, sell no more than inventory,
or consume one reset token. The attacker gains extra value or bypasses a state
transition by making checks observe the same stale state. Parallel `200` responses
without an incorrect final balance or state are not sufficient impact.

## Case: one-use promotional credit

Inspect `/api/account`, redeem once normally, restart, then run the exploit. It
sends synchronized requests and checks the durable balance. The patched app makes
check-and-update one critical section; production code should use a transaction,
conditional update, uniqueness constraint, or idempotency key.
