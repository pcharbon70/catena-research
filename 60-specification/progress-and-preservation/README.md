---
title: "Progress and Preservation Specification"
kind: map
created: "2026-09-01"
tags:
  - archive-navigation
  - directory-index
  - metatheory
  - specification
aliases:
  - "Catena 0.1.45 progress and preservation specification"
---

# Progress and Preservation Specification (`60-specification/progress-and-preservation`)

## Purpose

This directory contains the Catena 0.1.45 contract for the
remaining progress and preservation targets: the effects-and-
failure target statements, the composed integrated theorem with
its routed proof obligation, the conditional process and foreign
extensions, and the conformance obligations.

The repository-level [Specification Authority](../../SPECIFICATION-AUTHORITY.md)
controls status, applicability, rendered labels, and conflicts. The
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md) controls
requirement force, invalidity, and variability. The
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md)
policy governs resource disclosure; this area adds no new dimension.

## What belongs here

Put the effects-and-failure targets, the composed integrated
theorem, the conditional extensions, and C132 conformance
obligations here. The data-era targets remain C002's, the
condition-era targets C003's, and the kernel targets C010's —
restated here as composition parts, not amended. The resumption
discipline remains C005's. The failure terminal remains C036's.
The trace-agreement methodology remains C030's. Public processes
remain G084/G085's and foreign values G095/G096's to ship.

## Variability register

This area introduces no implementation-defined choice,
recommendation, bounded unspecified presentation, or implementation
limit. The targets and conditionals bind every conforming
implementation identically; no registry or tooling behavior may
vary.

## Index

### Subdirectories

- None yet.

### Documents

- [The Effects and Failure Targets](the-effects-and-failure-targets.md)
  — handler-calculus preservation and progress with `trap` as the
  failure terminal.
- [The Integrated Theorem](the-integrated-theorem.md)
  — the composed statement, the composition lemma, and the
  conditional process and foreign extensions.
- [Progress and Preservation Diagnostics and Conformance](diagnostics-and-conformance.md)
  — zero new families, abstract boundaries, and the `PP-OBL-*`
  obligations with evidence sets.

## Maintaining this index

Update this README when a chapter is added, renamed, or archived.
Every direct child belongs in the index. When the composition
lemma is discharged or a conditional extension activates, link the
discharging revision here.
