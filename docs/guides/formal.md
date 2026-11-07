# Formal verification

A proof assistant such as Lean, Rocq (formerly Coq), Isabelle or Agda, or a checked certificate from a SAT or SMT solver, adds **selective** assurance to the obligations where it is worth the most. It is not a badge for every lemma. A checker run establishes a statement in a pinned environment. Whether that statement says what the mathematics says is a separate question, settled by an independent correspondence review.

## Choosing the destination

Start from the article's claims, not from the lemmas a library happens to offer. Name the terminal: the exact result a campaign aims at. A faithful formalization of a terminal uses the article's actual objects, maps, quantifiers and hypotheses. Every nontrivial input is either proved in the checked chain or kept visibly as a hypothesis of a **weaker, named intermediate theorem**. There is no hidden assumption equivalent to the conclusion, and no abstract model silently standing in for the real object. A connected conditional argument over the actual objects is an honest milestone; it is never presented as the unconditional theorem. Standard logical axioms are separate from unproved mathematical assumptions.

Before execution, compare a few candidate first contracts, each with its minimum faithful statement and its first obstruction, and freeze one. Available workers are not a reason to start several proof lanes. Count discharged obligations and faithful connections, not files, declarations or tags. The most useful next gain is usually a connected lemma that removes a real external assumption.

## Choosing what to formalize

Formalize where the check adds substantial assurance: completeness of a case analysis, a subtle reduction, an exact correspondence, a calculation too large to inspect. Skip mathematics that is checkable by inspection, and do not count universal quantification or many declarations as value in themselves. Reject a **proxy**, such as a check of one sampled parameter, a single invariant standing in for the full statement, or a certificate for one final step: the result would look like assurance without giving it. Existing valid evidence is preserved even when its marginal value is modest.

Each candidate passes a **feasibility gate** before full work. Check early whether the prerequisites exist in the tool's library (for Lean, Mathlib) or in the project. When the real cost is building a general theory the library lacks, stop and bring a scoped proposal to the researcher. There is no lemma quota, and no whole-document formalization.

## Evidence states

- **Source candidate:** the route and the relevant library declarations have been inspected; the project statement has not compiled.
- **Compiled consumer:** the exact project-facing statement compiled, with its dependencies and transitive axioms recorded. It is not yet known to say the intended mathematics.
- **Qualified endpoint:** its types, hypotheses, maps and correspondence have passed the required review and acceptance.
- **Integrated result:** the qualified endpoint is used in the intended proof chain, and that connection has been reviewed.
- **Reported, awaiting reconciliation:** a result someone reported whose decisive source and receipt have not been inspected. It enlarges no verified scope.

A library result being present in source and being faithfully applicable to the project's theorem are separate facts. A library's unreviewed or frontier area is not reviewed by being imported, and a tag or docstring may cover only part of a statement: read the literal signature. AI or external provenance is neither proof of applicability nor a reason to discard checked work.

## The candidate register

At every substantive stop, assess the completed argument for formal candidates, and record them, or "none identified", in `formal/CANDIDATES.md`. Each row:
- a stable ID and the exact source claim with its locator;
- the intended formal endpoint and its hypotheses;
- the value: what assurance it adds;
- reusable prerequisites;
- effort and risk;
- **exclusions:** what the formal statement does not cover, such as an input it assumes without proof;
- status: queued, active, completed (with correspondence review), deferred, paused, or declined (assessed and not worth formalizing), with a reason;
- a link to the report.

Recording a candidate authorizes nothing and extends no effort bound or timebox. A checker run alone never completes a candidate. A checked component never marks the surrounding theorem verified. The register owns candidate identities and a campaign's plan owns its strategy; link them rather than starting a competing ledger.

## Running a check

Pin the tool and library versions per project, in `formal/README.md`. Keep a runner script that:
1. verifies the pinned versions and a clean dependency checkout;
2. builds the targets;
3. reports what each endpoint depends on, and accepts only the tool's standard foundations, with no unfinished proofs and no custom axioms. In Lean, `#print axioms` should show only `propext`, `Classical.choice` and `Quot.sound`, and no `sorry`;
4. writes the logs, commands and source hashes outside Git.

Commit the recipe and the pins; caches and toolchains belong to the environment. Replay in the pinned environment before claiming a formal check. If no checker ran, say so.

- **One compiler owner per shared runtime.** Keep one queue of builds, with each run's source, dependency and option bindings. Source reading, review and preservation run in parallel where their files and outcomes are separate.
- **Bounded runs.** Give a diagnostic run a limit and assess a failure before extending it. Record the real outcome of the build itself apart from any wrapper's exit. Never relabel a failure or a hold as success, and never repeat a failed run unchanged to hide uncertainty.
- **Reuse before rerunning.** Start from existing receipts. Rerun only a named consumer or a missing decisive check, and record why existing evidence cannot replace it. A rerun is new dated evidence, not recovered old logs; no blanket replay of history.
- **Version moves are deliberate.** Keep the production pin. Move a named consumer to a newer version only after qualifying its dependencies there, and never chase each upstream release.
- **Compiled artifacts.** Back up a build cache worth keeping to private storage outside Git, with hashes, and verify it by a fresh download. Source and file inventories are not binary backups, and restored binaries are not a fresh compiler check.
- **Dated recipes are history.** An old recipe, branch name or schedule records its date. It is not a live queue; check the actual environment before reusing it.

## Correspondence review

Through the [review-dispatch skill](../../.agents/skills/review-dispatch/SKILL.md), a reviewer compares the literal formal statement and its hypotheses with the informal claim, line by line. Disclose placeholders and newly assumed statements, and name every residual bridge, that is, every part of the informal claim the formal statement does not reach. Say which kind of correspondence holds: to the **statement**, to the **steps of the printed proof** (a formal proof may take a different route), or **partial coverage**. While a certificate is active, freeze the informal statement it corresponds to. Any later change to that statement is compared explicitly with the certificate.

Source and semantic review, the compiler and axiom check, correspondence, preservation and presentation are separate gates; a PASS names its gate, scope and revision. Re-review the exact repair, and stop when the required findings are resolved, not after a fixed number of rounds.

## In the article

Mathematical clarity comes before verification layout (see "Polishing passes" in the [central-article guide](central-article.md)). Call a result formally verified only when the displayed statement matches the checked statement exactly; otherwise say "formally checked step". Formal evidence is mapped in the last appendix, which separates the three kinds of correspondence above. Its prominence follows the assurance it adds, not the size of the effort.

Classify each retained certificate by its role: completeness or integrality evidence, an interface to the actual objects, a narrow safeguard on conventions, or a supporting helper. Being reproducible does not earn equal prominence.

Mathematics developed during formal work that a reader should see, such as a new argument or an explicit construction, can go in a separate **mathematical supplement** beside the article. It keeps written proofs and formal checks distinct: a written argument is never relabelled formally proved because a nearby statement compiled.

## Tools

Libraries and their search tools find correspondence candidates: for Lean, Mathlib's documentation search and its `stacks` attribute, which records Stacks Project tags; Isabelle's Archive of Formal Proofs; Rocq's package index. A candidate's statement, hypotheses and axioms still need review. Community skill packs for proof assistants exist. Adopting one changes how the work runs, so agree it with the researcher first; then pin it and record what it changed. This guide installs nothing.
