---
title: "Module Dependency Cycles Specification"
kind: map
created: "2026-08-24"
tags:
  - archive-navigation
  - directory-index
  - modules
  - separate-compilation
  - specification
aliases:
  - "Catena 0.1.20 cycles specification"
---

# Module Dependency Cycles Specification (`60-specification/module-dependency-cycles`)

## Purpose

This directory contains the Catena 0.1.20 contract for module dependency
cycles: strongly-connected-component admission, the two resolution
regimes, joint component digests, the initialization, inference, and
separate-compilation consequence clauses, the dependency-inversion
alternative, the stable `CYC001` diagnostic, and executable conformance
obligations.

The repository-level [Specification Authority](../../SPECIFICATION-AUTHORITY.md)
controls status, applicability, rendered labels, and conflicts. The
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md) controls
requirement force, invalidity, and variability. The
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md)
policy governs resource disclosure; this area adds no new dimension.

## What belongs here

Put cycle admission, the SCC unit, intra-SCC and cross-SCC resolution,
joint digests, the consequence clauses, the inversion alternative, and
C024 conformance obligations here. Digest-bound import admission remains
C022's. Package assembly, lockfiles, and joint-digest compatibility
treatment remain G025/G028's. The concrete recursive `use` surface
remains P109's. Intra-module recursive groups remain C002's. The
pre-declared-interface-files alternative is declined and unowned.

## Variability register

This area introduces no implementation-defined choice, recommendation,
bounded unspecified presentation, or implementation limit. It introduces
one diagnostic family, `CYC001`, and no warning. Joint digest computation
is deterministic and adds no variability.

## Index

### Subdirectories

- None yet.

### Documents

- [SCC Admission and Resolution](scc-admission-and-resolution.md) —
  cycle admission, the maximal-SCC unit, intra-SCC signature resolution,
  cross-SCC digest admission, joint digests, the degenerate acyclic case,
  and the inversion alternative.
- [Checking, Initialization, and Caching](checking-initialization-and-caching.md)
  — the three SCC-adapted consequence clauses and the digest-circularity
  rationale.
- [Diagnostics and Conformance](diagnostics-and-conformance.md) — stable
  `CYC001` for regime mixing and signature gaps, the abstract SCC
  grouping boundary and the concrete compilation boundary,
  `CY-OBL-001`–`CY-OBL-010`, evidence sets, and persistence separation.

## Maintaining this index

Keep all chapters at one lifecycle status and version. Admitting
pre-declared interface files, per-member digests inside an SCC, or joint
inference requires an explicit later semantic revision from the owning
gap — not an edit here. Keep the traceability map, sibling compiler
tests, source-language guides, and this inventory synchronized.
