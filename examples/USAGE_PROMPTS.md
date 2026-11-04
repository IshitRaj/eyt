# Practical prompts for EYT

A user does not need to know the architecture to use the skill. Describing the problem and constraints is enough to get started. Use `$eyt` explicitly if the agent does not invoke it automatically.

## 1. Starting from an idea

> Use $eyt to help me build a small site where people can save recipes to return to later. I am the only user initially, don't need accounts yet, and want a quiet mobile-first interface. Tell me what must persist and what could go wrong. Then implement the smallest complete version and test it. Don't add analytics by default.

Expected behavior: the agent should not impose multi-tenant auth or a billing system; it should clarify whether the recipes live only on this device and be truthful about backups/data loss.

## 2. Building a real SaaS

> Use $eyt to build a private notes app with email sign-in and multiple accounts. Users must never see each other's notes. Plan a simple architecture, explain authorization and failure paths, implement one complete save/edit/reload flow first, and test invalid/foreign IDs before expanding.

Expected behavior: server-derived ownership, actual persisted records, validation, explicit failure UX and adversarial access tests, not merely a hidden button.

## 3. UI that doesn't look generic

> Use $eyt to design and build the UI for a project journal. The feel should be editorial and calm, not a stock dashboard. Explain your design choices, create coherent states for empty/loading/error, and make keyboard and mobile interactions usable. Don't invent user activity or statistics.

Expected behavior: a task-specific design system, not a blanket prohibition of all cards or color; inspect UX at meaningful viewports and input methods.

## 4. Preserving an approved UI

> Use $eyt to refactor this app's data flow without changing the approved design. Preserve current rendered markup, CSS, assets and interactions. New UI must fit existing tokens and patterns. Set up targeted regression checks and report which visual states were actually compared.

Expected behavior: meaningful behind-the-boundary refactor, explicit UI change approval, no claim that static markup hashes prove all behavior.

## 5. A failed save and uncertain retry

> Use $eyt to investigate why clicking Save sometimes creates duplicates after a network timeout. Preserve the draft and account boundaries. Explain what happens if the server commits but the response is lost, then add a focused test for that case.

Expected behavior: stable operation identity, server-side deduplication/reconciliation if necessary, not a fresh random request on each retry.

## 6. Launch-readiness assessment (no deployment)

> Use $eyt to audit launch readiness for this authenticated web application. Do not deploy or modify production. Inspect auth, access control, secrets, dependency risk, error states, data lifecycle, backups and monitoring. Run safe checks where possible and separate verified results from assumptions.

Expected behavior: prioritized report with evidence and honest blockers, not a blanket declaration of security.

## 7. Planning only

> Use $eyt in planning-only mode for a simple appointment-booking service. I want an engineering brief, minimum data model, UX flow, key risks, acceptance criteria and release checks. Do not write code or create infrastructure yet.

Expected behavior: no unintended side effects or code; reservations and timezones considered where applicable.
