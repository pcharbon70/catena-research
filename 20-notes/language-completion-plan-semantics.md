---
title: "Language Completion Plan: Composition, Effects, and Processes"
kind: note
created: "2026-09-06"
maturity: developing
tags:
  - catena
  - language-design
  - specification
  - category-theory
  - conformance
aliases: []
---

# Language Completion Plan: Composition, Effects, and Processes

## Purpose and decision authority

This non-normative execution plan covers every checklist suffix **047–092**.
The baseline is the [audited checklist](../00-inbox/language-specification-completeness-checklist.md),
with compiler evidence pinned in the [completion audit](../50-journal/2026-09-06-checklist-completion-audit.md).
An existing C means preserve and integrate its bounded contract; a P or G
requires the stated missing work; a D remains deliberately deferred until its
separate admission gate is met. Planning or choosing an option completes none
of these items.

Every table row is a decision. A, B, C, and D are alternatives considered for
that decision, with a cost or limitation. The selected answer is both the
recommendation and **agent-selected under the user's delegation**. No row
claims that the user individually reviewed or approved it. A selected semantic
extension remains a proposal until its explicit applicability, normative
chapter, implementation, and conformance evidence are produced through
[Specification Authority](../SPECIFICATION-AUTHORITY.md). Newly discovered
implementation forks require the same four-alternative treatment in the
execution journal before their dependent change.

