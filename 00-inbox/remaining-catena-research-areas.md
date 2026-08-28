---
title: "Remaining Catena Research Areas"
kind: note
created: "2026-08-17"
maturity: seed
tags:
  - catena
  - language-design
  - specification
aliases:
  - "Catena research agenda"
  - "Open Catena research programs"
---

# Remaining Catena Research Areas

> Temporary planning synthesis. This document is non-normative and describes
> the archive at its current revision. It groups existing gaps into research
> programs; it does not reopen completed semantic slices or commit a future
> Catena revision to any feature.

## Purpose and reading rule

Catena has a coherent normative spine, but it is not yet a complete language,
toolchain, runtime contract, or ecosystem. The
[language-specification completeness checklist](language-specification-completeness-checklist.md)
tracks individual obligations with stable `C`, `G`, `P`, and `D` identifiers.
This document answers a different question: **which larger research programs
remain, how do they extend the current corpus, and what would completing them
bring to the design?**

The archive has four different kinds of evidence, which this agenda keeps
separate:

- [normative specifications](../60-specification/README.md) define current
  conformance obligations;
- [research notes](../20-notes/README.md) explain rationale, synthesis, and
  possible extensions;
- [inquiries](../40-inquiries/README.md) record whether a question is open or
  resolved and what would settle it; and
- [journal records](../50-journal/README.md) preserve executable, historical,
  and promotion evidence.

A normative slice can be complete while a wider research program remains
open. For example, 0.1.5 completely defines its bounded first-order handler
language, while resource cleanup, cancellation, higher-order effect scopes,
performance, and broader usability remain research questions. “Remaining” in
this document therefore means work needed for a larger usable language or a
stronger future revision, not a defect in an already bounded normative claim.

## Existing baseline

The following foundation should be treated as the starting point for new
research rather than repeatedly redesigned:

| Boundary | Current corpus result | Role in future work |
| --- | --- | --- |
| 0.1.1 / C001 | [Type System](../60-specification/type-system/README.md): principal rank-1 inference, separate row/trait/effect solving, annotation-directed advanced checking, and typed-core elaboration | New surface and runtime features must preserve or explicitly narrow this guarantee matrix. |
| 0.1.2 / C002 | [Data and Patterns](../60-specification/data-and-patterns/README.md): nominal ADTs, typed patterns, coverage, GADT boundaries, abstraction, derivation, and layout independence | Collection, module, comprehension, and foreign-data work must reuse its constructor, visibility, and refutability rules. |
| 0.1.3 / C003 | [Clause Conditions](../60-specification/clause-conditions/README.md): a total checked condition fragment, ordered guard trees, certified facts, dual lowering, and a bounded receive harness | Richer conditions and public receive must extend this model without turning faults into fallthrough. |
| 0.1.4 / C004 | [Traits and Categorical Operations](../60-specification/traits-and-categorical-operations/README.md): behavior-first trait ABI, coherence, law evidence, derivation, operational contracts, specialization, and erasure | Libraries and optimizers need to validate the usefulness and cost of this semantic hierarchy rather than invent a competing one. |
| 0.1.5 / C005 | [Effects and Handlers](../60-specification/effects-and-handlers/README.md): nominal requests, lexical capabilities, identity-aware rows, deep handlers, affine resumptions, and effect-directed CPS | Resource, failure, concurrency, and host-effect research must preserve handler identity, effect visibility, and affine control. |
| 0.1.6 / C006 | [Specifications and Governance](../60-specification/specifications-and-governance/README.md): typed claims, exact examples, evidence identity, offline authority, append-only lifecycle, artifact binding, and erasure | Stronger checking methods and distributed governance must remain explicit about evidence strength, trust, scope, and runtime cost. |
| 0.1.7 / C008 | [Editions and Feature Lifecycle](../60-specification/editions-and-feature-lifecycle/README.md): package-local editions, exact retained revisions, previews, compatibility records, migration descriptions, and version-bound artifacts | Every new feature needs an applicability, lifecycle, migration, and historical-retention story. |
| C007, C009, C011, C012 | [Specification authority](../SPECIFICATION-AUTHORITY.md), [conformance vocabulary](../CONFORMANCE-VOCABULARY.md), [rule-to-test traceability](../10-maps/conformance-traceability.md), and [implementation limits](../IMPLEMENTATION-LIMITS.md) | Future chapters inherit one authority model, no undefined behavior, explicit variability, permanent obligation identifiers, portable minima, and machine-readable finite-resource disclosure. |
| 0.1.8 / C010 | [Formal Semantic Kernel](../60-specification/formal-semantic-kernel/README.md): one strict small-step calculus integrating bounded data, rows, traits, handlers, traps, and typed local actors with BEAM evidence | It is the executable integration baseline, not the final surface language, OTP model, or whole-language theorem. |

## Research-program overview

