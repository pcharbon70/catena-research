---
title: "Catena Language Completion Plan"
kind: note
created: "2026-09-06"
maturity: developing
tags:
  - catena
  - language-design
  - specification
  - category-theory
  - conformance
  - decision-log
aliases:
  - "Catena implementation work-ahead"
---

# Catena Language Completion Plan

## Objective and authority

Complete an implementable, usable functional language whose types, data,
effects, and libraries support lawful composition on BEAM. Work from the
[141-item checklist](../00-inbox/language-specification-completeness-checklist.md)
and the [completion audit](../50-journal/2026-09-06-checklist-completion-audit.md),
preserving completed contracts while closing their remaining integration gaps.
Language implementation belongs in the sibling `../catena` repository;
this repository owns research, decisions, normative specifications, and evidence.

The user has delegated selection of the answers the agent would recommend,
after exploring at least four alternatives for every decision. The decisions
below and in the three volumes are **agent selections under that delegation**.
They are not separately reviewed user choices and they do not themselves
change normative language rules. The
[decision register](design-decision-register.md#language-completion-plan-2026-09-06)
preserves the alternatives, recommendations, selections, and their provenance.
Implementation discoveries requiring another decision get the same four-option
treatment in the execution journal before the dependent change is made.

**Public vocabulary is held.** Do not select new keywords, capability names,
standard-library spellings, pedagogical names, or a complete source grammar
during this work. P107 and P109 keep their later joint design gate. Existing
normative names and retained JSON/kernel notation remain usable as historical
and executable interfaces; using them to test semantics does not endorse them
as the final public vocabulary. Tool internals and semantic models can be
implemented before public naming is selected. A grammar-dependent item stays
partial until its actual parser/adoption obligations can be met.

The governing authority is
[Specification Authority](../SPECIFICATION-AUTHORITY.md#conflict-resolution),
with the [conformance vocabulary](../CONFORMANCE-VOCABULARY.md) and
[implementation-limits policy](../IMPLEMENTATION-LIMITS.md). A future change
to language behavior requires explicit normative applicability, lifecycle,
revision and migration treatment. A compiler correction to an existing rule
does not automatically consume a semantic revision. No test or plan silently
settles a normative contradiction.

## Baseline and coverage

Planning starts from research commit
`d93a655eae07c9e0dc539eff07487c4326d05eea` and compiler commit
`d7e0fcc484d3e1c3b4a292d4d3e703ddcc330535`. At that baseline the checklist has
85 complete items, 36 partials, 18 gaps and two deferrals. Its 713 obligations
are classified as 614 traced, 78 partial and 21 untraced. These are baseline
facts, not a forecast of implementation effort or a claim that the
whole-language composition proof is finished.
Status prefixes in the decision volumes record this planning baseline; their
immutable numeric IDs link the original choices to subsequent execution.
Consult the live checklist and execution state for later completion changes.

Every numeric identity appears once in the detailed plan:

| Volume | Coverage | Role |
| --- | --- | --- |
| [Foundations](language-completion-plan-foundations.md) | 001–046 | Preserve the type, data, category, effect, governance, lexical, module and expression contracts while integrating them. |
| [Semantics and runtime](language-completion-plan-semantics.md) | 047–092 | Complete comprehension evidence, resource lifetimes and the public runtime without weakening the existing type/effect boundaries. |
| [Interoperability and delivery](language-completion-plan-delivery.md) | 093–141 | Deliver checked foreign boundaries, library semantics, tools, security, integrated assurance, release gates and the late self-hosting milestone. |

Each item contains at least two concrete decisions; each unfinished item has
at least three. Each decision compares four alternatives, selects the
recommended one, and explains its tradeoffs. Each item also names dependencies,
implementation steps and observable acceptance evidence. For complete items,
these are preservation and integration decisions rather than an instruction
to redesign settled semantics. Deferred features receive explicit scope and
arrival gates rather than assumed admission.

The completed planning gate verified **392 decisions and 1,568 alternatives**:
92 foundation decisions, 137 semantics/runtime decisions, 151 delivery
decisions and 12 cross-cutting decisions. Every decision row is preserved
verbatim in the register. The initial implementation starts only after this
coverage check and archive validation passed.

## Category theory as a design constraint

The [category-theory synthesis](category-theory-for-programming.md#executive-conclusion)
and [combinator research](combinators-for-algebraic-data-and-categorical-programming.md#inclusion-standard)
give the decision standard: identify what composes, the least structure that
supports that composition, and the observations it must preserve. Retain the
existing nominal data, coherent trait evidence, effect rows, and lawful
derivations. Give every admitted operation both a type/law contract and an
execution contract covering order, multiplicity, failure and cost.

Do not infer effect commutativity, totality, resource safety, lawful user
instances, or efficient execution from a categorical name. Catena admits
general recursion; its operational semantics cannot be treated as the
category of total set functions without the relevant restrictions. Evidence
that a law holds for a pure total fragment cannot justify moving an effect,
duplicating a callback, dropping a trap, or erasing an authority check.
The existing
[trait laws](../60-specification/traits-and-categorical-operations/laws-derivation-and-testing.md)
and [operational contracts](../60-specification/traits-and-categorical-operations/operational-semantics.md)
remain the starting constraints.

Practical success needs executable composition across boundaries. The
integration corpus should include a pure data transformation with derived
operations; a handled effectful traversal; an acquire/use/release computation;
a supervised typed request/reply service; an explicitly authorized foreign
adapter; and a reproducibly built package carrying governance evidence.
Start these over retained internal inputs. Adapt the same semantic cases to
the public language only after P107/P109's joint design, without rewriting
the expected observations to make an implementation pass.

## Cross-cutting decisions

Each row is selected by the agent under the user's delegation. Alternatives
are compared as approaches to this task, not as retroactive amendments to
retained normative versions.

| Decision | A | B | C | D | Selected recommendation and reason |
| --- | --- | --- | --- | --- | --- |
| CP-G01 | Semantic contracts over retained inputs first; executable early, public presentation waits. | Freeze a new source language now; attractive demos but violates the vocabulary hold. | Write the entire specification before any execution; coherent prose but late feasibility feedback. | Implement whichever compiler feature is easiest; fast local progress but unresolved cross-boundary contracts. | **A (recommended; selected)**. Semantics first follows P109's existing capstone rule and permits real execution now. |
| CP-G02 | Types/laws plus explicit operational contracts; more obligations but preserves both composition and observations. | Treat familiar category laws as automatic optimizer permissions; fewer checks but unsound for effects or divergence. | Put mathematical structures only in optional libraries; easy core but discards established C004 commitments. | Make category terminology mandatory in source; visible mathematics but no demonstrated usability benefit. | **A (recommended; selected)**. The category and combinator research requires both extensional and operational evidence. |
| CP-G03 | Preserve completed contracts and add integration checks; concentrates effort on actual gaps. | Reimplement all 141 items; uniform new code but loses trusted evidence and repeats work. | Assume every checked item composes automatically; cheap but contradicts C132's outstanding proof obligation. | Reopen every item until a whole-language proof exists; conservative label but destroys useful bounded status. | **A (recommended; selected)**. Completion remains scoped; an actual contradiction triggers focused review under the authority policy. |
| CP-G04 | Repair the three comprehension evidence gaps first, then settle P086 explicitly; immediate execution feedback on agreed rules. | Add resource scopes first; useful capability but builds on unverified effect composition. | Begin final grammar; visible language but violates the hold. | Start self-hosting; exercises many subsystems but depends on missing runtime/tool contracts. | **A (recommended; selected)**. The audit supplies concrete falsifiable witnesses and current compiler targets. |
| CP-G05 | Per-slice normative rules, executable reference, BEAM evidence and traceability in one change set; coordination cost but reviewable closure. | Normative chapters only; authority clear but implementation feasibility unknown. | Code and tests first with prose later; fast experiment but risks silent semantics. | Large end-of-project integration; fewer releases but expensive conflict discovery. | **A (recommended; selected)**. Follow the archive's atomic publication and conformance rules, with experiments visibly separated from promotion. |
| CP-G06 | Independent small-step/reference observations plus compiled BEAM and explicit expected traces; catches shared and backend mistakes. | Treat generated source strings as behavioral evidence; easy assertions but does not execute the claim. | Run only the BEAM implementation; realistic execution but no independent semantic comparison. | Require mechanized proof before every fixture; strong assurance but blocks useful bounded empirical evidence. | **A (recommended; selected)**. P133/P134 grow systematically; proofs remain separately tracked rather than implied by tests. |
| CP-G07 | Add new semantic boundaries through explicit cumulative lifecycle records, and fix implementation defects against existing rules; accurate version meaning. | Bump a language revision for every test; easy chronology but confuses semantics with evidence. | Silently rewrite retained normative meaning; fewer files but breaks C008 applicability. | Freeze all existing defects forever; historical bytes retained but future conformance impossible. | **A (recommended; selected)**. Apply C008 and specification authority; allocate the next unused revision only when the slice needs one. |
| CP-G08 | Implement parser-independent tools now and hold source adoption; useful infrastructure with honest partial status. | Block all tools until grammar; clean ordering but wastes independent build/security work. | Invent temporary public syntax and promise later cleanup; fast demos but creates unsupported compatibility pressure. | Declare source tooling complete from mocked inputs; tidy checklist but false completion. | **A (recommended; selected)**. P107/P109 remain real gates; formatter/editor source completion follows them. |
| CP-G09 | A progressive integrated corpus with positive, negative, boundary, compatibility and cost observations per slice; broadening follows new risks. | Exhaustively retest everything after each text edit; reassuring output but little new evidence. | Happy-path examples alone; small suite but misses failures and exclusions. | Count obligation tags as proof; measurable coverage but conflates names with behavior. | **A (recommended; selected)**. The completion audit demonstrated why tagged coverage must be supported by actual assertions. |
| CP-G10 | Record every new implementation fork with four alternatives before selecting it; preserves reasoning as evidence changes. | Pretend this initial plan predicts every future choice; tidy document but hides discoveries. | Ask the user for every routine fork; explicit review but contradicts delegated autonomy. | Make unrecorded ad hoc choices; fast local decisions but unreviewable contract drift. | **A (recommended; selected)**. Existing user authorization covers recommended selections; new evidence can revise a recommendation with a recorded reason. |
| CP-G11 | Finish release gates with an explicit statement of remaining proof obligations and supported scope; accurate readiness claim. | Count checklist marks as release readiness; simple but ignores composition and performance. | Require self-hosting before any useful compiler release; strong bootstrap milestone but delays external utility. | Call a retained-input prototype a completed public language; demos run but vocabulary, parsing and usability remain absent. | **A (recommended; selected)**. G139 owns the disposition of C132's unproved composition lemma; G141 is the separate late-0.x milestone. |
| CP-G12 | Co-design shared semantic interfaces, implement a minimal checked adapter over explicit harness authority, then complete the mutually dependent public integration; avoids circular gates with clear partial status. | Require every dependency item complete before touching its peer; tidy ordering but deadlocks 094/096/106. | Bypass the missing authority interface using ambient host services; executable sooner but violates C082. | Merge foreign calls, runtime capabilities and all tools into one indivisible feature; coherent on paper but postpones feedback and makes review too large. | **A (recommended; selected)**. Treat interface prerequisites separately from whole-item completion, while preserving checked ingress, lexical effect scope and final integration evidence. |

## Dependency order and executable milestones

The following order describes admission gates, not a blanket ban on parallel
work. Proof, security, reproducibility, compatibility and diagnostics start
with the first affected slice and grow with it. The detailed item sections
refine these dependencies. Numeric IDs identify work independently of their
changing status prefixes.

| Milestone | Work and order | Exit evidence | Holds and dependencies |
| --- | --- | --- | --- |
| M0 — plan and baseline | Finish all three volumes; record every selected fork; verify 001–141 coverage, alternatives, links and current baselines. | Complete plan inventory, consistent decision register, archive validation. | Implementation begins only after this planning gate. |
| M1 — repair recorded gaps | Execute 050/053/057 together; then resolve 086's scan/starvation contradiction with explicit normative applicability and fixtures. Run relevant 001–079 preservation cases as dependencies. | Exact effect order/multiplicity and failure-prefix agreement on reference/BEAM; receive scan and retained-message witnesses; honest registry/checklist updates. | No new vocabulary; no weakening normative requirements to satisfy existing code. |
| M2 — lifetime and local concurrency | Specify 080 and 088's shared cancellation/cleanup interface; implement 084 and the local facets of 085, then 087/090 and 089's lifecycle adapter. Establish the outcome shape and 093/097 representation interfaces as needed. | Resource event traces, affine escape rejection, cancellation races, typed local delivery and supervised restart model agree with BEAM. | Ordinary ADTs can model outcomes before 103's named library. 089 needs a narrow checked OTP adapter; 085's remote facet waits for 091. |
| M3 — checked host boundary | Co-design the shared 093–100/106/126/127/129/131 interfaces; implement checked ingress before foreign adapters, then complete the host-boundary integration jointly with M4. | Admission/rejection corpus, calling-convention and failure mapping, metadata and supported-OTP witnesses. | Initial adapters use explicit harness authority, never ambient services. Whole-item completion waits for the promised callback, provisioning and lifecycle integration. Native code remains an explicitly classified trust boundary. |
| M4 — practical library semantics | Complete 101–106/108 with minimal coherent operations, explicit outcomes, numeric/text semantics and environmental capabilities. | Law-qualified data composition, operational order, invalid input and resource/failure tests; a capability-supplied tool computation runs. | 107 public names held. 106 must explicitly amend the current zero-argument entry boundary if capability parameters are admitted. |
| M5 — distribution and operations | Complete 091/092 after local process, foreign identity, compatibility and migration interfaces; integrate 116/121/128/130. | Node/version disagreement, serialization, disconnect, upgrade/rollback and locked-build evidence. | Distribution and hot upgrades are admitted only through their own scope and failure contracts, never assumed from BEAM availability. |
| M6 — tools before public adoption | Build semantic services for 117/119–125: structured diagnostics, docs attachment, sessions, package builds, tests, incremental analysis, debugging and migrations. Prepare 118's comment/formatting constraints. | Real retained-input workloads, deterministic diagnostics, reset/replay, safe edits, build/cache isolation and tooling protocol tests. | 118 and grammar-dependent portions of 119/120/123/125 remain partial until source adoption; no replacement public syntax. |
| M7 — integrated assurance | Grow 133–136/138/139 throughout M1–M6; complete missing reference rules, generators/shrinkers, rewrite premises, historical compatibility, performance envelope and release criteria. | Cross-feature observations and failure traces, reproducible minimized counterexamples, measured costs, explicit proof ledger and readiness report. | C132 completes targets only. Tests do not prove the outstanding composition lemma. |
| M8 — later joint vocabulary and grammar | After the user releases the hold, jointly settle 107/109; integrate existing semantics into the agreed parser and language tools, finish 118 and source-dependent services, and run 137. | Lossless parse/adoption and diagnostic corpus; round-trip/idempotent formatting; observed task-based usability; unchanged semantic observations. | This milestone cannot be executed under the present instruction to defer vocabulary. Its alternatives concern process/adoption, not selecting words now. |
| M9 — release and bootstrap | Apply 139 to the admitted public language; later execute 141 over the sufficient compiler subset, compare stages and preserve rollback. | Published-scope readiness evidence, reproducible bootstrap stages, fixed-point or justified semantic equivalence and retained trusted bootstrap. | No implied publication authorization. Self-hosting does not change the BEAM target. 059/083 stay scoped by their separate inclusion/exclusion gates. |

### Breaking dependency cycles

Resource scopes and cancellation are designed together at the semantic
interface, then implemented with deterministic local fixtures before public
time/actor APIs are layered on. Outcome values can be modeled using existing
nominal ADTs before library names are chosen. Checked foreign admission must
precede library adapters, while tool services use explicit host harnesses
until environmental capabilities are normatively admitted. Library semantics
and tool engines therefore do not need a prematurely fixed grammar.

For 094/096/106, dependencies first mean agreed calling, admission, authority
and lifetime interfaces, not that each entire item must already be complete.
Implement the smallest checked adapter with explicitly supplied test-harness
authority, then integrate the normative launch channel and callback lifetime
before closing the wider items. An ordinary opaque service-authority descriptor
is distinct from a C005 lexical capability identity: the latter does not become
a first-class, storable or sendable value through the launch amendment.
Similarly, 091 consumes local message semantics from 085, then supplies the
remote-delivery evidence that closes 085's wider scope. Local resource
experiments use the already admitted ADT outcome model before the standard
outcome library is ready. Supervision needs the chosen narrow typed OTP
lifecycle adapter from 096, rather than every future foreign-call facility.

Reproducibility, trust and the reference evaluator cannot wait until the
end: each new slice extends their inventories and examples. Whole-language
claims wait for all admitted boundaries and their integrated evidence. A
feature exclusion must state its consequences and rejection behavior; it
cannot be used merely to avoid implementing essential practical capabilities.

## Slice execution procedure

1. Read the complete checklist item, current normative headings, its research
   trail and relevant implementation. Verify dependencies and record the
   current source identity; preserve unrelated changes in both repositories.
2. Apply the selected decisions. If feasibility or evidence changes the
   choice, record at least four alternatives and the new recommendation in
   the slice journal, distinguishing it from the original selection.
3. Define observable acceptance cases before implementation: values, types,
   effects, order/multiplicity, failures, rejected programs, limits, compatibility
   and applicable cost. Include an independent expected observation, not just
   agreement between two implementations sharing the same defect.
4. For new semantics, create the focused research/inquiry/specification bundle,
   governing-rule anchors, conformance IDs, variability declarations and
   explicit lifecycle. For an existing-rule bug, cite the governing contract
   and add a failing regression first; do not create a revision solely for a fix.
5. Implement in `../catena` using the retained frontend/core interfaces.
   Keep compiler internals out of future public vocabulary decisions. Extend
   the reference and BEAM paths when their domains change.
6. Run relevant focused tests, compilation and the full affected suite at
   the slice gate. Inspect traces, boundary failures and generated artifacts
   where the contract calls for them. Record actual commands and results.
7. Synchronize the traceability register, active notes/inquiries/maps/indexes
   and checklist only when the stated item's complete evidence gate passes.
   Preserve numeric IDs and dated historical records. An implemented subset
   earns a precise partial statement, not a completed checkbox.
8. Run `python3 validate_archive.py`, validator tests when tooling changes,
   and `git diff --check`; review the complete diff and record the next
   dependency-ready unit. Commits, pushes, PRs and publication remain separate
   user-requested actions.

## Execution state

The [completion inquiry](../40-inquiries/how-can-catena-complete-its-language-definition.md)
tracks unresolved cross-item questions. The
[execution journal](../50-journal/2026-09-06-language-completion-plan.md)
records the planning gate and first implementation results. The
[capability integration journal](../50-journal/2026-09-08-capability-kernel-integration.md)
tracks the resumed implementation. Update this
section with observed results, while keeping the baseline and original
decision alternatives above intact.

| Unit | State | Evidence or next action |
| --- | --- | --- |
| M0 planning | Complete | All 141 items, 392 decisions and 1,568 alternatives verified; register and archive validated. |
| M1 first implementation | Complete within its bounded scope | Backend call/handler repairs and real locally handled comprehension traces applied in `../catena`; 624 full-suite tests, clean compilation, formatting and escript build pass. The journal records the remaining general-effect boundary. |
| M1 general comprehension effects | C050 complete; P053/P057 acceptance next | The 0.1.50 closed capability target now checks fragment rows, preserves enclosing handlers and emits distinct BEAM artifacts. Exact C010 remains unchanged. |
| M1 receive resolution | Complete at 0.1.49 | Explicit amendment, exact lifecycle registration, and stepper/BEAM selection, residual-mailbox and waiting witnesses; see the September 8 journal. |
| M2–M7 | Planned | Follow dependencies and per-item gates; no claim of implementation from planning. |
| M8 vocabulary and grammar | Held by user scope | Keep preparation semantic; return to joint design only after the hold is released. |
| M9 release and self-hosting | Planned with prerequisites | Complete public adoption and measured readiness first. |

The first experiments refined M1's dependency order: C047's named exact
kernel target cannot express its general repeated escaping-effect row.
The journal records the four-option target decision and deferred metadata
choices. This changes execution sequencing; it does not rewrite the
baseline decisions or promote checklist items from bounded local evidence.

## Connections

- [Language completion map](../10-maps/language-completion.md) routes from
  the ledger through decisions to executable evidence.
- [Design decision register](design-decision-register.md) preserves historical
  user choices and distinguishes the new delegated agent selections.
- [Formal semantic kernel](catena-formal-semantic-kernel.md) explains the
  existing reference/BEAM seam used for early integration.
- [Algebraic effects and handlers](algebraic-effects-and-handlers.md) supplies
  the capability, scope and resumption model; categorical equations alone
  cannot settle its runtime consequences.
