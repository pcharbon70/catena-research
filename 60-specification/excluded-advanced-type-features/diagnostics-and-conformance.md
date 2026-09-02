---
title: "Excluded Advanced Type Features Diagnostics and Conformance"
kind: specification
created: "2026-09-01"
status: normative
spec_version: "0.1.44"
tags:
  - conformance
  - diagnostics
  - type-system
  - specification
  - testing
aliases:
  - "Catena 0.1.44 advanced exclusions conformance"
---

# Excluded Advanced Type Features Diagnostics and Conformance

## Status and authority

This chapter is the normative Catena 0.1.44 excluded-advanced-type
diagnostic, abstract frontend, and conformance contract. It is
governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies [The Exclusion Table and Gate](the-exclusion-table-and-gate.md).

## Stable diagnostics

This area introduces **zero new diagnostic families**
(`EA-OBL-001`, `EA-OBL-002`). Rejections of excluded forms keep
the profile-boundary identities C001 requires; unknown type forms
keep the structural diagnostics of their frontends.

## Abstract public boundaries

The shipped boundaries witness the contract on existing machinery;
the bootstrap adds no new public API (`EA-OBL-001`):

- **Checkers** — a program attempting an excluded form rejects
  with the profile-boundary diagnostic; a checked-profile program
  (explicit higher rank, signature-directed GADT) checks unchanged.
- **Type inventory** — the frozen type grammar admits no excluded
  form's spelling.

Implementations MUST NOT use these boundaries to claim any
excluded form or to widen the checked profile (`EA-OBL-002`,
`EA-OBL-005`).

## Determinism

Unchanged programs produce identical values, traces, and
diagnostics on every conforming target (`EA-OBL-002`).

## Conformance obligations

| ID | Obligation | Required executable evidence |
| --- | --- | --- |
| `EA-OBL-001` | apply exclusion rules only at exact 0.1.44 and register the stable lifecycle addition with zero new families and no new API | exact selection, registry, and lifecycle tests |
| `EA-OBL-002` | keep all seven forms excluded with the checked profile unchanged | absence and regression tests |
| `EA-OBL-003` | keep the seven-point gate as the only amendment route | exclusion tests |
| `EA-OBL-004` | keep rejections identifying the profile boundary | rejection witnesses |
| `EA-OBL-005` | keep C068's checked advanced profile checking unchanged | positive-complement pins |
| `EA-OBL-006` | admit no omnibus advanced-features revision | exclusion tests |
| `EA-OBL-007` | keep the contract deterministic with no excluded spelling accepted | determinism and absence tests |

Every obligation has at least one tagged passing test. The sibling
compiler gates the complete `EA-OBL-*` set against unknown and
uncovered identifiers before C140 conformance is claimed.

## Required evidence sets

Positive evidence includes a checked-profile program (explicit
higher rank through the annotation boundary) checking and running
unchanged; and the lifecycle registration of 0.1.44.

Negative evidence — in the definitional sense — includes programs
attempting excluded forms rejecting with profile-boundary
diagnostics; and no excluded form's type spelling accepted on any
frontend.

Exclusion evidence demonstrates unchanged predecessor diagnostic
identities and predecessor APIs retaining their exact selections
and defaults.

## Revision and persistence separation

Revision `0.1.44` adds the exclusion table and the arrival gate;
it adds no JSON AST version, kernel S-expression version,
interface version, artifact version, signature domain, typing
rule, runtime behavior, BEAM representation, manifest field,
public API name, or diagnostic family, and amends no retained
revision (`EA-OBL-001`, `EA-OBL-002`).

The source-text decoder accepts cumulative revisions `0.1.9` through
`0.1.44`; every predecessor API retains its exact selection. The next
unused semantic patch is `0.1.45`.

## Rationale and evidence (non-normative)

The design route is preserved in the
[excluded-advanced-types synthesis](../../20-notes/catena-excluded-advanced-types.md),
the [resolved inquiry](../../40-inquiries/how-do-the-excluded-advanced-type-forms-stay-excluded.md),
and the [topic map](../../10-maps/excluded-advanced-type-features.md).
The [C140 evidence
record](../../50-journal/2026-09-01-c140-exclusions.md)
preserves the sibling-compiler commands and archive validation.
