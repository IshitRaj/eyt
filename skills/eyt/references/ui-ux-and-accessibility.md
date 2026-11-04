# UI/UX that serves the task instead of looking generically generated

**Do not design from a component catalog. Design from the user's job.** The aim is not to make every website minimalist or forbid cards, gradients and rounded corners. The aim is to make each visual decision have a reason tied to content, brand, hierarchy or interaction.

## Step 1. Draw the user's scan path in words

Before writing JSX, answer these for each important screen:

1. **Arrival:** where did the user come from and what do they need to know first?
2. **Primary action:** what is the one task this screen should make easy?
3. **Recognition:** what actual content (title, URL, item, date, owner, state) helps orientation?
4. **Secondary choices:** what can wait until after the primary task?
5. **Outcome:** what visible change proves the action completed?
6. **Recovery:** what does the user see if data is absent, loading, denied or failed?

Example for a link-saving popup: put the URL and recognized page at the top, allow a direct Save, then optional organization or notes. Forcing a user to choose a folder, category, reading status and tags before the first save creates friction. This pattern is an example, not a universal rule for all forms.

## Step 2. Build visual hierarchy from content

Select one coherent type scale, spacing rhythm, meaningful palette, interaction treatment and icon system. Use **different structures for different data types**. A note preview, chart, command palette, status choice and navigation rail do not all need the same card shell.

Choose visual identity from the user's context, provided references and existing product conventions. If no identity is provided, state a restrained direction and let the product content distinguish the interface. Use whitespace, typographic hierarchy, alignment and dividers before adding more decoration.

### Generic AI UI smell -> better decision -> test

| Warning sign | Better approach when appropriate | Quick test |
| --- | --- | --- |
| Purple/blue gradient behind every headline | Palette with semantic roles: text, surface, border, action, status, identity | Remove background effects; is hierarchy still clear? |
| Three equal feature cards on every landing page | Show the actual user journey with meaningful product surfaces and varied section rhythm | Can a visitor explain how to complete the product's main task? |
| Every section and icon wrapped in cards | Use plain lists, tabs, dividers or whitespace where items belong together | Does each container convey a distinct artifact/group or just decoration? |
| Everything has the same corner radius, badge and heavy shadow | Reserve visual weight for primary actions and special artifacts | Identify primary action in 3 seconds without reading every label |
| Repeated tiny gray metadata/eyebrow labels | Clear heading and readable secondary information only when necessary | Remove labels that restate the same adjacent meaning |
| Generic copy: "supercharge productivity" | Say exactly what the user can do and what happens to their data | Could the same text describe ten unrelated apps? If yes, rewrite |
| Fake users, activity graphs, stats, reviews or testimonials | Genuine empty state, or **explicitly labeled** synthetic demo examples only when authorized | Fresh account never presents fabricated activity as real |
| Color used independently for every item | Use color for brand, selection, severity, category or actual state | Does every accent have a stable meaning? |
| Decorative icons/emoji with inconsistent visual language | Consistent icons, favicons or recognizable content-specific assets | Can an item be recognized without reading extra filler labels? |
| Every element animates on entry or loops forever | Short motion showing cause, continuity or transition; provide reduced motion | Can the page be read promptly and used with reduced motion? |
| Static interactive-looking demo controls | Make them work, label them as demonstrations or remove their affordance | Keyboard/click activates a real effect or an explicit demo |
| Endless page-wide spinners | Retain confirmed content and show pending feedback near the item/action | Slow request doesn't erase context or move focus unexpectedly |

These are heuristic probes, **not metrics or universal aesthetic rules**. Well-designed applications can legitimately use gradients, cards and motion.

## Step 3. Give every important state a truthful treatment

| Situation | Required information/action | Failure to avoid |
| --- | --- | --- |
| New account, no records | What belongs here; one relevant first action | Fake graph and “You saved 23 items” |
| Loading | Preserve layout/context; meaningful busy label where needed | Premature “Nothing found” |
| Failed read | Distinguish service error from zero records; offer retry | Empty list hiding an outage |
| Pending save | Preserve draft, disable duplicate intent, show local feedback | Close form before confirmation |
| Confirmed save | Show durable item or specific success | Success toast while storage failed |
| Conflict | Keep draft; offer reload/review resolution | Silent overwrite |
| Offline/uncertain response | State whether the item is local, queued or confirmed remotely | Claiming cloud save from local-only state |
| Delete/Undo | Show exactly which item changed and whether restore is pending | Stale snapshot restores across another user's changes |
| Session expired | Preserve safe draft and explain reauthentication | Clear input or switch identity silently |

The right UI feedback can be modest: a button label, localized spinner, inline error and retained value are often better than a full-screen animation. Pending action state should remain recognizable; independent items can often proceed concurrently.

## Step 4. Adapt to device, keyboard and assistive use

Use [WCAG 2.2](https://www.w3.org/TR/WCAG22/) as a relevant standards reference, not a substitute for testing.

- Real buttons and anchors; meaningful labels and headings; no clickable `div` when a semantic control fits.
- Keyboard operation, visible focus, logical tab order and focus return after dismissing overlays.
- Focus trapping only when appropriate for modal dialogs. Prevent hidden controls from being accidentally focusable.
- Announce meaningful asynchronous status/errors without flooding screen readers.
- Inputs have labels; validation connects error text to the field; never rely solely on red borders.
- Ensure text readability, contrast, zoom, touch targets, narrow viewport and orientation behavior.
- Support `prefers-reduced-motion`; content must remain readable even when animation is disabled.
- Verify with real content lengths, long titles, empty datasets and errors, not only polished mock text.

### Screen-specific smoke paths

- **Signup/login:** fresh browser can reach forms; redirects do not loop; errors preserve the input that may safely remain.
- **Create/edit:** form values survive validation/network failure; after success the record is visible after reload.
- **Search:** field/frame remain stable; old requests do not replace new results; empty and failed query are distinct.
- **Dialogs:** keyboard and focus work; closing returns to logical trigger; saved data isn't lost on navigation.
- **Mobile:** test narrow width, long content, touch target spacing and horizontal overflow.
- **Themes:** when multiple modes exist, test each with real state and focus, not only the static landing page.

## Step 5. Preserve the approved product

If an existing product has an approved design, this reference is a **diagnostic lens, not a redesign license**. Internal extraction must preserve existing DOM/CSS/assets/copy/layout/themes/motion/interactions as required by the user. New necessary UI follows established tokens and patterns. Ask before elective visual changes or genuine design conflicts.

Historical design feedback can be superseded by later approvals. Do not use a generic anti-card heuristic to remove an intentionally designed capacity card, or a typography preference to rewrite established branding.

## Avoid two opposite mistakes

1. **Template slop:** same dashboard grid, badges and gradients regardless of job.
2. **Taste dictatorship:** assuming one engineer's favorite minimal style is correct for every audience.

The corrective principle is purpose, coherence, accessibility and evidence. Validate with users where possible; a static screenshot or AI aesthetic preference does not establish usability.
