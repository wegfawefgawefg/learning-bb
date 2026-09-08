# IDOR / BOLA

Authentication identifies a caller; object authorization decides access to this
record. Both routes require a valid Alice or Bob session. Run `solve.py` as Alice:
note 1 is hers, but changing only the URL ID from `1` to `2` returns Bob's note on
the vulnerable route. The fixed route authenticates the same Alice session and
then verifies that the requested note belongs to Alice.

This is the classic IDOR/BOLA workflow: create or observe objects under accounts
A and B, capture A's legitimate request, replace its object identifier with B's,
and check whether the server enforces object ownership. UUIDs make identifiers
harder to guess but do not replace authorization.
