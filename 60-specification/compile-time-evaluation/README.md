---
title: "Compile-Time Evaluation Specification"
kind: map
created: "2026-08-26"
tags:
  - archive-navigation
  - directory-index
  - compile-time-evaluation
  - specification
aliases:
  - "Catena 0.1.34 compile-time specification"
---

# Compile-Time Evaluation Specification (`60-specification/compile-time-evaluation`)

## Purpose

This directory contains the Catena 0.1.34 contract for compile-time
evaluation: the absence-plus-gate stance for constants, attributes,
and macros; the derivations-as-generation classification; the cited
totality and determinism restriction table; the abstract boundaries;
and executable conformance obligations.

The repository-level [Specification Authority](../../SPECIFICATION-AUTHORITY.md)
controls status, applicability, rendered labels, and conflicts. The
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md) controls
requirement force, invalidity, and variability. The
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md)
policy governs resource disclosure; this area adds no new dimension —
the budgets it cites remain their owning areas'.

## What belongs here

Put the compile-time stance, the derivations classification, the
restriction table, and C038 conformance obligations here. The gate
remains C034's, inherited verbatim. The condition fragment and its
budgets remain C003's. The specification checker remains C006's.
Law checking remains C004's. The derivation engines remain
C002/C004's. Spellings for any future const/macro/attribute surface
remain P109's. Deriving extensions remain G040's, classified under
this area's rules on arrival. Code-generation programs remain
G005/G116's. Build tooling remains G121's.

## Variability register

This area introduces no implementation-defined choice, recommendation,
bounded unspecified presentation, or implementation limit. The stance
and table are deterministic classifications; no registry or tooling
behavior may vary. The cited budgets belong to their areas and are
unchanged.

## Index

### Subdirectories

- None yet.

### Documents

- [The Compile-Time Stance](the-compile-time-stance.md) — the
  absence-plus-gate decision for constants, attributes, and macros,
  and the derivations-as-generation classification.
- [Totality and Determinism Restrictions](totality-and-determinism-restrictions.md)
  — the cited restriction table as the complete set at 0.1.34.
- [Diagnostics and Conformance](diagnostics-and-conformance.md) — the
  zero-new-families contract, the witness boundaries,
  `CE-OBL-001`–`CE-OBL-008`, evidence sets, and persistence
  separation.

## Maintaining this index

Keep all chapters at one lifecycle status and version. A stance,
classification, or table change requires an explicit later semantic
revision. Any arriving evaluator ships total-or-bounded in its own
slice. Keep the traceability map, sibling compiler tests,
source-language guides, and this inventory synchronized.
