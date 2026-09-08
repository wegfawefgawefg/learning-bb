# SQL injection

SQL injection occurs when attacker-controlled data changes SQL grammar rather
than remaining a value. The useful question is not “does a quote produce an
error?” but “can controlled input change the result of a database decision?”

## Case: store catalogue

The challenge exposes a normal product search backed by SQLite. The application
does not reveal its query or database errors. Begin with searches that should
return zero, one, and several products. Form a boolean hypothesis, preserve the
rest of the request, and make a false search return rows. The provided exploit
does this differential before demonstrating a union result containing planted
internal data.

## Data flow and variants

`q` travels from the query string into a dynamically assembled `LIKE` predicate.
The database parser cannot distinguish developer SQL from user data after they
are concatenated. Error-based, boolean-based, union-based, stacked, and time-based
techniques are different observation channels for this same boundary failure.
Injection also occurs in numeric IDs, JSON, headers, sorting fields, ORM escape
hatches, and second-order data that is stored safely but concatenated later.

## False positives and impact

A `500`, delay, or blocked quote alone is not proof. Compare matched controls and
repeat timing observations. Impact depends on the database account and reachable
statements: reading other tables, bypassing a decision, modifying data, or in rare
configurations reaching filesystem or execution features.

## Why an attacker cares

The objective is normally to cross the data or authentication boundary enforced
by the database. The primitive is changing SQL structure through `q`. A true
predicate proves control, but the useful capability is selecting data the product
never intended this feature to return. In this case, a public catalogue search is
turned into a reader for an internal staff table. Other realistic chains include
bypassing a login predicate, recovering password-reset records, changing account
state when multiple statements are enabled, or using database-specific privileged
features. The last two require configurations this SQLite case does not claim.

## Remediation

The patched application uses bound parameters. Parameters protect values, not
dynamic table or column names; those require mapping user choices to a small
developer-owned allowlist. Add least database privilege and generic client errors.
