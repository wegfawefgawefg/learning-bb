# SOP, CORS, postMessage, JSONP

SOP blocks many cross-origin reads, not all sends. CORS and `postMessage` relax
different boundaries, so they are separate cases. `case-01-account-api` reflects
origins while allowing credentials; its patch uses an exact allowlist and `Vary`.
`case-02-payment-widget` sends receipt data to any messaging window; its patch
checks exact origin, message shape, and reply destination.

## Why an attacker cares

The objective is reading or influencing data across a browser origin boundary.
Permissive CORS matters when credentials are accepted and the response contains
sensitive data. A `postMessage` mistake matters when a foreign window can trigger
privileged behavior or receive secrets. `Access-Control-Allow-Origin: *` on a
public unauthenticated resource is often intentional and harmless.
