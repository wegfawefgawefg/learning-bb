# Information disclosure and traversal

Leaks appear in errors, debug routes, maps, backups, repositories, logs, headers,
bundles, metadata, and path handling. Prefer opaque file IDs; otherwise resolve
and constrain paths. Disable debug output and keep
secrets out of artifacts and logs.

## Why an attacker cares

Disclosure supplies data or primitives needed for a larger goal: credentials,
reset tokens, personal records, source code, internal hostnames, object IDs, or
framework details that make another exploit reliable. A version banner alone is
usually low value; a planted secret outside the intended document root proves a
real confidentiality boundary crossing.

## Case: account export download

The exploit downloads Alice's expected CSV, then changes only the filename to
escape the export directory and read a planted environment backup. The patch maps
an opaque export ID to a server-owned path.
