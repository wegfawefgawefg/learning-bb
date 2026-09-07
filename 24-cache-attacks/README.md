# Cache poisoning and deception

A cache key must contain every input that changes the response. Inventory unkeyed
headers, host/proto overrides, path normalization, query handling, `Vary`, and
authenticated content. Write the key as a function, compare its inputs with all
response-varying inputs, then test with a unique harmless marker and record
`Age`/cache-status headers. Avoid caching personalized responses by default.

