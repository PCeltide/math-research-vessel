# Workflow

The [policy](../collaboration.md) owns authority and evidence; this guide says how the work runs. Use the sections a task needs. Ordinary discussion needs no task file. Create a directory only when a real record goes in it.

Where things live, once they exist:
- `docs/plans/<task>.md`: assignment plans;
- `docs/reports/<task>.md`: the canonical report, with `docs/reports/<task>-evidence/` for maps, outputs and reviews (`review-1.md`, `review-1-delta.md`, …);
- `docs/handoffs/<task>.md`: stop handoffs, and `docs/handoffs/<task>-brief.md` for a dispatch brief;
- `notes/<task>.tex`: developed proofs before admission to the article;
- `scripts/`: computations; `sources/`: the source inventory (see the sources guide); `formal/`: formal work;
- `docs/ledger.md` and `docs/context/status-history.md`: created on first use.

Scale the records to the work. A short result can have a report of a few paragraphs and a handoff whose headings mostly say "none"; what matters is that every claim's state and every open item is written down.

The lifecycle: **foundation**, then **assignments** (research or audit), each ending in a **result** and its **review**. Reviewed results enter the **article** (see the [central-article guide](central-article.md)). Open directions live on the **ledger**. Every real stop ends in **preservation** and a **handoff**. A small one-off question needs none of this; answer it and say how far it was checked.

## Foundation

The researcher's request to fill in the charter launches foundation; it needs no separate plan file. It is done when the [charter](../project-charter.md) has no blank that the first investigation depends on, and a bounded first assignment is drafted for the researcher to launch.

