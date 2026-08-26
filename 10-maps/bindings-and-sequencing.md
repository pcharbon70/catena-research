---
title: "Bindings and Sequencing"
kind: map
created: "2026-08-25"
tags:
  - archive-navigation
  - catena
  - bindings
  - sequencing
aliases:
  - "Catena bindings map"
---

# Bindings and Sequencing

## Scope

This map connects the C010 kernel rules that fix substitute-after-value
and the signed recursion environment, C021's innermost-wins shadowing,
C024's SCC as mutual recursion's home, C030's let and sequence
schedules, C022's IMP001 deny-able-warning precedent, the C031
decision artifacts — non-recursive bindings, the sequencing idiom,
`BS001` with its `_`-prefix exemption — and the owners of functions,
branching, termination, and syntax.

## Start here

- [Catena Bindings and Sequencing](../20-notes/catena-bindings-and-sequencing.md)
  develops binding structure, the recursion boundary, unused-binding
  fate, the sequencing idiom, and shadowing.
- [Resolved bindings inquiry](../40-inquiries/how-should-catena-define-bindings-and-sequencing.md)
  records the operational question, hypotheses, and resolution.
- [Bindings and Sequencing Specification](../60-specification/bindings-and-sequencing/README.md)
  is the candidate version 0.1.27 contract.
- [Values and Evaluation map](values-and-evaluation.md) and
  [Evaluation Order map](evaluation-order.md) — the trilogy's first
  two stops.

## Trails

### Foundations that constrain any answer

- [Sequential Dynamics](../60-specification/formal-semantic-kernel/sequential-dynamics.md)
  fixes substitute-after-value, unused-bindings-valid, and the signed
  definition environment inside the exact 0.1.8 boundary.
- [Shadowing and Ambiguity](../60-specification/namespaces-and-shadowing/shadowing-and-ambiguity.md)
  fixes the innermost-wins rule bindings restate.
- [SCC Admission and Resolution](../60-specification/module-dependency-cycles/scc-admission-and-resolution.md)
  fixes mutual recursion among definitions.
- [Ordered Forms and Entry Rule](../60-specification/evaluation-order/ordered-forms-and-entry-rule.md)
  fixes the let and sequence schedules.

### Evidence

- [Import Declarations and Admission](../60-specification/imports-and-exports/import-declarations-and-admission.md)
  supplies the IMP001 deny-able-warning pattern `BS001` copies.

### Limits and traceability

- [Conformance Traceability](conformance-traceability.md) registers
  `BS-OBL-001` through `BS-OBL-008` against normative anchors and
  immutable sibling compiler evidence.
- G032 functions and calls; G033 branching; P034 termination; P035
  equality; P109 syntax; and G088 cancellation remain the future
  owners.

## Open questions

C031 is complete at revision `0.1.27`. G032 may add local-function
forms on this discipline; P109 may surface sequencing punctuation;
the `_`-exemption rule awaits linting evidence.
