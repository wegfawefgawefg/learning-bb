# JWTs and sessions

A JWT signature supplies integrity, not confidentiality or authorization. Verify
the expected algorithm/key, issuer, audience, times, token type, and subject.
Study refresh rotation/replay, revocation, fixation, logout, cookie flags, session
regeneration, and idle/absolute expiry.

Exercise: build negative tests for wrong issuer, audience, algorithm, key ID,
token type, expiry, future issue time, reused refresh token, and post-logout use.
Decoding a token is not signature verification.

