# Security code review

Trace untrusted sources to sensitive sinks, then work backward from sinks. Mark
trust boundaries, middleware, object authorization, queries, rendering, outbound
HTTP, files, parsers, process execution, crypto, secrets, logging, and errors.

Review lessons `02-17` without running them. For each write: source,
transformations, sink, missing invariant, reachability, exploit hypothesis,
root-cause patch, and regression test. Then compare with its fixed route.

