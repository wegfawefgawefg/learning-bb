# RCE, command injection, file inclusion

Shells, `eval`, templates, imports, and includes are interpreter boundaries. This
lab uses a toy shell: append `cat flag.txt` without exposing a real workstation
shell. Replace command strings with structured APIs and argument arrays, validate
values, drop privileges, and isolate risky processors.

## Why an attacker cares

Server-side execution converts a narrow feature into the server process's
capabilities: reading application secrets, modifying data, contacting internal
services, or controlling generated output. The valuable boundary is not simply
that a metacharacter is accepted; it is that an interpreter treats attacker data
as instructions. File inclusion can become disclosure or execution depending on
the included format and runtime.
