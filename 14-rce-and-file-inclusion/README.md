# RCE, command injection, file inclusion

Shells, `eval`, templates, imports, and includes are distinct boundaries. This
topic now has two cases. `case-01-diagnostics` uses a harmless second `printf` to
prove shell separator injection, then replaces the shell string with an argument
array and validation. `case-02-document-viewer` escapes a template directory;
its patch maps opaque document IDs to server-owned paths.

## Why an attacker cares

Server-side execution converts a narrow feature into the server process's
capabilities: reading application secrets, modifying data, contacting internal
services, or controlling generated output. The valuable boundary is not simply
that a metacharacter is accepted; it is that an interpreter treats attacker data
as instructions. File inclusion can become disclosure or execution depending on
the included format and runtime.

Do not collapse every result into “RCE.” Command injection gains interpreter
behavior. File inclusion may yield only disclosure, or execution when the runtime
interprets the included content.
