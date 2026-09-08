# API hacking

Study BOLA, function authorization, mass assignment, excessive fields, quantity
limits, version drift, content types, GraphQL fields/batching, WebSocket message
authorization, and webhook signatures/replay. Add `role` to the JSON update. The
authoritative endpoint allowlists mutable fields. Build an actor/action/object
and field matrix.

## Why an attacker cares

APIs are often the authoritative layer behind a restricted UI. The attacker asks
whether omitted fields, hidden operations, alternate versions, bulk calls, or
direct object references let an ordinary account obtain another actor's data or
privileges. Extra JSON fields matter only if the backend persists or acts on a
security-sensitive one.

## Case: profile mass assignment

Fetch the profile, make a legitimate display-name update, add the normally
immutable `role`, then call an admin-only audit endpoint. The final authorization
change, not merely an echoed `admin` string, is the impact. The patch allowlists
mutable model fields.
