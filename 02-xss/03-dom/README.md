# DOM XSS

The server can return a static page. Frontend JavaScript creates the vulnerability
by moving attacker-controlled data into an executable DOM sink.

```text
URL fragment -> location.hash -> innerHTML -> active elements
```

Run the challenge, use `/profile-preview#Alice` normally, then open the URL emitted
by `exploit/solve.py`. Fragments are not sent in HTTP requests, making the source
and sink entirely client-side. The vulnerable frontend assigns the decoded value
to `innerHTML`; the patched frontend uses `textContent`.

Other sources include `location.search`, `document.referrer`, messages, and API
responses. Dangerous sinks include `innerHTML`, `outerHTML`,
`insertAdjacentHTML`, `document.write`, string timers, and `eval`.

## Why an attacker cares

As with reflected XSS, the attacker wants code execution in the target origin;
the difference is where the vulnerable transformation happens. A crafted link can
turn client-side routing or preview logic into same-origin API access, UI changes,
or authenticated actions. If the value never reaches an executable sink, control
of the fragment alone is harmless.

