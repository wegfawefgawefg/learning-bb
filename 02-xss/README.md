# Cross-site scripting

Work through these independently:

1. `00-browser-storage`: cookies, `HttpOnly`, `localStorage`, and `sessionStorage`.
2. `01-reflected`: request input is inserted into the immediate server response.
3. `02-stored`: input is persisted and later rendered to other visitors.
4. `03-dom`: browser JavaScript moves input into an executable DOM sink.

In all three XSS cases, JavaScript executes under the vulnerable application's
origin. The payload location and data flow differ.

