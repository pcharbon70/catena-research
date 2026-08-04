---
title: "Catena Language Specification Completeness Checklist"
kind: note
created: "2026-08-01"
maturity: seed
tags:
  - catena
  - language-design
  - specification
aliases:
  - "Catena missing specification checklist"
---

# Catena Language Specification Completeness Checklist

> Temporary inbox capture. This is an audit and planning checklist, not a
> normative specification or a commitment to implement every feature listed.

Catena's research establishes a coherent architectural direction, but it does
not yet constitute a complete language specification. Completeness does not
mean including every familiar language feature. It means that every relevant
boundary is either defined precisely or explicitly excluded, with the
consequences of that exclusion recorded.

This checklist tracks the work needed to turn the current research into an
implementable, testable, and versioned language definition.

## How to use this checklist

Status labels describe the archive at this document's current Git revision:

- **Gap** — no focused research currently specifies the area.
- **Partial** — related research constrains the answer, but normative behavior
  remains undecided or scattered.
- **Deferred** — the research deliberately leaves the feature outside the
  initial core; the specification must still state that boundary explicitly.
- **Complete** — a versioned normative boundary and its required evidence are
  present for this item. Complete does not mean that neighboring items are
  complete.

Every checkbox has a unique reference identifier. `G` identifies a gap, `P`
identifies a partial specification, `D` identifies a deferred feature, and `C`
identifies a completed item. The
three-digit suffix records the item's position in this audit and is never
reused. When an item's status changes, preserve its numeric suffix, change the
prefix, and update every reference to its former identifier in the same
change.

An item is complete only when the language reference states, as applicable:

1. accepted syntax and name-resolution rules;
2. static typing, effect, and coverage rules;
3. dynamic semantics, including order and failure;
4. observable cost or resource guarantees where programmers rely on them;
5. lowering and BEAM interoperability constraints;
6. required diagnostics and representative examples; and
7. executable conformance tests or another verification method.

Checking an item may therefore mean either specifying the feature or recording
that Catena does not support it in the relevant language version.

## Existing research that needs normative consolidation

These areas already have substantial research. They still need to be rewritten
as small normative rules rather than copied wholesale into a specification.

- [x] **C001 — Complete — Hindley–Milner inference and the advanced typing boundary.**
  The [version 0.1 type-system specification](../60-specification/type-system/README.md)
  consolidates the principal core, advanced checking, rows, traits, effects,
  elaboration, metatheory, diagnostics, and executable conformance boundary.
- [x] **C002 — Complete — algebraic data types and pattern matching.** The
  [version 0.2 normative specification](../60-specification/data-and-patterns/README.md)
  and published compiler commit `ae311604ef587a022ce2b7b46599200fcb96a7ab`
  cover nominal declarations, recursive groups,
  visibility, construction, the initial pattern grammar, ordered matching,
  coverage, GADT scope, generated folds, interfaces, and representation
  independence.
