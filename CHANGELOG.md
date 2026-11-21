# Changelog

## [0.3.0] - 2026-11-21 (experimental prerelease)

- Shortened the skill entry point and linked all nine references by task. Added checks for retained requirements after revisions.
- Added practical tests of assertion effectiveness and scoped tool access. Revised the UI guide around actual decisions, interaction states and accessible controls.
- Removed EYT invocations from shared evaluation prompts. Added paired two-round trials, grader audits, seeded faults and reporting of costs and missing observations.
- Documented the [evidence and its limits](docs/RESEARCH.md). Controlled evaluation of EYT remains outstanding.

## [0.2.0] - 2026-11-04

- Reworked `SKILL.md` into a more explicit engineering workflow with actionable defaults and concrete checks.
- Added an agent-failure-pattern reference pairing observed shortcuts with likely consequences, corrective options and verification probes.
- Added a code-craft reference with before/after TypeScript examples and a cognitive-load review method.
- Added a worked authenticated-feature walkthrough connecting decisions, UI, code responsibilities, failure recovery and tests.
- Expanded UI/UX guidance into task-based hierarchy, purposeful design, state behavior, accessibility and anti-template checks.
- Expanded security, data integrity and verification guides with concrete negative test paths.
- Clarified the limited evidence: one informal unreplicated LLM-reviewed comparison has been reported, but the source and execution traces were not independently audited and v0.2.0 has no comparative coding-agent evaluations.
- Added OpenCode installation guidance and a readability-focused evaluation protocol.
- Kept one installable Agent Skill, its existing invocation name, and the existing MIT license.
- Classified as experimental. Structural checks pass; these tests do not establish engineering effectiveness. No comparative agent run has evaluated v0.2.0.

## [0.1.0] - 2026-11-04

Initial experimental release with one installable skill, engineering references, project field notes, evaluation scenarios, contribution instructions and static package checks. No comparative effectiveness claims.
