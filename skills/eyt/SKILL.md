---
name: eyt
description: Guide proportionate engineering decisions when building, changing or reviewing web apps and SaaS, including UI, persistence, trust boundaries and verification.
license: MIT
metadata:
  version: "0.3.0"
---

# EYT: Engineer Your Thing

Use this experimental skill to turn a product request into observable behavior. Start with the user's task, the repository's conventions and the permissions already granted. For a plan or review, deliver the requested analysis. For a build or change, implement and verify the requested behavior. Publishing, destructive operations and new data collection each need authorization covering that action.

## Establish the change

- Trace the primary action from the user's entry point to its visible result. Identify who can perform it, where the authoritative data lives and which failure would matter most. A static page may need only a reading order, working links and a narrow-screen check.
- On an existing feature, identify what the new requirement replaces and which neighboring behavior still matters. Run a relevant existing check or capture an observable baseline before editing. Include existing records or callers when a change crosses a stored-data or API boundary.
- Respect approved designs and contracts. Resolve routine choices from project evidence. Raise a conflict when it materially changes scope, data ownership or user-visible behavior. Consult the [decision guide](references/decision-guide.md) when the right level of infrastructure is unclear.

## Implement the smallest coherent change

Follow one real path through the feature. Keep parsing, policy, storage and feedback easy to locate wherever those responsibilities already live. Reuse established components and dependencies. A new package or abstraction should solve a concrete problem worth its maintenance cost. See [architecture and readability](references/architecture-and-readability.md) for boundary changes, [code craft](references/code-craft.md) for dense logic or a [worked vertical slice](references/vertical-slice-playbook.md) for a new account-backed feature.

Read only the references implicated by the task.

| When the change touches | Decision to make and check |
| --- | --- |
| Screens or interaction | Give real content and the next action a clear reading order. Follow approved components, keyboard interactions and responsive behavior. Check the actual task with representative content and relevant pending, empty, failed or completed states. See [UI/UX and accessibility](references/ui-ux-and-accessibility.md). |
| Inputs, accounts or integrations | Validate untrusted input where authority resides. Derive ownership from verified identity and apply it to related records, lists and exports. Exercise both an allowed action and its denied counterpart with isolated data. See [security and privacy](references/security-and-privacy.md). |
| Writes or asynchronous work | Decide when success is durable. Preserve recoverable input on failure. If a write can commit before a response is lost, reconcile a retry against the original intent. Bind late responses to the initiating view and account. See [data and state](references/data-and-state.md). |
| A suspected implementation shortcut | Trace its consequence for this product and choose a check that would expose it. The [failure patterns](references/agent-failure-patterns.md) pair examples with verification probes. |

## Verify the result and retained behavior

Exercise the changed behavior through an entry point its caller actually uses. For an authentication UI change, navigate from signed out through sign-in to the private screen. For a storage change, inspect the persisted result after reload. Assert the expected result from the requirement, including a meaningful negative case where relevant.

After a revision, rerun the affected earlier checks alongside the new acceptance check. If a repair fails, inspect the first divergence from the last working state before making another edit. Change an existing expectation only when the revised requirement explains why.

Use the [verification and release guide](references/verification-and-release.md) to choose evidence proportionate to the claim. Report the behavior observed, checks run, failures and remaining gaps. A passing package check verifies packaging alone.
