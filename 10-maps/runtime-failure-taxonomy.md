---
title: "Runtime Failure Taxonomy"
kind: map
created: "2026-08-26"
tags:
  - archive-navigation
  - catena
  - failure
  - traps
aliases:
  - "Catena failure map"
---

# Runtime Failure Taxonomy

## Scope

This map connects C010's completion-and-trap rules, C029's terminal
contract, C034's divergence exclusion, C005's unhandleable-trap rule,
and C018's arithmetic deferral, to the C036 decision artifacts — the
single outcome with kinded reasons, the six-way mapping, kernel-
verbatim observability, the per-producer entry rule — and the owners
of library types, foreign calls, runtime death, and spellings.

## Start here

- [Catena Runtime Failure Taxonomy](../20-notes/catena-runtime-failure-taxonomy.md)
  develops the single-outcome stance, the mapping, and the gate.
- [Resolved failure inquiry](../40-inquiries/what-counts-as-runtime-failure.md)
  records the operational question, hypotheses, and resolution.
- [Runtime Failure Taxonomy Specification](../60-specification/runtime-failure-taxonomy/README.md)
  is the candidate version 0.1.32 contract.
- [Values and Evaluation map](values-and-evaluation.md) fixes the
  terminal contract this elevates.

## Trails

### Foundations that constrain any answer

- [Actors, Messages, and Failures](../60-specification/formal-semantic-kernel/actors-messages-and-failures.md)
  fixes `trap(reason)`, its side effects, and its unhandleability.
- [Strictness and Terminal Outcomes](../60-specification/values-and-evaluation/strictness-and-terminal-outcomes.md)
  fixes the two-outcome terminal contract.
- [Program Recursion Is Unrestricted](../60-specification/recursion-and-termination/program-recursion-is-unrestricted.md)
  fixes divergence outside the taxonomy.
- [Deep Handlers and Affine Resumptions](../60-specification/effects-and-handlers/deep-handlers-and-affine-resumptions.md)
  fixes that handlers cannot intercept traps.

### Limits and traceability

- [Conformance Traceability](conformance-traceability.md) will
  register `FT-OBL-001` through `FT-OBL-008` against normative anchors
  and sibling compiler tests.
- G105 library types; G095/G096 foreign calls; G084 process death and
  signals; G092 VM termination; G088 cancellation; G037 failure-path
  observability; P109 assert/panic spellings remain the future
  owners.

## Open questions

C036 is complete at revision `0.1.32`. Arithmetic faults await the
first faulting operator; assertions await their form; foreign raises
await G095/G096 — all gated to arrive as `trap(reason)`.
