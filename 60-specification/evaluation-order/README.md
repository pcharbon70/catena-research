---
title: "Evaluation Order Specification"
kind: map
created: "2026-08-25"
tags:
  - archive-navigation
  - directory-index
  - evaluation-order
  - specification
aliases:
  - "Catena 0.1.26 evaluation order specification"
---

# Evaluation Order Specification (`60-specification/evaluation-order`)

## Purpose

This directory contains the Catena 0.1.26 contract for evaluation
order: the closed ordered-forms table with its typed-core completions,
the future-form entry rule, the order-versus-structure boundary
against bindings and calls, trace observability with dual-target
agreement, the abstract boundaries, and executable conformance
obligations.

The repository-level [Specification Authority](../../SPECIFICATION-AUTHORITY.md)
controls status, applicability, rendered labels, and conflicts. The
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md) controls
requirement force, invalidity, and variability. The
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md)
policy governs resource disclosure; this area adds no new dimension.

## What belongs here

Put the ordered-forms table, the entry rule, order observability, and
C030 conformance obligations here. The kernel calculus remains C010's,
frozen at its 0.1.8 exact-input boundary. The strictness invariant and
its edition-record gate remain C029's. Scrutinee, condition, clause,
trait traversal, and handler-order details keep their homes in
C002/C003/C004/C005; this area consolidates them at the language
level. Binding structure remains G031's. Arity, currying as typing,
and tail calls remain G032's. Branch forms remain G033's.
Collections, interpolation, and each G040 compound's order entry
remain G040's. Surface syntax remains P109's.

## Variability register

This area introduces no implementation-defined choice, recommendation,
bounded unspecified presentation, or implementation limit. Declared
order is deterministic and observable; no registry or tooling
behavior may vary. Implementations retain only unobservable
within-step freedom, exactly as the kernel's trace semantics draws
it.

## Index

### Subdirectories

- None yet.

### Documents

- [Ordered Forms and Entry Rule](ordered-forms-and-entry-rule.md) —
  the closed table (kernel list elevated plus curried application,
  trait calls, handler installation, and annotate transparency), the
  future-form entry rule, and the G031/G032 boundary.
- [Observability and Trace Agreement](observability-and-trace-agreement.md)
  — order as observable semantics, the trace-equality requirement,
  and dual reference/BEAM agreement.
- [Diagnostics and Conformance](diagnostics-and-conformance.md) — the
  zero-new-families contract, the trace-witness boundaries,
  `EO-OBL-001`–`EO-OBL-008`, evidence sets, and persistence
  separation.

## Maintaining this index

Keep all chapters at one lifecycle status and version. A table, entry
rule, or observability change requires an explicit later semantic
revision. Each G040 compound enters with its order entry in its own
slice. Keep the traceability map, sibling compiler tests,
source-language guides, and this inventory synchronized.
