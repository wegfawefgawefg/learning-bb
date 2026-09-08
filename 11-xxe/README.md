# XXE

An XML parser resolving external entities can read files or make server requests.
Run `solve.py` against both endpoints. Disable DTD loading, entity resolution,
and networking in every XML entry point, including SVG and document converters.

## Why an attacker cares

External entity resolution makes the parser fetch attacker-selected resources.
That can expose server files, reach internal HTTP services, or create an out-of-
band signal from a blind document processor. A parser accepting harmless DTD
syntax is not enough; the useful capability is resolution across a file or network
boundary. Resource-exhaustion payloads are a separate availability risk.
