---
title: "Recursion and Termination Specification"
kind: map
created: "2026-08-26"
tags:
  - archive-navigation
  - directory-index
  - recursion
  - termination
  - specification
aliases:
  - "Catena 0.1.31 recursion specification"
---

# Recursion and Termination Specification (`60-specification/recursion-and-termination`)

## Purpose

This directory contains the Catena 0.1.31 contract for recursion and
termination: the unrestricted program-recursion stance with divergence
as non-termination, the cited separation table for meta-level
evaluators, the entry rule for future recursive-total fragments, the
abstract boundaries, and executable conformance obligations.

The repository-level [Specification Authority](../../SPECIFICATION-AUTHORITY.md)
controls status, applicability, rendered labels, and conflicts. The
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md) controls
requirement force, invalidity, and variability. The
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md)
policy governs resource disclosure; this area adds no new dimension.

## What belongs here

Put the program-recursion stance, the separation table, the G038 entry
rule, and C034 conformance obligations here. The kernel calculus
remains C010's, frozen at 0.1.8. Where recursion lives remains C031's.
The tail guarantee remains C032's. The condition fragment and `CND004`
remain C003's. The 20,000-step checker remains C006's. Bounded laws
remain C004's. Compile-time evaluation design remains G038's, under
this area's gate. The failure taxonomy remains G036's. Cancellation
remains G088's.

## Variability register

This area introduces no implementation-defined choice, recommendation,
bounded unspecified presentation, or implementation limit. The stance
and the table are deterministic classifications; no registry or
tooling behavior may vary. Existing implementation limits (the kernel
reference budget, the specification checker budget) remain their
owning areas'.

## Index

### Subdirectories

- None yet.

### Documents

- [Program Recursion Is Unrestricted](program-recursion-is-unrestricted.md)
  — the elevated stance: recursion free, divergence as non-termination,
  the tail guarantee as the only stack promise, the analysis-only gate.
- [The Separation Table](the-separation-table.md) — the cited
  classification of every meta-level evaluator's regime and the entry
  rule for G038 and future recursive-total fragments.
- [Diagnostics and Conformance](diagnostics-and-conformance.md) — the
  zero-new-families contract, the witness boundaries,
  `RT-OBL-001`–`RT-OBL-008`, evidence sets, and persistence
  separation.

## Maintaining this index

Keep all chapters at one lifecycle status and version. A stance, table
row, or gate change requires an explicit later semantic revision.
G038 arrives total-or-bounded or not at all. Keep the traceability
map, sibling compiler tests, source-language guides, and this
inventory synchronized.
