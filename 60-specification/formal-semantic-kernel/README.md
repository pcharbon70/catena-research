---
title: "Formal Semantic Kernel Specification"
kind: map
created: "2026-08-06"
tags:
  - concurrency
  - formal-semantics
  - specification
aliases:
  - "Catena 0.1.8 semantic kernel specification"
---

# Formal Semantic Kernel Specification (`60-specification/formal-semantic-kernel`)

## Purpose

This directory contains the normative Catena 0.1.8 contract that composes the
bounded executable subsets of the earlier type, data, condition, trait, and
effect slices into one small-step model. It adds a canonical S-expression
kernel input, structural record and variant terms, explicit traps, and a local
typed-process calculus. Broader constructs of the retained revisions keep
their existing inputs and are not silently re-encoded here.

The repository-level [Specification Authority](../../SPECIFICATION-AUTHORITY.md)
controls status and applicability. The [Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md)
controls requirement force, invalidity, variability, limits, and explicit
runtime failure.
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md)
controls portable minima, finite-resource measurement, evidence-bound
classification, and exhaustion reporting.

## What belongs here

Put only the integrated 0.1.8 kernel grammar, judgments, dynamics, proof
claims, BEAM obligations, and conformance gate here. Full ergonomic source
files, packages, foreign values, cleanup scopes, time, supervision,
distribution, and hot upgrade remain separate checklist work.

## Variability register

| Governing rule | Permitted variability |
| --- | --- |
| [Static Semantics and Elaboration — Normal forms](static-semantics-and-elaboration.md#normal-forms) | Fresh synthesized type-variable and open-tail spelling may differ only by alpha-renaming under the corpus-wide unspecified-presentation rule. |
| [Actors, Messages, and Failures — Opaque process identity](actors-messages-and-failures.md#opaque-process-identity) | Process-handle presentation is opaque; no permitted presentation difference changes equality because 0.1.8 exposes no process equality or inspection. |

No 0.1.8 rule introduces an implementation-defined language choice. The
bootstrap compiler uses the single fixed row layout defined by the BEAM
chapter.

## Index

### Subdirectories

- None yet.

### Documents

- [Overview and Applicability](overview-and-applicability.md) — authority,
  cumulative applicability, scope, and exclusions.
- [Canonical Kernel Syntax](canonical-kernel-syntax.md) — the versioned
  S-expression input and complete bounded grammar.
- [Static Semantics and Elaboration](static-semantics-and-elaboration.md) —
  unified types, effects, rows, evidence, sendability, and typed core.
- [Sequential Dynamics](sequential-dynamics.md) — values, strict order,
  functions, rows, handlers, recursion, and traps.
- [Actors, Messages, and Failures](actors-messages-and-failures.md) — typed
  process entries, mailboxes, global transitions, scheduling, and lifetime.
- [Metatheory](metatheory.md) — named soundness, coherence, preservation, and
  progress claims with bounded evidence expectations.
- [BEAM, Diagnostics, and Conformance](beam-diagnostics-and-conformance.md) —
  fixed representations, public interfaces, diagnostics, limits, and the
  completed promotion record.

## Maintaining this index

Keep all chapters on one version and lifecycle status. Any rule that refines
an earlier slice must cite the earlier heading and state applicability
explicitly. Keep the variability register synchronized with normative `MAY`,
`SHOULD`, and presentation clauses. Preserve the immutable compiler identity
and post-commit evidence linked by the conformance chapter.
