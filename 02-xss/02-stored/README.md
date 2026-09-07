# Stored XSS

The application saves attacker-controlled input and later renders it as active
HTML. Every viewer of a comment, profile, ticket, or admin dashboard may trigger
it without opening a special link.

Run `app.py`, then `solve.py`. Visit `/vuln` to render the saved comment and
`/fixed` to see the same bytes rendered as text. Fix at the output boundary with
encoding for the actual context; input blacklists are not reliable XSS defenses.

