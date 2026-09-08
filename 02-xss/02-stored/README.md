# Stored XSS

The application saves attacker-controlled input and later renders it as active
HTML. Every viewer of a comment, profile, ticket, or admin dashboard may trigger
it without opening a special link.

The case is a customer feedback system. A customer submits text through
`/feedback`; a moderator later opens `/moderation`. The exploit first submits a
normal control, then stores markup that changes the moderator page and reads a
planted moderator-only field.

## Why an attacker cares

Persistence delivers execution to viewers the attacker cannot directly contact,
often support agents or administrators. The useful capability is acting inside a
more privileged viewer's origin and session. Impact depends on who views the data
and what their session can access; storage alone is not severity.

The patch renders every stored comment as a template value. Input validation can
enforce product rules, but tag blacklists are not a substitute for contextual
output encoding.

