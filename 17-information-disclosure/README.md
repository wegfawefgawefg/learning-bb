# Information disclosure and traversal

Leaks appear in errors, debug routes, maps, backups, repositories, logs, headers,
bundles, metadata, and path handling. `solve.py` escapes `public/`. Prefer opaque
file IDs; otherwise resolve and constrain paths. Disable debug output and keep
secrets out of artifacts and logs.

