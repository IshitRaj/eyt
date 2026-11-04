# Decide what engineering is justified

EYT does not prescribe a stack. Start from user journeys, trust boundaries, cost, and change frequency. Reuse established conventions unless evidence warrants a switch.

## Questions that change design

1. **Who uses it?** Just the author, public visitors, or separate accounts? Do accounts own private resources? Is sharing planned or merely imagined?
2. **What can be lost?** A draft typed into a temporary demo differs from paid purchases or months of stored notes.
3. **What is persisted?** Browser preference, offline outbox, authoritative record, operational log, and historical event serve different purposes.
4. **What can fail?** Network loss, retries, identity changes, quota limits, interrupted exports, slow third-party services, and errors after an otherwise successful write.
5. **What must be verified?** A brochure needs different evidence than a public multi-account service.
6. **What is already approved?** UI identity, business rules, API contracts, data shape, provider constraints, migrations, or release workflow.

## Make the invariant observable

For each critical operation, write a small invariant and a testable observation:

| Operation | Invariant | Negative test |
| --- | --- | --- |
| Create private item | Authorized user owns the persisted item | Another user cannot read it using its ID |
| Save draft | No success without confirmed persistence or recovery path | Network times out after server commit; retry does not duplicate |
| Update item | Concurrent edits cannot silently overwrite a later revision | Two clients edit the same version |
| Import | Only explicitly selected source records are admitted within quotas | Partial/oversize input cannot silently truncate or overwrite |
| Delete and Undo | Restore respects intervening changes and identity | Restore with stale or foreign receipt is rejected |
| Fetch arbitrary URL | Untrusted destinations cannot reach forbidden internal services | Redirect/DNS changes point at private address |

Not every project needs every row. Pick the rows that fit actual functionality.

## Choosing scope and structure

- **Static:** semantic HTML, responsive layout, minimal JS, no account layer.
- **Single-user local app:** clear local persistence semantics, errors, backups/exports if data matters; don't counterfeit cloud synchronization.
- **Authenticated app:** explicit session, ownership, scoped API/data access, server validation, rate/abuse limits based on exposed operations.
- **Multi-tenant SaaS:** inspect every query, aggregation, relation, background task, and export for tenant isolation. Use transactions for multi-record invariants as supported by the datastore.
- **Payments / high-stakes:** add provider verification, reconciliation, auditability, appropriate human/professional review; do not self-certify.

Use an existing framework/database when suitable. Add a separate backend, queue, cache, event bus, or repository abstraction only for a concrete failure mode or operational constraint. Record why a simpler alternative was insufficient.

## Approval boundaries

Ordinary internal extraction and tests may proceed within granted scope. Ask for explicit approval before: public deployment; data deletion/migration with material risk; payments or purchasing services; new tracking/PII collection; expanding privilege; redefining an approved UX; disclosing private artifacts; or modifying production infrastructure in ways that affect availability.

## Decision notes (if warranted)

For nontrivial choices record 3–6 lines: *context, options, chosen approach, trade-off, reversible?, verification*. Avoid an ADR file per trivial helper.
