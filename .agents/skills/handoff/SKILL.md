---
name: handoff
description: Write or receive a handoff for mathematical research work. Use when pausing or stopping, before a likely compaction, when resuming from an earlier session, and when passing work to or from a worker or reviewer.
---

# Handoff

A handoff lets a fresh agent, or the researcher, continue without the conversation that produced the work. It records state and points to the records that hold the substance; it never replaces them. One form serves every transition, so the next reader always knows where to look.

## 1. Pick the kind

- **Stop:** a pause, the end of an assignment, a stop the researcher asked for, or a likely compaction. Write `docs/handoffs/<task>.md` and link it from status.
- **Dispatch:** sending work to a worker or reviewer. The handoff is the brief; for a review, write it through the [review-dispatch skill](../review-dispatch/SKILL.md), which adds the reviewer's rules.
- **Hand-back:** a worker's or reviewer's return. It is their report, preserved as the review-dispatch skill says; add only a provenance header.
- **Resume:** picking up someone else's handoff. Go to step 4.

*Done when* you know which file you are writing or reading.

## 2. Write it

Under these headings, in this order. Link to reports, proofs, plans and commits by path and revision rather than copying them.

1. **Task and authority:** the exact task, who launched it and when, and what it authorizes. A prepared prompt authorizes nothing until the researcher sends it.
2. **Claims and their evidence states:** each claim the work touches, with its exact statement or a locator for it, and its state: proposed, author-checked, independently reviewed, computed, formally checked, researcher-accepted. Keep a conditional claim conditional, and name the premise.
3. **Open premises and findings:** unresolved premises, open review findings and known gaps, each with what depends on it.
4. **Identities:** the source editions, the candidate and review identities, and the branch and exact commit (or file hashes, if uncommitted). Copy the branch and commit from `git branch --show-current` and `git rev-parse HEAD`, never from memory; if the branch comes back empty, HEAD is detached, so write "detached at <commit>".
5. **Owned files and dirty work:** what this work owns, what is uncommitted or unpushed, and what others are working on that must stay intact.
6. **Bound:** the effort bound and how much of it is used, the stopping condition and how close the work is to it. If timeboxing is on, also the start, the gates, any excluded spans and the time remaining.
7. **Preservation:** the last pushed commit and its remote readback evidence; or "local only" with the reason (no remote yet or push not allowed); or "preservation blocked; close-out incomplete" with the blocker.
8. **Decisions pending with the researcher:** each one, phrased so it can be answered.
9. **Next prompt:** one concrete prompt, with its required reading (the startup files, then the named inputs) and the guides and skills it should use.

Keep secrets, credentials, personal data and private source text out of it.
*Done when* someone with only the repository could continue: every heading is filled or says "none", and every claim has a state.

## 3. Check and save it

For a stop, first run the workflow's [Preservation](../../../docs/guides/workflow.md#preservation) and [Handoff and stop](../../../docs/guides/workflow.md#handoff-and-stop) sections: the privacy check, commit, push, remote comparison and readback, the formal candidates when formal verification is in use, and moving finished status entries to the history file.

Then reread the handoff against the actual repository: the commits exist and are pushed, the files are where it says, and status points to it. A record cannot contain its own commit SHA; name the parent commit, or record the SHA in status afterwards.
*Done when* the preservation steps are done, the handoff is committed, and status links it.

## 4. Resume from one

1. Do the startup reading in AGENTS.md first. A handoff never replaces it.
2. Read the handoff, then check it against the repository: the branch, the commits, the remote, the dirty files and the claimed evidence states. On facts of state, such as which commits, files and branches exist, the actual repository wins over the handoff and status. A disagreement about authority or a claim's evidence state follows the policy's conflict rule: name both records, continue the unaffected work and ask the researcher. Record every discrepancy.
3. Confirm that the authority still holds. A handoff does not extend permission or reset an effort bound or timebox.
4. Continue with its next prompt, or report why it no longer applies.

*Done when* the discrepancies are recorded and the next action is under way or reported as blocked.
