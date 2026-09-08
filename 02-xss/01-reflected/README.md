# Reflected XSS

The request contains attacker-controlled input and the backend immediately places
it into returned HTML. Nothing is saved.

```text
crafted link -> victim requests target -> target reflects input -> browser parses it
```

The case is a logged-in knowledge-base search. First search normally and inspect
the response. Then open the URL produced by `exploit/solve.py`. The proof reads a
planted account field from `/api/me` and places it into the page title, showing
why execution in the application's origin matters beyond an alert.

## Why an attacker cares

The crafted link causes code to run with the target origin's browser privileges.
That code can read same-origin pages and APIs, alter the UI, and send authenticated
requests. `HttpOnly` may hide the cookie value, but it does not stop the browser
from attaching the cookie to requests made by the injected code. Reflected XSS is
less useful when no victim can be induced to open the link or the reachable origin
contains no sensitive data or actions.

The patched app keeps template source constant and passes `q` as data, allowing
Jinja to encode it for the HTML text context.

