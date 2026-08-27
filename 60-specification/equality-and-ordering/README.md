---
title: "Equality and Ordering Specification"
kind: map
created: "2026-08-26"
tags:
  - archive-navigation
  - directory-index
  - equality
  - ordering
  - specification
aliases:
  - "Catena 0.1.30 equality specification"
---

# Equality and Ordering Specification (`60-specification/equality-and-ordering`)

## Purpose

This directory contains the Catena 0.1.30 contract for equality and
ordering: the closed comparable set with structural recursion,
bit-exact float equality and total float ordering, monomorphic
comparison, the frozen guard fragment split, the built-ins-before-
traits boundary, stable diagnostics, the abstract boundaries, and
executable conformance obligations.

The repository-level [Specification Authority](../../SPECIFICATION-AUTHORITY.md)
controls status, applicability, rendered labels, and conflicts. The
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md) controls
requirement force, invalidity, and variability. The
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md)
policy governs resource disclosure; this area adds no new dimension.

## What belongs here

Put the comparable set, float comparison semantics, structural
equality, monomorphism, `EQN001`, and C035 conformance obligations
here. The condition fragment remains C003's, frozen at Int/Bool. The
operator inventory and spellings remain C019's. The value grammar
remains C029's. Numeric literal and coercion rules remain C018's.
Identity observability remains G037's. Handle semantics remain
G084's. Future types' comparability entries remain G040's. Eq/Ord
trait layers remain G061/G101's.

## Variability register

This area introduces no implementation-defined choice, recommendation,
bounded unspecified presentation, or implementation limit. Comparison
is deterministic; no registry or tooling behavior may vary.

## Index

### Subdirectories

- None yet.

### Documents

- [The Comparable Set](the-comparable-set.md) — the closed equality
  and ordering domains with structural recursion, the closure/handle
  exclusion, the G040 entry rule, and monomorphism.
- [Float Equality and Semantics](float-equality-and-semantics.md) —
  bit-exact equality with `−0.0 ≠ 0.0`, total ordering with
  `−0.0 < 0.0`, the no-NaN elevation of C018's contract, and the OTP
  precedent.
- [Diagnostics and Conformance](diagnostics-and-conformance.md) — the
  `EQN001` contract, the guard split, the classifier and operator
  boundaries, `EQ-OBL-001`–`EQ-OBL-008`, evidence sets, and
  persistence separation.

## Maintaining this index

Keep all chapters at one lifecycle status and version. A comparable-
set, float-semantics, or monomorphism change requires an explicit
later semantic revision (and is C028-minor only when additive). Each
G040 type enters with its comparability in its own slice. Keep the
traceability map, sibling compiler tests, source-language guides, and
this inventory synchronized.
