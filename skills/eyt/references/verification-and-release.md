# Evidence-based verification and responsible release

## Test ladder

Choose the smallest check that can expose a given failure, and escalate only where the claim requires it:

1. **Review and static checks:** diff, dependency/secret inspection, formatting, lint/type checks, unused code, broken imports.
2. **Focused unit tests:** pure validation, policy, formatting, deterministic ordering, edge cases.
3. **Component/lifecycle tests:** interaction state, timers, stale async callbacks, account-bound cache coordination; these do not prove browser layout or networking.
4. **Integration/API tests:** owned/foreign operations, transactions, retry identities, storage limits, migrations, stream failure, rate-limit behavior. Isolated databases only.
5. **Browser/manual testing:** keyboard, focus, layout, themes, dialogs, motion, actual authentication and cross-page flow.
6. **Deployed preview:** real runtime, headers, secrets, origins, cold/warm behavior and smoke workflows with isolated credentials/data.
7. **Production promotion:** verified candidate and rollback; owner approval for material cutover; smoke checks against actual deployment.

Batch browser checks at meaningful milestones to save agent/tool usage, but do not confuse efficiency with evidence. Screenshots or DOM hashes protect selected visual states; they cannot establish complete responsive, focus, animation or error behavior.

## Claim/evidence table

| Claim | Minimum credible evidence example | What it still does not prove |
| --- | --- | --- |
| Compiles | Recorded type/build command output | Functional behavior |
| Unit-tested | Tests with actual assertions and passing output | DB/session correctness |
| Cross-account isolation checked | Authorized and adversarial integration requests against scoped test data | All endpoints unless covered |
| UI visually preserved | Baseline comparison at selected viewports/themes and interactions | Every viewport and edge case |
| Performance improved | Repeatable representative before/after measures | SLA under real load |
| Preview working | Exact URL/build revision, runtime smoke | Production correctness |
| Release-ready | Completed applicable checks, external dependencies, rollback and sign-off | Guaranteed freedom from bugs |

Never inflate "test count" into all-feature proof. Report test cases, environment and known gaps.

## Deployment checklist (adapt, don't cargo-cult)

- Confirm source revision, dependency lockfile, build scripts and environment variable contracts.
- Check secret scanning in changed files and **relevant tracked history**; if leaked, rotate the real credential, not just delete a line.
- Keep development, integration, Preview and Production data/credentials isolated, least-privileged and correctly scoped.
- Validate session cookie/origin/redirect behavior and publicly exposed runtime metadata.
- Review migrations as a distinct, safety-critical operation; require backups/restore confidence for meaningful data.
- Verify monitoring/alerting, retention, backup schedule, recovery ownership and rollback path appropriate to user impact.
- Protect production branch and publish only after authorized promotion. Deployment success is distinct from public launch.
- For extensions, app stores, payment providers, legal documents, and third-party policies, identify **external release gates** rather than claiming the code alone finishes the product.

## Reporting template

```text
Outcome: [what changed / what was reviewed]
Evidence:
- [command or manual flow] -> [observed result] [revision/environment]
- ...
Not verified:
- [risk and why]
Release decision: [blocked / candidate for review / approved by owner]
Next: [one actionable step]
```

Do not forge logs, screenshots, passing counts, or reviewer approval. If browser or cloud access was unavailable, say so.

## The missed-browser-flow failure mode

An informal evaluation report described an implementation with many passing HTTP checks but a real browser sign-in page that redirected signed-out users to itself. This is a **reported example**, not an independently reproduced EYT benchmark. It illustrates the limit of direct HTTP tests: they may exercise handlers without following framework-specific streamed redirects or browser lifecycle behavior.

When authentication is in scope, a minimal real-interaction smoke should test:

1. Fresh browser opens signup and reaches a usable form without navigation loops.
2. A new account can complete registration and arrive at its own data.
3. Sign-out actually revokes/ends the session.
4. The same account can sign back in and retrieve persisted data.
5. Another account cannot access those records.

If no browser is available, mark these checks **not verified**. Do not replace them with raw POST requests and claim the UI journey passed.

## Minimum code-quality evidence

Formatters and `tsc` are helpful but not measures of human readability. Review at least one **real request trace**: UI input -> validation -> authorization -> business operation -> persistence -> response -> visible state. Record if any step is hard to locate, hidden behind generic abstractions or packed into a long conditional. A significant refactor should also preserve negative tests and prior accepted input behavior.

## Avoid test-count theater

Report tests by **what they exercise**. "84 passing tests" can still miss the primary user journey. "Screenshot matches" can still miss keyboard focus and failed-save behavior. "No audit warnings" can still miss an authorization bug. Prefer a small set of checks that deliberately targets the most consequential failures over a larger set of shallow successes.
