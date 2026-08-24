---
title: "Imports and Exports Specification"
kind: map
created: "2026-08-22"
tags:
  - archive-navigation
  - directory-index
  - exports
  - imports
  - specification
aliases:
  - "Catena 0.1.18 import specification"
---

# Imports and Exports Specification (`60-specification/imports-and-exports`)

## Purpose

This directory contains the Catena 0.1.18 contract for imports and
exports: explicit private-by-default export declarations with type
transparency modes, import admission through qualification plus explicit
name lists, declared exclusions of wildcards, renaming, and re-exports,
export-set validation, the deny-able unused-import warning, stable
diagnostics, the abstract event boundary, and executable conformance
obligations.

The repository-level [Specification Authority](../../SPECIFICATION-AUTHORITY.md)
controls status, applicability, rendered labels, and conflicts. The
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md) controls
requirement force, invalidity, warning presentation, and variability. The
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md)
policy governs aggregate-input disclosure; this area adds no new resource
dimension.

## What belongs here

Put export declaration semantics and visibility defaults, import
admission and export-set validation, the declared exclusions, unused
import analysis, import/export diagnostics, and C022 conformance
obligations here. Module recursion and initialization order are admitted by the normative 0.1.20
[Module Dependency Cycles](../module-dependency-cycles/README.md) area.
Package identity, re-export assembly, lockfiles, and duplicate-module
rejection remain G025. Prelude contents and opt-out remain G026. Entry
modules are subsequently fixed by C027. Interface digest verification remains C006/C008 —
this layer consumes digests as opaque identity. The concrete
`use`/`export` surface punctuation remains P109.

## Variability register

This area introduces no implementation-defined choice and no bounded
unspecified presentation. It introduces one deny-able warning, `IMP001`,
through the existing C008 warning machinery. It introduces no
implementation limit; export-set validation remains subject to the
aggregate-input policy of the G129 owner.

## Index

### Subdirectories

- None yet.

### Documents

- [Export Declarations and Visibility](export-declarations-and-visibility.md)
  — the private-by-default rule, per-category export events, type
  transparency modes, undeclared-export rejection, and interface
  reflection.
- [Import Declarations and Admission](import-declarations-and-admission.md)
  — module admission with qualification rights, explicit name lists and
  the qualified-only empty form, export-set validation, the declared
  exclusions, and C021 precedence interaction.
- [Diagnostics and Conformance](diagnostics-and-conformance.md) — stable
  `IMP001` (warning) and `IMP002`–`IMP003`/`EXP001` (errors), the
  abstract event boundary and unused-import analysis, `IM-OBL-001`–
  `IM-OBL-013`, evidence sets, and persistence separation.

## Maintaining this index

Keep all chapters at one lifecycle status and version. A visibility
default, admission rule, exclusion, or diagnostic change requires an
explicit later semantic revision. Keep the traceability map, sibling
compiler tests, source-language guides, and this inventory synchronized.
