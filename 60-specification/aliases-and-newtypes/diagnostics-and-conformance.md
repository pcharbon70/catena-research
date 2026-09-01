---
title: "Aliases and Newtypes Diagnostics and Conformance"
kind: specification
created: "2026-09-01"
status: candidate
spec_version: "0.1.41"
tags:
  - conformance
  - diagnostics
  - type-system
  - specification
  - testing
aliases:
  - "Catena 0.1.41 aliases and newtypes conformance"
---

# Aliases and Newtypes Diagnostics and Conformance

## Status and authority

This chapter is the normative Catena 0.1.41 aliases-and-newtypes
diagnostic, abstract frontend, and conformance contract. It is
governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies [The Alias Exclusion](the-alias-exclusion.md) and
[The Newtype Form](the-newtype-form.md).

## Stable diagnostics

This area introduces **zero new diagnostic families**
(`AN-OBL-001`, `AN-OBL-002`). An invalid transparency value keeps
`EXP001`; unknown or malformed declarations keep the C002
declaration diagnostics; type mismatches between a wrapper and its
wrapped type keep the typing families — that rejection is the
coercion rule's evidence (`AN-OBL-006`).

## Abstract public boundaries

The shipped boundaries witness the contract on existing machinery;
the bootstrap adds no new public API (`AN-OBL-001`):

- **Kernel and JSON-AST checkers** — a declared single-constructor
  single-field datatype constructs, matches, compares, and derives
  exactly as any nominal datatype; a program confusing the wrapper
  with the wrapped type rejects with the typing families.
- **Abstract export** — the same declaration exported `abstract`
  refuses outside construction and matching per C022/C023.
- **Value classification and comparison** — wrapper values are
  values; comparability recurses through the single field (C035).

Implementations MUST NOT use these boundaries to claim alias
forms, automatic instance flow, implicit coercion, per-constructor
exposure, or cost/layout promises (`AN-OBL-002`).

## Determinism

Unchanged programs produce identical values, traces, and
diagnostics on every conforming target (`AN-OBL-002`).

## Conformance obligations

| ID | Obligation | Required executable evidence |
| --- | --- | --- |
| `AN-OBL-001` | apply alias-and-newtype rules only at exact 0.1.41 and register the stable lifecycle addition with zero new families and no new API | exact selection, registry, and lifecycle tests |
| `AN-OBL-002` | keep transparent aliases excluded with the four arrival conditions recorded | absence tests |
| `AN-OBL-003` | fix the newtype as the nominal single-constructor single-field datatype with its own identity | newtype witness tests |
| `AN-OBL-004` | keep representation invisible with no cost or layout promises attached to a newtype | absence tests |
| `AN-OBL-005` | route opaque types to the binary authority vocabulary and keep nominal-spelled diagnostics | abstract-export and error-message witnesses |
| `AN-OBL-006` | keep coercion explicit: constructor wraps, pattern unwraps, confusion rejects | type-mismatch rejection tests |
| `AN-OBL-007` | keep deriving explicit-target only with no instance flow through the wrapper | derivation witnesses |
| `AN-OBL-008` | keep the exclusion amendable only by a revision discharging all four arrival conditions | exclusion tests |

Every obligation has at least one tagged passing test. The sibling
compiler gates the complete `AN-OBL-*` set against unknown and
uncovered identifiers before C062 conformance is claimed.

## Required evidence sets

Positive evidence includes a declared `Email`-style newtype
constructing, matching, comparing, and passing through a smart
constructor over an `abstract` export, agreeing on the reference
targets by selected values; explicit-target derivation on the
wrapper; and the lifecycle registration of 0.1.41.

Negative evidence — in the definitional sense — includes programs
confusing wrapper and wrapped types rejecting; no alias form or
entry point on any frontend; an invalid transparency value
rejecting `EXP001`; and no automatic-deriving or coercion entry
points.

Exclusion evidence demonstrates unchanged predecessor diagnostic
identities and predecessor APIs retaining their exact selections
and defaults.

## Revision and persistence separation

Revision `0.1.41` adds the alias exclusion and the newtype rules;
it adds no JSON AST version, kernel S-expression version, interface
version, artifact version, signature domain, typing rule, runtime
behavior, BEAM representation, manifest field, public API name, or
diagnostic family, and amends no retained revision (`AN-OBL-001`,
`AN-OBL-002`).

The source-text decoder accepts cumulative revisions `0.1.9` through
`0.1.41`; every predecessor API retains its exact selection. The next
unused semantic patch is `0.1.42`.

## Rationale and evidence (non-normative)

The design route is preserved in the
[aliases-and-newtypes synthesis](../../20-notes/catena-aliases-and-newtypes.md),
the [resolved inquiry](../../40-inquiries/should-catena-admit-type-aliases-and-newtypes.md),
and the [topic map](../../10-maps/aliases-and-newtypes.md). The C062
evidence record will preserve the sibling-compiler commands and
archive validation.
