---
title: "List Comprehensions Specification"
kind: map
created: "2026-08-31"
tags:
  - archive-navigation
  - directory-index
  - comprehensions
  - specification
aliases:
  - "Catena 0.1.39 list comprehensions specification"
---

# List Comprehensions Specification (`60-specification/list-comprehensions`)

## Purpose

This directory contains the Catena 0.1.39 contract for list
comprehensions: the surface contract, the generator and qualifier
rules, evaluation and effect order, the elaboration and
fused-worker boundary, and the conformance obligations with the
`LCP` diagnostic families.

The repository-level [Specification Authority](../../SPECIFICATION-AUTHORITY.md)
controls status, applicability, rendered labels, and conflicts. The
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md) controls
requirement force, invalidity, and variability. The
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md)
policy governs resource disclosure; this area adds no new dimension.

## What belongs here

Put the comprehension grammar's semantic roles and keywords, the
qualifier typing and dynamics, the execution and effect order, the
elaboration contract, and C047 conformance obligations here. The
generator refutability principle is C044's. Evaluation order is
C030's. Bindings are C031's. Pattern coverage is C045's. Nominal
List declarations are G101's. Token-level surface integration is
P109's. Neighboring iteration syntax is D059's.

## Variability register

This area introduces no implementation-defined choice,
recommendation, bounded unspecified presentation, or implementation
limit. Traversal order, failure timing, effect rows, and the
elaboration target are semantic and bind every conforming
implementation identically; no registry or tooling behavior may
vary.

## Index

### Subdirectories

- None yet.

### Documents

- [The Surface Contract](the-surface-contract.md)
  — the grammar's semantic roles and keywords, eager production,
  and the result-type boundary.
- [Generator and Qualifier Rules](generator-and-qualifier-rules.md)
  — sources, traversal, filters, the pattern-generator split, and
  qualifier scope.
- [Evaluation Effects and Execution](evaluation-effects-and-execution.md)
  — exact order, multiplicity, failure timing, effect rows, and the
  sequential-execution rule.
- [Elaboration and Lowering](elaboration-and-lowering.md)
  — the qualifier-tree target, extensional equations, the fused
  worker, cost honesty, and the dormant-adoption boundary.
- [List Comprehensions Diagnostics and Conformance](diagnostics-and-conformance.md)
  — the `LCP` families, the reuse map, and the `LC-OBL-*`
  obligations with evidence sets.

## Maintaining this index

Update this README when a chapter is added, renamed, or archived.
Every direct child belongs in the index. When P109 adopts the
surface tokens, link that adoption here and record which grammar
roles it realized.
