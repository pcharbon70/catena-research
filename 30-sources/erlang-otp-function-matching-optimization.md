---
title: "Erlang/OTP Function Matching and Optimization"
kind: source
created: "2026-08-01"
published: null
citation_key: null
container: "Erlang/OTP Efficiency Guide"
edition: null
isbn: null
doi: null
url: "https://www.erlang.org/doc/system/eff_guide_functions.html"
accessed: "2026-08-01"
tags:
  - compilers
  - pattern-matching
aliases:
  - "Erlang function matching efficiency"
---

# Erlang/OTP Function Matching and Optimization

## Reference

Erlang/OTP, “Functions,” *Erlang/OTP Efficiency Guide*, current online edition
accessed 2026-08-01.
[Canonical documentation](https://www.erlang.org/doc/system/eff_guide_functions.html).

The consulted page identified itself as Erlang/OTP 28.0. The guide is living
documentation and may change at the canonical URL.

## Research question

How do clause order and guards constrain the match optimizations performed by
the Erlang compiler?

## Findings

- The guide states that pattern matching in function heads, `case`, and
  `receive` is optimized by the compiler.
- Its worked example shows a broad variable pattern followed by a type-test
  guard. Because that pattern overlaps later literal clauses, the compiler
  must test the guard before it can reach those later clauses.
- Moving all literals together or moving the guarded catch-all clause ahead of
  them permits a better selection structure. The example makes the
  optimization constraint concrete: source-order fallthrough across an
  overlapping guarded clause is observable and must be preserved.
- The guide also shows that compilers can restructure non-overlapping
  structural matches into nested tests without changing the source meaning.

## Relevance

Catena needs a semantic match representation that records ordering and
fallthrough before optimization. A backend may share or reorder constructor
tests, but it cannot move a guard across an overlapping clause merely because
the guard is pure. Purity removes side effects; it does not erase selection
order, divergence, or evaluation cost.

## Limits

This is practical performance guidance rather than a formal compiler
correctness result. It describes Erlang source and its current compiler, not a
required Catena intermediate representation or a benchmark of proposed Catena
lowerings.

## Derived work

- [Clause Guards](../20-notes/clause-guards.md)
- [Clause Guards map](../10-maps/clause-guards.md)
