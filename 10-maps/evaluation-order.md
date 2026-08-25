---
title: "Evaluation Order"
kind: map
created: "2026-08-25"
tags:
  - archive-navigation
  - catena
  - evaluation-order
aliases:
  - "Catena evaluation order map"
---

# Evaluation Order

## Scope

This map connects the C010 kernel backbone that fixes strict
left-to-right order for its form list, the C002/C003/C004/C005
fragments that complete scrutinee, condition, trait, and handler
order, C029's strictness invariant above them all, the C030 decision
artifacts — the closed ordered-forms table with typed-core
completions, the entry rule, trace observability — and the owners of
bindings, future forms, and syntax.

## Start here

- [Catena Evaluation Order](../20-notes/catena-evaluation-order.md)
  develops the ordered-forms table, the typed-core completions, the
  entry rule, and trace observability.
- [Resolved order inquiry](../40-inquiries/when-does-each-subexpression-evaluate.md)
  records the operational question, hypotheses, and resolution.
- [Evaluation Order Specification](../60-specification/evaluation-order/README.md)
  is the normative version 0.1.26 contract.
- [C030 evidence record](../50-journal/2026-08-25-c030-evaluation-order.md)
  records the dual-target trace evidence and verification.
- [Values and Evaluation map](values-and-evaluation.md) — the
  trilogy's first stop: the invariant this table schedules.

## Trails

### Foundations that constrain any answer

- [Sequential Dynamics](../60-specification/formal-semantic-kernel/sequential-dynamics.md)
  fixes the kernel's ordered-forms list, left-first binaries, and the
  two skips inside the exact 0.1.8 boundary.
- [Operational Semantics](../60-specification/traits-and-categorical-operations/operational-semantics.md)
  fixes trait subject order and callback positions.
- [Deep Handlers and Affine Resumptions](../60-specification/effects-and-handlers/deep-handlers-and-affine-resumptions.md)
  makes handler order observable and fixes resumed-prefix order.
- [Strictness and Terminal Outcomes](../60-specification/values-and-evaluation/strictness-and-terminal-outcomes.md)
  fixes the invariant above the table and its edition-record gate.

### Evidence

- The C005 reference/BEAM trace-agreement tests are the dual-target
  template; the [Structural Operational Semantics
  note](../30-sources/plotkin-2004-structural-operational-semantics.md)
  supplies the transition-system method behind both machines.

### Limits and traceability

- [Conformance Traceability](conformance-traceability.md) registers
  `EO-OBL-001` through `EO-OBL-008` against normative anchors and
  immutable sibling compiler evidence.
- G031–G033 bindings, calls, and branching; P035 equality; G036
  failure; G040 collections and interpolation entry; G088
  cancellation; and P109 syntax remain the future owners.

## Open questions

C030 is complete at revision `0.1.26`. G040 enters each new compound
with its table entry; the edition-record gate awaits any future
exception; G031 completes the trilogy.
