# File uploads and archives

Uploads cross filename, path, declared MIME, actual content, browser rendering,
archive extraction, and asynchronous parser boundaries. Exercise a local handler
with mismatched MIME/magic bytes, double extensions, SVG, `../` archive entries,
duplicates, and oversized dimensions.

Generate storage names, store outside the web root, validate content and size,
re-encode media, serve from a non-cookie origin with safe disposition,
canonicalize archive entries, and isolate processors.

## Why an attacker cares

An uploaded file may execute in another visitor's origin, overwrite a server
path, exploit a parser, consume worker resources, or become publicly hosted
attacker content on a trusted domain. Upload success alone is expected behavior;
the finding is a boundary crossed during storage, processing, or delivery.
