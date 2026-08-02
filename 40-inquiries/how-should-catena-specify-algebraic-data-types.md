---
title: "How Should Catena Specify Algebraic Data Types?"
kind: inquiry
created: "2026-07-31"
status: resolved
tags:
  - algebraic-data-types
  - catena
  - language-design
  - pattern-matching
  - type-inference
aliases:
  - "Catena algebraic-data-type inquiry"
  - "What Should Catena ADTs Guarantee?"
---

# How Should Catena Specify Algebraic Data Types?

## Why this matters

An algebraic datatype crosses nearly every language boundary: name and kind
resolution, type inference, pattern typing, control flow, module abstraction,
generic derivation, runtime layout, separate compilation, diagnostics, and API
evolution. If those parts infer different meanings from the same declaration,
the apparent simplicity of sums and products becomes a source of unsoundness
or surprise.

The current synthesis proposes a deliberately small ordinary-ADT core. This
inquiry asks how to make that proposal executable and what evidence would
justify each extension.

## Operational question

Can Catena define and implement closed nominal ordinary ADTs such that:

- each declaration introduces a fresh, kind-correct nominal type identity;
- mutually recursive declarations elaborate atomically;
- every constructor has a rank-1 polymorphic scheme with one uniform declared
  result type;
- adding ordinary ADTs is conservative over principal HM inference;
- typed patterns are pure constructor observations with deterministic ordered
  semantics;
- coverage and uselessness checks terminate, understand empty types and module
  visibility, and produce bounded witnesses;
- refutable failure never appears as an implicit runtime exception;
- module signatures precisely control construction and matching authority;
- requested derivations state and satisfy structural preconditions and laws;
- source semantics do not expose default runtime layout; and
- GADTs, structural row variants, views, codata, and stable layouts enter only
  through explicit separate contracts?

## Working hypotheses

1. A fresh nominal identity, explicit parameters, nullary or product-payload
   constructors, and uniform constructor results are enough for the initial
   declaration calculus.
2. Constructor application and matching can reuse rank-1 instantiation and
   unification without weakening HM soundness, completeness, or principality.
3. Non-exhaustive and useless ordinary matches should be errors, with concrete
   witnesses and no implicit `Match` exception.
4. Coverage checking should be a semantic analysis of typed pattern matrices,
   separate from decision-tree generation and bounded against exponential
   cases.
5. Transparent constructor export and fully abstract type export are enough
   for the first module system; selective construction/matching authority can
   be staged.
6. Basic datatype well-formedness need not imply positivity or regularity, but
   structural derivations and induction claims must check those conditions.
7. Only canonical structure-driven operations should be compiler-derived;
   traversal order and evidence status are part of their public contract.
8. The optimizer can select tags, boxes, niches, and wrappers behind opaque
   types; stable ABI or wire layouts need explicit opt-in schemas.
9. Nominal ADTs and structural row variants should remain distinct because
   they offer different identity, openness, inference, and evolution models.
10. Refined constructor results belong to an annotation-directed GADT feature
    with scoped equality evidence, not the principal ordinary-ADT core.

## Paths to explore

### Declaration calculus

- Specify kind headers, fresh nominal generation, constructor identity,
  recursive scope, and atomic mutual groups.
- Decide whether the initial implementation accepts nested and negative
  recursion as opaque payload structure or temporarily restricts declarations
  to a positive regular subset.
- Specify aliases, newtypes, single-constructor products, empty datatypes, and
  any explicit datatype-replication form.
- Define constructor namespaces, qualification, import conflict handling, and
  typed core identities independently of capitalization conventions.

### Type inference and elaboration

- Extend the Algorithm W reference implementation with constructor schemes and
  bidirectional typed-pattern checking.
- Prove or property-test that programs without datatype syntax elaborate as
  before and that uniform-result constructors preserve principal schemes.
- Specify recursive consumer signatures for nested datatypes and reject hidden
  polymorphic recursion with a targeted diagnostic.
- Preserve the separate annotation boundary for higher-rank fields,
  existentials, and GADT branch equalities.

### Match semantics and coverage

- Define scrutinee evaluation, top-to-bottom row selection, bindings, guards,
  or-patterns, literals, and nested patterns in the dynamic semantics.
- Implement Maranget-style usefulness over resolved typed constructor
  matrices, returning missing-pattern and shadowing witnesses.
- Add a terminating inhabitation analysis for empty and recursively empty
  types; remain conservative when inhabitation is unknown.
- Model constructor visibility, open row tails, guards, and later GADT
  equalities explicitly rather than treating all types as closed and inhabited.
- Bound matrix expansion and measure adversarial and real pattern corpora.

### Modules and abstraction

