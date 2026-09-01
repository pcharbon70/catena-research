---
title: "The Intralanguage Exclusions"
kind: specification
created: "2026-09-01"
status: normative
spec_version: "0.1.43"
tags:
  - type-system
  - safety
  - specification
aliases:
  - "Catena unsafe exclusions"
---

# The Intralanguage Exclusions

## Status and authority

This chapter is the normative Catena 0.1.43 intralanguage
exclusion rule set. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It states the roof over three standing anchors: the guard
vocabulary of [Syntax and Safety](../clause-conditions/syntax-and-safety.md),
the erasure rule of [Artifacts, Erasure, and CLI](../specifications-and-governance/artifacts-erasure-and-cli.md),
and the failure taxonomy of
[The Six Categories](../runtime-failure-taxonomy/the-six-categories.md).

The rules apply only to source-language revision `0.1.43`. They do
not reinterpret retained manifests, interfaces, artifacts, or
signed formats.

## The exclusions

> **Normative definition.**

No cast, runtime type inspection, unchecked operation, compiler
intrinsic, or reflection form exists in edition `0.1`
(`DU-OBL-002`): unsafety cannot be written in Catena source.
Specifically (`DU-OBL-002`):

- **casts** — no operation asserts a type the checker did not
  prove, checked or unchecked;
- **runtime type inspection** — no form branches on a value's
  runtime type; there is no typecase, no reflection, no
  `type_of`, and no runtime type information to inspect (the
  erasure rule, unchanged);
- **unchecked operations** — no operation escapes the proof
  obligations of its typing rule;
- **compiler intrinsics** — no compiler-internal primitive is
  exposed as callable source surface; the kernel and reference
  stepper are tools, not library functions (`DU-OBL-002`);
- the C003 guard fragment's rejection of "a foreign call, dynamic
  test, reflection operation, or unchecked cast" stands unchanged
  as the standing vocabulary (`DU-OBL-003`).

## Arrival conditions

> **Normative definition.**

A slice that admits any excluded form MUST, in its own normative
revision (`DU-OBL-006`):

1. **state its representation** — amending the erasure rule
   (C006/C113) if any type or specification material must survive
   to runtime;
2. **state its failure classification** — amending the failure
   taxonomy (C036) with a named kind; no cast failure may inhabit
   an existing kind silently;
3. **state its visibility** — how every use site and every entry
   point is declared and diagnosable; and
4. **state its evidence interaction** — whether and how
   specifications, governance evidence, and derivations observe it.

Until all four are stated with witnesses, the exclusions bind
(`DU-OBL-002`).

## Rationale and evidence (non-normative)

The [dynamic-and-unsafe-boundaries synthesis](../../20-notes/catena-dynamic-and-unsafe-boundaries.md)
argues the three-anchor reading: the exclusion states facts the
corpus already established rather than renouncing anything live.
The [resolved
inquiry](../../40-inquiries/should-catena-have-dynamic-or-unsafe-boundaries.md)
preserves the decision route.
