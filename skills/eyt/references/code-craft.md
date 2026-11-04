# Code craft: lowering cognitive load in generated software

This is the most concrete part of EYT. Agents know how to make code compile; they still need to **optimize how humans read it**. Good readability is not simply formatting, short files, naming a folder `services`, or running Prettier.

## A working definition

A new maintainer should answer without a tour of the entire codebase:

1. Where does this behavior start, and where is it implemented?
2. Which values are untrusted, validated, authenticated or derived?
3. What does this operation change, and what must always remain true?
4. Which errors are expected, and what happens when one occurs?
5. What other modules must change when this behavior changes?

Optimize to reduce the number of unrelated concepts that must be held in memory simultaneously. Favor meaning over compressed syntax.

## 1. Turn compressed logic into named decisions

Less legible:

```ts
const rows = (await db.find({ owner: user.id, q: q?.trim() || undefined, limit: Math.min(100, +(limit || 24)) })).filter(x => !x.deletedAt).map(x => ({ ...x, label: x.title || x.url }));
```

Problems: coercion and invalid limit behavior are hidden; filter might occur after an unscoped/under-bounded read; DB-specific work, policy and presentation mapping are fused.

More auditable shape (illustrative, not a drop-in implementation):

```ts
const searchText = query.search?.trim() || undefined;
const pageSize = parsePageSize(query.limit); // Validates and caps at the boundary.

const records = await listOwnedPages({
  workspaceId: context.workspaceId,
  searchText,
  pageSize,
  excludeDeleted: true,
});

return records.map(toPageListItem);
```

Here the reader can see the identity scope and the named query. **The repository function must actually enforce ownership and bounded filtering**, not merely be named `listOwnedPages`.

## 2. Give branching a shape

Harder to scan:

```ts
const status = pending ? 'loading' : error ? 'error' : rows.length ? 'ready' : 'empty';
```

A small, obvious ternary is fine. But if branches carry different side effects or data sources, a named branch is easier to audit:

```ts
if (pending) return renderLoading();
if (error) return renderError(error);
if (rows.length === 0) return renderEmpty();
return renderRows(rows);
```

Preserve each actual state; never map failed fetch to `[]` and then render "Nothing saved yet."

## 3. Split responsibilities, not line counts

A bad structure can be one 900-line React component with auth/session state, item creation, fetching, search, rendering, notifications and retries. But splitting every function into its own file is another bad structure.

A small expense-tracking feature might have:

```text
features/expenses/
  ExpenseForm.tsx       UI and client-side form feedback
  ExpenseList.tsx       Presentation of loaded items
  expense-contract.ts   Shared input and domain types (if needed)
  expense-service.ts    Authenticated create/edit/summary operations
  expense-store.ts      SQL statements and transaction details
app/api/expenses/route.ts  HTTP glue
```

These names are examples, **not mandatory files**. For a tiny local app, the service and storage may be one cohesive module. A form component may handle simple pending state without a dedicated hook. Keep structure aligned with real change boundaries.

### Placement decision

- **Transport parse / headers / status codes?** HTTP boundary.
- **Who is allowed / what the action means?** Auth context + feature operation.
- **SQL / network / transaction?** Storage adapter/service.
- **Form and visible error?** UI, through a narrow feature API.
- **Used by several real features and stable?** Shared module.
- **Only one line called once?** Usually leave it inline.

## 4. Make state relationships understandable

Do not create independent booleans such as `isLoading`, `isError`, `isSaved`, `isEmpty` when invalid combinations are easy to produce. Consider a discriminated state if the transitions are truly mutually exclusive:

```ts
type LoadState<T> =
  | { kind: 'loading' }
  | { kind: 'ready'; value: T }
  | { kind: 'error'; message: string };
```

But don't force a reducer or state machine for a button with one pending bit. Separate durable records, transient drafts, pending locks, view preferences and query caches. A tab-local draft is not the source of truth for server data.

## 5. Write the simplest correct operation

Before implementing one create/update path, establish:

- **Input:** parse and validate exactly once at the relevant trust boundary.
- **Context:** authenticated actor and tenant/workspace if applicable.
- **Invariant:** owner, relationship, quota, version or date rule.
- **Effect:** one transaction or well-defined sequence.
- **Response:** a typed result or explicit expected error.
- **Recovery:** repeat request, failed response and changed account.

Keep those concepts visibly separated, but not necessarily in six different files.

## 6. Avoid comments that duplicate code

Weak:

```ts
// Set isSaving to true.
setIsSaving(true);
```

Useful:

```ts
// Keep the original key across a lost response; creating a new key could
// duplicate a write that the server already committed.
const retryKey = pendingIntent.key;
```

Explain **why a non-obvious invariant exists**, not what a line syntactically does.

## 7. A five-minute clarity review

After a substantial function or feature, re-read as a maintainer:

- Circle the primary decision in each function. If you find unrelated decisions, consider extraction.
- Replace vague variables, mixed abbreviations, accidental terminology and magic numbers with domain-specific names.
- Break long expressions that hide validation, fallback or authorization.
- Look for nested branches that could become early exits or named policies.
- Check one-hop discoverability: can the caller be located and the effect traced without searching many generic helpers?
- Look for duplication of real business rules. Consolidate once, rather than abstracting unrelated syntax.
- Verify that extracted helpers have tests/formatting coverage; a new folder omitted from checks is not an improvement.
- Compare behavior before/after a refactor. Clean-looking code with changed validation semantics is a regression.

## 8. Simple comparison exercise for reviewers

Ask independent readers to find the edit point for a new category, a new validation rule and a failed save. Record **which files they needed and what they misunderstood**, not just a 0-to-5 attractiveness score. A formatter pass, line count, cyclomatic metric, file count or number of abstractions can help locate issues but cannot alone establish readability.

## Common wrong responses to this guide

- Splitting every 80-line module into multiple files.
- Introducing dependency injection for one concrete database.
- Declaring a dozen generic interfaces before the first working feature.
- Replacing a cohesive server action with a custom HTTP framework without need.
- Turning every conditional into a named helper, worsening navigation.
- Treating clean TypeScript compile output as proof that a request works in a real browser.

**The target is local reasoning:** when a requirement changes, the developer sees the relevant path and can change it without accidentally modifying unrelated behavior.
