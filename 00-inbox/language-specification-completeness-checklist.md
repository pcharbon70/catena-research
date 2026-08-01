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

Status labels describe the archive as of 2026-08-01:

- **Gap** — no focused research currently specifies the area.
- **Partial** — related research constrains the answer, but normative behavior
  remains undecided or scattered.
- **Deferred** — the research deliberately leaves the feature outside the
  initial core; the specification must still state that boundary explicitly.

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

- [ ] **Partial — Hindley–Milner inference and the advanced typing boundary.**
  Consolidate principal rank-1 inference, generalization, annotations,
  higher-rank checking, rows, trait constraints, and deferred GADTs into one
  formal static semantics.
- [ ] **Partial — algebraic data types and pattern matching.** Consolidate data
  declarations, visibility, positivity, derivation, ordered matching,
  exhaustiveness, redundancy, and representation independence.
- [ ] **Partial — clause guards.** Settle the exact guard-safe expression set,
  user-defined predicates, coverage-fact precision, receive-safe subset, and
  surface syntax.
- [ ] **Partial — traits and category-inspired operations.** Freeze the initial
  hierarchy, public vocabulary, implementation coherence, law evidence,
  derivation rules, and operational contracts.
- [ ] **Partial — algebraic effects and handlers.** Turn the proposed nominal
  operations, effect rows, lexical capabilities, deep handlers, and affine
  resumptions into one calculus and surface design.
- [ ] **Partial — language-integrated specifications and governance.** Freeze
  claim forms, evidence semantics, governed scopes, authorization, erasure,
  artifact binding, and transition rules.

## 1. Specification form and conformance

- [ ] **Gap — normative document structure.** Define which documents are
  normative, how examples and rationale are distinguished, and how conflicts
  between the reference, compiler, and tests are resolved.
- [ ] **Gap — language editions and feature lifecycle.** Define version syntax,
  compatibility promises, deprecation, experimental features, and migration
  between editions.
- [ ] **Gap — conformance vocabulary.** Define required, implementation-defined,
  unspecified, and invalid behavior; avoid leaving accidental undefined
  behavior.
- [ ] **Partial — formal semantic kernel.** Integrate types, value rows, effect
  rows, traits, patterns, guards, handlers, and elaboration in one core model.
- [ ] **Gap — executable conformance suite.** Connect every normative rule to
  positive programs, negative programs, expected diagnostics, and runtime
  observations.
- [ ] **Gap — implementation limits.** Specify which limits may vary—arity,
  literal size, type-checking resources, mailbox behavior, and generated module
  size—and how implementations report them.

## 2. Lexical grammar and source files

- [ ] **Gap — source encoding and normalization.** Specify Unicode encoding,
  byte-order marks, newline handling, normalization policy, and invalid input.
- [ ] **Gap — identifiers.** Specify permitted characters, case rules,
  normalization, qualification, reserved words, and visually confusable names.
- [ ] **Gap — whitespace and layout.** Decide whether indentation is semantic,
  where separators are required, and how multiline constructs continue.
- [ ] **Gap — comments and documentation comments.** Define nesting, attachment
  to declarations, Markdown treatment, and whether doctests are executable.
- [ ] **Gap — literal grammar.** Define integers, floats, strings, characters,
  atoms or symbols, lists, tuples, records, maps, binaries, escapes, and
  interpolation.
- [ ] **Gap — numeric literal semantics.** Define default types, bases,
  separators, overflow, rounding, exceptional floating-point values, and
  negative-literal parsing.
- [ ] **Gap — operators and punctuation.** Define precedence, associativity,
  fixity declarations or their absence, pipes, qualification, and parse-error
  recovery.
- [ ] **Gap — file-to-module relationship.** Define whether filenames determine
  module names, how many modules a file may contain, and how generated files
  are identified.

## 3. Names, modules, packages, and separate compilation

- [ ] **Gap — namespaces and shadowing.** Define namespaces for values, types,
  constructors, traits, effects, specifications, and modules, plus ambiguity
  and shadowing rules.
