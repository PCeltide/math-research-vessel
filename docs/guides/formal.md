# Formal verification

A proof assistant such as Lean, Rocq (formerly Coq), Isabelle or Agda, or a checked certificate from a SAT or SMT solver, adds **selective** assurance to the obligations where it is worth the most. It is not a badge for every lemma. A checker run establishes a statement in a pinned environment. Whether that statement says what the mathematics says is a separate question, settled by an independent correspondence review.

## Choosing what to formalize

Formalize where the check adds substantial assurance: completeness of a case analysis, a subtle reduction, an exact correspondence, a calculation too large to inspect. Skip mathematics that is checkable by inspection, and do not count universal quantification or many declarations as value in themselves. Reject a **proxy**, such as a check of one sampled parameter, a single invariant standing in for the full statement, or a certificate for one final step: the result would look like assurance without giving it. Existing valid evidence is preserved even when its marginal value is modest.

Each candidate passes a **feasibility gate** before full work. Check early whether the prerequisites exist in the tool's library (for Lean, Mathlib) or in the project. When the real cost is building a general theory the library lacks, stop and bring a scoped proposal to the researcher. There is no lemma quota, and no whole-document formalization.

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

Recording a candidate authorizes nothing and extends no timebox. A checker run alone never completes a candidate. A checked component never marks the surrounding theorem verified.

## Running a check

Pin the tool and library versions per project, in `formal/README.md`. Keep a runner script that:
1. verifies the pinned versions and a clean dependency checkout;
2. builds the targets;
3. reports what each endpoint depends on, and accepts only the tool's standard foundations, with no unfinished proofs and no custom axioms. In Lean, `#print axioms` should show only `propext`, `Classical.choice` and `Quot.sound`, and no `sorry`;
4. writes the logs, commands and source hashes outside Git.

Commit the recipe and the pins; caches and toolchains belong to the environment. Replay in the pinned environment before claiming a formal check. If no checker ran, say so.

## Correspondence review

Through the [review-dispatch skill](../../.agents/skills/review-dispatch/SKILL.md), a reviewer compares the literal formal statement and its hypotheses with the informal claim, line by line. Disclose placeholders and newly assumed statements, and name every residual bridge, that is, every part of the informal claim the formal statement does not reach. While a certificate is active, freeze the informal statement it corresponds to. Any later change to that statement is compared explicitly with the certificate.

## In the article

Mathematical clarity comes before verification layout (see "Polishing passes" in the [central-article guide](central-article.md)). Call a result formally verified only when the displayed statement matches the checked statement exactly; otherwise say "formally checked step". Formal evidence is mapped in the last appendix. Its prominence follows the assurance it adds, not the size of the effort.

## Tools

Libraries and their search tools find correspondence candidates: for Lean, Mathlib's documentation search and its `stacks` attribute, which records Stacks Project tags; Isabelle's Archive of Formal Proofs; Rocq's package index. A candidate's statement, hypotheses and axioms still need review. Community skill packs for proof assistants exist. Adopting one changes how the work runs, so agree it with the researcher first; then pin it and record what it changed. This guide installs nothing.