| Priority relationship | Research program | Corpus state | Main design value |
| --- | --- | --- | --- |
| Foundational | Approachable source language | Semantic inputs exist; public grammar and many names remain open | Makes Catena writable, teachable, parsable, and toolable without weakening its semantics. |
| Foundational | Complete expression and failure semantics | Strict bounded kernel exists; general source dynamics are incomplete | Gives every ordinary program one predictable evaluation and failure model. |
| Foundational | Names, modules, packages, and application boundaries | Public semantic interfaces and revision selection exist; source organization does not | Enables separate compilation, dependency management, executable entry points, and stable APIs. |
| Foundational | Integrated type and elaboration guarantees | Strong component contracts exist; whole-language proof and edge policies remain open | Preserves principality, coherence, and soundness as the language grows. |
| Language layer | Practical data, collections, and representation | Nominal data and bounded structural rows exist; the general data model does not | Makes Catena suitable for ordinary data processing and stable module/foreign boundaries. |
| Language layer | Comprehensions and iteration | Detailed synthesis and open inquiry exist; no normative slice exists | Adds concise iteration while retaining explicit pattern failure, effects, order, and cost. |
| Library layer | Traits, combinators, and standard library | Trait semantics are normative; the useful library and empirical API remain open | Turns mathematical structure into reusable, discoverable programming tools. |
| Runtime layer | Effects, exceptions, cleanup, and resource scopes | First-order handlers are normative; lifetime semantics are absent | Makes I/O and control safe in the presence of abort, cancellation, and failure. |
| Language/runtime seam | Conditions and selective receive | Bounded condition semantics and receive harness exist | Extends safe routing and matching to realistic predicates and mailboxes. |
| Runtime layer | Processes, structured concurrency, and OTP behavior | Typed local actors exist in the kernel; OTP-scale behavior is deliberately excluded | Delivers the fault-tolerance and concurrency part of Catena's stated identity. |
| Platform layer | BEAM and Erlang interoperability | Fixed bounded lowering paths exist; the general foreign boundary does not | Lets Catena participate safely in the BEAM ecosystem. |
| Assurance layer | Stronger specifications and long-lived governance | A bounded offline governance spine is normative | Adds graduated runtime, model, proof, and distributed evidence without conflating their meanings. |
| Experience layer | Diagnostics, tools, migration, and usability | Slice-specific diagnostics and migration descriptions exist | Makes the guarantees understandable and the language practical to develop with. |
| Trust layer | Security, reproducibility, and operational limits | Signed artifacts and deterministic failure policy exist; system threat model is incomplete | Makes conformance and governance credible under real resource and supply-chain threats. |
| Validation layer | Whole-language metatheory, optimization, and performance | C010 and C011 provide bounded integration and traceability | Demonstrates that independently sound slices compose and can be implemented efficiently. |
| Lifecycle layer | Compatibility, release readiness, and self-hosting | Exact revision retention exists; ecosystem maturity criteria do not | Turns a prototype line into an evolvable, independently implementable language. |

## 1. Approachable source language

**Relation to the current corpus.** Catena currently has exact semantic inputs:
the earlier normative slices use versioned JSON forms, 0.1.8 uses a canonical
S-expression kernel, and C013 now defines a strict 0.1.9 UTF-8 source-text
envelope with logical newlines and original-byte scalar spans. Those exact
forms make conformance reproducible. C014 adds pinned Unicode 17
standalone identifiers, NFC, security profiles, keyword escaping,
qualification, and confusable warnings. C015 adds non-semantic indentation,
narrow layout whitespace, newline/semicolon separators, and an abstract
token-capability continuation engine. C016 adds nested comments,
comment-internal layout preservation, forward documentation attachment,
CommonMark, and explicit doctest metadata. C017 adds exact atomic Boolean,
numeric, text, character, and byte spelling, decoding, provenance, raw-line
ownership, and active literal limits, but
the [Catena Language Overview](../language-overview.md) explicitly says they do
not replace a future approachable frontend. The
[approachable-vocabulary synthesis](../20-notes/approachable-language-vocabulary.md)
proposes a behavior-first public language, and the associated
[vocabulary inquiry](../40-inquiries/how-should-catena-expose-mathematical-structure-without-mathematical-jargon.md)
remains open. C004 has selected one behavior-first trait ABI, while clause,
effect, specification, governance, and comprehension punctuation remain partly
provisional. C013 closes byte decoding, C014 closes standalone names, C015
closes layout classification, C016 closes comments, C017 closes atomic
literals, C018 closes numeric literal meaning, C019 closes operators,
punctuation, and the whole-source token stream, C020 closes the
file-to-module relationship, C021 closes namespaces and shadowing, and
C022 closes imports and exports. Checklist item
`P109` describes the remaining atomic gap of this program.

**Remaining research.** This program must define:

- integration of C014's fixed identifier rules and C017's literal boundaries
  into real maximal whole-file tokenization;
- integration of C016 documentation metadata with the complete declaration
  grammar, generated documentation, formatting, and file-to-module rules;
- declaration and application grammar over the fixed C019 token stream,
  C020 file frame, and C022 import/export events, plus a new explicitly
  prefixed future interpolation form if justified;
- concrete source forms for functions, bindings, data, patterns, conditions,
  traits, effects, handlers, specifications, governance, and packages;
- a lossless concrete syntax tree, source-to-core mapping, and version-aware
  formatter/migration representation; and
- prediction, task-selection, and diagnostic-repair studies for risky public
  terms and syntax, especially the categorical capabilities and effect model.

**What it would bring.** A completed frontend would make the existing semantic
language accessible to programmers without asking them to write compiler
protocols or learn the theory ledger. It would also establish stable input for
formatters, editors, documentation tools, source migrations, code review, and
future compatibility analysis. Most importantly, it would test whether the
archive's promise of mathematical rigor without prerequisite jargon is
actually achievable.

**Completion evidence.** The result needs a versioned grammar and lexical
contract, parser and formatter round trips, negative syntax and normalization
cases, preserved source locations through typed-core elaboration, migration
tests across syntax changes, and programmer studies showing that the chosen
forms predict the intended semantics.

## 2. Complete expression, evaluation, and failure semantics

**Relation to the current corpus.** The formal kernel fixes strict
left-to-right dynamics for a bounded calculus. C002 and C003 define precise
ordering for constructor fields, scrutinees, patterns, conditions, and clause
commitment; C005 fixes handler order and resumption behavior. The completeness
audit nevertheless marks general values, calls, sequencing, branching,
recursion, equality, failure, resource observability, and compile-time
evaluation as `P029`–`G038`.