- [ ] **Gap — imports and exports.** Define qualification, renaming, wildcard
  imports or their exclusion, re-exports, unused-import diagnostics, and
  visibility defaults.
- [ ] **Partial — abstraction boundaries.** Finish constructor visibility,
  opaque types, public signatures, stable layout opt-in, and separate
  construction versus matching authority.
- [ ] **Gap — dependency cycles.** Define whether module recursion exists and
  how initialization, inference, and separate compilation behave across cycles.
- [ ] **Gap — package identity and dependency resolution.** Define manifests,
  semantic versioning expectations, lockfiles, source identity, integrity, and
  conflicting transitive versions.
- [ ] **Gap — prelude policy.** Define automatic imports, opt-out behavior,
  shadowing, and what is guaranteed by every language edition.
- [ ] **Gap — entry points and application structure.** Define executable and
  library roots, top-level effects, application startup, and shutdown results.
- [ ] **Gap — API and ABI compatibility.** Define source, type, behavior, and
  BEAM-level compatibility, including what changes require a major version.

## 4. Core expressions and evaluation

- [ ] **Partial — value and evaluation definition.** State precisely that the
  language is strict and define which forms are values.
- [ ] **Gap — evaluation order.** Define order for function and operator
  arguments, record fields, constructor fields, collection elements, guards,
  trait operations, and interpolations.
- [ ] **Gap — bindings and sequencing.** Define `let`-like syntax, scope,
  recursive bindings, mutual recursion, unused values, and sequencing of
  effectful expressions.
- [ ] **Gap — functions and calls.** Define currying or fixed arity, partial
  application, closure capture, named functions, anonymous functions, local
  functions, and tail-call guarantees.
- [ ] **Gap — conditionals and general branching.** Specify Boolean conditions,
  match expressions, branch typing, missing alternatives, and whether any
  statement-like control forms exist.
- [ ] **Partial — recursion and termination.** Separate unrestricted program
  recursion from total fragments used by guards, specifications, laws, and
  compile-time evaluation.
- [ ] **Gap — equality and ordering of primitive values.** Define integers,
  floats including NaN, strings, binaries, functions, references, processes,
  and mixed numeric types.
- [ ] **Gap — runtime failure taxonomy.** Distinguish typed failure, explicit
  panic or crash, arithmetic faults, failed assertions, foreign exceptions,
  and VM termination.
- [ ] **Gap — resource and allocation observability.** State which allocation,
  sharing, object identity, garbage collection, stack use, and finalization
  behaviors programs may observe.
- [ ] **Gap — compile-time evaluation.** Decide whether constants, attributes,
  generated derivations, or macros execute code during compilation and under
  which totality and determinism restrictions.

## 5. Data, collections, and patterns

- [ ] **Partial — algebraic data declaration syntax.** Freeze type parameters,
  constructor fields, record constructors, recursive types, derives, and
  visibility syntax.
- [ ] **Gap — built-in data model.** Define unit, Boolean, numeric, string,
  binary, tuple, list, map, set, process, reference, and function types, or
  explicitly exclude each nonessential built-in.
- [ ] **Partial — structural records and variants.** Specify literal, selection,
  update, extension, restriction, row-polymorphic typing, duplicate labels, and
  runtime representation.
- [ ] **Gap — collection construction and update.** Define persistent update,
  duplicate map keys, ordering, key equality, bounds failures, and complexity
  promises.
- [ ] **Partial — complete pattern grammar.** Settle constructor, literal,
  tuple, list, record, variant, binary, as-pattern, or-pattern, wildcard, and
  nested patterns.
- [ ] **Partial — refutability by context.** Define which patterns may appear in
  function parameters, local bindings, generators, receives, handlers, and
  exception clauses, and what failure means in each place.
- [ ] **Partial — coverage and redundancy.** Freeze the coverage model for
  closed data, open rows, guards, abstract types, integer ranges, strings, and
  future refinements.
- [ ] **Deferred — programmable patterns.** Explicitly exclude or separately
  specify view patterns, pattern synonyms, active patterns, and their effects,
  totality, coverage, evaluation count, and cost.

