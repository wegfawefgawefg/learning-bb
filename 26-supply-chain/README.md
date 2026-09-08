# Dependencies and supply-chain trust

Inventory direct/transitive packages, lockfiles, registries, install scripts, CI
permissions, provenance, artifacts, update bots, and secret access. A version
match is only a lead: confirm the vulnerable feature is reachable.

Generate an SBOM for one project. For three advisories trace dependency path,
affected range, vulnerable symbol, runtime reachability, fix, and regression risk.
Threat-model dependency confusion, publisher takeover, malicious install hooks,
cache poisoning, and compromised CI actions.

## Why an attacker cares

Build systems hold publishing tokens, cloud credentials, signing keys, and the
ability to modify downstream artifacts. The objective is to turn trust in a
package name, registry, maintainer, or workflow into execution during install,
build, or deployment.

For advisory review, record dependency path, resolved version, affected feature,
runtime reachability, process privilege, mitigation, fixed version, and regression
risk. Separately threat-model dependency-confusion registry selection and CI event
triggers, fork behavior, action pinning, artifact trust, environment approvals,
token permissions, secret lifetime, and build-network access.
