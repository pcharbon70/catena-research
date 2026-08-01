---
title: "A New Implementation Technique for Applicative Languages"
kind: source
created: "2026-08-01"
authors:
  - "David A. Turner"
published: 1979
citation_key: "turner1979ApplicativeImplementation"
container: "Software: Practice and Experience 9(1): 31–49"
edition: null
isbn: null
doi: "10.1002/spe.4380090105"
url: "https://onlinelibrary.wiley.com/doi/10.1002/spe.4380090105"
accessed: "2026-08-01"
tags:
  - combinatory-logic
  - compilation
  - functional-programming
  - program-transformation
aliases:
  - "Turner's combinator implementation"
---

# A New Implementation Technique for Applicative Languages

## Reference

David A. Turner, “A New Implementation Technique for Applicative Languages,”
*Software: Practice and Experience* 9, no. 1 (1979): 31–49.
[DOI and publisher record](https://doi.org/10.1002/spe.4380090105).

## Contribution

Turner translates a higher-order applicative language into variable-free code
using combinatory logic, then executes that code on a reduction machine. The
work is an implementation use of combinators, distinct from a source library
whose users explicitly call `map`, `fold`, or categorical composition.

## Method

The paper applies bracket abstraction to remove bound variables, describes an
abstract machine for the resulting combinator expressions, and compares the
approach with a conventional interpreter. The evaluation focuses on executing
higher-order functional programs compactly and efficiently on the proposed
machine.

## Findings

- Lambda-bound variables can be eliminated by translating expressions into a
  fixed combinator basis plus program primitives.
- The resulting code is executed by graph-like reduction rather than an
  environment-based evaluator for the original variables.
- A compiler can therefore use combinators as an intermediate representation
  even when the source program is written with ordinary functions and lexical
  binding.
- The paper reports implementation advantages over the interpreter it compares
  against, especially for programs that use higher-order functions heavily.

## Relevance

Catena should reserve terminology carefully. Library combinators describe
source-level composition and carry user-facing laws. Turner's combinators are
compiler terms produced by a variable-elimination transform. A future
categorical or combinatory core may be valuable, but it should be judged by IR
verification, optimization, code size, and diagnostics—not by the usefulness
of the public `Functor` or `Monad` APIs.

## Limits

The implementation and comparison predate modern closure conversion, typed
SSA, native register allocation, garbage collectors, and optimizing functional
compilers. The result does not imply that a combinator IR is the best backend
for Catena, nor that programmers should write in an `S`/`K` basis. The
publisher record and paper establish the historical technique, not a modern
production comparison.

## Derived work

- [Combinators for Algebraic Data and Categorical Programming](../20-notes/combinators-for-algebraic-data-and-categorical-programming.md)
- [Which Combinators Should Catena Provide and Derive?](../40-inquiries/which-combinators-should-catena-provide-and-derive.md)
- [Combinators for Algebraic Data and Categorical Programming map](../10-maps/combinators-for-algebraic-data-and-categorical-programming.md)
