# Clickjacking

A sensitive page permits framing, so misleading UI can overlay it. Visit
`http://127.0.0.1:5000/attack`: the lure is visible underneath an almost
transparent iframe loaded from `http://localhost:5000/vuln`. Those hostnames are
different browser origins even though they reach the same local server.

Click **Claim prize**. The click actually lands on the target origin's **Delete
project** button, and the lab observer reports the state change. The attacker
does not replace the real button; they visually align the real framed button with
their lure.

Change the iframe source to `/fixed` and restart the app. Firefox will refuse to
frame it because the fixed response uses CSP `frame-ancestors 'none'` and
`X-Frame-Options: DENY`. Re-authentication for critical actions adds another
useful boundary.

## Why an attacker cares

Framing is only the primitive. The attacker wants a victim who is already logged
in to perform a consequential target action while believing they are interacting
with the attacker's page. Delete, transfer, permission-grant, camera-enable, and
OAuth-consent controls are useful targets. Read-only pages, actions requiring
fresh confirmation, and pages that cannot be aligned reliably produce little or
no practical impact.
