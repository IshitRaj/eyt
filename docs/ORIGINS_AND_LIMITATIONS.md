# Origins, scope and limitations

## Where EYT came from

EYT v0.1.0 was drafted from a set of engineering notes supplied by the developer of a personal web/extension product, including early backend-readiness findings, UX/visual audit revisions, backend contracts, persistence and account recovery decisions, operational checklists and release-evidence notes. The supplied materials concern **one evolving project**. They are useful as *observations of failure modes and attempted corrections*, not as a representative sample of all AI-generated software.

The repository intentionally does **not** distribute those source documents, implementation code, credentials, internal environment names, deployment URLs, local test data, or brand-specific UI tokens. Examples have been generalized and rewritten. The author of the source project supplied the material for this exercise; its claims were not independently verified against the complete application source in preparing EYT.

## What can be claimed

- The skill package follows the open [Agent Skills format](https://agentskills.io/specification) structurally.
- Guidance was informed by the submitted project's documented engineering decisions and by publicly available security/accessibility materials linked below.
- The repository includes self-checks for packaging, links and example coverage. These are **structural checks only**.

## What cannot yet be claimed

- **No controlled comparison** demonstrates that agents using EYT build fewer bugs or more secure products than agents without it.
- It has **not** been exercised against multiple independent apps, agents, or model versions as part of this release.
- It has **not** undergone an independent security review, usability study, accessibility audit or expert peer review.
- Following EYT cannot guarantee correct architecture, secure code, legal compliance, accessibility or production readiness.
- Claims in the original project notes (including any test counts or deployment evidence) have not been reproduced here; no such counts are used as proof of EYT's effectiveness.

## Principles versus hypotheses

**Grounded professional guidance:** untrusted-input validation, server authorization, meaningful error recovery, data lifecycle design, safe secret handling, and evidence-matched release claims align with established engineering/security guidance.

**Experience-derived heuristics needing broader testing:** how much process improves agent behavior, when agents tend toward generic visual patterns, whether specific prompt instructions reduce UI drift, and how much an engineered skill helps beginners. Treat these as testable hypotheses, not universal facts.

## Public references (not copied into this project)

- [Agent Skills specification](https://agentskills.io/specification)
- [OWASP ASVS](https://asvs.owasp.org/) and [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)
- [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [OpenAI: Testing Agent Skills Systematically with Evals](https://developers.openai.com/blog/eval-skills)

These resources offer independent frameworks for further improvement; EYT does not claim their endorsement.

## How contributors can improve truthfulness

Publish reproducible prompts, exact agent/model versions, input repositories or shareable synthetic fixtures, the EYT revision used, observed outputs, test commands, false positives and regressions. Include negative results. Compare similar runs with and without EYT where possible. Never upload private project documents, user records, tokens, or production logs to support a public issue.
