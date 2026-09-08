---
title: "Language Completion Plan: Foundations"
kind: note
created: "2026-09-06"
maturity: developing
tags:
  - catena
  - language-design
  - specification
  - category-theory
aliases:
  - "Catena completion plan items 001–046"
---

# Language Completion Plan: Foundations

## Scope and decision authority

This volume covers every checklist item **001–046**, all **46 currently
complete**, with **92 implementation and integration decisions**. It preserves
those completed bounded contracts. The work below is the integration and
regression work needed when unfinished items build on them; it is not a claim
that all 46 implementations need rewriting or that their evidence has vanished.
Reuse an existing witness when it already proves the stated observation; add a
test only for an uncovered interaction or changed path.

The user delegated selection of the answer the agent would recommend. Each
row explores four alternatives and records the recommended answer selected by
the agent under that delegation. These are **non-normative execution choices**,
not claims that the user reviewed each fork or that this note amends language
rules. Any actual semantic change requires an explicit normative slice and
applicability record under [Specification Authority](../SPECIFICATION-AUTHORITY.md#repair-and-promotion-workflow).
Where an alternative would change a settled contract, its tradeoff identifies
that conflict; it is not a proposal to reopen that contract gratuitously.

Category theory supplies the model of typed composition, sums/products,
coherent capabilities and laws. The [category-theory synthesis](category-theory-for-programming.md#executive-conclusion)
explains why it does not determine evaluation order, termination, resource
lifetime, representation or public terminology. The plan preserves the chosen
strict, immutable, explicitly effectful language and the narrow law domains
already supported by research. General recursion prevents an unqualified claim
that all programs are arrows in the category of sets and total functions.

**No new public vocabulary, reserved words, source spellings or whole-language
grammar are selected here.** Existing API names and JSON/kernel notation below
identify current implementation boundaries. P109 remains the later source
adoption owner. A real language can be developed and exercised through existing
typed transports while vocabulary work remains deliberately pending.

## Baseline and execution discipline

The baseline is the [audited checklist](../00-inbox/language-specification-completeness-checklist.md)
and [6 September evidence record](../50-journal/2026-09-06-checklist-completion-audit.md).
Compiler paths below are relative to the sibling `/home/ducky/code/catena`
repository, inspected at the audit's `d7e0fcc484d3e1c3b4a292d4d3e703ddcc330535`
semantic baseline. Research-prefixed paths are relative to this archive. The
existing suite already contains the named area tests; exact future fixtures are
added beside them only when needed. This planning pass did not rerun those
compiler suites or claim a new implementation result.

Execute each item in this order: read its linked governing rule and the current
code; retain already passing evidence; perform the stated integration when its
consumer arrives; verify positive, negative and boundary observations; record
exact revisions, commands and results; then update relevant traceability. Do not
mark a new implementation conformant from obligation tags or final-value tests
when the rule requires actual effect traces, rejection or transactional evidence.

**Status gate for all 46 items:** retain the existing C prefix and checked state.
The item-specific acceptance set is a gate for a *new integration claim*, not a
second completion ceremony for settled work. A demonstrated contradiction or
missing mandatory witness blocks the affected claim and triggers a focused audit;
it does not automatically reopen adjacent items. Items 023, 025 and 028 identify
specific wording checks that must be resolved before stronger integrated claims
rely on those sentences. A proposed interpretation is not their resolution.

The most useful immediate work from this volume is C011's evidence discipline,
C030's actual request-trace oracle for P050/P053/P057, and C008's serialized
revision allocation. Do not spend the first implementation wave rewriting
completed lexical or type-system components. Defer source-adapter integration
until the source-vocabulary hold is explicitly lifted.

## Item 001 — Principal inference and the advanced typing boundary

**Baseline:** C001 complete; preserve and integrate. **Dependencies:** C005, C010; integrates with P133/P134.

**Grounding:** [Governing rule](../60-specification/type-system/principal-inference-and-generalization.md#generalization); [research rationale](catena-greenfield-type-system.md). The recommendation cells apply these sources within this item's bounded contract.

**Compiler targets:** `lib/catena/type/infer.ex`; `lib/catena/type/advanced.ex`; `lib/catena/typed_core/verifier.ex`.

**Existing evidence home:** `test/catena/type_conformance_test.exs`.

| Decision | Question | A | B | C | D | Recommended selection and reason |
| --- | --- | --- | --- | --- | --- | --- |
| CP-001-1 | Where should new semantic forms enter inference? | Extend existing inference and advanced-checking entry points; preserves local guarantees. | First merge JSON and kernel checkers; removes duplication but delays semantics and expands regression scope. | Write a new inference engine; cleaner architecture but discards accumulated evidence. | Use a separate checker per future feature; isolates work but makes composition difficult. | A (recommended; selected by agent under user delegation): existing principal and annotated boundaries preserve the documented promise while permitting incremental evidence. |
| CP-001-2 | How should integration evidence distinguish principality from soundness? | Maintain fragment-labelled inference, rejection, and core-verification witnesses; accurate but requires classification. | Use accepted-program examples only; cheap but does not support principality. | Attempt whole-language completeness proof before extensions; strongest claim but exceeds the promised fragment. | Compare inferred type strings only; simple but confuses alpha-equivalence with correctness. | A (recommended; selected by agent under user delegation): the research partitions guarantees; P133/P134 own stronger composed results. |

**Ordered implementation steps:**

1. Record which typed constructs enter principal inference and which require annotation-directed checking; preserve effect-aware generalization.
2. Route each later semantic extension through its existing checker boundary and independently verify resulting core; keep the old frontends executable.
3. Add only the cross-feature regressions missing for each arriving slice and bind evidence to the selected revision.

**Acceptance evidence:** Positive: one pure identity binding used at Int and Bool. Negative: effectful expansive binding cannot acquire unsound polymorphism; occurs-check and skolem-escape rejection. Boundary: alpha-renaming and constraint work-list permutations preserve principal schemes and diagnostic families.

**Completion gate:** C001 remains complete. A new consumer is ready only when the above observations pass on its actual path and its obligation links resolve; defer unsupported semantic extensions to the named owners and public spelling to P109.

## Item 002 — Nominal data and pattern matching

**Baseline:** C002 complete; preserve and integrate. **Dependencies:** C001; later P101/P102 and P093.

**Grounding:** [Governing rule](../60-specification/data-and-patterns/declarations-and-nominal-identity.md#nominal-generation); [research rationale](algebraic-data-types.md). The recommendation cells apply these sources within this item's bounded contract.

**Compiler targets:** `lib/catena/data.ex`; `lib/catena/pattern/coverage.ex`; `lib/catena/derive.ex`.

**Existing evidence home:** `test/catena/c002_data_test.exs`.

| Decision | Question | A | B | C | D | Recommended selection and reason |
| --- | --- | --- | --- | --- | --- | --- |
| CP-002-1 | How should library data reuse nominal semantics? | Feed ordinary declarations into Data.elaborate; reuses identity and authority checks. | Hard-code each collection into inference; quick initially but creates privileged identities. | Ship opaque host objects for all collections; simple BEAM reuse but needs foreign contracts. | Replace nominal identity with structural equivalence; generic but breaks existing abstraction. | A (recommended; selected by agent under user delegation): ordinary declarations preserve the sum/product model and the established nominal boundary. |
| CP-002-2 | How should representation independence be guarded? | Run shared observations on both supported layouts; checks the required abstraction directly. | Freeze one layout for new libraries; easier debugging but creates accidental ABI dependence. | Only compare serialized interfaces; catches identity drift but misses runtime observations. | Add a third backend immediately; broader diversity but premature maintenance. | A (recommended; selected by agent under user delegation): two-layout semantic observations target C002’s existing guarantee without inventing a public layout. |

**Ordered implementation steps:**

1. Carry canonical nominal identities through new library declarations, interfaces, and typed core.
2. Reuse constructor-authority and coverage checks when integrating collections; audit representation-independent lowering on both existing layouts.
3. Retain atomic recursive-group publication and derivation eligibility checks when importing compiled libraries.

**Acceptance evidence:** Positive: the same exported datatype crosses a module boundary on both layouts. Negative: identically shaped declarations from different origins do not unify; abstract constructors remain inaccessible. Boundary: empty, mutually recursive, negative and nested declarations preserve their existing acceptance and derivation distinctions.

**Completion gate:** C002 remains complete. A new consumer is ready only when the above observations pass on its actual path and its obligation links resolve; defer unsupported semantic extensions to the named owners and public spelling to P109.

## Item 003 — Clause conditions

**Baseline:** C003 complete; preserve and integrate. **Dependencies:** C001/C002; P086 and G080 must preserve purity.

**Grounding:** [Governing rule](../60-specification/clause-conditions/syntax-and-safety.md#evaluation); [research rationale](clause-guards.md). The recommendation cells apply these sources within this item's bounded contract.

**Compiler targets:** `lib/catena/condition.ex`; `lib/catena/condition/facts.ex`; `lib/catena/kernel/checker.ex`.

**Existing evidence home:** `test/catena/c003_clause_condition_test.exs`.

| Decision | Question | A | B | C | D | Recommended selection and reason |
| --- | --- | --- | --- | --- | --- | --- |
| CP-003-1 | How should future branch contexts share condition semantics? | Reuse the existing condition checker and ordered tree; one bounded contract. | Translate arbitrary expressions into host guards; convenient but admits undocumented operations. | Reimplement the condition subset in each context; local convenience risks semantic drift. | Broaden conditions with every new primitive; expressive but requires an explicit later revision. | A (recommended; selected by agent under user delegation): the frozen total fragment supports predictable coverage and BEAM guard equivalence. |
| CP-003-2 | What evidence should protect receive integration? | Compare condition-tree decisions and retained mailbox observations; directly tests selection. | Inspect generated guard text alone; readable but misses runtime fallthrough. | Benchmark receive throughput alone; useful operationally but not semantic evidence. | Replace the native harness with a pure model only; deterministic but loses backend evidence. | A (recommended; selected by agent under user delegation): selection depends on evaluation and mailbox observations, especially the reopened P086 boundary. |

**Ordered implementation steps:**

1. Maintain the exact Bool/Int condition fragment and signed acyclic predicate boundary.
2. Reuse condition checking in receive and pattern integration; keep ordinary expressions separate from the restricted condition evaluator.
3. Exercise coverage facts and native lowering against the same ordered condition trees.

**Acceptance evidence:** Positive: a signed acyclic integer predicate permits its matching clause. Negative: non-Bool, effectful, recursive and out-of-fragment conditions reject with existing families. Boundary: predicate-cycle rejection, integer difference-constraint limits and false-condition fallthrough leave coverage honest.

**Completion gate:** C003 remains complete. A new consumer is ready only when the above observations pass on its actual path and its obligation links resolve; defer unsupported semantic extensions to the named owners and public spelling to P109.

## Item 004 — Traits and category-inspired operations

**Baseline:** C004 complete; preserve and integrate. **Dependencies:** C001/C002/C005; P101/P102 and P135.

**Grounding:** [Governing rule](../60-specification/traits-and-categorical-operations/operational-semantics.md#laws-do-not-schedule-work); [research rationale](category-theory-for-programming.md). The recommendation cells apply these sources within this item's bounded contract.

**Compiler targets:** `lib/catena/categorical.ex`; `lib/catena/categorical/standard.ex`; `lib/catena/categorical/law.ex`; `lib/catena/package/linker.ex`.

**Existing evidence home:** `test/catena/c004_categorical_test.exs`.

| Decision | Question | A | B | C | D | Recommended selection and reason |
| --- | --- | --- | --- | --- | --- | --- |
| CP-004-1 | How should category theory guide library integration? | Use the weakest existing capability matching each operation; keeps laws precise. | Require the strongest hierarchy member everywhere; uniform but overconstrains clients. | Add new categorical classes before use cases; expressive but creates unsupported law obligations. | Use only concrete collection operations; easy locally but loses existing reusable structure. | A (recommended; selected by agent under user delegation): the synthesis recommends weakest sufficient lawful structure with independent operational contracts. |
| CP-004-2 | Which optimizations may consume law evidence? | Retain specialization and erasure without new law rewrites; fits existing authority. | Enable every familiar categorical equation; concise optimizer but ignores effect assumptions. | Treat sampled laws as universal proofs; fast development but invalid evidence upgrade. | Disable all specialization until mechanized proofs; conservative but abandons implemented direct-call benefits. | A (recommended; selected by agent under user delegation): C004 permits specialization yet explicitly denies scheduling or rewriting rights from class membership. |

**Ordered implementation steps:**

1. Inventory the shipped seventeen-class hierarchy, kinds, law domains and existing behavior-first ABI without renaming any method.
2. Integrate library instances through existing coherence, template verification and specialization routes.
3. Pair law evidence with separate callback-order, multiplicity, failure and stack witnesses.

**Acceptance evidence:** Positive: lawful identity/composition cases and deterministic specialized calls agree with reference execution. Negative: overlaps, ambiguous evidence and unsupported derivation reject. Boundary: at least 250,000 List mapping/reduction positions remain stack safe; effectful callbacks retain order despite algebraic identities.

**Completion gate:** C004 remains complete. A new consumer is ready only when the above observations pass on its actual path and its obligation links resolve; defer unsupported semantic extensions to the named owners and public spelling to P109.

## Item 005 — Algebraic effects and handlers

**Baseline:** C005 complete; preserve and integrate. **Dependencies:** C001/C010/C081/C082; G080/D083/P106.

**Grounding:** [Governing rule](../60-specification/effects-and-handlers/deep-handlers-and-affine-resumptions.md#affine-resumption-form); [research rationale](algebraic-effects-and-handlers.md). The recommendation cells apply these sources within this item's bounded contract.

**Compiler targets:** `lib/catena/effect.ex`; `lib/catena/effect/row.ex`; `lib/catena/effect/reference.ex`; `lib/catena/effect/runtime.ex`; `lib/catena/runtime/resumption_token.ex`.

**Existing evidence home:** `test/catena/c005_effects_test.exs`.

| Decision | Question | A | B | C | D | Recommended selection and reason |
| --- | --- | --- | --- | --- | --- | --- |
| CP-005-1 | How should new effects fit the existing runtime? | Extend declared requests and typed capability plumbing; preserves deep affine semantics. | Use implicit process-dictionary handlers; simpler invocation but breaks lexical selection. | Make resumptions ordinary closures; familiar implementation but admits escape and duplication. | Introduce shallow handlers simultaneously; useful control model but adds a separate semantic feature. | A (recommended; selected by agent under user delegation): existing lexical requests already support composable interpretation without changing control multiplicity. |
| CP-005-2 | How should cleanup assumptions be treated during integration? | Record cleanup as G080’s explicit dependency and keep current abortion behavior observable. | Treat handler return clauses as universal finalizers; small change but does not cover every exit. | Rely on BEAM garbage collection for resource cleanup; convenient but no timely-release contract. | Add implicit finally behavior to every handler; broad coverage but silently changes C005. | A (recommended; selected by agent under user delegation): the deep-handler chapter explicitly disclaims cleanup; resource semantics require their own rule and evidence. |

**Ordered implementation steps:**

1. Keep nominal requests, lexical capability identity, duplicate effect rows, deep handlers and affine resumptions as the integration baseline.
2. Thread new environmental capabilities through typed core and both evaluators; explicitly route cleanup proposals to G080.
3. Check scope escape and continuation consumption independently before trusting lowering.

**Acceptance evidence:** Positive: nested handlers forward by identity and resumption reinstalls the matching handler. Negative: duplicate resume, capability escape and stored continuation reject. Boundary: abandoned remainder produces no later effects; runtime token rejects a second invocation before user code.

**Completion gate:** C005 remains complete. A new consumer is ready only when the above observations pass on its actual path and its obligation links resolve; defer unsupported semantic extensions to the named owners and public spelling to P109.

## Item 006 — Integrated specifications and governance

**Baseline:** C006 complete; preserve and integrate. **Dependencies:** C004/C008; P116/P128/P130/P131.

**Grounding:** [Governing rule](../60-specification/specifications-and-governance/claims-examples-and-checking.md#exact-executable-examples); [research rationale](language-integrated-specifications-and-governance.md). The recommendation cells apply these sources within this item's bounded contract.

**Compiler targets:** `lib/catena/specification.ex`; `lib/catena/governance.ex`; `lib/catena/assurance.ex`; `lib/catena/governance/crypto.ex`.

**Existing evidence home:** `test/catena/c006_specification_governance_test.exs`.

| Decision | Question | A | B | C | D | Recommended selection and reason |
| --- | --- | --- | --- | --- | --- | --- |
| CP-006-1 | How should new completion evidence use governance? | Reuse typed claims and exact digest binding; preserves the difference between evidence and approval. | Store unstructured success notes only; easy but weak provenance. | Treat a successful build as approval of every claim; convenient but conflates authority and evidence. | Design a replacement proof language immediately; potentially stronger but adds unrelated syntax and trust work. | A (recommended; selected by agent under user delegation): C006’s bounded claim graph is already sufficient for traceable implementation evidence. |
| CP-006-2 | How should new release metadata evolve? | Version artifacts explicitly while keeping semantic selection separate; precise compatibility. | Increment the language revision for every metadata change; simple numbering but mixes axes. | Add ignored fields to signed objects; flexible but destabilizes meaning and canonical bytes. | Freeze all metadata forever; stable bytes but obstructs necessary extension. | A (recommended; selected by agent under user delegation): the existing identity and lifecycle rules require deliberate format changes rather than silent signature drift. |

**Ordered implementation steps:**

1. Preserve typed claim subjects, explicit evidence classes and governance identity through each new package artifact.
2. Bind evidence to semantic digests and keep every runtime-to-verification dependency illegal.
3. Extend artifact audits only after recording format evolution separately from language selection.

**Acceptance evidence:** Positive: supported bounded examples bind to the exact claim and artifact. Negative: invalid signatures, stale digests and runtime references to verification-only definitions reject. Boundary: 20,000-step exhaustion stays distinct from counterexample; erasure removes verification code from final BEAM.

**Completion gate:** C006 remains complete. A new consumer is ready only when the above observations pass on its actual path and its obligation links resolve; defer unsupported semantic extensions to the named owners and public spelling to P109.

## Item 007 — Normative document structure

**Baseline:** C007 complete; preserve and integrate. **Dependencies:** Every later semantic slice; no new language revision.

**Grounding:** [Governing rule](../SPECIFICATION-AUTHORITY.md#repair-and-promotion-workflow); [research rationale](catena-conformance-vocabulary-and-behavior-classes.md). The recommendation cells apply these sources within this item's bounded contract.

**Compiler targets:** `Research: templates/specification.md`; `validate_archive.py`; `sibling lifecycle specification references`.

**Existing evidence home:** `Research: test_validate_archive.py`.

| Decision | Question | A | B | C | D | Recommended selection and reason |
| --- | --- | --- | --- | --- | --- | --- |
| CP-007-1 | Where should planning decisions become authority? | Promote focused specification chapters with evidence; retains archive roles. | Treat this plan as a normative omnibus; faster publication but skips applicability review. | Let compiler tests define unspecified behavior; executable but reverses authority. | Rewrite research notes as normative in place; compact but loses synthesis provenance. | A (recommended; selected by agent under user delegation): the authority policy reserves normative force for properly classified chapters. |
| CP-007-2 | How should cross-cutting documentation changes be checked? | Use deterministic archive validation plus focused semantic review; covers distinct failure modes. | Rely only on Markdown rendering; attractive pages can retain broken obligations. | Rely only on schema validation; misses body contradictions and traceability meaning. | Require manual review of every historical journal on each slice; thorough-looking but needlessly rewrites history. | A (recommended; selected by agent under user delegation): structural checks and applicability review preserve provenance without converting history into current claims. |

**Ordered implementation steps:**

1. Keep plans, source interpretation and executable evidence non-normative; promote only explicit rule chapters.
2. Require each new rule to name its owner, applicability, diagnostics and conformance obligations before implementation claims depend on it.
3. Update directory inventories, conceptual routes and validator-enforced links atomically.

**Acceptance evidence:** Positive: a well-labelled candidate promotes with correct version and traceability. Negative: missing authority links, unclassified normative fences and broken governing anchors fail archive validation. Boundary: contradictory applicable rules block only the disputed claim until explicit resolution.

**Completion gate:** C007 remains complete. A new consumer is ready only when the above observations pass on its actual path and its obligation links resolve; defer unsupported semantic extensions to the named owners and public spelling to P109.

## Item 008 — Editions and feature lifecycle

**Baseline:** C008 complete; preserve and integrate. **Dependencies:** All new semantic slices; P116/P136.

**Grounding:** [Governing rule](../60-specification/editions-and-feature-lifecycle/edition-selection-and-applicability.md#cumulative-applicability); [research rationale](language-editions-and-feature-lifecycle.md). The recommendation cells apply these sources within this item's bounded contract.

**Compiler targets:** `lib/catena/language_version.ex`; `lib/catena/language_selection.ex`; `lib/catena/language_lifecycle.ex`; `lib/catena/package/manifest.ex`.

**Existing evidence home:** `test/catena/c008_editions_lifecycle_test.exs`.

| Decision | Question | A | B | C | D | Recommended selection and reason |
| --- | --- | --- | --- | --- | --- | --- |
| CP-008-1 | How should parallel implementation allocate versions? | Use one serialized registry allocator after draft slices stabilize; avoids collisions. | Give every agent a guessed patch number; fast locally but branches can conflict. | Use checklist numbers as patch numbers; memorable but contradicts existing sequence. | Combine all unfinished semantics into one revision; fewer records but makes review and rollback difficult. | A (recommended; selected by agent under user delegation): exact cumulative revisions require one ordered promotion stream; current next unused patch is 0.1.49. |
| CP-008-2 | How should compatibility be checked during extension? | Keep a retained-revision fixture matrix beside current tests; exposes accidental semantic drift. | Run only the newest default; cheap but misses pinned users. | Permit old pins to float silently; minimal code but violates package selection. | Fork a compiler for every revision; isolates history but multiplies maintenance. | A (recommended; selected by agent under user delegation): C008 requires retained acceptance and explicit transitions in a current compiler. |

**Ordered implementation steps:**

1. Allocate semantic revisions serially after the current latest entry; record explicit applicability and any replacement.
2. Keep package-local exact selection and retained frontends independent from artifact/signature format versions.
3. Exercise old pins and new selections together before promoting each slice.

**Acceptance evidence:** Positive: each retained revision resolves exactly with its recorded features. Negative: unavailable revisions, mismatched selections and unselected previews reject. Boundary: changing the compiler default leaves an explicitly pinned package unchanged; every replacement cites its migration record.

**Completion gate:** C008 remains complete. A new consumer is ready only when the above observations pass on its actual path and its obligation links resolve; defer unsupported semantic extensions to the named owners and public spelling to P109.

## Item 009 — Conformance vocabulary

**Baseline:** C009 complete; preserve and integrate. **Dependencies:** C007/C012; every new diagnostic and runtime producer.

**Grounding:** [Governing rule](../CONFORMANCE-VOCABULARY.md#behavior-classes); [research rationale](catena-conformance-vocabulary-and-behavior-classes.md). The recommendation cells apply these sources within this item's bounded contract.

**Compiler targets:** `Research: CONFORMANCE-VOCABULARY.md`; `validate_archive.py`; `sibling lib/catena/conformance_info.ex`.

**Existing evidence home:** `Research: test_validate_archive.py`; `sibling test/catena/c012_implementation_limits_test.exs`.

| Decision | Question | A | B | C | D | Recommended selection and reason |
| --- | --- | --- | --- | --- | --- | --- |
| CP-009-1 | How should a new failure be classified? | Use the governing behavior class and owner’s stable diagnostic; uniform consequences. | Map every failure to generic invalid input; simple but hides capacity and runtime distinctions. | Expose raw host exceptions as semantics; little adapter code but unstable meaning. | Let individual implementations decide the class; flexible but forfeits portable conformance. | A (recommended; selected by agent under user delegation): the vocabulary separates semantic rejection, bounded evidence, capacity and runtime failure. |
| CP-009-2 | How much implementation variability should be introduced? | Retain one observable rule unless a measured need justifies a bounded declared choice. | Allow all host-dependent behavior; cheap implementation but untestable portability. | Forbid every internal strategy variation; rigid without improving observable semantics. | Document differences only in compiler release notes; practical but lacks governing permission. | A (recommended; selected by agent under user delegation): C009 allows bounded internal variation while preventing silent semantic divergence. |

**Ordered implementation steps:**

1. Classify each proposed behavior as required, invalid, bounded presentation, implementation limit or explicit trap before coding.
2. Keep optional implementation strategy separate from acceptance, effect order and artifact identity.
3. Audit machine profiles against the actual choice register and stable diagnostic families.

**Acceptance evidence:** Positive: profiles enumerate defined limits and choices accurately. Negative: undefined behavior, undocumented implementation-defined choices and invalidity with published partial outputs are rejected by review/checks. Boundary: equivalent diagnostic presentation may vary while stable identity and acceptance stay fixed.

**Completion gate:** C009 remains complete. A new consumer is ready only when the above observations pass on its actual path and its obligation links resolve; defer unsupported semantic extensions to the named owners and public spelling to P109.

## Item 010 — Formal semantic kernel

**Baseline:** C010 complete; preserve and integrate. **Dependencies:** C001–C006; P133/P134 and process extensions.

**Grounding:** [Governing rule](../60-specification/formal-semantic-kernel/sequential-dynamics.md#values-and-evaluation-contexts); [research rationale](catena-formal-semantic-kernel.md). The recommendation cells apply these sources within this item's bounded contract.

**Compiler targets:** `lib/catena/kernel/parser.ex`; `lib/catena/kernel/checker.ex`; `lib/catena/kernel/verifier.ex`; `lib/catena/kernel/stepper.ex`; `lib/catena/kernel/backend.ex`.

**Existing evidence home:** `test/catena/c010_formal_semantic_kernel_test.exs`.

| Decision | Question | A | B | C | D | Recommended selection and reason |
| --- | --- | --- | --- | --- | --- | --- |
| CP-010-1 | Which implementation path should lead semantic completion? | Extend the existing kernel and typed transports before source adoption; fastest route to executable rules. | Build a public parser first; visible progress but prematurely chooses vocabulary. | Replace the kernel with BEAM semantics alone; convenient but loses independent reference. | Build a new mechanized executable language before any runtime work; strong assurance but serializes all delivery. | A (recommended; selected by agent under user delegation): the existing kernel supplies a syntax-neutral experimental boundary and explicit semantics. |
| CP-010-2 | How should disagreements between executors be resolved? | Minimize the witness and consult its governing normative heading; preserve independent evidence. | Always prefer BEAM behavior; deployment realism but host accidents become language rules. | Always prefer the stepper; simple arbitration but models can be wrong. | Change both until tests agree; removes symptoms without establishing correctness. | A (recommended; selected by agent under user delegation): the authority policy makes neither executable path authoritative. |

**Ordered implementation steps:**

1. Use the existing internal S-expression transport for semantic experiments without introducing a public language grammar.
2. For each admitted semantic form extend static rules, independent verification, sequential/actor transitions and BEAM lowering together.
3. Maintain reference/BEAM observations with explicit bounded exploration outcomes; route composed proof work to P133/P134.

**Acceptance evidence:** Positive: checked core executes to equal values/traces on reference and BEAM. Negative: forged core types, malformed actor entries and invalid effects reject independently. Boundary: exploration exhaustion is inconclusive; stuckness, waiting, trap and value remain distinct.

**Completion gate:** C010 remains complete. A new consumer is ready only when the above observations pass on its actual path and its obligation links resolve; defer unsupported semantic extensions to the named owners and public spelling to P109.

## Item 011 — Executable conformance suite

**Baseline:** C011 complete; preserve and integrate. **Dependencies:** C007/C009; reopened P050/P053/P057/P086 and P133/P134.

**Grounding:** [Governing rule](../SPECIFICATION-AUTHORITY.md#references-and-traceability); [research rationale](catena-formal-semantic-kernel.md). The recommendation cells apply these sources within this item's bounded contract.

**Compiler targets:** `Research: 10-maps/conformance-traceability.md`; `validate_archive.py`; `sibling test/catena/*traceability_coverage_test.exs`.

**Existing evidence home:** `Research: test_validate_archive.py`; `sibling per-area conformance suites`.

| Decision | Question | A | B | C | D | Recommended selection and reason |
| --- | --- | --- | --- | --- | --- | --- |
| CP-011-1 | What constitutes evidence completion? | Require behavior assertions matched to each obligation; meaningful but demands review. | Require only obligation tags; scalable but already produced false completeness. | Require 100 percent line coverage; measurable but unrelated to specification coverage. | Require one end-to-end happy path per area; useful smoke test but omits rejection boundaries. | A (recommended; selected by agent under user delegation): the September audit reopened missing effect witnesses despite passing tagged suites. |
| CP-011-2 | How should the large suite be organized? | Retain area ownership and add cross-area integration witnesses; preserves diagnostic locality. | Merge all cases into one global test; fewer files but difficult failure attribution. | Duplicate every case into every dependent area; apparent coverage but maintenance noise. | Replace examples with random generation only; broad exploration but weak targeted regression guarantees. | A (recommended; selected by agent under user delegation): focused ownership plus independent composition cases distinguishes mechanism completeness from behavioral coverage. |

**Ordered implementation steps:**

1. Keep permanent obligation IDs and exact normative anchors attached to focused tests.
2. Separate tag coverage from actual behavioral witnesses and mark partial evidence honestly.
3. Add concrete result/trace assertions for repaired gaps, then update registry status only after the evidence passes.

**Acceptance evidence:** Positive: every new obligation resolves to its cited rule and relevant witness. Negative: tagged tests with no required observation do not earn traced status; invalid final status cells reject. Boundary: the word partial in descriptions/links must not change traced/partial/untraced counts.

**Completion gate:** C011 remains complete. A new consumer is ready only when the above observations pass on its actual path and its obligation links resolve; defer unsupported semantic extensions to the named owners and public spelling to P109.

## Item 012 — Implementation limits

**Baseline:** C012 complete; preserve and integrate. **Dependencies:** C009; P129 capacity and every bounded solver.

**Grounding:** [Governing rule](../IMPLEMENTATION-LIMITS.md#portable-minimum-contract); [research rationale](catena-implementation-limits-and-portability.md). The recommendation cells apply these sources within this item's bounded contract.

**Compiler targets:** `lib/catena/implementation_limits.ex`; `lib/catena/conformance_info.ex`; `lib/catena/otp/compiler.ex`.

**Existing evidence home:** `test/catena/c012_implementation_limits_test.exs`.

| Decision | Question | A | B | C | D | Recommended selection and reason |
| --- | --- | --- | --- | --- | --- | --- |
| CP-012-1 | How should new compiler phases obtain budgets? | Use the central registry with explicit measurement units; consistent reporting. | Embed independent numeric constants; quick but allows drift between phases. | Use host memory availability implicitly; adaptive but irreproducible and unclassified. | Make every finite budget a language constant; predictable but needlessly constrains implementations. | A (recommended; selected by agent under user delegation): C012 separates portable minima and configured implementation limits from semantics. |
| CP-012-2 | How should resource tests remain practical? | Probe exact boundaries in focused suites and use reduced configurable budgets for algorithms. | Stress until the host runs out of memory; realistic worst case but disruptive and nondeterministic. | Test only small valid inputs; cheap but misses off-by-one refusal. | Run all maximal stress tests after every doc change; expensive with no additional semantic evidence. | A (recommended; selected by agent under user delegation): boundary-focused witnesses establish the contract while reserving deployment capacity for P129. |

**Ordered implementation steps:**

1. Consume the central limit registry in new compiler passes and publish actual configured values.
2. Keep refusal transactional and distinguish source invalidity from exhausted evidence and deployment capacity.
3. Add at-floor and beyond-floor probes only where a new consumer or limit is introduced.

**Acceptance evidence:** Positive: 253 callable arguments, 4,096 integer digits, 65,536 decoded literal bytes and 1,048,576 generated module bytes are supported at their applicable floors. Negative: lower profiles cannot claim conformance. Boundary: step/depth exhaustion reports its limit outcome with no partial artifact publication.

**Completion gate:** C012 remains complete. A new consumer is ready only when the above observations pass on its actual path and its obligation links resolve; defer unsupported semantic extensions to the named owners and public spelling to P109.

## Item 013 — Source encoding and normalization

**Baseline:** C013 complete; preserve and integrate. **Dependencies:** C014–C020; P117/G123 and later P109.

**Grounding:** [Governing rule](../60-specification/source-text/source-text-envelope.md#utf-8-byte-domain); [research rationale](catena-source-text-encoding-and-normalization.md). The recommendation cells apply these sources within this item's bounded contract.

**Compiler targets:** `lib/catena/source_text.ex`; `lib/catena/source_span.ex`; `lib/catena/tokenizer.ex`.

**Existing evidence home:** `test/catena/c013_source_text_test.exs`.

| Decision | Question | A | B | C | D | Recommended selection and reason |
| --- | --- | --- | --- | --- | --- | --- |
| CP-013-1 | What representation should downstream tools share? | Reuse lossless source units and byte-span mapping; supports precise diagnostics. | Convert immediately to normalized host strings; convenient but loses original spelling. | Give each tool its own decoder; independent but risks inconsistent acceptance. | Store byte offsets only and recompute scalar positions repeatedly; small storage but duplicated location logic. | A (recommended; selected by agent under user delegation): the source envelope intentionally separates physical bytes from logical scalar locations. |
| CP-013-2 | Where should Unicode normalization occur? | Keep source bytes unchanged and validate identifiers separately; follows split ownership. | Normalize the entire file once; simple but changes literal/comment meaning. | Normalize only when rendering diagnostics; attractive but locations can become misleading. | Let host locale choose normalization; convenient but nondeterministic. | A (recommended; selected by agent under user delegation): C013 preserves scalars while C014 owns NFC identifier acceptance. |

**Ordered implementation steps:**

1. Make the decoded source-unit stream the shared input for lexer and eventual tooling.
2. Preserve original bytes, scalar locations and LF/CRLF mapping through all adapters.
3. Keep malformed input rejection ahead of token interpretation and avoid host replacement decoding.

**Acceptance evidence:** Positive: valid multibyte scalars and LF/CRLF map to the expected original-byte spans. Negative: overlong UTF-8, surrogates, leading BOM and lone CR reject. Boundary: empty input, U+FFFD encoded literally and supplementary scalars remain distinct from malformed-byte recovery.

**Completion gate:** C013 remains complete. A new consumer is ready only when the above observations pass on its actual path and its obligation links resolve; defer unsupported semantic extensions to the named owners and public spelling to P109.

## Item 014 — Identifiers

**Baseline:** C014 complete; preserve and integrate. **Dependencies:** C013/C021/C066; P117/G123/P127.

**Grounding:** [Governing rule](../60-specification/identifiers/identifier-syntax-and-equivalence.md#unicode-data-and-profile); [research rationale](catena-identifiers-and-name-security.md). The recommendation cells apply these sources within this item's bounded contract.

**Compiler targets:** `lib/catena/identifier.ex`; `lib/catena/qualified_name.ex`; `lib/catena/identifier_audit.ex`; `lib/catena/unicode_data.ex`.

**Existing evidence home:** `test/catena/c014_identifiers_test.exs`.

| Decision | Question | A | B | C | D | Recommended selection and reason |
| --- | --- | --- | --- | --- | --- | --- |
| CP-014-1 | How should Unicode acceptance remain stable? | Retain vendored versioned tables; reproducible despite host updates. | Use host identifier predicates; fewer assets but changing acceptance. | Reduce identifiers to ASCII; simple security story but breaks the selected Unicode contract. | Update Unicode automatically in each compiler release; current tables but violates revision pinning. | A (recommended; selected by agent under user delegation): C014 pins properties and normalization to the selected revision. |
| CP-014-2 | How should semantic name roles consume lexical validation? | Validate segments once then apply category and scope rules; clear layering. | Infer namespace solely from Unicode validity; insufficient category information. | Enforce every module-depth restriction in the segment scanner; tight coupling to later syntax. | Duplicate script/confusable checks inside each resolver; local convenience but drifting security policies. | A (recommended; selected by agent under user delegation): lexical identity, namespace role and resolution are distinct existing contracts. |

**Ordered implementation steps:**

1. Reuse pinned Unicode tables and standalone segment validation in all later source adapters.
2. Keep syntactic segment validity separate from namespace role and qualification-depth admission.
3. Propagate exact spelling, confusable evidence and deny-able warnings without adding reserved words.

**Acceptance evidence:** Positive: NFC XID names and allowed escaped existing keywords validate. Negative: non-NFC spelling, forbidden scripts and invalid starts reject. Boundary: host Unicode upgrade leaves accepted sets unchanged; segment-valid deep names may still be rejected by namespace rules.

**Completion gate:** C014 remains complete. A new consumer is ready only when the above observations pass on its actual path and its obligation links resolve; defer unsupported semantic extensions to the named owners and public spelling to P109.

## Item 015 — Whitespace and layout

**Baseline:** C015 complete; preserve and integrate. **Dependencies:** C013/C016/C019; G118/G123/P109.

**Grounding:** [Governing rule](../60-specification/whitespace-and-layout/separators-and-line-continuation.md#resolution-order); [research rationale](catena-whitespace-layout-and-line-continuation.md). The recommendation cells apply these sources within this item's bounded contract.

**Compiler targets:** `lib/catena/layout.ex`; `lib/catena/tokenizer.ex`; `lib/catena/operator.ex`.

**Existing evidence home:** `test/catena/c015_whitespace_layout_test.exs`.

| Decision | Question | A | B | C | D | Recommended selection and reason |
| --- | --- | --- | --- | --- | --- | --- |
| CP-015-1 | How should layout be integrated with tokenization? | Keep the capability/event interface and one resolver; already supports lossless consumers. | Move layout into a future parser; familiar approach but delays source tooling. | Infer continuation from indentation; ergonomic possibility but contradicts fixed non-semantic indentation. | Let each token scanner consume its own separators; convenient locally but loses global frame consistency. | A (recommended; selected by agent under user delegation): C015 fixes abstract events while C019 supplies concrete capabilities. |
| CP-015-2 | How should layout regressions be selected? | Use cross-product cases for frame, neighboring capability and newline ownership; targets interaction bugs. | Snapshot entire source files only; easy but failures obscure the governing cause. | Test only ordinary spaces and LF; fast but misses comments and delimiter edges. | Require formatter output before validating layout; circular dependency on G118. | A (recommended; selected by agent under user delegation): event combinations exercise the actual continuation decision without choosing new grammar. |

**Ordered implementation steps:**

1. Preserve ordered layout events and delegate token capabilities to the existing tokenizer/operator layer.
2. Exercise delimiter frames and comment-contained newlines through one shared resolver.
3. Provide lossless layout data to future formatter/editor work while postponing declaration grammar.

**Acceptance evidence:** Positive: indentation changes preserve meaning and continued parentheses soften permitted LF. Negative: non-ASCII layout spaces and invalid frame endings reject. Boundary: semicolon remains hard inside continued frames; blank LF and raw-literal LF retain correct ownership.

**Completion gate:** C015 remains complete. A new consumer is ready only when the above observations pass on its actual path and its obligation links resolve; defer unsupported semantic extensions to the named owners and public spelling to P109.

## Item 016 — Comments and documentation comments

**Baseline:** C016 complete; preserve and integrate. **Dependencies:** C013/C015/C020; P119/G118/P109.

**Grounding:** [Governing rule](../60-specification/comments-and-documentation-comments/documentation-attachment-and-markdown.md#documentation-body-normalization); [research rationale](catena-comments-and-documentation-comments.md). The recommendation cells apply these sources within this item's bounded contract.

**Compiler targets:** `lib/catena/comment.ex`; `lib/catena/layout.ex`; `lib/catena/tokenizer.ex`.

**Existing evidence home:** `test/catena/c016_comments_documentation_test.exs`.

| Decision | Question | A | B | C | D | Recommended selection and reason |
| --- | --- | --- | --- | --- | --- | --- |
| CP-016-1 | How should documentation enter later tooling? | Expose existing normalized bodies with provenance; renderer can remain a separate consumer. | Render HTML in the lexer; fewer handoffs but mixes syntax and presentation. | Strip all comments during scanning; simplest compiler path but loses documentation/formatting evidence. | Treat every comment as executable documentation; convenient examples but violates explicit selection. | A (recommended; selected by agent under user delegation): the comment contract already separates attachment, normalization and future execution. |
| CP-016-2 | How should nested comments preserve layout? | Retain one event for every logical LF with its original span; exact downstream behavior. | Replace each comment with a single space; cheap but changes separators. | Count newlines without positions; approximate diagnostics but loses lossless reconstruction. | Rescan raw bytes later for layout; modular-looking but repeats recognition and can disagree. | A (recommended; selected by agent under user delegation): C016’s lossless LF ownership connects directly to C015’s resolver. |

**Ordered implementation steps:**

1. Retain exact nested comment scanning, source spans and internal newline events.
2. Pass normalized documentation and attachment events to later documentation tools without executing examples.
3. Keep raw HTML inert and distinguish ordinary near-prefix comments from exact outer documentation forms.

**Acceptance evidence:** Positive: nested blocks preserve body and layout; exact documentation prefixes normalize deterministically. Negative: unterminated nesting and invalid attachment reject. Boundary: four slashes and empty block comments remain ordinary; only the expressly selected future doctest fences may execute under P119.

**Completion gate:** C016 remains complete. A new consumer is ready only when the above observations pass on its actual path and its obligation links resolve; defer unsupported semantic extensions to the named owners and public spelling to P109.

## Item 017 — Atomic literal grammar

**Baseline:** C017 complete; preserve and integrate. **Dependencies:** C013/C018/C040; P104/P105/P109.

**Grounding:** [Governing rule](../60-specification/literal-grammar/literal-forms-and-boundaries.md#exact-numeric-result); [research rationale](catena-literal-grammar.md). The recommendation cells apply these sources within this item's bounded contract.

**Compiler targets:** `lib/catena/literal.ex`; `lib/catena/numeric.ex`; `lib/catena/text.ex`; `lib/catena/tokenizer.ex`.

**Existing evidence home:** `test/catena/c017_literal_grammar_test.exs`.

| Decision | Question | A | B | C | D | Recommended selection and reason |
| --- | --- | --- | --- | --- | --- | --- |
| CP-017-1 | How should scanner results feed semantics? | Keep exact decoded components and provenance until typed elaboration; avoids lossy conversion. | Return only host runtime values; simpler API but cannot verify original rounding or spelling. | Let every frontend reparse literal strings; flexible but duplicates boundary rules. | Expand literal syntax with each library feature; convenient notation but violates the current vocabulary hold. | A (recommended; selected by agent under user delegation): C017 scanning deliberately precedes C018/C040 semantic classification. |
| CP-017-2 | How should raw-literal robustness be improved if needed? | Exercise iterative delimiter matching and exact boundary limits; protects current syntax. | Impose a new small hash limit; easy implementation but changes accepted input. | Treat approximate closing delimiters as recovery; friendly appearance but changes content. | Translate raw literals into cooked source and rescan; reusable scanner but introduces escaping and span errors. | A (recommended; selected by agent under user delegation): the normative arbitrary-hash contract calls for bounded-resource implementation without a new language limit. |

**Ordered implementation steps:**

1. Retain exact literal components and source pieces as the interface to numeric/text elaboration.
2. Pass the established literal meanings through future typed transports without expanding accepted spellings.
3. Test token boundaries beside comments/operators and enforce digit/payload limits before publication.

**Acceptance evidence:** Positive: cooked/raw Text and Bytes and one-scalar Character decode exactly. Negative: bad separators, unsupported suffixes and invalid escapes reject. Boundary: arbitrary hash counts, raw LF, maximum decoded payload and adjacent numeric-looking tokens preserve maximal-boundary rules.

**Completion gate:** C017 remains complete. A new consumer is ready only when the above observations pass on its actual path and its obligation links resolve; defer unsupported semantic extensions to the named owners and public spelling to P109.

## Item 018 — Numeric literal semantics

**Baseline:** C018 complete; preserve and integrate. **Dependencies:** C017/C035/C061; P105.

**Grounding:** [Governing rule](../60-specification/numeric-literal-semantics/decimal-conversion-and-overflow.md#correct-rounding); [research rationale](catena-numeric-literal-semantics.md). The recommendation cells apply these sources within this item's bounded contract.

**Compiler targets:** `lib/catena/numeric.ex`; `lib/catena/literal.ex`; `lib/catena/values.ex`.

**Existing evidence home:** `test/catena/c018_numeric_literal_semantics_test.exs`.

| Decision | Question | A | B | C | D | Recommended selection and reason |
| --- | --- | --- | --- | --- | --- | --- |
| CP-018-1 | Which decimal conversion should later frontends call? | Reuse the exact component converter; known one-step rounding semantics. | Delegate to any host decimal parser; simple but requires unestablished equivalence. | Round through decimal floating point first; familiar but risks double rounding. | Adopt arbitrary precision decimal as Float; useful alternative type but changes the chosen domain. | A (recommended; selected by agent under user delegation): C018 requires one correctly rounded binary64 result from exact decimal meaning. |
| CP-018-2 | How should arithmetic-library work reuse numeric typing? | Keep monomorphic literals and explicit conversion boundaries; predictable composition. | Infer numeric type from surrounding operations; ergonomic but adds defaulting constraints. | Coerce Int to Float automatically; familiar but silently loses precision. | Accept NaN/infinity for library convenience; broad host compatibility but contradicts finite Float. | A (recommended; selected by agent under user delegation): numeric relationships and fault producers have later owners without reopening literal semantics. |

**Ordered implementation steps:**

1. Keep exact integer/rational decimal conversion and finite binary64 classification centralized.
2. Require later numeric producers to declare their own faults and conversions without changing literal defaulting.
3. Reuse exact boundary vectors when new literal transports or arithmetic libraries are integrated.

**Acceptance evidence:** Positive: halfway ties round to even and subnormal values decode correctly. Negative: overflow threshold and mixed implicit coercion reject. Boundary: signed zero, smallest subnormal, underflow to zero and 4,096 component digits preserve exact type/value outcomes.

**Completion gate:** C018 remains complete. A new consumer is ready only when the above observations pass on its actual path and its obligation links resolve; defer unsupported semantic extensions to the named owners and public spelling to P109.

## Item 019 — Operators and punctuation

**Baseline:** C019 complete; preserve and integrate. **Dependencies:** C014–C018/C061; later P109.

**Grounding:** [Governing rule](../60-specification/operators-and-punctuation/precedence-and-associativity.md#the-fixed-ladder); [research rationale](catena-operators-and-punctuation.md). The recommendation cells apply these sources within this item's bounded contract.

**Compiler targets:** `lib/catena/operator.ex`; `lib/catena/tokenizer.ex`; `lib/catena/layout.ex`.

**Existing evidence home:** `test/catena/c019_operators_test.exs`.

| Decision | Question | A | B | C | D | Recommended selection and reason |
| --- | --- | --- | --- | --- | --- | --- |
| CP-019-1 | How should later syntax reuse operator parsing? | Compose with the existing fixed ladder as an expression subparser; minimizes drift. | Replace it with user-defined fixity; flexible but a different language contract. | Let the host Erlang parser determine precedence; easy lowering but incorrect surface assumptions. | Specify a new whole grammar immediately; complete-looking but explicitly postponed by the user. | A (recommended; selected by agent under user delegation): C019 already owns the expression ladder; P109 owns eventual composition. |
| CP-019-2 | How should role-sensitive layout be protected? | Check token identity and prefix/binary role at the existing expression boundary; preserves capability refinement. | Assign minus one universal grammatical role; simpler but loses legitimate expressions. | Hard-code continuation by neighboring characters; compact but mishandles comments and tokens. | Ignore LF around every operator-like character; permissive but accepts reserved punctuation. | A (recommended; selected by agent under user delegation): the token/capability distinction is already normative and needs interaction evidence. |

**Ordered implementation steps:**

1. Preserve the closed existing token inventory and its expression precedence implementation.
2. Check maximal munch and prefix-role capabilities when integrating source consumers.
3. Keep any future application/declaration grammar isolated from these already selected operator meanings.

**Acceptance evidence:** Positive: prefix negation, multiplication and pipe grouping match the fixed ladder. Negative: comparison chains, reserved spellings and unsupported fixity declarations reject. Boundary: longest token match, minus role and dot qualification remain stable across whitespace/comment gaps.

**Completion gate:** C019 remains complete. A new consumer is ready only when the above observations pass on its actual path and its obligation links resolve; defer unsupported semantic extensions to the named owners and public spelling to P109.

## Item 020 — File-to-module relationship

**Baseline:** C020 complete; preserve and integrate. **Dependencies:** C013–C019/C025; P121/P109.

**Grounding:** [Governing rule](../60-specification/files-and-modules/file-units-and-module-binding.md#file-units); [research rationale](catena-files-and-modules.md). The recommendation cells apply these sources within this item's bounded contract.

**Compiler targets:** `lib/catena/file_unit.ex`; `lib/catena/comment.ex`; `lib/catena/package/linker.ex`.

**Existing evidence home:** `test/catena/c020_file_unit_test.exs`.

| Decision | Question | A | B | C | D | Recommended selection and reason |
| --- | --- | --- | --- | --- | --- | --- |
| CP-020-1 | How should discovery expose file units? | Return explicit module/no-module results through the resolver; retains valid empty units. | Treat every .cat file as a module named by basename; easy discovery but contradicts declarations. | Reject empty files; simple build logic but invalidly narrows source. | Infer modules from directory names; convenient convention but new name semantics. | A (recommended; selected by agent under user delegation): C020 deliberately separates file identity from eventual header spelling. |
| CP-020-2 | How should generated-source provenance be recognized? | Use the existing significant-unit marker classifier; exact placement and diagnostics. | Require physical line one only; simple but excludes permitted leading whitespace. | Search for the marker anywhere; robust discovery but incorrectly gives inert text authority. | Trust a build-tool flag instead of source evidence; convenient but loses the source contract. | A (recommended; selected by agent under user delegation): the normative marker rule is more precise than first-line shorthand. |

**Ordered implementation steps:**

1. Use the abstract file-unit resolver for source discovery and package assembly.
2. Preserve no-module units and exact declared-name/basename checks independently from a future module-header grammar.
3. Carry generated-source provenance using the normative first-significant-unit rule, preserving inert later markers.

**Acceptance evidence:** Positive: empty/comment-only .cat files declare nothing; a matching module basename resolves. Negative: multiple modules, wrong extension and basename mismatch reject. Boundary: preceding whitespace may precede a generated marker; earlier significant comments/tokens make a later marker inert.

**Completion gate:** C020 remains complete. A new consumer is ready only when the above observations pass on its actual path and its obligation links resolve; defer unsupported semantic extensions to the named owners and public spelling to P109.

## Item 021 — Namespaces and shadowing

**Baseline:** C021 complete; preserve and integrate. **Dependencies:** C014/C022/C026/C066; P109/G123.

**Grounding:** [Governing rule](../60-specification/namespaces-and-shadowing/shadowing-and-ambiguity.md#cross-origin-precedence); [research rationale](catena-namespaces-and-shadowing.md). The recommendation cells apply these sources within this item's bounded contract.

**Compiler targets:** `lib/catena/namespace.ex`; `lib/catena/qualified_name.ex`; `lib/catena/type/infer.ex`.

**Existing evidence home:** `test/catena/c021_namespaces_test.exs`.

| Decision | Question | A | B | C | D | Recommended selection and reason |
| --- | --- | --- | --- | --- | --- | --- |
| CP-021-1 | How should new adapters resolve program names? | Build the existing category-labelled scope environment first; deterministic lexical resolution. | Resolve names by expected type; powerful disambiguation but contradicts C066. | Use one global table of spellings; small implementation but merges distinct namespaces. | Let each compiler phase resolve again; local flexibility but inconsistent binding identity. | A (recommended; selected by agent under user delegation): the normative namespace inventory is the stable interface for later syntax and tooling. |
| CP-021-2 | How should ambiguous imports be diagnosed? | Retain every competing origin in canonical order; actionable and deterministic. | Choose the first imported origin; simple but import-order dependent. | Prefer a prelude origin; convenient defaults but changes C026 precedence. | Emit only an unknown-name error; generic but hides the actual conflict. | A (recommended; selected by agent under user delegation): C021 requires origin-complete ambiguity rejection rather than heuristic selection. |

**Ordered implementation steps:**

1. Reuse category-labelled scope events and local-over-import precedence in every adapter.
2. Keep constructor uniqueness, quantifier scope and governed identities distinct.
3. Retain full ambiguity origins and order independence when adding preludes and tooling suggestions.

**Acceptance evidence:** Positive: innermost same-category binding shadows silently while other categories remain accessible. Negative: same-domain duplicates and multiple imported origins reject. Boundary: import order permutations and quantifier shadowing preserve resolution; excessive semantic qualification depth stays rejected.

**Completion gate:** C021 remains complete. A new consumer is ready only when the above observations pass on its actual path and its obligation links resolve; defer unsupported semantic extensions to the named owners and public spelling to P109.

## Item 022 — Imports and exports

**Baseline:** C022 complete; preserve and integrate. **Dependencies:** C021/C023/C024/C026/C028; P109.

**Grounding:** [Governing rule](../60-specification/imports-and-exports/import-declarations-and-admission.md#admission); [research rationale](catena-imports-and-exports.md). The recommendation cells apply these sources within this item's bounded contract.

**Compiler targets:** `lib/catena/namespace.ex`; `lib/catena/interface.ex`; `lib/catena/package/linker.ex`.

**Existing evidence home:** `test/catena/c022_import_exports_test.exs`.

| Decision | Question | A | B | C | D | Recommended selection and reason |
| --- | --- | --- | --- | --- | --- | --- |
| CP-022-1 | How should new package consumers obtain visibility? | Decode existing digest-bound export sets; stable separate-compilation contract. | Read dependency source files directly; simple prototype but bypasses interface identity. | Expose all definitions and filter in tooling; easy linking but leaks private names. | Add automatic re-exports for convenience; helpful facades but explicitly excluded by C028. | A (recommended; selected by agent under user delegation): C022 makes admission a checked interface operation, not a naming shortcut. |
| CP-022-2 | How should unused-import checking compose with tooling? | Reuse actual resolved unqualified-use evidence; accurate under shadowing. | Count matching token strings; cheap but confuses qualified and shadowed uses. | Disable the warning whenever imports compile; fewer diagnostics but loses required policy. | Let formatters remove apparently unused imports; attractive automation but insufficient semantic authority. | A (recommended; selected by agent under user delegation): the warning depends on resolved admissions and remains deny-able through manifest policy. |

**Ordered implementation steps:**

1. Consume explicit export and import events against bound interfaces before body checking.
2. Preserve private-by-default visibility and separate qualified access from unqualified admission.
3. Carry unused-import evidence through deny promotion without adding aliases, wildcards or re-export facades.

**Acceptance evidence:** Positive: exported members resolve qualified; an explicit list admits chosen unqualified names. Negative: private members, wildcard/alias events and digest disagreement reject. Boundary: a qualified-only use does not satisfy an unused unqualified admission; an empty admission list still permits qualification.

**Completion gate:** C022 remains complete. A new consumer is ready only when the above observations pass on its actual path and its obligation links resolve; defer unsupported semantic extensions to the named owners and public spelling to P109.

## Item 023 — Abstraction boundaries

**Baseline:** C023 complete; preserve and integrate. **Dependencies:** C002/C022/C028/C046; P093/P094/G095.

**Grounding:** [Governing rule](../60-specification/abstraction-boundaries/authority-and-representation-exclusions.md#representation-is-never-observable); [research rationale](catena-abstraction-boundaries.md). The recommendation cells apply these sources within this item's bounded contract.

**Compiler targets:** `lib/catena/data.ex`; `lib/catena/interface.ex`; `lib/catena/namespace.ex`; `lib/catena/backend/erlang_abstract.ex`.

**Existing evidence home:** `test/catena/c023_abstraction_test.exs`.

| Decision | Question | A | B | C | D | Recommended selection and reason |
| --- | --- | --- | --- | --- | --- | --- |
| CP-023-1 | How should library invariants cross module boundaries? | Use abstract nominal types, validating constructors and observers; existing compositional contract. | Expose all constructors and rely on naming convention; easy use but cannot enforce invariant. | Introduce constructor-only authority; more granular but currently excluded. | Expose a representation predicate and raw host term; flexible but bypasses the abstraction boundary. | A (recommended; selected by agent under user delegation): C023 already sanctions abstract types plus explicit outcome-bearing validation. |
| CP-023-2 | How should the smart-constructor wording ambiguity be handled? | Compare rule text and runtime witness, then make any required explicit clarification with evidence. | Interpret all invalid inputs as static type errors; literal reading but impossible for arbitrary runtime data. | Silently rewrite the test to accept any input; removes rejection without preserving invariant. | Ignore the sentence until the final manual; postpones a foundational inconsistency. | A (recommended; selected by agent under user delegation): a precise observed validation case must establish whether the prose needs clarification before broader claims. |

**Ordered implementation steps:**

1. Retain the exact transparent/abstract authority pair and reject layout or selective-authority extensions.
2. Exercise an abstract library datatype through a validating function and observers across module boundaries.
3. Review the smart-constructor wording against the executable runtime-validation witness before using it in whole-language documentation.

**Acceptance evidence:** Positive: a validated abstract value is consumed only through exports. Negative: external constructor use, selective authority modes and layout attributes reject. Boundary: invalid well-typed input returns the declared failure value without exposing an invalid abstract value; both backend layouts preserve observations.

**Focused consistency gate:** The [sanctioned invariant idiom](../60-specification/abstraction-boundaries/smart-constructor-idiom-and-conformance.md#the-sanctioned-invariant-idiom) says invalid input is rejected “by typing before any value exists.” Establish whether this describes invalid abstract-value construction or incorrectly describes runtime input validation. This plan chooses investigation, not a silent semantic interpretation.

**Completion gate:** C023 remains complete. A new consumer is ready only when the above observations pass on its actual path and its obligation links resolve; defer unsupported semantic extensions to the named owners and public spelling to P109.

## Item 024 — Module dependency cycles

**Baseline:** C024 complete; preserve and integrate. **Dependencies:** C021/C022/C025; P121/P128.

**Grounding:** [Governing rule](../60-specification/module-dependency-cycles/scc-admission-and-resolution.md#the-two-resolution-regimes); [research rationale](catena-dependency-cycles.md). The recommendation cells apply these sources within this item's bounded contract.

**Compiler targets:** `lib/catena/scc.ex`; `lib/catena/namespace.ex`; `lib/catena/package/linker.ex`.

**Existing evidence home:** `test/catena/c024_module_cycles_test.exs`.

| Decision | Question | A | B | C | D | Recommended selection and reason |
| --- | --- | --- | --- | --- | --- | --- |
| CP-024-1 | What should be the build and cache unit? | Reuse maximal SCCs; preserves atomic mutual checking. | Cache each module independently even in cycles; more reuse but violates joint validity. | Treat the entire package as one component; simpler but unnecessary rebuilds. | Reject cyclic modules; easy dependency order but narrows existing semantics. | A (recommended; selected by agent under user delegation): C024 makes signatures break the resolution cycle and the SCC the atomic unit. |
| CP-024-2 | How should parallel compilation respect SCCs? | Parallelize independent components after dependencies resolve; safe speedup. | Parallelize member publication independently; faster appearance but exposes incomplete groups. | Infer signatures jointly from all bodies first; expressive but changes the checking regime. | Use stale member digests to bootstrap checking; practical shortcut but mixes identities. | A (recommended; selected by agent under user delegation): parallelism is an internal strategy only when component-level identity and transactionality remain unchanged. |

**Ordered implementation steps:**

1. Pass module graphs through SCC partitioning before checking or caching.
2. Use companion signatures inside a component and digest-bound imports across components.
3. Preserve atomic publication and canonical joint identity as package build tooling is connected.

**Acceptance evidence:** Positive: self-loop, two-member and longer SCCs check under declared signatures. Negative: missing signature or intra-SCC digest regime mixing rejects transactionally. Boundary: member-order and supported-layout permutations preserve joint digest; changing any member invalidates the whole component cache.

**Completion gate:** C024 remains complete. A new consumer is ready only when the above observations pass on its actual path and its obligation links resolve; defer unsupported semantic extensions to the named owners and public spelling to P109.

## Item 025 — Package identity and dependency resolution

**Baseline:** C025 complete; preserve and integrate. **Dependencies:** C008/C024/C026/C028; P121/P128/P130.

**Grounding:** [Governing rule](../60-specification/package-identity-and-dependencies/resolution-and-lockfile.md#single-version-resolution); [research rationale](catena-package-identity-and-dependencies.md). The recommendation cells apply these sources within this item's bounded contract.

**Compiler targets:** `lib/catena/package/deps.ex`; `lib/catena/package/manifest.ex`; `lib/catena/package/linker.ex`.

**Existing evidence home:** `test/catena/c025_package_deps_test.exs`.

| Decision | Question | A | B | C | D | Recommended selection and reason |
| --- | --- | --- | --- | --- | --- | --- |
| CP-025-1 | How should build tooling consume resolution? | Supply a verified immutable environment to the existing pure resolver; keeps transport separate. | Resolve opportunistically while fetching; responsive but environment changes can affect results. | Delegate all semantics to Hex resolution; convenient transport reuse but loses registry-neutral rules. | Allow multiple versions per name silently; resolves more graphs but changes nominal identity assumptions. | A (recommended; selected by agent under user delegation): C025 fixes deterministic single-version resolution while P121/P130 own transport and trust. |
| CP-025-2 | How should lockfile identity be preserved? | Replay exact pins and digests before compiling; reproducible and tamper-evident. | Re-resolve every build; fresh dependencies but silently changes selected inputs. | Trust package names and versions without digests; easy caching but ignores content identity. | Treat any lock mismatch as ordinary source invalidity; one error path but loses specified stale/tamper distinctions. | A (recommended; selected by agent under user delegation): exact replay is the interface between package semantics and reproducible builds. |

**Ordered implementation steps:**

1. First isolate package-name acceptance for underscore, hyphen and malformed inputs against the exact manifest rule and existing tests.
2. Keep deterministic dependency resolution and exact lock replay independent of fetching/registry trust.
3. Integrate fetch/build tooling through the resolution environment and verify bundle identities before using cached outputs.

**Acceptance evidence:** Positive: highest jointly satisfying version resolves independently of metadata order. Negative: package cycles, unsatisfied constraints, stale/tampered locks and duplicate build-equivalent versions reject. Boundary: 0.x caret/tilde and prerelease restrictions remain fixed; the underscore-name discrepancy receives a documented conflict disposition before new claims rely on it.

**Focused consistency gate:** The [dependencies-field rule](../60-specification/package-identity-and-dependencies/manifest-dependencies-and-versions.md#the-dependencies-field) describes a letters/digits/hyphens spelling domain while explicitly accepting `json_tools`. Source inspection of `lib/catena/package/deps.ex:16` finds a lowercase/digit/hyphen regex that excludes underscores; this is code inspection, not a fresh runtime result. Probe `json_tools`, `json-tools`, `Json_tools` and malformed separator cases through the public dependency decoder, record actual compiler behavior, and give the conflicting normative grammar/example an explicit disposition. Compiler acceptance alone cannot choose the language rule.

**Completion gate:** C025 remains complete. A new consumer is ready only when the above observations pass on its actual path and its obligation links resolve; defer unsupported semantic extensions to the named owners and public spelling to P109.

## Item 026 — Prelude policy

**Baseline:** C026 complete; preserve and integrate. **Dependencies:** C021/C025/C028; P101/P121/P136.

**Grounding:** [Governing rule](../60-specification/prelude-policy/shadowing-optout-and-edition-guarantee.md#the-edition-guarantee); [research rationale](catena-prelude-policy.md). The recommendation cells apply these sources within this item's bounded contract.

**Compiler targets:** `lib/catena/package/manifest.ex`; `lib/catena/package/deps.ex`; `lib/catena/namespace.ex`.

**Existing evidence home:** `test/catena/c026_prelude_policy_test.exs`.

| Decision | Question | A | B | C | D | Recommended selection and reason |
| --- | --- | --- | --- | --- | --- | --- |
| CP-026-1 | How should the future standard library enter scope? | Remain explicit package-local opt-in; respects the zero-implicit-name contract. | Enable it automatically for every package; convenient but changes edition behavior. | Add a magic compiler-only namespace; easy bootstrap but bypasses package identity. | Expose all standard modules globally; familiar scripting model but creates collisions and vocabulary commitments. | A (recommended; selected by agent under user delegation): C026 already specifies ordinary dependency admission and deliberate opt-out. |
| CP-026-2 | How should prelude contents be planned before vocabulary selection? | Describe semantic capabilities and typed interfaces with existing internal names only. | Choose final beginner-facing names now; attractive documentation but expressly deferred. | Freeze every current research synonym as an alias; broad compatibility but bloated public vocabulary. | Delay all library semantics until naming; avoids labels but blocks independent implementation. | A (recommended; selected by agent under user delegation): P101 can settle capability behavior while public naming remains a later user-directed stage. |

**Ordered implementation steps:**

1. Keep absent/null selection as no implicit names and resolve an opted-in prelude as an ordinary dependency.
2. Integrate the future core library without freezing new public names during this work.
3. Verify collision, local shadowing, locking and compatibility with the same paths used for explicit imports.

**Acceptance evidence:** Positive: a selected prelude exports an ordinary import origin and exact lock entry. Negative: duplicate prelude declarations, bad requirement and conflicting imported origin reject. Boundary: absent and null are equivalent; no-prelude builds remain usable and locals still win.

**Completion gate:** C026 remains complete. A new consumer is ready only when the above observations pass on its actual path and its obligation links resolve; defer unsupported semantic extensions to the named owners and public spelling to P109.

## Item 027 — Entry points and application structure

**Baseline:** C027 complete; preserve and integrate. **Dependencies:** C025/C028/C082; P084/G089/P121.

**Grounding:** [Governing rule](../60-specification/entry-points/startup-and-shutdown.md#launch); [research rationale](catena-entry-points.md). The recommendation cells apply these sources within this item's bounded contract.

**Compiler targets:** `lib/catena/entry.ex`; `lib/catena/package/manifest.ex`; `lib/catena/package/linker.ex`; `lib/catena/cli.ex`.

**Existing evidence home:** `test/catena/c027_entry_points_test.exs`.

| Decision | Question | A | B | C | D | Recommended selection and reason |
| --- | --- | --- | --- | --- | --- | --- |
| CP-027-1 | How should runnable packages be wired first? | Wrap existing validated launch in tooling; minimal functional path. | Introduce a universal implicit main function; convenient convention but invents source vocabulary. | Automatically supervise every entry; BEAM-oriented but changes lifetime semantics. | Run module definitions at load time; familiar scripting behavior but contradicts C024/C082. | A (recommended; selected by agent under user delegation): C027 already supplies invocation-only startup independent of future process machinery. |
| CP-027-2 | Where should OS exit behavior be specified? | In P121’s host adapter with explicit mapping from launch reports; separates language values from process status. | Encode OS exit codes into every function result; simple shell integration but changes types. | Treat a normal return as a runtime trap; convenient single error channel but wrong taxonomy. | Rely on raw VM process termination; little code but unspecified reports. | A (recommended; selected by agent under user delegation): the entry contract ends at value/trap report; operational adapters need their own documented boundary. |

**Ordered implementation steps:**

1. Keep entry discovery and validation in the manifest/linker route.
2. Let CLI packaging invoke the existing launch operation and translate its report only at the host boundary.
3. Keep process supervision, lifetime and operational shutdown extensions under their separate owners.

**Acceptance evidence:** Positive: a declared closed entry returns its value and a trapping entry reports the same trap identity. Negative: missing export, nonclosed effects and multiple launch markers reject. Boundary: absent/null/empty entry arrays describe the same library; launch installs no hidden handlers and spawns no implicit process.

**Completion gate:** C027 remains complete. A new consumer is ready only when the above observations pass on its actual path and its obligation links resolve; defer unsupported semantic extensions to the named owners and public spelling to P109.

## Item 028 — API and ABI compatibility

**Baseline:** C028 complete; preserve and integrate. **Dependencies:** C002/C008/C025; P094/P116/P136.

**Grounding:** [Governing rule](../60-specification/api-and-abi-compatibility/breaking-change-matrix.md#the-matrix); [research rationale](catena-api-and-abi-compatibility.md). The recommendation cells apply these sources within this item's bounded contract.

**Compiler targets:** `lib/catena/package/compat.ex`; `lib/catena/interface.ex`; `lib/catena/language_lifecycle.ex`.

**Existing evidence home:** `test/catena/c028_api_compat_test.exs`.

| Decision | Question | A | B | C | D | Recommended selection and reason |
| --- | --- | --- | --- | --- | --- | --- |
| CP-028-1 | How should release tooling classify changes? | Reuse decoded semantic-interface comparison; evaluates the actual contract. | Compare source text diffs; easy integration but unrelated formatting dominates. | Compare bundle digests only; deterministic but any identity change looks breaking. | Trust publisher-provided SemVer labels; simple registry flow but unverified claims. | A (recommended; selected by agent under user delegation): the normative matrix already separates semantic interface changes from representation and identity. |
| CP-028-2 | How should potential lifecycle wording conflict be resolved? | Build a rule/transition comparison and clarify explicit applicability before stronger claims. | Assume later C028 text overrides C008; convenient but lacks a replacement record. | Assume every prototype patch is nonbreaking; conservative API story but contradicts permitted transitions. | Let each compiler choose an interpretation; flexible but creates nonconformance ambiguity. | A (recommended; selected by agent under user delegation): C008’s conflict discipline requires an explicit relationship instead of numeric recency. |

**Ordered implementation steps:**

1. Apply the existing decoded-interface diff matrix in release tooling, retaining representation changes as identity-only unless separately contracted.
2. Exercise additions, removals, changed type/effect schemes and entry sets against exact versions.
3. Before a whole-language compatibility claim, reconcile C028’s monotonic acceptance sentence with C008’s explicit prototype breaking-change policy.

**Acceptance evidence:** Positive: compatible additions and representation-only changes classify as specified. Negative: renamed exports, widened effects and false compatibility claims reject. Boundary: pre-1.0 version increments and retained pins remain exact; interface compatibility is never presented as a behavioral or BEAM ABI theorem.

**Focused consistency gate:** Review [C028 source compatibility](../60-specification/api-and-abi-compatibility/compatibility-layers-and-versions.md#the-four-layers), which says acceptance never removes, against [C008 prototype compatibility](../60-specification/editions-and-feature-lifecycle/edition-selection-and-applicability.md#prototype-compatibility-boundary), which permits documented breaking patches. Establish scope or record a defect; this plan does not silently replace either rule.

**Completion gate:** C028 remains complete. A new consumer is ready only when the above observations pass on its actual path and its obligation links resolve; defer unsupported semantic extensions to the named owners and public spelling to P109.

## Item 029 — Values and strict evaluation

**Baseline:** C029 complete; preserve and integrate. **Dependencies:** C010/C018/C040; P084/P093/P104/P105.

**Grounding:** [Governing rule](../60-specification/values-and-evaluation/strictness-and-terminal-outcomes.md#the-strictness-invariant); [research rationale](catena-values-and-evaluation.md). The recommendation cells apply these sources within this item's bounded contract.

**Compiler targets:** `lib/catena/values.ex`; `lib/catena/kernel/stepper.ex`; `lib/catena/effect/runtime.ex`; `lib/catena/kernel/backend.ex`.

**Existing evidence home:** `test/catena/c029_values_test.exs`.

| Decision | Question | A | B | C | D | Recommended selection and reason |
| --- | --- | --- | --- | --- | --- | --- |
| CP-029-1 | How should value-classifier extensions be introduced? | Update the owning normative slice and every semantic consumer together; prevents half-admitted values. | Accept any host term the backend can carry; convenient but undermines the closed boundary. | Infer valuehood from JSON shape alone; easy transport but confuses metadata and values. | Keep independent classifier lists with no shared audit; local speed but accumulated drift. | A (recommended; selected by agent under user delegation): the value grammar has an explicit future-type entry rule and non-value exclusions. |
| CP-029-2 | How should strictness survive optimizations? | Use observable traces and terminal outcomes to validate transformations; direct semantic evidence. | Assume functional code is free of effects; simple optimizer but invalid in Catena. | Evaluate unused expressions lazily; saves work but changes effects/divergence. | Use host evaluation order without checking; often matches but no guarantee at elaboration boundaries. | A (recommended; selected by agent under user delegation): C029’s strictness and C030’s order are semantic obligations distinct from algebraic laws. |

**Ordered implementation steps:**

1. Use the value classifier and typed-core constructors when integrating new ordinary library data.
2. Preserve strict at-most-once evaluation and distinguish waiting requests from terminal outcomes.
3. Admit any new value category only through its explicit owner, classifier and all consumer boundaries.

**Acceptance evidence:** Positive: closures, records, constructors and later classified Text/Bytes are values with their declared observations. Negative: evidence, capability names, resumptions and raw references are not ordinary values. Boundary: suspended requests are pending; divergence is running; skipped Boolean operands remain the named strictness exceptions.

**Completion gate:** C029 remains complete. A new consumer is ready only when the above observations pass on its actual path and its obligation links resolve; defer unsupported semantic extensions to the named owners and public spelling to P109.

## Item 030 — Evaluation order

**Baseline:** C030 complete; preserve and integrate. **Dependencies:** C029/C031/C032; P050/P053/P057 and every new compound form.

**Grounding:** [Governing rule](../60-specification/evaluation-order/observability-and-trace-agreement.md#dual-target-agreement); [research rationale](catena-evaluation-order.md). The recommendation cells apply these sources within this item's bounded contract.

**Compiler targets:** `lib/catena/effect/reference.ex`; `lib/catena/effect/runtime.ex`; `lib/catena/kernel/stepper.ex`; `lib/catena/kernel/backend.ex`.

**Existing evidence home:** `test/catena/c030_evaluation_order_test.exs`.

| Decision | Question | A | B | C | D | Recommended selection and reason |
| --- | --- | --- | --- | --- | --- | --- |
| CP-030-1 | What should be the order oracle? | An expected request sequence derived from the normative form table plus independent executions. | Only equality between reference and backend; useful but both can share the same error. | Generated source-string ordering; cheap but does not demonstrate execution. | Final value equality only; compact but misses observable ordering. | A (recommended; selected by agent under user delegation): C030 fixes traces, so tests need an independently stated expected sequence. |
| CP-030-2 | How should new effectful forms be tested economically? | Compose small labelled requests around each evaluation position and failure boundary. | Use one enormous application trace; broad but failures become hard to localize. | Use timing delays as order markers; intuitive but scheduler-dependent. | Test pure replacements only; deterministic but erases the observation being claimed. | A (recommended; selected by agent under user delegation): small explicit request traces expose multiplicity and skipped suffixes without adding public vocabulary. |

**Ordered implementation steps:**

1. Assign new compound forms their explicit place in the order table before lowering.
2. Use distinguishable actual requests to observe callee, arguments, field construction and handler installation.
3. Preserve traces across reference, typed-core lowering and BEAM execution, including prefixes terminated by failure.

**Acceptance evidence:** Positive: callee then arguments, subject then callbacks and written record fields produce exact expected request sequences. Negative: a deliberately reordered lowering must fail the trace witness. Boundary: false conjunction, true disjunction and handler abort omit only the specified suffix.

**Completion gate:** C030 remains complete. A new consumer is ready only when the above observations pass on its actual path and its obligation links resolve; defer unsupported semantic extensions to the named owners and public spelling to P109.

## Item 031 — Bindings and sequencing

**Baseline:** C031 complete; preserve and integrate. **Dependencies:** C001/C021/C030/C044; P117/P109.

**Grounding:** [Governing rule](../60-specification/bindings-and-sequencing/binding-structure-and-scope.md#local-binding-structure); [research rationale](catena-bindings-and-sequencing.md). The recommendation cells apply these sources within this item's bounded contract.

**Compiler targets:** `lib/catena/bindings.ex`; `lib/catena/type/infer.ex`; `lib/catena/kernel/checker.ex`; `lib/catena/kernel/stepper.ex`.

**Existing evidence home:** `test/catena/c031_bindings_test.exs`.

| Decision | Question | A | B | C | D | Recommended selection and reason |
| --- | --- | --- | --- | --- | --- | --- |
| CP-031-1 | How should new sequencing consumers lower? | Reuse existing let/discard semantics; one scope and effect model. | Add independent statement sequencing to the core; convenient syntax but duplicated semantics. | Optimize unused bindings by dropping RHS; fast but changes observable effects. | Make every local binding recursive; familiar functional convenience but breaks current scope. | A (recommended; selected by agent under user delegation): C031 supplies the needed expression sequencing without introducing language words. |
| CP-031-2 | How should unused-binding evidence survive refactoring? | Track resolved occurrences within the binding’s body; correct under nested shadowing. | Count spelling occurrences in raw text; easy but comments and shadows fool it. | Treat underscore-prefixed names as nonexistent binders; simple warnings but incorrect scope. | Promote every unused binding to a hard error; stricter style but exceeds policy. | A (recommended; selected by agent under user delegation): the deny-able diagnostic is separate from validity and RHS execution. |

**Ordered implementation steps:**

1. Retain nonrecursive RHS scope and value-before-substitution across every input adapter.
2. Keep sequencing as the existing discard-binding semantics and preserve RHS effects.
3. Integrate warnings using resolved scope and manifest deny policy without introducing a new statement form.

**Acceptance evidence:** Positive: a shadowed binding observes the previous outer value on its RHS and the new value in its body. Negative: otherwise-unbound self reference rejects; pattern-valued binders remain absent. Boundary: unused RHS effects still occur and underscore-prefixed warning exemptions do not erase evaluation.

**Completion gate:** C031 remains complete. A new consumer is ready only when the above observations pass on its actual path and its obligation links resolve; defer unsupported semantic extensions to the named owners and public spelling to P109.

## Item 032 — Functions and calls

**Baseline:** C032 complete; preserve and integrate. **Dependencies:** C001/C030/C031/C034; P094.

**Grounding:** [Governing rule](../60-specification/functions-and-calls/arity-and-application.md#the-semantic-unary-model); [research rationale](catena-functions-and-calls.md). The recommendation cells apply these sources within this item's bounded contract.

**Compiler targets:** `lib/catena/type/infer.ex`; `lib/catena/kernel/checker.ex`; `lib/catena/backend/erlang_abstract.ex`; `lib/catena/kernel/backend.ex`.

**Existing evidence home:** `test/catena/c032_functions_test.exs`.

| Decision | Question | A | B | C | D | Recommended selection and reason |
| --- | --- | --- | --- | --- | --- | --- |
| CP-032-1 | How should a practical calling convention relate to unary semantics? | Permit internal saturated-call optimization with proven observational equivalence; efficient and faithful. | Expose BEAM fixed arity as the language model; simple host mapping but breaks free partial application. | Box every application forever; simple correctness baseline but may leave avoidable overhead. | Rewrite all functions into tuple-taking values; convenient ABI but changes source types. | A (recommended; selected by agent under user delegation): C032 fixes semantics while P094 may optimize representation under explicit equivalence. |
| CP-032-2 | How should tail-call integration be checked? | Retain deep execution witnesses in each changed tail-position path; observes the guarantee. | Inspect only emitted function names; cheap but cannot establish bounded stack use. | Benchmark shallow loops; quick feedback but weak tail evidence. | Promise stack safety for all recursion; attractive but exceeds C034. | A (recommended; selected by agent under user delegation): proper tail calls are a concrete runtime obligation with already established stress evidence. |

**Ordered implementation steps:**

1. Keep functions semantically unary and lower multi-argument operations as ordered application steps.
2. Preserve lexical immutable capture and first-class prefix application when specifying the BEAM calling convention.
3. Keep tail positions visible through match, closure and handler lowering before optimizing calls.

**Acceptance evidence:** Positive: curried and partial applications agree across evaluators and BEAM. Negative: applying a non-function is a type error, not a new arity category. Boundary: the existing five-million-step tail-recursion witness completes; closure capture remains fixed under later shadowing.

**Completion gate:** C032 remains complete. A new consumer is ready only when the above observations pass on its actual path and its obligation links resolve; defer unsupported semantic extensions to the named owners and public spelling to P109.

## Item 033 — Conditionals and branching

**Baseline:** C033 complete; preserve and integrate. **Dependencies:** C002/C003/C030/C032/C044; later P109.

**Grounding:** [Governing rule](../60-specification/branching/branch-rules-consolidated.md#the-consolidated-rules); [research rationale](catena-branching.md). The recommendation cells apply these sources within this item's bounded contract.

**Compiler targets:** `lib/catena/pattern/coverage.ex`; `lib/catena/condition.ex`; `lib/catena/kernel/stepper.ex`; `lib/catena/kernel/backend.ex`.

**Existing evidence home:** `test/catena/c033_branching_test.exs`.

| Decision | Question | A | B | C | D | Recommended selection and reason |
| --- | --- | --- | --- | --- | --- | --- |
| CP-033-1 | What selection representation should later features target? | Existing typed match nodes; shares coverage and commitment semantics. | A second conditional core with separate evaluator cases; simple local lowering but duplicated rules. | Host exception-based branch retry; flexible but violates irreversible commitment. | Choose a new public conditional syntax now; visible progress but vocabulary is deferred. | A (recommended; selected by agent under user delegation): C033 already makes Bool conditionals a semantics-preserving future desugaring. |
| CP-033-2 | How should branch optimization be constrained? | Compare ordered selection traces including failed conditions and selected-body failure. | Reorder clauses by estimated likelihood; faster dispatch but may change semantics. | Drop conditions after pattern coverage succeeds; avoids checks but changes acceptance. | Check only exhaustiveness before optimizing freely; coverage alone does not establish ordering. | A (recommended; selected by agent under user delegation): the consolidated table makes order and commitment independent obligations from coverage. |

**Ordered implementation steps:**

1. Use match as the single selection core when implementing later expression-level conveniences.
2. Maintain scrutinee-once, pattern-before-condition, source order and irreversible commitment.
3. Keep future conditional spelling deferred while retaining its already specified Bool-match meaning.

**Acceptance evidence:** Positive: guarded fallthrough reaches the next applicable clause and runs only its body. Negative: branch-type disagreement, missing coverage and redundant clauses reject. Boundary: a selected body’s trap never retries another clause; tail-position calls retain C032’s guarantee.

**Completion gate:** C033 remains complete. A new consumer is ready only when the above observations pass on its actual path and its obligation links resolve; defer unsupported semantic extensions to the named owners and public spelling to P109.

## Item 034 — Recursion and termination

**Baseline:** C034 complete; preserve and integrate. **Dependencies:** C001/C024/C032/C038; P133/P134.

**Grounding:** [Governing rule](../60-specification/recursion-and-termination/the-separation-table.md#the-separation); [research rationale](catena-recursion-and-termination.md). The recommendation cells apply these sources within this item's bounded contract.

**Compiler targets:** `lib/catena/kernel/stepper.ex`; `lib/catena/condition.ex`; `lib/catena/specification.ex`; `lib/catena/categorical/law.ex`.

**Existing evidence home:** `test/catena/c034_recursion_test.exs`.

| Decision | Question | A | B | C | D | Recommended selection and reason |
| --- | --- | --- | --- | --- | --- | --- |
| CP-034-1 | What should a compiler promise about general recursion? | Preserve sound typing and proper tail calls without claiming totality; matches the program model. | Reject all recursion; easy termination but destroys admitted programs. | Infer totality automatically for every function; attractive guarantee but undecidable generally. | Treat bounded test completion as universal termination; convenient evidence but invalid extrapolation. | A (recommended; selected by agent under user delegation): category-theory laws require their stated total domains; ordinary Catena still admits divergence. |
| CP-034-2 | How should new compile-time computation be admitted? | Ship its total-or-bounded regime and distinct exhaustion evidence in the same slice. | Use an unbounded evaluator initially; easy implementation but can hang compilation. | Apply the runtime scheduler timeout as semantics; operationally safe but nondeterministic. | Silently reduce the existing example budget for speed; convenient tests but violates retained evidence. | A (recommended; selected by agent under user delegation): C034’s entry rule protects compiler termination without weakening runtime expressiveness. |

**Ordered implementation steps:**

1. Keep unrestricted program recursion distinct from bounded compiler-time evaluators.
2. Require each new meta-evaluator to name a terminating algorithm or explicit budget and outcome.
3. Preserve monomorphic/annotated recursion typing separately from runtime termination observations.

**Acceptance evidence:** Positive: legal recursive programs execute, and tail-recursive cases remain stack safe. Negative: recursive condition predicates reject under C003; no termination claim is inferred from a function type. Boundary: exhausted reference evaluation remains inconclusive/running evidence rather than a trap or proof of divergence.

**Completion gate:** C034 remains complete. A new consumer is ready only when the above observations pass on its actual path and its obligation links resolve; defer unsupported semantic extensions to the named owners and public spelling to P109.

## Item 035 — Equality and ordering

**Baseline:** C035 complete; preserve and integrate. **Dependencies:** C018/C037/C040/C061; P102/P104/P105.

**Grounding:** [Governing rule](../60-specification/equality-and-ordering/float-equality-and-semantics.md#bit-exact-equality); [research rationale](catena-equality-and-ordering.md). The recommendation cells apply these sources within this item's bounded contract.

**Compiler targets:** `lib/catena/values.ex`; `lib/catena/data.ex`; `lib/catena/kernel/checker.ex`; `lib/catena/kernel/backend.ex`.

**Existing evidence home:** `test/catena/c035_equality_test.exs`.

| Decision | Question | A | B | C | D | Recommended selection and reason |
| --- | --- | --- | --- | --- | --- | --- |
| CP-035-1 | How should collection keys obtain equality? | Use the existing comparable-type contract and explicit library operation constraints. | Delegate directly to BEAM term equality; fast but may conflate signed zeros and foreign shapes. | Use object identity for speed; efficient hashing shortcut but violates C037. | Select a trait instance implicitly for built-in equality; extensible but contradicts non-overloadability. | A (recommended; selected by agent under user delegation): C035/C040 define semantic equality independently of storage and trait dictionaries. |
| CP-035-2 | How should Float semantics be protected across libraries? | Share bit-level boundary vectors with comparison, conversion and future hashing tests. | Use host numeric comparison everywhere; simple but collapses signed zero. | Forbid negative zero at library entry; easier equality but narrows Float. | Add NaN comparison cases as accepted values; host-friendly but outside the finite domain. | A (recommended; selected by agent under user delegation): the selected Float equivalence needs consistent consumers, not a new numeric vocabulary. |

**Ordered implementation steps:**

1. Use the declared comparable/orderable domains in new library operations and key constraints.
2. Preserve bit-exact Float equality and record field-order independence on every lowering path.
3. Keep built-in comparison distinct from trait-instance APIs and the restricted guard fragment.

**Acceptance evidence:** Positive: structural values compare by content and finite Float ordering distinguishes negative from positive zero. Negative: mixed numeric types, closures and process handles reject comparison. Boundary: Text/Character/Bytes use their later content order, while Bool remains equality-only and Unit retains its declared exclusion.

**Completion gate:** C035 remains complete. A new consumer is ready only when the above observations pass on its actual path and its obligation links resolve; defer unsupported semantic extensions to the named owners and public spelling to P109.

## Item 036 — Runtime failure taxonomy

**Baseline:** C036 complete; preserve and integrate. **Dependencies:** C010/C034/C081; G080/G088/G095/G096/P103/P105.

**Grounding:** [Governing rule](../60-specification/runtime-failure-taxonomy/the-six-categories.md#the-entry-rule); [research rationale](catena-runtime-failure-taxonomy.md). The recommendation cells apply these sources within this item's bounded contract.

**Compiler targets:** `lib/catena/kernel/stepper.ex`; `lib/catena/kernel/backend.ex`; `lib/catena/effect/runtime.ex`; `lib/catena/entry.ex`.

**Existing evidence home:** `test/catena/c036_failure_test.exs`.

| Decision | Question | A | B | C | D | Recommended selection and reason |
| --- | --- | --- | --- | --- | --- | --- |
| CP-036-1 | How should new foreign/arithmetic faults enter? | Define each producer’s trap or typed-result contract explicitly with its admitting slice. | Expose raw host exception classes directly; convenient but unstable and unclassified. | Turn every error into an ordinary null value; simple API but loses typed meaning. | Add catchable exceptions by default; familiar recovery but changes the terminal taxonomy. | A (recommended; selected by agent under user delegation): C036 and C081 already route producer failures without allowing a second implicit outcome class. |
| CP-036-2 | How should resource cleanup interact with terminal failure? | Make G080 state any required explicit revision and order guarantees before changing runtime behavior. | Attach cleanup to every trap silently; desirable intuition but unsupported semantic change. | Claim garbage collection satisfies cleanup; easy implementation but ignores external resources. | Ban resources permanently to preserve traps; avoids interaction but forecloses the requested language goal. | A (recommended; selected by agent under user delegation): a useful functional runtime needs an explicit cleanup design rather than an inferred exception mechanism. |

**Ordered implementation steps:**

1. Classify every future fault producer before implementing it: ordinary typed value, terminal trap or external operational event.
2. Preserve reason identity and terminal trap observations across reference and BEAM adapters.
3. Require explicit applicability changes for resource cleanup or process signaling that would alter the existing trap boundary.

**Acceptance evidence:** Positive: the same explicit reason reaches the trap outcome on both executors. Negative: a trapped computation cannot resume or retry a clause. Boundary: child trap discards its mailbox without changing the current spawner contract; a collection miss is a value and divergence remains running.

**Completion gate:** C036 remains complete. A new consumer is ready only when the above observations pass on its actual path and its obligation links resolve; defer unsupported semantic extensions to the named owners and public spelling to P109.

## Item 037 — Resource and allocation observability

**Baseline:** C037 complete; preserve and integrate. **Dependencies:** C023/C032/C035; P084/P085/P093/G095/G124.

**Grounding:** [Governing rule](../60-specification/resource-observability/the-observability-model.md#the-six-way-classification); [research rationale](catena-resource-observability.md). The recommendation cells apply these sources within this item's bounded contract.

**Compiler targets:** `lib/catena/values.ex`; `lib/catena/kernel/stepper.ex`; `lib/catena/kernel/backend.ex`.

**Existing evidence home:** `test/catena/c037_observability_test.exs`.

| Decision | Question | A | B | C | D | Recommended selection and reason |
| --- | --- | --- | --- | --- | --- | --- |
| CP-037-1 | Where should debugging expose implementation details? | Use G124’s external instrumentation channel; preserves ordinary program meaning. | Add address/GC reflection to all values; convenient debugging but changes abstraction. | Encode allocation IDs into equality; easy identity tracking but breaks interchangeable values. | Forbid all debugger visibility; strong abstraction but unnecessarily blocks tooling. | A (recommended; selected by agent under user delegation): C037 distinguishes implementation observation by tools from program-observable identity. |
| CP-037-2 | How should representation optimizations be validated? | Compare values, requests and allowed process observations while varying layout/allocation. | Require byte-identical runtime heaps; strong identity but impossible and not promised. | Compare wall-clock timings as semantics; useful benchmarks but environment-dependent. | Assume any memory optimization is invisible; fast iteration but can change effect or alias behavior. | A (recommended; selected by agent under user delegation): categorical abstraction supports representation independence only under the declared observable relation. |

**Ordered implementation steps:**

1. Maintain semantic value observations while allowing internal allocation/layout changes.
2. Keep opaque process identity restricted to its admitted operations and preserve non-comparability.
3. Design debugging and cost instrumentation through external tooling or separately specified boundaries.

**Acceptance evidence:** Positive: independently allocated equal records have the same semantic observations. Negative: address, closure identity, GC hooks and handle comparison are not ordinary language operations. Boundary: tail-call completion remains observable, but message-copy strategy and stack-frame layout do not become values.

**Completion gate:** C037 remains complete. A new consumer is ready only when the above observations pass on its actual path and its obligation links resolve; defer unsupported semantic extensions to the named owners and public spelling to P109.

## Item 038 — Compile-time evaluation

**Baseline:** C038 complete; preserve and integrate. **Dependencies:** C003/C004/C006/C034; P121/P128/P131.

**Grounding:** [Governing rule](../60-specification/compile-time-evaluation/the-compile-time-stance.md#generated-derivations); [research rationale](catena-compile-time-evaluation.md). The recommendation cells apply these sources within this item's bounded contract.

**Compiler targets:** `lib/catena/derive.ex`; `lib/catena/specification.ex`; `lib/catena/categorical/law.ex`; `lib/catena/package/linker.ex`.

**Existing evidence home:** `test/catena/c038_compile_time_test.exs`.

| Decision | Question | A | B | C | D | Recommended selection and reason |
| --- | --- | --- | --- | --- | --- | --- |
| CP-038-1 | How should repetitive library code be generated now? | Use existing checked derivation templates or external build generation; avoids new compile-time language features. | Add a macro evaluator; flexible but requires a new totality and authority contract. | Execute library initialization during compilation; convenient constants but violates the no-execution boundary. | Hand-expand every derivation into unchecked backend forms; fast generation but skips verifier guarantees. | A (recommended; selected by agent under user delegation): C038 already permits deterministic internal generation followed by ordinary checking. |
| CP-038-2 | What should deterministic generation evidence compare? | Compare typed output, provenance and final artifacts under identical inputs; covers semantics and reproducibility. | Compare generated source formatting only; readable but misses selected identities. | Only assert generation terminates once; useful smoke test but no determinism evidence. | Ignore metadata in all comparisons; reduces noise but can hide provenance/digest changes. | A (recommended; selected by agent under user delegation): the contract separates display-only data from meaningful provenance and artifact identity. |

**Ordered implementation steps:**

1. Keep derived definitions as deterministic compiler-internal templates with compiler_derived provenance.
2. Run generated output through ordinary checking and independent verification before use.
3. Preserve absence of user constant execution, macros and attributes while later tooling generates ordinary source externally.

**Acceptance evidence:** Positive: repeated derivation yields identical checked artifacts and records compiler-derived provenance. Negative: unsupported macro/attribute/constant evaluator forms remain rejected. Boundary: bounded laws/examples and acyclic conditions retain distinct outcomes and exact budgets.

**Completion gate:** C038 remains complete. A new consumer is ready only when the above observations pass on its actual path and its obligation links resolve; defer unsupported semantic extensions to the named owners and public spelling to P109.

## Item 039 — Algebraic data declaration boundary

**Baseline:** C039 complete; preserve and integrate. **Dependencies:** C001/C002/C062; P101 and later P109.

**Grounding:** [Governing rule](../60-specification/data-and-patterns/declarations-and-nominal-identity.md#recursive-groups); [research rationale](algebraic-data-types.md). The recommendation cells apply these sources within this item's bounded contract.

**Compiler targets:** `lib/catena/ast/decoder.ex`; `lib/catena/data.ex`; `lib/catena/kind.ex`; `lib/catena/kernel/parser.ex`.

**Existing evidence home:** `test/catena/c002_data_test.exs`.

| Decision | Question | A | B | C | D | Recommended selection and reason |
| --- | --- | --- | --- | --- | --- | --- |
| CP-039-1 | How should new library declarations be authored before source vocabulary? | Use existing JSON/kernel semantic inputs; immediately executable and meaning-focused. | Choose final datatype keywords and punctuation now; readable but user-deferred. | Embed every datatype as Elixir structs; convenient host tooling but bypasses Catena identity. | Wait for P109 before specifying data; avoids temporary formats but blocks semantic libraries. | A (recommended; selected by agent under user delegation): C039 already completes resolved declaration structure independently of eventual public syntax. |
| CP-039-2 | How should declaration adapters preserve advanced information? | Carry explicit kinds, existentials and refined results to existing validation. | Erase them before checking; simpler AST but loses soundness boundaries. | Infer all refined results heuristically; concise input but weakens explicit annotation guarantees. | Reject all advanced declarations on new transports; safe subset but cannot claim full existing support. | A (recommended; selected by agent under user delegation): the nominal declaration contract requires exact information at the resolved boundary. |

**Ordered implementation steps:**

1. Encode future library datatypes with existing semantic declaration forms, kinded parameters and atomic recursive groups.
2. Retain explicit existential/refined-result information through interfaces and typed core.
3. Keep final source declaration spelling deferred while preserving the already specified resolved data model.

**Acceptance evidence:** Positive: nullary, positional and named-product constructors elaborate with canonical nominal identities. Negative: duplicate names, wrong kinds, malformed refined results and inaccessible constructors reject. Boundary: empty and mutually recursive groups publish atomically; negative occurrences do not automatically earn fold derivation.

**Completion gate:** C039 remains complete. A new consumer is ready only when the above observations pass on its actual path and its obligation links resolve; defer unsupported semantic extensions to the named owners and public spelling to P109.

## Item 040 — Built-in data model

**Baseline:** C040 complete; preserve and integrate. **Dependencies:** C017/C018/C029/C035; P101/P104/P097/G098/P109.

**Grounding:** [Governing rule](../60-specification/built-in-data-model/the-twelve-way-classification.md#the-decision); [research rationale](catena-built-in-data-model.md). The recommendation cells apply these sources within this item's bounded contract.

**Compiler targets:** `lib/catena/text.ex`; `lib/catena/values.ex`; `lib/catena/data.ex`; `lib/catena/kernel/type.ex`.

**Existing evidence home:** `test/catena/c040_data_model_test.exs`.

| Decision | Question | A | B | C | D | Recommended selection and reason |
| --- | --- | --- | --- | --- | --- | --- |
| CP-040-1 | How should collections relate to built-ins? | Keep them ordinary library data with separately specified APIs; preserves explicit classification. | Promote every common collection to a primitive; convenient optimization but enlarges trusted core. | Represent all collections as structural records; reusable rows but conflates nominal and structural roles. | Use unrestricted host containers; efficient bootstrap but requires absent foreign guarantees. | A (recommended; selected by agent under user delegation): C040 deliberately keeps collection design in P101/P102 while owning primitive meanings. |
| CP-040-2 | How should text-like values first reach full execution? | Extend existing typed transports and both execution paths in a focused integration slice. | Treat scanned payloads as already executable language values everywhere; quick but ignores frontend absence. | Choose a new source literal syntax; unnecessary because C017 already defines spelling. | Implement only backend decoding; runtime progress but no independent checked semantics. | A (recommended; selected by agent under user delegation): the current classifier-level completion does not by itself claim every frontend can encode these values. |

**Ordered implementation steps:**

1. Keep Text, Character and Bytes semantic domains separate from source provenance and host representations.
2. Use ordinary nominal declarations for List/map/set rather than promoting library types to compiler primitives.
3. When a transport first carries text-like literals, connect their types, verifier cases, runtime observations and comparison together.

**Acceptance evidence:** Positive: Text scalar content and Bytes octets elaborate deterministically and compare in their declared order. Negative: a multi-scalar Character, unclassified host reference and implicit collection primitive reject at the appropriate boundary. Boundary: canonically equivalent but distinct scalar sequences are not silently normalized; empty Text and Bytes remain valid.

**Completion gate:** C040 remains complete. A new consumer is ready only when the above observations pass on its actual path and its obligation links resolve; defer unsupported semantic extensions to the named owners and public spelling to P109.

## Item 041 — Structural records and variants

**Baseline:** C041 complete; preserve and integrate. **Dependencies:** C001/C030/C035/C040/C066; P109/P133.

**Grounding:** [Governing rule](../60-specification/structural-records-and-variants/rows-and-representation.md#the-row-model); [research rationale](catena-structural-records.md). The recommendation cells apply these sources within this item's bounded contract.

**Compiler targets:** `lib/catena/kernel/type.ex`; `lib/catena/kernel/checker.ex`; `lib/catena/kernel/stepper.ex`; `lib/catena/kernel/backend.ex`; `lib/catena/type/row.ex`.

**Existing evidence home:** `test/catena/c041_records_test.exs`.

| Decision | Question | A | B | C | D | Recommended selection and reason |
| --- | --- | --- | --- | --- | --- | --- |
| CP-041-1 | How should row-polymorphic APIs be implemented? | Use open type signatures over closed record values; matches the existing row calculus. | Add open runtime record fragments; flexible merging but new expression semantics. | Erase labels and use field positions as meaning; efficient representation but breaks structural identity. | Replace rows with nominal subtyping; familiar OO model but changes inference. | A (recommended; selected by agent under user delegation): C041 preserves structural composition through type constraints without exposing runtime representation. |
| CP-041-2 | How should row canonicalization interact with evaluation? | Canonicalize semantic type/identity data after preserving written evaluation order. | Sort field expressions before evaluation; deterministic storage but reorders effects. | Keep declaration order in equality; simple maps but violates semantic field-order independence. | Avoid canonicalization everywhere; easy provenance but risks unstable interface identity. | A (recommended; selected by agent under user delegation): the operation table explicitly assigns order to evaluation and unordered labels to meaning. |

**Ordered implementation steps:**

1. Reuse the seven existing semantic operations for record/variant integration.
2. Keep runtime values closed and unique-labelled while open tails remain type-position constraints.
3. Preserve written field evaluation order independently of row identity and structural equality.

**Acceptance evidence:** Positive: select/update/extend/restrict and variant dispatch agree on reference and BEAM. Negative: duplicate labels and impossible missing-label operations reject statically. Boundary: permuting pure fields preserves equality while effectful construction retains written request order; open signatures instantiate over closed values.

**Completion gate:** C041 remains complete. A new consumer is ready only when the above observations pass on its actual path and its obligation links resolve; defer unsupported semantic extensions to the named owners and public spelling to P109.

## Item 042 — Collection construction and update

**Baseline:** C042 complete; preserve and integrate. **Dependencies:** C002/C035/C040; P101/P102/P103.

**Grounding:** [Governing rule](../60-specification/collection-construction-and-update/miss-as-value-and-complexity.md#miss-as-value); [research rationale](catena-collection-operations.md). The recommendation cells apply these sources within this item's bounded contract.

**Compiler targets:** `lib/catena/data.ex`; `lib/catena/kernel/checker.ex`; `lib/catena/kernel/backend.ex`; `lib/catena/standard_list.ex`.

**Existing evidence home:** `test/catena/c042_collections_test.exs`.

| Decision | Question | A | B | C | D | Recommended selection and reason |
| --- | --- | --- | --- | --- | --- | --- |
| CP-042-1 | What implementation mechanism should collections use initially? | Ordinary declarations and match recursion with existing backend optimization; compositional and testable. | Dedicated collection-update core opcodes for every type; fast paths but expands language machinery. | Mutable host objects behind unrestricted aliases; efficient updates but incompatible persistence assumptions. | Only expose host Erlang libraries without typed wrappers; immediate utility but bypasses foreign contracts. | A (recommended; selected by agent under user delegation): C042 makes constructor application and match recursion sufficient for the language layer. |
| CP-042-2 | Where should collection performance promises live? | In P101/P102’s named library-operation contracts with measured implementation evidence. | In universal language semantics for every representation; strong claim but contradicts C042. | Nowhere; easy specification but leaves users unable to choose suitable operations. | Infer asymptotic cost from categorical laws; elegant appearance but laws do not establish complexity. | A (recommended; selected by agent under user delegation): the categorical synthesis and C042 separate extensional structure from operational cost. |

**Ordered implementation steps:**

1. Implement library construction and persistent update as ordinary typed constructor/match programs.
2. Require each key-carrying library declaration to state duplicate handling and key-equality constraints.
3. Represent lookup/bounds misses as declared outcome values and place operation costs in library contracts.

**Acceptance evidence:** Positive: declared List construction, length and replacement agree across execution paths. Negative: noncomparable keys cannot enter equality-dependent operations. Boundary: empty/missing lookup yields a typed value without a trap; old persistent values remain unchanged after update.

**Completion gate:** C042 remains complete. A new consumer is ready only when the above observations pass on its actual path and its obligation links resolve; defer unsupported semantic extensions to the named owners and public spelling to P109.

## Item 043 — Initial pattern grammar

**Baseline:** C043 complete; preserve and integrate. **Dependencies:** C002/C003/C044/C045; P109 and P099.

**Grounding:** [Governing rule](../60-specification/data-and-patterns/construction-and-pattern-typing.md#complete-012-pattern-grammar); [research rationale](algebraic-data-types.md). The recommendation cells apply these sources within this item's bounded contract.

**Compiler targets:** `lib/catena/ast/decoder.ex`; `lib/catena/data.ex`; `lib/catena/pattern/coverage.ex`; `lib/catena/kernel/parser.ex`.

**Existing evidence home:** `test/catena/c002_data_test.exs`.

| Decision | Question | A | B | C | D | Recommended selection and reason |
| --- | --- | --- | --- | --- | --- | --- |
| CP-043-1 | How should future notation consume initial patterns? | Elaborate to existing resolved patterns only where semantics already permits; retains checker reuse. | Treat arbitrary expression syntax as patterns; uniform parser but admits calls/effects. | Let backend pattern support decide acceptance; convenient but host forms exceed Catena. | Invent final pattern spellings now; readable but violates the vocabulary hold. | A (recommended; selected by agent under user delegation): C043 completes the initial semantic pattern set; syntax adoption has a later owner. |
| CP-043-2 | How should pattern binding consistency be enforced? | Keep one typed pattern environment and check every alternative’s binder agreement. | Union all alternative binders; permissive but some branch variables lack values. | Pick binders from the first alternative; simple but hides inconsistent branches. | Reject all nested/or patterns in new adapters; safe subset but narrows existing support. | A (recommended; selected by agent under user delegation): the construction/pattern rules make binder agreement a static invariant. |

**Ordered implementation steps:**

1. Preserve the resolved wildcard/binder/literal/tuple/constructor/as/or pattern forms on every relevant adapter.
2. Keep binder consistency and constructor authority in pattern typing rather than parser heuristics.
3. Treat any later list/record/binary convenience as its own explicit admission or desugaring with the correct owner.

**Acceptance evidence:** Positive: nested positional/named constructor patterns and valid as/or binders type correctly. Negative: inconsistent binders, inaccessible constructors and excluded programmable patterns reject. Boundary: literal-pattern domains remain those of the admitted frontend; a new transport cannot silently add a pattern family.

**Completion gate:** C043 remains complete. A new consumer is ready only when the above observations pass on its actual path and its obligation links resolve; defer unsupported semantic extensions to the named owners and public spelling to P109.

## Item 044 — Refutability by context

**Baseline:** C044 complete; preserve and integrate. **Dependencies:** C002/C031/C033/C045; C047–C058/P086/D083.

**Grounding:** [Governing rule](../60-specification/pattern-contexts/the-three-context-classes.md#the-classification); [research rationale](catena-pattern-contexts.md). The recommendation cells apply these sources within this item's bounded contract.

**Compiler targets:** `lib/catena/ast/decoder.ex`; `lib/catena/pattern/coverage.ex`; `lib/catena/comprehension.ex`; `lib/catena/kernel/checker.ex`.

**Existing evidence home:** `test/catena/c044_pattern_contexts_test.exs`.

| Decision | Question | A | B | C | D | Recommended selection and reason |
| --- | --- | --- | --- | --- | --- | --- |
| CP-044-1 | What should a new binding context do with refutable patterns? | Require totality or an explicitly specified failure behavior; follows the three-class rule. | Raise an implicit runtime match exception; familiar but excluded by C036/C044. | Silently discard mismatches everywhere; convenient filtering but changes ordinary bindings. | Accept any pattern and rely on tests; flexible but no static guarantee. | A (recommended; selected by agent under user delegation): the context classification protects composition by making every mismatch observable or impossible. |
| CP-044-2 | How should totality reasoning be shared? | Use the existing usefulness relation with context-specific obligations; one coverage foundation. | Write ad hoc syntactic irrefutability checks in each feature; cheap but misses typed cases. | Treat only wildcard as total; safe but unnecessarily rejects admitted total patterns. | Require a universal proof assistant certificate for every binder; strong but excessive for decidable cases. | A (recommended; selected by agent under user delegation): C044 deliberately reuses C045’s relation and diagnostics instead of inventing a second coverage theory. |

**Ordered implementation steps:**

1. Classify each arriving binding context as exhaustive, irrefutable-only or explicit-failure before introducing it.
2. Reuse usefulness/totality checking and preserve plain binders in contexts that have no admitted patterns.
3. State mismatch outcomes explicitly for comprehensions and receive without inventing hidden match exceptions.

**Acceptance evidence:** Positive: exhaustive match and a total ordinary generator retain accepted behavior. Negative: refutable plain binding positions and unsupported pattern parameters reject. Boundary: explicit filtering mismatch skips exactly one candidate; terminal traps are not treated as match fallthrough.

**Completion gate:** C044 remains complete. A new consumer is ready only when the above observations pass on its actual path and its obligation links resolve; defer unsupported semantic extensions to the named owners and public spelling to P109.

## Item 045 — Coverage and redundancy

**Baseline:** C045 complete; preserve and integrate. **Dependencies:** C002/C003/C044; P133/P134.

**Grounding:** [Governing rule](../60-specification/data-and-patterns/match-semantics-and-coverage.md#usefulness-model); [research rationale](algebraic-data-types.md). The recommendation cells apply these sources within this item's bounded contract.

**Compiler targets:** `lib/catena/pattern/coverage.ex`; `lib/catena/condition/facts.ex`; `lib/catena/data.ex`.

**Existing evidence home:** `test/catena/c002_data_test.exs`; `test/catena/c003_clause_condition_test.exs`.

| Decision | Question | A | B | C | D | Recommended selection and reason |
| --- | --- | --- | --- | --- | --- | --- |
| CP-045-1 | How should coverage extensions preserve soundness? | Extend the existing typed usefulness relation with explicit cases and witness construction. | Approximate every unknown type as empty; fast but accepts nonexhaustive matches. | Enumerate only currently observed values; useful testing but not a coverage proof. | Let BEAM pattern compilation decide completeness; reusable host path but lacks Catena abstractions. | A (recommended; selected by agent under user delegation): C045’s relation links acceptance, redundancy and missing witnesses under one declared model. |
| CP-045-2 | How should hard coverage cases terminate? | Retain deterministic budgets and unknown/exhaustion outcomes with distinct diagnostics. | Use unlimited recursive search; mathematically attractive but can hang compilation. | Treat timeout as nonexhaustiveness without explanation; safe rejection but misclassifies evidence limits. | Trust a sampling pass to certify completeness; fast but unsound for infinite domains. | A (recommended; selected by agent under user delegation): bounded search must report its epistemic limit without converting it into semantic certainty. |

**Ordered implementation steps:**

1. Retain one usefulness relation across initial patterns, guards, abstract types and GADT refinements.
2. Add cross-feature witnesses when new data libraries or pattern contexts consume that relation.
3. Keep three-valued inhabitation and budget exhaustion distinct from proved emptiness or completeness.

**Acceptance evidence:** Positive: exhaustive constructor/Bool/tuple matches check and redundant rows reject. Negative: omitted inhabited constructors produce a concrete missing witness. Boundary: empty/recursive/GADT-constrained types and exhausted search never manufacture a false exhaustive result.

**Completion gate:** C045 remains complete. A new consumer is ready only when the above observations pass on its actual path and its obligation links resolve; defer unsupported semantic extensions to the named owners and public spelling to P109.

## Item 046 — Programmable-pattern exclusion

**Baseline:** C046 complete; preserve and integrate. **Dependencies:** C002/C003/C023/C044; P109.

**Grounding:** [Governing rule](../60-specification/pattern-contexts/context-rules-and-reservations.md#the-programmable-pattern-exclusion); [research rationale](catena-pattern-contexts.md). The recommendation cells apply these sources within this item's bounded contract.

**Compiler targets:** `lib/catena/ast/decoder.ex`; `lib/catena/kernel/parser.ex`; `lib/catena/pattern/coverage.ex`.

**Existing evidence home:** `test/catena/c044_pattern_contexts_test.exs`.

| Decision | Question | A | B | C | D | Recommended selection and reason |
| --- | --- | --- | --- | --- | --- | --- |
| CP-046-1 | How should programmable-pattern use cases be handled now? | Use explicit computation followed by ordinary match; functional and already supported. | Add views immediately; expressive but demands new effect/totality/coverage semantics. | Permit hidden conversions in constructor matching; compact surface but unspecified evaluation. | Ban observer composition as well; simple exclusion but unnecessarily weakens ordinary programming. | A (recommended; selected by agent under user delegation): C046 completes an exclusion; useful composition does not require expanding the pattern language. |
| CP-046-2 | What should trigger reconsideration of the exclusion? | A demonstrated repeated use case plus a separate slice covering effects, totality, coverage, count and cost. | Availability of similar syntax in another language; familiar but not sufficient Catena evidence. | A compiler implementation that happens to work; practical but reverses normative authority. | A new public word that sounds approachable; appealing but vocabulary alone establishes no semantics. | A (recommended; selected by agent under user delegation): the existing arrival gate requires operational and proof obligations before any later admission. |

**Ordered implementation steps:**

1. Keep view patterns, pattern synonyms and active patterns outside the current accepted semantic forms.
2. Provide ordinary functions, observers and explicit match composition for the use cases that motivate them.
3. Preserve the recorded future arrival requirements without reserving words or scheduling an unnecessary feature.

**Acceptance evidence:** Positive: observers and ordinary function results can be matched explicitly using existing data. Negative: calls, effects, conversions and user-defined tests in a pattern reject. Boundary: future convenience lowering may not duplicate evaluation or evade totality/coverage by hiding a view call.

**Completion gate:** C046 remains complete. A new consumer is ready only when the above observations pass on its actual path and its obligation links resolve; defer unsupported semantic extensions to the named owners and public spelling to P109.

## Connections

- The [completion checklist](../00-inbox/language-specification-completeness-checklist.md)
  is the current status ledger; this volume does not replace its completion criteria.
- The [conformance registry](../10-maps/conformance-traceability.md) separates
  obligation identity from the strength of its present evidence.
- The [design decision register](design-decision-register.md) preserves the
  delegated option selections with their plan provenance.
- The [type-system research](catena-greenfield-type-system.md) motivates
  explicit guarantee boundaries; the [category-theory research](category-theory-for-programming.md)
  motivates lawful composition without implicit operational promises.
