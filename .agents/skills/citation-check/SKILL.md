---
name: citation-check
description: Check citations and attributions against their primary sources. Use when adding, changing, moving or auditing a citation or a credit in LaTeX or a report; when admitting a note into the article; or for a citation or wording pass that must leave the mathematics untouched.
---

# Citation check

A citation is checked at its use: the same reference can be right in one sentence and wrong in the next. Check only the uses that are new or changed, and keep the recorded checks of the unchanged ones. For a whole-document audit, check them all. Evidence goes in the task's evidence directory, `docs/reports/<task>-evidence/`.

## 1. Map the uses

Keep a **citation-use map**. Each use of a citation command gets a stable ID (`K001`, `K002`, …) that is never reused, along with its file, line, key, locator and sentence. From the project root, run:

```sh
python .agents/skills/citation-check/cite_map.py manuscript/article.tex --out docs/reports/<task>-evidence/cite-map-vN.json --previous <path of map vN-1>
```

Use `python3` or `py` where that is the interpreter's name. For a standalone note, give the note as the entry file. Omit `--previous` only for the very first map. Each map gets a new versioned name, and the extractor refuses to overwrite an existing file. Record the current map's path in status, or in the admission map's header, so the next run finds it. A map written by an older extractor format is not compared for statements; start a fresh pair.

The extractor needs only the standard library. It:
- follows `\input` and `\include`, ignores comments and handles citations that span lines;
- counts the `\cite` family, the common natbib and biblatex variants and `\citeauthor`, but not `\nocite`. Multi-citation commands such as biblatex's `\cites{a}{b}`, and `\citetitle` or `\fullcite`, are not parsed; the cross-check below catches them;
- carries IDs forward and classifies each use as **unchanged**, **changed-locator**, **changed-context**, **new** or **removed**.

File paths in the map are relative to the entry file's folder, as LaTeX resolves `\input`, and the map records only the entry's file name; record the entry's path from the project root in the report. Matching is by key, file and sentence; line numbers are only hints. Two cases show up differently from what you might expect:
- A use whose locator and sentence both changed appears as new plus removed.
- Moving a citation to another file shows the same way.

Pair these by hand and record the basis. Settle any match flagged ambiguous the same way. Leave earlier maps frozen.

Cross-check the summary's `commands` count against a literal search over the manuscript, for example `grep -rohE '[\][A-Za-z]*cite[A-Za-z]*' --include=*.tex manuscript | grep -vc nocite` (the bracket form avoids a backslash escape that some grep builds mishandle; a count of 0 while the extractor reports citation commands means the search failed). The literal search also counts commented-out commands, so explain every difference rather than expecting equality. One extractor missing a citation is the typical failure.
For citations in a Markdown report, which the extractor does not read, list each use by hand with the same fields and IDs.
*Done when* every use in scope has an ID and a class.

## 2. Check each new or changed use

Work with the primary source in hand, in the edition the bibliography names. Check four things:

1. **Existence.** The item is at that number and page. Record the printed page, the PDF page and the offset between them.
2. **Content.** The source supports what is attributed, with no stronger conclusion and no conclusion a later paper adds.
3. **Hypotheses.** They match the use: the setting, the class of objects, the direction of each map, a family versus a single object, published versus preprint numbering. Add the charter's confusable notions to this list.
4. **Attribution.** The credit goes to the right author and work.

Give each use one disposition: ADEQUATE, LOCATOR-REPAIR, ATTRIBUTION-REPAIR, MISSING-INPUT, MATERIALLY-DIFFERENT, UNRESOLVED-ACCESS or OUTSIDE-SCOPE. Report them in a per-use table in which every ID appears exactly once. The counts must add up to the scope.
When a source missing at the check arrives later, check the affected uses, change their dispositions in a new table, and run the extractor again with `--previous` into the next map version.
*Done when* the table is complete and the counts reconcile.

## 3. Trace attribution beyond the citation commands

Statement and mechanism are separate questions. Record where each newly admitted **statement** comes from, and where its proof **mechanism**, ansatz or key observation comes from: the literature, the researcher's earlier work, or this project. A new theorem can borrow a method, and an independent proof does not make a known theorem new.

**Being written here does not make a result new.** For every statement or mechanism credited to this project, record its basis: either a positioning search that found no equivalent (link its query log, as in the sources guide) or the words "novelty not claimed". A classical result reproved in passing gets its classical citation, checked like any other. Until a source is checked, record "classical; no source checked" with the lead in the report and in a LaTeX source comment beside the statement; the rendered text may call the result classical but names no unchecked source.

Credit at admission, in the article's credit list. Project-origin credit is the kind most easily lost in an integration diff, so check that earlier credits survive every edit. Add no decorative citations, and keep every project contribution even when adjacent literature exists.
*Done when* every new statement and mechanism has a recorded origin and basis, and the credit list matches.

## 4. Repairs are new claims

Write each repair sentence against the exact source statement, and prefer the smallest change. Give the reviewer the repair diff, not only the original findings. A repair that strengthens a conclusion, or moves a property from one object to another, is the characteristic defect.

## 5. A pass that leaves the mathematics untouched

For a citation, wording or layout pass, show mechanically that no mathematics changed.
- **Statement fingerprints.** `cite_map.py --previous` must report no changed, added or removed statements. It fingerprints each environment declared with `\newtheorem`, `\spnewtheorem` or `\declaretheorem`, plus the usual defaults. The fingerprint covers the environment name and the text but not the label, so changing `conjecture` to `theorem` counts as a change, and a pure relabelling is reported as relabelled. Confirm that the summary's `numbered` count equals the number of numbered statements in the PDF; starred environments and those declared with `\newtheorem*` or `numbered=no` count as unnumbered. Other numbering options (such as `numbered=unless unique`) are not detected, so explain any mismatch from them by hand. A warning that no statements were found means the gate has not run. Read each relabelled statement against its previous text as well. A relabelling combined with an edit appears as removed plus added.
- **Proof lines.** Proofs are not fingerprinted. List every changed line inside a proof, old and new.
- **PDF text.** Word-diff the extracted text and read the diff in full: `pdftotext -enc UTF-8 -layout` (from poppler, which some TeX distributions do not include), then `git diff --no-index --word-diff`.
- **Build.** The build is clean, with no undefined references or new overfull boxes. Render and view the changed pages, and record the PDF hash.

A reviewer still reads every changed line. A build or a diff never verifies mathematics, and a changed hypothesis or proof route is a proposal, not a citation repair.

## 6. Review

Send the map, the table, the attribution trace and the evidence through the [review-dispatch skill](../review-dispatch/SKILL.md). Split a large audit into lanes by source, one book or paper in hand per lane, plus one lane for versions and positioning. The reviewer checks the primary sources before opening the author's table.
