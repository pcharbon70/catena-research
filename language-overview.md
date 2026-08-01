---
title: "Catena Language Overview"
kind: note
created: "2026-08-01"
maturity: developing
tags:
  - catena
  - language-design
  - program-semantics
aliases:
  - "Catena architecture overview"
---

# Catena Language Overview

Catena is a category theory-inspired functional programming language for the
BEAM VM. Its central design goal is to make reliable composition, explicit
effects, and mathematically grounded abstractions useful to ordinary
programmers without requiring them to learn the formal vocabulary first.

The mathematics belongs in the language's semantics, laws, derivations, and
compiler guarantees. The everyday surface should instead describe recognizable
programming behaviors: mapping values, combining results, sequencing work,
handling requests, checking promises, and composing flows.

This document consolidates the current research into one architectural view.
It is a developing design overview rather than a finished language
specification. Detailed arguments, evidence, and unresolved questions remain in
the linked notes, maps, and inquiries.

## Architecture at a glance

```text
Catena source
    |
    v
Approachable surface language
    |  functions, algebraic data, patterns, traits, effects, specifications
    v
Static semantics
    |  kinds, types, rows, traits, effects, coverage, derivation
    v
Typed elaborated core
    |  explicit dictionaries, capabilities, handlers, and spec references
    |
    +---------------- verification path ----------------+
    |                                                   |
    v                                                   v
Runtime lowering                               Specification graph
    |  effect lowering, optimization               |  evidence, policy,
    |                                               |  authorization, history
    v                                               v
BEAM code                                      Verification result
    |                                                   |
    +---------------- artifact binding -----------------+
                            |
                            v
               .beam modules + signed manifest
```

The architecture separates three concerns that are often conflated:

1. The **surface language** is optimized for comprehension and useful
   diagnostics.
2. The **typed core** makes every abstraction explicit enough for checking,
   elaboration, and compilation.
3. The **artifact model** separates executable runtime obligations from
   verification evidence that can be erased from BEAM code.

## Design principles

### Familiar behavior first

Catena should teach programmers what an abstraction does before exposing its
mathematical name. Documentation and diagnostics may connect an approachable
public term to a formal concept, but formal terminology should not be required
to write ordinary programs. The current vocabulary research is developed in
[An Approachable Vocabulary for Catena](20-notes/approachable-language-vocabulary.md).

### Inference for ordinary code, annotations at complexity boundaries

Ordinary rank-1 code should receive complete Hindley–Milner inference and
principal types. Explicit annotations become necessary when a programmer asks
for higher-rank polymorphism, recursive polymorphism, abstraction boundaries,
or other features whose inference would be unpredictable.

### Mathematical laws are meaningful, but not magical

Traits can state laws and derived operations can depend on them. Merely naming
an implementation does not prove that it obeys those laws, however. Compiler
optimizations should trust laws only when the implementation is built in,
derived by a trusted rule, or accompanied by evidence the compiler can check.
Operational concerns such as evaluation order, effects, strictness, and cost
remain separate contracts.

### Effects remain visible

A function's type should distinguish its returned value from the requests it
may make. Handlers interpret those requests. Capabilities should be lexical and
statically elaborated, avoiding runtime searches for an appropriate handler.

### Governance is opt-in at the project boundary and strict inside its scope

A project does not have to adopt Catena's language-integrated specification and
governance system. Once a declaration or project area is governed, its claims,
evidence requirements, authorization policy, and state transitions are
compiler-visible obligations rather than advisory comments.

### Verification material should not become accidental runtime weight

Proofs, specifications, evidence, and governance history may be checked during
compilation and omitted from generated `.beam` modules when they create no
runtime obligation. Erasure must be justified; tests, approvals, or bounded
checks do not automatically prove that a runtime monitor is unnecessary.

## The language layers

### 1. Surface and usability

The outer layer contains modules, names, expressions, declarations,
annotations, diagnostics, and documentation vocabulary. It should be
expression-oriented, immutable by default, and explicit where program behavior
would otherwise be surprising.

The surface language is responsible for:

- approachable names for common abstractions;
- readable algebraic data declarations and exhaustive pattern matching;
- eager list comprehensions whose iteration, filtering, effects, and mismatch
  behavior are visible in the language contract;
- concise type and effect annotations;
- syntax for declaring and handling effects;
- syntax for traits, implementations, laws, and derived operations;
- specification and governance declarations where a project opts into them;
- diagnostics that explain both the immediate problem and the relevant
  abstraction.

Exact syntax and many public names are still open design questions. The
semantic distinctions below are more settled than their spelling.

### 2. Functional core and type inference

The foundational static type system is a strict, expression-oriented,
rank-1 Hindley–Milner core. Its important initial properties are:

