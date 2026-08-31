---
title: "Collection Construction and Update Specification"
kind: map
created: "2026-08-31"
tags:
  - archive-navigation
  - directory-index
  - collections
  - specification
aliases:
  - "Catena 0.1.37 collections specification"
---

# Collection Construction and Update Specification (`60-specification/collection-construction-and-update`)

## Purpose

This directory contains the Catena 0.1.37 contract for collection
construction and update: the six-topic decision table, the
miss-as-value bounds-failure classification, the complexity
exclusion with its rationale, the abstract boundaries, and
executable conformance obligations.

The repository-level [Specification Authority](../../SPECIFICATION-AUTHORITY.md)
controls status, applicability, rendered labels, and conflicts. The
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md) controls
requirement force, invalidity, and variability. The
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md)
policy governs resource disclosure; this area adds no new dimension.

## What belongs here

Put the six-topic routing, the miss classification, the complexity
exclusion, and C042 conformance obligations here. Collection type
declarations remain G101's under C040's classification. Structural
records remain C041's. The comparable set remains C035's. The
failure taxonomy remains C036's. Representation invisibility remains
C037's. Miss-type contents and collection libraries remain G105's.
Spellings remain P109's.

## Variability register

This area introduces no implementation-defined choice, recommendation,
bounded unspecified presentation, or implementation limit. Collection
semantics ride nominal declarations; complexity is excluded from the
language layer; no registry or tooling behavior may vary.

## Index

### Subdirectories

- None yet.

### Documents

- [The Six-Topic Decision](the-six-topic-decision.md) — the
  per-topic routing table with shipped machinery and named owners.
- [Miss as Value and Complexity](miss-as-value-and-complexity.md) —
  the bounds-failure classification and the complexity exclusion
  with its C037 rationale.
- [Diagnostics and Conformance](diagnostics-and-conformance.md) — the
  zero-new-families contract, the nominal-ADT witness boundaries,
  `CO-OBL-001`–`CO-OBL-008`, evidence sets, and persistence
  separation.

## Maintaining this index

Keep all chapters at one lifecycle status and version. A routing,
classification, or exclusion change requires an explicit later
semantic revision. G101 declares the canonical collections on this
contract. Keep the traceability map, sibling compiler tests,
source-language guides, and this inventory synchronized.
