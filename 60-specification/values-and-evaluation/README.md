---
title: "Values and Evaluation Specification"
kind: map
created: "2026-08-24"
tags:
  - archive-navigation
  - directory-index
  - values
  - evaluation
  - specification
aliases:
  - "Catena 0.1.25 values specification"
---

# Values and Evaluation Specification (`60-specification/values-and-evaluation`)

## Purpose

This directory contains the Catena 0.1.25 contract for values and
evaluation: the closed value grammar, the non-value list, uniform
first-classness, the strictness invariant with its named exceptions
and edition-record gate, the value-or-trap terminal outcome contract,
the abstract boundaries, and executable conformance obligations.

The repository-level [Specification Authority](../../SPECIFICATION-AUTHORITY.md)
controls status, applicability, rendered labels, and conflicts. The
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md) controls
requirement force, invalidity, and variability. The
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md)
policy governs resource disclosure; this area adds no new dimension.

## What belongs here

Put the value grammar, the non-value list, first-classness, the
strictness invariant, terminal outcomes, and C029 conformance
obligations here. The kernel calculus remains C010's, frozen at its
0.1.8 exact-input boundary. Per-form evaluation order remains P030's.
Bindings, calls, and branching remain G031–G033's. Equality and
ordering remain P035's. The failure taxonomy beyond traps remains
G036's. Allocation observability remains G037's. Compile-time
evaluation remains G038's. Each future type's value status remains
G040's. Surface syntax remains P109's.

## Variability register

This area introduces no implementation-defined choice, recommendation,
bounded unspecified presentation, or implementation limit. Value
classification is deterministic; no registry or tooling behavior may
vary.

## Index

### Subdirectories

- None yet.

### Documents

- [Value Forms and First-Classness](value-forms-and-first-classness.md)
  — the closed ten-form value grammar with Float, the completed
  non-value list, uniform first-classness with named exclusions, and
  the G040 entry rule for future types.
- [Strictness and Terminal Outcomes](strictness-and-terminal-outcomes.md)
  — the language invariant, the `and`/`or` exceptions, the
  edition-record gate for future lazy forms, and the value-or-trap
  terminal contract.
- [Diagnostics and Conformance](diagnostics-and-conformance.md) — the
  zero-new-families contract, the classifier boundaries,
  `VA-OBL-001`–`VA-OBL-008`, evidence sets, and persistence separation.

## Maintaining this index

Keep all chapters at one lifecycle status and version. A grammar,
first-classness, invariant, or terminal change requires an explicit
later semantic revision. Each G040 type enters with its value status
in its own slice. Keep the traceability map, sibling compiler tests,
source-language guides, and this inventory synchronized.
