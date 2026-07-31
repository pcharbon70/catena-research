---
title: "Hindley–Milner Type Inference"
kind: map
created: "2026-07-31"
tags:
  - catena
  - hindley-milner
  - type-inference
aliases:
  - "HM map"
---

# Hindley–Milner Type Inference

## Scope

This map connects the mathematical foundation of principal types, the
mechanics of Algorithm W, the trait and effect extensions relevant to Catena,
and the current project-specific inquiry.

## Start here

- [How Hindley–Milner Type Inference Works](../20-notes/hindley-milner-type-inference.md)
  is the main synthesis: begin here for the algorithm, examples, limits, and
  Catena implications.
- [How should Catena preserve principal inference while extending HM?](../40-inquiries/how-should-catena-preserve-principal-inference.md)
  is the live decision and verification workbench.

## Trails

### Foundations and guarantees

1. [Hindley 1969](../30-sources/hindley-1969-principal-type-scheme.md) introduces
   principal type schemes in combinatory logic.
2. [Milner 1978](../30-sources/milner-1978-type-polymorphism.md) gives the
   programming-language discipline and Algorithm W.
3. [Damas and Milner 1982](../30-sources/damas-and-milner-1982-principal-type-schemes.md)
   proves completeness and principality for the `let`-polymorphic core.

### From proof to implementation

- [Typing Haskell in Haskell](../30-sources/jones-1999-typing-haskell-in-haskell.md)
  makes substitutions, kind-preserving unification, schemes, predicates,
  patterns, and binding groups executable.
- [Catena HM implementation audit](../50-journal/2026-07-31-catena-hm-implementation-audit.md)
  records where those mechanisms appear in the current Erlang code and where
  integration needs testing.

### Traits and evidence

- [A Theory of Qualified Types](../30-sources/jones-1994-theory-of-qualified-types.md)
  extends W with predicates and exposes the added issues of entailment,
  evidence, ambiguity, and coherence.
- [Current Catena type and effect system](../30-sources/catena-2026-type-and-effect-system.md)
  records the project's qualified scheme and instance-resolution surface.

### Effects and generalization

- [Simple Imperative Polymorphism](../30-sources/wright-1995-simple-imperative-polymorphism.md)
  explains why strict effects constrain `let` generalization.
- [Koka's row-polymorphic effects](../30-sources/leijen-2014-koka-row-polymorphic-effects.md)
  demonstrates an HM-shaped alternative based on effect rows and
  effect-directed generalization.

## Open questions

- Which exact Catena fragment promises complete, principal inference?
- What is the canonical equality theory for effect rows?
- Which bindings may generalize type, trait, effect, and resumption variables?
- How are constraints divided between a local scheme and its enclosing scope?
- What termination and coherence rules govern trait evidence?

Track these in the
[principal-inference inquiry](../40-inquiries/how-should-catena-preserve-principal-inference.md).
