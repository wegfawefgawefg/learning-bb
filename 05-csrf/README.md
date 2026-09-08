# CSRF

CSRF stands for **cross-site request forgery**. A page on one origin causes the
victim's browser to submit a state-changing request to another origin. Cookies
belonging to the destination are attached automatically, so the target can see an
authenticated request even though the attacker never learns the cookie.

The case models an account email change. Run the target and attacker separately:

```bash
uv run python case-01-email-change/challenge/app.py
uv run python case-01-email-change/exploit/attacker.py
```

Visit `http://127.0.0.1:5000/login`, then `http://127.0.0.1:5001`. Submit both
forms. The browser sends the target's session cookie to port 5000. The vulnerable
endpoint accepts the action; the fixed one rejects it because the attacker lacks
the CSRF token and its `Origin` is port 5001.

An origin is **scheme + hostname + port**, so ports 5000 and 5001 are different
origins. A “site” is a related but broader cookie concept and normally ignores
the port. That is why a `SameSite=Lax` cookie can still be sent in this particular
cross-origin, same-site lab.

The same-origin policy normally stops the attacker page from reading the target
response, but ordinary HTML forms can still send requests. Defend with framework
CSRF middleware, suitable `SameSite` cookies, origin validation, and no
state-changing GET endpoints.

The patched application is a separate process. It verifies a synchronizer token
stored in the server session and validates `Origin`; it does not expose a second
“fixed” route that would never exist in a real product.


## Why an attacker cares

The attacker wants the victim's browser to lend its authenticated authority to a
chosen action without revealing the session secret. Useful outcomes include
changing recovery details, adding an integration, creating a key, or initiating a
transaction. A request that only reads data the attacker cannot observe, changes
no durable state, or is blocked by `SameSite`, tokens, or re-authentication may
have no useful consequence.
