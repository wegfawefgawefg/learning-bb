# Clickjacking

A sensitive page permits framing, so misleading UI can overlay it. Visit
`/attack`, then point its iframe at `/fixed`. Prevent with CSP `frame-ancestors`
and `X-Frame-Options`; re-authenticate critical actions.

