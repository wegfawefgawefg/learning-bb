# Insecure deserialization

Native object formats may invoke attacker-selected gadget behavior while being
decoded. `solve.py` makes pickle create `pwned.txt`. Prefer simple data with a
strict schema; never deserialize native objects from an untrusted boundary.

## Why an attacker cares

Deserialization can turn data into behavior before normal application validation
runs. A usable gadget chain may execute code, read files, make requests, or alter
privileged object fields. Merely recognizing a serialized format is not a finding:
the attacker must control bytes that reach an unsafe decoder, bypass integrity
checks if present, and demonstrate a consequential property or gadget.
