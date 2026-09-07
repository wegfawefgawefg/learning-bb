# SSO, OAuth/OIDC, SAML

Identity flows depend on exact redirect binding, one-time state, PKCE, OIDC nonce,
issuer/audience, signatures, time, and safe account linking. Shared cookies and
abandoned subdomains widen trust. `/vuln/callback` ignores state; `/fixed` consumes
a value created by `/start`.

