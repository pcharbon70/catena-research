---
title: "Exception Boundary Diagnostics and Conformance"
kind: specification
created: "2026-09-01"
status: candidate
spec_version: "0.1.47"
tags:
  - conformance
  - diagnostics
  - failure
  - specification
  - testing
aliases:
  - "Catena 0.1.47 exception boundary conformance"
---

# Exception Boundary Diagnostics and Conformance

## Status and authority

This chapter is the normative Catena 0.1.47 exception-boundary
diagnostic, abstract frontend, and conformance contract. It is
governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies [The Mechanism Partition](the-mechanism-partition.md).

## Stable diagnostics

This area introduces **zero new diagnostic families**
(`XB-OBL-001`, `XB-OBL-002`). Trap observation keeps C036's
kernel-verbatim identities; effect-row and resumption diagnostics
keep C005's; there is no exception form whose failure could carry
a new identity.

## Abstract public boundaries

The shipped boundaries witness the contract on existing machinery;
the bootstrap adds no new public API (`XB-OBL-001`):

- **The effect pattern** — a kernel effect whose handler declines
  to resume (the operation clause returns a fallback without
  resuming), aborting to the handler's result, agreeing on the
  reference stepper and compiled BEAM.
- **Trap terminality** — the C036 fixture: a trapping evaluation
  terminates its process with a kinded reason; nothing catches it.
- **Process locality** — C010's local-trap/spared-spawner outcome
  re-pinned.

Implementations MUST NOT use these boundaries to claim a language
exception form, a catchable trap, a separate panic construct, or
any silent class conversion (`XB-OBL-002`, `XB-OBL-006`).

## Determinism

Unchanged programs produce identical values, traces, and
diagnostics on every conforming target (`XB-OBL-002`).

## Conformance obligations

| ID | Obligation | Required executable evidence |
| --- | --- | --- |
| `XB-OBL-001` | apply partition rules only at exact 0.1.47 and register the stable lifecycle addition with zero new families and no new API | exact selection, registry, and lifecycle tests |
| `XB-OBL-002` | keep the partition: values, the pattern, and the terminal trap visibly distinct with no silent conversion | partition witnesses |
| `XB-OBL-003` | keep the pattern blessing descriptive: declining to resume aborts to the handler's result, per unchanged C005 | effect-pattern witnesses |
| `XB-OBL-004` | keep panics as trap kinds entering with their producers | absence and kind tests |
| `XB-OBL-005` | keep the routing table's owners: G084, G095/G096, G088, G105, G103 | routing witnesses |
| `XB-OBL-006` | keep the reopening door as the only amendment route for a language exception form | absence tests |
| `XB-OBL-007` | keep the contract deterministic with the C036/C010 failure corpus unchanged | determinism and re-pin tests |

Every obligation has at least one tagged passing test. The sibling
compiler gates the complete `XB-OBL-*` set against unknown and
uncovered identifiers before C081 conformance is claimed.

## Required evidence sets

Positive evidence includes the effect-pattern witness (handler
declining to resume, abort to result, both targets agreeing); the
trap fixture's terminal state; C010's spared-spawner outcome; and
the lifecycle registration of 0.1.47.

Negative evidence — in the definitional sense — includes no
raise/catch/try/rescue entry points on any frontend; no catchable
trap; no panic construct; and no producer shipping the reserved
panic kind yet.

Exclusion evidence demonstrates unchanged predecessor diagnostic
identities and predecessor APIs retaining their exact selections
and defaults.

## Revision and persistence separation

Revision `0.1.47` adds the partition, the pattern blessing, the
panic classification, and the routing table; it adds no JSON AST
version, kernel S-expression version, interface version, artifact
version, signature domain, typing rule, runtime behavior, BEAM
representation, manifest field, public API name, or diagnostic
family, and amends no retained revision (`XB-OBL-001`,
`XB-OBL-002`).

The source-text decoder accepts cumulative revisions `0.1.9` through
`0.1.47`; every predecessor API retains its exact selection. The next
unused semantic patch is `0.1.48`.

## Rationale and evidence (non-normative)

The design route is preserved in the
[synthesis](../../20-notes/catena-exception-boundary.md), the
[resolved inquiry](../../40-inquiries/are-exceptions-an-effect-a-trap-or-a-value.md),
and the [topic map](../../10-maps/exception-boundary.md). The C081
evidence record will preserve the sibling-compiler commands and
archive validation.
