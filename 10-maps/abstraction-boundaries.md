---
title: "Abstraction Boundaries"
kind: map
created: "2026-08-23"
tags:
  - abstraction
  - archive-navigation
  - catena
  - modules
aliases:
  - "Catena abstraction map"
---

# Abstraction Boundaries

## Scope

This map connects the shipped C002 representation contract and C022
transparency vocabulary that implied the boundary's shape, the
Leroy/SML evidence behind representation independence and signature
abstraction, the C023 decision artifacts that complete the boundary with
two exclusions and one sanctioned idiom, and the owners of everything
deliberately left outside edition 0.1.

## Start here

- [Catena Abstraction Boundaries](../20-notes/catena-abstraction-boundaries.md)
  develops the no-stable-layout and no-authority-split exclusions and the
  smart-constructor-over-abstract-type idiom with its coverage
  consequence.
- [Resolved abstraction inquiry](../40-inquiries/how-should-catena-draw-its-abstraction-boundaries.md)
  records the operational question, hypotheses, and resolution.
- [Abstraction Boundaries Specification](../60-specification/abstraction-boundaries/README.md)
  is the normative version 0.1.19 contract.
- [C023 evidence record](../50-journal/2026-08-23-c023-abstraction-boundaries.md)
  records the executable exclusion-proof and idiom corpus and
  verification.
- [Imports and Exports map](imports-and-exports.md) fixes the export
  vocabulary whose transparency pair this boundary declares complete.

## Trails

### Shipped contracts that imply the boundary

- [Interfaces and Representation](../60-specification/data-and-patterns/interfaces-and-representation.md)
  fixes layout-free interfaces, both-layout conformance, `L001`, and the
  anticipated future schema contract.
- [Export Declarations and Visibility](../60-specification/imports-and-exports/export-declarations-and-visibility.md)
  fixes the exact transparent/abstract enum.
- [Match Semantics and Coverage](../60-specification/data-and-patterns/match-semantics-and-coverage.md)
  fixes the wildcard-remainder coverage the abstract idiom relies on.

### Evidence

- [Unboxed Objects and Polymorphic Typing](../30-sources/leroy-1992-unboxed-objects.md)
  grounds representation independence versus observable-layout
  compatibility surfaces.
- [The Definition of Standard ML (Revised)](../30-sources/milner-et-al-1997-definition-standard-ml.md)
  grounds signature-controlled abstraction without dedicated constructs.
- [Algebraic Data Types](algebraic-data-types.md) supplies the
  smart-constructor and views framing.

### Limits and traceability

- [Conformance Traceability](conformance-traceability.md) registers
  `AB-OBL-001` through `AB-OBL-007` against normative anchors and sibling
  compiler tests.
- [Implementation Limits and Portability map](implementation-limits-and-portability.md)
  carries the generated-module bounds that both-layout conformance
  already exercises.

## Open questions

C023 is complete at revision `0.1.19`. G028 retains any layout-stability or ABI contract; D046/G040 retain views and
selective exposure; P093 retains BEAM representation mapping under
non-observability; G095 retains foreign-term validation; G101+ consumes
the sanctioned idiom in the standard library.
