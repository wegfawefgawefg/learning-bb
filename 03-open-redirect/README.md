# Open redirects

An open redirect lets input select a navigation destination on a trusted origin.
Redirects are normal product behavior after login, checkout, SSO, and outbound
link warnings; the security question is whether the destination remains inside
the boundary promised by that trusted URL.

## Case: post-login continuation

The challenge is a project portal. Its login link carries a `continue` parameter
so users return to the page they originally requested. Use the portal normally,
capture the login request, then determine whether the continuation must be local.
The exploit creates a realistic trusted-domain link whose final page is a local
lookalike served by `exploit/attacker.py` on port 5001.

## Why an attacker cares

A redirect is usually a low-value primitive alone. Its value is laundering an
untrusted destination through a trusted-looking link, or chaining around a trust
decision. A useful chain might leak an OAuth authorization code through an
allowed callback, send a password-reset email recipient to a convincing phishing
page, or make an SSRF allowlist accept a trusted first hop that redirects inward.
If the final destination is obvious and no other system trusts the redirecting
origin, the impact may be little more than phishing assistance.

More valuable variants appear in OAuth callback allowlists, password-reset emails,
SSRF filters that validate only the first hop, and mobile deep links. Do not call
a `Location` header exploitable until you confirm the browser follows it and the
destination crosses the intended boundary.

## Remediation

The patched portal accepts a destination key and maps it to a server-owned path.
If arbitrary paths are required, parse and canonicalize them, reject schemes and
authorities, and account for protocol-relative URLs and parser differences.
