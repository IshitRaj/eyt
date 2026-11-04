# Contributing to EYT

EYT is experimental. The best contribution is a **specific, reproducible improvement** rather than a stronger marketing claim.

## Good contributions

- A scenario in which the agent ignores an important data, UX, accessibility or authorization invariant.
- A false positive where EYT imposes excessive process on a small project.
- A refactor that makes `SKILL.md` clearer or reduces unnecessary reference loading.
- An evaluation comparing similar runs with and without EYT (including cases where EYT made things worse).
- A correction grounded in authoritative documentation or practical engineering evidence.
- A portability improvement for an Agent Skills-compatible client, with the tested client/version stated.

## Reporting an evaluation

Include: minimal shareable task; agent/model/version; tool permissions and environment; whether skill invocation was confirmed; exact prompts and EYT revision; observable acceptance checks; results of those checks; limitations; costs/time if measured. Do not use synthetic "test passed" claims without actual artifacts. Use [the rubric](evaluations/RUBRIC.md) and [results template](evaluations/RESULTS_TEMPLATE.md).

Redact credentials, session cookies, tokens, real account records, user emails, provider metadata with secrets, and private code/documentation before opening an issue. When in doubt, create a synthetic reproduction.

## Improving actionable guidance

Prefer a useful **smell -> cause -> practical default -> verification** example over another generic statement such as "write scalable, secure code." A proposed rule should say **when it applies**, what a small project should do instead, and what would make the rule inappropriate. Code-quality proposals should include small before/after excerpts that preserve semantics, or explicitly note when behavior changes. UI advice must describe user goals and accessibility rather than impose one aesthetic.

Report failures of the skill itself, including when it adds unnecessary complexity, introduces inaccessible patterns, changes approved UX or leaves a critical user journey untested.

## Updating the skill

Keep one installable `skills/eyt/SKILL.md`. Put detailed policy in focused `references/` files and link to them directly from the skill. Prefer precise, conditional instructions over "always use [framework/pattern]". Respect higher-priority user instructions. Avoid promising that EYT eliminates bugs. Maintain beginner readability.

Run `python3 scripts/check_repo.py` and `python3 -m unittest discover -s tests -v`, then manually check the changed guidance for contradictions and overgeneralization. These checks do not establish real-world effectiveness.

## License and evidence

By submitting changes, you agree that your contributions may be distributed under this repository's MIT license. Do not copy copyrighted standards or private documentation into the repo; link and paraphrase within the relevant rights. Product-specific anecdotes should be marked as such, not presented as representative research.
