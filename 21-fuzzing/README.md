# Fuzzing

Start from a valid request, mutate one dimension, preserve state, classify and
deduplicate responses, then manually validate. Run `fuzz.py`; it uses a tiny
corpus and exposes response deviations. Extend it with JSON/content-type
mutations, body normalization, saved reproducers, and a request-rate limit. The
coupon-parser case begins with valid `CAMPAIGN:DISCOUNT`, mutates one property at
a time, and marks crashes or surprising accepts for manual investigation.

## Why an attacker cares

Fuzzing is a discovery amplifier, not an impact by itself. It finds parser edges,
hidden states, crashes, and response differentials that deserve a human
hypothesis. A useful workflow converts an anomaly into a stable boundary crossing;
thousands of unexplained `500` responses are noise rather than findings.
