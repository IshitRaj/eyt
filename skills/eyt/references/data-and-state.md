# Data, state and recovery are part of product correctness

## Classify every state holder

- **Authoritative records:** server/database or deliberately local-first store. Define ownership, versions and persistence guarantees.
- **Client query cache:** disposable views of server data; account-scoped and invalidated correctly.
- **Drafts:** unsaved user intent; keep separate from confirmed records and protect from failed requests.
- **Pending operation locks:** prevent duplicate/opposite actions while preserving unrelated interaction.
- **Presentation preferences:** theme, view density and similar settings, which may live locally.
- **Offline outbox:** explicitly unsynced intents with bounded retention, identity attribution and clear sync status.
- **History/activity:** events at the time they happened; not automatically equivalent to the current record's fields.

Do not conflate these sources. A localStorage entry or React state change does not establish server persistence. An empty API response after an outage is not proof that a user's workspace is empty.

## Mutation lifecycle

For a meaningful write, identify: intent → validation → authorization → stable idempotency key (if necessary) → expected version → transactional mutation → confirmed response → client state update → recovery behavior.

- **Known failure:** keep prior confirmed state and user draft, explain next action.
- **Unknown outcome:** if the server might have committed, retry/reconcile using the **same operation identity** rather than issuing another create.
- **Concurrent update:** compare revisions; offer a safe way to review/reapply the user's draft. Avoid silent last-write-wins unless explicitly approved.
- **Delete/Undo:** server-backed receipts or other well-defined restoration policy; don't restore stale snapshots over intervening changes.
- **Account switch:** late requests cannot mutate the newly active account's cache, navigation, downloads, draft or cookie/session context.

An idempotency key is not a universal solution: it requires scope, request matching, retention, and concurrent admission rules. Keep mechanisms proportionate; simple local settings may not need a server receipt system.

## Relations and counts

Use immutable record IDs for identity; mutable names can be labels and routing decoration. Validate every referenced parent/space/group within the authenticated scope. Make multi-record transitions atomic when a failure would violate invariants. Count changes and record writes must agree under concurrency. Import, restoration and duplicate detection must not charge twice; define whether a deletion refunds a limit before implementing the counter.

Keep timestamps as instants with clear timezone conversion; calendar dates are not timestamps. Decide whether a metric means current state, first-ever completion or repeat events. Store history accordingly and do not fabricate it from current values.

## Data migration, import and export

- Migrations should be explicit, bounded, testable and reversible where possible; never silently merge demo seed records into a real account.
- Imports should be user-selected, previewable, scoped, bounded and idempotent. Preserve relationship mapping and user choice; don't truncate records based on a UI preview size.
- Export should represent the promised scope, stream/batch for large data, fail visibly on interruptions, and exclude credentials.
- If export limits exceed one import request, plan a bounded staged/batch import path before claiming round-trip support.
- Deleted records, soft-delete retention, Undo reservations and backups need documented lifecycle rules; account erasure must be evaluated across all retained copies and logs.

## Extension/sync specifics (only if applicable)

A browser extension is a distinct, potentially untrusted client. Use explicit account pairing/authorization, least-privilege scopes and revocation; do not treat a popup's local profile label as proof of identity. Display limits must **not** truncate durable capture storage. Unsynced data should not be silently uploaded to another signed-in account. Credentials do not belong in capture exports. Local encryption helps with a narrow threat model, not full-device compromise.

## A practical save/retry example

A user presses Save, the server commits, but the response is lost. The UI cannot conclude either "saved" or "not saved" from a timeout alone.

**For a durable mutation where duplicate creation matters:**

1. Create a stable intent identity before the request.
2. Keep the original payload and intent identity for retry or reconciliation.
3. On the server, bind intent identity to the authenticated actor and operation; reject reuse with different payloads.
4. If the first operation committed, return or discover the previous result instead of creating a duplicate.
5. Keep the draft visible or recoverable while the outcome is unknown.

For a tiny local app this may be satisfied by a uniquely indexed record and a deterministic retry. Don't introduce a distributed event bus just to implement Save.

## State ownership boundaries

| Kind of state | Example | Correct owner or lifetime |
| --- | --- | --- |
| Authoritative record | Saved expense, budget, page, note | Durable store/database with authorized operations |
| Draft | Unsubmitted title and note | UI session/tab until success or explicit discard |
| Query cache | Retrieved expense list | Scoped to requesting account and query |
| Pending lock | Saving this expense right now | Specific intent/item, released after confirmed outcome |
| Appearance preference | Theme and density | Local preference, or server setting if requested |
| Offline outbox | Explicit unsynced capture | Bounded durable client queue, with real sync status |
| Activity event | "Finished reading" occurred at time T | Persisted event or explicitly defined derived metric |

If two kinds of state share a variable or generic global store, ask whether a failure could cause one to overwrite the other. An account switch can invalidate query results while preserving an unsent draft for the correct account. A live UI list can show only 20 items while the durable store retains all of them.