## 6. List comprehensions, generators, and iteration

The [list-comprehension synthesis](../20-notes/list-comprehensions.md) now
proposes a coherent initial answer. Every item remains unchecked because the
proposal still needs normative grammar, formalization, implementation, and
validation.

- [ ] **Partial — list-comprehension surface syntax.** Validate the proposed
  result-producing `for ... yield` shape and specify total generator,
  filtering generator, Boolean filter, binding, and nested qualifier grammar.
- [ ] **Partial — generator protocol.** Confirm the proposed initial `List A`
  source; keep iterators, streams, effectful producers, and generic foldable
  sources explicitly outside that version.
- [ ] **Partial — multiple-generator meaning.** Formalize the proposed
  left-to-right, depth-first Cartesian traversal, dependency, source-evaluation
  count, and empty-input behavior.
- [ ] **Partial — filter semantics.** Validate ordinary typed `Bool` filters
  with visible effects, false-as-skip, and propagation of all other failures.
- [ ] **Partial — pattern-generator failure.** Formalize exhaustive ordinary
  generators and explicitly marked filtering generators whose pattern mismatch
  alone skips an element.
- [ ] **Partial — qualifier bindings and scope.** Validate left-to-right
  visibility, non-recursive exhaustive bindings, no escaping names, and the
  proposed same-comprehension rebinding error.
- [ ] **Partial — evaluation and effect order.** Specify and test exact source
  traversal, qualifier order, multiplicity, short-circuiting, failure timing,
  and effect-row inference.
- [ ] **Partial — eager versus lazy production.** Confirm eager ordered list
  results; keep lazy streams and infinite inputs under a separate resource and
  cancellation contract.
- [ ] **Partial — elaboration contract.** Formalize the typed qualifier-tree
  target, pure extensional equations with `map` and `flat_map`, and the fused
  worker behavior that must preserve effects and failures.
- [ ] **Partial — result type.** Confirm initial `List B` output and explicitly
  exclude maps, sets, binaries, streams, validation values, and arbitrary
  `Applicative` or `Monad` targets.
- [ ] **Partial — sequential versus parallel execution.** Make sequential
  source-order behavior normative and require separate syntax, effects, and
  structured-concurrency rules for any future parallel form.
- [ ] **Partial — termination and cost.** Verify tail-recursive workers, linear
  output allocation, no intermediate map/filter lists, Cartesian cost
  explanations, and debugger/profiler source fidelity.
- [ ] **Deferred — neighboring iteration syntax.** Research ranges,
  effect-only loops, generator functions, async streams, binary and map
  comprehensions, zip qualifiers, and generic collectors independently.

## 7. Type-system surface and advanced boundaries

- [ ] **Partial — type syntax.** Freeze function, tuple, constructor, record,
  variant, effect-row, constrained, quantified, and higher-rank type notation.
- [ ] **Gap — primitive numeric relationships.** Decide whether numeric
  overloading uses traits, literal constraints, defaulting, coercions, or
  distinct operators.
- [ ] **Gap — aliases, opaque types, and newtypes.** Define identity,
  representation, constructor access, coercion, deriving, and error messages.
- [ ] **Partial — generalization boundary.** Freeze value restriction or
  effect-aware generalization, signature subsumption, and recursive annotation
  rules.
- [ ] **Partial — row semantics.** Define record, variant, and effect row
  equality separately, including duplicate labels, lacks constraints, and
  ambiguity.
- [ ] **Partial — trait constraint solving.** Freeze instance scope,
  termination, coherence, ambiguity, defaulting, and failure diagnostics.
- [ ] **Gap — type-directed name resolution.** State whether field, method,
  constructor, literal, and operator resolution may depend on inferred types.
- [ ] **Gap — dynamic and unsafe boundaries.** Define casts, runtime type
  inspection, unchecked operations, compiler intrinsics, and how unsafety is
  made visible—or explicitly exclude them.
