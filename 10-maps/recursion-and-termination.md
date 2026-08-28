---
title: "Recursion and Termination"
kind: map
created: "2026-08-26"
tags:
  - archive-navigation
  - catena
  - recursion
  - termination
aliases:
  - "Catena recursion map"
---

# Recursion and Termination

## Scope

This map connects the kernel's recursion permission, C032's tail
guarantee, C029's divergence clause, C031's definitions-only boundary,
and the three shipped meta-level regimes (C003 conditions, C006
specification checking, C004 laws), to the C034 decision artifacts —
the unrestricted stance, the cited separation table, the G038 entry
rule — and the owners of compile-time evaluation, failure, and
cancellation.

## Start here

- [Catena Recursion and Termination](../20-notes/catena-recursion-and-termination.md)
  develops the stance, the table, and the gate.
- [Resolved recursion inquiry](../40-inquiries/how-does-catena-separate-recursion-from-termination.md)
  records the operational question, hypotheses, and resolution.
- [Recursion and Termination Specification](../60-specification/recursion-and-termination/README.md)
  is the candidate version 0.1.31 contract.
- [Functions and Calls map](functions-and-calls.md) fixes the tail
  guarantee this stance complements.

## Trails

### Foundations that constrain any answer

- [Sequential Dynamics](../60-specification/formal-semantic-kernel/sequential-dynamics.md)
  fixes "general recursion may reduce forever" and the signed
  environment.
- [Strictness and Terminal Outcomes](../60-specification/values-and-evaluation/strictness-and-terminal-outcomes.md)
  fixes divergence as non-termination, never a trap.
- [Binding Structure and Scope](../60-specification/bindings-and-sequencing/binding-structure-and-scope.md)
  fixes recursion as definitions-only.

### The shipped meta-level regimes

- [Clause Conditions Diagnostics](../60-specification/clause-conditions/diagnostics-and-conformance.md)
  — conditions acyclic; recursion is `CND004`.
- [Claims, Examples, and Checking](../60-specification/specifications-and-governance/claims-examples-and-checking.md)
  — the fixed 20,000-step pure checker.
- [Traits README](../60-specification/traits-and-categorical-operations/README.md)
  — bounded law checks and bounded samples.

### Limits and traceability

- [Conformance Traceability](conformance-traceability.md) will
  register `RT-OBL-001` through `RT-OBL-008` against normative anchors
  and sibling compiler tests.
- G038 compile-time evaluation under the gate; P109 syntax; G036
  failure taxonomy (divergence outside it); G084 process loops; G088
  cancellation remain the future owners.

## Open questions

C034 is complete at revision `0.1.31`. G038 arrives total-or-bounded
or not at all; any termination checker arrives as a gated opt-in
analysis.
