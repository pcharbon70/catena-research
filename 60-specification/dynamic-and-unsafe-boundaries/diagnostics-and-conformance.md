---
title: "Dynamic and Unsafe Boundaries Diagnostics and Conformance"
kind: specification
created: "2026-09-01"
status: candidate
spec_version: "0.1.43"
tags:
  - conformance
  - diagnostics
  - type-system
  - specification
  - testing
aliases:
  - "Catena 0.1.43 unsafe boundaries conformance"
---

# Dynamic and Unsafe Boundaries Diagnostics and Conformance

## Status and authority

This chapter is the normative Catena 0.1.43 dynamic-and-unsafe-
boundaries diagnostic, abstract frontend, and conformance
contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies [The Intralanguage Exclusions](the-intralanguage-exclusions.md) and
[The Foreign Visibility Routing](the-foreign-visibility-routing.md).

## Stable diagnostics

This area introduces **zero new diagnostic families**
(`DU-OBL-001`, `DU-OBL-002`). The guard fragment's rejections keep
their C003 identities; unknown forms keep the structural
diagnostics of their frontends; there is no cast or typecase form
whose failure could carry a new identity.

## Abstract public boundaries

The shipped boundaries witness the contract on existing machinery;
the bootstrap adds no new public API (`DU-OBL-001`):

- **Guard fragment** — the dynamic vocabulary (dynamic test,
  reflection, unchecked cast, foreign call) rejects inside
  conditions exactly as C003 fixed.
- **Erasure** — compiled artifacts carry no type or specification
  material (C006's rule); there is no runtime representation for
  inspection to branch on.
- **Value classification** — the comparable set and the value
  grammar are the only classification surface (C035/C029), with no
  `dyn`, `any`, or `unknown` type existing.

Implementations MUST NOT use these boundaries to claim cast,
inspection, intrinsic, reflection, or dyn forms, or any dynamic
entry path that does not discharge the foreign visibility
requirement (`DU-OBL-002`, `DU-OBL-004`).

## Determinism

Unchanged programs produce identical values, traces, and
diagnostics on every conforming target (`DU-OBL-002`).

## Conformance obligations

| ID | Obligation | Required executable evidence |
| --- | --- | --- |
| `DU-OBL-001` | apply boundary rules only at exact 0.1.43 and register the stable lifecycle addition with zero new families and no new API | exact selection, registry, and lifecycle tests |
| `DU-OBL-002` | keep all five intralanguage exclusions: no casts, no runtime type inspection, no unchecked operations, no intrinsics, no reflection | absence tests |
| `DU-OBL-003` | keep the guard fragment's rejection of the dynamic vocabulary unchanged from C003 | guard rejection witnesses |
| `DU-OBL-004` | enforce the cross-edge requirement: dynamic or unsafe values enter only through a visible, typed, failure-classified foreign boundary | routing witnesses |
| `DU-OBL-005` | keep the standing precedents cited and add no mechanism or spelling | absence tests |
| `DU-OBL-006` | keep the exclusions amendable only by a revision discharging all four arrival conditions | exclusion tests |
| `DU-OBL-007` | keep erasure intact: no runtime type or specification material for inspection | erasure witnesses |
| `DU-OBL-008` | keep the contract deterministic with no dyn, any, or unknown type existing | determinism and absence tests |

Every obligation has at least one tagged passing test. The sibling
compiler gates the complete `DU-OBL-*` set against unknown and
uncovered identifiers before C067 conformance is claimed.

## Required evidence sets

Positive evidence includes the guard fragment rejecting the
dynamic vocabulary; erasure evidence showing no type or
specification material in compiled artifacts; and the lifecycle
registration of 0.1.43.

Negative evidence — in the definitional sense — includes no cast,
typecase, reflection, intrinsic, or unchecked-operation entry
points; no `dyn`, `any`, or `unknown` type spelling on any
frontend; and no dynamic entry path that bypasses the foreign
owners.

Exclusion evidence demonstrates unchanged predecessor diagnostic
identities (C003 guard rejections, C006 erasure reporting) and
predecessor APIs retaining their exact selections and defaults.

## Revision and persistence separation

Revision `0.1.43` adds the exclusions, the arrival conditions, and
the foreign visibility routing; it adds no JSON AST version, kernel
S-expression version, interface version, artifact version,
signature domain, typing rule, runtime behavior, BEAM
representation, manifest field, public API name, or diagnostic
family, and amends no retained revision (`DU-OBL-001`,
`DU-OBL-002`).

The source-text decoder accepts cumulative revisions `0.1.9` through
`0.1.43`; every predecessor API retains its exact selection. The next
unused semantic patch is `0.1.44`.

## Rationale and evidence (non-normative)

The design route is preserved in the
[dynamic-and-unsafe-boundaries synthesis](../../20-notes/catena-dynamic-and-unsafe-boundaries.md),
the [resolved inquiry](../../40-inquiries/should-catena-have-dynamic-or-unsafe-boundaries.md),
and the [topic map](../../10-maps/dynamic-and-unsafe-boundaries.md).
The C067 evidence record will preserve the sibling-compiler
commands and archive validation.