- [ ] **Deferred — advanced type features.** Record the initial exclusion and
  future compatibility boundary for GADTs, existential types, higher-kinded
  polymorphism, linear types beyond resumptions, dependent types, and
  unrestricted type-level computation.

## 8. Traits, derivation, and categorical libraries

- [ ] **Partial — declaration and implementation syntax.** Define parameters,
  constraints, methods, defaults, visibility, documentation, and implementation
  placement.
- [ ] **Partial — coherence and ownership.** Freeze orphan rules,
  overlap prohibition, local implementations, implementation identity, and
  separate-compilation behavior.
- [ ] **Partial — associated information.** Decide whether traits support
  associated types, functional dependencies, constants, or only methods and
  constraints in the initial language.
- [ ] **Partial — laws and trusted evidence.** Define which laws are
  documentation, generated evidence, checked properties, proof obligations, or
  optimizer assumptions.
- [ ] **Partial — derivation.** Specify eligible datatype shapes, generated
  names, customization, failure diagnostics, law provenance, and public API
  stability.
- [ ] **Partial — operational contracts.** Freeze order, strictness,
  multiplicity, short-circuiting, stack safety, and effect policy for standard
  operations such as mapping, combining, chaining, folding, and traversing.
- [ ] **Gap — dispatch and dictionary observability.** Define specialization,
  dictionary identity, equality, reflection, performance, and whether
  elaboration can change observable behavior.

## 9. Effects, failure, and resource scopes

- [ ] **Partial — effect declaration and use syntax.** Freeze operations,
  request syntax, effect annotations, capability binding, handling, forwarding,
  return clauses, and resumption syntax.
- [ ] **Partial — handler selection.** Resolve repeated labels, multiple
  instances of one effect, lexical inference, explicit capability passing, and
  ambiguity diagnostics.
- [ ] **Partial — resumption discipline.** Decide whether affine use is checked
  statically, dynamically, or both, and specify escape, storage, thread, and
  second-resume behavior.
- [ ] **Partial — effect ordering.** Define nested handler order, state and
  failure interaction, forwarding, abort, and behavior when return or operation
  clauses perform effects.
- [ ] **Gap — cleanup and resource scopes.** Specify acquisition, release,
  cancellation, abort, panic, normal return, process exit, and foreign-frame
  unwinding.
- [ ] **Gap — exception boundary.** Decide whether exceptions are an effect,
  process exits, foreign failures, programmer panics, or several distinct
  mechanisms, and how each is typed and caught.
- [ ] **Gap — top-level effects.** Define which requests an application entry
  point may leave unhandled and who interprets them.
- [ ] **Deferred — scoped and multi-shot computations.** Explicitly bound
  generators, async, nondeterminism, transactions, shallow handlers,
  higher-order effects, and multi-shot continuations until their semantics are
  separately specified.

## 10. Processes, concurrency, and distribution

- [ ] **Gap — process creation and lifetime.** Define spawn, normal completion,
  crash, links, monitors, trapping exits, parent-child relationships, and
  structured task scopes.
- [ ] **Gap — message semantics.** Define send results, copying and sharing,
  ordering guarantees, mailbox growth, unsupported values, and remote delivery.
- [ ] **Partial — selective receive.** Connect patterns, receive-safe guards,
  timeouts, mailbox scan order, starvation, and compiler lowering in one
  normative rule.
- [ ] **Gap — typed protocols.** Decide whether mailbox protocols, process
  handles, replies, and protocol evolution are statically tracked or library
  conventions.
- [ ] **Gap — cancellation and time.** Define cancellation propagation,
  deadlines, monotonic time, sleep, timer races, and cleanup.
- [ ] **Gap — supervision.** Specify which OTP supervision concepts are direct
  language features, standard-library APIs, generated specifications, or plain
  Erlang interoperability.
- [ ] **Gap — scheduler observability.** State fairness assumptions, reduction
  preemption, process priority, blocking foreign work, and determinism limits.
- [ ] **Gap — distribution.** Define node identity, serialization, code-version
  skew, connection failure, partitions, authentication, and delivery claims.
