---
title: "Top-Level Effects Diagnostics and Conformance"
kind: specification
created: "2026-09-01"
status: normative
spec_version: "0.1.48"
tags:
  - conformance
  - diagnostics
  - effects
  - specification
  - testing
aliases:
  - "Catena 0.1.48 top-level conformance"
---

# Top-Level Effects Diagnostics and Conformance

## Status and authority

This chapter is the normative Catena 0.1.48 top-level-effects
diagnostic, abstract frontend, and conformance contract. It is
governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies [The Top-Level Boundary](the-top-level-boundary.md).

## Stable diagnostics

This area introduces **zero new diagnostic families**
(`TL-OBL-001`, `TL-OBL-002`). A non-effect-closed entry keeps
`ENT001` (C027, unchanged); there is no top-level request whose
failure could carry a new identity.

## Abstract public boundaries

The shipped boundaries witness the contract on existing machinery;
the bootstrap adds no new public API (`TL-OBL-001`):

- **Launch** — an entry declared over a total, effect-closed
  export, launched to completion with its report (C027's
  `Catena.Entry.launch/2` corpus).
- **Entry validation** — a manifest declaring an entry over a
  non-effect-closed export rejects `ENT001`.

Implementations MUST NOT use these boundaries to claim an ambient
host handler, a parameterized launch, or any capability injection
without G106's channel (`TL-OBL-004`, `TL-OBL-005`).

## Determinism

Unchanged programs produce identical values, traces, reports, and
diagnostics on every conforming target (`TL-OBL-002`).

## Conformance obligations

| ID | Obligation | Required executable evidence |
| --- | --- | --- |
| `TL-OBL-001` | apply boundary rules only at exact 0.1.48 and register the stable lifecycle addition with zero new families and no new API | exact selection, registry, and lifecycle tests |
| `TL-OBL-002` | keep the boundary: entries leave nothing unhandled and nobody interprets | launch and ENT001 witnesses |
| `TL-OBL-003` | keep launch as invocation only: to completion, no scope, no injection | launch re-pins |
| `TL-OBL-004` | keep the capability interface: explicit typed values via G106's channel or nothing; entry rules bind until then | absence tests |
| `TL-OBL-005` | keep no ambient handler reserved and supervision routed as failure-only | absence and routing tests |
| `TL-OBL-006` | keep the door: entry-form widening amends C027 explicitly with who-interprets-what stated | exclusion tests |
| `TL-OBL-007` | keep the contract deterministic with the C027 entry corpus unchanged | determinism and re-pin tests |

Every obligation has at least one tagged passing test. The sibling
compiler gates the complete `TL-OBL-*` set against unknown and
uncovered identifiers before C082 conformance is claimed.

## Required evidence sets

Positive evidence includes an entry launched to completion with
its report agreeing across runs; and the lifecycle registration
of 0.1.48.

Negative evidence — in the definitional sense — includes a
manifest entry over a non-effect-closed export rejecting
`ENT001`; and no ambient-handler, host-effect, or
parameterized-launch entry points existing.

Exclusion evidence demonstrates unchanged predecessor diagnostic
identities and predecessor APIs retaining their exact selections
and defaults.

## Revision and persistence separation

Revision `0.1.48` adds the boundary statement, the capability
interface, the supervision routing, and the door; it adds no JSON
AST version, kernel S-expression version, interface version,
artifact version, signature domain, typing rule, runtime behavior,
BEAM representation, manifest field, public API name, or
diagnostic family, and amends no retained revision (`TL-OBL-001`,
`TL-OBL-002`).

The source-text decoder accepts cumulative revisions `0.1.9` through
`0.1.48`; every predecessor API retains its exact selection. The next
unused semantic patch is `0.1.49`.

## Rationale and evidence (non-normative)

The design route is preserved in the
[synthesis](../../20-notes/catena-top-level-effects.md), the
[resolved inquiry](../../40-inquiries/who-interprets-top-level-requests.md),
and the [topic map](../../10-maps/top-level-effects.md). The C082
evidence record will preserve the sibling-compiler commands and
archive validation.
