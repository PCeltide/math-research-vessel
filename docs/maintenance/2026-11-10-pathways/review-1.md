# Independent review: reusable research pathways

**Verdict: PASS for the five-file candidate identified below.** No actionable defect remains in the reviewed scope. This is a documentation and workflow integration review, not authorization to launch research, admit article content, merge, publish, or push.

## Reviewer, system, and times

- Reviewer: fresh reviewer agent `/root/vessel_pathways_review`.
- System: Codex, GPT-6 family. The exact deployed model identifier is not exposed in this reviewer context; no model substitution was requested or observed.
- Date and timezone of this assessment: 2026-11-09, UTC.
- First recorded review-clock sample: 2026-11-09 23:31:20 UTC. Initial startup and candidate reads preceded this sample; no more precise start time was recorded.
- Final identity and scope checks completed at the 2026-11-09 23:33:05 UTC clock sample.
- Role: read-only repository review. The lead owns every repository edit. The reviewer writes only this assessment at `/tmp/vessel-pathways-review/review-1.md`.

## Exact candidate

Repository: `/workspace/math-research-vessel`.

Observed branch: `work`. Observed HEAD and comparison base: `990e61357a975187b7f059337303b2088110d6f7`.

The candidate is the working-tree snapshot named by `/tmp/vessel-pathways-review/candidate-v1.json`, not an already-created commit. The manifest itself has SHA-256 `f65478cd19bd8f7d3cb3310de0a1c7552cbbdf9739abde89c87284d4a7e1b3c0`.

| File | SHA-256 of reviewed working-tree bytes |
|---|---|
| `AGENTS.md` | `b72257c91ced65cf0ba9717b5e9674e1554a36c749353c83553925158ba63747` |
| `README.md` | `45cdc590186cbac2af699cefe395125e04a98109c1286c11f29f5bfa2f6fce27` |
| `docs/guides/workflow.md` | `b28f29a844cf3e5772c1aee39185bfaa1362cf8a16628d4616234cd95e8ce8cb` |
| `docs/pathways/README.md` | `98188c172e225b7cb2b27cefcc5a31feaf93a401ac554186088d1eb98ed54ba7` |
| `docs/pathways/TEMPLATE.md` | `85e0cf00a14c795a61f19068d159c2a005e1b56294c550c062801004189d0265` |

All five hashes matched the manifest at initial verification, during the mechanical checks, and at final identity verification. The first three paths exist in the base commit and were reviewed with their complete diff against it. Both pathway files are new relative to that base and were read in full as additions.

## Scope and gate

The review checks whether these exact files provide a generic, reusable pathway and priority-bucket system; preserve the existing scope, launch, evidence, and article-selection boundaries; integrate proportionate checkpoint upkeep; remain discoverable to future agents; supply a usable card template; and are suitable for the public vessel template without project-specific research or private material.

The dispatch reports the user's authorization to integrate the general system directly in one commit, with no new branch or PR. That authority is an input to this review. The blank research charter does not prevent this authorized template-maintenance review: no research assignment or mathematical result is being launched here.

## Inputs actually checked and read spans

The following candidate files were read in full at the hashes above:

| Input | Read span |
|---|---|
| `AGENTS.md` | lines 1–26 |
| `README.md` | lines 1–80 |
| `docs/guides/workflow.md` | lines 1–136 |
| `docs/pathways/README.md` | lines 1–44 |
| `docs/pathways/TEMPLATE.md` | lines 1–35 |

The following governing and comparison inputs were read in full and mechanically verified byte-identical to their versions at base commit `990e61357a975187b7f059337303b2088110d6f7`:

| Input | Read span | Use |
|---|---|---|
| `docs/collaboration.md` | lines 1–41 | Authority, bounded work, evidence, independent review, preservation, and public-data rules |
| `docs/context/status.md` | lines 1–11 | Startup state and exposure disclosure |
| `docs/project-charter.md` | lines 1–45 | Existing scope and reserved-decision structure |
| `docs/guides/central-article.md` | lines 1–109 | Distinguishing research records, article selection, admission, and acceptance |
| `.agents/skills/review-dispatch/SKILL.md` | lines 1–56 | Candidate freeze, isolation, assessment form, preservation, and delta-review requirements |
| `.agents/skills/handoff/SKILL.md` | lines 1–50 | Startup, identity checks, and reviewer hand-back requirements |

Also checked: the complete candidate manifest; repository branch, HEAD, tracked diff, and untracked path inventory; every local Markdown link in the five candidate files; and the factual timezone clarification described below. The cloud-environment runtime skill was read for execution-environment requirements, and the environment status was inspected. It supplied no substantive research input.

One initial aggregated tool response was truncated. The workflow and complete tracked diff were read again without truncation before relying on them. No omitted required span remains unread.

## Exposure and isolation limits

This reviewer received the task brief in a fresh context and did not inspect the author's conversation, private project, other reviewers' conclusions, or unrelated maintenance evidence. The mandatory status file is the unchanged blank-workspace status: it says no assignment is launched and no result is claimed. It contains no substantive conclusion about this candidate. The candidate's own claims about its boundaries were treated as claims to check against the governing documents.

