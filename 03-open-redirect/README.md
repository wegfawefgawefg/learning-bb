# Open redirects

User input becomes a redirect target, enabling phishing and OAuth/SSRF chains.
Make `/vuln` emit an external `Location`. Prefer destination IDs or exact parsed
allowlists; substring matching is not validation.

## Why an attacker cares

A redirect is usually a low-value primitive alone. Its value is laundering an
untrusted destination through a trusted-looking link, or chaining around a trust
decision. A useful chain might leak an OAuth authorization code through an
allowed callback, send a password-reset email recipient to a convincing phishing
page, or make an SSRF allowlist accept a trusted first hop that redirects inward.
If the final destination is obvious and no other system trusts the redirecting
origin, the impact may be little more than phishing assistance.