- [ ] **Gap — hot code upgrade.** Define state migration, old and new code
  coexistence, capability and type compatibility, rollback, and governance
  evidence.

## 11. BEAM representation and Erlang interoperability

- [ ] **Gap — Catena-to-BEAM value mapping.** Define representation of every
  primitive, ADT, record, variant, closure, trait dictionary, capability, and
  erased artifact.
- [ ] **Gap — calling conventions.** Define exported names and arities,
  currying, closures, tail calls, callbacks, stack traces, and module metadata.
- [ ] **Gap — Erlang type boundary.** Specify how dynamically typed terms enter
  Catena, which checks occur, how failures are represented, and whether gradual
  or explicit dynamic types exist.
- [ ] **Gap — foreign calls and callbacks.** Define syntax, effect declarations,
  trust, exceptions, blocking behavior, cancellation, ownership, and callback
  lifetime.
- [ ] **Gap — binaries, maps, PIDs, ports, references, and funs.** Define which
  BEAM-native values are first-class and what type and equality guarantees they
  receive.
- [ ] **Gap — NIFs and ports.** Define unsafe boundaries, scheduler classes,
  resource finalization, VM crashes, capability requirements, and packaging.
- [ ] **Gap — OTP compatibility policy.** Define supported versions, feature
  detection, portable guard subset, generated bytecode level, and upgrade
  cadence.
- [ ] **Gap — debugging metadata.** Define source locations, inlined frames,
  generated code, erased specifications, effect handlers, and dictionary frames
  in traces and tooling.

## 12. Standard library contract

- [ ] **Gap — minimum prelude.** Freeze core types, constructors, functions,
  traits, effects, and automatic imports.
- [ ] **Partial — collection protocols.** Specify list, map, set, iterator,
  stream, fold, traversal, builder, and early-termination contracts, including
  complexity.
- [ ] **Partial — outcome types.** Define `Option`, `Result`, validation, panic,
  and process failure without conflating their behavior.
- [ ] **Gap — text and binary model.** Define Unicode scalar values, graphemes,
  indexing, slicing, normalization, encoding conversion, interpolation, and
  binary pattern matching.
- [ ] **Gap — numeric library.** Define integer ranges or arbitrary precision,
  floating-point behavior, decimal support, conversions, parsing, and checked
  arithmetic.
- [ ] **Gap — environmental effects.** Define standard capabilities for I/O,
  files, network, time, randomness, environment, logging, and process control.
- [ ] **Partial — category-inspired API names.** Validate the approachable
  vocabulary, choose canonical operation names, and specify how formal names
  appear in reference material without creating competing public APIs.
- [ ] **Gap — stability and performance policy.** State which APIs, laws,
  traversal orders, asymptotic bounds, and representations are compatibility
  promises.

## 13. Specifications, governance, and erasure

- [ ] **Partial — surface grammar.** Freeze syntax for claims, evidence,
  assumptions, governed scopes, policy, authorization, decisions, and
  transitions.
- [ ] **Partial — checking language.** Define the pure, total, deterministic
  fragment; termination checking; available data; and diagnostic behavior.
- [ ] **Partial — enforcement modes.** Freeze project opt-in, inheritance,
  local draft behavior, protected actions, dependency boundaries, and
  fail-closed behavior.
- [ ] **Partial — evidence lifecycle.** Define identity, attribution,
  freshness, revocation, expiry, replacement, external observations, and
  reproducibility.
- [ ] **Partial — erasure semantics.** Formally preserve types, effects,
  behavior, dependency closure, monitors, assumptions, and debugger behavior
  when verification-only material is removed.
- [ ] **Partial — artifact format.** Freeze canonical serialization, hashes,
  signatures, manifests, BEAM binding, multi-module releases, and verification
  profiles.
- [ ] **Gap — governance identity and trust roots.** Define principals, key
  rotation, delegation, compromised keys, transparency, organizational change,
  and offline verification.
- [ ] **Gap — long-term evolution.** Define schema migration, policy-version
  interpretation, archived evidence, reproducible historical decisions, and
  compatibility with newer compilers.

