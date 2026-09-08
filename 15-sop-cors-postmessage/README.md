# SOP, CORS, postMessage, JSONP

SOP blocks many cross-origin reads, not all sends. Send an arbitrary `Origin` to
both routes. The vulnerable route reflects it with credentials. Audit
`postMessage` for exact `event.origin` checks and strict message schemas. JSONP
is executable cross-origin data and should be retired.

## Why an attacker cares

The objective is reading or influencing data across a browser origin boundary.
Permissive CORS matters when credentials are accepted and the response contains
sensitive data. A `postMessage` mistake matters when a foreign window can trigger
privileged behavior or receive secrets. `Access-Control-Allow-Origin: *` on a
public unauthenticated resource is often intentional and harmless.