No new public word, keyword, punctuation, or API spelling is chosen here.
Existing identifiers quoted below identify retained contracts or compiler
internals. Future semantic operations are described by their behavior. P109
owns the later integrated surface decision. This follows the research's
[separation of categorical structure from execution](category-theory-for-programming.md)
and its [combinator inclusion standard](combinators-for-algebraic-data-and-categorical-programming.md#inclusion-standard):
use the weakest sufficient structure, keep types and laws precise, and specify
order, failure, and resources separately. Old exploratory naming suggestions
are evidence of design history, not instructions to invent today's vocabulary.

## Inspected implementation and sequencing

The implementation root is `../catena`, not this archive. Inspected existing
boundaries include `lib/catena/comprehension.ex`, `lib/catena/type/`,
`lib/catena/categorical.ex`, `lib/catena/derive.ex`, `lib/catena/effect/`,
`lib/catena/kernel/{checker,stepper,backend,explorer}.ex`,
`lib/catena/namespace.ex`, and `lib/catena/entry.ex`. Paths below are relative
to that sibling root unless prefixed otherwise. The archive owns contracts,
decisions, research, and evidence records; the sibling owns executable code.

The immediate sequence is P050/P053/P057 together, followed by P086's explicit
conflict resolution. Preserve C047–C058 throughout. Then use the following
acyclic staging: retain the C060–C079 foundations; define a common lifecycle
transition model for G080/P084/G088; implement local process lifetime and
resource transitions; add messages/protocols and supervised lifecycle; then
bound scheduling; finally admit remote transport and upgrade. G096/G098
foreign frames depend on the lifecycle model but local lifecycle work does
not require a functioning foreign interface. P106 capability injection
consumes C082 and the local runtime model. G091 consumes the local portion of P085; P085 closes its remote
facet after G091, so neither waits for the other's whole checklist completion.
G089 consumes a narrow typed OTP lifecycle admission contract rather than
waiting for every G096 callback facility. G091 needs G095/G096/P099/P130;
G092 additionally needs C028, G091, P116, and the lifecycle model. P109 follows
all semantic admission choices and remains deferred by the current instruction.

Cross-target agreement means checking one fixture, evaluating it with the
independent applicable reference path, compiling it to BEAM, executing it,
and comparing the documented observations. A generated string or obligation
tag is useful structural evidence but cannot substitute for that execution.
New runtime services require a transition model and bounded deterministic
schedule exploration before timing-dependent integration tests. Each item
below names positive, negative, and boundary evidence and a completion gate.

## Item 047 — Retained comprehension roles (C047)

**Dependencies and scope:** C044/C045 and C030; integrate with P053/C055 now,
P109 later. Preserve the existing semantic-role grammar and its dormant status.

| Decision | Four explored alternatives | Selected recommendation and research basis |
| --- | --- | --- |
| CP-047-1 | A: Keep the dedicated qualifier tree, preserving explicit roles but requiring an adapter. B: Parse new surface text now, easing demos but violating the vocabulary boundary. C: Route through generic carrier methods, reducing nodes but hiding execution. D: Encode a library macro, avoiding core changes but weakening source attribution. | **A, recommended and agent-selected.** The [elaboration contract](../60-specification/list-comprehensions/elaboration-and-lowering.md#the-qualifier-tree-target) already chooses this semantic boundary. |
| CP-047-2 | A: Integrate roles with existing kernel validation, gaining executable coverage at modest fixture cost. B: Validate strings only, cheap but semantically weak. C: Freeze punctuation alongside roles, concrete but premature. D: Remove dormant examples, simpler documentation but lost evidence. | **A, recommended and agent-selected.** The [dormant adoption boundary](../60-specification/list-comprehensions/elaboration-and-lowering.md#the-dormant-adoption-boundary) requires executable roles without a public frontend claim. |

**Implementation:** (1) Inventory each existing qualifier node in
`lib/catena/comprehension.ex`; (2) reuse it for the effect fixtures;
(3) retain current rejection of a non-generator first qualifier in
`test/catena/c047_list_comprehensions_test.exs`; (4) connect role coverage to
the later frontend adapter without extending token recognition.
**Evidence/gate:** positive mixed-role checking and execution; negative missing
initial generator; boundary one generator and empty source. Retain C047 only
within its existing dormant role scope; no surface adoption claim.

## Item 048 — List generator source boundary (C048)

**Dependencies and scope:** C040/C042, P053, and D059's separate producer gate.

| Decision | Four explored alternatives | Selected recommendation and research basis |
| --- | --- | --- |
| CP-048-1 | A: Keep concrete List sources, ensuring predictable traversal but limiting carriers. B: Accept any foldable source, broader but insufficient for dependent enumeration. C: Accept pull iterators, flexible but introduces lifecycle state. D: Accept streams, compositional but adds cancellation and backpressure. | **A, recommended and agent-selected.** [Generator sources](../60-specification/list-comprehensions/generator-and-qualifier-rules.md#sources) fix this boundary; genericity alone does not supply the missing protocols. |
| CP-048-2 | A: Distinguish effectful expressions returning lists from effectful producer protocols, preserving useful effects at documentation cost. B: Ban all source effects, simple but contradicts order rules. C: Treat both as producers, uniform but widens scope. D: Infer protocol meaning from source implementation, convenient but unstable. | **A, recommended and agent-selected.** [Effect rows](../60-specification/list-comprehensions/evaluation-effects-and-execution.md#effect-rows) explicitly include source-expression effects; the excluded producer has incremental production semantics. |

**Implementation:** (1) Add an existing-kernel request whose result is a
fully materialized List; (2) type-check that source through
`lib/catena/kernel/checker.ex`; (3) preserve non-list rejection in the C047
suite; (4) explain the expression/protocol distinction in evidence.
**Evidence/gate:** positive effectful list result; negative non-list source;
boundary empty effectful source performs its effect once. C048 stays complete
without iterator or stream admission.

## Item 049 — Dependent Cartesian traversal (C049)

**Dependencies and scope:** C048, C052, and P053's repeated-source trace.

| Decision | Four explored alternatives | Selected recommendation and research basis |
| --- | --- | --- |
| CP-049-1 | A: Preserve depth-first nested traversal, explicit dependency at potentially Cartesian cost. B: Zip inputs, bounded cost but different results. C: Breadth-first enumerate, fairer for infinite inputs but changes order. D: Sort output, stable presentation but loses effect order. | **A, recommended and agent-selected.** [Traversal](../60-specification/list-comprehensions/generator-and-qualifier-rules.md#traversal) and the [list algebra](list-comprehensions.md#lists-give-map-and-flatten-naturally) agree on nested bind. |
| CP-049-2 | A: Execute a dependent later source per reached prefix, observable and testable. B: Hoist all sources, cheaper but wrong with dependencies. C: Memoize equal prefixes, faster but repeats fewer effects. D: Test only final products, compact but cannot distinguish timing. | **A, recommended and agent-selected.** [Exact order](../60-specification/list-comprehensions/evaluation-effects-and-execution.md#exact-order) governs observations beyond pure equations. |

**Implementation:** (1) Extend the C047 Cartesian fixture with an inner
source that uses the outer binder; (2) include a prefix whose inner source is
empty; (3) compare reference/BEAM value and source-event sequences;
(4) preserve `workers/3` and `inner_suffix/8` dependency parameters in
`lib/catena/comprehension.ex`.
**Evidence/gate:** positive dependent Cartesian values; negative hoisted-source
mutant would change trace; boundary empty inner list still evaluates that
inner source once. C049 remains retained, with stronger integrated evidence.

## Item 050 — Effectful filters and failures (P050)

**Dependencies and scope:** C048/C049, C005/C036/C081, and P053/P057. This is
part of the first executable evidence slice, not a new semantic revision.

| Decision | Four explored alternatives | Selected recommendation and research basis |
| --- | --- | --- |
| CP-050-1 | A: Use real handled requests in Bool filters, directly witnessing effects with harness work. B: Annotate pure filters with uses rows, easy but no performed effect. C: Log host-side elaboration, visible but wrong phase. D: Restrict filters to guards, simpler but changes existing meaning. | **A, recommended and agent-selected.** [Filter rules](../60-specification/list-comprehensions/generator-and-qualifier-rules.md#filters) require ordinary effect-typed expressions, and the [audit](../50-journal/2026-09-06-checklist-completion-audit.md#comprehension-evidence) identifies the missing witness. |
| CP-050-2 | A: Test false, trap, and handler-abort separately, distinguishing three outcomes at fixture cost. B: Treat all as skip, convenient but loses failures. C: Assert only trap identity, cheap but misses suffix work. D: Compare only the successful list, simple but cannot establish stopping. | **A, recommended and agent-selected.** [Failure timing](../60-specification/list-comprehensions/evaluation-effects-and-execution.md#failure-timing) and [handler abort](../60-specification/effects-and-handlers/deep-handlers-and-affine-resumptions.md#result-and-clause-effects) distinguish skipping from abandonment. |
| CP-050-3 | A: Observe request-event prefixes and completion state on stepper and BEAM, stronger but requires normalization. B: Inspect generated branches, stable but not execution. C: Assert wall-clock duration, practical but flaky. D: Reuse one evaluator as both oracles, cheap but correlated. | **A, recommended and agent-selected.** The [required evidence](../60-specification/list-comprehensions/diagnostics-and-conformance.md#required-evidence-sets) calls for target agreement on effects and failures. |

**Implementation:** (1) Add a filter request returning false for one candidate
and true for another through existing kernel effect/handler declarations;
(2) assert the false candidate's request survives while its binding/yield
suffix is absent; (3) add trap and declining-handler variants with a later
sentinel request that must never occur; (4) run `Catena.check_kernel`,
`Catena.Kernel.Stepper.run`, and actual `Catena.compile_kernel`/BEAM invocation;
(5) repair only exposed elaboration/checking/lowering bugs in
`lib/catena/comprehension.ex` or its consumed kernel paths; (6) replace weak
claims in `test/catena/c047_list_comprehensions_test.exs` and update
LC-OBL-005 evidence.
**Evidence/gate:** positive effectful true and false; negative non-Bool filter
and absent suffix after failure; boundary first/last failing candidate and
empty input. Mark complete only after both targets agree on successful
values, exact retained prefixes, trap identity or whole-handler abort result,
and absence of any partial list result on failure.

## Item 051 — Explicit pattern filtering (C051)

**Dependencies and scope:** C044/C045, C048, and P050.

| Decision | Four explored alternatives | Selected recommendation and research basis |
| --- | --- | --- |
| CP-051-1 | A: Preserve total ordinary generators and explicit filtering generators, safer with two roles. B: Silently skip every mismatch, concise but loses data. C: Trap every mismatch, strict but rejects intended filtering. D: Infer filtering from pattern shape, convenient but unstable under datatype edits. | **A, recommended and agent-selected.** The [pattern split](../60-specification/list-comprehensions/generator-and-qualifier-rules.md#the-pattern-generator-split) implements the [explicit-refutability research](list-comprehensions.md#explicit-refutability-and-carrier-translation). |
| CP-051-2 | A: Keep compiler coverage as authority and test effect-prefix preservation around mismatches, integrated but more fixtures. B: Duplicate coverage in elaborator, local but divergent. C: Trust constructor names alone, cheap but misses types. D: Suppress impossible-pattern diagnostics, permissive but hides mistakes. | **A, recommended and agent-selected.** [Coverage obligations](list-comprehensions.md#total-generators-reuse-coverage-analysis) require reuse of the usefulness relation. |

**Implementation:** (1) Retain `M001`, `LCP002`, and `LCP003` fixtures;
(2) run a source with matching and rejected constructors through
`lib/catena/comprehension.ex` and `lib/catena/pattern/coverage.ex`;
(3) verify mismatches skip only their suffix.
**Evidence/gate:** positive explicit filtering; negative ordinary partial
pattern and impossible marker; boundary all-mismatch and already-total marker.
C051 stays complete with no implicit filtering expansion.

## Item 052 — Qualifier scope (C052)

**Dependencies and scope:** C021/C031/C044 and P053's binding effects.

| Decision | Four explored alternatives | Selected recommendation and research basis |
| --- | --- | --- |
| CP-052-1 | A: Retain left-to-right nonrecursive qualifier scope, predictable but order-sensitive. B: Hoist bindings globally, flexible but introduces recursion. C: Permit local rebinding, familiar but can hide dependency errors. D: Export qualifier binders, convenient but breaks expression isolation. | **A, recommended and agent-selected.** [Scope and rebinding](../60-specification/list-comprehensions/generator-and-qualifier-rules.md#scope-and-rebinding) governs the generated worker environment. |
| CP-052-2 | A: Test source-origin diagnostics through generated workers, useful with provenance plumbing. B: Expose worker names, easy but confusing. C: Discard warnings on elaboration, quiet but loses existing BS001. D: Rename user variables globally, hygienic-looking but changes diagnostic identity. | **A, recommended and agent-selected.** [Source attribution](../60-specification/list-comprehensions/elaboration-and-lowering.md#the-fused-worker) requires qualifier-facing diagnostics. |

**Implementation:** (1) Exercise prior-binding visibility and ordinary outer
shadowing in the C047 suite; (2) retain `check_rebinding/1` and unused-binding
advisories in `lib/catena/comprehension.ex`; (3) ensure effectful binding
fragments retain user origin in checker errors.
**Evidence/gate:** positive dependent binding; negative same-comprehension
rebinding and forward reference; boundary shadowed outer name and unused
binder advisory. Preserve C052's exact scope rules.

## Item 053 — Exact comprehension effect order (P053)

**Dependencies and scope:** C005/C030/C032/C049/C052 and P050/P057. Resolve
latent-effect threading before claiming the first executable slice complete.

| Decision | Four explored alternatives | Selected recommendation and research basis |
| --- | --- | --- |
| CP-053-1 | A: Use a nested fixture with distinguishable source/filter/binding/yield requests, precise but verbose. B: Count requests only, cheap but misses permutations. C: Compare list values only, compact but misses effects. D: Test independent single-position fixtures only, localized but misses nesting interactions. | **A, recommended and agent-selected.** [Exact order](../60-specification/list-comprehensions/evaluation-effects-and-execution.md#exact-order) fixes both order and per-prefix multiplicity; localized variants supplement the nested witness. |
| CP-053-2 | A: Propagate required latent effects into generated worker arrows at actual execution stages, accurate but needs checker-guided tests. B: Keep every arrow pure and add top-level uses, small but potentially unsound. C: Put all effects on every curry stage, easy but overstates closure construction. D: Bypass checking for test modules, executable but destroys evidence. | **A, recommended and agent-selected.** [Application typing](../60-specification/type-system/principal-inference-and-generalization.md#declarative-judgment) charges latent effects at application; `fn_type/3` currently emits empty rows, an inspected risk to test before repair. |
| CP-053-3 | A: Compare explicit expected event sequences against both independent paths, strongest with modest normalization work. B: Compare targets only, catches disagreement but can share a wrong lowering. C: Derive expected traces from elaborator output, convenient but circular. D: Use random stress alone, broad but hard to diagnose. | **A, recommended and agent-selected.** [Differential discipline](list-comprehensions.md#property-and-differential-tests) needs a contract-derived oracle in addition to backend agreement. |
| CP-053-4 | A: Test failure separately at source/filter/binding/yield and record exact prefixes, complete with more cases. B: Test only first-source failure, cheap but misses inner workers. C: Test only final-yield failure, broad traversal but misses early stop. D: Assume C036/C081 transfer automatically, concise but ignores elaboration bugs. | **A, recommended and agent-selected.** [Failure timing](../60-specification/list-comprehensions/evaluation-effects-and-execution.md#failure-timing) applies at every reached qualifier, not just the outer expression. |
| CP-053-5 | A: Add explicit per-fragment row metadata to the dormant typed tree and verify it with nonrecursive checker probes, precise with annotation work. B: Build a general expression-effect inference API, automatic but much larger scope. C: Put aggregate uses on every final worker arrow, easy but recursive calls can mask overdeclaration. D: Permit only pure comprehensions, small but contradicts the existing contract. | **A, recommended and agent-selected.** [The typed qualifier tree](../60-specification/list-comprehensions/elaboration-and-lowering.md#the-qualifier-tree-target) already requires expression/type/row evidence, and [effect declarations](../60-specification/effects-and-handlers/capabilities-rows-and-selection.md#union-unification-and-subtraction) require exact identity-aware checking. |
| CP-053-6 | A: Use handler-returned observations for successful runs and test-only BEAM call tracing for terminal prefixes, independent without production instrumentation. B: Add production request logging solely for tests, convenient but broadens runtime work. C: Use resume counts alone, cheap but misses request positions and failures. D: Use only final writer values, pure-looking but loses evidence when a trap discards the result. | **A, recommended and agent-selected.** [Required effect/failure evidence](../60-specification/list-comprehensions/diagnostics-and-conformance.md#required-evidence-sets) needs observable prefixes even without a return value; tracing is conformance instrumentation, not a new language observation. |
| CP-053-7 | A: Classify backend effect control from checked transitive effect evidence plus explicit control nodes, accurate with regression work. B: Keep literal request/handle/resume detection only, simple but misses effectful global calls. C: CPS-convert every expression, robust but unnecessarily broadens pure execution. D: Special-case generated worker names, quick but brittle and incomplete. | **A, recommended and agent-selected.** [Typed-core CPS contract](../60-specification/effects-and-handlers/typed-core-cps-and-beam.md) requires effectful calls to preserve their selected capability environment; purely reserved process operations retain their established direct handling. |

**Implementation:** (1) Build checked kernel fixtures with at least two outer
candidates, a dependent inner source, and one false filter; (2) distinguish
events by position and candidate so the expected trace determines counts and
order; (3) inspect `fn_type/3`, `workers/3`, per-context and per-qualifier rows,
aggregate row equality, and reverse worker purity in `lib/catena/comprehension.ex`; (4) if checking fails, thread
latent rows where the generated function executes work, preserving pure curry
stages, pure closure-construction definitions, and the pure reverse pass; use
explicit fragment metadata and nonrecursive checker probes so recursive
self-calls cannot legitimize an overstated row; retain legacy pure inputs
without requiring new public vocabulary; (5) repair backend classification when a caller reaches effects only through
a typed global call, preserving lexical handlers across CPS; execute stepper
and BEAM with handler-returned successful observations and test-only tracing
for terminal prefixes, since the existing runtime trace hook records resumes
but kernel requests do not all use that hook;
(6) test all four failure positions; (7) update LC-OBL-008 only from passing
assertions. Kernel checking and backend CPS lowering are independent review
surfaces; a compile-only success is not sufficient.
**Evidence/gate:** positive exact expected trace including inner-source
reevaluation; negative missing/forged effect rows reject and failure sentinel
never fires; boundary zero candidates, false first candidate, and final
candidate failure. P053 closes only with all required roles, multiplicities,
and immediate failure behavior witnessed on both targets.

## Item 054 — Eager production (C054)

**Dependencies and scope:** C048/C049/C056, P053, and deferred D059/D083.

| Decision | Four explored alternatives | Selected recommendation and research basis |
| --- | --- | --- |
| CP-054-1 | A: Preserve fully eager ordered lists, simple ownership with whole-result allocation. B: Make evaluation lazy, memory-friendly but changes effects. C: Return a pull iterator, incremental but adds resource lifetime. D: Select eager/lazy by context, convenient but unpredictable timing. | **A, recommended and agent-selected.** [Eager production](../60-specification/list-comprehensions/the-surface-contract.md) and [stream limitations](list-comprehensions.md#streams-and-iterators) separate these contracts. |
| CP-054-2 | A: Assert all reached yield effects precede result observation, direct with trace setup. B: Assert output shape only, cheap but could hide thunks. C: Assert allocation counts as semantics, precise but overcommits representation. D: Infer eagerness from host lists, easy but ignores deferred element effects. | **A, recommended and agent-selected.** [Execution order](../60-specification/list-comprehensions/evaluation-effects-and-execution.md#exact-order) determines when production finishes. |

**Implementation:** (1) Reuse the P053 yield trace; (2) assert result is a
realized nominal list in `test/catena/c047_list_comprehensions_test.exs` on
both targets; (3) retain no-lazy-entry-point tests.
**Evidence/gate:** positive all yields before completion; negative deferred
producer entry remains unavailable; boundary empty result and terminal final
yield. Preserve C054 without a new suspension mechanism.

## Item 055 — Dedicated lowering (C055)

**Dependencies and scope:** C010/C030/C038, P053, and C058; no open dispatch.

| Decision | Four explored alternatives | Selected recommendation and research basis |
| --- | --- | --- |
| CP-055-1 | A: Keep fused kernel workers, preserving semantics with generated-code complexity. B: Expand through open traits, reusable but instance-dependent. C: Lower directly to native comprehension, concise but bypasses reference semantics. D: Interpret qualifier trees at runtime, simple but adds runtime machinery. | **A, recommended and agent-selected.** [Elaboration](../60-specification/list-comprehensions/elaboration-and-lowering.md#the-qualifier-tree-target) fixes the common checked target. |
| CP-055-2 | A: Use pure map/flatten equations only within their domain plus separate effect traces, honest with two evidence kinds. B: Rewrite by laws for all callbacks, fast but unsound. C: Discard algebraic equations, conservative but loses a useful oracle. D: Trust trait law labels, convenient but not proof. | **A, recommended and agent-selected.** [Extensional equations](../60-specification/list-comprehensions/elaboration-and-lowering.md#extensional-equations) remain subordinate to execution semantics. |

**Implementation:** (1) Keep pure hand-written-recursion equivalence fixtures;
(2) add actual BEAM execution to their helper; (3) review P053 worker changes
against direct traversal and no trait dispatch; (4) retain deterministic
`Comprehension.elaborate/1` output.
**Evidence/gate:** positive pure equation and effectful ordered trace;
negative no unverified open dispatch; boundary empty and nested generators.
C055 stays complete; optimization beyond these premises belongs to P135.

## Item 056 — Concrete list result (C056)

**Dependencies and scope:** C040/C042/C048 and deferred D059 collectors.

| Decision | Four explored alternatives | Selected recommendation and research basis |
| --- | --- | --- |
| CP-056-1 | A: Keep List B results, predictable with explicit subsequent conversion. B: Infer result carrier from expected type, ergonomic but adds type-directed behavior. C: Select arbitrary applicatives, general but filtered algebra needs more structure. D: Provide built-in map/set/binary targets now, useful but adds duplicate and encoding policies. | **A, recommended and agent-selected.** [Result contract](../60-specification/list-comprehensions/the-surface-contract.md) and [filtering algebra](list-comprehensions.md#monad-is-insufficient-for-filtered-comprehensions) reject accidental carrier generalization. |
| CP-056-2 | A: Verify nominal output identity and element typing through both targets, reliable at small test cost. B: Assert host list shape alone, simple but misses identity. C: Coerce mixed yields, convenient but violates C061. D: Allow opaque collectors through foreign values, flexible but bypasses the closed boundary. | **A, recommended and agent-selected.** [Typed qualifier target](../60-specification/list-comprehensions/elaboration-and-lowering.md#the-qualifier-tree-target) keeps the checker authoritative. |

**Implementation:** (1) Retain `result_element_type` checking and generated
List declaration in `lib/catena/comprehension.ex`; (2) add heterogeneous-yield
rejection; (3) verify decoded nominal values after BEAM execution.
**Evidence/gate:** positive List result; negative incompatible element types
and unavailable collector entries; boundary empty list preserves declared
element type. No generic collector is admitted.

## Item 057 — Sequential execution (P057)

**Dependencies and scope:** P050/P053 and C030/C074; shares the first evidence
slice without treating another item's checkbox as proof.

| Decision | Four explored alternatives | Selected recommendation and research basis |
| --- | --- | --- |
| CP-057-1 | A: Assert each candidate completes its suffix before the next, direct but requires event identities. B: Assert no parallel API exists, cheap but insufficient. C: Inspect spawned process count, observable but misses reordering in one process. D: Benchmark deterministic timing, accessible but flaky. | **A, recommended and agent-selected.** [Sequential execution](../60-specification/list-comprehensions/evaluation-effects-and-execution.md#sequential-execution-is-normative) defines the event order itself. |
| CP-057-2 | A: Use handler state or observable requests whose order changes output, sensitive with carefully chosen fixtures. B: Use commutative counters alone, cheap but cannot detect permutations. C: Use pure additions, fast but insensitive. D: Sleep between yields, visually persuasive but scheduler-dependent. | **A, recommended and agent-selected.** [Laws do not schedule work](../60-specification/traits-and-categorical-operations/operational-semantics.md#laws-do-not-schedule-work) requires noncommuting observations to test order. |
| CP-057-3 | A: Preserve serial lowering and document future parallel admission separately, stable but limits optimization. B: Parallelize inferred-pure qualifiers, attractive but disallowed by this revision. C: Add an implicit runtime flag, flexible but changes semantics per deployment. D: Parallelize then reorder results, tempting but leaves effects reordered. | **A, recommended and agent-selected.** [The current execution contract](../60-specification/list-comprehensions/evaluation-effects-and-execution.md#sequential-execution-is-normative) explicitly excludes these alternatives. |

**Implementation:** (1) Reuse P053's nested trace but add LC-OBL-012-specific
assertions of complete suffix blocks and no later candidate after abort;
(2) execute generated BEAM, rather than relying on string checks;
(3) preserve serial worker calls in `lib/catena/comprehension.ex` and
`lib/catena/kernel/backend.ex`; (4) retain API absence as supplementary evidence.
**Evidence/gate:** positive exact serial blocks on both targets; negative
permuted or interleaved event expectations differ; boundary a false filter and
an empty inner source still permit only the defined next step. P057 closes
with actual executable serial evidence, independently linked to LC-OBL-012.

## Item 058 — Termination and honest cost (C058)

**Dependencies and scope:** C034/C037/C042/C055 and P129's resource limits.

| Decision | Four explored alternatives | Selected recommendation and research basis |
| --- | --- | --- |
| CP-058-1 | A: Preserve fused accumulation and final reversal, bounded intermediate allocation with one extra pass. B: Build repeated append chains, simple but quadratic. C: Materialize every qualifier stage, modular but allocation-heavy. D: Use lazy output, memory-efficient but changes C054. | **A, recommended and agent-selected.** [Fused worker](../60-specification/list-comprehensions/elaboration-and-lowering.md#the-fused-worker) already fixes this strategy. |
| CP-058-2 | A: Measure accepted-size stack behavior and report traversal multiplicity separately, honest with bounded evidence. B: Claim universal linear time, concise but false for Cartesian input. C: Treat parser limits as runtime limits, easy but conflates boundaries. D: Treat successful small tests as asymptotic proof, cheap but unsupported. | **A, recommended and agent-selected.** [Cost honesty](../60-specification/list-comprehensions/elaboration-and-lowering.md#cost-honesty) and [implementation limits](../IMPLEMENTATION-LIMITS.md) distinguish contracts from witness bounds. |

**Implementation:** (1) Retain the existing 900-element BEAM witness;
(2) ensure P053 changes keep the reverse helper pure and workers tail-positioned;
(3) add a small multi-depth value/trace check; (4) record input construction
and parser limits independently from runtime traversal evidence.
**Evidence/gate:** positive accepted long output; negative deliberately
nonterminating source stays subject to C034 rather than a false totality
claim; boundary empty/singleton output. Retain C058's published bounded scope.

## Item 059 — Neighboring iteration families (D059)

**Dependencies and scope:** G080/G088, P102, P109, and D083. The current
instruction does not authorize vocabulary definition; this item stays deferred.

| Decision | Four explored alternatives | Selected recommendation and research basis |
| --- | --- | --- |
| CP-059-1 | A: Keep each family behind a separate admission dossier, slower but preserves distinct semantics. B: Add all through one generic collector, compact but hides differences. C: Copy a host language's iteration surface, familiar but imports accidental behavior. D: Permanently ban all extensions, simple but overstates the research. | **A, recommended and agent-selected.** [Neighboring features](list-comprehensions.md#result-shape-and-neighboring-features) identifies distinct resource and algebra requirements. |
| CP-059-2 | A: Prioritize library comparisons for ranges/zip/collection conversion, useful without new syntax. B: Begin with async streams, ambitious but lifecycle dependencies dominate. C: Add generator functions first, convenient but requires suspension ownership. D: Add query optimization first, powerful but lacks semantic premises. | **A, recommended and agent-selected.** [Inclusion standard](combinators-for-algebraic-data-and-categorical-programming.md#inclusion-standard) favors demonstrated simpler composition before special forms. |
| CP-059-3 | A: Require per-family order, failure, exhaustion, and evidence gates before admission, explicit but substantial. B: Require only type signatures, quick but leaves operational gaps. C: Require only examples, approachable but incomplete. D: Treat categorical laws as the gate, elegant but does not govern resources. | **A, recommended and agent-selected.** [Evidence-gated extensions](list-comprehensions.md#stage-4-evidence-gated-extensions) supplies the existing research direction. |

**Implementation:** (1) Inventory ranges, effect-only loops, generator functions,
async streams, binary/map comprehensions, zip, and collectors in separate
behavior rows; (2) compare ordinary-library encodings using existing internal
ASTs; (3) record unmet lifecycle and algebra prerequisites; (4) retain explicit
rejections/absences in the C047 suite. No new frontend or public API is created.
**Evidence/gate:** positive library encodings of bounded use cases; negative
unadmitted forms remain unavailable; boundary early stop, empty input, and
abandoned producer scenarios become admission tests. D059 cannot honestly be
checked complete as implemented iteration; its current deliverable is a
reviewable deferral and future per-family gate.

## Item 060 — Retained type notation (C060)

**Dependencies and scope:** C001/C068/C140 and P109. Preserve existing type
forms and their meaning; no new vocabulary or surface punctuation now.

| Decision | Four explored alternatives | Selected recommendation and research basis |
| --- | --- | --- |
| CP-060-1 | A: Maintain versioned internal type representations, precise but requires adapters. B: Unify every frontend immediately, simpler later but risks compatibility. C: Design new type punctuation, readable but outside current scope. D: Infer types from runtime values, flexible but conflicts with erasure. | **A, recommended and agent-selected.** [Type language](../60-specification/type-system/type-language-and-kinds.md) is the retained boundary; vocabulary adoption belongs to P109. |
| CP-060-2 | A: Check kind/row/quantifier round trips across admitted representations, targeted with fixture cost. B: Snapshot pretty text only, cheap but misses meaning. C: Accept arbitrary higher kinds, powerful but crosses C140. D: Remove advanced notation, simpler but regresses C068. | **A, recommended and agent-selected.** [Greenfield kind separation](catena-greenfield-type-system.md#2-kinds-keep-solver-domains-separate) protects solver domains while preserving explicit advanced forms. |

**Implementation:** (1) Map existing `lib/catena/type/parser.ex`,
`lib/catena/kernel/type.ex`, and `lib/catena/categorical/type_term.ex`
constructors to their normative forms; (2) extend only integration codecs
needed by later slices; (3) retain exact revision selection.
**Evidence/gate:** positive function, row, constructor, and quantified forms;
negative wrong kinds and malformed quantification; boundary higher-rank
checking only where C068 admits it. C060 stays complete within existing notation.

## Item 061 — Primitive numeric relationships (C061)

**Dependencies and scope:** C018/C035 and P105. Do not let new categorical
libraries turn primitive arithmetic into open trait dispatch.

| Decision | Four explored alternatives | Selected recommendation and research basis |
| --- | --- | --- |
| CP-061-1 | A: Preserve closed Int/Float instantiation, deterministic but not overloadable. B: Resolve arithmetic through traits, extensible but changes identities. C: Insert coercions automatically, ergonomic but breaks explicit typing. D: Default ambiguous operands, convenient but violates no-defaulting. | **A, recommended and agent-selected.** [Numeric relationships](../60-specification/numeric-relationships/README.md) and the [synthesis](catena-numeric-relationships.md) fix the closed-set rule. |
| CP-061-2 | A: Keep float-typed engine witnesses and stage frontend adoption separately, honest but dormant. B: Claim full float syntax from literal decoding, attractive but unsupported. C: Drop Float from the engine, simpler but regressive. D: Add numeric-library operations here, efficient batching but conflates P105. | **A, recommended and agent-selected.** [Numeric literal meaning](../60-specification/numeric-literal-semantics/numeric-types-and-literal-typing.md) does not itself establish end-to-end source adoption. |

**Implementation:** (1) Preserve closed numeric selection in
`lib/catena/type/infer.ex`; (2) rerun
`test/catena/c061_numeric_relationships_test.exs` when P105 integrates;
(3) keep `lib/catena/numeric.ex` literal conversion separate from runtime
arithmetic producers. **Evidence/gate:** positive homogeneous Int and dormant
Float operands; negative mixed operands/user overload/defaulting; boundary
finite float and explicit conversion ownership. C061 stays complete.

## Item 062 — Aliases and nominal wrappers (C062)

**Dependencies and scope:** C022/C028/C065/C073 and P101/P103 libraries.

| Decision | Four explored alternatives | Selected recommendation and research basis |
| --- | --- | --- |
| CP-062-1 | A: Use existing nominal single-field datatypes for wrappers, explicit but slightly verbose internally. B: Add transparent aliases, convenient but currently excluded. C: Treat wrappers as structural records, simple but loses identity. D: Promise representation erasure, fast-looking but unsupported ABI commitment. | **A, recommended and agent-selected.** [Newtype contract](../60-specification/aliases-and-newtypes/the-newtype-form.md) preserves nominal identity without a cost promise. |
| CP-062-2 | A: Require explicit wrapping, unwrapping, and instance targets, predictable with explicit operations. B: Inherit underlying instances automatically, convenient but can violate domain laws. C: Allow implicit coercion, concise but masks boundaries. D: Let abstract exports expose representation for deriving, powerful but breaks abstraction. | **A, recommended and agent-selected.** [Aliases/newtypes synthesis](catena-aliases-and-newtypes.md) routes opacity through existing export authority. |

**Implementation:** (1) Use `lib/catena/data.ex`, `lib/catena/derive.ex`, and
`lib/catena/namespace.ex` unchanged as the starting point for new libraries;
(2) rerun `test/catena/c062_aliases_newtypes_test.exs` across those additions;
(3) include instance-less twins of new domain wrappers.
**Evidence/gate:** positive explicit wrapper and smart-constructor behavior;
negative representation access/coercion/automatic instance flow; boundary
same underlying representation with different nominal identities. Retain C062.

## Item 063 — Generalization (C063)

**Dependencies and scope:** C001/C005/C068/C078 and all new resource bindings.

| Decision | Four explored alternatives | Selected recommendation and research basis |
| --- | --- | --- |
| CP-063-1 | A: Preserve the effect-aware hybrid rule, useful inference with a purity obligation. B: Generalize every let, convenient but unsound with capabilities. C: Generalize only syntactic values, safe but unnecessarily restrictive. D: Require all signatures, simple checking but abandons inference-first design. | **A, recommended and agent-selected.** [Generalization](../60-specification/type-system/principal-inference-and-generalization.md#generalization) and [the research boundary](catena-greenfield-type-system.md#generalization-in-a-strict-language) already select it. |
| CP-063-2 | A: Audit new resource/handler allocations for nongeneralization, targeted with cross-feature tests. B: Treat all opaque values as pure, easy but can hide affine state. C: Generalize by host immutability, convenient but wrong abstraction. D: Disable polymorphism inside handlers, conservative but overrestrictive. | **A, recommended and agent-selected.** [Advanced scope rules](../60-specification/type-system/advanced-type-checking.md#affine-resumptions) make token allocation relevant even when values look immutable. |

**Implementation:** (1) Preserve `lib/catena/type/infer.ex` and kernel
checker closing rules; (2) classify every G080/P084/G088 allocation in the
lifecycle slice; (3) extend `test/catena/type_conformance_test.exs` and C010's
generalization cases only for newly exposed interactions.
**Evidence/gate:** positive pure expansive and latent-effect lambda values;
negative generalized allocated capability/resumption; boundary unknown purity
stays monomorphic and annotated polymorphic recursion remains checked. Retain C063.

## Item 064 — Separate row theories (C064)

**Dependencies and scope:** C001/C005/C041/C077 and P053's latent rows.

| Decision | Four explored alternatives | Selected recommendation and research basis |
| --- | --- | --- |
| CP-064-1 | A: Retain separate unique value rows and capability-aware effect rows, explicit with more solver code. B: Use sets for every row, simple but collapses distinct capabilities. C: Use multisets for records, uniform but permits duplicate fields. D: Replace rows with subtyping, flexible but changes inference guarantees. | **A, recommended and agent-selected.** [Rows, traits, and effects](../60-specification/type-system/rows-traits-and-effects.md) separates the domains and records the 0.1.5 refinement. |
| CP-064-2 | A: Test alpha-renaming and duplicate-identity behavior per revision, accurate but version-aware. B: Treat 0.1.5 as retroactive, simpler but rewrites historical meaning. C: Collapse repeated labels before identities resolve, cheap but unsound. D: Depend on insertion order, easy but nondeterministic evidence. | **A, recommended and agent-selected.** [Hybrid row equality](../60-specification/effects-and-handlers/capabilities-rows-and-selection.md#hybrid-row-equality) coalesces the same identity while preserving distinct ones. |

**Implementation:** (1) Keep `lib/catena/type/row.ex` historical semantics
separate from `lib/catena/effect/row.ex`; (2) test generated P053 worker rows
with the applicable checker; (3) preserve lacks constraints through new
interface codecs. **Evidence/gate:** positive reordered fields and repeated
same-capability requests; negative duplicate record labels and capability
collapse; boundary two abstract family occurrences and open-tail unification.
Retain C064 without claiming an unproved general combined solver theorem.

## Item 065 — Trait solving (C065)

**Dependencies and scope:** C001/C069–C075, C066, and new library instances.

| Decision | Four explored alternatives | Selected recommendation and research basis |
| --- | --- | --- |
| CP-065-1 | A: Preserve terminating coherent solving with explicit failure, predictable but rejects some expressive instances. B: Allow overlap with priorities, ergonomic but order-sensitive. C: Defer constraints to runtime dictionaries, flexible but changes evidence semantics. D: Default unresolved traits, convenient but hides ambiguity. | **A, recommended and agent-selected.** [Trait solver rules](../60-specification/type-system/rows-traits-and-effects.md#traits) support stable categorical composition. |
| CP-065-2 | A: Check ownership, decreasing measure, fundep consistency, and normalization together for each library addition, thorough with fixture cost. B: Test only successful lookup, quick but misses coherence. C: Trust standard packages, cheaper but creates unsound privilege. D: Increase search budget until acceptance, pragmatic but confuses nontermination with capacity. | **A, recommended and agent-selected.** [Solver interface](../60-specification/type-system/rows-traits-and-effects.md#solver-interface) requires termination and schedule independence. |

**Implementation:** (1) Add future instances through `lib/catena/type/trait.ex`
and `lib/catena/categorical.ex`; (2) preserve existing diagnostics and explicit
budget exhaustion; (3) compare reordered imports and separate compilations
in type/C004 tests. **Evidence/gate:** positive unique lawful-shaped instance;
negative overlap, orphan ownership, ambiguity and nondecreasing context;
boundary exact resolution budget versus malformed constraint. Retain C065.

## Item 066 — Scope-only name resolution (C066)

**Dependencies and scope:** C021/C022/C061/C065, P101, and later P109.

| Decision | Four explored alternatives | Selected recommendation and research basis |
| --- | --- | --- |
| CP-066-1 | A: Resolve names before type-directed evidence selection, deterministic with explicit names. B: Use expected types to pick names, terse but unstable. C: Resolve by elaboration order, easy but implementation-dependent. D: Search every imported constructor by unification, convenient but ambiguity-prone. | **A, recommended and agent-selected.** [Name-resolution synthesis](catena-name-resolution.md) preserves the normative scope-only invariant. |
| CP-066-2 | A: Add annotation-invariance pairs for each new module/library boundary, focused but repetitive. B: Snapshot resolved text only, cheap but misses annotation effects. C: Permit implicit field adaptation, ergonomic but excluded. D: Defer trait evidence to callers, flexible but breaks instance-time settlement. | **A, recommended and agent-selected.** [Resolution specification](../60-specification/name-resolution/README.md) distinguishes field labels, constructors, and evidence. |

**Implementation:** (1) Feed library imports through `lib/catena/namespace.ex`;
(2) keep instance solving in `lib/catena/categorical.ex` at its present boundary;
(3) extend `test/catena/c066_name_resolution_test.exs` only where new adapters
could alter target identity. **Evidence/gate:** positive stable resolved target
with/without annotations; negative import collision and missing constructor;
boundary field labels remain structural and numeric operators remain closed.
Retain C066 and defer public naming to P109.

## Item 067 — No intralingual unsafety (C067)

**Dependencies and scope:** C003/C006/C036/C113 and G095/G096/G098.

| Decision | Four explored alternatives | Selected recommendation and research basis |
| --- | --- | --- |
| CP-067-1 | A: Keep casts/reflection/unchecked operations excluded, clear but demands explicit foreign adapters. B: Add a universal dynamic type, convenient but changes the type contract. C: Expose compiler intrinsics, powerful but leaks implementation. D: Permit hidden unsafe standard code, expedient but obscures authority. | **A, recommended and agent-selected.** [Dynamic/unsafe synthesis](catena-dynamic-and-unsafe-boundaries.md) routes unsafety to visible foreign boundaries. |
| CP-067-2 | A: Audit every new runtime and foreign admission for typed validation and classified failure, precise with adapter work. B: Trust all BEAM terms, easy but violates typing. C: Keep checks in documentation only, cheap but unenforced. D: Expose erased evidence as runtime types, convenient but violates C113. | **A, recommended and agent-selected.** [Dynamic boundary specification](../60-specification/dynamic-and-unsafe-boundaries/README.md) requires visibility without intralingual escape hatches. |

**Implementation:** (1) Preserve C067 rejection and artifact absence tests;
(2) route G095/G096/G098 changes through typed boundary validation rather than
`lib/catena/type/infer.ex` casts; (3) audit `lib/catena/kernel/backend.ex`
for any new unchecked ingress. **Evidence/gate:** positive admitted typed
value boundary later; negative fabricated type evidence and unadmitted forms;
boundary non-finite foreign floats and escaped runtime resources belong to
their producers' tests. Retain C067's exclusion, not a claim of VM-level safety.

## Item 068 — Checked advanced typing (C068)

**Dependencies and scope:** C001/C063/C064/C140 and C132/P133/P134 formal evidence.

| Decision | Four explored alternatives | Selected recommendation and research basis |
| --- | --- | --- |
| CP-068-1 | A: Keep explicit predicative higher-rank checking and signed GADT matches, expressive with annotations. B: Infer arbitrary higher rank, convenient but unsupported. C: Admit impredicative metavariables, powerful but changes solver theory. D: Remove advanced features, simpler but discards established capability. | **A, recommended and agent-selected.** [Advanced entry boundary](../60-specification/type-system/advanced-type-checking.md#entry-boundary) is the adopted research compromise. |
| CP-068-2 | A: Test branch-local equality and existential escape across new resource/protocol encodings, targeted with scope fixtures. B: Promote equalities globally, easy but unsound. C: Hide escapes through closures, flexible but violates abstraction. D: Treat all annotated code as trusted, cheap but bypasses checking. | **A, recommended and agent-selected.** [GADT patterns](../60-specification/type-system/advanced-type-checking.md#gadt-patterns) and [the inference research](catena-greenfield-type-system.md#7-gadts-and-local-equalities-are-a-later-checked-fragment) require rigid local scope. |

**Implementation:** (1) Preserve `lib/catena/type/advanced.ex` and checking
paths in `lib/catena/type/infer.ex`; (2) ensure P087's initial protocol
approach needs no new advanced type mechanism; (3) rerun type/C140 boundary
fixtures when interface schemas change. **Evidence/gate:** positive signed
GADT and higher-rank examples; negative escaping skolems and unannotated GADT
matching; boundary sibling branches remain independent. C068 stays complete
for its bounded profile; composed metatheory remains a separate task.

## Item 069 — Trait declarations and implementations (C069)

**Dependencies and scope:** C065/C070/C071 and P101/P102/P108.

| Decision | Four explored alternatives | Selected recommendation and research basis |
| --- | --- | --- |
| CP-069-1 | A: Retain JSON AST declaration roles and exact minimal methods, stable with explicit adapters. B: Invent new trait surface forms, approachable but premature. C: Permit arbitrary method subsets, flexible but incomplete dictionaries. D: Encode every trait as ordinary records, uniform but loses current coherence metadata. | **A, recommended and agent-selected.** [Declarations and coherence](../60-specification/traits-and-categorical-operations/declarations-instances-and-coherence.md) define the admitted internal boundary. |
| CP-069-2 | A: Reuse one authoritative interface description for checking and library generation, consistent but requires schema discipline. B: Hand-code backend-only special cases, quick but divergent. C: Infer methods from implementations, convenient but changes public contracts. D: Freeze all proposed research classes anew, exhaustive but gratuitously redesigns C004. | **A, recommended and agent-selected.** [Minimal dictionary research](combinators-for-algebraic-data-and-categorical-programming.md#executive-conclusion) favors one minimal implementation with derived conveniences. |

**Implementation:** (1) Extend libraries through `lib/catena/categorical.ex`
and `lib/catena/categorical/standard.ex`; (2) preserve AST validation in
`lib/catena/ast/decoder.ex`; (3) keep package ownership and visibility metadata
in interfaces. **Evidence/gate:** positive kinded parent-constrained trait;
negative missing/excess methods and invalid placement; boundary empty derived
convenience set still retains exact minimal dictionary. Retain C069 without
new public punctuation.

## Item 070 — Coherence and ownership (C070)

**Dependencies and scope:** C022/C025/C028/C065 and all added standard instances.

| Decision | Four explored alternatives | Selected recommendation and research basis |
| --- | --- | --- |
| CP-070-1 | A: Keep trait-or-type ownership and no overlap, compositional with explicit wrapper needs. B: Allow local instances, convenient but context-dependent. C: Prefer last import, simple but nondeterministic meaning. D: Trust standard-library overlap, expedient but fractures the model. | **A, recommended and agent-selected.** [Coherence rules](../60-specification/traits-and-categorical-operations/declarations-instances-and-coherence.md) protect separate compilation. |
| CP-070-2 | A: Test nominal identity across dependency aliases and rebuilds, robust with multi-package fixtures. B: Identify instances by display name, simple but collision-prone. C: Use file paths as identity, easy but nonreproducible. D: Select instances at call sites after linking, flexible but violates settlement rules. | **A, recommended and agent-selected.** [Qualified-type research](catena-greenfield-type-system.md#4-traits-are-coherent-qualified-types) requires stable evidence independent of import order. |

**Implementation:** (1) Keep `lib/catena/type/trait.ex` ownership rejection;
(2) combine future P101 package fixtures with C025 nominal origin resolution;
(3) rebuild with import order and checkout path variations through
`lib/catena/package/linker.ex`. **Evidence/gate:** positive same selected
identity; negative duplicate/orphan implementations; boundary two wrappers
over one representation can own distinct lawful instances. Retain C070.

## Item 071 — Associated information (C071)

**Dependencies and scope:** C065/C069/C070 and P101's hierarchy use cases.

| Decision | Four explored alternatives | Selected recommendation and research basis |
| --- | --- | --- |
| CP-071-1 | A: Retain methods, fundeps, and terminating associated types, useful with solver obligations. B: Add associated constants, convenient but currently excluded. C: Permit unrestricted type families, powerful but threatens termination. D: Remove associated information, simpler but breaks existing trait expressivity. | **A, recommended and agent-selected.** [Trait constraints](../60-specification/type-system/rows-traits-and-effects.md#traits) constrain normalization after unique instance selection. |
| CP-071-2 | A: Add consistency and cycle counterexamples for each new associated equation, targeted with testing cost. B: Normalize before selecting instances, tempting but can choose evidence circularly. C: Assume equations are injective, powerful but unjustified. D: Stop only on runtime timeout, pragmatic but not a semantic termination rule. | **A, recommended and agent-selected.** [Solver measures](../60-specification/type-system/rows-traits-and-effects.md#solver-interface) provide a finite, reproducible rejection discipline. |

**Implementation:** (1) Add library equations through `lib/catena/type/trait.ex`;
(2) preserve serialized associated types in `lib/catena/categorical.ex`;
(3) extend existing type/C004 fixtures for the actual new equations.
**Evidence/gate:** positive determined output and terminating normalization;
negative inconsistent fundeps/cycles/associated constants; boundary unresolved
inputs remain ambiguous. Retain C071, without adding general type computation.

## Item 072 — Laws and evidence levels (C072)

**Dependencies and scope:** C004/C110/C111/C113 and P135 optimizer restrictions.

| Decision | Four explored alternatives | Selected recommendation and research basis |
| --- | --- | --- |
| CP-072-1 | A: Preserve promised/tested/derived with explicit domains, honest but less grand than proof claims. B: Treat passing properties as proof, convenient but false. C: Trust standard instances universally, fast but unsupported. D: Remove law metadata, simple but loses reviewable guarantees. | **A, recommended and agent-selected.** [Evidence tiers](../60-specification/traits-and-categorical-operations/laws-derivation-and-testing.md#evidence-tiers) and [category research](category-theory-for-programming.md#the-lawfulness-ladder) distinguish evidence strength. |
| CP-072-2 | A: Test laws with explicit equality and finite callback samples, reproducible with bounded coverage. B: Use host equality implicitly, easy but bypasses Catena instances. C: Test effectful callbacks as pure laws, broad but invalid domain. D: Let law labels authorize fusion, fast but changes observations. | **A, recommended and agent-selected.** [Law testing](../60-specification/traits-and-categorical-operations/laws-derivation-and-testing.md#law-testing) records seeds, domains, identities, and invalidation. |

**Implementation:** (1) Use `lib/catena/categorical/law.ex` for new library
law suites; (2) record instance/type/interface digest and finite domains;
(3) include intentionally unlawful instances in
`test/catena/c004_categorical_test.exs`; (4) keep law claims erased from
runtime. **Evidence/gate:** positive reproducible bounded laws; negative
unlawful instance/missing equality/reserved trust level; boundary changed
instance digest invalidates evidence. Retain C072 without universal proof.

## Item 073 — Structural derivation (C073)

**Dependencies and scope:** C002/C062/C065/C072/C074 and P102's standard collections.

| Decision | Four explored alternatives | Selected recommendation and research basis |
| --- | --- | --- |
| CP-073-1 | A: Keep explicit-target structural derivation with shape checks, safe but rejects hard datatypes. B: Derive from requested names alone, easy but unsound. C: Offer manual override hooks, useful but changes minimal method authority. D: Infer target parameters heuristically, concise but ambiguous for multiple slots. | **A, recommended and agent-selected.** [Structural derivation](../60-specification/traits-and-categorical-operations/laws-derivation-and-testing.md#structural-derivation) fixes target, variance, positivity, and regularity checks. |
| CP-073-2 | A: Keep standard List stack-safe implementations distinct from general structural templates, honest with two paths. B: Claim every derived recursive function stack-safe, simple but false. C: Replace all derivation with runtime reflection, general but violates erasure. D: Equate collecting traversal with pure mapping, easy but loses contextual sequencing. | **A, recommended and agent-selected.** [Operational obligations](../60-specification/traits-and-categorical-operations/operational-semantics.md#stack-and-cost-obligations) apply only to supported standard instances and declared shapes. |

**Implementation:** (1) Reuse `lib/catena/derive.ex` checks for new datatypes;
(2) keep `lib/catena/standard_list.ex` stack-safe algorithms; (3) test explicit
single/two-slot targets and rejected negative/existential/GADT shapes;
(4) do not infer a standard collecting instance from its datatype template.
**Evidence/gate:** positive constructor-complete derived operation; negative
unsupported shape and implicit targets; boundary 250,000-element supported
standard operations versus separately disclosed general derivation stack cost.
Retain C073.

## Item 074 — Categorical operation execution (C074)

**Dependencies and scope:** C030/C072/C073, P053/P057, and P102/P108.

| Decision | Four explored alternatives | Selected recommendation and research basis |
| --- | --- | --- |
| CP-074-1 | A: Preserve strict left-to-right exact-once traversal and subject-last ABI, stable with explicit early-stop protocols. B: Let associativity reorder callbacks, fast but invalid with effects. C: Implicitly parallelize applicatives, attractive but unsound scheduling inference. D: Short-circuit every fold, efficient but changes cardinality. | **A, recommended and agent-selected.** [Categorical operation semantics](../60-specification/traits-and-categorical-operations/operational-semantics.md#strict-sequential-baseline) fixes execution independently of laws. |
| CP-074-2 | A: Add noncommuting callback traces and failure prefixes for new operations, sensitive with more fixtures. B: Test pure final values only, cheap but incomplete. C: Trust derived provenance for order, compact but conflates correctness facets. D: Compare timings, practical but nondeterministic. | **A, recommended and agent-selected.** [Divergence and effects](../60-specification/traits-and-categorical-operations/operational-semantics.md#divergence-and-effects) preserve prefix order even outside law domains. |

**Implementation:** (1) Preserve `lib/catena/standard_list.ex` and generated
field order in `lib/catena/derive.ex`; (2) exercise future P102 operations
with per-position observations; (3) retain subject-last interface snapshots
and actual compiled calls. **Evidence/gate:** positive ordered callbacks;
negative hidden duplication/reordering/early stop; boundary divergence or trap
after a finite prefix prevents later callbacks. Retain C074.

## Item 075 — Dispatch and dictionary observability (C075)

**Dependencies and scope:** C065/C070/C113, P093/P094/P128, and P135.

| Decision | Four explored alternatives | Selected recommendation and research basis |
| --- | --- | --- |
| CP-075-1 | A: Preserve manifest-directed specialization and direct calls, predictable with companion artifacts. B: Pass runtime dictionaries everywhere, flexible but changes observability. C: Use reflective lookup, extensible but violates erasure. D: Specialize from incidental build order, quick but nonreproducible. | **A, recommended and agent-selected.** [Specialization and BEAM](../60-specification/traits-and-categorical-operations/interfaces-specialization-and-beam.md) establishes the current artifact contract. |
| CP-075-2 | A: Pair artifact inspection with trace equivalence, complete with two evidence views. B: Check only no metadata chunks, cheap but misses runtime plumbing. C: Check only values, compact but misses reflection leaks. D: Assume erasure follows optimization, convenient but unsupported. | **A, recommended and agent-selected.** [Evidence erasure observations](../60-specification/traits-and-categorical-operations/operational-semantics.md#divergence-and-effects) include messages, effects, and cleanup. |

**Implementation:** (1) Inspect compiled exports/chunks/direct calls after
new instances using `lib/catena/compiler.ex` and package specialization;
(2) preserve one declared companion BEAM; (3) repeat builds under controlled
input changes in C004 tests. **Evidence/gate:** positive identical observable
traces and deterministic artifacts; negative reflection/evidence escape and
undeclared specialization; boundary separate compilation with retained
interface digest. Retain C075.

## Item 076 — Existing effect declaration roles (C076)

**Dependencies and scope:** C005/C077–C079/C082, P053, G080, and later P109.

| Decision | Four explored alternatives | Selected recommendation and research basis |
| --- | --- | --- |
| CP-076-1 | A: Reuse existing operation/handler roles in internal ASTs, stable but adapter-heavy. B: Invent resource-specific effect syntax now, concise but violates vocabulary boundary. C: Encode requests as untyped host calls, expedient but loses rows. D: Add higher-order operations immediately, expressive but exceeds the current callback contract. | **A, recommended and agent-selected.** [Declarations and requests](../60-specification/effects-and-handlers/declarations-requests-and-signatures.md) define the available roles; higher-order effects remain D083. |
| CP-076-2 | A: Preserve complete handlers and mandatory return clauses in new fixtures, explicit with some boilerplate. B: Generate missing clauses implicitly, convenient but hides authority. C: Use ambient host defaults, quick but conflicts with C082. D: Accept partial handlers by nearest-label fallback, flexible but breaks lexical selection. | **A, recommended and agent-selected.** [Deep handler results](../60-specification/effects-and-handlers/deep-handlers-and-affine-resumptions.md#result-and-clause-effects) makes every interpretation explicit. |

**Implementation:** (1) Use `lib/catena/effect.ex` and kernel declarations
for P053/G080 harnesses; (2) preserve decoder/checker diagnostics;
(3) rerun `test/catena/c005_effects_test.exs` cross-module witnesses after
new row plumbing. **Evidence/gate:** positive complete existing-role handlers;
negative missing return/operation and unknown request; boundary pure function
operation arguments remain closed and effect-free. Retain C076 without any
new public words.

## Item 077 — Lexical handler selection (C077)

**Dependencies and scope:** C064/C076/C078 and all capability-bearing runtime work.

| Decision | Four explored alternatives | Selected recommendation and research basis |
| --- | --- | --- |
| CP-077-1 | A: Preserve static lexical identity selection, compositional with explicit ambiguity errors. B: Choose nearest runtime label, intuitive but captures abstract effects. C: Choose by family only, simple but collapses multiple capabilities. D: Pass a global handler registry, easy but ambient and mutable. | **A, recommended and agent-selected.** [Lexical capability identity](../60-specification/effects-and-handlers/capabilities-rows-and-selection.md#lexical-capability-identity) and [abstraction safety research](algebraic-effects-and-handlers.md#why-nearest-matching-label-is-not-enough) support the current model. |
| CP-077-2 | A: Exercise same-family distinct capabilities through new worker/callback boundaries, sensitive with identity normalization. B: Use one handler per family, simpler but misses the invariant. C: Remove all family occurrences when handling, easy but unsound. D: Resolve ambiguous requests by source order, convenient but changes meaning. | **A, recommended and agent-selected.** [Row subtraction](../60-specification/effects-and-handlers/capabilities-rows-and-selection.md#union-unification-and-subtraction) removes exactly the selected identity. |

**Implementation:** (1) Audit P053 worker forwarding and future P106 service
values through `lib/catena/effect/row.ex` and kernel checker/backend;
(2) preserve C005 distinct-capability and ambiguity fixtures;
(3) keep runtime handles opaque. **Evidence/gate:** positive explicitly selected
same-family handlers; negative ambiguous/unbound selection and fresh identity
escape; boundary handling one occurrence leaves the other residual. Retain C077.

## Item 078 — Affine resumptions (C078)

**Dependencies and scope:** C063/C068/C076, G080/G088, and D083's exclusion gate.

| Decision | Four explored alternatives | Selected recommendation and research basis |
| --- | --- | --- |
| CP-078-1 | A: Keep static affine checking plus consumed runtime token, robust with dual enforcement. B: Rely only on static checks, lighter but loses defect defense. C: Permit multi-shot resumptions, powerful but duplicates resources. D: Require exactly one resume, simpler cleanup but removes handler abort. | **A, recommended and agent-selected.** [Affine resumption form](../60-specification/effects-and-handlers/deep-handlers-and-affine-resumptions.md#affine-resumption-form) allows zero or one use, not general linear values. |
| CP-078-2 | A: Audit abandonment and consumption across cleanup/cancellation transitions, necessary with a lifecycle model. B: Infer cleanup from token consumption, simple but unsupported. C: Store resumptions in resource records, convenient but violates scope. D: Make resumptions sendable, expressive but breaks process-local authority. | **A, recommended and agent-selected.** [One-shot versus exactly-once research](algebraic-effects-and-handlers.md#one-shot-means-exactly-once) explains why affine control does not supply finalization. |

**Implementation:** (1) Preserve typed-core verifier checks and
`lib/catena/runtime/resumption_token.ex`; (2) add lifecycle tests at G080/G088
without widening resumption values; (3) retain both static rejection and
runtime double-entry defense tests in C005/resumption suites.
**Evidence/gate:** positive one resume on mutually exclusive branches and
zero-use abort; negative escape/storage/double use; boundary cancellation
before/after token consumption has a single defined terminal transition.
Retain C078; resource guarantees require their own slice.

## Item 079 — Handler execution order (C079)

**Dependencies and scope:** C030/C076–C078, P053, and G080/G088.

| Decision | Four explored alternatives | Selected recommendation and research basis |
| --- | --- | --- |
| CP-079-1 | A: Preserve deep reinstallation and outer-scope clause effects, precise with explicit nesting. B: Switch to shallow handlers, useful but changes continuations. C: Run clauses under themselves implicitly, convenient but changes forwarding. D: Commute handlers with equal families, optimization-friendly but observably wrong. | **A, recommended and agent-selected.** [Deep request rule](../60-specification/effects-and-handlers/deep-handlers-and-affine-resumptions.md#deep-request-rule) fixes the interpretation boundary. |
| CP-079-2 | A: Reuse independent free-request evaluation and kernel/BEAM traces for integration, strong with normalization work. B: Compare only compiled values, cheap but misses order. C: Compare generated CPS text, stable but not execution. D: Test only one nesting order, simple but cannot reveal noncommutativity. | **A, recommended and agent-selected.** [Handler-order research](algebraic-effects-and-handlers.md#handler-order-is-semantic) treats nesting as observable rather than an algebraic rearrangement. |

**Implementation:** (1) Preserve `lib/catena/effect/reference.ex` independently
from `lib/catena/effect/runtime.ex`; (2) rerun C005 outer-scope argument,
forwarding, and reversed-nesting tests after P053/G080 changes;
(3) add only interactions not already covered. **Evidence/gate:** positive
exact argument/request/resume/return order; negative discarded continuation
never runs; boundary return/operation clauses perform effects through outer
identities. Retain C079 without assuming resource unwinding is already solved.

## Item 080 — Cleanup and resource scopes (G080)

**Dependencies and scope:** C036/C078/C081, P084/G088 transition model,
G096/G098 foreign ownership, and P103 typed failure semantics modeled first
with existing ADTs. These are integration interfaces; local scopes do not
wait for completed foreign calls or the final named outcome library. Define local rules first;
foreign-frame behavior is a separate integration gate, not an assumed benefit
of affine handlers. The following choices are proposed semantic extensions.

| Decision | Four explored alternatives | Selected recommendation and research basis |
| --- | --- | --- |
| CP-080-1 | A: Introduce a runtime-owned lexical resource scope in the dormant core, explicit lifetime with new verification work. B: Encode cleanup as ordinary first-order effects, elegant but abandonment can discard it. C: Rely on garbage collection, simple but nondeterministic. D: Require user-managed release only, minimal but leak-prone under abort. | **A, recommended and agent-selected.** [Scoped-effect research](algebraic-effects-and-handlers.md#scoped-and-higher-order-effects) shows first-order handlers do not establish resource scopes; no new public syntax follows from an internal model. |
| CP-080-2 | A: Register release only after successful acquisition and unwind acquired resources in reverse order, compositional with bookkeeping. B: Release in acquisition order, simple but breaks nested dependencies. C: Release before acquisition returns, easy bookkeeping but may release nonexistent resources. D: Allow unordered release, parallel-friendly but changes effects. | **A, recommended and agent-selected.** [Resource-scope gap](../60-specification/effects-and-handlers/deep-handlers-and-affine-resumptions.md#result-and-clause-effects) needs explicit acquisition/abandonment rules; reverse dependency order is a proposed extension, not a theorem supplied by category laws. |
| CP-080-3 | A: Separate normal return, typed failure, handler abort, trap, cancellation, process exit, and VM loss in an outcome matrix, precise with many cases. B: Call every path an exception, familiar but violates C081. C: Promise cleanup even after VM crash, reassuring but unrealizable. D: Specify success only, small but leaves the hard cases open. | **A, recommended and agent-selected.** [Exception boundary](../60-specification/exception-boundary/README.md) and [runtime limits](../IMPLEMENTATION-LIMITS.md#runtime-and-mailbox-capacity) require classified failure and honest external-failure limits. |
| CP-080-4 | A: Preserve primary failure provenance, attempt remaining bounded releases, and classify release errors by explicit precedence, informative with ordering policy. B: Replace the primary failure with the last release failure, simple but loses cause. C: Ignore release failures, quiet but hides leaks. D: Resume the abandoned computation after cleanup failure, recoverable-looking but violates terminal/abort semantics. | **A, recommended and agent-selected.** [Failure partition research](catena-exception-boundary.md) keeps value failure, abort, and terminal trap distinct; the secondary-report mechanism must be specified without making traps catchable. |
| CP-080-5 | A: Mask cooperative cancellation during bounded release and expose forced termination as a limit, robust with a deadline policy. B: Allow arbitrary repeated cancellation inside release, responsive but leak-prone. C: Make release uninterruptible forever, strong cleanup but can hang shutdown. D: Assume foreign unwinding always cooperates, simple but unsupported. | **A, recommended and agent-selected.** [Effects/resources research](algebraic-effects-and-handlers.md#verification-and-falsification) requires explicit cancellation and foreign-frame boundaries; G088 supplies the bounded policy. |
| CP-080-6 | A: Preserve an existing primary trap; otherwise a failed mandatory release makes completion fail terminally, retaining ordered secondary diagnostics. B: Report success when only release failed, convenient but conceals a broken guarantee. C: Replace every primary failure with the last release error, simple but loses cause. D: Convert traps into an aggregate recoverable value, informative but violates C081. | **A, recommended and agent-selected.** [The failure partition](catena-exception-boundary.md) requires terminal traps to remain terminal; the new release-failure producer needs explicit normative classification rather than a catch-all exception form. |
| CP-080-7 | A: Give each resource one runtime scope owner with nonescaping typed handles and one release registration, bounded with escape checks. B: Use general linear types for all values, strong but crosses C140. C: Let aliases independently release, easy but double-frees. D: Transfer ownership implicitly on closure capture, convenient but hides lifetime. | **A, recommended and agent-selected.** [Affine control limits](../60-specification/type-system/advanced-type-checking.md#affine-resumptions) do not imply general linear resources; ordinary resource handles are distinct from non-first-class lexical effect capability identities. |

**Implementation:** (1) Write a proposed transition table for unacquired,
acquired, releasing, and released scope entries, including nested scopes and
reentrancy; (2) define failure precedence and masked-release deadlines jointly
with G088; (3) add a small executable reference state machine and dormant
core/verifier representation in the sibling, using existing effect/handler
roles for computations; (4) lower local scope control through
`lib/catena/kernel/backend.ex` while preserving terminal trap semantics;
(5) integrate release ownership with P084 process exit; (6) add explicit
foreign registration/ownership adapters only when G096/G098 arrive;
(7) promote a revision only after the local and admitted foreign obligations
have matching implementation evidence. New core storage is proposed work;
no existing resource-scope module is claimed.
**Evidence/gate:** positive nested normal release and abort cleanup; negative
use-after-release, double release, acquisition failure, release failure and
repeated cancellation; boundary trap, blocked release, external kill, VM loss,
and foreign nonlocal failure each have an explicit guarantee or exclusion.
G080 remains open until every listed path is classified and executable for
the admitted boundary; a local bracket demonstration alone cannot close it.

## Item 081 — Value failure, abort, and terminal trap (C081)

**Dependencies and scope:** C036/C044/C076–C079, G080/G088, P103/P105,
and G095/G096. Preserve the already completed partition.

| Decision | Four explored alternatives | Selected recommendation and research basis |
| --- | --- | --- |
| CP-081-1 | A: Keep typed failure values, handler escape, and terminal traps distinct, clear with separate contracts. B: Add one catch-all exception form, familiar but changes the language. C: Turn all traps into values, convenient but breaks terminality. D: Turn all failure values into traps, simple but destroys recoverable composition. | **A, recommended and agent-selected.** [Exception synthesis](catena-exception-boundary.md) and the [normative boundary](../60-specification/exception-boundary/README.md) establish the partition. |
| CP-081-2 | A: Integrate cleanup beneath terminal control without exposing a source catch operation, useful with runtime discipline. B: Let cleanup catch and resume traps, flexible but violates C036. C: Skip every release after trap without review, easy but preempts G080. D: Let host exceptions leak unchanged, cheap but obscures classification. | **A, recommended and agent-selected.** [Handler abandonment](../60-specification/effects-and-handlers/deep-handlers-and-affine-resumptions.md#result-and-clause-effects) and [G080's gap](../00-inbox/language-specification-completeness-checklist.md) leave cleanup to an explicit extension while retaining terminality. |

**Implementation:** (1) Keep `test/catena/c081_exception_boundary_test.exs`
value/abort/trap witnesses; (2) use them as regression anchors for G080/G088;
(3) require G095/G096 to map foreign outcomes at the visible boundary;
(4) preserve reserved trap kinds until their producer slices arrive.
**Evidence/gate:** positive declining handler and typed outcome composition;
negative source recovery from terminal trap; boundary process-local trap does
not silently acquire spawner propagation. Retain C081.

## Item 082 — Explicit entry authority (C082)

**Dependencies and scope:** C027/C077, P106 environmental services, and G089.

| Decision | Four explored alternatives | Selected recommendation and research basis |
| --- | --- | --- |
| CP-082-1 | A: Preserve effect-closed invocation-only entries until an explicit capability-channel amendment, clear with staged work. B: Install ambient host handlers, easy demos but violates authority. C: Treat supervision as effect interpretation, convenient but conflates domains. D: Add hidden environment globals, familiar but untyped and ambient. | **A, recommended and agent-selected.** [Top-level boundary](../60-specification/top-level-effects/the-top-level-boundary.md) fixes the current silence and P106's explicit amendment route. |
| CP-082-2 | A: Require a deny-able typed launch capability contract when P106 arrives, principled with entry revision work. B: Smuggle capability through zero-argument globals, quick but contradictory. C: Widen every entry preemptively, flexible but unnecessary. D: Forbid environmental programs permanently, simple but defeats a functional language. | **A, recommended and agent-selected.** [Top-level synthesis](catena-top-level-effects.md) separates a future channel from ambient authority. |

**Implementation:** (1) Preserve `lib/catena/entry.ex` checks and
`test/catena/c082_top_level_test.exs`; (2) define P106's typed service values
and denial semantics before changing entries; (3) amend C027/C082 applicability
explicitly in that future slice; (4) keep supervisors concerned with process
failure only. **Evidence/gate:** positive closed zero-argument launch now;
negative residual effects (`ENT001`); boundary missing/denied future capability
is defined only by its admitted channel. Retain C082 until that explicit revision.

## Item 083 — Scoped and multi-shot computations (D083)

**Dependencies and scope:** C078/C140, G080/G088, P102, and D059. This is a
research and admission program; it does not widen resumptions or vocabulary.

| Decision | Four explored alternatives | Selected recommendation and research basis |
| --- | --- | --- |
| CP-083-1 | A: Preserve affine deep handlers and separately gate each control family, safe but slower expansion. B: Admit multi-shot by removing the consumed token, tiny code change but unsafe. C: Add shallow handlers under the same form, convenient but changes meaning. D: Ban all higher-order control forever, simple but stronger than evidence. | **A, recommended and agent-selected.** [Multi-shot resource risks](algebraic-effects-and-handlers.md#multi-shot-is-just-calling-a-function-twice) and [scope research](algebraic-effects-and-handlers.md#scoped-and-higher-order-effects) make separate contracts necessary. |
| CP-083-2 | A: Compare bounded library encodings before new core control, evidence-driven with prototype cost. B: Choose by theoretical elegance alone, coherent but ignores practical failure. C: Copy a host continuation API, quick but imports unsafe ownership. D: Generalize every effect operation to accept computations, uniform but threatens abstraction. | **A, recommended and agent-selected.** [Combinator inclusion criteria](combinators-for-algebraic-data-and-categorical-programming.md#inclusion-standard) require a simpler-library comparison. |
| CP-083-3 | A: Require continuation ownership, cancellation, cleanup, and foreign-frame evidence per admitted family, complete with large gates. B: Require only a typing rule, small but misses runtime hazards. C: Require only benchmarks, practical but misses correctness. D: Treat categorical laws as resumption safety, elegant but false. | **A, recommended and agent-selected.** [Verification obligations](algebraic-effects-and-handlers.md#verification-and-falsification) explicitly separate these guarantees. |

**Implementation:** (1) Inventory generators, async, nondeterminism,
transactions, shallow handlers, higher-order effects, and multi-shot control
individually; (2) prototype bounded encodings using existing
`lib/catena/effect/reference.ex` and typed core; (3) document where encoding
fails lifecycle requirements; (4) retain C005/C140 exclusion tests.
**Evidence/gate:** positive bounded library use cases; negative captured,
duplicated, or escaped resumptions remain rejected; boundary abandoned
resource-bearing continuation is an admission counterexample. Keep D083
unchecked until a separately scoped form satisfies the gate; no omnibus
control feature or vocabulary is planned now.

## Item 084 — Process lifetime and relationships (P084)

**Dependencies and scope:** C010/C078/C081, G080/G088 transition model,
the local message baseline, and later P087/G089 integration. Protocols and
supervision consume the new lifetime primitives; they are not prerequisites
for defining those primitives. Retain existing unlinked spawn behavior and add wider
lifetime semantics explicitly rather than reinterpreting it.

| Decision | Four explored alternatives | Selected recommendation and research basis |
| --- | --- | --- |
| CP-084-1 | A: Retain raw isolated spawn and add explicit library-managed structured lifetimes, compatible with two use cases. B: Make every spawn parent-owned, tidy but changes C010. C: Expose raw OTP lifecycle primitives without typing, quick but leaks host semantics. D: Forbid detached actors, structured but incompatible with existing behavior. | **A, recommended and agent-selected.** [Actors contract](../60-specification/formal-semantic-kernel/actors-messages-and-failures.md#spawn-and-self) already fixes isolation; [actor research](../30-sources/agha-1986-actors.md) motivates independent lifetime. |
| CP-084-2 | A: Define typed monitored completion separately from symmetric linked failure propagation, precise with explicit policies. B: Treat links and monitors identically, simple but semantically wrong. C: Turn all exits into arbitrary mailbox terms, familiar but breaks closed typing. D: Infer relationships from lexical nesting, convenient but hides failure paths. | **A, recommended and agent-selected.** [Pinned OTP process research](../30-sources/erlang-otp-29-processes.md) identifies these facilities as extensions beyond ordinary messages. |
| CP-084-3 | A: Specify terminal states and one notification per relationship before backend mapping, reviewable with a transition table. B: Wrap host calls first and document outcomes later, fast but inherits accidents. C: Poll liveness, straightforward but racy. D: Let process handles expose status fields, useful but changes opacity and equality. | **A, recommended and agent-selected.** [Completion and trap](../60-specification/formal-semantic-kernel/actors-messages-and-failures.md#completion-and-trap) supplies a baseline whose observability must be amended explicitly. |
| CP-084-4 | A: Keep child capabilities explicit and process-local while allowing only admitted sendable values, secure with more wiring. B: Inherit all parent handlers, easy but leaks authority. C: Share resumption tokens, efficient but violates affine scope. D: Use ambient supervision services, convenient but conflicts with C082. | **A, recommended and agent-selected.** [Spawn isolation](../60-specification/formal-semantic-kernel/actors-messages-and-failures.md#spawn-and-self) and [capability scope](../60-specification/effects-and-handlers/capabilities-rows-and-selection.md#scope-and-abstraction) preserve compositional authority. |
| CP-084-5 | A: Give a structured child exactly one lexical lifetime owner and join all owned children before normal scope completion, compositional with waiting. B: Detach children automatically on return, responsive but leaks work. C: Let several scopes own one child, flexible but makes cancellation ambiguous. D: Make all existing raw spawns structured, uniform but reinterprets C010. | **A, recommended and agent-selected.** [Raw spawn isolation](../60-specification/formal-semantic-kernel/actors-messages-and-failures.md#spawn-and-self) remains unchanged; structured ownership is an explicitly admitted library-managed lifetime. |
| CP-084-6 | A: On an observed child failure cancel sibling owned work, await bounded cleanup, and return the first observed failure plus secondary evidence, prompt with schedule-dependent first observation. B: Wait forever for every sibling, complete results but poor failure response. C: Ignore child failures, independent but defeats structured failure. D: Terminate siblings immediately without cleanup, fast but breaks G080. | **A, recommended and agent-selected.** [Process-local failure](../60-specification/formal-semantic-kernel/actors-messages-and-failures.md#completion-and-trap) is retained for raw actors; the new owner explicitly interprets it and does not promise deterministic first failure across schedules. |

**Implementation:** (1) Extend the C010 state model with explicit relationship
records and typed terminal observations, leaving raw spawn unchanged;
(2) define registration/termination races, demonitoring, link propagation,
exit-trapping scope, and parent cancellation in the shared lifecycle table;
(3) extend dormant core checking and reference transitions in
`lib/catena/kernel/checker.ex`/`stepper.ex`; (4) map admitted operations to OTP
only after checking pinned primary docs and reproducing edge cases;
(5) implement structured lifetime management as a typed library over the
minimal admitted primitives; (6) compare modeled and actual traces.
**Evidence/gate:** positive normal child completion, linked failure, monitor
observation, and structured join; negative capability inheritance, duplicate
notification, forged handles, and escaped resumptions; boundary child exits
before relationship registration, parent cancellation during acquisition, and
unread mailbox disposal. P084 closes only with every listed relationship
classified and witnessed, including interaction with G080/G088.

## Item 085 — Messages, capacity, and transport (P085)

**Dependencies and scope:** C010/C037/C040, P084/P129 and the minimal G095/G098 ownership contract; P087/G091 are
consumers of local messaging and later final integration gates.

| Decision | Four explored alternatives | Selected recommendation and research basis |
| --- | --- | --- |
| CP-085-1 | A: Preserve local Unit-returning asynchronous send and dead-target discard, compatible but no delivery acknowledgement. B: Change send to acknowledge processing, useful but blocking and incompatible. C: Report liveness from send, convenient but racy. D: Retry implicitly, reliable-looking but may duplicate effects. | **A, recommended and agent-selected.** [Local send](../60-specification/formal-semantic-kernel/actors-messages-and-failures.md#send) is already normative; acknowledged protocols belong to P087. |
| CP-085-2 | A: Keep value immutability while allowing unobservable physical sharing, efficient with checked foreign ownership. B: Require deep copying everywhere, simple but costly and unsupported. C: Expose sharing identity, optimizable but breaks abstraction. D: Share mutable foreign buffers unchecked, fast but violates sendability. | **A, recommended and agent-selected.** [Value-level send semantics](../60-specification/formal-semantic-kernel/actors-messages-and-failures.md#send) separates meaning from layout; G095/G098 own foreign validation. |
| CP-085-3 | A: Classify mailbox capacity as deployment-defined with explicit overload controls above raw send, honest with layered APIs later. B: Promise a universal message-count floor, simple but ignores size. C: Block every send at a hidden quota, protective but changes order/liveness. D: Silently drop live-target messages under pressure, cheap but violates the admitted local contract. | **A, recommended and agent-selected.** [Resource-control research](../30-sources/erlang-otp-29-runtime-resource-controls.md) and [capacity policy](../IMPLEMENTATION-LIMITS.md#runtime-and-mailbox-capacity) reject a universal numeric mailbox floor. |
| CP-085-4 | A: Specify remote delivery separately with explicit uncertainty and no automatic application retry, honest with more protocol work. B: Extend local guarantees blindly across nodes, easy but false. C: Promise exactly-once processing, attractive but lacks transactional evidence. D: Prohibit all remote sends permanently, safe but defeats G091. | **A, recommended and agent-selected.** [Local scope](../60-specification/formal-semantic-kernel/actors-messages-and-failures.md#deliberately-absent-process-facilities) leaves remote guarantees to a distinct slice. |
| CP-085-5 | A: Finish and credit local capacity/ownership rules before remote integration, with P085's final remote gate consuming G091, acyclic but staged. B: Require complete distribution before any local message work, tidy but circular. C: Mark all P085 complete after local tests, quick but false. D: Fold G091 into the local kernel, uniform but hides new failure semantics. | **A, recommended and agent-selected.** [The local kernel boundary](../60-specification/formal-semantic-kernel/actors-messages-and-failures.md#deliberately-absent-process-facilities) already separates local message foundations from remote delivery. |

**Implementation:** (1) Preserve existing `send` reference/backend cases and
C010 FIFO/dead-target tests; (2) document admitted immutable value/foreign
resource sendability cases; (3) integrate deployment limits and overload
observations with P129, fixing stale capacity-owner profile labels there;
(4) add typed backpressure/request protocols above raw send;
(5) let G091 implement the remote transport contract explicitly.
**Evidence/gate:** positive local FIFO and immutable payload observations;
negative invalid payload and hidden live-message discard; boundary multiple
senders, dead target, oversized resources, quota-triggered process death, and
remote uncertainty each have owned outcomes. Local extensions can be credited
without pretending remote delivery is already complete.

## Item 086 — Selective receive conflict (P086)

**Dependencies and scope:** C003/C010/C044, P085/P087, G088 and later P109.
Resolve the actual contradiction before changing the checklist or traceability.

| Decision | Four explored alternatives | Selected recommendation and research basis |
| --- | --- | --- |
| CP-086-1 | A: Clarify starvation to waiting when no queued message matches and scheduler/selection starvation otherwise, coherent with scan rules. B: Block behind every rejected prefix, simple FIFO but changes selective receive. C: Consume rejected messages, avoids backlog but violates preservation. D: Declare scan implementation-defined, flexible but abandons existing guarantees. | **A, recommended and agent-selected.** [C010 selective receive](../60-specification/formal-semantic-kernel/actors-messages-and-failures.md#selective-receive) and [the audit](../50-journal/2026-09-06-checklist-completion-audit.md#selective-receive-conflict) support an explicit correction to the contradictory C086 starvation statement. |
| CP-086-2 | A: Publish the correction at the next unused semantic revision with explicit amended applicability and retained history, reviewable with version bookkeeping. B: Retroactively replace the old wording without a new revision, small but changes retained authority. C: Let compiler behavior decide authority, easy but violates governance. D: Withdraw all receive rules, conservative but discards supported semantics. | **A, recommended and agent-selected.** [Authority and applicability](../SPECIFICATION-AUTHORITY.md#status-and-applicability) require resolving the text conflict rather than treating tests as law. |
| CP-086-3 | A: Test rejected-prefix bypass, wholly rejected waiting, and repeated selection separately, precise with three fixtures. B: Reuse only the blocked mailbox fixture, cheap but never exercises bypass. C: Assert only final value, compact but misses preservation. D: Time out a host receive and infer starvation, simple but scheduler-dependent. | **A, recommended and agent-selected.** [Receive rules](../60-specification/selective-receive/the-receive-rule-set.md#the-rules) constrain selected value, one-time removal, and the residual mailbox. |
| CP-086-4 | A: Describe scan work by examined candidates without universal repeated-rescan claims, honest with implementation freedom. B: Promise a rescan of every rejected prefix on every runtime wakeup, concrete but may overstate implementation work. C: Promise constant-time receive, attractive but unsupported. D: Hide all scan-cost discussion, safe but unhelpful. | **A, recommended and agent-selected.** [C010 cost model](../60-specification/formal-semantic-kernel/actors-messages-and-failures.md#selective-receive) counts actually examined messages and clauses; C042 excludes a broader complexity promise. |

**Implementation:** (1) Write the exact proposed amendment to
`60-specification/selective-receive/the-receive-rule-set.md`, separating
no-match suspension, message starvation, and scheduler nonfairness;
(2) allocate the next unused semantic patch centrally (the audited next patch
is `0.1.49`) and state the amended applicability under C008, preserving the
old revision and historical manifests/evidence rather than silently
reinterpreting them; (3) inspect retained `find_receive/2` in
`lib/catena/kernel/stepper.ex` and native lowering in `backend.ex`;
(4) add C086-specific stepper/BEAM witnesses selecting a later match while
preserving the prefix, plus genuine no-match waiting and one-time removal;
(5) update RC-OBL-004, the inquiry, maps, and checklist together only after
normative applicability and evidence agree.
**Evidence/gate:** positive bypass and oldest matching selection; negative
prefix consumption/reordering and duplicate removal; boundary empty mailbox,
all rejected, and an earlier repeatedly accepted candidate. Completion does
not assert scheduler fairness or timeout semantics.

## Item 087 — Typed protocol contracts (P087)

**Dependencies and scope:** C010/C062/C068, P084/P085/P086, G088, P103,
and C028/G091 for evolution. Payload typing remains distinct from protocol proof.

| Decision | Four explored alternatives | Selected recommendation and research basis |
| --- | --- | --- |
| CP-087-1 | A: Begin with closed payload types plus explicit library state machines, practical without new type features. B: Add linear session types now, strong but crosses C140 and needs new theory. C: Use phantom-state handles alone, lightweight but duplication defeats sequencing claims. D: Leave protocols as untyped conventions, quick but loses existing checking. | **A, recommended and agent-selected.** [Actor typing](../60-specification/formal-semantic-kernel/actors-messages-and-failures.md) and [advanced boundaries](../60-specification/type-system/advanced-type-checking.md#explicit-exclusions) support typed data without claiming session guarantees. |
| CP-087-2 | A: Model request/reply correlation, terminal reply, timeout, and cancellation explicitly, robust with state bookkeeping. B: Pair replies by arrival order, simple but unsafe with interleaving. C: Use raw process identity as request identity, cheap but conflates concurrent requests. D: Retry until any reply arrives, convenient but duplicates effects. | **A, recommended and agent-selected.** [Selective-receive routing](../60-specification/selective-receive/the-routed-interfaces.md#typed-protocols-p087) requires protocols to compose with closed message types and preservation. |
| CP-087-3 | A: Version protocol state/message schemas and reject incompatible peers before exchange, predictable with handshake work. B: Assume constructors are backward-compatible, easy but false for closed sums. C: Widen receivers to dynamic terms, flexible but violates C067. D: Infer compatibility from matching display names, cheap but ignores identity. | **A, recommended and agent-selected.** [API compatibility](../60-specification/api-and-abi-compatibility/README.md) supplies the nominal compatibility discipline; remote encoding still needs G091. |

**Implementation:** (1) Specify protocol transition tables as ordinary typed
data/handlers using existing internal forms; (2) implement correlation and
terminal-state enforcement in a library layer with compiler-checked closed
mailbox signatures; (3) add local overlapping-request examples through
`lib/catena/kernel/interface.ex` and checker;
(4) integrate deterministic timeout/cancellation races from G088;
(5) define evolution checks with C028/G091. **Evidence/gate:** positive
interleaved request/reply with distinct correlations; negative wrong payload,
stale/double reply, invalid state transition and mismatched schema; boundary
peer death and late reply after timeout do not resurrect a completed request.
Close P087 only as the chosen explicit-library contract; do not claim static
session fidelity without a later admitted type system.

## Item 088 — Cancellation and time (G088)

**Dependencies and scope:** G080/P084 shared lifecycle model, P086's timeout
reservation, C036/C081, P103/P106, and G096/G098 blocking boundaries.

| Decision | Four explored alternatives | Selected recommendation and research basis |
| --- | --- | --- |
| CP-088-1 | A: Use monotonic relative durations and absolute monotonic deadlines with a virtual-clock reference, deterministic with conversion rules. B: Use wall time, familiar but jumps. C: Use reduction counts as language time, reproducible-looking but platform-dependent. D: Delegate all timing to unspecified host calls, easy but untestable semantics. | **A, recommended and agent-selected.** [Timeout interface](../60-specification/selective-receive/the-routed-interfaces.md#timeouts-and-cancellation-g088) requires explicit evaluation and race rules; exact host behavior must be verified before backend adoption. |
| CP-088-2 | A: Propagate cooperative cancellation through explicit owned scopes, controlled with defined safe points. B: Kill every child immediately, responsive but bypasses cleanup. C: Use global cancellation by process name, easy but ambient and racy. D: Ignore cancellation during computation, simple but unusable for resource scopes. | **A, recommended and agent-selected.** [Resource control research](algebraic-effects-and-handlers.md#scoped-and-higher-order-effects) requires cancellation to respect ownership rather than follow algebraic laws implicitly. |
| CP-088-3 | A: Define one linearized completion choice among message, deadline, cancellation, and failure, precise with schedule exploration. B: Let both timeout and reply callbacks run, easy but double-completes. C: Always prefer cancellation retroactively, convenient but rewrites completed observations. D: Use wall-clock arrival timestamps as total order, intuitive but distributed clocks cannot justify it. | **A, recommended and agent-selected.** [Receive timeout obligations](../60-specification/selective-receive/the-routed-interfaces.md#timeouts-and-cancellation-g088) demand an explicit permitted-interleaving set. |
| CP-088-4 | A: Evaluate timeout expression once before scanning, scan available messages, then suspend until the selected terminal event, clear with exact zero-duration rules. B: Reevaluate timeout after every rejected message, simple loop but repeats effects. C: Always time out before inspecting queued matches, deterministic but surprising. D: Reset duration on every arrival, responsive but can wait forever unintentionally. | **A, recommended and agent-selected.** The [routing chapter](../60-specification/selective-receive/the-routed-interfaces.md#timeouts-and-cancellation-g088) leaves this choice open; this proposal preserves ordinary once-per-reaching evaluation and oldest-match scanning. |
| CP-088-5 | A: Bound masked cleanup and classify noncooperative foreign work as outside prompt cancellation, honest with shutdown policy. B: Promise immediate cancellation of every foreign call, attractive but unsupported. C: Mask indefinitely, leak-resistant but can hang. D: Cancel finalizers freely, responsive but breaks release guarantees. | **A, recommended and agent-selected.** [Resource scope research](algebraic-effects-and-handlers.md#verification-and-falsification) requires separate normal cleanup and external termination claims. |
| CP-088-6 | A: Use exact nonnegative integer nanosecond durations and opaque local monotonic origins, rounding waits upward to host granularity, precise with conversions. B: Use floating seconds, familiar but introduces rounding ambiguity. C: Use wall-clock timestamps, interoperable but subject to clock changes. D: Expose host-dependent timer units, cheap but nonportable. | **A, recommended and agent-selected.** [Numeric domain discipline](catena-numeric-relationships.md) favors explicit exact conversion; this selects semantic measurement, not public time-type or operation names. |
| CP-088-7 | A: Poll cooperative cancellation at admitted task backedges/call boundaries and before or after blocking runtime work, useful with defined latency limits. B: Poll only at explicit user checks, simple but can miss termination. C: Interrupt at any machine instruction, prompt but unsafe for scope invariants. D: Make pure top-level evaluation cancellable through ambient state, convenient but changes C082. | **A, recommended and agent-selected.** [Resource observability](catena-resource-observability.md) separates scheduling from meaning; cancellation applies only within the explicitly admitted owned task model, never silently to retained pure entries. |

**Implementation:** (1) Define units, overflow, negative duration rejection,
zero deadline, clock origin, and timeout-expression order; (2) extend the
reference configuration with virtual time and cancellation state; (3) add
explicit safe-point and scope-ownership transitions jointly with G080/P084;
(4) enumerate race schedules using the pattern of
`lib/catena/kernel/explorer.ex`; (5) map to verified OTP monotonic clock/timer
operations through a typed runtime boundary; (6) integrate total receive
fallback and mailbox preservation; (7) add deterministic tests before
wall-clock smoke tests. **Evidence/gate:** positive cancellation propagation,
sleep/deadline completion, and cleanup; negative double completion, invalid
duration, leaked timer, or removal of unselected messages; boundary queued
matching message at zero timeout, deadline/reply race, cancelled waiting
receive, masked finalizer expiry, and foreign blockage all have named outcomes.
G088 closes only when the permitted outcomes match reference and BEAM behavior.

## Item 089 — Supervision (G089)

**Dependencies and scope:** P084/G080/G088, C025/C027/C028/C082,
the pinned P099 runtime profile, and G096's minimal typed OTP lifecycle
admission contract. General callbacks and complete environmental libraries
are later integration work, not prerequisites for this narrow adapter.

| Decision | Four explored alternatives | Selected recommendation and research basis |
| --- | --- | --- |
| CP-089-1 | A: Provide typed library supervision over minimal lifecycle primitives, familiar deployment with a bounded adapter. B: Make supervision a new language construct, integrated but expands core/vocabulary. C: Require handwritten untyped Erlang everywhere, flexible but weakens guarantees. D: Hide supervision inside every spawn, convenient but changes C010. | **A, recommended and agent-selected.** [Local kernel exclusions](../60-specification/formal-semantic-kernel/actors-messages-and-failures.md#deliberately-absent-process-facilities) reserve the facility, while [OTP research](../30-sources/erlang-otp-29-processes.md) provides the host context. |
| CP-089-2 | A: Specify supported restart policies and child lifecycle as typed data, explicit with validation. B: Expose arbitrary host configuration, flexible but under-specified. C: Restart every failure forever, resilient-looking but creates storms. D: Let failures silently terminate the whole tree, simple but loses supervision purpose. | **A, recommended and agent-selected.** [Resource capacity policy](../IMPLEMENTATION-LIMITS.md#runtime-and-mailbox-capacity) requires bounded operational controls; exact OTP policy mapping needs primary-source verification in this slice. |
| CP-089-3 | A: Keep supervision as process-failure interpretation with explicit capability provisioning, compositional with wiring. B: Let supervisors handle arbitrary language effects, convenient but violates C082. C: Inherit all child capabilities across restart, easy but may retain stale authority. D: Persist resumptions across restart, powerful but violates affine/process scope. | **A, recommended and agent-selected.** [Top-level boundary](../60-specification/top-level-effects/the-top-level-boundary.md) explicitly separates supervision from effect interpretation. |
| CP-089-4 | A: Generate deterministic validated OTP child specifications from typed descriptions, reviewable with an adapter artifact. B: Generate arbitrary runtime code, flexible but hard to audit. C: Interpret unvalidated maps at startup, quick but late failures. D: Freeze one hardcoded tree shape, simple but inadequate for applications. | **A, recommended and agent-selected.** [Entry and compatibility contracts](../60-specification/entry-points/README.md) motivate checked application structure with artifact provenance. |
| CP-089-5 | A: Support restart of the failed child, all children, or that child and later siblings, plus explicit always/abnormal-only/never child policies, useful with a finite policy matrix. B: Support failed-child restart only, simple but cannot model dependent children. C: Permit arbitrary supervisor callbacks to invent policies, flexible but hard to validate. D: Restart every child on every exit, easy but excessive and incompatible with temporary work. | **A, recommended and agent-selected.** [Pinned OTP process research](../30-sources/erlang-otp-29-processes.md) motivates host-aligned lifecycle concepts; exact supervisor mappings require the primary-source checks already scheduled, and these behavior descriptions do not select Catena API names. |
| CP-089-6 | A: Require explicit positive restart-count/window bounds and bounded cooperative shutdown grace, then classify forced termination, controlled with configuration burden. B: Restart without limits and wait indefinitely on shutdown, simple but storm-prone. C: Kill every child immediately, fast but bypasses cleanup. D: Apply undocumented global defaults, convenient but makes behavior environment-dependent. | **A, recommended and agent-selected.** [Runtime capacity policy](../IMPLEMENTATION-LIMITS.md#runtime-and-mailbox-capacity) requires disclosed operational bounds; source vocabulary for these configuration roles remains held. |
| CP-089-7 | A: Define the minimal typed OTP lifecycle adapter contract early, implement local supervision, then finish general foreign interoperability, acyclic with a narrow admission boundary. B: Wait for all G096 callbacks before supervision, orderly-looking but circular with cleanup. C: Bypass G096 with untyped host calls in libraries, expedient but unsafe. D: Add supervision primitives throughout the language core, direct but excessive. | **A, recommended and agent-selected.** [Visible foreign admission](catena-dynamic-and-unsafe-boundaries.md) requires a checked boundary, not completion of every unrelated foreign facility. |

**Implementation:** (1) Research pinned OTP supervisor/child-spec documentation
and preserve source notes for substantive new evidence; (2) encode the three selected restart strategies, three child restart
classes, explicit intensity bounds, and bounded shutdown grace in typed data;
(3) implement library validation and generated descriptors in the sibling,
consuming `lib/catena/entry.ex` and package metadata; (4) model restart decisions
independently from host execution; (5) test real process trees with deterministic
failure triggers; (6) document unsupported OTP features and interop escape
through G096. **Evidence/gate:** positive restart, ordered shutdown, permanent
child and temporary child policies; negative invalid child signature,
restart storm, stale capability, and bad shutdown bounds; boundary child
fails during startup/restart/shutdown. G089 closes only with the supported
policy inventory, runtime evidence, and compatibility story explicit.

## Item 090 — Scheduler observability (P090)

**Dependencies and scope:** C010/C037, P084/P085/P129, G088, G096/G098,
and P099's supported runtime profile.

| Decision | Four explored alternatives | Selected recommendation and research basis |
| --- | --- | --- |
| CP-090-1 | A: Preserve nondeterministic schedules and no language fairness guarantee, honest with weaker liveness claims. B: Promise deterministic scheduling, test-friendly but incompatible with ordinary BEAM operation. C: Promise round-robin fairness, intuitive but unsupported. D: Expose reduction counts as semantics, precise-looking but backend-dependent. | **A, recommended and agent-selected.** [Global configuration](../60-specification/formal-semantic-kernel/actors-messages-and-failures.md#global-configuration) defines permitted interleavings, not a fair scheduler. |
| CP-090-2 | A: Treat priorities and preemption as explicitly bounded runtime policy, practical with disclosure. B: Make priorities silently alter message order, efficient but violates P085. C: Hide all scheduler policy, simple but insufficient for blocking boundaries. D: Allow arbitrary user scheduler replacement, flexible but changes the execution model. | **A, recommended and agent-selected.** [Resource observability](catena-resource-observability.md) separates observable semantics from implementation and deployment controls. |
| CP-090-3 | A: Classify foreign work as nonblocking, scheduled blocking, or unsafe unbounded work, actionable with adapter obligations. B: Assume all FFI is preemptible, easy but unsafe. C: Run every foreign call on ordinary schedulers, fast but starvation-prone. D: Forbid all foreign work, safe but defeats interoperability. | **A, recommended and agent-selected.** [Runtime controls evidence](../30-sources/erlang-otp-29-runtime-resource-controls.md) motivates concrete capacity boundaries; G096/G098 must verify exact host classes. |

**Implementation:** (1) Publish a variability register for scheduling,
priorities, reduction preemption, and foreign-work admission; (2) preserve
reference nondeterminism in `lib/catena/kernel/explorer.ex`;
(3) add runtime-profile fields and validators in
`lib/catena/conformance_info.ex`/`implementation_limits.ex`;
(4) test accepted trace sets and blocked-work isolation under admitted FFI
classes. **Evidence/gate:** positive per-sender order across several schedules;
negative false deterministic/fairness claims and unclassified blocking calls;
boundary quiescence, starvation, priority differences, and exhausted foreign
worker capacity. P090 closes only with policy disclosure and classified
observability, not a universal liveness theorem.

## Item 091 — Distribution (G091)

**Dependencies and scope:** P084–P087/G088/P090, C025/C028/C067,
G095/G096/P099, P116/P128/P130/P131. The local C010 handle stays local until an
explicit remote boundary is admitted.

| Decision | Four explored alternatives | Selected recommendation and research basis |
| --- | --- | --- |
| CP-091-1 | A: Introduce an explicit typed transport boundary with opaque remote identity, portable with adapter cost. B: Treat every local Process handle as transparently remote, convenient but hides failure. C: Expose raw node/PID terms, familiar but leaks host representation. D: Permanently exclude distribution, simple but fails the intended operational scope. | **A, recommended and agent-selected.** [Local process limits](../60-specification/formal-semantic-kernel/actors-messages-and-failures.md#deliberately-absent-process-facilities) and [unsafe boundary routing](catena-dynamic-and-unsafe-boundaries.md) require explicit admission. |
| CP-091-2 | A: Use versioned typed codecs with bounded decoding and compatibility checks, robust with schema work. B: Serialize arbitrary BEAM terms, easy but unsafe and representation-dependent. C: Serialize closures/capabilities, convenient but violates erasure and authority. D: Infer schema from runtime values, flexible but nondeterministic compatibility. | **A, recommended and agent-selected.** [API/ABI compatibility](../60-specification/api-and-abi-compatibility/README.md) excludes an implicit stable BEAM ABI and requires semantic identity. |
| CP-091-3 | A: Report connection loss and delivery uncertainty explicitly and make retry/deduplication application-owned, honest with protocol effort. B: Promise exactly-once execution, attractive but requires unprovided distributed transactions. C: Retry invisibly forever, convenient but duplicates effects and hangs. D: Silently treat partitions as dead-target local discard, simple but conceals remote uncertainty. | **A, recommended and agent-selected.** [Send's local scope](../60-specification/formal-semantic-kernel/actors-messages-and-failures.md#send) does not justify remote delivery claims; P087 owns correlated application semantics. |
| CP-091-4 | A: Require authenticated encrypted transport and explicit node/service authorization, deployable with key lifecycle work. B: Trust network location, easy but weak. C: Embed shared secrets in artifacts, convenient but leaks credentials. D: Treat transport authentication as application typing, elegant but conflates identity and payload validity. | **A, recommended and agent-selected.** [No ambient authority](catena-top-level-effects.md) supports explicit transport capability provisioning; exact security design requires primary-source research and P130/P131 review. |
| CP-091-5 | A: Model partitions, reconnects, and version skew before real-node tests, reproducible with simulator work. B: Test only healthy nodes, cheap but misses defining failures. C: Use randomized network stress alone, broad but difficult to reproduce. D: Infer correctness from OTP transport reuse, quick but bypasses Catena's typed boundary. | **A, recommended and agent-selected.** [Actor kernel method](../60-specification/formal-semantic-kernel/actors-messages-and-failures.md#global-configuration) supplies a model-first pattern, not a distributed theorem. |
| CP-091-6 | A: Start with explicit typed application framing over an authenticated TLS socket adapter, bounded ingress with codec work. B: Treat transparent native distribution as the Catena protocol, convenient but imports host term and failure behavior. C: Use plaintext trusted-network transport, easy but insufficient authentication. D: Require an external broker, robust infrastructure but an unnecessary universal dependency. | **A, recommended and agent-selected.** [Foreign-boundary routing](catena-dynamic-and-unsafe-boundaries.md) favors checking before values enter Catena; the TLS adapter and exact framing require primary-source review and bounded implementation tests, not new language vocabulary. |
| CP-091-7 | A: Use deterministic schema-generated encodings for closed sendable data with explicit exact numeric representations and length/depth bounds, safe with codec generation. B: Encode arbitrary runtime terms, convenient but admits unsafe values. C: Guess schemas from examples, easy but incomplete. D: Use opaque serialized closures and pointers, powerful but nonportable and authority-leaking. | **A, recommended and agent-selected.** [Nominal data and sendability](../60-specification/formal-semantic-kernel/actors-messages-and-failures.md#send) provide the admitted value domain; the wire format is a separately versioned protocol artifact, not an assumed stable BEAM ABI. |

**Implementation:** (1) Research pinned OTP distribution/transport/security
and serialization behavior from primary documentation; (2) write normative
identity, codec, authentication, failure, and compatibility contracts without
new surface names; (3) implement a bounded transport-state reference model;
(4) add typed codec/admission modules in the sibling beside the existing
kernel/interface boundaries, keeping raw host values behind G095/G096;
(5) add deployment capability/configuration validation; (6) execute multi-node
healthy, skewed, partitioned, and reconnecting fixtures and retain trace seeds;
(7) integrate package/provenance checks. **Evidence/gate:** positive typed
cross-node exchange and authenticated reconnect; negative invalid schema,
malformed payload, unauthorized peer, leaked capability, duplicate retry and
unsupported version; boundary disconnect before/after remote enqueue exposes
only the documented uncertainty. G091 cannot close from localhost messaging
alone or from a claim of exactly-once delivery without independent evidence.

## Item 092 — Hot code upgrade (G092)

**Dependencies and scope:** C025/C028/C077/C078, P084/G080/G088/G089,
G091, P094/P099/P116/P128/P130. Finish local lifecycle/compatibility rules
before distributing upgrade coordination.

| Decision | Four explored alternatives | Selected recommendation and research basis |
| --- | --- | --- |
| CP-092-1 | A: Start with explicit quiescent upgrade points and typed state migration, auditable with pauses. B: Replace arbitrary live frames, seamless-looking but unsafe. C: Restart everything without state migration, simple but insufficient for hot upgrade. D: Infer migration from field names, convenient but semantically ambiguous. | **A, recommended and agent-selected.** [Compatibility authority](../60-specification/api-and-abi-compatibility/README.md) and [nominal abstraction](catena-aliases-and-newtypes.md) require declared mappings between state identities. |
| CP-092-2 | A: Execute pure checked migration with explicit step/memory bounds and abort upgrade on noncompletion, predictable with a bounded failure outcome. B: Allow arbitrary I/O migration, powerful but hard to roll back. C: Permit migration to reuse live resumptions, efficient but violates scope. D: Trust host record conversion, quick but loses Catena type guarantees. | **A, recommended and agent-selected.** [Compile-time evaluation discipline](../60-specification/compile-time-evaluation/README.md) and [pure-total law limits](../60-specification/traits-and-categorical-operations/laws-derivation-and-testing.md#law-domain) motivate an explicitly bounded transformation, not a claim that arbitrary migration terminates or a new totality type system. Migration runs at the controlled runtime upgrade boundary, not as arbitrary compiler-time user evaluation. |
| CP-092-3 | A: State old/new code coexistence, draining, and incompatibility rejection explicitly, robust with version tracking. B: Assume every closure upgrades automatically, convenient but false abstraction. C: Keep old versions indefinitely, safe for frames but unbounded resources. D: Force-purge old code immediately, simple but can kill work unexpectedly. | **A, recommended and agent-selected.** [Process and runtime boundaries](../60-specification/formal-semantic-kernel/actors-messages-and-failures.md#deliberately-absent-process-facilities) leave coexistence unpromised; exact OTP mapping must be researched and witnessed. |
| CP-092-4 | A: Require a staged validation, migration, activation, and rollback contract with immutable evidence, reviewable with orchestration cost. B: Deploy then validate, fast but exposes bad state. C: Promise rollback of external effects, reassuring but generally unsupported. D: Use mutable latest-version tags as evidence, convenient but unreproducible. | **A, recommended and agent-selected.** [Governance provenance](../60-specification/README.md) and C028 compatibility require exact identities; rollback applies only to explicitly reversible state transitions. |
| CP-092-5 | A: Refuse upgrades with live incompatible capabilities or unfinished affine control, safe with drain/restart fallback. B: Rewrite capability identities, automatic but breaks lexical selection. C: Serialize resumptions for migration, powerful but prohibited. D: Ignore capability changes if value layout matches, cheap but semantically unsafe. | **A, recommended and agent-selected.** [Capability scope](../60-specification/effects-and-handlers/capabilities-rows-and-selection.md#scope-and-abstraction) and [affine control](../60-specification/effects-and-handlers/deep-handlers-and-affine-resumptions.md#affine-resumption-form) constrain migration independently of representation. |
| CP-092-6 | A: Allow one active and one draining version per upgrade unit, reject another activation until old users drain, bounded with an upgrade pause. B: Retain unlimited versions, flexible but unbounded. C: Purge old code immediately, simple but kills valid work. D: Rewrite existing closures to new code, seamless-looking but changes captured meaning. | **A, recommended and agent-selected.** [Resource and compatibility constraints](../60-specification/api-and-abi-compatibility/README.md) require an explicit coexistence envelope; its OTP realizability must be verified before promotion. |
| CP-092-7 | A: Keep immutable pre-migration state until activation commits, restore it on precommit failure, and require explicit reverse migration after commit, precise with snapshot cost. B: Promise automatic rollback of all effects, comforting but unsupported. C: Destroy old state before validation, efficient but irreversible. D: Rerun old initialization as rollback, simple but may lose state and repeat effects. | **A, recommended and agent-selected.** [Failure/authority separation](catena-exception-boundary.md) and [compatibility rules](../60-specification/api-and-abi-compatibility/README.md) make rollback a defined state transition, never an implicit reversal of external history. |

**Implementation:** (1) Research pinned OTP code loading, old-code limits,
supervisor release handling, and state migration from primary sources;
(2) specify an internal upgrade descriptor containing exact old/new interface,
state-schema and artifact identities, migration evidence, drain conditions,
and rollback limits; require one active/one draining version and retain the
pre-migration snapshot until activation commits; (3) implement reference transitions for preflight,
quiescence, migration, activation, and failure; (4) add typed migration
checking and package compatibility validation using
`lib/catena/package/compat.ex`, `lib/catena/interface.ex`, and governance
machinery; (5) implement the admitted OTP adapter; (6) run old/new coexistence,
failed migration, rollback, and staged distributed fixtures.
**Evidence/gate:** positive compatible migration and preserved message/state
observations; negative wrong schema/digest, escaping capability, nonterminating
migration, unsupported active frame, and unvalidated artifact; boundary crash
between migration and activation, new message during drain, rollback after
activation, and mixed-node versions each have an explicit outcome. G092 closes
only when migration, coexistence, rollback limits, and evidence governance are
all implemented for the admitted upgrade profile.

## Completion discipline and research connections

The selected program treats categorical composition as a constraint on
interfaces and reasoning, not as permission to reorder work or ignore
resource lifetime. The [category-theory synthesis](category-theory-for-programming.md),
[combinator synthesis](combinators-for-algebraic-data-and-categorical-programming.md),
[type-system synthesis](catena-greenfield-type-system.md),
[effect synthesis](algebraic-effects-and-handlers.md), and
[comprehension synthesis](list-comprehensions.md) are the current research
basis. Normative chapters win over older exploratory choices; in particular,
existing operation direction, trait names, effect roles, and exclusion gates
are preserved without choosing fresh vocabulary.

The new runtime proposals are deliberately distinguished from established
research results. The current corpus supports isolation, lexical capabilities,
affine deep control, explicit order, and bounded evidence. It does not already
supply a full cleanup protocol, session-type theorem, secure distribution
protocol, or hot-upgrade theorem. Those slices begin with the primary-source
and executable-model work specified above, and any evidence that falsifies a
selected proposal triggers another recorded four-alternative decision before
implementation proceeds.

For each execution slice: pin both repository revisions and toolchain; write
or amend the applicable rule and its obligation identities; implement in the
sibling; run targeted positive/negative/boundary and applicable cross-target
tests; run required broader compiler checks; record commands/results in a
journal; update the registry, checklist, inquiry, maps, and directory indexes
atomically; validate the archive and review the diff. Keep incomplete facets
open. No checkbox closes because the plan has enough rows, a tag exists, a
string looks right, or one target returns the expected value.
