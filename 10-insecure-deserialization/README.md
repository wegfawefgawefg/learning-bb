# Insecure deserialization

Native object formats may invoke attacker-selected gadget behavior while being
decoded. `solve.py` makes pickle create `pwned.txt`. Prefer simple data with a
strict schema; never deserialize native objects from an untrusted boundary.

