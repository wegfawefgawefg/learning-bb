# SSO, OAuth/OIDC, SAML

Identity flows depend on exact redirect binding, one-time state, PKCE, OIDC nonce,
issuer/audience, signatures, time, and safe account linking. Shared cookies and
abandoned subdomains widen trust. `/vuln/callback` ignores state; `/fixed` consumes
a value created by `/start`.

## Why an attacker cares

Identity flows move login authority between systems. The attacker wants to bind
their authorization response to the victim's session, steal a code or token, link
the wrong identity, or make one relying party trust an assertion intended for
another. Missing `state` matters when it enables login CSRF or account linking;
an arbitrary callback error alone does not.
