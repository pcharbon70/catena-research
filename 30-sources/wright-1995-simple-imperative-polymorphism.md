---
title: "Simple Imperative Polymorphism"
kind: source
created: "2026-07-31"
authors:
  - "Andrew K. Wright"
published: 1995
citation_key: "wright1995SimpleImperativePolymorphism"
container: "LISP and Symbolic Computation 8: 343–355"
edition: null
isbn: null
doi: "10.1007/BF01018828"
url: "https://www.cs.tufts.edu/~nr/cs257/archive/andrew-wright/imperative-poly.pdf"
accessed: "2026-07-31"
tags:
  - effects
  - let-polymorphism
  - type-soundness
  - value-restriction
aliases:
  - "Wright value restriction"
---

# Simple Imperative Polymorphism

## Reference

Andrew K. Wright, “Simple Imperative Polymorphism,” *LISP and Symbolic
Computation* 8 (1995), 343–355.
[DOI](https://doi.org/10.1007/BF01018828) and
[archived PDF](https://www.cs.tufts.edu/~nr/cs257/archive/andrew-wright/imperative-poly.pdf).

## Research question

How can a strict HM language safely combine `let`-polymorphism with references,
exceptions, and continuations without burdening types with imperative-variable
annotations?

## Method

Wright analyzes the standard polymorphic-reference counterexample, proposes a
syntactic restriction on generalization, relates the restricted system to an
existing sound system, and studies the restriction's effect on a corpus of ML
programs.

## Findings

- Unrestricted generalization is unsound when a `let`-bound computation creates
  shared mutable state. Separate instantiations can then assign incompatible
  types to uses of one shared cell.
- The proposed rule generalizes a `let` binding only when its right-hand side
  is a syntactic value; applications and other expansive computations remain
  monomorphic.
- The rule keeps ordinary HM schemes for both functional and imperative
  implementations of an abstraction, at the cost of rejecting some purely
  functional HM-typable programs.
- The restricted system retains principal inference: translate an expansive
  `let` into lambda application, then run ordinary HM inference.
- Continuations are a particularly direct warning for any language with
  resumable control: duplicating a control-producing computation by the
  reasoning used for polymorphic `let` can change its meaning.

## Relevance

A greenfield language considering algebraic effects must treat generalization
as a semantic soundness boundary, not just a usability preference. It must
either justify unrestricted generalization from its effect discipline or adopt
an explicit restriction.

## Limits

The proposal is intentionally conservative and syntactic. It predates modern
algebraic-effect systems that can use inferred effects to permit more
generalization than a value-only rule. Its empirical corpus is useful but not
a proof that the usability tradeoff will be small in a new language.

## Derived work

- [Hindley–Milner type inference](../20-notes/hindley-milner-type-inference.md)
- [A greenfield type system for Catena](../20-notes/catena-greenfield-type-system.md)
- [What should a greenfield Catena type system guarantee?](../40-inquiries/what-should-a-greenfield-catena-type-system-guarantee.md)
- [Hindley–Milner type inference map](../10-maps/hindley-milner-type-inference.md)
