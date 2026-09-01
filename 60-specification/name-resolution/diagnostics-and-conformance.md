---
title: "Name Resolution Diagnostics and Conformance"
kind: specification
created: "2026-09-01"
status: candidate
spec_version: "0.1.42"
tags:
  - conformance
  - diagnostics
  - name-resolution
  - specification
  - testing
aliases:
  - "Catena 0.1.42 name resolution conformance"
---

# Name Resolution Diagnostics and Conformance

## Status and authority

This chapter is the normative Catena 0.1.42 name-resolution
diagnostic, abstract frontend, and conformance contract. It is
governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md),
and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies [The Resolution Invariant](the-resolution-invariant.md) and
[Boundaries and Reservations](boundaries-and-reservations.md).

## Stable diagnostics

This area introduces **zero new diagnostic families**
(`RN-OBL-001`, `RN-OBL-002`). Import collision keeps C021's
collision diagnostics — rejection, never type disambiguation;
missing or ambiguous trait evidence keeps `TRT004`; unknown names
keep the unbound-name diagnostics of the typing families.

## Abstract public boundaries

The shipped boundaries witness the contract on existing machinery;
the bootstrap adds no new public API (`RN-OBL-001`):

- **Annotation invariance** — a program and its annotation-bearing
  twin resolve every name identically, producing the same values
  and diagnostics.
- **Scope-structure resolution** — shadowing resolves by scope,
  and import collision rejects rather than disambiguating.
- **Evidence before call sites** — trait calls run through
  instance evidence selected at the instance; missing or ambiguous
  evidence rejects there.

Implementations MUST NOT use these boundaries to claim
overloaded-by-type names, expected-type adaptation, call-site
ambiguity deferral, or inference-directed field access
(`RN-OBL-005`).

## Determinism

Unchanged programs produce identical values, traces, and
diagnostics on every conforming target; resolution outcomes are
independent of annotation placement and elaboration order
(`RN-OBL-002`).

## Conformance obligations

| ID | Obligation | Required executable evidence |
| --- | --- | --- |
| `RN-OBL-001` | apply resolution rules only at exact 0.1.42 and register the stable lifecycle addition with zero new families and no new API | exact selection, registry, and lifecycle tests |
| `RN-OBL-002` | keep resolution type-independent: annotations never change a name's target and results never depend on elaboration order | annotation-invariance witnesses |
| `RN-OBL-003` | keep the five-way classification: labels not names, constructors by visibility, literals by spelling, operators closed-set | classification witnesses |
| `RN-OBL-004` | keep evidence selection distinct from name resolution, settled at the instance with no call-site deferral | trait evidence witnesses |
| `RN-OBL-005` | keep the four exclusions: no overloading by type, no expected-type adaptation, no call-site deferral, no inference-directed field access | absence tests |
| `RN-OBL-006` | keep the table amendable only by a revision stating order-independence | exclusion tests |
| `RN-OBL-007` | keep scope-structure resolution with collision rejection unchanged from C021 | shadowing and collision witnesses |
| `RN-OBL-008` | keep the contract deterministic with the reuse map enforced | determinism tests |

Every obligation has at least one tagged passing test. The sibling
compiler gates the complete `RN-OBL-*` set against unknown and
uncovered identifiers before C066 conformance is claimed.

## Required evidence sets

Positive evidence includes an annotation-invariance pair (same
program, added and removed signatures, identical resolution
outcomes on the reference targets); a shadowing program resolving
by scope; a trait call running through explicit instance evidence;
and the lifecycle registration of 0.1.42.

Negative evidence — in the definitional sense — includes import
collision rejecting rather than disambiguating; missing or
ambiguous trait evidence rejecting at the instance (`TRT004`);
and no overload, adaptation, deferral, or inference-access entry
points existing.

Exclusion evidence demonstrates unchanged predecessor diagnostic
identities and predecessor APIs retaining their exact selections
and defaults.

## Revision and persistence separation

Revision `0.1.42` adds the invariant, the classification table,
and the exclusions; it adds no JSON AST version, kernel
S-expression version, interface version, artifact version,
signature domain, typing rule, runtime behavior, BEAM
representation, manifest field, public API name, or diagnostic
family, and amends no retained revision (`RN-OBL-001`,
`RN-OBL-002`).

The source-text decoder accepts cumulative revisions `0.1.9` through
`0.1.42`; every predecessor API retains its exact selection. The next
unused semantic patch is `0.1.43`.

## Rationale and evidence (non-normative)

The design route is preserved in the
[name-resolution synthesis](../../20-notes/catena-name-resolution.md),
the [resolved inquiry](../../40-inquiries/may-name-resolution-depend-on-inferred-types.md),
and the [topic map](../../10-maps/name-resolution.md). The C066
evidence record will preserve the sibling-compiler commands and
archive validation.