1. Record the question, why it matters, the reader and the existing work. Clarify any ambiguity that changes the answer before inventing a theorem.
2. Fix the definitions, quantifiers, setting, hypotheses and exclusions. Start the confusable-notions list.
3. List the accepted inputs with exact sources and evidence states, and the premises still open. Mark each source as available, read or checked in application, or as a pointer not yet obtained (see the [sources guide](sources.md)).
4. **Calibrate.** Fill in the People section of the charter. If the researcher supplies earlier writing, run the calibration in the [writing guide](mathematical-writing.md#calibrate-to-the-researcher).
5. Record in the charter which optional tools the work uses (the article, computation, formal verification, discovery) and why, and whether timeboxing is on.
6. Propose the first decisive test, with ownership, a stopping condition and the review it needs. A boundary case, a known reconstruction, a precise ambiguity or a source blocker can be the right answer. A finite sample does not prove a universal statement.
7. Have the charter and proposal reviewed when the first investigation is substantial (see [review dispatch](../../.agents/skills/review-dispatch/SKILL.md)). The researcher may waive this review; record "charter unreviewed" in status. The researcher then decides whether to launch.

## Audit

Use audit mode when existing mathematics, such as a thesis, a draft or an earlier result, becomes a foundation. It is done when every inventoried item has a locator, an outcome and its evidence.

- Inventory every definition, assertion, proof and substantive prose inference in the assigned span, including implicit steps, boundary cases and changes of notation.
- Give each item one outcome: **accounted for**, **needs repair** or **unresolved**. Distinguish a correct but compressed argument (an exposition repair) from an invalid inference and from a statement that needs stronger hypotheses.
- Check each cited result against its actual statement, and map every hypothesis to the present use. Inspect its proof when the application, its interpretation or a suspected issue requires it. Record the background accepted as input rather than re-proving all prerequisites.
- Preserve the original unchanged. Develop repairs in a separate working copy, and show each repair beside the original.
- Report an examination finished with gaps as an audit with open issues. A span becomes a usable foundation only when every load-bearing issue is resolved or declared as an assumption that dependents carry.

## Assignment

Save each substantive task as `docs/plans/<task>.md`, or link an approved contract. Preparing a plan is not launching it: the researcher's instruction launches it. The plan records:

- **Authority:** who launched it, and when.
- **Deliverable and decisive test:** the recommended target, the alternatives considered with the reason each was deferred, a **legitimate partial endpoint** and **what would not count** (for example, a failed finite search is not nonexistence).
- **Inputs:** exact revisions and sections, each with the reason it is read.
- **Scope:** what is included, what is excluded, and the owned output paths, including caches.
- **Gates:** the checks and reviews required, and where evidence goes.
- **Effort bound:** what limits the work, such as a number of routes or attempts, a scope, or a review gate. When the charter turns timeboxing on, this is a wall-clock timebox (see below).
- **Stop:** the stopping condition, and who decides the next step.

**Keep going while a path is open.** An assignment stops only when the researcher asks, the stopping condition is met, the effort bound is used up, no justified in-scope route remains (record the obstruction), or the next step needs the researcher or is blocked from outside (an approval, a scope change, a reserved decision, a denial, a missing input or tool). A likely compaction pauses work for a handoff; it does not end the assignment. Reaching a checkpoint, finishing a subtask, a natural pause or a long session is none of these. If a clear next step lies inside scope and the bound, take it; checkpoint as you go. Before stopping, list the open in-scope paths and say which of these reasons ends each one. A stop handoff that names an in-scope next step, within the bound and needing no one else, that the agent could have taken itself was premature.

Every dispatch to a worker names the AGENTS.md startup route plus its extra inputs. Every report records the files read and their revisions.

## Optional: timeboxing

When the charter turns timeboxing on, each plan also records a start time and timezone, a production gate, and a ceiling that includes startup, with the final share protected for review and preservation.

Measure in wall time. Compaction, a change of route and a resume prompt never reset it. When an outside interruption blocks all work (a usage limit, an outage), record its span and cause and extend every later gate and the ceiling by it; then resume the active phase at full scope. Time spent on partial blockers, waiting and review all counts. Minute precision is enough. At the production gate, stop new production and move to review and preservation. At the ceiling, preserve an honest partial result. Stop early when the deliverable is checked: the ceiling is a bound, not a quota.

## Result

Keep one canonical report per assignment at `docs/reports/<task>.md`, updated in place, with evidence in `<task>-evidence/` only as needed. Use these headings:

1. **Outcome:** the result in a few sentences, with its status; the author or agent, the date, the branch and the content commit the claims are about (a report cannot name the commit that contains it; for uncommitted work, file hashes).
2. **Question and hypotheses:** the exact statements, quantifiers and setting.
3. **Argument and evidence:** a link to the canonical proof; a short derivation where it makes the report readable; computations and checks with their outputs; source uses with locators, hypotheses and read spans. Keep author checks, independent review, computation, formal checks and the researcher's reading apart. State gaps, failed checks, contradictory evidence and skipped work plainly.
4. **What downstream can rely on:** the conclusions, their hypotheses, evidence states and revision; what remains conditional; and what is explicitly not claimed.
5. **Attempts worth retaining:** failed routes, counterexamples and obstructions, with the conditions for reopening each.
6. **Candidates for formal checking:** the useful candidates, or "none identified" (only when formal verification is in use).
7. **Review and handoff:** links to the complete reviews and the preservation receipt.

A developed proof lives once, in LaTeX: in `notes/<task>.tex` until it is admitted to the article. Start the note from a copy of `templates/standalone-note.tex`, or from any LaTeX file that follows the writing guide. Reports link to it. A message that changes a claim is reflected in the report before the assignment closes. A superseded claim stays recoverable through Git but is never shown as current.

## Test a claim

Before asking for independent review, try to break the claim yourself, and record what you tried in the report:
- check the smallest and degenerate cases, and the boundary of each hypothesis;
- drop each hypothesis in turn and look for an example showing it is needed. Record whether it is shown necessary, used only by this proof, or of unknown necessity. Failing to find an example does not license dropping it: that is a mathematical change, a proposal for the researcher;
- search for counterexamples, by hand or by computation, and state the search's coverage;
- test against known special cases and results in the literature;
- recompute any constant, sign or index by a second route.

Passing these tests is author evidence, not review. A counterexample found here is a result too: record it under attempts worth retaining.

## Ledger

Keep open directions, optional improvements and parked questions in `docs/ledger.md` once there is more than one. Each row has a stable ID that is never reused: the exact source or claim, the benefit, the decisive first check, dependencies, effort and risk, the disposition with its date, and links. Dispositions: open, active, completed, parked, or retained with a reason. A single short pass may keep its dispositions in a table in its report; ledger rows are for items that outlive the pass. The ledger records; it authorizes nothing. Proof gaps belong in the report and status, not here. A direction found in the literature is labelled preliminary until it is checked.

## Review

Run review through the [review-dispatch skill](../../.agents/skills/review-dispatch/SKILL.md): freeze the candidate, brief a fresh reviewer, preserve the complete first assessment, dispose of every finding, and send each repair back as a delta. For citation work, use the [citation-check skill](../../.agents/skills/citation-check/SKILL.md) first.

## Preservation

At checkpoints and real stops:

1. Run the relevant checks, and inspect every path and its metadata against the destination's rights and privacy.
2. Commit with a message that says what changed, why, what was checked and what is open. An agent sets its own identity for that one command, for example `git -c user.name="<agent>" -c user.email="<agent's address>" commit`, and adds any trailers its harness specifies.
3. Push with an ordinary push to the remote the charter names, if agents may push, then compare `git ls-remote` with the intended commit and read back the files that matter at that commit. If the remote has advanced, inspect it and keep the competing work. Preserve a large packet in small, disjoint batches, verifying each before the next.
4. Outside Git, transfer an identified snapshot and its manifest, retrieve it separately and compare hashes.
5. If there is no remote yet, or a transfer fails or is refused, the work is preserved locally only. Record the exact action, its target, the reason, whether it was denied, is pending or is uncertain, and what still lacks a remote copy. Surface it at each handoff until it is resolved. Tell a transport error or a cancellation apart from a denial, and check an uncertain outcome before retrying. Batching is a normal method, not a response to a denial. A denial means stop and ask: never retry in smaller pieces, by another route or with changed credentials, and never change a repository's visibility to get around it.

A record cannot contain its own commit SHA. Name the parent commit instead, or record the SHA afterwards in status or the next commit. Status names the last content commit; commits after it that only add records are expected. A dated record describes its own date: "pending" or "local only" in an old report is not the current state.

When a record gives a file's hash, hash the committed bytes, `git show <commit>:<path> | sha256sum`. Git stores text with LF line endings (see `.gitattributes`), so a warning that CRLF will be replaced by LF is expected on Windows.

Keep few active branches: one per line of work, plus one for each concurrent writer. Before any cleanup, including removing a finished branch, verify ownership, that the required work is included and durably preserved, that nothing depends on it, and that heads are unchanged. Keep any evidence you are unsure about.

## Handoff and stop

At a real stop, the end of an assignment, a stop requested by the researcher, or a likely compaction, write a handoff with the [handoff skill](../../.agents/skills/handoff/SKILL.md) and link it from status. Use the same skill when resuming, and when passing work to or from a worker or reviewer.

When formal verification is in use, the stop also records the session's formal candidates, or "none identified", in `formal/CANDIDATES.md`. A prepared prompt does not execute itself. Move finished status entries verbatim to `docs/context/status-history.md` with a one-line pointer.