- complete inference and principal types for the ordinary rank-1 fragment;
- let-polymorphism with a generalization discipline compatible with effects;
- structural records and variants described by kinded rows and lacks
  constraints;
- no implicit nominal subtyping;
- coherent traits elaborated into explicit evidence or dictionaries;
- explicit universal quantification and bidirectional checking for
  higher-rank boundaries;
- stable public module signatures as compilation and compatibility contracts.

Pure function types can use the familiar form `A -> B`. An effectful
function needs a distinct form such as `A ->{e} B`, where `e`
describes the permitted requests. Value rows and effect rows are related
techniques but different theories; the compiler should not treat them as one
undifferentiated row mechanism.

The initial language deliberately avoids overlapping or local trait
implementations, inferred polymorphic recursion, unrestricted type-level
functions, implicit subtyping, and first-class resumptions. These exclusions
protect predictability and leave room for later, evidence-driven extensions.
See [A Greenfield Type System for Catena](20-notes/catena-greenfield-type-system.md)
and [Hindley–Milner Type Inference](20-notes/hindley-milner-type-inference.md).

### 3. Algebraic data and patterns

Closed nominal algebraic data types are part of the ordinary inferred
language. Initial constructors should have uniform result types, keeping them
within the Hindley–Milner fragment. Structural row variants remain a separate
tool for open data.

Pattern matching is ordered, pure at the pattern boundary, and checked for
exhaustiveness and redundancy. Diagnostics should provide useful witnesses for
missing cases. A module may hide constructors to preserve an abstract
representation, and the runtime layout of a type is not part of its public
contract unless a separate stable-layout mechanism says so.

The compiler may derive operations when positivity, variance, regularity, and
field order justify the derivation. Generalized algebraic data types,
programmable views, pattern synonyms, and codata are later design spaces, not
features to smuggle into the initial data model. Their effects on inference,
coverage, totality, and evaluation cost must be specified first. See
[Algebraic Data Types](20-notes/algebraic-data-types.md).

[Clause Guards](20-notes/clause-guards.md) develops the condition between a
successful structural pattern and commitment to its body, including purity,
totality, coverage, selective receive, and BEAM lowering.

### 4. Traits and categorical structure

Category-inspired abstractions should be ordinary traits rather than privileged
syntax. The current starting hierarchy contains seventeen concepts:

- value structure: `Setoid`, `Ord`, `Semigroup`, and
  `Monoid`;
- unary structure: `Foldable`, `Functor`, `Apply`,
  `Applicative`, `Chain`, `Monad`, `Extend`,
  `Comonad`, and `Traversable`;
- binary structure: `Bifunctor`;
- composition structure: `Semigroupoid`, `Category`, and
  `Arrow`.

Their relationships matter more than a flat list. For example, ordering builds
on equality; a monoid adds an identity to a semigroup; applicative structure
builds on mapping and application; and traversing combines mapping with
reduction-like structure.

The formal hierarchy is a design commitment under active refinement, while
public names remain experimental. Candidate behavior-first names include
`Mapper`, `Combiner`, `Pipeline`, `Collector`,
`Composable`, and `Flow`. Formal names should remain available in
the semantic reference so experienced readers can recognize the underlying
model. See
[Category Theory for Programming](20-notes/category-theory-for-programming.md).

### 5. Combinators and derived libraries

Most reusable composition belongs in libraries and derivation rather than
syntax. The research proposes five tiers:

1. universal function and data-routing combinators;
2. minimal trait operations plus derived operations;
3. modules derived for particular algebraic data types;
4. focused advanced packages such as optics or recursion schemes;
5. compiler-internal combinators used to implement elaboration and analysis.

Each combinator needs two kinds of contract. Its extensional contract describes
the values it computes and the laws it obeys. Its operational contract
describes evaluation order, strictness, effects, allocation, stack behavior,
and short-circuiting.

Pure mapping remains pure. Effectful traversal should be expressed through a
traversal abstraction, an effect row, or a domain-specific operation rather
than silently changing the meaning of `map`. See
[Combinators for Algebraic Data and Categorical Programming](20-notes/combinators-for-algebraic-data-and-categorical-programming.md).

List comprehensions are a dedicated list control form above this library
vocabulary. Their typed qualifier tree preserves left-to-right, depth-first
evaluation, distinguishes total from filtering patterns, and can lower to
fused tail-recursive workers without making open class dispatch part of their
meaning. See [List Comprehensions](20-notes/list-comprehensions.md).

### 6. Algebraic effects and capabilities

An effect declaration introduces nominal request operations. A function's
effect row records which families of requests it may perform, while a handler
provides an interpretation. The leading initial design uses:

- first-order effect operations;
- open effect rows with a defined policy for repeated labels;
- lexical, statically elaborated capabilities;
- deep handlers;
- affine resumptions that may be abandoned or resumed once;
- clause-scoped, non-escaping resumption values;
- open forwarding for requests a handler does not interpret.

