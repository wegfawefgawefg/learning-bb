# Open redirects

User input becomes a redirect target, enabling phishing and OAuth/SSRF chains.
Make `/vuln` emit an external `Location`. Prefer destination IDs or exact parsed
allowlists; substring matching is not validation.