**Remaining research.** Catena still needs a whole-source-language account of:

- ~~which forms are values~~ — closed by C029: the closed ten-form value
  grammar with Float, uniform first-classness, and the strictness
  invariant with its edition-record gate; when each subexpression is
  evaluated remains P030;
- ~~when each subexpression is evaluated~~ — closed by C030: the closed
  ordered-forms table with typed-core completions, the future-form
  entry rule, and trace-observable order with reference/BEAM
  agreement;
- ~~nonrecursive and recursive bindings, mutual recursion, unused effectful
  values, and sequencing~~ — closed by C031: non-recursive local lets,
  definitions-only recursion with SCC mutual recursion, the sequencing
  idiom, and deny-able `BS001`;
- ~~currying or fixed arity, partial application, closure capture, named and
  anonymous functions, callbacks, and proper tail calls~~ — closed by
  C032: semantic-unary currying, free partial application, lexical
  immutable capture, let-bound local functions, and the elevated
  proper-tail-call guarantee; calling conventions remain G094;
- ~~conditionals and other branch forms in relation to exhaustive matches~~ —
  closed by C033: match is the single branch form, the conditional
  sugar promise fixes `if` desugaring, and statement forms are
  declared absent;
- ~~primitive equality and ordering, including floats, strings, binaries,
  process values, and mixed numeric types~~ — closed by C035: the
  closed comparable set with bit-exact floats, structural composites,
  and monomorphic comparison; strings/binaries enter with G040,
  process handles never compare;
- ~~typed domain failure, `Option`/`Result`, explicit trap or panic, arithmetic
  faults, failed assertions, foreign exceptions, process exit, and VM
  termination as distinct outcomes~~ — closed by C036: the single
  `trap(reason)` outcome with kinded reasons and the per-producer
  gate; library contents remain G105, foreign calls G095/G096,
  process death G084;
- allocation, sharing, object identity, garbage collection, stack use, and
  finalization to the extent programs can observe them; and
- whether constants, derivations, macros, or other compile-time computations
  execute code, and under which purity, totality, and resource limits.

**What it would bring.** This work would turn the collection of exact feature
slices into one predictable language of ordinary expressions. It would give
optimizers, debuggers, effect analyses, resource scopes, and foreign calls a
shared definition of order and failure instead of forcing each feature to
invent one locally.

**Completion evidence.** A unified dynamic semantics should cover every
surface expression, distinguish all terminal and suspended states, preserve
source order in a reference evaluator, and agree with BEAM traces on generated
programs including failure and tail-call cases.

## 3. Names, modules, packages, and application boundaries

**Relation to the current corpus.** C001 requires public signatures; C002
defines transparent versus abstract datatype exposure; C004 and C005 carry
trait and capability identity through module interfaces; C008 defines
package-local edition and revision selection. These are semantic interface
pieces, not yet a complete source module and package system. The former
obligations `G021`–`G028` are now closed: C021 through C028 complete the
names, modules, packages, and separate-compilation program.

**Remaining research.** The archive needs decisions for:

- distinct or shared namespaces for values, types, constructors, traits,
  effects, specifications, capabilities, and modules;
- shadowing, qualification, renaming, re-export, wildcard imports, unused
  imports, and visibility defaults;
- ~~module cycles, recursive modules, initialization, inference across
  strongly connected components, and separate-compilation cache
  boundaries~~ — closed by C024: SCC admission with signature regimes,
  joint digests, definition-only initialization, and component cache
  units;
- ~~opaque types, construction versus matching authority, and any
  stable-layout opt-in~~ — closed by C023: the binary vocabulary is
  complete, no stable layout exists, and future ABI contracts belong to
  the compatibility program;
- ~~package identity, manifests, dependency resolution, lockfiles,
  integrity, conflicting versions, and offline operation~~ — closed by
  C025: manifest dependencies, SemVer operators, single-version
  resolution, `catena.lock`, and registry-neutral bundle digests with
  the Hex transport profile; fetch tooling and signing remain G121/G130;
- ~~prelude contents and opt-out or shadowing policy~~ — closed by
  C026: opt-in manifest selection at ordinary precedence with
  zero-implicit-names guarantee; contents remain G101;
- ~~executable and library roots, entry points, startup, shutdown, and
  permitted top-level effects~~ — closed by C027: named zero-argument
  effect-closed entries with derived libraries and invocation-only,
  return-is-shutdown launch; supervision and tooling remain
  G084/G089/G121; and
- ~~source, type, behavior, artifact, BEAM ABI, and hot-upgrade
  compatibility~~ — closed by C028 for API/ABI: strict interface diff
  matrix with minor-as-breaking under 0.x, declared behavior and ABI
  absences; migration, registry, and hot-upgrade work remains
  G116/G130/G092.

**What it would bring.** This program would make Catena a language for
multi-file applications and libraries rather than isolated semantic modules.
It would enable deterministic builds, dependency reuse, API evolution,
separate compilation, and meaningful package publication while preserving the
exact-revision model.

**Completion evidence.** A multi-package conformance corpus should exercise
qualification, abstraction, cycles or their rejection, cross-revision
interfaces, public previews, dependency conflicts, entry-point effects, and
stable rebuilds without re-inferring unaffected packages.

## 4. Integrated type and elaboration guarantees

**Relation to the current corpus.** The
[greenfield type-system synthesis](../20-notes/catena-greenfield-type-system.md)
and normative 0.1.1 establish a strong layered contract. C010 demonstrates one
bounded integration of functions, rows, traits, handlers, and actors. The
[type-system inquiry](../40-inquiries/what-should-a-greenfield-catena-type-system-guarantee.md)
remains open because component proofs, the complete handler calculus, the
whole-language theorem, and annotation usability are not yet complete.
Checklist items `G061`, `G062`, `G066`, `G067`, `D140`, and `P132` own several
visible edges.

