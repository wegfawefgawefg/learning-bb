# SSRF

A fetcher lets the caller choose where the server connects. Fetch `/internal`
through `/vuln`. Prefer source IDs rather than URLs; also use egress policy,
scheme/port restrictions, DNS and redirect validation, and response limits.

## Why an attacker cares

The application server often reaches hosts the attacker cannot: cloud metadata,
admin panels, databases, service discovery, or firewall-restricted APIs. The URL
parameter becomes a proxy from a privileged network position. A fetch of public
content is usually low value; the finding becomes meaningful when it crosses a
network or credential boundary, exposes a response, or triggers an internal
state-changing request.

## Case: invoice logo import

The exploit first imports an expected logo, then substitutes an internal
diagnostics URL. Protected service data returned through the public importer is
the consequence. The patch replaces arbitrary URLs with server-owned logo IDs;
real deployments also need egress policy and redirect/DNS revalidation.
