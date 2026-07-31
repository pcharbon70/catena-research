---
title: "How Should Catena Preserve Principal Inference While Extending HM?"
kind: inquiry
created: "2026-07-31"
status: open
tags:
  - catena
  - effect-rows
  - hindley-milner
  - principal-types
  - trait-constraints
aliases:
  - "Catena principal inference inquiry"
---

# How Should Catena Preserve Principal Inference While Extending HM?

## Why this matters

Catena describes Hindley–Milner-style inference as its type-theoretic core, but
its promoted language also includes trait constraints, higher-kinded
validation, effect rows, handlers, and first-class resumptions. Each extension
can change whether inference remains complete, principal, coherent, and
terminating.

A precise boundary lets the compiler make honest guarantees, lets tests target
semantic invariants instead of tuple shapes, and prevents experimental effect
or trait machinery from silently weakening the core.

## Operational question

For what explicitly named Catena fragment can the project demonstrate all of
the following?

- every inferred type-and-effect scheme is derivable in a declarative system;
- every typable unannotated term in the fragment is accepted;
- every alternative valid scheme is an instance of the inferred scheme;
- trait evidence is coherent and instance search terminates;
- row unification returns a most-general solution and terminates;
- the generalization rule is sound for strict evaluation, handlers, and
  resumptions;
- the implementation is stable under alpha-renaming and inference traversal
  choices.

If the full promoted surface cannot meet all seven criteria, the answer should
partition it into a principal-inference core and sound annotation-directed
extensions.

## Working hypotheses

1. Catena can preserve complete, principal inference for a rank-1 pure core
   with algebraic data, ordinary higher-kinded constructor variables, and
   first-order row unification.
2. Trait predicates can preserve principal *qualified* types if instance
   entailment, ambiguity, overlap, improvement, and evidence coherence are
   constrained explicitly.
3. Effects can preserve an HM-shaped algorithm only after Catena selects one
   row equality theory and quantifies row variables in the same canonical
   scheme machinery as value-type variables.
4. Strict evaluation and first-class resumptions require either an
   effect-directed generalization rule, a value restriction, or a proof that
   Catena's semantics makes unrestricted generalization sound.
5. Higher-rank terms and polymorphic recursion should remain
   annotation-directed rather than part of complete implicit inference.

## Paths to explore

### Formal model

- Define a declarative judgment for values and effects.
- Define scheme instantiation and generalization over value, constructor, and
  row variables.
- State the substitution and type-scheme generality relations.
- State the trait predicate entailment and evidence equivalence relations.
- State handler typing and the semantics of effect removal and resumptions.

### Current implementation tests

- Construct a captured-environment case that distinguishes `gen(Γ, τ)` from
  `gen(SΓ, Sτ)`.
- Verify constraints from one nested binding are retained or deferred without
  contaminating unrelated schemes.
- Compare expression-level `let` with the monomorphic `check_program` path.
- Exercise a higher-order function whose argument has an open latent effect.
- Exercise generalization of a function containing an effect-row tail.
- Test recursive binding groups and confirm the intended post-group
  generalization boundary.
- Generate ambiguous and overlapping trait evidence cases and compare
  elaborated behavior.

### Reference and differential testing

- Implement a small, clarity-first inferencer for the guaranteed core.
- Generate well-scoped terms and compare alpha-normalized schemes with the
  production compiler.
- Exhaustively compare small-term inference with bounded declarative search.
- Add semantic evaluation checks for state, handlers, and resumption modes.

## Findings

The current synthesis is
[How Hindley–Milner Type Inference Works](../20-notes/hindley-milner-type-inference.md).
It establishes the following starting points:

- Classic W forms a generalized scheme relative to the **substituted**
  environment and freshly instantiates it at every variable use.
- Qualified types can have principal schemes, but coherence and ambiguity are
  extra conditions beyond ordinary unification.
- Koka demonstrates one sound, principal effect-row design; its result depends
  on duplicate-label row equality and effect-directed generalization and does
  not transfer automatically to Catena.
- Catena's committed implementation has recognizable W cases and dedicated
  trait, kind, row, and resumption machinery.
- Static inspection found integration questions around substituted
  environments, constraint ownership, top-level generalization, duplicate
  instantiation paths, and multiple effect representations. The evidence is in
  the [implementation audit](../50-journal/2026-07-31-catena-hm-implementation-audit.md).

## Outcome

Open. The literature supports a layered design, but Catena still needs to name
the guaranteed fragment and resolve or test the implementation boundaries
above. Resolution should produce:

1. a declarative type-and-effect specification;
2. a documented generalization and recursive-group policy;
3. a canonical scheme and row representation;
4. explicit trait solver guarantees; and
5. differential and semantic conformance tests.