- Specify transparent and abstract datatype components in public signatures.
- Verify that hidden constructors and generated nominal identities cannot leak
  through inference, reflection, serialization, error messages, or derived
  evidence.
- Compare smart constructors and observer functions with selectively public
  patterns on realistic invariant-bearing APIs.
- If considering views, specify totality, effects, failure, evaluation count,
  cost, coverage assertions, and trust before proposing syntax.

### Derivation

- Use the focused
  [combinator inquiry](which-combinators-should-catena-provide-and-derive.md)
  to distinguish class primitives, class-derived functions, datatype-generated
  operations, and advanced recursion or optic libraries.
- Define positivity, variance, regularity, and parameter-role analyses over
  constructor payload types.
- Generate `Setoid`, `Ord`, `Functor`, `Bifunctor`, `Foldable`, `Traversable`,
  and regular folds only when their structural obligations hold.
- State constructor precedence, field order, applicative effect order, and
  constraints in generated public signatures.
- Check generated code in the same typed core as user code and record its
  evidence status for the law system.
- Collect failed derivations to determine whether diagnostics identify the
  exact obstructing occurrence.

### Representation and compatibility

- Define a layout IR that separates source constructors from runtime tags,
  payload packing, recursion indirection, niches, and uniform polymorphic
  boundaries.
- Compare boxed, unboxed, niche, and wrapper-erased layouts on allocation,
  cache behavior, code size, coercions, GC maps, and debugging.
- Make the typed lower-level verifier check every representation coercion and
  exhaustive dispatch after layout selection.
- Specify separate default, stable Catena ABI, foreign ABI, and wire-schema
  contracts before exposing representation attributes.
- Write source compatibility rules for adding constructors, changing payloads,
  changing visibility, derived ordering, and serialized tags.

### Language usability

- Build examples for syntax trees, recursive collections, protocol states,
  error types, abstract invariant-bearing values, empty types, phantom types,
  nested datatypes, and mutually recursive declarations.
- Compare exhaustive errors, wildcard fallbacks, explicit `Option`/`Result`,
  and any proposed partial-match syntax.
- Test whether constructor qualification, missing witnesses, and abstract-type
  errors remain understandable under imports and generated code.
- Measure how often transparent-or-abstract export is insufficient before
  adding selective constructor authority or views.

## Findings

The current synthesis is
[Algebraic Data Types](../20-notes/algebraic-data-types.md). The evidence so far
supports these boundaries:

- finite constructor-built data supplies structural recursion and induction
  cases, but not automatic termination or a model of cyclic graphs;
- an HM-family formal semantics can give datatype declarations fresh nominal
  identity and ordinary polymorphic constructor schemes;
- exhaustiveness and redundancy are two uses of a typed-pattern usefulness
  test, while empty types and richer patterns require extensions to the classic
  inhabited closed-world model;
- hiding constructors preserves invariants and representation independence but
  removes direct constructor matching from the client interface;
- programmable views can restore pattern-shaped observations only by adding
  conversion semantics and trust obligations;
- typed compilation can reconcile specialized unboxed layout with uniform
  polymorphic and abstract boundaries, so source declarations need not freeze
  representation; and
- GADT constructors refine result indices and create local equalities, making
  annotations and a narrower inference contract necessary.

These findings justify a prototype, not a final language specification.

## Outcome

Resolved for version 0.2 by the normative
[Data and Pattern Specification](../60-specification/data-and-patterns/README.md)
and the published compiler evidence in the
[C002 executable conformance record](../50-journal/2026-08-02-c002-executable-data-and-pattern-conformance.md).

The result provides the declaration and dynamic calculus, executable
elaborator, independent typed-core verifier, usefulness checker, three-valued
inhabitation analysis, concrete witnesses, nominal module interfaces,
transparent and abstract constructor tests, explicit generated folds, two
opaque BEAM layouts, a semantic evaluator, and bounded differential evidence.

The investigation changed two initial boundaries deliberately. GADT patterns
and explicit constructor existentials are included behind the C001
annotation-directed profile because leaving them as an unspecified promise
would make the data contract internally incomplete. Recursive declarations
accept any well-kinded payload; positivity and regularity constrain later
derivations rather than basic declaration validity.

Version 0.2 explicitly excludes programmable views, structural variants,
stable external layouts, `non_exhaustive` evolution, categorical instance
generation, and foreign-term validation. Those remain follow-on work rather
than unresolved parts of the normative slice. Promotion is supported by
compiler commit `ae311604ef587a022ce2b7b46599200fcb96a7ab`. The evidence route is retained in the
[Algebraic Data Types map](../10-maps/algebraic-data-types.md), while public
terminology continues in the
[vocabulary inquiry](how-should-catena-expose-mathematical-structure-without-mathematical-jargon.md).
