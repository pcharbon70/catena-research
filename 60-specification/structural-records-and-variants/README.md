---
title: "Structural Records and Variants Specification"
kind: map
created: "2026-08-29"
tags:
  - archive-navigation
  - directory-index
  - records
  - specification
aliases:
  - "Catena 0.1.36 records specification"
---

# Structural Records and Variants Specification (`60-specification/structural-records-and-variants`)

## Purpose

This directory contains the Catena 0.1.36 contract for structural
records and variants: the consolidated operation table, the
kernel-verbatim row typing, the semantic-map representation clause,
the frontend-absence statement, the abstract boundaries, and
executable conformance obligations.

The repository-level [Specification Authority](../../SPECIFICATION-AUTHORITY.md)
controls status, applicability, rendered labels, and conflicts. The
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md) controls
requirement force, invalidity, and variability. The
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md)
policy governs resource disclosure; this area adds no new dimension.

## What belongs here

Put the operation table, the row model, the representation clause,
and C041 conformance obligations here. The kernel calculus remains
C010's, frozen at 0.1.8. Nominal declarations and their exclusions
remain C002's. Evaluation-order rows remain C030's. Variant match
dispatch remains C033's. Record equality remains C035's.
Representation invisibility remains C037's. Collection construction
and update remain G042's. Aliases and newtypes remain G062's.
Refutability by context remains P044's. Spellings and the frontend
path remain P109's.

## Variability register

This area introduces no implementation-defined choice, recommendation,
bounded unspecified presentation, or implementation limit. Record and
variant semantics are deterministic; representation is invisible per
C037; no registry or tooling behavior may vary.

## Index

### Subdirectories

- None yet.

### Documents

- [The Operation Table](the-operation-table.md) — the consolidated
  elevation of the seven operations with cited homes.
- [Rows and Representation](rows-and-representation.md) — the
  kernel-verbatim row model and the semantic-map clause.
- [Diagnostics and Conformance](diagnostics-and-conformance.md) — the
  zero-new-families contract, the kernel-path witness boundaries, the
  frontend-absence clause, `SR-OBL-001`–`SR-OBL-008`, evidence sets,
  and persistence separation.

## Maintaining this index

Keep all chapters at one lifecycle status and version. An operation,
row, or representation change requires an explicit later semantic
revision. Open-record literals, if ever demanded, arrive as a gated
slice. Keep the traceability map, sibling compiler tests,
source-language guides, and this inventory synchronized.
