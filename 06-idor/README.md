# IDOR / BOLA

IDOR means insecure direct object reference; API literature often calls the same
failure broken object-level authorization (BOLA). The identifier is not the bug.
The bug is accepting an attacker-controlled reference without checking whether
the authenticated actor may perform this action on that object.

## Case: support tickets

The challenge is a small support API with two authenticated customers. Alice can
list and read her own tickets. Bob owns a private billing ticket. The list route
is correctly scoped, which gives you one legitimate Alice ticket ID and does not
simply advertise Bob's ID.

Start `case-01-support-tickets/challenge/app.py`. Use the product as Alice, map the
ticket endpoints, then determine whether changing only an object reference crosses
the account boundary. The exploit performs the full two-account method: establish
Alice's baseline, use Bob to create/observe the control object, then retry Bob's
identifier while preserving Alice's session.

## Mental model

Authentication answers “who is calling?” Object authorization answers “may this
caller read, edit, delete, export, or share this particular object?” Checks must
cover every action and nested resource. Hiding IDs, using UUIDs, or filtering the
list endpoint does not authorize the detail endpoint.

## Why an attacker cares

The attacker objective is protected data or actions belonging to another account.
The primitive is control over a ticket ID. The gained capability is reading any
ticket whose ID becomes known. In a real support system that might expose reset
links, addresses, invoices, internal staff replies, or attachments. An attacker
may learn IDs from their own sequential objects, URLs shared with them, browser
history, notifications, API responses, or another disclosure.

If every referenced object is public, contains no additional data, or is already
shared with the caller, changing the ID has no security impact. The cross-account
response is what converts identifier control into a finding.

## Hunting and variants

Test horizontal access between peer accounts and vertical access between roles.
Look in URLs, JSON bodies, GraphQL variables, filenames, export jobs, websocket
messages, and indirect references such as team or tenant IDs. Compare read, edit,
delete, attachment, history, and bulk routes independently.

False positives include public objects, deliberately shared objects, and a `404`
whose timing or body reveals nothing useful. Prove impact with objects belonging
to your two controlled accounts.

## Remediation

Scope the database query through the authenticated principal or a centralized
policy decision. The patched implementation queries by both ticket ID and owner,
and returns the same not-found response for missing and unauthorized objects.
