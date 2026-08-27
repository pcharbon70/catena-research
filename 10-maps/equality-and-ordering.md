---
title: "Equality and Ordering"
kind: map
created: "2026-08-26"
tags:
  - archive-navigation
  - catena
  - equality
  - ordering
aliases:
  - "Catena equality map"
---

# Equality and Ordering

## Scope

This map connects C003's fragment-level equality, C018's finite
binary64 Float, C029's closed value grammar, the kernel's
record-equality fact, and the OTP signed-zero precedent, to the C035
decision artifacts — the comparable set, bit-exact float semantics,
structural recursion, monomorphism, the trait boundary — and the
owners of identity observability, future types, and trait layers.

## Start here

- [Catena Equality and Ordering](../20-notes/catena-equality-and-ordering.md)
  develops the comparable set, float semantics, and the guard split.
- [Resolved equality inquiry](../40-inquiries/which-values-compare-and-how.md)
  records the operational question, hypotheses, and resolution.
- [Equality and Ordering Specification](../60-specification/equality-and-ordering/README.md)
  is the normative version 0.1.30 contract.
- [C035 evidence record](../50-journal/2026-08-26-c035-equality.md)
  records the classifier, wiring, and witness evidence.
- [Values and Evaluation map](values-and-evaluation.md) — the grammar
  whose first operation this is.

## Trails

### Foundations that constrain any answer

- [Syntax and Safety](../60-specification/clause-conditions/syntax-and-safety.md)
  fixes the frozen Int/Bool guard fragment.
- [Numeric Literal Semantics Specification](../60-specification/numeric-literal-semantics/README.md)
  fixes finite binary64 with no coercions.
- [Value Forms and First-Classness](../60-specification/values-and-evaluation/value-forms-and-first-classness.md)
  fixes the closed grammar including both signed zeros.
- [Sequential Dynamics](../60-specification/formal-semantic-kernel/sequential-dynamics.md)
  fixes semantic record equality.

### Evidence

- [Erlang/OTP Support, Compatibility, Deprecations, and Removal](../30-sources/erlang-otp-compatibility-and-upgrading.md)
  — the OTP 27 signed-zero precedent and the no-bug-compatibility
  stance the model rides.

### Limits and traceability

- [Conformance Traceability](conformance-traceability.md) registers
  `EQ-OBL-001` through `EQ-OBL-008` against normative anchors and
  immutable sibling compiler evidence.
- G037 identity observability; G040 future types' comparability
  entries; G061/G101 Eq/Ord trait layers; P109 spellings remain the
  future owners.

## Open questions

C035 is complete at revision `0.1.30`. G040 enters each new type with
its comparability; G061/G101 build Eq/Ord on the built-ins; the
edition-record gate awaits any IEEE switch.
