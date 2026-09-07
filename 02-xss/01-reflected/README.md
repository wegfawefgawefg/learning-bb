# Reflected XSS

The request contains attacker-controlled input and the backend immediately places
it into returned HTML. Nothing is saved.

```text
crafted link -> victim requests target -> target reflects input -> browser parses it
```

Run `app.py`, then `solve.py`, and open the printed URLs. The vulnerable route
constructs template source from `q`; the fixed route keeps the template constant
and passes `q` as data, allowing Jinja to HTML-escape it. Common locations include
search terms, error messages, redirect failures, and previews.

