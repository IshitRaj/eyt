# Failure patterns to intercept before they become code

This is a **diagnostic playbook**, not a claim that every AI agent behaves this way. These tendencies were drawn from one project's documented corrections and an informal, unreplicated evaluation. Apply a pattern only when the project's requirements make it relevant. Treat every example as a testable risk.

Use this order: **notice the smell -> ask why it occurred -> choose a smaller, correct default -> add a check that would fail if it regressed.** Don't merely put another warning in a planning document.

| Often-generated shortcut or smell | Why it fails | More reliable default | Evidence to seek |
| --- | --- | --- | --- |
| Pretty dashboard with fake charts, testimonials, records, counters | Claims a product state that does not exist | Authentic empty state, labeled synthetic demo only with authorization | Fresh-account view contains no fabricated activity |
| Frontend says Saved before a durable write | Looks successful while losing data | Confirm persistence before success, or explicit rollback with draft retention | Simulate write failure / lost response and retry |
| LocalStorage treated as a cloud account database | A tab looks persistent but has no identity, sync or real ownership | Label a local prototype as local, or implement real server authority | Different browser/account sees only its own records |
| Sample seeds merged into every load | Deleted user data returns, or corrupt data gets overwritten | Isolate one-time migration, optional onboarding seed, and normal reads | Delete seeded item, reload, force parse failure |
| Arbitrary `.slice(0, N)` reused for stored data and displayed list | Quietly discards old saved records | Separate retention from view/windowing | Store N+1 items; all remain recoverable |
| Single client component owns auth, fetch, CRUD, filters, notifications, errors | Hard to reason about unrelated effects and races | Extract cohesive features/hooks by responsibility, not by line count | Find one behavior and its dependencies without tracing the whole app |
| Long ternaries, coercions, mixed business and transport logic | Hidden behavior and high review burden | Named intermediate values, guard clauses, named validation and business operations | Independently trace one invalid and one valid request |
| Generic repositories, factories or 5 layers for small CRUD | Increased navigation without clearer ownership | A small modular monolith; one feature service where needed | Point to the concrete problem each layer solves |
| Similar style of card, badge and gradient on every section | Flattens hierarchy; looks interchangeable with unrelated apps | Layout and component types follow actual content/action | Remove decoration; does the first action still stand out? |
| Obvious primary action buried after required folders/status/tags | User must decide taxonomy before completing core job | One direct path; defer optional metadata | First-time user completes task without understanding organization system |
| Every route has a generic blank screen/spinner | Slow, empty and broken all look the same | Context-specific skeleton, empty, loading and error states | Simulate slow, empty and failed fetch separately |
| Every click triggers a full-screen spinner | Removes context and feels unstable | Feedback on affected control or item; block duplicate intent | Slow action retains scroll, focus and previous confirmed value |
| Auth gate redirects signed-out `/signin` to `/signin` | Entire entry point unusable despite passing API tests | Positive auth condition for protected redirects; browser navigation smoke | New browser can register and sign in, no loop |
| Sessions stored as reusable raw cookie tokens in a DB | DB read access exposes bearer credentials | For opaque tokens, hash server-side lookup tokens at rest when architecture permits; choose vetted session library | Check cookie token cannot directly be looked up in DB |
| Password checks skip work for unknown usernames | Possible timing-based account enumeration | Use established auth implementation with enumeration mitigations | Compare failure handling and rate-limit behavior |
| Auth only checks UI route visibility | Direct API calls bypass UI restrictions | Verify session and record ownership inside server operation/query | Attempt reads/mutations with another user's ID |
| Query loads all account records to filter a page | Works in a demo, slows/fails at scale | Bounded pagination and scoped server search when scale warrants | Populate beyond one page; search full retained set |
| Duplicate save after network uncertainty | Server committed but client thinks it failed | Stable mutation intent/idempotency or reconcile before retry | Drop successful response, repeat request, inspect count |
| Client refetch from previous account updates new account view | Authorization alone does not protect delayed UI effects | Cancel and fence late responses by initiating account/view identity | Change account while response is pending |
| Delete/Undo restores old snapshot over newer edits | Conflicts cause data loss | Version/relationship-aware server operation; transaction if needed | Edit related record, attempt stale Undo |
| `npm run build` passes so agent claims launch-ready | Build does not exercise actual primary journey | Test key UI route, data writes, failure, isolation and deployment environment | Written evidence matrix with unverified rows |
| Repeated browser retries after each tiny change | Costs time/credits without improving diagnosis | Inspect logs/tests/API first; batch focused user-flow checks | Browser run has a named hypothesis and observable pass/fail |

## When the user is inexperienced

Do not force them to specify technology they cannot evaluate. Ask **what outcome and constraints they need**, then choose an appropriate default and explain the main trade-off in everyday language. Never treat a vague prompt as authorization to collect personal information, send analytics, implement payments, publish the site, or invent product claims.

### Useful agent response example

> I will build the smallest version where users can save and retrieve their own entries. Because accounts are required, I'll verify ownership on the server, not just hide other entries in the UI. I'll keep the save form visible on errors so drafts are not lost. I won't add analytics or subscriptions without a requirement. I will test the complete signup-to-save journey, not only whether it builds.

This is a **decision summary**, not a request for the user to approve every routine step.

## What not to conclude

A gradient, React client component, file longer than 150 lines, localStorage, or a repository abstraction is not inherently bad. Each can be valid when its task, lifetime and trade-off justify it. Avoid turning these warning signs into a rigid house style.
