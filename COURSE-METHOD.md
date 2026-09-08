# How to work a case

## 1. Use the product normally

Do not begin with a payload. Identify what the feature promises, which actor is
using it, what state exists before the request, and what state should exist after.
Capture a known-good request and response in a proxy.

## 2. Draw the data flow

Mark every boundary the input crosses: browser parser, proxy, application, query
builder, database, template engine, filesystem, outbound client, identity
provider, or worker. Write the invariant each boundary assumes.

## 3. Make one controlled change

Change one parameter, identifier, encoding, role, sequence, origin, or timing
property. Keep authentication and other inputs constant. A clean differential is
stronger evidence than a large payload list.

## 4. Demonstrate meaningful impact

Prove a boundary crossing with test accounts and planted data. Record the exact
request, response, prerequisite state, and resulting state change.

Before calling something valuable, complete this chain:

```text
attacker objective -> vulnerable primitive -> capability gained -> product action -> consequence
```

For example, “an iframe accepts clicks” is only a primitive. The meaningful chain
is “a logged-in owner visits an attacker page -> the target accepts framing -> a
disguised click reaches the real delete control -> the project is deleted.” State
the user interaction, authentication, browser behavior, or product configuration
the chain requires. If no meaningful consequence follows, the primitive may be a
low-value hardening observation rather than a vulnerability.

## 5. Explain the root cause

Name the missing invariant in developer terms. For example: an object query is
not scoped to the authenticated tenant; template source contains user data; a
coupon check and mutation are separate transactions.

## 6. Patch and regress

Only after the black-box investigation, compare `patched/`. A strong fix removes
the dangerous interpretation or enforces the invariant at the authoritative
layer. Turn the proof into a negative regression test.

## Notes to produce

- Product behavior and actors
- Endpoint and parameter inventory
- Normal request and response
- Trust boundary and expected invariant
- Hypothesis and single changed variable
- Observed result and impact
- Attacker objective, capability gained, and full impact chain
- Required victim interaction and other preconditions
- What makes the result valuable or low-value
- False-positive checks
- Root cause, patch, and regression test