- [x] **C003 — Complete — clause conditions.** The
  [version 0.3 normative specification](../60-specification/clause-conditions/README.md)
  and published compiler commit
  [`165fc4837f101d01016248e62479ef4caa0f20ce`](https://github.com/pcharbon70/catena/commit/165fc4837f101d01016248e62479ef4caa0f20ce)
  define the exact `Bool`/`Int`
  fragment, acyclic signed predicates, difference-constraint coverage,
  ordered guard trees, interface evidence, dual BEAM lowering, and a typed
  native receive harness. Public parser syntax, usability, performance, traits,
  recursive totality, and full receive semantics remain separately identified
  later work.
- [x] **C004 — Complete — traits and category-inspired operations.** The
  [normative 0.4 specification](../60-specification/traits-and-categorical-operations/README.md),
  [executable conformance record](../50-journal/2026-08-02-c004-executable-trait-conformance.md),
  and published compiler commit
  [`b69f6f7e3da6015bf9b3385152ca3f3687422472`](https://github.com/pcharbon70/catena/commit/b69f6f7e3da6015bf9b3385152ca3f3687422472)
  freeze the initial hierarchy, behavior-first ABI, coherence, law evidence,
  derivation, operational contracts, specialization, and erasure.
- [x] **C005 — Complete — algebraic effects and handlers.** The
  [normative 0.5 specification](../60-specification/effects-and-handlers/README.md),
  [executable conformance record](../50-journal/2026-08-03-c005-executable-effect-conformance.md),
  [compiler PR #67](https://github.com/pcharbon70/catena/pull/67), and
  immutable compiler commit
  [`b24e58d587c830dbb9d8c87770105714745fcd1b`](https://github.com/pcharbon70/catena/commit/b24e58d587c830dbb9d8c87770105714745fcd1b)
  integrate nominal first-order requests, identity-aware rows, lexical
  capabilities, named deep handlers, affine resumptions, explicit typed core,
  effect-directed CPS, cross-module handlers, and differential reference/BEAM
  traces. Cleanup, exceptions, host effects, scoped control, performance, and
  usability remain separately identified work rather than incompleteness in
  the bounded 0.5 feature.
- [x] **C006 — Complete — language-integrated specifications and governance.**
  The
  [normative 0.6 specification](../60-specification/specifications-and-governance/README.md),
  [executable conformance record](../50-journal/2026-08-03-c006-executable-specification-governance-conformance.md),
  and authorized immutable compiler commit
  `2f6805e166a086f7d67c2cc0f3023e9e34fe2cec` freeze the bounded claim forms,
  evidence semantics, governed scopes, authorization, erasure, artifact
  binding, and transition rules. Public source punctuation and long-term
  protocol evolution remain separately identified work rather than
  incompleteness in the bounded 0.6 feature.

## 1. Specification form and conformance

- [x] **C007 — Complete — normative document structure.** The repository-level
  [Specification Authority](../SPECIFICATION-AUTHORITY.md), enforced template
  and validator, complete 0.1–0.6 chapter migration, aligned compiler-facing
  guides, and [C007 validation record](../50-journal/2026-08-03-c007-normative-document-authority.md)
  define which documents are normative, visibly distinguish definitions,
  examples, rationale, and evidence, require document-and-heading citations,
  and make normative text the sole authority when reference paths, compiler
  behavior, and tests disagree. This governance completion creates no Catena
  0.7 slice or immutable compiler commit.
- [ ] **G008 — Gap — language editions and feature lifecycle.** Define version syntax,
  compatibility promises, deprecation, experimental features, and migration
  between editions.
- [ ] **G009 — Gap — conformance vocabulary.** Define required, implementation-defined,
  unspecified, and invalid behavior; avoid leaving accidental undefined
  behavior.
- [ ] **P010 — Partial — formal semantic kernel.** Normative 0.3 now adds a
  typed safe condition core, ordered guard-tree metadata, rechecked coverage
  facts, and BEAM lowering to the C001/C002 executable kernel. Integrate value rows,
  effect rows, traits, handlers, public processes, and source syntax in one
  model.
- [ ] **P011 — Partial — executable conformance suite.** C001 through C006 now
  have positive, negative, bounded-oracle,
  core-verification, interface-integrity, differential-layout or
  differential-lowering, receive-harness, and OTP 29 runtime evidence.
  Connect every remaining normative rule to positive programs, negative
  programs, expected diagnostics, and runtime observations.
- [ ] **G012 — Gap — implementation limits.** Specify which limits may vary—arity,
  literal size, type-checking resources, mailbox behavior, and generated module
  size—and how implementations report them.

## 2. Lexical grammar and source files

- [ ] **G013 — Gap — source encoding and normalization.** Specify Unicode encoding,
  byte-order marks, newline handling, normalization policy, and invalid input.
- [ ] **G014 — Gap — identifiers.** Specify permitted characters, case rules,
  normalization, qualification, reserved words, and visually confusable names.
- [ ] **G015 — Gap — whitespace and layout.** Decide whether indentation is semantic,
  where separators are required, and how multiline constructs continue.
- [ ] **G016 — Gap — comments and documentation comments.** Define nesting, attachment
  to declarations, Markdown treatment, and whether doctests are executable.
- [ ] **G017 — Gap — literal grammar.** Define integers, floats, strings, characters,
  atoms or symbols, lists, tuples, records, maps, binaries, escapes, and
  interpolation.
- [ ] **G018 — Gap — numeric literal semantics.** Define default types, bases,
  separators, overflow, rounding, exceptional floating-point values, and
  negative-literal parsing.
- [ ] **G019 — Gap — operators and punctuation.** Define precedence, associativity,
  fixity declarations or their absence, pipes, qualification, and parse-error
  recovery.
- [ ] **G020 — Gap — file-to-module relationship.** Define whether filenames determine
  module names, how many modules a file may contain, and how generated files
  are identified.

## 3. Names, modules, packages, and separate compilation

- [ ] **G021 — Gap — namespaces and shadowing.** Define namespaces for values, types,
  constructors, traits, effects, specifications, and modules, plus ambiguity
  and shadowing rules.
- [ ] **G022 — Gap — imports and exports.** Define qualification, renaming, wildcard
  imports or their exclusion, re-exports, unused-import diagnostics, and
  visibility defaults.
- [ ] **P023 — Partial — abstraction boundaries.** C002 completes transparent
  constructor export versus fully abstract type export and layout-free module
  interfaces. Stable layout opt-in and any separate construction versus
  matching authority remain open.
- [ ] **G024 — Gap — dependency cycles.** Define whether module recursion exists and
  how initialization, inference, and separate compilation behave across cycles.
- [ ] **G025 — Gap — package identity and dependency resolution.** Define manifests,
  semantic versioning expectations, lockfiles, source identity, integrity, and
  conflicting transitive versions.
- [ ] **G026 — Gap — prelude policy.** Define automatic imports, opt-out behavior,
  shadowing, and what is guaranteed by every language edition.
- [ ] **G027 — Gap — entry points and application structure.** Define executable and
  library roots, top-level effects, application startup, and shutdown results.
- [ ] **G028 — Gap — API and ABI compatibility.** Define source, type, behavior, and
  BEAM-level compatibility, including what changes require a major version.

## 4. Core expressions and evaluation

- [ ] **P029 — Partial — value and evaluation definition.** State precisely that the
  language is strict and define which forms are values.
- [ ] **P030 — Partial — evaluation order.** C002 defines single scrutinee
  evaluation and source-order constructor fields. C003 adds
  pattern-before-condition order, exactly one condition evaluation, lazy
  left-to-right Boolean composition, false fallthrough, irreversible body
  commitment, and shared or-pattern continuations. General function and
  operator arguments, collections, traits, interpolation, and other forms
  remain open.
- [ ] **G031 — Gap — bindings and sequencing.** Define `let`-like syntax, scope,
  recursive bindings, mutual recursion, unused values, and sequencing of
  effectful expressions.
- [ ] **G032 — Gap — functions and calls.** Define currying or fixed arity, partial
  application, closure capture, named functions, anonymous functions, local
  functions, and tail-call guarantees.
- [ ] **G033 — Gap — conditionals and general branching.** Specify Boolean conditions,
  match expressions, branch typing, missing alternatives, and whether any
  statement-like control forms exist.
- [ ] **P034 — Partial — recursion and termination.** C003 excludes
  recursive condition predicates and verifies an acyclic first-order fragment.
  Separate unrestricted program recursion from future recursive total
  fragments used by conditions, specifications, laws, and compile-time
  evaluation.
- [ ] **P035 — Partial — equality and ordering of primitive values.** C003
  defines exact equality for `Bool` and mathematical `Int`, plus integer
  order, only inside the closed condition fragment. Define their general
  expression forms and floats including NaN, strings, binaries, functions,
  references, processes, mixed numeric types, traits, and coercions.
- [ ] **G036 — Gap — runtime failure taxonomy.** Distinguish typed failure, explicit
  panic or crash, arithmetic faults, failed assertions, foreign exceptions,
  and VM termination.
- [ ] **G037 — Gap — resource and allocation observability.** State which allocation,
  sharing, object identity, garbage collection, stack use, and finalization
  behaviors programs may observe.
- [ ] **G038 — Gap — compile-time evaluation.** Decide whether constants, attributes,
  generated derivations, or macros execute code during compilation and under
  which totality and determinism restrictions.

## 5. Data, collections, and patterns

- [x] **C039 — Complete — algebraic data declaration syntax.** The 0.2 normative specification
  specifies kinded parameters, nullary, positional, and named-product
  constructors, atomic recursive groups, explicit existentials and refined
  results, `derives fold`, and transparent or abstract export.
- [ ] **G040 — Gap — built-in data model.** Define unit, Boolean, numeric, string,
  binary, tuple, list, map, set, process, reference, and function types, or
  explicitly exclude each nonessential built-in.
- [ ] **P041 — Partial — structural records and variants.** Specify literal, selection,
  update, extension, restriction, row-polymorphic typing, duplicate labels, and
  runtime representation.
- [ ] **G042 — Gap — collection construction and update.** Define persistent update,
  duplicate map keys, ordering, key equality, bounds failures, and complexity
  promises.
- [x] **C043 — Complete — initial pattern grammar.** The 0.2 normative specification supports
  wildcard, binder, integer and Boolean literal, tuple, positional and named
  constructor, `as`, `or`, and nested patterns; it explicitly excludes list,
  structural-record, row-variant, binary, range, and programmable forms.
- [ ] **P044 — Partial — refutability by context.** C002 defines all supported
  pattern forms in exhaustive matches. C003 makes multi-clause
  functions exhaustive and gives the typed receive harness selective
  nonconsuming rejection. Local bindings, generators, public receives,
  handlers, and exception clauses still need their own admissibility and
  failure rules.
- [x] **C045 — Complete — initial coverage and redundancy.** The 0.2 normative specification
  uses one usefulness relation for closed nominal data, Booleans, tuples,
  integer literals, abstract types, three-valued inhabitation, guards, `or`
  patterns, and GADT refinements, with witnesses and deterministic limits.
- [ ] **D046 — Deferred — programmable patterns.** Explicitly exclude or separately
  specify view patterns, pattern synonyms, active patterns, and their effects,
  totality, coverage, evaluation count, and cost. C002 explicitly excludes
  these forms without reserving hidden conversion semantics.

## 6. List comprehensions, generators, and iteration

The [list-comprehension synthesis](../20-notes/list-comprehensions.md) now
proposes a coherent initial answer. Every item remains unchecked because the
proposal still needs normative grammar, formalization, implementation, and
validation.

- [ ] **P047 — Partial — list-comprehension surface syntax.** Validate the proposed
  result-producing `for ... yield` shape and specify total generator,
  filtering generator, Boolean filter, binding, and nested qualifier grammar.
- [ ] **P048 — Partial — generator protocol.** Confirm the proposed initial `List A`
  source; keep iterators, streams, effectful producers, and generic foldable
  sources explicitly outside that version.
- [ ] **P049 — Partial — multiple-generator meaning.** Formalize the proposed
  left-to-right, depth-first Cartesian traversal, dependency, source-evaluation
  count, and empty-input behavior.
- [ ] **P050 — Partial — filter semantics.** Validate ordinary typed `Bool` filters
  with visible effects, false-as-skip, and propagation of all other failures.
- [ ] **P051 — Partial — pattern-generator failure.** Formalize exhaustive ordinary
  generators and explicitly marked filtering generators whose pattern mismatch
  alone skips an element.
- [ ] **P052 — Partial — qualifier bindings and scope.** Validate left-to-right
  visibility, non-recursive exhaustive bindings, no escaping names, and the
  proposed same-comprehension rebinding error.
- [ ] **P053 — Partial — evaluation and effect order.** Specify and test exact source
  traversal, qualifier order, multiplicity, short-circuiting, failure timing,
  and effect-row inference.
- [ ] **P054 — Partial — eager versus lazy production.** Confirm eager ordered list
  results; keep lazy streams and infinite inputs under a separate resource and
  cancellation contract.
- [ ] **P055 — Partial — elaboration contract.** Formalize the typed qualifier-tree
  target, pure extensional equations with `map` and `flat_map`, and the fused
  worker behavior that must preserve effects and failures.
- [ ] **P056 — Partial — result type.** Confirm initial `List B` output and explicitly
  exclude maps, sets, binaries, streams, validation values, and arbitrary
  `Applicative` or `Monad` targets.
- [ ] **P057 — Partial — sequential versus parallel execution.** Make sequential
  source-order behavior normative and require separate syntax, effects, and
  structured-concurrency rules for any future parallel form.
- [ ] **P058 — Partial — termination and cost.** Verify tail-recursive workers, linear
  output allocation, no intermediate map/filter lists, Cartesian cost
  explanations, and debugger/profiler source fidelity.
- [ ] **D059 — Deferred — neighboring iteration syntax.** Research ranges,
  effect-only loops, generator functions, async streams, binary and map
  comprehensions, zip qualifiers, and generic collectors independently.

## 7. Type-system surface and advanced boundaries

- [x] **C060 — Complete — type syntax.** Version 0.1 freezes function, tuple,
  constructor, record, variant, effect-row, constrained, quantified, and
  higher-rank type notation.
- [ ] **G061 — Gap — primitive numeric relationships.** Decide whether numeric
  overloading uses traits, literal constraints, defaulting, coercions, or
  distinct operators.
- [ ] **G062 — Gap — aliases, opaque types, and newtypes.** Define identity,
  representation, constructor access, coercion, deriving, and error messages.
- [x] **C063 — Complete — generalization boundary.** The effect-aware hybrid
  rule freezes generalization, signature subsumption, and recursive annotation
  behavior.
- [x] **C064 — Complete — row semantics.** Record, variant, and effect row
  equality are separate, including duplicate effects, lacks constraints, and
  ambiguity.
- [x] **C065 — Complete — trait constraint solving.** Version 0.1 freezes
  instance scope, termination, coherence, ambiguity rejection, no defaulting,
  and failure diagnostics.
- [ ] **G066 — Gap — type-directed name resolution.** State whether field, method,
  constructor, literal, and operator resolution may depend on inferred types.
- [ ] **G067 — Gap — dynamic and unsafe boundaries.** Define casts, runtime type
  inspection, unchecked operations, compiler intrinsics, and how unsafety is
  made visible—or explicitly exclude them.
- [x] **C068 — Complete — checked advanced type profile.** Predicative explicit
  higher rank, signature-directed GADTs, branch-local equalities, and explicit
  rigid constructor existentials are specified behind an annotation boundary.
- [ ] **D140 — Deferred — excluded advanced type features.** Impredicativity,
  inferred higher rank, general linear and dependent types, unrestricted
  type-level computation, and higher-kinded polymorphism over arbitrary kinds stay
  outside version 0.1.

## 8. Traits, derivation, and categorical libraries

- [x] **C069 — Complete — declaration and implementation forms.** Normative 0.4
  defines kinded parameters, parents, constraints, exact minimal methods,
  visibility metadata, implementation ownership, and placement through JSON
  AST 0.4. Public parser punctuation remains deliberately unfrozen.
- [x] **C070 — Complete — coherence and ownership.** Version 0.1 freezes
  trait-or-type ownership, prohibits overlap and local implementations, and
  requires import-order-independent identity and separate compilation.
- [x] **C071 — Complete — associated information.** Traits support methods,
  multi-parameter constraints, functional dependencies, and associated types;
  associated constants are excluded.
- [x] **C072 — Complete — laws and trusted evidence.** Normative 0.4 admits only
  promised, tested, and compiler-derived evidence, reserves trusted and proved,
  fixes the pure-total finite law domain, and forbids law rewrites.
- [x] **C073 — Complete — derivation.** Normative 0.4 adds explicit-target
  `Equatable`, `Orderable`, `Mapper`, `TwoSlotMapper`, `Reducible`, and
  `CollectingMapper` instances and type-qualified functions without override
  hooks, with tested stack-safe standard `List` mapping and reduction.
- [x] **C074 — Complete — operational contracts.** Normative 0.4 freezes strict
  left-to-right order, exact-once declaration-order visits, subject-last ABI,
  separate early termination, no law-implied concurrency, and standard
  collection stack safety.
- [x] **C075 — Complete — dispatch and dictionary observability.** Normative 0.4
  specifies deterministic manifest-directed specialization, direct calls, one
  companion BEAM, no reflection, and complete evidence erasure, with published
  artifact inspection and repeat-build evidence.

## 9. Effects, failure, and resource scopes

- [x] **C076 — Complete — effect declaration and use syntax.** Normative 0.5
  freezes normal parameter-list operations, `request`, behavior-first `uses`,
  optional explicit capability qualification, module-level `handler`
  declarations, `handle ... using ... as ...`, mandatory return and complete
  operation clauses, and `resume ... with ...`, with executable positive,
  negative, interface, and cross-module conformance evidence.
- [x] **C077 — Complete — handler selection.** Duplicate effect rows preserve
  lexical capability identity; handling removes the statically selected
  occurrence, never a runtime nearest-label match.
- [x] **C078 — Complete — resumption discipline.** Affine use is checked in the
  typed core and backed by a runtime consumed token; resumptions cannot escape,
  be stored, or be resumed twice.
- [x] **C079 — Complete — effect ordering.** Normative 0.5 freezes strict handler
  argument order, exact identity forwarding, observable nesting order, abort,
  deep reinstallation, and outer-scope effects from return and operation
  clauses. The independent free-request evaluator and generated BEAM agree on
  the bounded conformance traces.
- [ ] **G080 — Gap — cleanup and resource scopes.** Specify acquisition, release,
  cancellation, abort, panic, normal return, process exit, and foreign-frame
  unwinding.
- [ ] **G081 — Gap — exception boundary.** Decide whether exceptions are an effect,
  process exits, foreign failures, programmer panics, or several distinct
  mechanisms, and how each is typed and caught.
- [ ] **G082 — Gap — top-level effects.** Define which requests an application entry
  point may leave unhandled and who interprets them.
- [ ] **D083 — Deferred — scoped and multi-shot computations.** Explicitly bound
  generators, async, nondeterminism, transactions, shallow handlers,
  higher-order effects, and multi-shot continuations until their semantics are
  separately specified.

## 10. Processes, concurrency, and distribution

- [ ] **G084 — Gap — process creation and lifetime.** Define spawn, normal completion,
  crash, links, monitors, trapping exits, parent-child relationships, and
  structured task scopes.
- [ ] **G085 — Gap — message semantics.** Define send results, copying and sharing,
  ordering guarantees, mailbox growth, unsupported values, and remote delivery.
- [ ] **P086 — Partial — selective receive.** C003 provides a typed
  native-only lowering harness requiring one closed message type and portable
  inlined conditions, while preserving rejected messages. Connect public
  syntax, effect and protocol typing, timeouts, mailbox scan order, starvation,
  cancellation, and cost explanations in one normative rule.
- [ ] **G087 — Gap — typed protocols.** Decide whether mailbox protocols, process
  handles, replies, and protocol evolution are statically tracked or library
  conventions.
- [ ] **G088 — Gap — cancellation and time.** Define cancellation propagation,
  deadlines, monotonic time, sleep, timer races, and cleanup.
- [ ] **G089 — Gap — supervision.** Specify which OTP supervision concepts are direct
  language features, standard-library APIs, generated specifications, or plain
  Erlang interoperability.
- [ ] **G090 — Gap — scheduler observability.** State fairness assumptions, reduction
  preemption, process priority, blocking foreign work, and determinism limits.
- [ ] **G091 — Gap — distribution.** Define node identity, serialization, code-version
  skew, connection failure, partitions, authentication, and delivery claims.
- [ ] **G092 — Gap — hot code upgrade.** Define state migration, old and new code
  coexistence, capability and type compatibility, rollback, and governance
  evidence.

## 11. BEAM representation and Erlang interoperability

- [ ] **P093 — Partial — Catena-to-BEAM value mapping.** C002 defines and
  differentially checks uniform and compact nominal ADT layouts behind a
  layout-free typed interface. Records, variants, closures, trait dictionaries,
  capabilities, erased artifacts, and the full primitive model remain open.
- [ ] **G094 — Gap — calling conventions.** Define exported names and arities,
  currying, closures, tail calls, callbacks, stack traces, and module metadata.
- [ ] **G095 — Gap — Erlang type boundary.** Specify how dynamically typed terms enter
  Catena, which checks occur, how failures are represented, and whether gradual
  or explicit dynamic types exist.
- [ ] **G096 — Gap — foreign calls and callbacks.** Define syntax, effect declarations,
  trust, exceptions, blocking behavior, cancellation, ownership, and callback
  lifetime.
- [ ] **G097 — Gap — binaries, maps, PIDs, ports, references, and funs.** Define which
  BEAM-native values are first-class and what type and equality guarantees they
  receive.
- [ ] **G098 — Gap — NIFs and ports.** Define unsafe boundaries, scheduler classes,
  resource finalization, VM crashes, capability requirements, and packaging.
- [ ] **G099 — Gap — OTP compatibility policy.** Define supported versions, feature
  detection, portable guard subset, generated bytecode level, and upgrade
  cadence.
- [ ] **G100 — Gap — debugging metadata.** Define source locations, inlined frames,
  generated code, erased specifications, effect handlers, and dictionary frames
  in traces and tooling.

## 12. Standard library contract

- [ ] **G101 — Gap — minimum prelude.** Freeze core types, constructors, functions,
  traits, effects, and automatic imports.
- [ ] **P102 — Partial — collection protocols.** Specify list, map, set, iterator,
  stream, fold, traversal, builder, and early-termination contracts, including
  complexity.
- [ ] **P103 — Partial — outcome types.** Define `Option`, `Result`, validation, panic,
  and process failure without conflating their behavior.
- [ ] **G104 — Gap — text and binary model.** Define Unicode scalar values, graphemes,
  indexing, slicing, normalization, encoding conversion, interpolation, and
  binary pattern matching.
- [ ] **G105 — Gap — numeric library.** Define integer ranges or arbitrary precision,
  floating-point behavior, decimal support, conversions, parsing, and checked
  arithmetic.
- [ ] **G106 — Gap — environmental effects.** Define standard capabilities for I/O,
  files, network, time, randomness, environment, logging, and process control.
- [ ] **P107 — Partial — category-inspired API names.** Normative 0.4 chooses the
  canonical behavior-first trait and method ABI and confines formal names to
  reference metadata. Independent comprehension and usability validation is
  still required.
- [ ] **G108 — Gap — stability and performance policy.** State which APIs, laws,
  traversal orders, asymptotic bounds, and representations are compatibility
  promises.

## 13. Specifications, governance, and erasure

- [ ] **P109 — Partial — surface grammar.** Freeze syntax for claims, evidence,
  assumptions, governed scopes, policy, authorization, decisions, and
  transitions. Normative 0.6 freezes semantic JSON forms but intentionally
  leaves public parser punctuation open.
- [x] **C110 — Complete — checking language.** Normative 0.6 fixes an explicitly
  typed pure fragment, exact integer, Boolean, and nested-tuple examples,
  deterministic left-to-right evaluation, distinct failure outcomes, and a
  fixed 20,000-step bound. The compiler and independent tests enforce the
  typing, purity, dependency, and budget boundaries.
- [x] **C111 — Complete — enforcement modes.** Normative 0.6 selects optional
  package adoption, separate specification and governance adoption, additive
  package-to-subject scopes, inherited dependency claims, fail-closed policy,
  and distinct `build`, `publish`, and `activate` gates.
- [x] **C112 — Complete — evidence lifecycle.** Normative 0.6 binds compiler
  evidence, signed attestations, and explicit assumptions to exact claim,
  subject, tool, artifact, role, and logical sequence identities. Revocation,
  delegation, replacement, and hash-chained lifecycle replay have executable
  positive and adversarial coverage.
- [x] **C113 — Complete — erasure semantics.** Normative 0.6 forbids runtime
  reachability and export of verification-only definitions, erases the
  specification graph before Erlang Abstract Format, and requires complete
  accounting plus byte-identical package BEAM artifacts with and without fully
  discharged specifications. Runtime monitors are outside this version.
- [x] **C114 — Complete — artifact format.** Normative 0.6 fixes strict JCS,
  SHA-256, domain-separated Ed25519 signatures, trust-root, governance-bundle,
  and assurance-manifest formats, exact multi-module artifact binding, staged
  output transactions, and an external-signer payload.
- [x] **C115 — Complete — governance identity and trust roots.** Normative 0.6
  fixes offline principals, distinct-actor role thresholds, scoped delegation,
  revocation, old-and-new normal rotation, predeclared recovery, and historical
  root replay. Transparency services and network identity are excluded from
  the bounded offline protocol and remain possible later additions.
- [ ] **G116 — Gap — long-term evolution.** Define schema migration, policy-version
  interpretation, archived evidence, reproducible historical decisions, and
  compatibility with newer compilers.

## 14. Diagnostics, tools, and developer experience

- [ ] **P117 — Partial — diagnostic contract.** Define stable identifiers, severity,
  primary and secondary locations, inferred-type presentation, constraint
  provenance, missing-pattern witnesses, guard explanations, and generated-code
  attribution.
- [ ] **G118 — Gap — formatter.** Define canonical formatting, comments, idempotence,
  version coupling, and whether formatting is part of source compatibility.
- [ ] **G119 — Gap — documentation tool.** Define doc attachment, links, examples,
  doctests, hidden APIs, traits and implementations, effects, laws, and
  specification views.
- [ ] **G120 — Gap — interactive environment.** Define REPL typing and effects,
  declaration replacement, process lifetime, module loading, history, and
  governance behavior.
- [ ] **G121 — Gap — build system and package manager.** Define project discovery,
  profiles, dependency fetching, code generation, cache keys, offline builds,
  and reproducibility.
- [ ] **G122 — Gap — testing tools.** Define unit, property, model, concurrency, and
  specification tests; seeds; shrinking; timeouts; and evidence capture.
- [ ] **G123 — Gap — editor protocol.** Define incremental parsing and typing, partial
  programs, completion, hover, rename, formatting, semantic tokens, and stable
  diagnostic identity.
- [ ] **G124 — Gap — debugging and observability.** Define breakpoints, stack traces,
  handlers, processes, messages, generated derivations, erased declarations,
  tracing, profiling, and crash reports.
- [ ] **G125 — Gap — migration tools.** Define edition fixes, API refactors, deprecated
  syntax handling, and machine-applicable diagnostic edits.

## 15. Security, reproducibility, and operational limits

- [ ] **G126 — Gap — trusted computing base.** Enumerate parser, type checker, trait
  solver, effect checker, proof kernel, serializer, signer, runtime, and foreign
  components whose bugs can violate guarantees.
- [ ] **G127 — Gap — unsafe-code policy.** Define whether unsafe operations exist,
  where they may appear, what obligations they assume, and how artifacts expose
  them.
- [ ] **G128 — Gap — reproducible builds.** Define environmental inputs, timestamps,
  path normalization, dependency integrity, generated files, compiler version,
  and byte-for-byte expectations.
- [ ] **G129 — Gap — resource exhaustion.** Define compiler limits, runtime memory and
  mailbox pressure, recursion, unbounded type search, denial-of-service risks,
  and required diagnostics or controls.
- [ ] **G130 — Gap — supply-chain policy.** Define package signing, provenance,
  compromised releases, yanks, lockfiles, native dependencies, and governance
  evidence.
- [ ] **G131 — Gap — secrets and capabilities.** Define how credentials and ambient VM
  authority enter programs without being hidden by effects, build scripts, or
  specification evaluation.

## 16. Formal validation and release gates

- [ ] **P132 — Partial — progress and preservation targets.** C002 states the
  nominal and structural claims; C003 adds condition typing, closed
  safety, predicate expansion, fallthrough, commitment, guarded exhaustive
  progress, fact soundness, lowering equivalence, receive preservation, and
  evidence-erasure targets. Effects, public processes, foreign values, and the
  integrated theorem remain open.
- [ ] **P133 — Partial — reference evaluator.** The executable oracle now covers
  C001 pure expressions, C002 nominal matching and folds, and C003
  primitive conditions, lazy Boolean composition, predicate calls, and ordered
  fallthrough. Effects, processes, foreign values, explicit failures, and the
  remaining language forms are not yet modeled.
- [ ] **P134 — Partial — differential testing.** C002 compares reference,
  uniform-layout, and compact-layout observations; C003 compares the
  reference evaluator with forced native and ordinary BEAM condition lowering.
  Effects, failures, traces, public concurrency, foreign values, and resource
  scopes remain open.
- [ ] **G135 — Gap — optimizer validity.** Identify which rewrites rely on pure
  semantics, trait laws, evaluation order, totality, or trusted evidence and
  reject rewrites whose premises are absent.
- [ ] **G136 — Gap — compatibility suite.** Test public signatures, data evolution,
  package resolution, artifact manifests, OTP versions, hot upgrades, and
  language editions.
- [ ] **G137 — Gap — usability gate.** Test whether programmers can predict `map`,
  `map2`, `and_then`, traversal, handlers, guards, comprehensions, and
  diagnostics without prerequisite mathematical vocabulary.
- [ ] **G138 — Gap — performance envelope.** Benchmark direct calls, traits, ADTs,
  pattern matching, guards, comprehensions, effects, processes, erasure, code
  size, compile time, and diagnostic provenance.
- [ ] **G139 — Gap — release-readiness definition.** State the minimum normative
  chapters, conformance coverage, platform support, known limitations, and
  stability promises required before calling a version complete.

## Suggested research order

The checklist is too broad to turn into independent deep dives all at once.
The following order resolves dependencies first:

1. **Surface and dynamic kernel:** lexical grammar, expression grammar,
   evaluation order, failures, and core pattern contexts.
2. **Modules and execution boundary:** names, signatures, packages, entry
   points, separate compilation, and BEAM calling conventions.
3. **Collections and iteration:** concrete collection model, iterator protocol,
   list comprehensions, generator failure, effect order, and lowering.
4. **Effects and runtime scopes:** exceptions, cleanup, cancellation,
   processes, selective receive, and supervision.
5. **Interoperability and standard library:** BEAM values, Erlang calls, text,
   numerics, environmental effects, and compatibility policy.
6. **Normative consolidation:** combine existing type, ADT, guard, trait,
   effect, and governance research into a versioned reference plus tests.
7. **Tooling and release gates:** formatter, documentation, REPL, package and
   build tools, diagnostics, conformance, security, and performance.

## Connections

- The [Catena Language Overview](../language-overview.md) supplies the current
  architecture and its explicit open design boundaries; this checklist expands
  those boundaries into reviewable specification obligations.
- [A Greenfield Type System for Catena](../20-notes/catena-greenfield-type-system.md)
  constrains the type-system and elaboration items but remains a design
  synthesis rather than a normative reference.
- [Algebraic Data Types](../20-notes/algebraic-data-types.md) and
  [Clause Guards](../20-notes/clause-guards.md) constrain patterns, coverage,
  failure, and selective receive, including several decisions needed by
  comprehension qualifiers.
- [Combinators for Algebraic Data and Categorical Programming](../20-notes/combinators-for-algebraic-data-and-categorical-programming.md)
  supplies the operations to which comprehensions might lower, while leaving
  their surface syntax and operational equivalence unspecified.
- [Algebraic Effects and Handlers](../20-notes/algebraic-effects-and-handlers.md)
  constrains comprehension effects, generators, cancellation, and resource
  scopes without defining those features completely.
- [Language-Integrated Specifications and Governance](../20-notes/language-integrated-specifications-and-governance.md)
  supplies the assurance architecture that a complete language reference must
  eventually express normatively.

## Promotion criterion

After review, split this capture into a selective specification-roadmap map and
focused inquiries for the highest-priority gaps. Archive or remove the inbox
copy once every retained item has an owner, destination, and explicit initial
language boundary.
