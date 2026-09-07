# DOM XSS

The server can return a static page. Frontend JavaScript creates the vulnerability
by moving attacker-controlled data into an executable DOM sink.

```text
URL fragment -> location.hash -> innerHTML -> active elements
```

Run `app.py`, then `solve.py`, and open both URLs. Fragments are not sent in HTTP
requests, making this example entirely client-side. The vulnerable page assigns
the fragment to `innerHTML`; the fixed page uses `textContent`.

Other sources include `location.search`, `document.referrer`, messages, and API
responses. Dangerous sinks include `innerHTML`, `outerHTML`,
`insertAdjacentHTML`, `document.write`, string timers, and `eval`.

