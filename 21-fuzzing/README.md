# Fuzzing

Start from a valid request, mutate one dimension, preserve state, classify and
deduplicate responses, then manually validate. Run `fuzz.py`; it uses a tiny
corpus and exposes response deviations. Extend it with JSON/content-type
mutations, body normalization, saved reproducers, and a request-rate limit.

