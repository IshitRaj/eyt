# EYT: Engineer Your Thing

**Make AI agents think beyond "it works."**

EYT is an experimental, open-source [Agent Skill](https://agentskills.io/specification) for building and reviewing **web applications and SaaS**. It tries to act as the engineering guide a user might not know to ask for: choosing a sensible architecture, avoiding generic UI decisions, writing readable code, protecting data, handling failure and checking whether real user journeys work.

**Version v0.3.0 (experimental, 21 November 2026).** This release contains research-informed engineering guidance. Its real-world effectiveness has yet to be established through controlled evaluation.

## The problem

Someone can describe the app they need without knowing to request server-side authorization, reliable write feedback, meaningful empty states, maintainable module boundaries, or a test that actually opens the sign-in screen. AI coding agents may make plausible choices that compile but fall short of those expectations.

EYT attempts to bridge the gap **without turning every hobby project into enterprise architecture**. It tells the agent what to examine, what default to choose, what AI-generated shortcuts to watch for, and how to test that the decision works.

## What changed in v0.3.0

The shorter core skill now asks the agent to identify what a revision must preserve, rerun those checks, and investigate a failed repair against the last working state. The references show how to check whether a regression test can detect the original fault, scope tool permissions, and exercise a UI with real content, keyboard input and failure recovery.

The evaluation materials now use neutral task prompts, repeated paired runs and audited hidden checks. The research notes distinguish benchmark findings, practitioner design examples and decisions that still need testing. See the [research review](docs/RESEARCH.md), [comparison protocol](evaluations/RUBRIC.md) and [release notes](releases/v0.3.0.md).

## A one-minute example

A beginner asks:

> Build a reading tracker where people can sign in, save links, and mark them finished. Make it look nice.

Without enough context, an agent might build an attractive mockup with sample activity, client-only accounts, one large component and a "Saved" toast before persistence. This is a possible failure pattern, **not a claim about every agent**.

With EYT, the agent is instructed to choose a proportionate approach: establish actual account ownership, separate durable records from UI drafts, show truthful pending/error states, give the primary Save action a clear reading path, organize cohesive feature logic, and test signup through the actual UI and a save after reload. It should report what was checked rather than assume it worked.

## Install the single skill

Copy the **entire** `skills/eyt/` folder, including `references/`. Only `SKILL.md` is loaded initially by many clients; the reference files are used when relevant. Exact discovery behavior is client-specific.

### OpenCode (project-local)

```bash
mkdir -p .opencode/skills
cp -R /path/to/eyt/skills/eyt .opencode/skills/eyt
```

### Codex (project-local)

```bash
mkdir -p .agents/skills
cp -R /path/to/eyt/skills/eyt .agents/skills/eyt
```

### Claude Code (project-local)

```bash
mkdir -p .claude/skills
cp -R /path/to/eyt/skills/eyt .claude/skills/eyt
```

Restart or reload a session after installation if your agent doesn't discover new skills automatically. Consult your client documentation if the path differs. We have not independently verified every client on every version.

## Upgrading an existing installation

Replace the existing project-local `eyt` skill directory with the full `skills/eyt/` folder from v0.3.0, including all reference files. If you modified a local copy, review and preserve those changes first. Open a new agent session and confirm it loads the intended version.

The skill name and invocation remain `eyt`. Existing projects do **not** need architecture or UI rewrites just because the guidance changed. EYT should continue to respect approved designs, existing contracts and data.

## Ask the agent to use it

**Starting a project**

> Use EYT to build a small personal reading tracker. I know the features I want, but not all the architecture and security decisions. Choose simple, justified defaults, create a usable interface, write readable maintainable code, and test the real user journey. Do not add tracking, payments or deployment.

**Improving existing code**

> Use EYT to review this application. Identify actual problems in readable code structure, data flow, UI states and trust boundaries. Distinguish critical faults from style choices. Keep approved UI and behavior unchanged. Fix confirmed root causes in narrow, verified changes.

**Planning only**

> Use EYT in planning-only mode. Produce a concise engineering brief, user journeys, architecture decisions, trust boundaries, failure states, and acceptance checks. Do not write code or deploy.

**Release review**

> Use EYT to review launch readiness. Run checks you have access to and report exact failures, unknowns and approvals still required. Do not deploy without permission.

For OpenCode, the agent must actually load the skill using its skill mechanism. Mentioning EYT without the tool loading `SKILL.md` does not establish that the instructions were applied. See the [official OpenCode skill documentation](https://opencode.ai/docs/skills).

More examples: [usage prompts](examples/USAGE_PROMPTS.md).

## What the skill includes

```text
eyt/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CHANGELOG.md
├── skills/eyt/
│   ├── SKILL.md                  Core, executable engineering guidance
│   └── references/
│       ├── agent-failure-patterns.md
│       ├── vertical-slice-playbook.md
│       ├── code-craft.md
│       ├── ui-ux-and-accessibility.md
│       ├── architecture-and-readability.md
│       ├── decision-guide.md
│       ├── security-and-privacy.md
│       ├── data-and-state.md
│       └── verification-and-release.md
├── docs/                        Origins, field notes, limitations
├── examples/                    Prompts for different use cases
├── evaluations/                 Scenarios, rubric and results template
└── scripts/ and tests/          Static packaging checks only
```

The primary skill is intentionally compact. It asks the agent to read relevant references when necessary instead of loading an encyclopedia into each small task.

## Testing and evidence

There has been one **informal, unreplicated comparison reported by a user**, reviewed by a second LLM. It reported a better end-to-end user flow in the EYT-assisted candidate, but also found a session-storage weakness there. The candidate source trees and original execution traces were not independently audited here. The reviewer report alone **does not establish causality, general improvement or security effectiveness**. Neither v0.2.0 nor v0.3.0 has a controlled comparison.

To help evaluate EYT:

1. Choose a shareable task with acceptance criteria fixed before generation.
2. Run the same agent/model/environment both with and without EYT. Verify the skill was loaded and record limitations, tokens/time, and interventions.
3. Review with independent tests, including real UI journeys, security negatives, readability and extension cost. Reviewers should be blinded to the treatment if practical.
4. Publish reproducible results, including negative outcomes and extra complexity.

See the [evaluation scenarios](evaluations/SCENARIOS.md), [rubric](evaluations/RUBRIC.md) and [results template](evaluations/RESULTS_TEMPLATE.md).

### Local structural checks

```bash
python3 scripts/check_repo.py
python3 -m unittest discover -s tests -v
```

Passing these tests means the package has a valid structure and links. **It does not test that an agent follows EYT or builds better software.**

## What it does not promise

EYT does not guarantee security, accessibility, legal compliance, performance, production readiness, maintainability or bug-free applications. It does not have authority to deploy, collect analytics, activate payments or delete live data. It is not a universal stack, UI theme, code generator or substitute for adversarial testing. The original observations come primarily from **one evolving project**, not a representative study of AI-generated software.

See [origins and limitations](docs/ORIGINS_AND_LIMITATIONS.md) and [field notes](docs/FIELD_NOTES.md). Criticism and corrections are welcome through issues and pull requests.

## License

[MIT](LICENSE). Copyright (c) 2026 Ishit Raj. Third-party references remain under their respective terms.
