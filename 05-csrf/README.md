# CSRF

Browsers attach ambient cookies to attacker-chosen requests. Visit `/login`, then
`/attack`. The fixed endpoint requires a session-bound token. Use framework CSRF
middleware, `SameSite`, origin checks, and no state-changing GETs.

