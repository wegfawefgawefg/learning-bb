# Logic errors and access control

Logic bugs violate product invariants through valid-looking operations. Here the
server trusts client price and role. Derive both from server state. Write explicit
invariants and test negative role, state, quantity, and sequence combinations.

## Why an attacker cares

The attacker is looking for a product rule that the server assumes the normal UI
will enforce: price, quantity, order, approval, role, invitation state, or account
ownership. Altering a client value matters when the authoritative backend accepts
an impossible business state, such as buying below price or performing an admin
action. Weird input that is rejected or normalized has no impact.
