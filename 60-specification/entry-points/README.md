---
title: "Entry Points Specification"
kind: map
created: "2026-08-24"
tags:
  - archive-navigation
  - directory-index
  - entry-points
  - specification
aliases:
  - "Catena 0.1.23 entry points specification"
---

# Entry Points Specification (`60-specification/entry-points`)

## Purpose

This directory contains the Catena 0.1.23 contract for entry points and
application structure: the manifest `entries` declaration, the derived
library/executable distinction, effect-closed entry validity, the
one-launch-marker rule, invocation-only startup, return-is-shutdown
results, stable diagnostics, the abstract boundaries, and executable
conformance obligations.

The repository-level [Specification Authority](../../SPECIFICATION-AUTHORITY.md)
controls status, applicability, rendered labels, and conflicts. The
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md) controls
requirement force, invalidity, and variability. The
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md)
policy governs resource disclosure; this area adds no new dimension.

## What belongs here

Put entry declarations, library derivation, effect-closure validation,
launch semantics, shutdown results, entry diagnostics, and C027
conformance obligations here. Manifest framing and selection remain
C008's. Manifest optional-field structure remains C025's. Name
resolution, precedence, and import admission remain C021/C022's.
Evaluation order, completion, and trap semantics remain C010's.
Supervision, restart, and process lifetime remain G084/G089's.
Cancellation and deadlines remain G088's. The CLI and host-process
boundary remain G121's. Compatibility meanings of entry-set changes
are subsequently fixed by C028's.

## Variability register

This area introduces no implementation-defined choice, recommendation,
bounded unspecified presentation, or implementation limit. Entry
validation, launch, and reports are deterministic; no registry or
tooling behavior may vary.

## Index

### Subdirectories

- None yet.

### Documents

- [Entry Declarations](entry-declarations.md) — the manifest `entries`
  field, entry validity (existing zero-argument effect-closed export,
  recorded result type), the one-launch-marker rule, and the derived
  library/executable distinction.
- [Startup and Shutdown](startup-and-shutdown.md) — invocation-only
  launch under strict kernel semantics, return-is-shutdown results, the
  failure report, and the explicitly excluded runtime machinery.
- [Diagnostics and Conformance](diagnostics-and-conformance.md) — stable
  `ENT001`–`ENT003` plus reused families, the abstract boundaries across
  manifest decode, package validation, and launch, `EN-OBL-001`–`EN-OBL-010`,
  evidence sets, and persistence separation.

## Maintaining this index

Keep all chapters at one lifecycle status and version. An entry-shape,
closure, launch, or report change requires an explicit later semantic
revision. Supervision-era extensions remain G084/G089 work over this
mechanism. Keep the traceability map, sibling compiler tests,
source-language guides, and this inventory synchronized.
