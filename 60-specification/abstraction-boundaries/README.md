---
title: "Abstraction Boundaries Specification"
kind: map
created: "2026-08-23"
tags:
  - abstraction
  - archive-navigation
  - directory-index
  - specification
aliases:
  - "Catena 0.1.19 abstraction specification"
---

# Abstraction Boundaries Specification (`60-specification/abstraction-boundaries`)

## Purpose

This directory contains the Catena 0.1.19 contract for the abstraction
boundary: the declared exclusion of stable-layout opt-in, the declared
completeness of the binary constructor-authority vocabulary, the
sanctioned smart-constructor-over-abstract-type invariant idiom with its
coverage consequence, and executable conformance obligations.

The repository-level [Specification Authority](../../SPECIFICATION-AUTHORITY.md)
controls status, applicability, rendered labels, and conflicts. The
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md) controls
requirement force, invalidity, and variability. The
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md)
policy governs resource disclosure; this area adds no new dimension.

## What belongs here

Put the boundary-level exclusions, the sanctioned invariant idiom, and
C023 conformance obligations here. The layout-free interface contract,
both-layout conformance, and `L001` remain C002's. The transparent and
abstract export modes and their validation remain C022's. Any
layout-stability or ABI contract is subsequently fixed by C028's
declared absence. Views, pattern synonyms,
and selective construction/matching exposure remain D046/G040's. BEAM
representation mapping remains P093's. Foreign-term validation remains
G095's.

## Variability register

This area introduces no implementation-defined choice, recommendation,
bounded unspecified presentation, or implementation limit. It introduces
no new diagnostic: exclusions surface through existing `EXP001`,
C002 coverage diagnostics, and invalid-event rejection.

## Index

### Subdirectories

- None yet.

### Documents

- [Authority and Representation Exclusions](authority-and-representation-exclusions.md)
  — the complete binary authority vocabulary, the stable-layout exclusion
  with its C028 resolution, and the selective-exposure and views exclusions
  with their D046/G040 owners.
- [Smart-Constructor Idiom and Conformance](smart-constructor-idiom-and-conformance.md)
  — the sanctioned invariant pattern over abstract types, its coverage
  consequence, `AB-OBL-001`–`AB-OBL-007`, evidence sets, and persistence
  separation.

## Maintaining this index

Keep all chapters at one lifecycle status and version. Admitting a
stable-layout contract, a third authority mode, or views requires an
explicit later semantic revision from the owning gap — not an edit here.
Keep the traceability map, sibling compiler tests, source-language
guides, and this inventory synchronized.
