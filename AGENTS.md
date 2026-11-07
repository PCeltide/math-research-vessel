# Working here

This is a mathematical research workspace shared by a researcher and AI agents. At startup, and after any context restart, read this file, the [policy](docs/collaboration.md) and the [live status](docs/context/status.md) in full. A summary, memory or handoff does not replace them. Then inspect the actual branch or snapshot, any uncommitted changes and who owns them. Read the active assignment and its named inputs at their recorded revisions. If a required input is missing, pause the work that depends on it and continue the rest. If tool output is truncated, read the omitted part before relying on it. While the charter still has blanks the first investigation depends on, run the workflow's Foundation with the researcher before starting any research assignment.

A small question that needs no new result (an explanation, a definition, a quick check) can be answered directly. Say how far the answer was checked, and record it only if later work will rely on it.

## Guides and when to read them

When a trigger below fires, read that guide in full before acting (for the workflow, the section for your step). A fired trigger is a requirement.

- [Charter](docs/project-charter.md): starting any assignment (read it in full; it is short), and any question of scope, hypotheses or the researcher's preferences.
- [Workflow](docs/guides/workflow.md): framing a project, starting an assignment, auditing existing mathematics, testing or writing up a result, updating the ledger, committing or pushing a checkpoint, stopping.
- [Mathematical writing](docs/guides/mathematical-writing.md): drafting, revising or reviewing any mathematical exposition, whether a proof, note, report or the article.
- [Sources](docs/guides/sources.md): receiving, storing, recovering or reading a source; recording an edition or locator; running a literature or positioning search.
- [Central article](docs/guides/central-article.md): editing, admitting a result into, restructuring or reviewing the article in `manuscript/` or its NARRATIVE.md; building the PDF; changing the LaTeX template.
- [Computation](docs/guides/computation.md): writing, running or citing a scripted calculation, search or symbolic check.
- [Formal verification](docs/guides/formal.md): considering, running or reviewing a proof-assistant check; describing formal evidence in prose.
- [Discovery](docs/guides/discovery.md): searching for known theorems or prior results, or mapping the project's own results and their dependencies.
- [Review dispatch](.agents/skills/review-dispatch/SKILL.md): a claim, proof, repair, citation change or integration needs an independent check.
- [Citation check](.agents/skills/citation-check/SKILL.md): adding, changing, moving or auditing a citation or an attribution. Run it before review dispatch.
- [Handoff](.agents/skills/handoff/SKILL.md): pausing, stopping, a likely compaction, resuming, or passing work to or from a worker or reviewer.

A guide for a part the project does not use, such as the central article, a proof assistant or a computer algebra system, simply never fires.
