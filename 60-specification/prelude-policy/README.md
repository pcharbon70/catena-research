---
title: "Prelude Policy Specification"
kind: map
created: "2026-08-24"
tags:
  - archive-navigation
  - directory-index
  - prelude
  - specification
aliases:
  - "Catena 0.1.22 prelude specification"
---

# Prelude Policy Specification (`60-specification/prelude-policy`)

## Purpose

This directory contains the Catena 0.1.22 contract for the prelude: the
manifest `prelude` selection, admission as an ordinary import-class
origin under unchanged C021 precedence, absent/`null` opt-out, the
zero-implicit-names edition guarantee, dependency resolution and
lockfile treatment of prelude selections, stable diagnostics, the
abstract boundaries, and executable conformance obligations.

The repository-level [Specification Authority](../../SPECIFICATION-AUTHORITY.md)
controls status, applicability, rendered labels, and conflicts. The
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md) controls
requirement force, invalidity, and variability. The
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md)
policy governs resource disclosure; this area adds no new dimension.

## What belongs here

Put prelude selection, admission and precedence, opt-out, the edition
guarantee, prelude diagnostics, and C026 conformance obligations here.
Name resolution and precedence remain C021's. Import admission and its
diagnostics remain C022's. Package identity, requirement resolution,
and lockfile semantics remain C025's. Prelude contents and the name
freeze remain G101's. Collection protocols remain P102's. Tooling
scaffolding remains G121's. Entry points are subsequently fixed by C027. Compatibility
meanings of prelude version bumps are subsequently fixed by C028/G136's.

## Variability register

This area introduces no implementation-defined choice, recommendation,
bounded unspecified presentation, or implementation limit. Prelude
admission and lock treatment are deterministic; no registry or tooling
behavior may vary.

## Index

### Subdirectories

- None yet.

### Documents

- [Prelude Selection and Admission](prelude-selection-and-admission.md)
  — the manifest `prelude` field, one-selection rule, origin injection
  at import precedence, package identity via C025, and resolution into
  environments.
- [Shadowing, Opt-Out, and the Edition Guarantee](shadowing-optout-and-edition-guarantee.md)
  — the executed C021 precedence table, absent/`null` opt-out, the
  zero-implicit-names guarantee, and the lifecycle-record path for any
  future edition default.
- [Diagnostics and Conformance](diagnostics-and-conformance.md) — stable
  `PRE001` plus reused families, the abstract boundaries across
  manifest, environment builder, and dependency resolution,
  `PL-OBL-001`–`PL-OBL-010`, evidence sets, and persistence separation.

## Maintaining this index

Keep all chapters at one lifecycle status and version. A selection,
admission, precedence, opt-out, or guarantee change requires an explicit
later semantic revision. Freezing contents is G101's work on this
mechanism. Keep the traceability map, sibling compiler tests,
source-language guides, and this inventory synchronized.
