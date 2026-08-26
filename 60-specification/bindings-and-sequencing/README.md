---
title: "Bindings and Sequencing Specification"
kind: map
created: "2026-08-25"
tags:
  - archive-navigation
  - directory-index
  - bindings
  - sequencing
  - specification
aliases:
  - "Catena 0.1.27 bindings specification"
---

# Bindings and Sequencing Specification (`60-specification/bindings-and-sequencing`)

## Purpose

This directory contains the Catena 0.1.27 contract for bindings and
sequencing: non-recursive local binding structure, sequential-lexical
scope with C021 shadowing, the definitions-only recursion boundary,
unused-binding validity with the deny-able `BS001` warning and its
`_`-prefix exemption, the let idiom as the normative sequencing form,
the abstract boundaries, and executable conformance obligations.

The repository-level [Specification Authority](../../SPECIFICATION-AUTHORITY.md)
controls status, applicability, rendered labels, and conflicts. The
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md) controls
requirement force, invalidity, and variability. The
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md)
policy governs resource disclosure; this area adds no new dimension.

## What belongs here

Put binding structure, scope, the recursion boundary, unused-binding
fate, the sequencing idiom, `BS001`, and C031 conformance obligations
here. The kernel calculus remains C010's, frozen at its 0.1.8
exact-input boundary. Shadowing precedence remains C021's. Mutual
recursion among definitions remains C024's. The let and sequence
evaluation schedules remain C030's. Functions, arity, closures, tail
calls, and named local functions remain G032's. Branch forms remain
G033's. Termination remains P034's. Pattern-binding surface forms
remain C002/P109's. Cancellation mid-sequence remains G088's.

## Variability register

This area introduces no implementation-defined choice, recommendation,
bounded unspecified presentation, or implementation limit. Binding
semantics and the `BS001` warning are deterministic; no registry or
tooling behavior may vary.

## Index

### Subdirectories

- None yet.

### Documents

- [Binding Structure and Scope](binding-structure-and-scope.md) — the
  non-recursive `let`, sequential-lexical scope, C021 shadowing
  restated, and the definitions-only recursion boundary with C024 as
  mutual recursion's home.
- [Unused Bindings and Sequencing](unused-bindings-and-sequencing.md)
  — unused-bindings-are-valid with preserved RHS effects, the
  deny-able `BS001` warning with `_`-prefix exemption, and the let
  idiom as the normative sequencing form.
- [Diagnostics and Conformance](diagnostics-and-conformance.md) — the
  `BS001` contract, the witness boundaries, `BS-OBL-001`–`BS-OBL-008`,
  evidence sets, and persistence separation.

## Maintaining this index

Keep all chapters at one lifecycle status and version. A structure,
scope, recursion-boundary, or warning change requires an explicit
later semantic revision. G032's local-function forms build on this
discipline. Keep the traceability map, sibling compiler tests,
source-language guides, and this inventory synchronized.
