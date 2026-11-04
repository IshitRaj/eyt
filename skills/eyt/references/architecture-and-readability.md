# Architecture and readability without cargo cults

Aim for **low cognitive load, explicit ownership, and changes that stay localized**. "Clean architecture" is not an instruction to create five folders per endpoint.

## Prefer boundaries that mirror responsibilities

A reasonable authenticated web app might have:

- **UI/presentation:** renders state and forwards user intents; no database credentials.
- **Client data adapter:** request/response mapping, cancellation, account-specific cache keys, retries with stable intent identity where appropriate.
- **HTTP route/controller:** parses transport input, obtains verified context, delegates, maps established response envelope.
- **Application/domain service:** validates operation and invariants, applies business rules, coordinates persistence.
- **Persistence/third-party adapter:** query construction, transactions, provider-specific details.
- **Shared contracts:** safe data types, runtime schemas and pure policy functions where actually shared.

These are responsibilities, not mandatory directories or classes. A 150-line cohesive module can be clearer than many trivial wrappers. Keep feature code discoverable; factor duplicated domain rules, not coincidentally similar syntax.

## Practical code-review questions

- Can a new contributor find where a specific behavior lives in under a few hops?
- Is authorization an explicit server boundary, or scattered in UI checks?
- Are domain invariants expressed once and tested at the operation that changes data?
- Does the route handler contain pagination/query orchestration, policy logic and transport handling all intertwined?
- Are names descriptive, and are complex branches written as clear steps instead of nested ternaries?
- Does a "generic" abstraction have more than one genuine consumer or an expected variability it solves today?
- Are client-side records, session drafts, and persistent records being conflated?
- Is the data model canonical (IDs, optional relations, dates, versioning), with legacy conversion contained at a boundary?
- Are errors explicitly classified and safe to expose, or hidden behind success/empty fallbacks?

## Example: separate responsibilities

Before (illustrative pseudo-code): an API route parses every optional parameter, manually validates the cursor, assembles database filters, handles quota decisions and returns HTTP all inside one dense handler.

After (still simple):

1. HTTP handler obtains a verified account context and passes normalized query input to a feature function.
2. Named query parser validates allowed filters, limits, cursor scope and deterministic ordering.
3. Owned read service applies access scope **before** querying, obtains bounded records/real totals and formats the domain result.
4. HTTP handler maps result or expected domain failure into the existing API response.

Do not split out helpers that merely rename a single line. Preserve accepted input normalization, error codes and cursor signatures when refactoring a live API.

## Rewrites and migrations

- Start by writing down accepted behavior and tests around it, including failure paths and ownership. Refactor **behind stable contracts** in narrow slices.
- Prefer a working vertical slice and incremental changes over a big-bang rewrite.
- For data/schema changes, distinguish code changes, migration, rollback, and existing record compatibility.
- Never drop unknown records or reset accounts to solve a parsing mismatch.
- Remove historical recovery machinery only after the replacement has meaningful regression coverage; don't remove legitimate error recovery or Undo.
- Compare measured before/after behavior. A test count or smaller bundle is not evidence of improved real-world latency.

## Performance decisions

Look for actual N+1 queries, repeated session/db lookup, unbounded list loading, redundant fetches, stale requests, unnecessary re-renders, and over-eager polling. Measure representative datasets, cold/warm requests, concurrency and errors before optimizing. Use pagination, indexes, request coalescing, bounded caching and connection reuse only when applicable; understand the serverless concurrency and cache isolation consequences.

**Never** trade authorization checks, transactions, idempotency, or data integrity for marginal speed.
