# XSS

Input becomes executable in an HTML, attribute, URL, or JavaScript context. Make
`/vuln?q=...` execute; compare `/fixed`. Prevent with context-aware encoding,
safe DOM sinks, careful HTML sanitization, and CSP as defense in depth.

