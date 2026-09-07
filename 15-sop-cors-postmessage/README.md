# SOP, CORS, postMessage, JSONP

SOP blocks many cross-origin reads, not all sends. Send an arbitrary `Origin` to
both routes. The vulnerable route reflects it with credentials. Audit
`postMessage` for exact `event.origin` checks and strict message schemas. JSONP
is executable cross-origin data and should be retired.

