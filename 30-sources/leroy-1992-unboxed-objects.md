---
title: "Unboxed Objects and Polymorphic Typing"
kind: source
created: "2026-07-31"
authors:
  - "Xavier Leroy"
published: 1992
citation_key: "leroy1992UnboxedObjects"
container: "POPL '92: Proceedings of the 19th ACM SIGPLAN-SIGACT Symposium on Principles of Programming Languages, 177–188"
edition: null
isbn: "0-89791-453-8"
doi: "10.1145/143165.143205"
url: "https://xavierleroy.org/publi/unboxed-polymorphism.pdf"
accessed: "2026-07-31"
tags:
  - algebraic-data-types
  - compilation
  - data-representation
  - polymorphism
aliases:
  - "Leroy on unboxed polymorphic objects"
---

# Unboxed Objects and Polymorphic Typing

## Reference

Xavier Leroy, “Unboxed Objects and Polymorphic Typing,” in *POPL '92:
Proceedings of the 19th ACM SIGPLAN-SIGACT Symposium on Principles of
Programming Languages* (ACM, 1992), 177–188.
[DOI](https://doi.org/10.1145/143165.143205) and
[author-hosted paper](https://xavierleroy.org/publi/unboxed-polymorphism.pdf).

## Research question

Can a polymorphically typed functional language use efficient unboxed and
multiword value representations without losing type safety, separate
compilation, or the uniform calling convention required by unknown types?

## Method

Leroy gives source and target calculi, directs representation choices from
typing derivations, inserts coercions where specialized and uniform
representations meet, and proves typing and semantic preservation for the
translation. An implementation in the Gallium compiler is evaluated on
benchmarks.

## Findings

- Static type information can justify specialized representations for known
  products, numbers, and constructor payloads instead of boxing every value.
- Polymorphic code and abstract interfaces require a uniform representation at
  boundaries where the concrete type is unknown.
- Explicit compiler-inserted wrapping and unwrapping can reconcile specialized
  local layout with those uniform boundaries.
- Representation selection can be driven by separately compiled type
  interfaces rather than whole-program analysis.
- Benchmark effects vary: eliminating allocation and indirection helps some
  programs substantially, changes little in others, and can hurt when inserted
  conversions dominate. “Unboxed” is not an unconditional optimization.

## Relevance

An algebraic datatype equation determines values and eliminations, not an ABI.
Catena should leave tags, boxing, payload packing, single-constructor erasure,
niche use, and polymorphic wrappers to a representation phase. Public layout
must remain opaque unless a declaration deliberately opts into a stable
foreign or binary representation.

## Limits

The paper studies an early ML-family compiler, not modern garbage collectors,
cache hierarchies, SIMD, foreign ABIs, recursive unboxing analyses, or
zero-sized and niche representations. Its performance measurements establish
feasibility and tradeoffs, not a universally optimal layout policy.

## Derived work

- [Algebraic Data Types](../20-notes/algebraic-data-types.md)
- [How Should Catena Specify Algebraic Data Types?](../40-inquiries/how-should-catena-specify-algebraic-data-types.md)
- [Algebraic Data Types map](../10-maps/algebraic-data-types.md)
