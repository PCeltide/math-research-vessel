# Writing mathematics

Read this before drafting, revising or reviewing any mathematical exposition. The researcher's stated preferences, recorded in the [charter](../project-charter.md#people), refine it. Where the two differ, the charter wins.

## Write for a reader following an argument

A reader should always know what question is being answered, why the next definition or lemma is needed, and how the conclusion follows. Give the direction of a proof before its details. Thoroughness means enough reasoning to reconstruct the argument; it does not mean saying the same thing several ways.

- Open each section with its **purpose** and the hypotheses in force.
- Introduce an object when its role becomes visible.
- Before a substantial lemma, say what difficulty it removes. After using it, say what is settled and what remains.
- In a transition, name the concrete use of what comes next ("To bound the exceptional configuration, …"). That is more informative than calling a result "crucial" or "important".
- Give a long proof a roadmap. Keep short proofs short.
- Organize the text by mathematical dependence. The chronology of the investigation, its corrections and failed routes belongs in reports, not in the exposition.

## Before drafting a claim

Write the exact target. Fix the setting, the quantifiers and the hypotheses the argument actually uses: the base field, ring or space, the class of objects allowed, where each object lives, the hypotheses on each map, and any regularity, finiteness or convergence assumption. These are prompts for inspection; do not add them automatically. A theorem for compact spaces does not gain an application to noncompact ones by dropping the word "compact".

Keep three things apart in the supporting report: the claim, with its quantifiers and hypotheses; the proof or evidence available now; and the unproved obligations, with what depends on them. If only $L\Rightarrow T$ is proved, write the conditional and name $L$. A speculative claim never appears as an ordinary theorem.

## Statements, notation and references

- State a result with the hypotheses needed to apply it: the direction of each implication, any exceptional case, and whether it asserts existence, nonexistence, uniqueness or classification. The wording is never stronger than the proof.
- Every symbol earns its place. Prefer a descriptive phrase to a symbol used once. Introduce each symbol before using it. Keep a source's notation where it stays clear, and explain any change. Give each map its domain and codomain. Keep changes of setting explicit, such as restriction, extension of scalars, passage to a quotient or a dual; never move an object between settings silently.
- Give results stable descriptive labels so dependencies stay legible. A macro earns its place by fixing a repeated mathematical object, not by saving keystrokes.
- At each external invocation, cite the precise theorem or span and say why its hypotheses hold here (see the [citation-check skill](../../.agents/skills/citation-check/SKILL.md)). A search snippet or a remembered theorem name is a lead for retrieval, not evidence.
- Keep each item on the charter's confusable-notions list distinct in every statement.

## Make every warrant visible

For a long argument, start with the **mechanism**: what is reduced to what, which result does the main work, and where a special hypothesis enters. Then give the steps in dependency order.

At each substantial step, name its warrant: the theorem, calculation, estimate, identification or construction that justifies it, and where each hypothesis is used. Routine algebra may be compressed when a reader can reconstruct it. A change of hypothesis is always shown. "Clearly" and "standard" are not warrants. For an exact sequence or a chain of estimates, identify each object or term and what links it to the next. For a diagram, label its maps and state the property the argument needs; a diagram illustrates a claim, it does not prove it. Treat a formula as part of a sentence, with punctuation and a stated role. End a proof by naming what it established, especially after cases or reductions.

## Trim without losing precision

Shorter is better only when the hypotheses, the attribution and the reasoning a reader needs all survive.

- **Cut freely:** repeated statements of outcomes, research-history transitions, a second summary of a short proof, disclaimers repeated paragraph after paragraph.
- **Cut cautiously:** proof steps. Background may be compressed into a precise citation. A project-specific step is never replaced by "standard" or by a pointer to private notes.
- **Extract** a shared lemma only when it improves its real applications without needless generality. Keep each application's own hypothesis checks. Where two proofs differ in substance, keep both and record why.
- **No length targets.** Length alone is neither a reason to add nor a reason to cut. A longer passage earns its space by making an argument inspectable.
- **Close each suggestion.** Every suggested improvement ends as implemented, or as retained with a written reason. A finished polishing pass stops; further polish answers a concrete reading difficulty or a request from the researcher.

## Repairs

Distinguish three kinds of repair:
- **exposition:** the same claim and argument, with missing explanation supplied;
- **justification:** a step newly supported by an argument or a correctly matched reference;
- **mathematical change:** a different hypothesis, conclusion or proof route.

A mathematical change is a proposal for the researcher, shown with its effect on dependents; a weakened theorem is never hidden under smoother prose. For an invalid step, quote only the necessary passage, explain the failure and give the replacement or the open obligation. For a valid but compressed step, say what was filled in without calling it an error. Write repairs in a working copy; the original stays unchanged.

## Where writing lives

Developed proofs, reusable diagrams and the article are written in LaTeX. Reports, audits, handoffs and learning notes are written in Markdown with LaTeX mathematics. Define any macros a report uses within it. There is one canonical proof; reports link to it with exact locators and a revision, never "see above". Use repository-relative links, and pair important locators with a commit or a source hash. Learning exchanges stay in conversation or in separate notes, not in the manuscript. Keep agent bookkeeping, task IDs and audit chronology out of the rendered mathematics; a LaTeX source comment can carry provenance unseen.

## A final pass before sharing

Read the draft five times, each with one question:
1. **Narrative.** Following only the sequence of statements, can a reader tell what each result contributes?
2. **Evidence.** Does every assertion have its evidence, and does every application meet its hypotheses?
3. **Precision.** Are the notation, quantifiers, exceptional cases, references and open conditions right?
4. **Rendering.** Is the rendered mathematics clear: no broken references, clipped displays or unclear diagrams?
5. **Record.** Does the report name the actual revision and checks, and has every changed dependency been revisited?

Author checks passing is not acceptance. Independent review and the researcher's response are recorded separately.

## Calibrate to the researcher

When the researcher supplies earlier writing, such as a thesis, papers or notes, calibrate before writing at length:
1. Read the whole corpus for narrative and style: motivation, the order of definitions and results, notation, transitions, the level of proof detail, rhythm. This is not a mathematical audit.
2. Record the **observed habits** with exact locators, kept separate from your **recommendations**.
3. Write a short calibration passage in that voice and ask for the researcher's reaction.
4. Record their feedback, and the guidance it settles, in the charter's People section.

The calibration stays revisable. One accepted passage sets a direction, not a permanent rule, and no habit becomes a rule merely because it occurred.

Reference articles can also calibrate exposition. Identify what a technique does for the reader, such as motivating a definition, staging dependencies or making a proof inspectable. Distinguish that lesson from the reference's subject, maturity, length and section hierarchy. Adopt only what serves the present question and audience; a polished paper's architecture and an individual writer's habits do not become universal requirements.

Amended 2026-11-09 at the researcher's request: make reference-based calibration useful across subjects and stages without importing a finished article's architecture.
