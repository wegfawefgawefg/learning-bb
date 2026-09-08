# Security code review

Trace untrusted sources to sensitive sinks, then work backward from sinks. Mark
trust boundaries, middleware, object authorization, queries, rendering, outbound
HTTP, files, parsers, process execution, crypto, secrets, logging, and errors.

Review lessons `02-17` without running them. For each write: source,
transformations, sink, missing invariant, reachability, exploit hypothesis,
root-cause patch, and regression test. Then compare with its fixed route.

## Why an attacker cares

Behavior shows what happened; source reveals sibling routes, workers, alternate
content types, and authorization paths sharing the mistake. Reachability and
attacker control matter more than a dangerous function name.

Perform three passes: map actors, trust zones, stores, and middleware; trace
untrusted sources forward into sensitive sinks; then start at SQL, templates,
files, HTTP clients, parsers, and subprocesses and work backward to every caller.
For each candidate, document prerequisite, controlled value, security decision,
consequence, existing mitigation, patch, and a focused negative test.
