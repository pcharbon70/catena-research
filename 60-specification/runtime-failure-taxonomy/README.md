---
title: "Runtime Failure Taxonomy Specification"
kind: map
created: "2026-08-26"
tags:
  - archive-navigation
  - directory-index
  - failure
  - taxonomy
  - specification
aliases:
  - "Catena 0.1.32 failure specification"
---

# Runtime Failure Taxonomy Specification (`60-specification/runtime-failure-taxonomy`)

## Purpose

This directory contains the Catena 0.1.32 contract for the runtime
failure taxonomy: the single `trap(reason)` outcome with kinded
reasons, the six-category mapping, kernel-verbatim trap
observability, the per-producer entry rule, the abstract boundaries,
and executable conformance obligations.

The repository-level [Specification Authority](../../SPECIFICATION-AUTHORITY.md)
controls status, applicability, rendered labels, and conflicts. The
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md) controls
requirement force, invalidity, and variability. The
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md)
policy governs resource disclosure; this area adds no new dimension.

## What belongs here

Put the single-outcome stance, the kinded-reason model, the
six-category mapping, trap observability, the entry rule, and C036
conformance obligations here. The kernel calculus remains C010's,
frozen at 0.1.8. The terminal contract remains C029's. Divergence and
its exclusion remain C034's. Handler-unhandleability remains C005's.
Option/Result contents remain G105's. Foreign calls remain G095/G096's.
Process death, links, and monitors remain G084's. VM termination
remains G092/G121's. Cancellation remains G088's. Allocation
observability of failure paths remains G037's. Assert/panic spellings
remain P109's.

## Variability register

This area introduces no implementation-defined choice, recommendation,
bounded unspecified presentation, or implementation limit. The
taxonomy is a deterministic classification; no registry or tooling
behavior may vary. Trap-reason spelling follows the reason value's
own value semantics.

## Index

### Subdirectories

- None yet.

### Documents

- [The Single Outcome](the-single-outcome.md) — `trap(reason)` as
  the one runtime failure outcome, the terminal contract restated by
  citation, and kernel-verbatim trap observability.
- [The Six Categories](the-six-categories.md) — the mapping of the
  checklist's categories to classifications and reserved kinds, and
  the per-producer entry rule.
- [Diagnostics and Conformance](diagnostics-and-conformance.md) — the
  zero-new-families contract, the witness boundaries,
  `FT-OBL-001`–`FT-OBL-008`, evidence sets, and persistence
  separation.

## Maintaining this index

Keep all chapters at one lifecycle status and version. A stance,
mapping, or observability change requires an explicit later semantic
revision. Each reserved kind arrives with its producer, classified as
`trap(reason)`. Keep the traceability map, sibling compiler tests,
source-language guides, and this inventory synchronized.
