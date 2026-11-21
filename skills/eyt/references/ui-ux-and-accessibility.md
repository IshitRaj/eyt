# UI/UX and accessibility

Use this guide when building or changing a screen. For an approved design, identify the required components, tokens, copy, assets and interactions before making changes. Keep elective redesign outside a maintenance task.

## Compose the screen around the user's decision

Start with a real example. What brought the user here, what information do they need next, and how will they recognize the outcome? In a link-saving popup, showing the recognized page beside Save lets the user check the destination. Folder selection can wait if filing is optional.

| When reviewing a screen | Decision to make | Check in context |
| --- | --- | --- |
| A dashboard opens with equally prominent cards | Give prominence to information that changes the next decision. Use cards for independently browsable items, aligned rows or columns for comparisons, and a sequence for ordered work. | With realistic records, locate the item that needs attention and act on it. |
| A heading repeats a badge, eyebrow or adjacent label | Keep copy that identifies content, distinguishes a state or explains an action. Use the product's own vocabulary. | Remove the repeated words and check whether the section still makes sense when navigating by headings. |
| A screen looks crowded or disconnected | Align comparable fields, group a label with its value and leave more space between groups. Reuse type roles and spacing from neighboring screens. | Substitute long names and wrapped text. Can the reader still tell which value belongs to which label? |
| Everything competes for attention | Tie emphasis to reading order, state or brand. A gradient can keep text readable over a photo. Shadows can distinguish an overlay. | Check the actual foreground against varied backgrounds and in each supported theme. |
| An icon or surface looks actionable | Use familiar controls with consistent labels and states. Give icon-only controls accessible names and add a visible label if the meaning is unclear. | Find and activate the control using keyboard and touch. Essential instructions must be available without hover. |

Use genuine empty states for first-time users. Label any authorized sample content. Choose the layout that serves the product and its audience. The examples above offer design options. [USWDS card guidance](https://designsystem.digital.gov/components/card/)

## Make state and recovery visible

| Situation | What the user needs |
| --- | --- |
| Loading, no records or no matches | Preserve relevant context during a read. Offer a first action for an empty collection or a way to adjust an unsuccessful search. Distinguish a failed read and offer recovery. |
| Pending or failed save | Show feedback beside the action. Keep safe input through validation and retry, prevent duplicate submission and connect an error to the affected field. |
| Confirmed, queued or uncertain write | Identify which item changed and whether it is durable, queued locally or awaiting confirmation. Show success when the application can substantiate it. |
| Conflict, Undo or expired session | Identify the affected record and offer the available next step. Preserve safe drafts and keep them scoped to the right account. |

## Exercise the changed flow

Choose the checks that apply. Use the running interface to follow the task from its normal entry point through the result. For a save flow, try a failed submission, correct or retry it, and reload to check the stored result. For search, change the query while a previous request is pending. Use screenshots to compare an approved layout, and exercise controls to verify behavior.

- **Keyboard and assistive use.** Use native buttons, links and labeled inputs where they fit. Follow the task by keyboard in a logical order. Check that focus stays visible around sticky content. Expose meaningful asynchronous updates to assistive technology without taking focus or repeating every update. [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- **Modal dialog.** Open it by keyboard. Verify its accessible name, initial focus, forward and reverse tab order inside it, and dismissal with Escape. Check that focus returns to the opener or the next logical control if the opener is gone. [WAI-ARIA dialog pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)
- **Responsive layout.** At narrow widths and increased text size, check long content, reading order, target spacing and access to actions. Keep necessary two-dimensional scrolling, such as a wide data table, local to that region where possible. [WCAG reflow](https://www.w3.org/TR/WCAG22/#reflow)
- **Color and motion.** Check text contrast, meaningful control boundaries and state indicators on the surfaces where they appear, including dark mode when supported. Pair color with another cue for errors and selection. With reduced motion enabled, confirm that the action's result remains clear. [WCAG use of color](https://www.w3.org/TR/WCAG22/#use-of-color) and [non-text contrast](https://www.w3.org/TR/WCAG22/#non-text-contrast)

Record which paths, input methods and states you exercised. For questions about whether the intended audience understands the flow, observe a representative user trying the task when possible.
