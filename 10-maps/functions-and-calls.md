---
title: "Functions and Calls"
kind: map
created: "2026-08-25"
tags:
  - archive-navigation
  - catena
  - functions
  - currying
  - tail-calls
aliases:
  - "Catena functions map"
---

# Functions and Calls

## Scope

This map connects the C010 kernel rules that fix closures, repeated
unary application, and the proper-tail-call guarantee, the backend
chapter that preserves tail position on both lowering paths, C030's
application-order rows, C031's binding discipline that local
functions inherit, the C032 decision artifacts — semantic-unary
currying, free partial application, lexical immutable capture,
let-bound local functions, the elevated tail guarantee — and the
owners of branching, termination, allocation, and syntax.

## Start here

- [Catena Functions and Calls](../20-notes/catena-functions-and-calls.md)
  develops the arity model, partial application, capture, local
  functions, and the tail guarantee.
- [Resolved function-model inquiry](../40-inquiries/what-is-catenas-function-and-call-model.md)
  records the operational question, hypotheses, and resolution.
- [Functions and Calls Specification](../60-specification/functions-and-calls/README.md)
  is the normative version 0.1.28 contract.
- [C032 evidence record](../50-journal/2026-08-25-c032-functions.md)
  records the witness evidence and verification.
- [Values and Evaluation map](values-and-evaluation.md),
  [Evaluation Order map](evaluation-order.md), and
  [Bindings and Sequencing map](bindings-and-sequencing.md) — the
  trilogy this completes.

## Trails

### Foundations that constrain any answer

- [Sequential Dynamics](../60-specification/formal-semantic-kernel/sequential-dynamics.md)
  fixes closures as values, one-argument substitution, and the
  proper-tail-call guarantee inside the exact 0.1.8 boundary.
- [BEAM Diagnostics and Conformance](../60-specification/formal-semantic-kernel/beam-diagnostics-and-conformance.md)
  fixes tail preservation on both lowering paths.
- [Ordered Forms and Entry Rule](../60-specification/evaluation-order/ordered-forms-and-entry-rule.md)
  fixes the curried-call schedule.
- [Binding Structure and Scope](../60-specification/bindings-and-sequencing/binding-structure-and-scope.md)
  fixes the non-recursion and shadowing local functions inherit.

### Limits and traceability

- [Conformance Traceability](conformance-traceability.md) registers
  `FC-OBL-001` through `FC-OBL-008` against normative anchors and
  immutable sibling compiler evidence.
- G033 branching; P034 termination beyond the tail guarantee; G037
  closure allocation identity; G084 process-entry tails; P109
  surface spellings remain the future owners.

## Open questions

C032 is complete at revision `0.1.28`. P109 may surface multi-
parameter and application spellings with this model as their
semantics; G094 may lower through uncurried conventions under it.
