---
title: "Compile-Time Evaluation"
kind: map
created: "2026-08-26"
tags:
  - archive-navigation
  - catena
  - compile-time-evaluation
aliases:
  - "Catena compile-time map"
---

# Compile-Time Evaluation

## Scope

This map connects C034's gate and the three shipped bounded
meta-evaluators to the C038 decision artifacts — the absence-plus-
gate stance, the derivations-as-generation classification, the cited
restriction table — and the owners of spellings, deriving
extensions, and code generation.

## Start here

- [Catena Compile-Time Evaluation](../20-notes/catena-compile-time-evaluation.md)
  develops the stance, the classification, and the table.
- [Resolved compile-time inquiry](../40-inquiries/what-executes-during-compilation.md)
  records the operational question, hypotheses, and resolution.
- [Compile-Time Evaluation Specification](../60-specification/compile-time-evaluation/README.md)
  is the candidate version 0.1.34 contract.
- [Recursion and Termination map](recursion-and-termination.md)
  fixes the gate this slice inherits.

## Trails

### Foundations that constrain any answer

- [The Separation Table](../60-specification/recursion-and-termination/the-separation-table.md)
  fixes the gate and lists compile-time evaluation as its consumer.
- [Claims, Examples, and Checking](../60-specification/specifications-and-governance/claims-examples-and-checking.md)
  fixes the 20,000-step budget precedent.
- [Data and Patterns README](../60-specification/data-and-patterns/README.md)
  and [Traits README](../60-specification/traits-and-categorical-operations/README.md)
  fix the derivation engines this slice classifies.

### Limits and traceability

- [Conformance Traceability](conformance-traceability.md) will
  register `CE-OBL-001` through `CE-OBL-008` against normative anchors
  and sibling compiler tests.
- P109 spellings; G040 deriving extensions; G005/G116 code
  generation; G121 build tooling remain the future owners.

## Open questions

C038 is complete at revision `0.1.34`. Const-eval, macros, and
attributes arrive — if ever — through gated slices of their own;
derive extensions that run user code arrive as new gated evaluators.
