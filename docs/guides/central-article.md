# The central article

The project maintains one **central article**, the canonical exposition of its reviewed results. Reports feed it, and it is the account a reader follows. Read this guide, the [writing guide](mathematical-writing.md) and the article's [narrative companion](../../manuscript/article/NARRATIVE.md) before editing, admitting into, restructuring or reviewing the article.

"Central article" names a role. It does not certify readiness for publication or the researcher's acceptance. Maintenance happens inside authorized assignments; this guide creates no recurring task.

## One canonical account

Once a result is admitted, the article holds its canonical proof. Earlier standalone notes and audit PDFs remain frozen records with their original review identities, so there are never two live copies of one proof. A later correction updates the article and a dated report. When it changes an earlier claim's validity, put a superseding pointer in status and in the affected report.

## The narrative companion

`manuscript/article/NARRATIVE.md` owns the story:
- the central question and its present answer;
- the reader;
- the contribution in a few connected steps;
- the reading order (movement, what the reader gains, why it belongs there);
- emphasis and restraint;
- the credit list.

The charter keeps the intended reader, and the policy keeps the evidence rules; the narrative changes as results change the story.

Before adding a result, answer three questions in the integration report (an "Integration" section of the result's report, or `docs/reports/<task>-integration.md` when several results are admitted together):
1. Which sentence of the central answer changes?
2. Which reader question does the result resolve?
3. Does it replace, strengthen or merely support an existing passage?

When the answer changes the emphasis or order, revise NARRATIVE.md **first**. Review it as an editorial artifact: is the contribution clear, the emphasis proportionate, the order right for a new reader? Then implement and check the article against it. Git holds the history; the narrative carries no chronology.

## Admission

A result enters only when its statement, its proof and its load-bearing source uses have a recorded independent mathematical review, with no unresolved required finding at the scope used. Its dependencies meet the same bar, or are accepted standard results with checked hypotheses. A conditional proof never admits an unconditional claim.

Keep an **admission map** at `manuscript/article/admission-map.md` from the first admission. Each row gives the article label, the originating report and label, the source revision, the review identity, the external sources, the changes made during integration and the integration review. Include substantive prose consequences, not only numbered theorems. Reviewed inherited mathematics is ready for drafting, but rewritten statements, combinations and new proofs need fresh review: a PASS never transfers to new bytes.

A new claim noticed while editing goes to a bounded research record first. It is never promoted to a theorem in place. Run the [citation-check skill](../../.agents/skills/citation-check/SKILL.md) on every admission: its citations are rechecked in their new wording, and the origin of each statement and mechanism is credited now.

## What the rendered article contains

- **Theorems** are proved results only. Open questions belong in a short closing section that delimits the theorems or names a concrete next problem. A speculative table never carries the status of a result.
- Failed routes, audit chronology, task IDs and unfinished formalization stay out of the rendered text; a LaTeX source comment beside a claim can carry its review record.
- **Essential project proofs** are written inside the article and cross-referenced internally. They are never delegated to private notes or replaced by self-citations to earlier versions.
- **Citations** use one numbered bibliography with exact theorem, section or page locators at the point of use. Prefer the checked published edition; otherwise say which version the locators follow.
- **Authorship and submission metadata** stay blank until the researcher settles them. Never render placeholder metadata as fact.

## Structure

- **Audience:** write for a specialist in the area who has not followed the project. Give the question, the main results and the mechanism early, and introduce machinery when it first solves a visible problem. Use article sections.
- **Introduction:** give it a hierarchy. Foreground the few headline results, and place supporting results at their natural locations, with pointers from the introduction.
- **Contribution:** present it in a few connected steps, such as construct, contrast, conclude. Reach the destination once, after all its inputs are in place. Complete both sides of a contrast before interpreting it.
- **Shared inputs:** state them once, early, at their first use. Keep distinct mechanisms local; never merge proofs just to look uniform.
- **Prior literature:** compare after the positive results and their mechanism. State the exact clauses that change and what replaces them, and let no catalogue of corrections become the paper's identity. Describe what is established, without asserting priority. A classical result proved along the way gets a checked citation, or, until one is found, a LaTeX source comment and report entry reading "classical; no source checked" (see the citation-check skill, §3); the rendered text never names an unchecked source. "We prove" is not "we discover".
- **Appendices** are sub-stories. Each opens with a question or obstruction left visible in the main text, develops the answer, and closes by making its consequence for the paper plain; each keeps its own rhythm. Order them by mathematical role and dependency, never by date added.
- **Verification** is always the last appendix, a scan-first evidence map:
  - an overview table;
  - headings tied to article results;
  - short lists of checked obligations;
  - a labelled boundary of the input that was not checked formally or computationally;
  - a separate table for computations.

  Scale this to the evidence: with only one or two computations, a single table suffices. Distinguish computations used in a proof, independent corroboration and exploratory searches. For formal evidence, separate full from partial statement correspondence, and both from correspondence to the printed proof's steps (see the [formal guide](formal.md#correspondence-review)).
- **A mathematical supplement** may sit beside the article, under this guide's admission and review rules; the [formal guide](formal.md#in-the-article) says what it holds.

## Polishing passes

Polishing runs as a bounded assignment. A short pass keeps a disposition table in its integration report; items that outlive the pass become ledger rows. Each item records the exact passage, the reader benefit, the proposed change, its effort and risk, and its decision with the review. The trimming rules in the [writing guide](mathematical-writing.md#trim-without-losing-precision) apply. In addition:

- **Clarity before verification layout.** Mathematics decides a proof's structure. Verification markers only describe their exact scope, and a proof must read fluently with the markers ignored. Never fragment a good proof to fit coverage; use a scoped note and a link to the appendix. Place markers sparingly, at natural boundaries, with no quota.
- **Label verification exactly.** "Formally verified lemma" (or "Lean-verified", naming the tool) means the whole displayed statement, quantifiers and hypotheses match the checked declaration. Anything narrower is a "formally checked step". Surrounding text never inherits verification by proximity.
- **Retained with reason.** A choice not to change something is a disposition, with its reason recorded.
- **Finish.** A finished campaign stops. A stable reading edition is worth more than continual polish.

## Review: two tracks

Every substantive integration passes two separate tracks through the [review-dispatch skill](../../.agents/skills/review-dispatch/SKILL.md). A readable article can still be wrong, and a correct one can still need substantial editorial work.

1. **Mathematical and source review:** every statement and substantive inference, completeness of dependencies, hypotheses, and citation applications.
2. **Editorial review:** on the exact frozen bytes, after track 1 passes. Read the abstract and introduction against the actual theorems and follow the narrative without the audit conversation. Check notation and transitions. Inspect **every rendered page** of an independent rebuild. Record the page count, warnings and the PDF hash.

A pass meant to leave the mathematics untouched uses the mechanical gate in the [citation-check skill](../../.agents/skills/citation-check/SKILL.md#5-a-pass-that-leaves-the-mathematics-untouched) in place of a full re-review of unchanged material. Rebuild after the last edit, and verify that the final PDF corresponds to the reviewed source.

## Build

Build from `manuscript/`, with outputs in the ignored `build/` folder or outside the repository:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=../build article.tex
```

The templates need a standard TeX distribution with amsart, TikZ and tikz-cd (TeX Live, MacTeX or MiKTeX). Record the TeX distribution and version. Copy the PDF into the repository only after confirming the source identity. Check for undefined references, overfull boxes, clipped displays and unsupported characters. A clean build proves typesetting, not mathematics. If `microtype` font expansion fails with the local fonts, disable expansion. Compile preserved originals only in separate copies.

## Files and templates

- `manuscript/article.tex` is the driver.
- `manuscript/article/preamble.tex`, `sections/` and `bibliography.tex` hold the content.
- `templates/standalone-note.tex` is for single-file notes, such as an audit or a result before admission.

The default layout is amsart at 11pt in a full-page text block, with a restrained theorem hierarchy on one counter, equation numbering by section, coloured links and TikZ. Adapt the section names to the actual argument, and keep subject macros out of the preamble until the mathematics needs them.

To use your own template or a journal's class, put an unchanged copy under `templates/` and note its origin, date and SHA-256 in `templates/README.md`. Build the article from a copy, and record the choice in the charter. The rules in this guide still apply: they say what the article must do, not how it must look.
