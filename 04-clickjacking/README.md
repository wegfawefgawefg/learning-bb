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