**Remaining research.** Work includes:

- numeric literal constraints, defaulting or its absence, coercions, and the
  relationship between primitive and trait-based operations;
- aliases, opaque types, newtypes, representation identity, coercion, and
  deriving behavior;
- whether field, method, constructor, operator, or literal resolution may
  depend on inferred types without making results order-dependent;
- a clearly visible dynamic or unsafe boundary, or an explicit decision that
  the initial language has none;
- integrated preservation, progress, principality, coherence, row-unifier
  most-generality, evidence-erasure, and handler-abstraction results;
- the exact interaction among GADT equalities, effect rows, trait evidence,
  pattern coverage, specifications, and actor messages; and
- representative programs testing whether signatures and annotations appear
  at understandable boundaries rather than becoming pervasive.

**What it would bring.** Completing this program would justify Catena's most
important static promise at whole-language scale: ordinary code gets a
principal inferred type, while richer code crosses explicit and local checking
boundaries. It would also stop future conveniences from silently introducing
incoherence, solver-order dependence, or unsound generalization.

**Completion evidence.** The strongest result would be mechanized metatheory
for the integrated core plus an independent typed-core verifier. At minimum,
the archive needs explicit theorem scopes, bounded executable models,
order-independence and most-generality tests, negative counterexample corpora,
and usability evidence for annotation-heavy examples.

## 5. Practical data, collections, patterns, and representation

**Relation to the current corpus.** C002 gives nominal data a mature semantic
contract, while C010 gives structural records and variants executable term
forms under a fixed kernel representation. C004 defines selected structural
derivations. The initial pattern grammar deliberately excludes list,
structural-record, row-variant, binary, range, and programmable patterns.
Checklist items `G040`–`D046` and `P093` track the remaining general data model.

**Remaining research.** Catena needs to decide:

- which primitive and built-in types exist beyond C017's fixed atomic spelling:
  unit, numeric runtime types, text/character/byte semantics, tuples, lists,
  maps, sets, process handles, references, and functions;
- structural record and variant source operations, uniqueness, row-polymorphic
  behavior, effect order, and public representation guarantees;
- persistent collection construction and update, duplicate keys, ordering,
  equality, bounds failure, and complexity promises;
- which pattern contexts require exhaustiveness and which explicitly permit
  filtering or selective failure;
- whether later list, record, variant, binary, range, view, synonym, or active
  patterns justify their effect, totality, coverage, cost, and abstraction
  obligations; and
- the boundary between opaque Catena representation, stable native layout,
  serialized form, and foreign inspection.

**What it would bring.** This would provide the data vocabulary needed by
real applications, libraries, protocol adapters, and the compiler itself. It
would also let performance and compatibility claims refer to stable collection
and representation contracts rather than incidental BEAM layouts.

**Completion evidence.** Each admitted type needs construction, observation,
equality, ordering if any, failure, effect order, complexity, pattern, module,
serialization, and BEAM-lowering rules with reference and differential tests.
Excluded types or patterns should be named explicitly so absence cannot become
implementation-defined behavior.

## 6. Comprehensions, iteration, and streaming boundaries

**Relation to the current corpus.** The
[list-comprehension synthesis](../20-notes/list-comprehensions.md) proposes an
eager ordered list-to-list expression with total generators, explicitly
filtering generators, Boolean filters, exhaustive local bindings, and visible
effects. The
[list-comprehension inquiry](../40-inquiries/how-should-catena-specify-list-comprehensions.md)
and checklist items `P047`–`D059` remain open. No current normative revision
contains this surface feature.

**Remaining research.** The initial question requires:

- comprehension syntax and a reliably understood marker for filtering
  patterns;
- exact type, scope, rebinding, refutability, and effect-row rules;
- left-to-right depth-first source evaluation, result order, source
  multiplicity, failure timing, and short-circuit semantics;
- a typed qualifier-tree elaboration and fused tail-recursive BEAM worker that
  preserves source spans and effect traces;
- stack, allocation, and Cartesian-cost measurements; and
- a deliberate initial boundary for iterators, lazy streams, infinite inputs,
  zip, ranges, binaries, maps, sets, builders, reduction, effect-only loops,
  grouping, ordering, and parallel traversal.

**What it would bring.** A resolved list comprehension would make common data
pipelines concise without pretending that generic `map` is effectful or that
pattern mismatch is harmless. The later iterator and stream work would add
scalable producer/consumer composition, but only after resource lifetime,
cancellation, and backpressure have explicit contracts.

**Completion evidence.** Resolution requires grammar and comprehension tests,
formal qualifier-tree typing and dynamics, coverage diagnostics, reference and
BEAM equivalence for values/failures/effects, stack-safe linear-output
lowering, source-level debugging, and an explicit list of excluded neighboring
forms.

## 7. Traits, combinators, derivation, and the standard library

**Relation to the current corpus.** C004 normatively fixes the initial trait
hierarchy, behavior-first ABI, coherence, evidence categories, selected
derivations, operational order, specialization, and erasure. That resolves the
bounded language mechanism. It does not by itself establish that the complete
hierarchy is discoverable, that the derived library is sufficient, or that
advanced combinator families are worthwhile. The
[category-theory synthesis](../20-notes/category-theory-for-programming.md),
[combinator synthesis](../20-notes/combinators-for-algebraic-data-and-categorical-programming.md),
and [open combinator inquiry](../40-inquiries/which-combinators-should-catena-provide-and-derive.md)
own this wider program. Standard-library gaps are `G101`–`G108`.

**Remaining research.** This program should produce:

- a minimal prelude and reference implementation of the normative trait
  dictionaries and all derived operations;
