# UI/UX and accessibility: useful, not merely attractive

## Start with a journey, not a design trend

Identify: what users came to do, the shortest credible path, required information, what happens next, and what happens when something fails. Keep core actions discoverable. Let optional organization emerge later when the product allows it. Avoid inventing dashboards, engagement scores, gamification, testimonials, activity data, or fake user records to fill whitespace.

A minimal, purposeful UI is not synonymous with monochrome, cards, or a specific aesthetic. Preserve a project's approved design language and introduce new components only through existing tokens, type scale, spacing, patterns, interaction rules, responsive and dark-mode behavior. When no design exists, propose one coherent visual direction tied to the audience and task; do not assume generic glass cards, gradients, and hero illustrations are universally suitable.

## State truthfully

| State | What the interface owes the user | Avoid |
| --- | --- | --- |
| First-time empty | Explain what belongs here and one useful next action | Seeded fake data or empty charts of zeros posing as activity |
| Loading | Preserve context, reserve space when possible; label busy state | Rendering "no results" before a request completes |
| Error/unavailable | Preserve last useful confirmed data when safe; show retry/help | Pretending a failed fetch means an empty account |
| Pending write | Keep the action recognizable, avoid duplicate intent | Success toast before durable result |
| Conflict | Keep draft and explain reload/review choices | Last-write-wins data loss without warning |
| Offline | Explain what is local and what will sync, if applicable | Claiming cloud save for a local-only draft |
| Permission denied | Give a safe, comprehensible outcome | Exposing another user's record details |
| Completed | Confirm the real effect and let users continue | Gratuitous celebratory animation or invented productivity numbers |

Put feedback near the control or artifact that changed. A full-page spinner for a checkbox is often wrong; a local pending state with retained context is often clearer. Motion should communicate cause, change, or continuity, then stop. Support `prefers-reduced-motion`.

## Accessibility is a workflow requirement

Use [WCAG 2.2](https://www.w3.org/TR/WCAG22/) as a reference and define an appropriate conformance target rather than casually claiming compliance.

- Semantic buttons, links, headings, input labels; avoid clickable divs as substitute controls.
- Keyboard reachability, visible focus, sensible tab order, and focus return when closing dialogs or drawers.
- Manage focus inside modal surfaces; remove hidden content from keyboard/screen-reader traversal when dismissed.
- Names, roles, states, and relevant status/error announcements for controls and pending actions.
- Readable contrast, scalable text, usable touch targets and responsive layout at narrow widths and zoom.
- Don't rely only on color or animation; show text/symbol/state redundantly where it matters.
- Respect reduced motion and support error identification plus recovery.
- Automated checks help but cannot prove keyboard, screen reader, spatial layout, or cognitive usability.

## Practical review

Inspect the actual core journey on keyboard, narrow/mobile viewport, and light/dark (when supported). Try: slow request, failed save, duplicate submit, dialog opened then route changed, tab hidden/restored, session expired while editing. Verify whether drafts, focus, visible identity, and previous confirmed results survive appropriately.

## Anti-pattern probes

- Are we copying a fashionable template rather than matching the task?
- Does a content preview show so much information that it buries the next action?
- Is progress derived from real events or synthesized from current counters?
- Does animation repeat on every render or block the primary action?
- Do errors look indistinguishable from true empty states?
- Did new features silently alter an existing approved interface?
- Did a user request simple capture, but we force them into a folder taxonomy first?

Treat stylistic judgments as hypotheses to validate with users where practical; don't universalize preferences from a single product.
