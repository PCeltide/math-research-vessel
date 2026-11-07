---
name: review-dispatch
description: Independent review of a mathematical claim, proof, repair, citation change, survey, article integration or workspace change. Use when a result needs checking before others rely on it, when a repair or reviewer suggestion has been implemented, or when reviewed parts are combined.
---

# Review dispatch

Review is independent first and reconciled second. The author freezes, the reviewer assesses, and the author disposes. Each step below is finished only when its criterion holds.

## 1. Freeze the candidate

Commit the candidate, or snapshot it with hashes (hash committed bytes with `git show <commit>:<path> | sha256sum`, since working-copy line endings vary by machine). Write a manifest of the changed or reviewed files at that commit. For an article, also record the source commit and the rendered PDF's SHA-256.
*Done when* someone else can retrieve exactly these bytes.

## 2. Write the brief

Give the reviewer:
- the startup route (AGENTS, policy, status);
- the exact candidate and manifest;
- the primary inputs (sources, earlier results, exact editions);
- the scope and the gate: what this PASS will mean;
- where the assessment goes, normally `docs/reports/<task>-evidence/`;
- the **read-only** role: the reviewer writes nothing except its own assessment file;
- the assessment form below.

Leave out the author's conversation, any persuasive summary and other reviewers' conclusions. If mandatory reading exposes the reviewer to the author's claims (status mentions the result, say), ask them to disclose it and to treat it as unverified. For source work, the reviewer reads the primary source before any author inventory. For a charter or plan, the reviewer checks that the terms and hypotheses are exact, that the inputs and their evidence states are honest, and that the proposed test answers the question at the scope promised.
*Done when* the brief stands alone: a fresh agent could do the review from it with no other context.

Use a fresh context: at least a new agent session or subagent that has not seen the author's conversation. Prefer a strong reasoning model, ideally of a different family than the author's, and record the systems used. If the host refuses worker file writes, tell the reviewer that its final message is its complete assessment. Save a brief that should outlive the session as `docs/handoffs/<task>-brief.md`.

## 3. The assessment

The reviewer returns:

> Reviewer and system; times; exact candidate; scope; sources actually checked, with spans; exposure and isolation limits; checks run, with outputs. **PASS** or **REVISE** for this scope. Findings, each with an ID, severity, blocking status, reason and the required or optional repair. Remaining limits: what this verdict does not cover.

Severity:
- **Critical:** a wrong mathematical or computational conclusion, lost evidence, a broken trust rule or a broken required check.
- **Important:** a missing guarantee that downstream work relies on.
- **Minor:** exposition, polish or nonessential coverage.

A PASS covers its stated scope only.

## 4. Preserve, then dispose

Save the complete first assessment unchanged in `docs/reports/<task>-evidence/`. If it came back as a message, store it byte for byte under a provenance header: who, scope, candidate, times, "extracted from hand-back". Never substitute a summary. Then record a disposition for every finding: fixed, with the commit; declined, with the reason; or out of scope, with where it went.
*Done when* every finding ID has a disposition and the original assessment is untouched.

## 5. Delta review

Each implemented repair is a new claim, and wording the reviewer suggested counts too. Send the exact diff range back, preferably to the same reviewer. Each delta verdict is its own preserved report. Broaden the review when the repair changes dependencies or structure. A correction to a review is made by addendum, never by editing it.
*Done when* the final bytes, every byte, are covered by a PASS at the needed scope.

## Separate gates

Separate gates do not cover each other: mathematical or source fidelity, citation (the [citation-check skill](../citation-check/SKILL.md)), editorial or full-PDF review (the central-article guide), computational replay, formal correspondence. Combining reviewed parts makes a new candidate, which gets its own integration review. An unchanged component keeps its evidence only after an identity check. If no independent reviewer is available, the gate stays open; say so.