- exact extensional and operational contracts for mapping, application,
  chaining, traversal, reduction, early termination, composition, and context
  operations;
- conditional ADT derivation with positivity, variance, regularity, field
  order, visibility, law tests, and useful refusal diagnostics;
- iterator or `fold_while` contracts for strict, stack-safe, early-terminating
  consumption;
- concrete `Option`, `Result`, validation, list, map, set, text, numeric, and
  environmental-effect APIs;
- discoverability studies for qualified methods, pipelines, capability names,
  and any operators;
- parser, optic, recursion-scheme, modular-syntax, selective, dataflow, and
  explicit-computation prototypes with domain-specific cost and failure rules;
  and
- a policy for which laws are merely promised, tested, derived, proved, or
  trusted strongly enough to justify an optimizer transformation.

**What it would bring.** This work would turn the categorical foundation from
a coherent type-level vocabulary into useful everyday programming
infrastructure. It would clarify which abstractions belong in the prelude,
which should be generated per datatype, and which should remain focused
packages or compiler experiments.

**Completion evidence.** The archive needs a reference library checked through
the ordinary typed core, operational contract matrices, derivation and law
corpora, representative applications, compiler and runtime measurements, and
programmer evidence that users select the correct operation without needing
the formal-name ledger.

## 8. Effects, exceptions, cleanup, and resource scopes

**Relation to the current corpus.** Normative 0.1.5 closes the bounded
first-order effect question: requests have nominal identity, handler selection
is lexical, handlers are deep and open, and resumptions are affine and
non-escaping. C010 integrates a smaller selected handler surface with local
actors. The
[effect synthesis](../20-notes/algebraic-effects-and-handlers.md) and
[effect inquiry](../40-inquiries/which-algebraic-effect-semantics-should-catena-adopt.md)
remain open at the wider language level. Checklist items `G080`–`D083` capture
the main missing runtime semantics.

**Remaining research.** Catena must still define:

- acquisition and guaranteed release across normal return, handler abort,
  explicit trap or panic, process exit, cancellation, and foreign unwinding;
- whether domain errors, exceptions, panics, process exits, and foreign
  failures use one mechanism or several visibly distinct mechanisms;
- the set of top-level host effects and how application entry points receive
  their capabilities;
- structured scopes for tasks, files, sockets, locks, transactions, timeouts,
  and cancellation;
- the higher-order effect or dedicated runtime model needed by scoped
  operations such as `bracket`, rather than encoding all scopes as ordinary
  resumable requests;
- production handler lowering, stack traces, FFI interaction, effectful
  closures, and measured cost; and
- separate future cases for shallow handlers, stored or multi-shot
  continuations, nondeterminism, generators, and async control.

**What it would bring.** This is the bridge from an elegant effect calculus to
safe real-world I/O and control flow. It would let programmers know which
cleanup runs, which failures can be handled, how cancellation propagates, and
whether a captured continuation may retain or duplicate a resource.

**Completion evidence.** The archive needs an integrated scope-and-handler
calculus, cleanup and cancellation traces in the reference evaluator,
differential BEAM tests across every exit path, higher-order capture cases,
stack and FFI observations, performance measurements, and usability studies
for capability and residual-effect diagnostics.

## 9. Conditions, verified predicates, and selective receive

**Relation to the current corpus.** C003 already defines a strong bounded
answer: Boolean-only checked conditions, total acyclic predicates, ordered
fallthrough, difference-constraint facts, native and ordinary lowering, and a
native receive harness. The
[clause-guard synthesis](../20-notes/clause-guards.md) and
[guard inquiry](../40-inquiries/how-should-catena-design-clause-guards.md)
remain open only for the broader predicate, usability, performance, trait, and
public receive questions.

**Remaining research.** This extension program includes:

- approachable source syntax and diagnostics explaining why a condition is
  unsafe or why guarded clauses remain structurally non-exhaustive;
- evidence-backed trait methods inside conditions;
- recursive total predicates and the smallest usable termination or
  certificate discipline;
- measurements for shared guard trees, native versus ordinary lowering, and
  adversarial coverage facts;
- the possible value of pattern guards or handler-clause conditions;
- public receive syntax, message typing, timeout and cancellation behavior,
  mailbox scan order, preservation of rejected messages, starvation, and cost;
  and
- interaction of condition facts with GADT refinements, erased proof evidence,
  and later numeric types.

**What it would bring.** The result would extend Catena's safe match-selection
model to common validation and actor-routing code without admitting arbitrary
effects, divergence, or exception-to-false behavior. It would also make
selective receive a public typed feature rather than a backend conformance
harness.

**Completion evidence.** Representative validation and protocol corpora must
fit the checked fragment; accepted predicates need independently checkable
totality evidence; native and ordinary paths must agree; mailbox experiments
must confirm preservation and explain scan cost; and users must be able to
repair coverage and guard-safety diagnostics.

## 10. Processes, structured concurrency, and OTP behavior

**Relation to the current corpus.** C010 introduces the first normative actor
boundary: `Process M`, closed first-order messages, named process entries,
per-sender FIFO, oldest-matching receive, nondeterministic cross-sender
scheduling, suspension, and explicit traps. It deliberately promises no
protocol typing, fairness, deadlock freedom, links, monitors, timeouts,
cancellation, supervision, distribution, or hot upgrade. Checklist items
`G084`–`G092` own this program.

**Remaining research.** The runtime model needs to address:

- spawn authority, parent/child and peer relationships, normal completion,
  crash, mailbox disposal, links, monitors, and exit trapping;
- send results, copying or sharing, unsupported values, mailbox growth,
  backpressure, ordering, and remote delivery;
