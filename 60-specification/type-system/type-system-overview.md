---
title: "Type-System Overview"
kind: specification
created: "2026-08-01"
status: normative
spec_version: "0.1"
tags:
  - catena
  - principal-types
  - specification
  - type-inference
aliases:
  - "Catena 0.1 type-system profiles"
---

# Type-System Overview

## Status and authority

This chapter and its seven sibling chapters are the normative Catena 0.1
type-system slice. They complete checklist item C001 without claiming that the
whole language is specified. The
[normative 0.2 data and pattern specification](../data-and-patterns/README.md)
defines the complete nominal ADT and match slice. Source parsing, full handler
dynamics, and the public trait library remain separate work.

`MUST`, `MUST NOT`, `SHOULD`, and `MAY` express requirements. An *invalid*
program MUST be rejected. *Implementation-defined* behavior must be documented
by an implementation; this type-system slice introduces none. Examples and
rationale are non-normative unless a conformance obligation says otherwise.

When artifacts disagree, the newest applicable normative chapter controls,
then its linked conformance cases. A compiler bug does not amend the
specification. See the [specification index](../README.md) for lifecycle rules.

## Two guarantee profiles

Every checked definition belongs to exactly one profile:

1. **Principal core** — unannotated rank-1 terms. Inference is sound, complete,
   and principal relative to the declarative core. It includes ordinary
   let-polymorphism, effect-aware generalization, unique value rows, duplicate
   effect rows, and unambiguous trait constraints.
2. **Annotation-directed advanced** — terms whose enclosing signature uses
   explicit nested `forall`, GADT refinement, or explicit existential binders.
   Checking is local, predicative, sound, and decidable, but Catena makes no
   global principal-type or completeness claim for this profile.

The compiler MUST identify an annotation that moves a term into the advanced
profile. It MUST NOT silently weaken the principal-core guarantee because an
extension is available.

## Shared static contract

Both profiles MUST:

- reject ill-kinded types and escaping rigid variables;
- reject ambiguous constraints rather than apply defaulting;
- use the separate row theories in
  [Rows, Traits, and Effects](rows-traits-and-effects.md);
- elaborate accepted programs to the explicit core in
  [Typed-Core Elaboration](typed-core-elaboration.md);
- verify the elaborated term before backend lowering; and
- emit diagnostics belonging to the stable families in
  [Diagnostics and Conformance](diagnostics-and-conformance.md).

All exported values MUST have explicit signatures. Private principal-core
definitions may be inferred. An implementation MAY infer and display a
candidate export signature, but absence of the written signature is invalid.

## Version boundary

Version 0.1 supports the advanced features defined in
[Advanced Type Checking](advanced-type-checking.md). It deliberately excludes
impredicativity, inference of higher-rank types, unrestricted type-level
computation, dependent types, general linear types, polymorphic recursion
without a signature, overlapping instances, local instances, and associated
constants.

The research basis and remaining wider questions are routed by the
[Catena Type-System Design map](../../10-maps/catena-type-system-design.md).
