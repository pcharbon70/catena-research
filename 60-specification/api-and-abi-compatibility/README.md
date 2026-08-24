---
title: "API and ABI Compatibility Specification"
kind: map
created: "2026-08-24"
tags:
  - archive-navigation
  - directory-index
  - compatibility
  - api
  - abi
  - specification
aliases:
  - "Catena 0.1.24 compatibility specification"
---

# API and ABI Compatibility Specification (`60-specification/api-and-abi-compatibility`)

## Purpose

This directory contains the Catena 0.1.24 contract for API and ABI
compatibility: the four compatibility layers with their stances, the
version-increment meanings including what requires a major version,
the strict breaking-change matrix over decoded interfaces, the
declared behavior and BEAM ABI absences, the re-export facade
exclusion, joint-digest and version-skew treatment, stable
diagnostics, the abstract boundaries, and executable conformance
obligations.

The repository-level [Specification Authority](../../SPECIFICATION-AUTHORITY.md)
controls status, applicability, rendered labels, and conflicts. The
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md) controls
requirement force, invalidity, and variability. The
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md)
policy governs resource disclosure; this area adds no new dimension.

## What belongs here

Put compatibility-layer stances, version-increment meanings, the
breaking-change matrix, facade exclusion, entry-set and prelude-bump
classification, digest treatment, compatibility diagnostics, and C028
conformance obligations here. Edition mechanics and per-change
classification remain C008's. Interface content and verification remain
C002's. SemVer grammar, requirement operators, resolution, and lock
replay remain C025's. Entry declarations remain C027's. Migration
engines remain G116/P125's. Registry retirement, yanks, and
compromised versions remain G130's. Hot upgrade remains G092's.
Representation, calling-convention, and foreign-term contracts remain
P093/G094/G095's. Tooling defaults remain G121's.

## Variability register

This area introduces no implementation-defined choice, recommendation,
bounded unspecified presentation, or implementation limit. Diff
classification, claim validation, and diagnostics are deterministic;
no registry or tooling behavior may vary.

## Index

### Subdirectories

- None yet.

### Documents

- [Compatibility Layers and Versions](compatibility-layers-and-versions.md)
  — the four layers' stances, the major-version meaning with the 0.x
  Cargo rule, and source-compatibility rules.
- [Breaking Change Matrix](breaking-change-matrix.md) — the strict
  interface diff matrix, entry-set and prelude classification, digest
  treatment, version skew, and the re-export facade exclusion.
- [Diagnostics and Conformance](diagnostics-and-conformance.md) —
  stable `CMP001`–`CMP003` plus reused families, the abstract
  boundaries across interface decode, diff, and claim validation,
  `CP-OBL-001`–`CP-OBL-010`, evidence sets, and persistence
  separation.

## Maintaining this index

Keep all chapters at one lifecycle status and version. A layer-stance,
matrix, or version-meaning change requires an explicit later semantic
revision. The 1.0-era versioning switch belongs to a future edition
record; layout-stability contracts belong to P093/G094/G095. Keep the
traceability map, sibling compiler tests, source-language guides, and
this inventory synchronized.
