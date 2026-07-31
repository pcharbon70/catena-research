---
title: "What Should a Greenfield Catena Type System Guarantee?"
kind: inquiry
created: "2026-07-31"
status: open
tags:
  - catena
  - language-design
  - principal-types
  - type-inference
aliases:
  - "Catena type-system guarantee inquiry"
  - "How Should Catena Preserve Principal Inference While Extending HM?"
---

# What Should a Greenfield Catena Type System Guarantee?

## Why this matters

A language becomes difficult to reason about when “type inference” sometimes
means a theorem and sometimes means a best-effort solver. Catena needs a public
boundary between programs with complete principal inference and programs that
are checked with explicit type information.

This inquiry starts from no prior Catena specification or implementation. It
asks what contract is worth designing when the language name is the only fixed
input.

## Operational question

What smallest useful Catena can demonstrate all of the following?

- every accepted type-and-effect scheme is derivable in a declarative system;
- every typable unannotated program in the promised core is accepted;
- every alternative core scheme is an instance of the inferred scheme;
- every type, row, trait, and effect solver terminates on well-formed input;
- trait evidence is coherent and ambiguity is rejected;
- generalization is sound for strict evaluation and algebraic handlers;
- inferred results are stable under alpha-renaming and irrelevant solver order;
- elaboration produces a well-typed explicit core term.

For features that cannot meet those criteria implicitly, what annotation
boundary makes checking local, decidable, and understandable?

## Working hypotheses

1. The default fragment should be rank-1 HM with nominal algebraic data,
   pattern matching, and recursive groups generalized only after inference.
2. Unique-label records and variants can be added through kinded rows and lacks
   predicates without introducing subtyping.
3. Single-parameter, non-overlapping traits can retain principal qualified
   schemes when ambiguity, termination, and evidence coherence are explicit.
4. Effect rows should use a separate duplicate-label theory, and expansive
   effectful bindings should remain monomorphic.
5. Predicative higher-rank types belong in bidirectional checking behind
   explicit `forall` signatures.
6. GADTs, polymorphic recursion, multi-parameter traits, and type-level
   equations should be staged or annotation-directed rather than folded into
   the initial inference claim.
7. Public module signatures should be mandatory even when private code is
   inferred.

## Paths to explore

### Formal kernel

- Define the pure expression calculus, strict evaluation, and declarative
  rank-1 typing.
- Implement Algorithm W in a small executable specification.
- Prove substitution, preservation, progress, soundness, completeness, and
  principality for the promised core.
- Define recursive binding groups and public module checking.

### Rows

- Specify record and variant row kinds, equality, lacks predicates, and
  residual-constraint ambiguity.
- Specify effect rows independently, including duplicate labels, open tails,
  handler removal, and canonical display.
- Prove each unifier terminating and most-general under its own equality.

### Traits

- Define dictionary elaboration and observational evidence equivalence.
- Choose instance termination and orphan rules.
- Test whether real libraries need multi-parameter traits; if so, design
  functional dependencies with consistency and coverage checks.
- Reject examples whose apparent meaning depends on overlap or solver order.

### Effects and handlers

- Give operations and handlers an operational semantics before designing their
  surface syntax.
- Test the proposed generalization rule against references, exceptions,
  captured continuations, and state encapsulation.
- Decide whether lexical one-shot resumptions require linear types or can be
  enforced by scope and runtime representation.

### Annotation-directed features

- Prototype predicative higher-rank checking with ordered contexts.
- Measure where annotations are required in representative libraries.
- If considering GADTs, model pattern refinements as scoped implication
  constraints and prohibit generalization under local equalities.

### Language usability

- Compare inferred-signature stability under refactoring.
- Evaluate diagnostics using preserved constraint provenance.
- Test whether separate record, variant, and effect row syntax helps users
  understand their different equality theories.

## Findings

The current synthesis is
[A Greenfield Type System for Catena](../20-notes/catena-greenfield-type-system.md).
The independent literature supports a layered answer:

- classic HM justifies a strong implicit rank-1 core;
- qualified types permit principled traits only when entailment, evidence,
  ambiguity, and coherence are part of the language contract;
- unique structural rows and effect rows need different predicate and equality
  theories;
- strict effects constrain generalization;
- bidirectional checking extends expressiveness without pretending richer
  terms remain part of complete HM inference;
- local equality assumptions can remove principal types, so GADT-like features
  need a deliberately narrower checking contract.

These findings are design recommendations, not yet formal results for Catena.

## Outcome

Open. Resolve this inquiry only when the archive contains:

1. a declarative pure core and executable reference inferencer;
2. a written feature/guarantee matrix in the language specification;
3. separate formal row, trait, and effect solver contracts;
4. a proved or otherwise explicitly bounded generalization rule;
5. an elaborated typed core and independent verifier; and
6. representative programs showing that the annotation boundaries are usable.

The relevant reading routes are collected in the
[Catena Type-System Design map](../10-maps/catena-type-system-design.md).
