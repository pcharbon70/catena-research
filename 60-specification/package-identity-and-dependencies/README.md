---
title: "Package Identity and Dependencies Specification"
kind: map
created: "2026-08-24"
tags:
  - archive-navigation
  - directory-index
  - packages
  - specification
  - versioning
aliases:
  - "Catena 0.1.21 package specification"
---

# Package Identity and Dependencies Specification (`60-specification/package-identity-and-dependencies`)

## Purpose

This directory contains the Catena 0.1.21 contract for package identity
and dependency resolution: the manifest `dependencies` field, the SemVer
2.0.0 version grammar with exact/caret/tilde requirements, single-version
highest-satisfying resolution with conflict rejection, the generated
`catena.lock` with exact-pin replay, registry-neutral bundle-digest
identity with the hex.pm transport profile, stable diagnostics, the
abstract dependency-engine boundary, and executable conformance
obligations.

The repository-level [Specification Authority](../../SPECIFICATION-AUTHORITY.md)
controls status, applicability, rendered labels, and conflicts. The
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md) controls
requirement force, invalidity, and variability. The
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md)
policy governs resource disclosure; this area adds no new dimension.

## What belongs here

Put the dependency declaration form, the version grammar and requirement
operators, resolution and conflict rules, the lockfile format and replay
contract, bundle-digest identity, the Hex transport profile, and C025
conformance obligations here. The package manifest's selection semantics
remain C008's. Component joint digests remain C024's. JCS and SHA-256
remain C006's machinery. Build, fetch, and lock tooling remain G121's.
Supply-chain signing and threat modeling remain G130's. Compatibility
policy, version-skew rules, and re-export facades are subsequently fixed by
C028's. The
prelude remains G026's; entry points are subsequently fixed by C027's.

## Variability register

This area introduces no implementation-defined choice, recommendation,
bounded unspecified presentation, or implementation limit. Bundle digests
and lockfiles are deterministic; no registry behavior may vary.

## Index

### Subdirectories

- None yet.

### Documents

- [Manifest Dependencies and Versions](manifest-dependencies-and-versions.md)
  — the `dependencies` field, package-name spelling, the SemVer 2.0.0
  grammar and precedence, and the exact/caret/tilde requirement operators
  with Cargo-style 0.x semantics and the pre-release matching default.
- [Resolution and Lockfile](resolution-and-lockfile.md) — single-version
  highest-satisfying resolution, order independence, conflict rejection,
  the DAG requirement, the `catena.lock` shape, exact-pin replay, and
  bundle-digest identity with the Hex transport profile.
- [Diagnostics and Conformance](diagnostics-and-conformance.md) — stable
  `PKG001`–`PKG005`, the abstract dependency-engine boundary,
  `PK-OBL-001`–`PK-OBL-012`, evidence sets, the re-export re-ownership
  note, and persistence separation.

## Maintaining this index

Keep all chapters at one lifecycle status and version. A grammar,
operator, resolution, lockfile, or identity change requires an explicit
later semantic revision. Keep the traceability map, sibling compiler
tests, source-language guides, and this inventory synchronized.