- whether typed mailbox contents are sufficient or whether protocols,
  request/reply handles, typestate, or session-like transitions earn a place;
- structured task scopes, cancellation propagation, deadlines, monotonic
  time, sleep, timer races, and cleanup;
- supervision policies, restart identity, state recovery, escalation, and the
  boundary between language syntax and ordinary OTP-compatible libraries;
- scheduler observability, fairness assumptions, priorities, reductions, and
  blocking foreign work;
- distribution, authentication, serialization, partitions, version skew, and
  delivery claims; and
- hot code upgrade, state migration, old/new code coexistence, capability and
  type compatibility, rollback, and governance evidence.

**What it would bring.** This program would deliver the BEAM fault-tolerance
half of Catena's stated identity. The current kernel proves that typed local
actors can fit the language; the remaining work would make failures,
supervision, time, cancellation, distribution, and upgrades programmable and
predictable.

**Completion evidence.** Each added feature needs global operational rules,
mailbox and lifetime invariants, bounded schedule/model exploration, OTP
differential tests, adversarial failure scenarios, explicit fairness and
resource limits, debugger-visible process traces, and protocol-evolution tests
where static protocols are claimed.

## 11. BEAM representation and Erlang interoperability

**Relation to the current corpus.** Catena is BEAM-only and normatively lowers
through supported OTP Abstract Format. C002 tests two opaque nominal-data
layouts; C004 erases specialized trait evidence; C005 lowers bounded handlers;
C006 binds erased runtime artifacts; and C010 fixes one kernel representation
on OTP 29. Those successes do not define the general Erlang or native boundary.
Checklist items `P093`–`G100` describe the missing platform contract.

**Remaining research.** Required decisions include:

- Catena-to-BEAM mappings for every primitive, collection, structural row,
  closure, capability, process, and erased artifact;
- exported names and arities, currying, closure environments, callbacks,
  proper tail calls, stack traces, and module metadata;
- how arbitrary Erlang terms enter typed Catena and which dynamic checks or
  explicit dynamic types mediate the boundary;
- foreign-call and callback syntax, declared effects, blocking behavior,
  exceptions, cancellation, ownership, and callback lifetime;
- first-class treatment of binaries, maps, PIDs, ports, references, and funs;
- NIF and port unsafety, dirty scheduler classes, resource finalization, VM
  crash exposure, capabilities, and packaging;
- supported OTP versions, feature detection, portable guards, generated
  bytecode level, and upgrade cadence; and
- source maps, inlined and generated frames, handlers, dictionaries, erased
  specifications, and foreign frames in debugging metadata.

**What it would bring.** A defined interoperation layer would let Catena use
the existing Erlang/Elixir/OTP ecosystem without allowing dynamically typed or
native behavior to puncture its guarantees invisibly. It would also make
generated BEAM artifacts debuggable and operationally supportable.

**Completion evidence.** The work needs round-trip value tests, checked and
rejected foreign terms, callback lifetime and failure tests, tail-call and
stack-trace inspection, NIF/port threat and resource cases, multi-OTP CI, and
documented representation/ABI stability classes.

## 12. Stronger specifications and long-lived governance

**Relation to the current corpus.** C006 normatively defines a bounded typed
claim graph, exact examples, compiler evidence, signed attestations, explicit
assumptions, offline authorization, lifecycle replay, artifact binding, and
complete erasure. C008 versions those artifacts; C009 supplies behavior
classes; C011 provides obligation traceability. The
[governance synthesis](../20-notes/language-integrated-specifications-and-governance.md)
and [governance inquiry](../40-inquiries/how-should-catena-integrate-specifications-and-governance-into-the-language.md)
remain open for richer assurance. Checklist items `P109` and `G116` record the
most direct specification gaps.

**Remaining research.** Later assurance layers include:

- approachable source grammar for claims, evidence, assumptions, scopes,
  policy, decisions, and transitions;
- runtime contracts and retained monitors for higher-order functions,
  handlers, messages, failures, and process boundaries, with blame and cost;
- generated properties, shrinking, replay, bounded structural models,
  temporal models, refinement, deductive proofs, and proof certificates;
- a small certificate-checking kernel and explicit trusted assumptions for
  external solvers and workers;
- semantic digests and evidence invalidation that survive irrelevant edits but
  reject meaning changes;
- schema and policy migration, archived decision replay, historical compiler
  interpretation, and long-term evidence portability;
- credential freshness, revocation services, transparency logs, federated
  roots, and cross-organization authority; and
- performance, storage, incremental checking, and user comprehension on
  representative governed projects.

**What it would bring.** This work would allow Catena projects to select
graduated assurance—from executable examples to runtime contracts, bounded
models, and checked proof certificates—without equating any one of them with
truth or authority. Long-lived governance would make signed decisions and
evidence usable beyond one offline prototype schema.

**Completion evidence.** Each evidence method needs a distinct typed envelope,
sound scope statement, reproducible checker, failure semantics, invalidation
rules, and UI wording. Governance extensions need adversarial models,
historical replay across versions, portable trust profiles, bounded resource
use, and evidence that programmers distinguish proof, testing, attestation,
approval, and promotion.

## 13. Diagnostics, tools, migration, and usability

**Relation to the current corpus.** Every normative area has structured
diagnostics, C008 defines stable edition/preview/deprecation families and
ordered migration edits, and the type-system notes require constraint
provenance. The archive does not yet define a complete cross-language
diagnostic or developer-tool contract. Checklist items `P117`–`P125` and
`G137` cover this layer.

**Remaining research.** Catena needs:

- stable diagnostic identity, primary and secondary locations, causal chains,
  inferred-type and effect presentation, constraint provenance, pattern
  witnesses, condition facts, generated-code attribution, and concrete repair;