## 14. Diagnostics, tools, and developer experience

- [ ] **Partial — diagnostic contract.** Define stable identifiers, severity,
  primary and secondary locations, inferred-type presentation, constraint
  provenance, missing-pattern witnesses, guard explanations, and generated-code
  attribution.
- [ ] **Gap — formatter.** Define canonical formatting, comments, idempotence,
  version coupling, and whether formatting is part of source compatibility.
- [ ] **Gap — documentation tool.** Define doc attachment, links, examples,
  doctests, hidden APIs, traits and implementations, effects, laws, and
  specification views.
- [ ] **Gap — interactive environment.** Define REPL typing and effects,
  declaration replacement, process lifetime, module loading, history, and
  governance behavior.
- [ ] **Gap — build system and package manager.** Define project discovery,
  profiles, dependency fetching, code generation, cache keys, offline builds,
  and reproducibility.
- [ ] **Gap — testing tools.** Define unit, property, model, concurrency, and
  specification tests; seeds; shrinking; timeouts; and evidence capture.
- [ ] **Gap — editor protocol.** Define incremental parsing and typing, partial
  programs, completion, hover, rename, formatting, semantic tokens, and stable
  diagnostic identity.
- [ ] **Gap — debugging and observability.** Define breakpoints, stack traces,
  handlers, processes, messages, generated derivations, erased declarations,
  tracing, profiling, and crash reports.
- [ ] **Gap — migration tools.** Define edition fixes, API refactors, deprecated
  syntax handling, and machine-applicable diagnostic edits.

## 15. Security, reproducibility, and operational limits

- [ ] **Gap — trusted computing base.** Enumerate parser, type checker, trait
  solver, effect checker, proof kernel, serializer, signer, runtime, and foreign
  components whose bugs can violate guarantees.
- [ ] **Gap — unsafe-code policy.** Define whether unsafe operations exist,
  where they may appear, what obligations they assume, and how artifacts expose
  them.
- [ ] **Gap — reproducible builds.** Define environmental inputs, timestamps,
  path normalization, dependency integrity, generated files, compiler version,
  and byte-for-byte expectations.
- [ ] **Gap — resource exhaustion.** Define compiler limits, runtime memory and
  mailbox pressure, recursion, unbounded type search, denial-of-service risks,
  and required diagnostics or controls.
- [ ] **Gap — supply-chain policy.** Define package signing, provenance,
  compromised releases, yanks, lockfiles, native dependencies, and governance
  evidence.
- [ ] **Gap — secrets and capabilities.** Define how credentials and ambient VM
  authority enter programs without being hidden by effects, build scripts, or
  specification evaluation.

## 16. Formal validation and release gates

- [ ] **Partial — progress and preservation targets.** State the soundness
  claims for the pure core, rows, traits, effects, pattern matching, guards,
  elaboration, and erasure, with explicit foreign and panic boundaries.
- [ ] **Gap — reference evaluator.** Implement the typed semantic core as an
  executable oracle before production BEAM optimizations obscure behavior.
- [ ] **Gap — differential testing.** Run source programs through the reference
  evaluator and BEAM backend and compare values, effects, failures, traces where
  promised, and resource-scope behavior.
- [ ] **Gap — optimizer validity.** Identify which rewrites rely on pure
  semantics, trait laws, evaluation order, totality, or trusted evidence and
  reject rewrites whose premises are absent.
- [ ] **Gap — compatibility suite.** Test public signatures, data evolution,
  package resolution, artifact manifests, OTP versions, hot upgrades, and
  language editions.
- [ ] **Gap — usability gate.** Test whether programmers can predict `map`,
  `map2`, `and_then`, traversal, handlers, guards, comprehensions, and
  diagnostics without prerequisite mathematical vocabulary.
- [ ] **Gap — performance envelope.** Benchmark direct calls, traits, ADTs,
  pattern matching, guards, comprehensions, effects, processes, erasure, code
  size, compile time, and diagnostic provenance.
- [ ] **Gap — release-readiness definition.** State the minimum normative
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
