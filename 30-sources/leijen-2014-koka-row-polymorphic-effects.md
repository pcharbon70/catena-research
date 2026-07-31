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

This is the most direct comparison for Catena's effect rows and handlers. It
shows that “add a row to function types” is insufficient: row equality,
duplicate-label or lacks semantics, tail occurs checks, generalization policy,
and handler subtraction collectively determine principality and soundness.

## Limits

Koka's effects, row equality, state encapsulation, and operational semantics
are not identical to Catena's process-backed handlers and `Resumption` values.
The paper's proof cannot be transferred merely because both systems use the
phrase “effect rows.”

## Derived work

- [Hindley–Milner type inference](../20-notes/hindley-milner-type-inference.md)
- [How should Catena preserve principal inference while extending HM?](../40-inquiries/how-should-catena-preserve-principal-inference.md)
- [Catena HM implementation audit](../50-journal/2026-07-31-catena-hm-implementation-audit.md)
