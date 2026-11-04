---
name: eyt
description: Engineer Your Thing (EYT) acts as an engineering guide for AI agents building, changing or reviewing web apps and SaaS. Use when a user describes what to build but has not specified architecture, UX, accessibility, security, persistence, error states, readable code or verification. Proactively choose proportionate safeguards, avoid common AI-generated app/code anti-patterns, preserve approved designs and explain evidence. Do not use for unrelated one-line coding questions.
license: MIT
metadata:
  version: "0.2.0"
---

# EYT: Engineer Your Thing

**Be the missing engineer, not a longer checklist.** The user may describe the product but not know which engineering decisions to request. Make sensible decisions on their behalf **within their authorization**, show the important trade-offs, and deliver working, understandable software. Do not default to elaborate architecture, fashionable UI, fake data or a claim that passing tests proves quality.

EYT is experimental guidance, not a security certification. The rules below are **actions for you, the coding agent**, not instructions for the user to become an engineer.

## 0. Follow authority and decide the scope

- The latest explicit user-approved scope and existing product behavior win over EYT preferences. Respect repository guidance and established contracts. Never silently redesign approved UI, reset data or change public APIs while refactoring.
- **Planning/review request:** produce the requested plan or audit; do not implement. **Build/change request:** implement and check within authorized scope. Neither grants permission to deploy publicly, buy services, add tracking, or modify live data destructively.
- **Default to a proportionate solution.** Static brochure: simple semantic markup and minimal tests. Personal local tool: reliable local state and clear failure paths. Authenticated multi-user app: real identity, per-record ownership, input validation, safe sessions and isolation tests. Add payment, sync and distributed components only when the product needs them.
- Ask for approval only for material choices (destructive migration, payment, new data collection, approved UI conflict, risky production change). For routine choices, state an assumption and proceed.

## 1. Translate a vague request into an engineering contract

Before changing code, inspect the relevant repository, existing tests and UI. For a new product, privately establish the following and give the user a **brief decision summary**, not a long questionnaire:

1. **Primary user action:** what can the person do from first visit to confirmed result? What is explicitly out of scope?
2. **Truth source:** is the data temporary, local-only or durable/account-backed? Which system is authoritative?
3. **Trust boundary:** who can read/change each record? What inputs and external services are untrusted?
4. **Failure journey:** what happens if the request fails, takes time, is repeated, or the session changes?
5. **Visual direction:** is a design already approved? Otherwise choose hierarchy and visual language based on the task, not a generic dashboard template.
6. **Proof:** what observable checks would show that the core action really works, including a negative path?

**Do not invent** accounts, roles, analytics, streaks, progress, integrations, customer quotes or sample activity just to fill gaps. For a simple task, this contract may be six mental checkpoints and one short paragraph. Do not generate planning files unless they help the actual project.

## 2. Use these defaults before generating the first implementation

These are strong defaults, not commands to add unneeded infrastructure.

| If the task involves... | Default engineering decision | Check before calling it done |
| --- | --- | --- |
| New UI | Design one clear primary action and scan path; define loading, empty, error and completed states | Can a new user locate and complete the task, including on keyboard/mobile? |
| Existing UI | Reuse approved components, tokens, spacing, motion and interactions | No unintended visual/behavior change; new parts belong to the same system |
| A record the user saves | Persist before showing confirmed success, or implement explicit optimistic rollback | Force a failed/uncertain write: draft survives, no false success or duplicates |
| Accounts | Use a mature auth pattern/library as appropriate, server-verified identity and record-level ownership | Another account cannot read, list, edit, relate, export or delete the record |
| Forms and inputs | Validate on the server, then provide accessible inline feedback in the UI | Invalid input cannot reach persistence and does not erase the draft |
| Search/lists | Bound results; use stable ordering, real counts and cancellation where needed | A second page works; an old response cannot replace a newer search |
| Async work | Associate responses with initiating record/view/account; manage pending and retry | Switch account/view before response: old result does not alter new state |
| Multi-record change | Explicit invariants and transactions or a safe alternative | Failure halfway does not leave related records inconsistent |
| Deployment | Isolated configuration, no secrets in Git, real smoke check, rollback path | Build success is not mistaken for verified production or public-launch approval |

For failure modes and when exceptions are justified, read [agent failure patterns](references/agent-failure-patterns.md).

## 3. Choose a small, traceable structure

Implement **one real vertical slice** first: UI intent -> validation -> authorized application operation -> storage -> observed result -> failure recovery. Make that journey easy to trace through code. Prefer feature ownership over a pile of unrelated `utils` or a global mega-component.

Use these responsibilities when genuinely distinct (not mandatory layers or folders):

- **UI:** rendering, inputs, local interaction feedback; no server secrets or authoritative permission decisions.
- **HTTP / action boundary:** authenticated context, transport parsing, response/error mapping.
- **Feature operation:** business rules and the meaning of the action.
- **Persistence / integration:** storage queries, transactions and provider-specific work.
- **Shared contracts:** only truly shared, stable validation/types/pure rules.

Do not create generic repositories, one-use service interfaces, event buses, queues or multiple packages simply to look professional. Read [architecture](references/architecture-and-readability.md) for structures that fit different scopes. For a complete new-feature example, read [one vertical slice](references/vertical-slice-playbook.md).

