---
title: "Pattern Contexts Specification"
kind: map
created: "2026-08-31"
tags:
  - archive-navigation
  - directory-index
  - patterns
  - specification
aliases:
  - "Catena 0.1.38 pattern contexts specification"
---

# Pattern Contexts Specification (`60-specification/pattern-contexts`)

## Purpose

This directory contains the Catena 0.1.38 contract for pattern
admissibility by context: the three context classes, the
per-context rules and reservations for the five contexts P044
names, the programmable-pattern exclusion closing D046, and the
conformance obligations.

The repository-level [Specification Authority](../../SPECIFICATION-AUTHORITY.md)
controls status, applicability, rendered labels, and conflicts. The
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md) controls
requirement force, invalidity, and variability. The
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md)
policy governs resource disclosure; this area adds no new dimension.

## What belongs here

Put the context classification, the per-context rules and
reservations, and C044 conformance obligations here. Match-clause
coverage and redundancy remain C045's under C002. Generator
grammar, effects, and lowering remain Section 6's (P051). Public
receive grammar remains future work. The failure taxonomy remains
C036's. Handler clause structure remains C005's. `let` structure
remains C031's. Spellings remain P109's.

## Index

### Documents

- [The Three Context Classes](the-three-context-classes.md)
  — the classification principle and match's unchanged authority.
- [Context Rules and Reservations](context-rules-and-reservations.md)
  — the per-context table: let, parameters, generators, public
  receives, handlers, exception clauses, and the D046 exclusion.
- [Pattern Contexts Diagnostics and Conformance](diagnostics-and-conformance.md)
  — zero new families, abstract boundaries, and the `PC-OBL-*`
  obligations with evidence sets.

## Maintaining this index

Update this README when a chapter is added, renamed, or archived.
Every direct child belongs in the index. When a reserved context
gains its own slice, link that slice's area here and record the
consumed reservation.
