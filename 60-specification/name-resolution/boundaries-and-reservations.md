---
title: "Boundaries and Reservations"
kind: specification
created: "2026-09-01"
status: candidate
spec_version: "0.1.42"
tags:
  - name-resolution
  - specification
aliases:
  - "Catena resolution boundaries"
---

# Boundaries and Reservations

## Status and authority

This chapter is the normative Catena 0.1.42 resolution exclusion
rule set. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies [The Resolution Invariant](the-resolution-invariant.md).

The rules apply only to source-language revision `0.1.42`.

## The exclusions

> **Normative definition.**

No form of type-directed name selection exists in edition `0.1`
(`RN-OBL-005`):

- **overloaded-by-type names** — no value, method, or constructor
  name may denote different declarations chosen by inferred or
  expected types;
- **expected-type-adapted literals** — no literal changes meaning
  under an expected type (C018's clause, re-affirmed);
- **call-site ambiguity deferral** — no unresolved name waits for
  call-site types to disambiguate;
- **field-access-by-inference** — no access infers which field a
  spelling means from the expression's type; record operations
  remain typed operations over labels (`RN-OBL-005`).

## Arrival conditions

> **Normative definition.**

Any future form that lets types influence which declaration a name
denotes MUST arrive in its own revision that amends the
classification table of
[The Resolution Invariant](the-resolution-invariant.md#the-five-way-classification)
explicitly, and MUST state how it preserves order-independence of
results and diagnostics naming (`RN-OBL-006`). Until then, this
exclusion binds every conforming implementation (`RN-OBL-005`).

## Rationale and evidence (non-normative)

The [name-resolution synthesis](../../20-notes/catena-name-resolution.md)
records the order-dependence hazard that motivates the exclusion —
the failure mode the scope-structural model (C021) was chosen to
avoid, and the reason the corpus rejects the open-re-shadowing
family of designs.
