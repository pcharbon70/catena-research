---
title: "Values and Evaluation"
kind: map
created: "2026-08-24"
tags:
  - archive-navigation
  - catena
  - values
  - evaluation
  - strictness
aliases:
  - "Catena values map"
---

# Values and Evaluation

## Scope

This map connects the C010 kernel calculus that fixes the value forms
and strict order, the C005 handler semantics that force resumptions
out of the value class, the C018 Float the kernel grammar predates,
the C029 decision artifacts — the closed ten-form grammar, the
non-value list, uniform first-classness, the strictness invariant with
its edition-record gate, value-or-trap terminals — and the owners of
equality, failure, observability, and future types.

## Start here

- [Catena Values and Evaluation](../20-notes/catena-values-and-evaluation.md)
  develops the closed value grammar, uniform first-classness, the
  strictness invariant, and the terminal-outcome contract.
- [Resolved values inquiry](../40-inquiries/what-are-catenas-values-and-strictness.md)
  records the operational question, hypotheses, and resolution.
- [Values and Evaluation Specification](../60-specification/values-and-evaluation/README.md)
  is the candidate version 0.1.25 contract.
- [Package Identity and Dependencies map](package-identity-and-dependencies.md)
  and the Formal Semantic Kernel area fix the machinery this slice
  elevates.

## Trails

### Foundations that constrain any answer

- [Sequential Dynamics](../60-specification/formal-semantic-kernel/sequential-dynamics.md)
  fixes the kernel's nine value forms, five non-values, and strict
  call-by-value order inside the exact 0.1.8 boundary.
- [Deep Handlers and Affine Resumptions](../60-specification/effects-and-handlers/deep-handlers-and-affine-resumptions.md)
  fix why resumptions are runnable state, never data.
- [Numeric Literal Semantics Specification](../60-specification/numeric-literal-semantics/README.md)
  fixes the Float this slice admits as the tenth value form.
- [Actors, Messages, and Failures](../60-specification/formal-semantic-kernel/actors-messages-and-failures.md)
  fix traps as explicit terminal failures.

### Consumers of the closed grammar

- [Breaking Change Matrix](../60-specification/api-and-abi-compatibility/breaking-change-matrix.md)
  compares interface schemes over value types.
- [Prelude Policy](prelude-policy.md) and [Entry
  Points](entry-points.md) whose guarantees ride decidable value
  semantics.

### Limits and traceability

- [Conformance Traceability](conformance-traceability.md) will
  register `VA-OBL-001` through `VA-OBL-008` against normative anchors
  and sibling compiler tests.
- P030 per-form order, G031–G033 bindings and branching, P035
  equality, G036 failure taxonomy, G037 observability, G038
  compile-time evaluation, G040 future types, and P109 syntax remain
  the future owners.

## Open questions

C029 is complete at revision `0.1.25`. P035 consumes the classifier;
G040 enters each new type with its value status; the edition-record
gate awaits any future lazy form.
