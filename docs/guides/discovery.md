# Discovery

Discovery tools find **leads**: candidate theorems, papers, definitions and dependency routes. A lead becomes evidence only after the primary source is read and the use is checked (see the [sources guide](sources.md) and the [citation-check skill](../../.agents/skills/citation-check/SKILL.md)). A tool's metadata can be wrong too: years, titles and numbering are verified against the source itself.

## Theorem search

[TheoremSearch](https://www.theoremsearch.com) searches theorem statements semantically across arXiv and other corpora. The bundled helper needs no account:

```sh
python tools/theorem_search.py "statement or mechanism in words" --limit 5 --out docs/reports/<task>-evidence/search-<topic>.json
```

- Search by mechanism, equivalent statement and example, not only by the project's own phrasing. Paraphrase the hypotheses the way other authors would write them.
- Save the raw JSON for each search that informs a report. Add it to the survey's query log with the date, the query and which hits were read.
- If a host blocks the service, record it and use the other routes below. An unreachable service is a limit of the search, not a finding.

## Other routes

Pick the ones that fit the field, and log every query:
- **Literature indexes:** zbMATH Open, MathSciNet, arXiv listings and citation search, Google Scholar.
- **Reference works and databases:** the Stacks Project (cite by tag), nLab, the DLMF, the LMFDB, the OEIS, the House of Graphs, the Atlas of Finite Groups. Archive a web page you rely on as a dated snapshot.
- **Formal libraries:** for example Mathlib or the Archive of Formal Proofs. Matches are correspondence candidates whose statements, hypotheses and axioms still need review (see the [formal-verification guide](formal.md)).

Note rate limits and failed searches.

## Mapping the project's own results

As the project grows, a map of its own statements, dependencies and citations helps with routing and auditability. It can be a hand-kept table or a tool that builds a graph:
- Declare which files the map covers. Files outside it are not covered.
- Refresh it when its inputs change, and pin the version of any tool. Record the version with any research that depends on a query.
- Before using a tool's output, read its diagnostics, coverage, currency and truncation. Save the exact output bytes when they are evidence.
- A connected map is not a checked proof. An authored reference is not automatically a prerequisite. An absent edge or an empty search shows only a limit of the map.

A problem with a tool goes to the tool's maintainers as feedback; it is never patched into the research record. Keep literal search for literal text. This guide installs no mapping tool.
