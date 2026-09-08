# Server-side template injection

Input becomes template source rather than a value. Prove expression evaluation
on `/vuln`; compare `/fixed`. Template source should remain a developer-owned
constant. Sandboxing is only an engine-specific secondary defense.

## Why an attacker cares

Template expressions run on the server rather than in the visitor's browser.
Arithmetic proves interpretation, but the desired capability is reaching secrets,
application objects, files, outbound requests, or ultimately server-side code
execution. The engine, sandbox, exposed context, and process privileges determine
whether `49` can become real impact.