The reviewer noticed that the candidate's two amendment notes use 2026-11-10 while the sampled UTC date is 2026-11-09. The lead supplied a factual clarification during review: the amendment dates deliberately use the maintainer-session timezone `Asia/Calcutta` (UTC+05:30). This was the only substantive follow-up received. The reviewer independently checked the conversion: the 23:31:20 UTC sample is 2026-11-10 05:01:20 in that timezone. Date-only amendment metadata therefore has a consistent date basis and needs no repair. The choice of maintainer timezone is reported by the lead; no private records were opened to establish it.

The repository is shared, rather than a separate reviewer checkout. Hash checks at the beginning and end establish that all five reviewed files stayed at the pinned identities. During review, the lead added untracked maintenance manifest/brief paths outside the candidate; their contents were not inspected and this verdict does not cover them. No repository file was written by the reviewer.

## Checks and outputs

1. **Snapshot identity:** Python SHA-256 checks returned `MATCH` for all five manifest paths on every pass. Final HEAD remained `990e61357a975187b7f059337303b2088110d6f7`; final branch remained `work`.
2. **Comparison against base:** `git diff 990e61357a975187b7f059337303b2088110d6f7 -- AGENTS.md README.md docs/guides/workflow.md` was read completely. `git cat-file -e` confirmed the three existing paths and the absence of both new pathway files in the base. Both new files were reviewed in full.
3. **Whitespace:** `git diff --check` exited 0 with no output. This command covers the tracked diff; the untracked pathway files were separately read in full.
4. **Link integrity:** a local Markdown link/path-and-heading check across the five candidate files reported `Checked 33 local links; errors: []`. External URLs were not fetched.
5. **Governing-input identity:** all six comparison documents listed above returned `IDENTICAL TO BASE`.
6. **Date consistency:** Python `zoneinfo` converted `2026-11-09 23:31:20 UTC` to `2026-11-10T05:01:20+05:30` in `Asia/Calcutta`, consistent with the disclosed amendment-date convention.
7. **Manual workflow and template review:** the cases and conclusions below were checked directly against the complete text.

### Workflow assessment

- **Capture and scale:** a short ledger entry can retain an idea; a card is reserved for reasoning or restart information worth preserving. Capture does not permit a side investigation, and active proof gaps stay in the active report and status. The template explicitly permits unused prompts to be removed. No empty project ledger, demonstration claim, or recurring scan is introduced.
- **Organization:** the four buckets distinguish a selected next direction, a worthwhile later question, a conditional or tangential idea, and a settled or retired bounded question. Existing dispositions and optional readiness remain separate from priority. The ledger owns current priority; cards own reasons, routes, inputs, and history; plans own executable scope; canonical reports and evidence own results and review coverage. These roles avoid a second live assignment contract or duplicated proof store.
- **Authority and evidence:** a card, priority order, preparation, or review PASS does not launch work. Researcher selection, the actual launch instruction, exact plan/input revisions, and the existing assignment scope remain controlling. Card updates do not enlarge a launched plan. Inherited results, conjectures, unread leads, and open premises keep separate evidence states. Broad themes are not marked solved merely because one bounded investigation finishes.
- **Checkpoint integration:** assignment closeout, direction discussions, and dependency-changing results trigger reconciliation of affected entries. The instructions expressly limit the work to relevant entries, preserve retired IDs and history, and deny scheduled/background research authority. A separately selectable continuation receives its own candidate or identified continuation and the appropriate launch.
- **Article boundary:** candidate selection and research completion do not promise article inclusion. The pathway guide links the governing article guide, distinguishes possible reader value from admission, and keeps result acceptance separate. This is consistent with the existing central-article rules.
- **Future discovery:** AGENTS supplies a direct mandatory reading trigger, the workflow links pathways at preparation, assignment resumption, and ledger upkeep, and README explains the role. A future agent can reach the guide and template through ordinary startup and assignment work.
- **Template usability:** the card prompts cover precise question and payoff, provenance and decisions, exact input revisions and evidence, a decisive first test, alternatives/dependencies/risks, a proposed bounded deliverable, outcomes/reopening, and the canonical handoff links. It can begin small and expand without being mistaken for a launch or final proof.
- **Public-template suitability:** direct reading of all five files found general mathematical-workflow guidance, not subject-specific research, private source text, project results, or private personal data. The README update instructions distinguish vessel-owned guide/template files from project-owned pathway cards, so taking template updates does not instruct users to replace their own cards.

## Findings

None. There is no required repair, nonblocking defect, or optional stylistic expansion requested. No finding IDs require disposition.

## Remaining limits and hand-back

- PASS applies only to the five exact hashes above and the stated documentation scope. A change to those bytes requires the appropriate delta review.
- This is not mathematical, citation, computational, formal, rendered-PDF, or external-source review; the candidate makes no mathematical claim requiring those checks.
- The guide was checked by direct reading and concrete workflow walkthroughs, not by running a real research project or a live agent-resumption experiment.
- No private project was inspected or compared, and no broad repository or Git-history privacy certification is claimed. Public-template suitability is limited to direct inspection of the reviewed candidate.
- The eventual commit, preservation packet, remote state, and any later additions are not covered. The lead must preserve this complete original assessment unchanged, retain the manifest, and verify the final candidate identity when integrating.
- The reviewer hand-back is this report. It is currently local only at the assigned temporary path; repository integration and any authorized remote preservation remain the lead's work. The bounded review assignment is complete, with no open in-scope review path or pending researcher decision.
