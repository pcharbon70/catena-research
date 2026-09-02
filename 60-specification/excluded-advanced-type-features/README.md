---
title: "Excluded Advanced Type Features Specification"
kind: map
created: "2026-09-01"
tags:
  - archive-navigation
  - directory-index
  - type-system
  - specification
aliases:
  - "Catena 0.1.44 excluded advanced type features specification"
---

# Excluded Advanced Type Features Specification (`60-specification/excluded-advanced-type-features`)

## Purpose

This directory contains the Catena 0.1.44 contract for the
excluded advanced type features: the seven-form exclusion table,
the seven-point arrival gate as the amendment route, and the
conformance obligations.

The repository-level [Specification Authority](../../SPECIFICATION-AUTHORITY.md)
controls status, applicability, rendered labels, and conflicts. The
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md) controls
requirement force, invalidity, and variability. The
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md)
policy governs resource disclosure; this area adds no new dimension.

## What belongs here

Put the exclusion table, the arrival gate, and C140 conformance
obligations here. The exclusions themselves and the checked
advanced profile remain C001/C068's at `0.1.1`, restated here as
routing rows. The generalization boundary remains C063's. Trait
constraint solving remains C065's. Row semantics remains C064's.
Surface spellings remain P109's.

## Variability register

This area introduces no implementation-defined choice,
recommendation, bounded unspecified presentation, or implementation
limit. The table and the gate bind every conforming implementation
identically; no registry or tooling behavior may vary.

## Index

### Subdirectories

- None yet.

### Documents

- [The Exclusion Table and Gate](the-exclusion-table-and-gate.md)
  — the seven excluded forms and the seven-point arrival gate.
- [Excluded Advanced Type Features Diagnostics and Conformance](diagnostics-and-conformance.md)
  — zero new families, abstract boundaries, and the `EA-OBL-*`
  obligations with evidence sets.

## Maintaining this index

Update this README when a chapter is added, renamed, or archived.
Every direct child belongs in the index. If any excluded form ever
arrives, link the revision that discharged the gate here.
