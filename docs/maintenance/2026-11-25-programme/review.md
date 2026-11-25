# Independent review of the research programme guidance

**REVISE.** The new programme guide preserves launch, review and acceptance authority. One instruction in the article template assumes a kind of result that the existing guides explicitly allow a project to lack.

OpenAI Codex reviewed this candidate in a fresh, separately dispatched context on 2026-11-25, with checks completed at 13:41 UTC. The candidate commit identifies OpenAI Codex as its author. The reviewer received the review brief and commit range, read the template and worked from the frozen Git objects in the shared checkout. The reviewer had no author discussion or other verdict. This was a same-system review.

## Scope and identities

The gate covers the reusable guidance, its continuity with the existing workflow, research and editorial authority, internal links, and privacy of the release diff. Base `e2d6a3b2fe916688495e3ef177466054b57b3cb0`. Candidate `1af565051038938e3c3771c8be2a8e2b7445cfc8`. `git diff --raw --no-abbrev e2d6a3b 1af5650` returned this manifest.

```text
:100644 100644 6332232535cb93512f6fc34798bcaf3d78f98dc2 8432f475505d26c4aaed60e44527d6ac9c1a7fec M	AGENTS.md
:100644 100644 d79c62ae267c08672fa585ba07ca4cf7ab56627b cc0bbe63987302fa24d12e0f3b2966012549bbde M	README.md
:100644 100644 ed3e197795e7c1b4eca56ee229f353b55c1d0cdb 5c18917d5acab6788ba53ecf00c0132c7233db32 M	docs/guides/central-article.md
:100644 100644 cd4fb848a3adc016bbd9325e1f7aebc46d9f3eae 3aa5ada24e1d83d1f51f899f5d5e15f7604d97a5 M	docs/guides/computation.md
:100644 100644 afc3815a7e7bb09fb4ae9b86f9d8c6ab717342c2 61f5b0f174d4543d5940af32d69f837c9974e81a M	docs/guides/discovery.md
:000000 100644 0000000000000000000000000000000000000000 1b935063d8323e7e04b2d5b09e344eec173541ac A	docs/guides/research-programme.md
:100644 100644 8a8dbed5b7a296f648c3e03ef0614ec2786f6007 05a947682185bf7854a62378a26db0623992bfc3 M	docs/guides/workflow.md
:100644 100644 b38633b70ce0cb5e1161ba95e0a029a01637df0d 632bae7d1bd54e06430c2d384b4672896de9818e M	manuscript/article/NARRATIVE.md
```

## Checks and evidence

- Read the entire patch with `git diff e2d6a3b 1af5650`. For context, read all eight manifest paths, the policy, project charter, template status, pathway README, mathematical writing guide, and review-dispatch and handoff skills at the candidate checkout. `git status --short --branch` showed a clean worktree on main, one commit ahead of origin/main, at the start. `git rev-parse HEAD` matched the frozen candidate.
- `git diff --check e2d6a3b 1af5650` exited successfully with no output. A Python check read the paths with `git diff --name-only`, the candidate inventory with `git ls-tree -r --name-only`, and Markdown with `git show 1af5650:<path>`. It resolved all 50 relative inline link references in the eight files, including seven heading fragments. External link availability falls outside this check.
- Traced a two-session example through launch, independent work, a provisional dependency, integration, and the hearing. A worker can continue after the decisive test inside the approved scope, can return an obstruction, and can resume from a recorded stage. The receiving worker checks a pinned statement and carries any open premise. The lead checks reviewed file identities after integration. The hearing records the researcher's choice or the bounds of an explicit delegation. The existing plan, article admission and researcher acceptance gates still apply.
- Read every addition and inspected the names, modes and commit subject. The example uses abstract objects and an invariant. The new text contains no identifiable research case, project-specific result, private source excerpt, account, personal path, or credential. All eight entries are ordinary Markdown files. This assessment concerns the candidate changes and does not certify the full repository history.

## Findings

**R1 · Important · blocking.** In the article companion, “A tentative goalpost” asks for the theorem that makes the answer complete and an example outside its domain. Consider a working draft which reconstructs an implication and identifies the converse as unresolved, without a known separating example. That draft can answer the surrounding “central question” and “reader and contribution” prompts honestly. It cannot fill this one as written. Make the theorem and boundary example conditional on their availability. Let a partial result, reconstruction or obstruction identify what the reader can now decide and the exact implication still open.

**R2 · Minor · optional.** The README directs a returning session to “its coverage table.” The guide describes the column contents under “Convene on evidence” but supplies no table to copy. Add a blank table with the prescribed headings, or point the README to the instructions for making the table.

The lead owns disposition and preservation. A delta check should read the repaired passages against these two cases. Researcher acceptance, any mathematical result, an article admission, and release or push authorization are outside the verdict.