- a canonical version-aware formatter and comment-preserving syntax tree;
- documentation attachment, cross-links, examples, doctests, hidden APIs,
  traits, effects, laws, and specification views;
- a REPL model for polymorphism, effects, declaration replacement, process
  lifetime, module loading, history, and governance;
- build and package tools with profiles, dependency fetching, code generation,
  incremental cache keys, offline operation, and reproducibility;
- unit, property, model, concurrency, and specification testing with seeds,
  shrinking, timeouts, and evidence capture;
- editor behavior for partial programs, incremental inference, completion,
  hover, rename, semantic tokens, and stable diagnostics;
- source-level debugging, tracing, profiling, crash reports, handlers,
  processes, messages, derivations, and erased declarations; and
- transactional application of migration edits with backups, rollback,
  conflict handling, source rewrites, and API refactors.

**What it would bring.** This program would make Catena's rigor usable during
normal development. Good tools are also evidence about the language design:
if errors, effects, ownership, or migrations cannot be explained at source
level, the underlying abstraction may be too implicit or too complex.

**Completion evidence.** Tool protocols need versioned machine interfaces and
end-to-end source mapping. User studies should test prediction, task
completion, and repair across types, traits, effects, conditions,
comprehensions, concurrency, and governance. Performance tests should cover
incremental editing and large projects, not only batch compilation.

## 14. Security, reproducibility, authority, and operational limits

**Relation to the current corpus.** C006 defines canonical signed artifacts,
offline trust roots, delegation, revocation, recovery, staged output, and
artifact binding. C009 prohibits undefined behavior and requires explicit
implementation-defined choices and limits. C008 binds exact revisions and
historical signature domains. The wider threat, resource, and supply-chain
model now has the completed C012 portability baseline, while the wider threat
and supply-chain model remains open under `G126`–`G131`.

**Remaining research.** The system needs to specify:

- extensions to the C012 portable-minimum registry for future source forms,
  aggregate inputs, memory accounting, cancellation, recursion, and concrete
  mailbox admission or backpressure policy;
- the complete trusted computing base across parser, static solvers, core
  verifier, proof kernel, optimizer, serializer, signer, OTP runtime, and
  foreign components;
- whether unsafe code exists, how it is scoped, which obligations it assumes,
  and how interfaces and artifacts expose it;
- reproducible-build inputs, paths, timestamps, environment, dependency
  integrity, generated files, toolchain identity, and byte-for-byte or semantic
  equivalence expectations;
- compiler and runtime exhaustion, denial-of-service behavior, admission
  controls, and transactional failure;
- package signing, provenance, yanks, compromised releases, native
  dependencies, and governance evidence; and
- how secrets and ambient VM authority enter programs without being hidden in
  build scripts, FFI, environmental effects, or specification evaluation.

**What it would bring.** These rules would make Catena's claims credible under
hostile or resource-constrained conditions. They would also distinguish a
semantic rejection from a conforming implementation limit and keep a signed,
governed build from depending on undeclared ambient authority.

**Completion evidence.** The result needs a threat model, TCB inventory,
machine-readable implementation profile, reproducible-build experiments,
resource-exhaustion and malicious-input corpora, unsafe-boundary audits,
supply-chain incident procedures, and tests proving that failed or limited
actions publish no successful artifact.

## 15. Whole-language metatheory, optimizer validity, and performance

**Relation to the current corpus.** C010 is the first end-to-end semantic
kernel, with written metatheory, an independent stepper, bounded schedule
exploration, and BEAM differential tests. C011 gives all current
`MUST`/`MUST NOT` obligations permanent identities and maps executable units to
tests. Earlier slices also have focused reference paths. The completeness audit
still marks integrated proof, full reference evaluation, broad differential
testing, optimizer premises, compatibility, usability, performance, and
release gates as `P132`–`G139`.

**Remaining research.** This program should address:

- preservation, progress, principality, coherence, mailbox preservation,
  erasure, and semantic correspondence for the integrated admitted language;
- an independent reference evaluator covering ordinary expressions, all
  failures, handlers, resources, public actors, and foreign values;
- generated and adversarial differential tests for source, typed core,
  optimized core, BEAM output, and bounded concurrency outcomes;
- explicit optimizer proof obligations for evaluation order, totality,
  effects, sharing, trait law evidence, allocation, and traps;
- a compatibility suite spanning public interfaces, data evolution, packages,
  OTP versions, upgrades, and future editions;
- a performance envelope for direct calls, traits, ADTs, matching, conditions,
  comprehensions, handlers, processes, erasure, code size, compile time,
  incremental analysis, and diagnostics; and
- an explicit release-readiness definition tying normative coverage,
  platforms, known limits, usability, security, and performance together.

**What it would bring.** This is the evidence that Catena is one language
rather than several individually plausible calculi. It would also permit
optimization and performance work without using class names, passing tests, or
backend behavior as substitutes for semantic premises.

**Completion evidence.** Every claimed theorem needs a stated feature scope;
every optimization needs checkable premises and before/after differential
tests; every normative obligation needs traceability; every evidence limit
must remain distinct from semantic rejection; and release gates need measured
thresholds and published implementation profiles.

## 16. Compatibility, ecosystem evolution, and compiler self-hosting

**Relation to the current corpus.** C008 establishes exact retained language
revisions, package-local editions, preview lifecycles, migration records, and
selection-bound interfaces and artifacts. It intentionally does not define
the complete source/API/ABI policy, package ecosystem, all migration tooling,
OTP support horizon, or compiler bootstrap. These needs are spread across
`G099`, `G116`, `P125`, `P136`, `G139`, and `G141`; the API/ABI policy
itself is subsequently fixed by C028.

**Remaining research.** Long-term evolution requires:

