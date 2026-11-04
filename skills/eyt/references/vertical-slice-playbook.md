# Example: engineer one complete feature, not six disconnected screens

This is a **worked decision example**, not a template or a runnable implementation. Use it when the user asks for a new authenticated web-app feature and has not prescribed architecture, UX behavior or error handling. Adapt decisions to the actual stack and project.

## The request

> Build an expense tracker where people sign in, add expenses, filter by month and see a monthly total. Make it look nice.

An inexperienced requester has specified the outcome, not the engineering boundaries. The agent should supply those boundaries without demanding a long questionnaire.

## 1. Make five decisions before code

- **Primary journey:** sign up, add an expense, see it in this month's list and total, reload and find it unchanged.
- **Authority:** database owns accounts and expenses. The client owns draft text and pending feedback only.
- **Trust:** user can access only their own expenses and monthly totals; a client-supplied `ownerId` is ignored or rejected.
- **Money semantics:** store minor currency units as integers if a single currency is in scope; never silently mix currencies. Define dates/month boundaries explicitly rather than using arbitrary locale conversions.
- **UI:** one clear Add expense action; summary and recent entries grouped by meaning, not all forced into equal dashboard cards. Empty, loading and failed read are separate states.

For a real public app, account creation, sessions, abuse limits and secure deployment matter. For a local mockup that deliberately has no accounts, don't add all that infrastructure.

## 2. Sketch one vertical request path

```text
ExpenseForm
   -> submit validated draft
   -> authenticated createExpense operation
   -> check input + ownership + money/date rules
   -> database insert (and any required transaction)
   -> return saved expense / explicit error
   -> show the confirmed row and refreshed total
```

The error path is equally important:

```text
Save request failed or outcome unknown
   -> keep entered values and original intent
   -> show accurate inline message
   -> retry/reconcile safely
   -> never display "Saved" until confirmed
```

If the framework already provides an appropriate Server Action abstraction, the operation might not need an extra HTTP route. Keep the responsibility clear regardless of transport.

## 3. Give code a home

A proportionate structure could be:

```text
app/expenses/page.tsx            Page composition and initial data
features/expenses/ExpenseForm.tsx UI input and feedback
features/expenses/expense.ts     Validation/policy and operation
features/expenses/expense-db.ts  SQL and transaction logic
features/auth/                     Existing session integration
```

This is an example, not a mandatory directory structure. If `expense.ts` and `expense-db.ts` are tiny and cohesive, combining them may be clearer. Avoid one global `app.tsx` component doing auth, SQL, dashboard UI, notifications, navigation and saving together.

## 4. Write rules so they are visible

Illustrative pseudo-TypeScript:

```ts
async function createExpense(
  session: VerifiedSession,
  untrustedInput: unknown,
): Promise<Expense> {
  const input = parseExpenseInput(untrustedInput);

  return expenseStore.create({
    ownerId: session.userId,
    description: input.description,
    amountMinor: input.amountMinor,
    occurredOn: input.occurredOn,
    category: input.category,
  });
}
```

The store must implement the needed record authorization and durable write. Parsing and ownership are named, not hidden in an enormous inline expression. Don't infer that the example alone handles CSRF, rate limits, session expiry, validation or concurrent writes. Those depend on the real implementation.

## 5. Make the first screen honest

- **First use:** say there are no expenses for the selected month, with Add expense clearly accessible. Do not fabricate a chart.
- **Input:** label description, amount, category and date; validate and explain an invalid amount.
- **Saving:** local pending feedback on the button and no duplicate submission.
- **Failed save:** entered values still visible; clear retry action; no false success.
- **Success:** show the actual saved row and updated month total after confirmed persistence.
- **Mobile:** narrow width, long descriptions, reachable action and usable input controls.

A visually expressive interface is allowed. It should serve content and brand, not repeat an identical rounded panel for every heading and row.

## 6. Test what matters

1. In a clean browser, create an account, add an expense and reload. It remains.
2. Add `1.25` and `2.35` in the same currency. Total is exactly `3.60` at displayed precision, with no floating-point surprise.
3. Create two accounts. Account B cannot read, edit or delete A's expense or infer it from totals.
4. Submit invalid amount/date. No write occurs, and feedback identifies the relevant field.
5. Force a failed write or dropped response. Draft persists; no duplicate record on safe retry.
6. Open the UI in a narrow browser and use the keyboard through the primary flow.
7. Document any unavailable tests. Don't claim all cases passed because `next build` passed.

## 7. Review as a maintainer

A new developer should be able to answer quickly: Where do I add a new category? Where does the month boundary come from? Where is user ownership checked? Where does the UI decide success? Can I replace SQL later without rewriting a whole dashboard component?

If those answers require tracing many unrelated functions, simplify the code. If the app passes all checks but is split into a dozen single-use service layers, also simplify the code. Either form of complexity can be harmful.

## 8. Report accurately

> Built expense creation and the monthly summary. Used server-owned account identity and integer minor units for money. Verified [exact tests you actually ran]. Could not verify [unavailable browser/deployment cases]. Did not add analytics or deploy. Next: [specific pending check].

This is how EYT should guide the agent's decisions without taking away the user's product authority or pretending that every project needs the same architecture.
