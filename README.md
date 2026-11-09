# Math Research Vessel

A ready-to-use repository for mathematical research, exposition and computational investigation with AI agents such as Claude Code or Codex.

AI agents can draft proofs, search the literature and run checks. Left alone, they also lose track between sessions, cite results they never checked against the source, describe a plausible argument as a proven one, and leave the evidence scattered across chat logs. This repository gives the researcher and the agents one shared way of working, written as plain-text rules and guides that every agent reads:

- **Every claim says where it stands.** Proposed, checked by its author, independently reviewed, computed, formally verified, or accepted by the researcher. These are separate states, and a conditional result stays conditional.
- **Claims are tested, then reviewed independently.** The author tries small cases and counterexamples first. Then a fresh agent checks the exact text without the author's reasoning, and every fix goes back for another check.
- **Citations are checked.** Every load-bearing citation is checked against the exact edition and page of the source, with its hypotheses matched to how it is used.
- **Work is bounded, and finishes.** Each task has a deliverable and a stopping condition, and keeps going while a clear path inside its scope remains. The researcher decides what starts, what is accepted and what is published.
- **Nothing important lives only in a chat.** Results go into one report per task and proofs into LaTeX. Checkpoints are committed and pushed often, every stop is read back from the remote, and handoffs let a fresh session continue.

## Start a project

1. Click **Use this template** on GitHub and create your own repository, private if your research is unpublished. If you clone instead, point the copy at your own repository first (`git remote set-url origin <your-repository-url>`), so nothing is ever pushed back here.
2. Open it with your agent and say, for example: *"Read AGENTS.md and help me fill in the project charter for this question: …"*
3. Answer the agent's questions about the question, its exact setting and hypotheses, what you already know, who is involved, and how you like to work. Tell it which repository to push to and whether it may push. The charter it fills in steers everything after that.

A first investigation may clarify a question, reconstruct known mathematics or identify an obstruction; it need not promise a new theorem. For later work, the [workflow](docs/guides/workflow.md#prepare-the-next-assignment) describes a short preparation packet that compares possible next questions and ends with a prompt ready for the researcher to launch.

You need Git, an AI coding agent, and a TeX distribution (TeX Live, MacTeX or MiKTeX), because developed proofs are written in LaTeX. A proof assistant, a computer algebra system and Python are needed only if your project uses them.

## What is inside

```
AGENTS.md                  the entry point every agent reads first (CLAUDE.md points to it)
docs/collaboration.md      the policy: authority, evidence, review, preservation
docs/context/status.md     a short live snapshot of where the work stands
docs/project-charter.md    your question, scope, people and preferences
docs/guides/               how the work runs: workflow, writing, sources, and the optional parts below
docs/pathways/             a guide and template for retaining and choosing research directions
.agents/skills/            step-by-step procedures: review dispatch, citation check, handoff
manuscript/                the central article: a selected account of reviewed material
templates/                 a LaTeX template for standalone notes
tools/theorem_search.py    a small client for the TheoremSearch service
```

The optional parts sit quietly until the work needs them. Each one's guide is read only when its trigger in AGENTS.md fires:

| Part | Used when |
|---|---|
| Central article (`manuscript/`) | you develop a paper around a question, known literature or new results. The default layout is amsart; you can bring your own template or a journal's class. |
| Computation | a claim rests on a calculation in Python, SageMath, Macaulay2, GAP, Magma, Mathematica or similar. |
| Formal verification | a key step is worth checking in Lean, Rocq, Isabelle, Agda or a solver certificate. |
| Discovery | you search for known results (TheoremSearch, zbMATH, the Stacks Project, the LMFDB, the OEIS and others) or map the project's own results. |
| Research pathways | an idea should survive the session, or you need to compare possible next investigations. |

An unused part costs nothing, so the simplest choice is to leave it. If you do delete one, also delete its line in AGENTS.md and search the other guides for links to its file.

The [pathway guide](docs/pathways/README.md) keeps ideas in four buckets: next, worth returning to, conditional or tangential, and settled or retired. Start with a short ledger entry; use a pathway card when its reasoning or restart details deserve preservation. Agents capture ideas without diverting active work and reconcile affected entries at real checkpoints. A preferred order is a recommendation, and preparing a pathway does not launch it or promise article inclusion.

The research record preserves reviewed results and their evidence. The article selects what serves its question and reader: review alone does not admit material, and useful work can remain outside the paper. Its narrative can develop before there is a new theorem to announce.

## Agents

Any agent that reads `AGENTS.md` works, including Codex and Cursor: the skills are plain Markdown files that AGENTS.md links to. Claude Code reads `CLAUDE.md`, which points to AGENTS.md. To use the skills as Claude Code slash commands, copy `.agents/skills/` to `.claude/skills/`, and copy again after you change them so the two never drift.

The guides ask agents to use independent reviewers where they can, ideally from a different model family, and to say plainly when no independent check was possible.

## Make it yours

Rewrite this README to describe your project. Keep the vessel's license notice with its files: if you want your own license for your work, rename `LICENSE` to `LICENSE-vessel` and add yours. Adapt the policy and guides to how you work; the charter records your preferences, and it wins where it differs from a guide, except for the policy and the guides' mandatory rules. Record each change to AGENTS.md or the policy with its date and reason.

To take later improvements from the vessel, make a checkpoint you can return to, add the vessel as a remote, and read the difference before taking anything:

```sh
git remote add vessel https://github.com/PCeltide/math-research-vessel
git fetch vessel
git diff HEAD vessel/main -- AGENTS.md docs/collaboration.md docs/guides docs/pathways/README.md docs/pathways/TEMPLATE.md .agents templates tools manuscript/article/preamble.tex
```

Your charter, status, ledger, pathway cards, reports and manuscript are yours; the policy, guides, skills, templates and tools come from the vessel. In `docs/pathways/`, only README.md and TEMPLATE.md are vessel guidance; retain your project's cards when taking updates. Take an update between assignments: it never changes an active assignment's authority or bounds. A repository made with "Use this template" shares no history with the vessel, so merging needs `--allow-unrelated-histories`; copying the files you want is often simpler.

## Status

An early release. The rules come from a real research project and have been rewritten to be general. Feedback and suggestions are welcome as issues.

## License

Math Research Vessel by Pratik Apshinge. The Python files are under the MIT License, and everything else is under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); see [LICENSE](LICENSE). The research you do in a repository made from it is yours.
