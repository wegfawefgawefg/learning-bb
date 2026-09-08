# HTTP, proxying, and recon

Learn methods, paths, queries, headers, cookies, bodies, redirects, content type,
caching, origins, DNS, TLS, and sessions. Proxy a later lab through Burp or ZAP:
intercept, replay, change one value, compare. Inventory routes, authentication,
object IDs, roles, state changes, parsers, and sinks. Recon through product use,
docs, DNS/certificates, archives, JavaScript, source maps, and API schemas.

## Why an attacker cares

Useful bugs occur where components disagree about authority or meaning. Recon
finds those assumptions: undocumented APIs, old hosts, client-only role checks,
worker inputs, and identifiers shared across tenants. The output is an attack-
surface model, not the largest possible host list.

Proxy the IDOR case and save raw identity, list, and detail requests. Label method,
origin, credential, content type, object reference, and expected authorization.
Then black-box another case and produce an endpoint/actor/state/sink table before
reading source. Rank hypotheses by the capability they might create.
