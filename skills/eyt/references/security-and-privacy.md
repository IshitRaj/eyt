# Security and privacy: trust boundaries before checklists

Security depends on the application and its threats. Use [OWASP ASVS](https://asvs.owasp.org/) and the [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) for deeper, maintained control guidance. This skill is **not a security certification** or substitute for a qualified review.

## Threat-model the actual flow

Identify untrusted actors, valuable data, endpoints, provider credentials, allowed operations, and the point each user-controlled value crosses a trust boundary. For each boundary ask: who is authenticated, what exactly can they act on, how is ownership verified, what does failure reveal, and how is abuse bounded?

## Common failure modes

**Authentication is not authorization.** Authentication establishes identity. Authorization enforces access to **this record/action** and related objects. Every detail read, list, count, search, export, restore, relationship update and background worker must apply scope. For unauthorized private IDs, avoid leaking existence where the product requires non-disclosure. Verify cross-account tests for IDs, cursors, cached responses, device grants and privileged operations.

**TypeScript is not runtime input validation.** Validate body, query, headers, files, cursor signatures, IDs, page sizes, field lengths and relationships at untrusted boundaries. Parameterize database operations where applicable; constrain updates to allowed fields. Authorization must not depend on client-controlled `ownerId`, plan tier, role, or subscription status.

**Sessions, CSRF and tokens.** Follow the chosen auth framework's current documented flow. Use secure cookie attributes, verify origins/CSRF where appropriate, set session expiry, prevent account-switch leakage, and avoid putting bearer/refresh tokens in URLs, logs, or untrusted browser storage. Extension/public clients should request narrow capabilities and support revocation, expiry and refresh rotation when needed.

**External URLs, SSRF and redirects.** If the server fetches user-provided URLs, this creates a security boundary: constrain schemes and ports; reject private, loopback, link-local and metadata destinations; resolve and pin endpoints safely; re-check every redirect/DNS change; bound bytes, redirects and total execution time. Use [OWASP's SSRF prevention guidance](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html). Hostname regexes or a single preflight DNS check are insufficient defenses.

**Retries and concurrency.** A request can commit and lose its response. Stable idempotency IDs, server-side uniqueness, expected versions, and transactions protect against duplicate records, quota races, and silent overwrites. Keys must be scoped to identity and the exact intended request. A retry with a new key may create an unintended second item.

**Sensitive output.** Avoid reflecting raw driver errors, stack traces, tokens, secrets, PII, unauthorized records, untrusted HTML or third-party responses. Audit logs, metrics, crash reporters, preview deployment metadata and CLI output. Operational logs should be necessary, redacted, access-controlled and retained by policy.

**Dependencies and deployment.** Prefer maintained dependencies, review supply-chain risk when adding packages, scan changed dependency trees, never commit environment secrets, and inspect production bundles/configuration. Separate dev/test/preview/prod credentials and data. Do not run destructive verification against production. Prepare backups and rollback for critical data or risky schema changes.

## Privacy by design

Ask *whether* data collection is needed before choosing an analytics SDK. Distinguish:

- **Product data:** needed to provide an explicitly requested feature.
- **Security/operational diagnostics:** narrowly required for reliability or abuse detection.
- **Behavioral analytics/advertising:** optional tracking, not implied by a request to build a website.

For each collected category define purpose, minimization, retention, access, sharing and user-facing disclosure. Avoid third-party analytics and behavioral event capture by default unless the user approves an actual need. Do not make up privacy policy text or assume tracking is legally permitted. Legal compliance varies by jurisdiction; seek qualified review where required.

## Review evidence

At minimum for an authenticated project, test both allowed and denied paths. Think in pairs: own record / foreign record; valid session / expired session; free / forged paid status; legitimate URL / internal redirect; first commit / duplicate retry; active device / revoked device. Record exactly which scenarios ran; code review alone is not proof that runtime controls work.
