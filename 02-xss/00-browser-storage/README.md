# Browser storage and session cookies

Cookies are small name/value records managed by the browser. They are not fixed-
size C structs and do not have public field offsets. Conceptually, a stored cookie
contains `name`, `value`, `domain`, `path`, expiry, `Secure`, `HttpOnly`, and
`SameSite` fields.

```http
Set-Cookie: session=random-token; Path=/; Secure; HttpOnly; SameSite=Lax
Cookie: session=random-token; theme=dark
```

`HttpOnly` prevents frontend JavaScript from reading that cookie through
`document.cookie`. The browser still sends it with matching HTTP requests. This
reduces direct token theft through XSS, but injected JavaScript may still perform
authenticated actions as the user.

`localStorage` is an origin-scoped persistent string key/value store. JavaScript
can read it, it has no automatic expiry, and it is not automatically sent with
HTTP requests. `sessionStorage` is additionally scoped to a browser tab and
normally disappears when that tab closes. Neither has an `HttpOnly` equivalent.

Often an opaque cookie points to server-side state:

```text
cookie session_id=7f9... -> Redis key 7f9... -> {user_id: 42, role: "user"}
```

Some frameworks instead store signed session data in the cookie. A signature
prevents undetected modification; it does not encrypt the contents.

Run `app.py`, visit `/`, and inspect DevTools under Application and Network. The
page can display the normal cookie and Web Storage values, but not the `HttpOnly`
cookie. The HTTP request still contains both cookies.