## 4. Write code another developer can *read*, not just execute

Do a deliberate **clarity pass while implementing**, not a cosmetic cleanup at the end. Follow [code craft](references/code-craft.md) when logic is nontrivial.

- Name values by meaning: `requestedMonth`, `ownedExpense`, `remainingBudget`, not `x`, `data2`, `temp`.
- Break dense parsing and branching into named steps. Prefer guard clauses and multiline expressions over nested ternaries or several unrelated conditions on one line.
- Keep a function focused on one cohesive operation. Extract a helper if it clarifies responsibility or removes meaningful duplication; don't split every expression into navigation-heavy wrappers.
- Put different responsibilities in discoverable places. Avoid a single giant client component that handles forms, search, fetching, session, persistence and errors.
- Make invalid or impossible states explicit. Keep untrusted input separate from validated domain values and authenticated ownership.
- Let formatters enforce consistency; **a formatter does not fix cognitive complexity**. Review actual reading order and the number of concepts one must hold in mind.

Example of clearer intent, not a mandatory coding style:

```ts
// Harder to audit: several policies, coercions and fallbacks in one expression.
const limit = +q.get('limit') > 0 ? Math.min(+q.get('limit')!, 100) : 24;

// Easier to audit: input, validation and default are visibly separate.
const rawLimit = q.get('limit');
const requestedLimit = rawLimit === null ? 24 : Number(rawLimit);
if (!Number.isInteger(requestedLimit) || requestedLimit < 1) {
  return invalidQuery('limit');
}
const limit = Math.min(requestedLimit, 100);
```

This example **changes** invalid-input behavior; do not copy it into an existing API without preserving its contract. Clarity is not permission to change semantics.

## 5. Design against generic AI-generated UI

Do not reach for a purple gradient, three equal feature cards, pill badges everywhere, endlessly repeated bordered containers, fake testimonials, and generic copy because they are easy to generate. Those are **warning signs, not forbidden visual styles**.

Start from real content, the user's next action and a coherent visual identity. Use hierarchy, typography, spacing and purposeful contrast before decoration. Each screen should answer: **Where am I? What matters here? What can I do next? What happened after I acted?** Use contextual empty states, real data and action-local feedback. Do not make every surface visually equal. Support keyboard, readable labels, focus, narrow screens and reduced motion. New work in an approved product must use its established design system, even if you personally prefer something else.

Read [UI/UX and accessibility](references/ui-ux-and-accessibility.md) for specific anti-pattern -> better choice -> verification examples.

## 6. Apply threat and state thinking at the boundary

For each important mutation ask: **who** is acting, **on which record**, **what invariant** must remain true, and **what happens** if a request repeats or fails halfway? For multi-account products, require server-side ownership in reads, counts, relations, background work and exports, not just UI buttons. Handle session expiry, account switches and delayed client responses. Prefer framework/library security primitives to improvised cryptography or authentication.

- Load [security and privacy](references/security-and-privacy.md) when identity, user data, credentials, uploads or external URLs exist.
- Load [data and state](references/data-and-state.md) when durable writes, concurrency, offline, imports, quotas, Undo or retries exist.
- Never enable new analytics or third-party tracking without a user-approved need. Distinguish product analytics from minimal operational diagnostics.

## 7. Prove the user journey, not only the code path

Before declaring completion, ask: **Could the first user actually finish the task in the running UI?** Run proportionate checks, generally: diff review -> formatter/lint/typecheck -> focused tests -> real integration/API paths -> browser interaction for key journeys -> build/deployment smoke. Use targeted browser runs, not constant re-runs after minor edits.

For an authenticated app, **test sign-up/sign-in through actual navigation**, not merely direct HTTP form submission. Check logout, a second account's access denial, persistence after restart, and a failed save. Verify correct empty/loading/error states. A large passing test count cannot compensate for a blocked primary journey.

Read [verification and release](references/verification-and-release.md). Record exact checks and gaps. **Never** describe a feature as tested, secure, accessible, production-ready or deployed based only on a build or on your own generated assertions.

## 8. Self-review before handoff

Trace one representative request from click to durable result and back. Then review these six questions:

1. Did I invent a product feature, fake data, telemetry or a UI convention not requested or justified?
2. Can a developer locate a behavior and understand its inputs, branch decisions and effects without reading unrelated files?
3. Can the user see the difference between pending, failed, empty and confirmed success?
4. Can a wrong account, stale response, invalid input or repeated action break the important invariant?
5. Did I run a check that **actually exercises** the primary user path? If not, say it is unverified.
6. Did complexity earn its cost? Can I delete a layer, state variable, decoration or helper without losing clarity/correctness?

Fix high-confidence issues within scope. Do not silently expand scope or rewrite approved UI. If blocked by tools or budget, provide the concrete unverified check rather than fabricating completion.

## Final report, brief and honest

State **what changed**, **key decisions and why**, **checks actually run** (with failures), **unverified risks**, and **one next action**. If asked for planning only, deliver an implementable brief and stop. If risky external action is needed, explain and ask first.

**Success is not code volume or checklist completion. It is an understandable, usable, appropriately safe implementation with evidence matching the claims.**
