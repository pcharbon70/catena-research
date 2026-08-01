---
title: "Proving Properties of Programs by Structural Induction"
kind: source
created: "2026-07-31"
authors:
  - "Rod M. Burstall"
published: 1969
citation_key: "burstall1969StructuralInduction"
container: "The Computer Journal 12(1): 41–48"
edition: null
isbn: null
doi: "10.1093/comjnl/12.1.41"
url: "https://academic.oup.com/comjnl/article/12/1/41/311605"
accessed: "2026-07-31"
tags:
  - algebraic-data-types
  - program-verification
  - structural-induction
aliases:
  - "Burstall on structural induction"
---

# Proving Properties of Programs by Structural Induction

## Reference

Rod M. Burstall, “Proving Properties of Programs by Structural Induction,”
*The Computer Journal* 12, no. 1 (1969): 41–48.
[DOI](https://doi.org/10.1093/comjnl/12.1.41),
[publisher record](https://academic.oup.com/comjnl/article/12/1/41/311605), and
[archived paper](https://www.cs.rice.edu/~javaplt/402/14-fall/readings/Burstall.pdf).

## Research question

How can the inductive construction of program data provide a natural proof
principle for recursive functional programs?

## Method

Burstall models structures as finite terms built from atomic objects and a
finite collection of constructors. He defines the proper-constituent relation,
connects its well-foundedness to a generalized induction principle, proposes
syntax for recognizing and decomposing constructed values, and gives two
worked correctness proofs: a tree-sorting algorithm and a compiler for simple
expressions.

## Findings

- Constructor-built finite data carries a well-founded substructure relation:
  every proper constituent was used in constructing the containing value.
- To prove a property for every value, it is enough to prove each constructor
  case assuming the property for its recursive constituents. Nullary
  constructors supply the base cases.
- Structural induction is closely related to recursion induction, but its
  cases mirror the data declaration and often make a program proof easier to
  discover and read.
- A constructor, a recognizer, and component projection can be understood as
  related views of one construction operation. Pattern matching packages this
  recognition-and-decomposition protocol more directly.
- The proof principle depends on finite, well-founded construction. Mutable
  sharing, address identity, and cyclic structures need a different semantic
  account.

## Relevance

An algebraic datatype declaration is not only a runtime layout recipe. It
generates recursion and induction principles. Catena can use that structure to
justify constructor-complete definitions, generated folds, proof obligations,
and property-test decomposition. The source also explains why recursive data
and arbitrary cyclic object graphs must not be conflated.

## Limits

The paper assumes functional programs without assignment or jumps and treats
finite acyclic structures. It predates polymorphic type inference, modules,
modern operational semantics, coinduction, GADTs, and compiler coverage
diagnostics. Structural induction proves a property only after termination and
all semantic premises of the recursive program have been handled.

## Derived work

- [Algebraic Data Types](../20-notes/algebraic-data-types.md)
- [How Should Catena Specify Algebraic Data Types?](../40-inquiries/how-should-catena-specify-algebraic-data-types.md)
- [Algebraic Data Types map](../10-maps/algebraic-data-types.md)
