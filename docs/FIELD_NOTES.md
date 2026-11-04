# Field notes: from one project's corrections to reusable lessons

These are **generalized, anonymized patterns** derived from dated review, design, incident and release notes supplied by the creator of one web/extension project. They are **not independent audits** or measured evidence about all AI coding tools. Each entry is an observed/documented problem or decision, the broader engineering lesson it suggests, and a test another project can run.

| Documented pattern in the source project | Generalizable lesson | Reproducible check to propose |
| --- | --- | --- |
| A UI showed save success after writing browser state even when persistence failed. | Success feedback must match the actual durability guarantee; preserve drafts on failure. | Force write failure/unknown response; confirm no false success or duplicate on retry. |
| Demo initialization mixed sample records into a previously edited workspace. | Keep demo seeds and migrations separate from real account data; errors must not reset data. | Delete sample-like content, reload and simulate malformed stored data; verify no resurrection/overwrite. |
| An extension limited its *stored* captures using a “recent 12” display slice. | View pagination is not retention policy. | Save more than the visible list size and verify all persisted records remain. |
| Routes were derived from mutable, non-unique names. | Use stable identity for routes and relations; names are presentation. | Create same-name groups, rename one and check links still target intended records. |
| Client-only identity existed before real authentication and ownership enforcement. | Verified identity and record-level server authorization are different responsibilities. | Read/update a resource with another account's identifier; expect denial without disclosure. |
| Completion charts were reconstructed from current item state. | Define whether metrics represent current state or historical events and preserve time semantics. | Complete, reopen, complete and delete; inspect what history means and whether counts duplicate. |
| Lists/search aggregated all records in memory. | Prefer bounded server queries and stable cursor/order where real data scale requires it. | Populate beyond one page; compare counts, search scope and stable pagination across updates. |
| Multi-record move/delete/Undo had only local snapshot semantics. | Cross-record invariants need server-owned transitions and conflict-safe restoration. | Change a related child after deletion, then try stale Undo; verify no clobbering. |
| UI recovery followed an unintended redesign during code refactoring. | Freeze approved presentation while extracting internals; new views should inherit established patterns. | Compare representative screens across viewport/theme/focus and examine changed markup/CSS. |
| Async responses from an old account or dialog could reach newer state. | Late operations must be bound to the initiating identity and view, not only API credentials. | Switch accounts or reopen a different dialog before response; ensure old result doesn't take over. |
| An unknown response to a create could cause a duplicate when retried. | Distinguish failed versus uncertain outcomes; reuse intent identity for reconciliation. | Commit then drop response; retry and count records. |
| An export could exceed the supported single-request import size. | Check complete lifecycle interoperability, not isolated happy paths. | Export a near-capacity account and restore it via the documented importer. |
| Source hashes and builds passed while some browser/extension states remained unverified. | Evidence needs precise scope; compilation and partial visual snapshots are not launch certification. | Create an evidence matrix including environment, tested states and explicit gaps. |
| Operational gates such as monitoring, backups, legal materials, distribution setup and environment isolation remained external to code quality. | Production deployability and public-launch authorization are separate. | Rehearse release/rollback with isolated data and list unresolved external gates. |

## What is opinion rather than established fact?

The source notes contain project-specific visual preferences (for example particular palette choices and objections to a generic card-heavy layout). EYT **does not export those preferences as universal UI rules**. Instead, it asks an agent to choose a coherent visual language for each product, avoid invented content, honor approved designs, and test usability.

The original author's impression that AI agents often produce similar layouts or under-specify security is a motivating hypothesis. This repository does not assert a prevalence rate, prove causation, or claim the observations represent all models.

## Source handling

The original source archive and product `AGENTS.md` are intentionally excluded from the public repository. The examples above are paraphrased patterns, not copied project code or private operational material. For the scope of independent validation, see [origins and limitations](ORIGINS_AND_LIMITATIONS.md).
