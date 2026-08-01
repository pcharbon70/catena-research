---
title: "Simple Unification-Based Type Inference for GADTs"
kind: source
created: "2026-07-31"
authors:
  - "Simon Peyton Jones"
  - "Dimitrios Vytiniotis"
  - "Stephanie Weirich"
  - "Geoffrey Washburn"
published: 2006
citation_key: "peytonJonesEtAl2006GadtInference"
container: "ICFP '06: Proceedings of the Eleventh ACM SIGPLAN International Conference on Functional Programming, 50–61"
edition: null
isbn: "1-59593-309-3"
doi: "10.1145/1159803.1159811"
url: "https://www.microsoft.com/en-us/research/publication/simple-unification-based-type-inference-for-gadts/"
accessed: "2026-07-31"
tags:
  - algebraic-data-types
  - gadts
  - pattern-matching
  - type-inference
aliases:
  - "Simple GADT inference"
---

# Simple Unification-Based Type Inference for GADTs

## Reference

Simon Peyton Jones, Dimitrios Vytiniotis, Stephanie Weirich, and Geoffrey
Washburn, “Simple Unification-Based Type Inference for GADTs,” in *ICFP '06:
Proceedings of the Eleventh ACM SIGPLAN International Conference on Functional
Programming* (ACM, 2006), 50–61.
[DOI](https://doi.org/10.1145/1159803.1159811),
[Microsoft Research record](https://www.microsoft.com/en-us/research/publication/simple-unification-based-type-inference-for-gadts/),
and [author-hosted paper](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/dimitris-wobbly.pdf).

## Research question

What predictable annotation discipline can support useful GADT pattern
refinement while remaining a conservative extension of ordinary
Hindley–Milner inference?

## Method

The paper distinguishes *rigid* types fixed by programmer annotations from
*wobbly* types still open to inference. It gives a declarative type system and
a unification-based algorithm, proves soundness and completeness relative to
that chosen system, works through difficult examples, and reports its use in
the Glasgow Haskell Compiler.

## Findings

- A GADT constructor may return a particular instantiation of its datatype,
  such as `Term Int`, rather than the uniform `Term A` result of an ordinary
  parameterized ADT.
- Matching such a constructor introduces a local type equality. The equality
  justifies branch-local operations that are invalid outside that branch.
- Unrestricted inference is difficult because a local equality may admit
  multiple incomparable typings. Programmer annotations identify the rigid
  types that branch refinements may safely rewrite.
- The proposed discipline is sound, predictable, and conservative over HM:
  programs without GADTs retain ordinary inference behavior.
- An algorithm can be complete for a deliberately restricted declarative
  system without claiming completeness for every intuitively typable GADT
  program.

## Relevance

This is the boundary Catena should preserve. Ordinary constructors uniformly
return the declared nominal type and belong in the principal rank-1 fragment.
Refined constructor result types are a separate, annotation-directed GADT
feature whose pattern branches generate scoped equality evidence. Calling both
features “ADT syntax” must not erase that inference distinction.

## Limits

The system is intentionally restrictive and does not accept every program a
more powerful solver might check. The paper does not fully integrate type
classes, modern implication-constraint solving, effect rows, linearity,
dependent pattern matching, or Catena's proposed module discipline.

## Derived work

- [Algebraic Data Types](../20-notes/algebraic-data-types.md)
- [A Greenfield Type System for Catena](../20-notes/catena-greenfield-type-system.md)
- [How Should Catena Specify Algebraic Data Types?](../40-inquiries/how-should-catena-specify-algebraic-data-types.md)
- [Algebraic Data Types map](../10-maps/algebraic-data-types.md)
