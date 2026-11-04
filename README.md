# EYT  -  Engineer Your Thing

**Make AI agents think beyond “it works.”**

EYT is an experimental, open-source [Agent Skill](https://agentskills.io/) that gives coding agents a structured way to plan, build, refactor, review and prepare **web applications and SaaS** for release. It emphasizes useful UX, readable architecture, trustworthy data handling, server-side authorization, privacy by design, failure recovery and honest verification.

It is written for people who can describe **what they want to build** but may not know every technical decision they should ask an AI agent to make. It is also useful to developers who want a consistent engineering checklist without a rigid framework.

> **Status: v0.1.0  -  experimental.** EYT has not been benchmarked across independent projects or coding agents, independently security-audited, or proven to reduce defects. The package includes structural checks and proposed evaluations, **not performance results**. Contributions and critical testing are welcome.

## The problem EYT tries to address

A generated application can look complete while hiding problems: a save that didn't persist, an inaccessible dialog, an unscoped data query, fake demo records, a missing failure state, overcomplicated modules, or a production build with no tested rollback. A vague request like “build me a SaaS” does not tell an agent what assurances matter.

EYT supplies *procedural engineering questions and decision boundaries*. It does **not** supply a universal stack, force every site into enterprise architecture, or promise to catch every security issue.

## What it asks an agent to do

1. Understand the actual user goal, constraints, data sensitivity and approved design.
2. Choose an appropriately simple architecture and identify critical invariants.
3. Implement a small end-to-end feature with clear UI, domain, data and trust boundaries.
4. Handle failures, accessibility, privacy, concurrency and recovery in proportion to risk.
5. Verify with evidence appropriate to each claim; separate implementation from deployment and public launch.

A static site receives lightweight treatment. An authenticated product handling private data receives stronger validation, authorization, persistence and release checks.

## Installation

Install the **entire** skill directory, including `references/`. These are manual, local installation instructions; nothing is automatically installed or uploaded by this repository.

### Codex (project-level)

From a checkout of this repository, run these commands **inside the project that will use EYT**, replacing `/path/to/eyt` with the checkout path:

```bash
mkdir -p .agents/skills
cp -R /path/to/eyt/skills/eyt .agents/skills/eyt
```

For a user-level Codex installation:

```bash
mkdir -p ~/.agents/skills
cp -R /path/to/eyt/skills/eyt ~/.agents/skills/eyt
```

### Claude Code (project-level)

```bash
mkdir -p .claude/skills
cp -R /path/to/eyt/skills/eyt .claude/skills/eyt
```

Other agents implementing the Agent Skills format may support the same `SKILL.md`; **we have not verified compatibility across clients**. Consult your agent's current documentation for the relevant installation directory. Restart/reload the agent session if it does not discover the newly installed skill.

You can also read `skills/eyt/SKILL.md` directly and ask an agent to follow it, but skill discovery/invocation is not guaranteed in that case.

## How to use EYT

Ask the agent to invoke `$eyt` explicitly while you're learning. Automatic invocation depends on the agent and the task description.

**Starting a project:**

> Use $eyt to build a personal reading tracker. Explain the smallest sensible architecture and the data-loss/security trade-offs before coding. Keep the interface simple and accessible. Do not add tracking or sign-in unless needed.

**Existing project:**

> Use $eyt to review this application's architecture, persistence, authentication and UX. Validate whether my concerns are real. Propose prioritized fixes, preserve the approved UI and then implement only the agreed scope.

**Before release:**

> Use $eyt to assess whether this web app is ready for a public launch. Report exact checks performed, what remains unverified, security and data risks, and whether publication should be blocked. Do not deploy without my approval.

**Planning without code:**

> Use $eyt in planning-only mode. Turn my product idea into a concise engineering brief, trust boundaries, core flows, acceptance criteria, and a small milestone plan. Don't edit files.

More prompts: [examples](examples/USAGE_PROMPTS.md).

### What to expect in the answer

A useful output separates **decisions** from **observations** and **claims**. For substantive work, the skill asks for a brief handoff: outcome, trade-offs, checks actually run, remaining gaps, and next action. If a browser was unavailable, it should say so. If an API test failed, it should not quietly substitute a successful build.

## What's inside

```text
eyt/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CHANGELOG.md
├── skills/
│   └── eyt/
│       ├── SKILL.md                 # one installable skill
│       └── references/             # loaded by the agent when relevant
│           ├── decision-guide.md
│           ├── ui-ux-and-accessibility.md
│           ├── architecture-and-readability.md
│           ├── security-and-privacy.md
│           ├── data-and-state.md
│           └── verification-and-release.md
├── docs/
│   ├── FIELD_NOTES.md
│   └── ORIGINS_AND_LIMITATIONS.md
├── examples/
│   └── USAGE_PROMPTS.md
├── evaluations/
│   ├── SCENARIOS.md
│   ├── RUBRIC.md
│   └── RESULTS_TEMPLATE.md
└── scripts/ and tests/            # structural checks, not agent evaluations
```

The `SKILL.md` stays procedural and relatively small. Supporting references are read on demand. EYT is not intended to add a permanent stack of project documents to every repository.

## Try it and report whether it helps

There are **no published comparative results** in v0.1.0. To evaluate the claim that EYT improves engineering behavior:

1. Select a small, shareable project or synthetic fixture and define observable acceptance criteria **before** generating code.
2. Run similar tasks with the **same agent/model/environment**, once with and once without EYT. Record prompt, tool access, agent version, time/cost if known, and whether the skill was actually loaded.
3. Execute independent functional/security/UX checks. Assess the same criteria and record failures, regressions, and additional complexity.
4. Share both successful and unsuccessful findings, with sanitized artifacts and reproducible steps.

Start with [scenarios](evaluations/SCENARIOS.md) and the [rubric](evaluations/RUBRIC.md). A single anecdote is interesting, not proof of general improvement. Expect results to vary by model, task and user prompt.

### Local structural checks

From the repository root:

```bash
python3 scripts/check_repo.py
python3 -m unittest discover -s tests -v
```

These checks catch broken relative links and malformed packaging metadata. They do **not** invoke an AI agent, execute the example apps, assess security or establish that the skill works.

## What EYT will not do

- Guarantee security, legal compliance, accessibility, zero bugs, or production readiness.
- Replace penetration testing, professional review, user research, or a documented threat model for high-stakes systems.
- Force enterprise patterns into small sites or require a particular framework, database or cloud.
- Collect analytics or add third-party services without an approved requirement.
- Approve production deployment, payment activation, external side effects or destructive migrations by itself.
- Fabricate tests, benchmark results, user data, success states or launch evidence.

See [origins and limitations](docs/ORIGINS_AND_LIMITATIONS.md) for the evidence boundary and [field notes](docs/FIELD_NOTES.md) for the source-derived failure modes that informed the guidance.

## Contributing

Feedback from engineers, designers, security practitioners, testers, and first-time builders is welcome. Please include concrete reproduction steps and negative findings; avoid unsupported claims. Read [CONTRIBUTING.md](CONTRIBUTING.md) for how to propose changes and protect private data.

## License

[MIT](LICENSE). References to standards and external guides are informational; those works remain under their own terms and are not included in this repository.
