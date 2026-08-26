---
title: "Functions and Calls Specification"
kind: map
created: "2026-08-25"
tags:
  - archive-navigation
  - directory-index
  - functions
  - specification
aliases:
  - "Catena 0.1.28 functions specification"
---

# Functions and Calls Specification (`60-specification/functions-and-calls`)

## Purpose

This directory contains the Catena 0.1.28 contract for functions and
calls: the semantic-unary curried arity model, multi-parameter
desugaring and free partial application, lexical immutable closure
capture, the let-bound local-function form, the elevated
proper-tail-call guarantee, the abstract boundaries, and executable
conformance obligations.

The repository-level [Specification Authority](../../SPECIFICATION-AUTHORITY.md)
controls status, applicability, rendered labels, and conflicts. The
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md) controls
requirement force, invalidity, and variability. The
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md)
policy governs resource disclosure; this area adds no new dimension.

## What belongs here

Put the arity model, application semantics, partial application,
closure capture, local functions, tail calls, and C032 conformance
obligations here. The kernel calculus remains C010's, frozen at its
0.1.8 exact-input boundary. Application evaluation order remains
C030's. Binding structure, non-recursion, and shadowing remain
C031's. Branch forms remain G033's. Termination beyond the tail
guarantee remains P034's. Closure allocation and identity
observability remain G037's. Process-entry tails beyond C010's clause
remain G084's. Calling conventions remain G094's. Surface spellings
remain P109's.

## Variability register

This area introduces no implementation-defined choice, recommendation,
bounded unspecified presentation, or implementation limit. The
function model is deterministic; no registry or tooling behavior may
vary.

## Index

### Subdirectories

- None yet.

### Documents

- [Arity and Application](arity-and-application.md) — the
  semantic-unary model, multi-parameter desugaring, multi-argument
  application under C030's order, free partial application, and the
  named and anonymous forms.
- [Closures and Tail Calls](closures-and-tail-calls.md) — lexical
  immutable capture with G037's exclusion, the let-bound
  local-function form, and the elevated proper-tail-call guarantee
  with its positions enumerated.
- [Diagnostics and Conformance](diagnostics-and-conformance.md) — the
  zero-new-families contract, the witness boundaries,
  `FC-OBL-001`–`FC-OBL-008`, evidence sets, and persistence
  separation.

## Maintaining this index

Keep all chapters at one lifecycle status and version. An arity,
capture, local-function, or tail-rule change requires an explicit
later semantic revision. G094's calling conventions build under this
model's semantics; P109's spellings build over this desugaring. Keep
the traceability map, sibling compiler tests, source-language guides,
and this inventory synchronized.