- a compatibility taxonomy for source, inferred and explicit types, behavior,
  effects, traits, data evolution, serialization, BEAM ABI, governance, and hot
  upgrade;
- package registry and lockfile semantics, yanks, compromised versions,
  artifact retention, and dependency graphs spanning editions;
- source and API migration engines with conservative applicability,
  transactional edits, rollback, and human review;
- OTP-version support and retirement policy with reproducible historical
  builds;
- release criteria for preview, stable, deprecated, removed, prototype, and
  eventual 1.0 boundaries; and
- a late-0.x self-hosting gate: the Catena subset needed to express the
  compiler, bootstrap trust, stage-one/stage-two builds, fixed-point or semantic
  equivalence, rollback, distribution, and continued use of the supported OTP
  Abstract Format boundary.

**What it would bring.** This program would turn the 0.1 prototype line into a
language that can evolve without silently changing old programs or making
historical governed artifacts unverifiable. Self-hosting would test the
language on a demanding real application and reduce bootstrap dependence, but
only after the source, module, FFI, tooling, reproducibility, and release
contracts are strong enough.

**Completion evidence.** The ecosystem needs cross-edition dependency tests,
historical rebuilds, signature and artifact replay, API/ABI compatibility
fixtures, safe and rejected migrations, multi-OTP CI, published release gates,
and reproducible bootstrap stages whose equality criterion is explicit.

## 17. Deliberately deferred experimental features

**Relation to the current corpus.** Several notes identify attractive ideas
that are explicitly outside the initial language: programmable patterns,
generic or streaming comprehensions, impredicative and dependent typing,
general linear types, unrestricted type-level computation, shallow or
multi-shot handlers, higher-order effects, optics syntax, generalized
recursion schemes, categorical compilation, and distributed assurance
services. Checklist items `D046`, `D059`, `D083`, and `D140` preserve some of
these exclusions.

**Remaining research.** These should not become one omnibus “advanced
features” project. Each needs an independent problem statement, evidence of
repeated use, interaction audit, formal semantics, operational contract,
diagnostic story, and comparison with an ordinary library or explicit core
mechanism.

**What it would bring.** Successful proposals could add expressiveness,
modularity, alternate interpretation, streaming, or stronger static
guarantees. Their more immediate value is as falsification tests: they reveal
whether the core architecture can accommodate growth without sacrificing
principal inference, effect visibility, coherence, predictable cost, or
approachability.

**Completion evidence.** No deferred feature should be admitted merely because
it is known from another language or has an elegant categorical account. It
needs a focused inquiry, primary evidence, a reference model, negative cases,
an interaction matrix against the current normative corpus, implementation
measurements, and a versioned inclusion or exclusion decision.

## Dependency-aware research order

The current corpus suggests the following order. It is a dependency proposal,
not a release commitment.

1. **Define the approachable source and ordinary dynamic kernel.** Grammar,
   names, calls, sequencing, failure, and source-to-core elaboration are needed
   before most user-facing research can be tested honestly.
2. **Close modules, packages, built-in data, and application boundaries.** They
   establish the unit of separate compilation, interoperability, and
   compatibility.
3. **Finish the first practical control and library layer.** Validate
   conditions, comprehensions, collections, combinators, derivation, and the
   minimum standard library on representative programs.
4. **Specify resource lifetime and the OTP concurrency model.** Cleanup,
   exceptions, cancellation, selective receive, processes, supervision, and
   time must agree before generic streaming or async abstractions are safe.
5. **Define the BEAM and Erlang boundary.** Stable calling conventions,
   foreign values, callbacks, NIFs, OTP versions, and debugging make the
   language deployable.
6. **Build the developer and assurance ecosystem.** Diagnostics, formatter,
   editor, build, tests, migration, proof/model tools, and long-lived
   governance should consume the same source and semantic identities.
7. **Run whole-language validation and set release gates.** Integrated
   metatheory, optimization evidence, usability, security, performance,
   compatibility, reproducibility, and only then self-hosting determine when a
   broader revision is ready.

At every stage, the [conformance vocabulary](../CONFORMANCE-VOCABULARY.md)
requires deterministic invalidity, explicit limits and traps, bounded
variation, and no undefined behavior. The
[specification authority](../SPECIFICATION-AUTHORITY.md) requires the rule to
exist normatively before compiler behavior or tests can count as its meaning.

## Promotion path

This capture should be reviewed against the atomic checklist and then split
only where ownership is missing:

- keep existing open inquiries as the owners for type integration, effects,
  conditions, comprehensions, combinators, vocabulary, and wider governance;
- create focused inquiries for the source language, module/package system,
  runtime resource model, OTP concurrency model, BEAM interoperability,
  standard library, tooling, and release-readiness programs when active work
  begins;
- create or extend topic maps only after those programs have multiple durable
  artifacts and a useful reading route; and
- archive this synthesis after every retained program has an owner and the
  completeness checklist links to those owners.

## Connections

- The [Catena Language Overview](../language-overview.md) supplies the
  architecture-level commitments and open boundaries summarized here.
- The [language-specification completeness checklist](language-specification-completeness-checklist.md)
  remains the exhaustive ledger of atomic completed, partial, gap, and
  deferred obligations.
- The [Notes index](../20-notes/README.md) links the design syntheses from
  which the open programs were derived.
- The [Inquiries index](../40-inquiries/README.md) records which questions are
  resolved, which remain open, and the evidence required for resolution.
- The [Language Specification index](../60-specification/README.md) is the
  authority route for the existing 0.1.1 through 0.1.8 semantic boundaries.
- The [Conformance Traceability Registry](../10-maps/conformance-traceability.md)
  records current rule-to-test coverage and the explicitly carried future
  obligations.
