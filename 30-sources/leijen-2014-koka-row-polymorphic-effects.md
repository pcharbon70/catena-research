---
title: "Koka: Programming with Row-Polymorphic Effect Types"
kind: source
created: "2026-07-31"
authors:
  - "Daan Leijen"
published: 2014
citation_key: "leijen2014KokaRowEffects"
container: "Electronic Proceedings in Theoretical Computer Science 153: 100–126"
edition: null
isbn: null
doi: "10.4204/EPTCS.153.8"
url: "https://arxiv.org/abs/1406.2061"
accessed: "2026-07-31"
tags:
  - effect-rows
  - effects
  - hindley-milner
  - row-polymorphism
aliases:
  - "Koka row effects"
---

# Koka: Programming with Row-Polymorphic Effect Types

## Reference

Daan Leijen, “Koka: Programming with Row-Polymorphic Effect Types,” *EPTCS*
153 (2014), 100–126. [DOI](https://doi.org/10.4204/EPTCS.153.8) and
[arXiv version](https://arxiv.org/abs/1406.2061).

## Contribution

Leijen extends HM-style inference so expressions synthesize both value types
and effect rows. The system uses open rows and permits duplicate effect labels,
which makes effect elimination inferable without separate lacks constraints.

## Method

The paper presents a formal core calculus, declarative and syntax-directed
typing, an Algorithm W-like inference system, effect-row unification, semantic
soundness properties, and experience from an implementation in Koka.

## Findings

- Effect-polymorphic functions need row variables because the result effect may
  depend on the effects of higher-order arguments.
- Treating rows as multisets with duplicate labels yields principal
  unification for equations that would otherwise have multiple incomparable
  set-row solutions. The alternative design space includes lacks constraints
  or presence/absence flags.
- Handlers or eliminators can remove one occurrence of an effect while a
  handler body contributes another occurrence. Duplicate labels make this
  behavior expressible without forbidding the label in the open tail.
- The inference algorithm remains structurally close to W but generalizes and
  unifies effect variables as well as value-type variables.
- For state safety, the formal system generalizes only total expressions. This
  effect-directed restriction admits more programs than a purely syntactic
  value restriction while rejecting shared-state counterexamples.
- The paper proves soundness and completeness for its chosen calculus and row
  theory; those results depend on the specific row equality and unification
  rules.

## Relevance

This is direct evidence for a greenfield effect-row design. It shows that “add
a row to function types” is insufficient: row equality, duplicate-label or
lacks semantics, tail occurs checks, generalization policy, and handler
subtraction collectively determine principality and soundness.

## Limits

Koka's effects, row equality, state encapsulation, and operational semantics
form one coherent calculus. The paper's proof cannot be transferred to a new
language merely because it also uses the phrase “effect rows.”

## Derived work

- [Hindley–Milner type inference](../20-notes/hindley-milner-type-inference.md)
- [A greenfield type system for Catena](../20-notes/catena-greenfield-type-system.md)
- [Algebraic effects and handlers](../20-notes/algebraic-effects-and-handlers.md)
- [What should a greenfield Catena type system guarantee?](../40-inquiries/what-should-a-greenfield-catena-type-system-guarantee.md)
- [Which algebraic-effect semantics should Catena adopt?](../40-inquiries/which-algebraic-effect-semantics-should-catena-adopt.md)
- [Catena type-system design map](../10-maps/catena-type-system-design.md)
- [Algebraic effects and handlers map](../10-maps/algebraic-effects-and-handlers.md)