Multi-shot resumptions, shallow handlers, higher-order scoped effects, and
first-class resumption storage are intentionally outside the initial core.
Cleanup, cancellation, task lifetime, and other structured-runtime obligations
need a scope mechanism rather than being modeled solely as ordinary resumable
operations.

The implementation path begins with a small typed handler calculus and a
reference interpreter, then elaborates capabilities and uses a simple
continuation-passing backend. Measurement should determine where selective CPS
or native stack-segment support is worthwhile. See
[Algebraic Effects and Handlers](20-notes/algebraic-effects-and-handlers.md).

### 7. Specifications and governance

Catena's assurance layer treats specifications as typed language artifacts.
Its conceptual model contains:

- a typed graph of claims and their dependencies;
- evidence records distinct from the claims they support;
- authorization policy distinct from truth or proof;
- append-only governance transitions and decision history;
- explicit governed scopes and fail-closed checks for governed actions.

Useful claim forms include needs, promises, invariants, properties, examples,
models, refinement and conformance relationships, attestations, and decisions.
Each form requires a precise meaning; these are not interchangeable ways to
write comments.

Specification expressions should run in a pure, total, and deterministic
checking context. External observations arrive as attributable evidence rather
than hidden compiler effects. A governed package may reject release or another
protected transition when required evidence or authority is missing, while
local drafts may still compile if the declared policy permits them. Governance
does not automatically spread through every dependency.

See
[Language-Integrated Specifications and Governance](20-notes/language-integrated-specifications-and-governance.md).

### 8. Verification erasure and artifact integrity

After checking, the compiler divides specification material into two
categories:

- **verification-only material**, which may be erased; and
- **runtime material**, such as monitors, admission checks, or values the
  executable program actually needs.

A declaration can be well formed without being established. A claim can also
be assumed under an explicit policy without being proved. The compiler and
manifest must preserve these distinctions rather than presenting all accepted
builds as equally verified.

The default release artifact is:

- ordinary `.beam` modules containing the program and any genuinely
  required runtime checks; and
- a signed, content-addressed sidecar manifest containing claims, evidence,
  assumptions, policy decisions, transition records, and the exact digest of
  the BEAM artifacts it describes.

The full specification graph should not be placed in BEAM metadata by default.
An explicit profile may retain selected metadata for debugging or deployment
inspection.

Safe erasure requires preservation of types, effects, observable semantics, and
artifact binding. It also requires checking the transitive closure of runtime
dependencies: a proof term cannot be erased if executable code consumes it.
Provisional modes such as `static`, `monitor`, `assume`,
and `test` may make the intended assurance boundary visible, but their
exact surface design remains open.

## Compiler architecture

The compiler should be organized around explicit intermediate representations
and independently testable analyses.

### Front end

- lexer, parser, and concrete syntax tree;
- name and module resolver;
- kind checker;
- desugaring from approachable surface forms into a smaller semantic language.

### Static semantics

- Hindley–Milner unifier and generalizer;
- record and variant row solver;
- effect-row solver;
- coherent trait solver;
- bidirectional checker for explicit higher-rank types;
- match coverage and redundancy checker;
- guard-safety, totality, and guarded-coverage checker;
- variance, positivity, and derivation analysis;
- public-signature and compatibility checker.

### Elaboration

- trait evidence and dictionary elaborator;
- lexical capability elaborator;
- handler translation;
- typed list-comprehension qualifier-tree elaborator and fused worker
  generator;
- derived-operation generator;
- typed core verifier.

Elaboration is the architectural hinge: friendly source notation becomes a
small typed core in which dependencies that were implicit at the surface are
explicit and auditable.

### Assurance

- specification graph builder and type checker;
- property, model, and proof-obligation generator;
- small proof-certificate checker;
- authorization and policy evaluator;
- append-only transition validator;
- evidence store and manifest generator;
- canonical serializer, digest binder, and signature verifier;
- erasure analysis.

Large or replaceable solvers, test generators, model checkers, and CI
orchestrators can remain outside the trusted core when their output is
rechecked. The trusted base should be small enough to audit and must include
the normative semantics, static checkers, canonical serialization, digest
binding, policy interpretation, transition validation, and signature checks.

### Backend

- typed-core optimizer;
- effect and handler lowering;
- selective continuation transformation where needed;
- BEAM representation and calling-convention selection;
- module and debug metadata emission;
- `.beam` writer and artifact-manifest binder.

The resulting pipeline is:

```text
parse
  -> resolve names and kinds
  -> infer types, rows, traits, and effects
  -> check matches and derivations
  -> elaborate comprehensions, dictionaries, capabilities, and handlers
  -> verify the typed core
  -> split verification and runtime material
  -> check claims, evidence, policy, and transitions
  -> erase verification-only material
  -> lower effects and optimize
  -> emit .beam modules and a bound signed manifest
```

