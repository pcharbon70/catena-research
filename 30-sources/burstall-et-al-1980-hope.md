---
title: "HOPE: An Experimental Applicative Language"
kind: source
created: "2026-07-31"
authors:
  - "Rod M. Burstall"
  - "David B. MacQueen"
  - "Donald Sannella"
published: 1980
citation_key: "burstallEtAl1980Hope"
container: "LFP '80: Proceedings of the 1980 ACM Conference on LISP and Functional Programming, 136–143"
edition: null
isbn: null
doi: "10.1145/800087.802799"
url: "https://www.research.ed.ac.uk/en/publications/hope-an-experimental-applicative-language"
accessed: "2026-07-31"
tags:
  - algebraic-data-types
  - functional-programming
  - pattern-matching
  - polymorphism
aliases:
  - "The HOPE language paper"
---

# HOPE: An Experimental Applicative Language

## Reference

Rod M. Burstall, David B. MacQueen, and Donald Sannella, “HOPE: An
Experimental Applicative Language,” in *LFP '80: Proceedings of the 1980 ACM
Conference on LISP and Functional Programming* (ACM, 1980), 136–143.
[DOI](https://doi.org/10.1145/800087.802799),
[University of Edinburgh record](https://www.research.ed.ac.uk/en/publications/hope-an-experimental-applicative-language),
and [author-hosted paper](https://homepages.inf.ed.ac.uk/dts/pub/hope.pdf).

## Contribution

The paper presents a small typed functional language in which programmers can
declare their own algebraic data, define functions by pattern-indexed recursion
equations, use parametric polymorphism, package common recursion patterns in
higher-order functions, and hide constructors behind module boundaries.

## Method

The authors explain the design through syntax and examples, describe a compiler
to an abstract machine, and report preliminary performance observations. A
complete tree-sort program demonstrates declared recursive data, clausal
matching, higher-order iterators, and an abstract datatype whose internal
constructor is not exported.

## Findings

- A declaration presents a datatype as disjoint constructor alternatives;
  recursive constructor arguments make trees and lists direct user-defined
  types rather than encodings in low-level pairs.
- Constructors work in expressions and patterns. Function equations select a
  case by matching their left-hand-side patterns, and the intended equations
  exhaust the values admitted by the declaration.
- A parameterized declaration such as a list or tree introduces a type
  constructor, while each data constructor receives a polymorphic function
  type into the declared result type.
- Higher-order iterators package recurring forms of recursion, so datatype
  declarations support both explicit structural recursion and reusable generic
  consumers.
- Modules can hide primitive constructors and expose only invariant-preserving
  operations. The tree-sort example hides the internal node constructor; the
  exported insertion operation is therefore not itself usable as a pattern.
- Pattern matching and representation hiding pull in different directions:
  clients can deconstruct exactly the constructors they are allowed to see,
  but hidden representations require an abstract public interface.

## Relevance

HOPE supplies an early integrated programming model for the features Catena
needs to specify together: nominal user-defined data, polymorphic constructors,
clausal pattern matching, structural recursion, and constructor visibility.
The source also keeps *algebraic datatype* distinct from *abstract datatype*:
one describes values by constructors; the other hides an implementation behind
operations. A module may use both techniques at once.

## Limits

The paper is a language-design and implementation report, not a type-safety or
principal-inference proof. Its evaluation is preliminary and tied to an early
abstract-machine implementation. It does not give a modern coverage algorithm,
GADT refinements, row-polymorphic variants, representation optimization, or a
separate-compilation ABI.

## Derived work

- [Algebraic Data Types](../20-notes/algebraic-data-types.md)
- [How Should Catena Specify Algebraic Data Types?](../40-inquiries/how-should-catena-specify-algebraic-data-types.md)
- [Algebraic Data Types map](../10-maps/algebraic-data-types.md)
