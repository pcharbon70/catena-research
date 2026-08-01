---
title: "Structural and Semantic Pattern Matching Analysis in Haskell"
kind: source
created: "2026-08-01"
authors:
  - "Pavel Kalvoda"
  - "Tom Sydney Kerckhove"
published: 2019
citation_key: "kalvodaKerckhove2019StructuralSemanticPatternMatching"
container: "arXiv:1909.04160"
edition: null
isbn: null
doi: "10.48550/arXiv.1909.04160"
url: "https://arxiv.org/abs/1909.04160"
accessed: "2026-08-01"
tags:
  - compilers
  - pattern-matching
aliases:
  - "SMT analysis of Haskell pattern guards"
---

# Structural and Semantic Pattern Matching Analysis in Haskell

## Reference

Pavel Kalvoda and Tom Sydney Kerckhove, “Structural and Semantic Pattern
Matching Analysis in Haskell” (2019), arXiv:1909.04160.
[arXiv record](https://arxiv.org/abs/1909.04160) and
[DOI](https://doi.org/10.48550/arXiv.1909.04160).

## Research question

Can satisfiability solving make guard-aware exhaustiveness and redundancy
diagnostics more precise than structural analysis alone?

## Method

The work adapts an earlier GHC coverage algorithm, records Boolean equalities
arising from guards, translates a supported subset into SMT constraints, and
filters abstract input states through a satisfiability oracle. The authors
implemented a standalone tool and evaluated its behavior on Haskell examples.

## Findings

- Structural analysis can carry guard expressions as opaque constraints while
  remaining sound but imprecise.
- Translating supported Boolean expressions and arithmetic into SMT lets the
  prototype prove cases such as positive/zero/negative integer partitions that
  a simple guard oracle cannot establish.
- Arbitrary source expressions cannot be sent directly to an SMT solver.
  Translation needs an explicit supported theory, with unsupported functions
  remaining opaque.
- Pattern-coverage algorithms have exponential worst cases, and adding a
  solver creates many satisfiability queries. Incremental solving and bounded
  abstractions are implementation concerns, not incidental details.
- The prototype lacks full integration with GHC's type-constraint solver and
  consequently provides only limited GADT support.

## Relevance

This is evidence for a second, optional precision tier in Catena's coverage
checker. A small recognized theory can prove some guards contradictory or
jointly exhaustive, while every unsupported expression falls back to
conservative structural reasoning.

If solver results are allowed to suppress an exhaustiveness error, Catena must
make the trusted boundary explicit. A proof-producing solver or a small
rechecker is preferable to silently trusting a large external solver.

## Limits

The paper reports a prototype rather than a production compiler study. Its
semantics are Haskell-specific, its evaluation is limited, and an arXiv
preprint is not equivalent to a language specification. Solver support can
improve precision but does not make arbitrary guard coverage decidable.

## Derived work

- [Clause Guards](../20-notes/clause-guards.md)
- [How Should Catena Design Clause Guards?](../40-inquiries/how-should-catena-design-clause-guards.md)
- [Clause Guards map](../10-maps/clause-guards.md)
