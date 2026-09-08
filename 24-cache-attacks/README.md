# Cache poisoning and deception

A cache key must contain every input that changes the response. Inventory unkeyed
headers, host/proto overrides, path normalization, query handling, `Vary`, and
authenticated content. Write the key as a function, compare its inputs with all
response-varying inputs, then test with a unique harmless marker and record
`Age`/cache-status headers. Avoid caching personalized responses by default.

## Why an attacker cares

A shared cache can deliver one attacker-influenced response to many unrelated
visitors or store private content under a public key. The attacker looks for an
input that changes the response but not the cache key. A reflected header on an
uncached response is not poisoning; persistence and delivery to a clean client
are the meaningful evidence.
