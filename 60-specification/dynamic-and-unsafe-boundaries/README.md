---
title: "Dynamic and Unsafe Boundaries Specification"
kind: map
created: "2026-09-01"
tags:
  - archive-navigation
  - directory-index
  - type-system
  - specification
aliases:
  - "Catena 0.1.43 dynamic and unsafe boundaries specification"
---

# Dynamic and Unsafe Boundaries Specification (`60-specification/dynamic-and-unsafe-boundaries`)

## Purpose

This directory contains the Catena 0.1.43 contract for dynamic and
unsafe boundaries: the five intralanguage exclusions with their
arrival conditions, the foreign visibility routing, and the
conformance obligations.

The repository-level [Specification Authority](../../SPECIFICATION-AUTHORITY.md)
controls status, applicability, rendered labels, and conflicts. The
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md) controls
requirement force, invalidity, and variability. The
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md)
policy governs resource disclosure; this area adds no new dimension.

## What belongs here

Put the intralanguage exclusions, the arrival conditions, the
foreign visibility routing, and C067 conformance obligations here.
The guard fragment remains C003's. Erasure remains C006/C113's.
The failure taxonomy remains C036's. The foreign boundaries —
Erlang terms, foreign calls, NIFs — remain G095/G096/G098's to
implement. The checked advanced type profile remains C068's.

## Variability register

This area introduces no implementation-defined choice,
recommendation, bounded unspecified presentation, or implementation
limit. The exclusions and the routing bind every conforming
implementation identically; no registry or tooling behavior may
vary.

## Index

### Subdirectories

- None yet.

### Documents

- [The Intralanguage Exclusions](the-intralanguage-exclusions.md)
  — no casts, no runtime type inspection, no unchecked
  operations, no intrinsics, no reflection; arrival conditions.
- [The Foreign Visibility Routing](the-foreign-visibility-routing.md)
  — the cross-edge requirement for G095/G096/G098.
- [Dynamic and Unsafe Boundaries Diagnostics and Conformance](diagnostics-and-conformance.md)
  — zero new families, abstract boundaries, and the `DU-OBL-*`
  obligations with evidence sets.

## Maintaining this index

Update this README when a chapter is added, renamed, or archived.
Every direct child belongs in the index. If any excluded form ever
arrives, link the revision that discharged its arrival conditions
here.
