# Math Research Vessel

A ready-to-use repository for doing mathematical research with AI agents such as Claude Code or Codex.

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

You need Git, an AI coding agent, and a TeX distribution (TeX Live, MacTeX or MiKTeX), because developed proofs are written in LaTeX. A proof assistant, a computer algebra system and Python are needed only if your project uses them.

## What is inside

```
AGENTS.md                  the entry point every agent reads first (CLAUDE.md points to it)
docs/collaboration.md      the policy: authority, evidence, review, preservation
docs/context/status.md     a short live snapshot of where the work stands
docs/project-charter.md    your question, scope, people and preferences
docs/guides/               how the work runs: workflow, writing, sources, and the optional parts below
.agents/skills/            step-by-step procedures: review dispatch, citation check, handoff
manuscript/                the central article: one LaTeX paper that collects the reviewed results
templates/                 a LaTeX template for standalone notes
tools/theorem_search.py    a small client for the TheoremSearch service
```

The optional parts sit quietly until the work needs them. Each one's guide is read only when its trigger in AGENTS.md fires:

| Part | Used when |
|---|---|
| Central article (`manuscript/`) | you write up results as a paper. The default layout is amsart; you can bring your own template or a journal's class. |
| Computation | a claim rests on a calculation in Python, SageMath, Macaulay2, GAP, Magma, Mathematica or similar. |
| Formal verification | a key step is worth checking in Lean, Rocq, Isabelle, Agda or a solver certificate. |
| Discovery | you search for known results (TheoremSearch, zbMATH, the Stacks Project, the LMFDB, the OEIS and others) or map the project's own results. |

An unused part costs nothing, so the simplest choice is to leave it. If you do delete one, also delete its line in AGENTS.md and search the other guides for links to its file.

## Agents

Any agent that reads `AGENTS.md` works, including Codex and Cursor: the skills are plain Markdown files that AGENTS.md links to. Claude Code reads `CLAUDE.md`, which points to AGENTS.md. To use the skills as Claude Code slash commands, copy `.agents/skills/` to `.claude/skills/`, and copy again after you change them so the two never drift.

The guides ask agents to use independent reviewers where they can, ideally from a different model family, and to say plainly when no independent check was possible.

## Make it yours

Rewrite this README to describe your project. Keep the vessel's license notice with its files: if you want your own license for your work, rename `LICENSE` to `LICENSE-vessel` and add yours. Adapt the policy and guides to how you work; the charter records your preferences, and it wins where it differs from a guide, except for the policy and the guides' mandatory rules. Record each change to AGENTS.md or the policy with its date and reason.

To take later improvements from the vessel, make a checkpoint you can return to, add the vessel as a remote, and read the difference before taking anything:

```sh
git remote add vessel https://github.com/PCeltide/math-research-vessel
git fetch vessel
git diff HEAD vessel/main -- AGENTS.md docs/collaboration.md docs/guides .agents templates tools manuscript/article/preamble.tex
```

Your charter, status, reports and manuscript are yours; the policy, guides, skills, templates and tools come from the vessel. Take an update between assignments: it never changes an active assignment's authority or bounds. A repository made with "Use this template" shares no history with the vessel, so merging needs `--allow-unrelated-histories`; copying the files you want is often simpler.

## Status

An early release. The rules come from a real research project and have been rewritten to be general. Feedback and suggestions are welcome as issues.

## License

Math Research Vessel by Pratik Apshinge. The Python files are under the MIT License, and everything else is under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); see [LICENSE](LICENSE). The research you do in a repository made from it is yours.
