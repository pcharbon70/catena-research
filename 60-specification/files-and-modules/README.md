---
title: "Files and Modules Specification"
kind: map
created: "2026-08-21"
tags:
  - archive-navigation
  - directory-index
  - files
  - modules
  - specification
aliases:
  - "Catena 0.1.16 file specification"
---

# Files and Modules Specification (`60-specification/files-and-modules`)

## Purpose

This directory contains the Catena 0.1.16 contract for the file-to-module
relationship: file units and module multiplicity, the `.cat` extension,
file-level module-name spelling and basename verification, generated-file
markers, stable diagnostics, the abstract file-unit resolver boundary, and
executable conformance obligations.

The repository-level [Specification Authority](../../SPECIFICATION-AUTHORITY.md)
controls status, applicability, rendered labels, and conflicts. The
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md) controls
requirement force, invalidity, diagnostic presentation, and variability. The
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md)
policy governs aggregate-input disclosure; this area adds no new resource
dimension and defers aggregate file-size limits to the G129 owner.

## What belongs here

Put file-unit multiplicity, the no-module file class, the source extension,
file-level module-name spelling, basename verification, generated markers,
file-level diagnostics, and C020 conformance obligations here. The concrete
module-header syntax and declaration grammar remain P109. Module-name
resolution, namespaces, and imports remain G021/G022. Package assembly,
cross-file duplicate modules, and directory layout remain G025. Entry
modules are subsequently fixed by C027. Build, cache, and reproducibility policy remain
G121/G128. Module content semantics remain with their existing slices.

## Variability register

This area introduces no implementation-defined choice, recommendation, or
bounded unspecified presentation. It introduces no implementation limit.
Per-token limits of C013–C018 continue to apply to file content; aggregate
file-size and file-count limits remain with the G129 owner and are not
created here.

## Index

### Subdirectories

- None yet.

### Documents

- [File Units and Module Binding](file-units-and-module-binding.md) — the
  `.cat` extension, at-most-one module per file, no-module files,
  ASCII-uppercase module words, and declared-name basename verification.
- [Generated File Markers](generated-file-markers.md) — the exact marker
  comment on C016 forms, first-unit placement, single-marker rule,
  inert-elsewhere rule, and tool-identifier spelling.
- [Diagnostics and Conformance](diagnostics-and-conformance.md) — stable
  `FIL001`–`FIL005`, the abstract resolve boundary, `FU-OBL-001`–
  `FU-OBL-012`, evidence sets, and persistence separation.

## Maintaining this index

Keep all chapters at one lifecycle status and version. A multiplicity,
extension, name-spelling, match, or marker change requires an explicit later
semantic revision. Keep the traceability map, sibling compiler tests,
source-language guides, and this inventory synchronized.
