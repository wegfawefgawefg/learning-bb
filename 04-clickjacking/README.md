# Clickjacking

A sensitive page permits framing, so misleading UI can overlay it. Visit
`http://127.0.0.1:5000/attack`: the lure is visible underneath an almost
transparent iframe loaded from `http://localhost:5000/vuln`. Those hostnames are
different browser origins even though they reach the same local server.

Click **Claim prize**. The click actually lands on the target origin's **Delete
project** button, and the lab observer reports the state change. The attacker
does not replace the real button; they visually align the real framed button with
their lure.

The target and attacker are now separate programs and origins. Log in to the
target and inspect the project settings normally. Then run the attacker page and
click its visible “View invoice” lure. The transparent target iframe above it
receives the click and submits the real archive action.

## Why an attacker cares

Framing is only the primitive. The attacker wants a victim who is already logged
in to perform a consequential target action while believing they are interacting
with the attacker's page. Delete, transfer, permission-grant, camera-enable, and
OAuth-consent controls are useful targets. Read-only pages, actions requiring
fresh confirmation, and pages that cannot be aligned reliably produce little or
no practical impact.

The same-origin policy stops the attacker from reading the framed response, but
does not itself prevent framing or clicks. Browser third-party-cookie policy and
fresh confirmation can limit exploitability, so test the actual authenticated
state rather than reporting headers alone. The patched target uses CSP
`frame-ancestors 'none'`; `X-Frame-Options: DENY` covers older clients.