## The BEAM runtime boundary

Catena should use the BEAM where its semantics align with the runtime and add
abstraction only where the language requires stronger guarantees.

- Pure code should compile to ordinary direct calls and data operations.
- Effect handlers should impose overhead primarily on effectful paths.
- Erased specifications should impose no runtime execution cost.
- Runtime monitors and admission hooks remain when policy or semantics require
  them.
- Process identity is not sufficient as organizational or governance identity.
- Governance history must survive compilation and deployment as durable,
  authenticated evidence.
- Hot upgrades need explicit compatibility rules and evidence rather than an
  assumption that a successfully loaded module is semantically safe.

The exact process, supervision, structured-concurrency, foreign-function, and
hot-upgrade models remain important open layers. BEAM fault tolerance is a
runtime foundation, not a substitute for specifying how Catena programs expose
and control concurrency.

## Artifact model

The proposed toolchain produces several conceptually distinct artifacts:

| Artifact | Purpose |
| --- | --- |
| Source modules | Human-authored program, type, effect, trait, and specification declarations |
| Typed core | Explicit semantic record used by the compiler and checkers |
| Verification records | Claims, evidence, assumptions, proofs, policy decisions, and transitions |
| Runtime IR | Only executable values, operations, capabilities, handlers, and required checks |
| BEAM modules | Deployable code and selected runtime/debug metadata |
| Signed manifest | Content-addressed assurance record bound to the exact executable artifacts |

This separation lets a release remain small without severing the evidence that
explains why it was accepted.

## Current commitments

The research currently converges on these decisions:

- a strict functional core with rank-1 principal inference;
- closed nominal algebraic data types plus distinct structural row types;
- exhaustive, pure pattern matching;
- coherent traits with explicit elaboration;
- category-inspired abstractions expressed through ordinary traits and
  libraries;
- nominal algebraic effects with static effect rows and lexical capabilities;
- deep affine handlers as the initial resumption discipline;
- opt-in language-integrated specifications that become enforced within their
  declared scope;
- explicit separation of claims, evidence, authority, and historical
  transitions;
- erasure of verification-only material with a signed sidecar manifest bound
  to generated BEAM code.

These are architecture-level commitments. Syntax, naming, proof rules, and
runtime representation still require validation.

## Open design boundaries

The main unresolved areas are:

- exact surface syntax and behavior-first vocabulary;
- a single formal calculus integrating types, rows, traits, effects, and
  elaboration;
- the evidence model for trait laws and optimizer rewrites;
- effect-row duplication, handler selection, and the production lowering
  strategy;
- processes, supervision, structured concurrency, cancellation, and resource
  scopes;
- modules, packages, foreign calls, stable layouts, and hot upgrades;
- governance identity, revocation, transparency logs, and long-lived evidence;
- the proof kernel and interchange format for externally produced
  certificates;
- usability studies and performance measurements;
- later features such as GADTs, multi-shot handlers, programmable views,
  pattern synonyms, generic or streaming comprehensions, optics syntax, and
  recursion schemes.

An open boundary should not be mistaken for an invitation to choose features
independently. Each proposal must be checked against principal inference,
effect visibility, operational cost, BEAM behavior, diagnostics, and the goal
of keeping the language approachable.

## Research routes

The [home map](10-maps/home.md) remains the entry point to the complete archive.
The following maps provide the evidence trails behind this overview:

- [Approachable Catena Language Design](10-maps/approachable-catena-language-design.md)
  connects vocabulary, diagnostics, and progressive disclosure.
- [Catena Type-System Design](10-maps/catena-type-system-design.md) connects
  inference, rows, traits, effects, and higher-rank boundaries.
- [Algebraic Data Types](10-maps/algebraic-data-types.md) connects data
  declarations, pattern semantics, representation, and staged extensions.
- [Category Theory for Programming](10-maps/category-theory-for-programming.md)
  connects the initial trait hierarchy and its laws.
- [Combinators for Algebraic Data and Categorical Programming](10-maps/combinators-for-algebraic-data-and-categorical-programming.md)
  connects the proposed reusable operation tiers.
- [List Comprehensions](10-maps/list-comprehensions.md) connects surface
  iteration, pattern coverage, effects, algebraic explanation, and BEAM
  lowering.
- [Algebraic Effects and Handlers](10-maps/algebraic-effects-and-handlers.md)
  connects effect semantics, typing, capability elaboration, and BEAM lowering.
- [Language-Integrated Specifications and Governance](10-maps/language-integrated-specifications-and-governance.md)
  connects specifications, evidence, policy, history, and erasure.
