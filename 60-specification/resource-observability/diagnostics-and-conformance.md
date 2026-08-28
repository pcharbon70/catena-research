---
title: "Resource Observability Diagnostics and Conformance"
kind: specification
created: "2026-08-26"
status: candidate
spec_version: "0.1.33"
tags:
  - conformance
  - diagnostics
  - observability
  - specification
  - testing
aliases:
  - "Catena 0.1.33 observability conformance"
---

# Resource Observability Diagnostics and Conformance

## Status and authority

This chapter is the normative Catena 0.1.33 observability diagnostic,
abstract frontend, and conformance contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies [The Observability Model](the-observability-model.md) and
[Identity and Finalization](identity-and-finalization.md).

## Stable diagnostics

This area introduces **zero new diagnostic families** (`RO-OBL-001`,
`RO-OBL-008`). Observability is a classification, not an input rule:
nothing new is accepted or rejected, and every existing family keeps
its identity and meaning unchanged.

## Abstract public boundaries

Three shipped boundaries witness the contract; the bootstrap adds no
new public API (`RO-OBL-001`):

- **Value classification** — `Catena.Values` carries no
  identity-bearing primitive: only process-handle shapes represent
  identity, and no address, reference, or identity form exists in
  either carrier.
- **Evaluator and compiled BEAM** — semantic-identity agreement:
  records constructed at distinct sites compare equal; a closure
  applied twice yields equal results regardless of its allocation.
- **Kernel stepper** — the process-identity witness: fresh identity
  per spawn (two spawns, two distinct processes in the outcome
  record), `self` returning the current handle, and copy-irrelevant
  message semantics.

Implementations MUST NOT use these boundaries to claim in-language
identity operations, cleanup forms, stack observability, or any
excluded machinery (`RO-OBL-008`).

## Determinism

Equal programs observe equally: identical values, outcomes, and
traces, independent of representation choices (`RO-OBL-008`).

## Conformance obligations

| ID | Obligation | Required executable evidence |
| --- | --- | --- |
| `RO-OBL-001` | apply observability behavior only at exact 0.1.33 and register the stable lifecycle addition | exact selection, registry, and lifecycle tests |
| `RO-OBL-002` | fix the six-way classification: addresses, sharing, GC, and identity (except process) unobservable; stack only via the tail guarantee; finalization absent | classification-shape tests |
| `RO-OBL-003` | keep semantic identity: equal values interchangeable, representation never changing meaning, storage observing nothing | semantic-identity agreement tests |
| `RO-OBL-004` | keep process identity the only identity-bearing value: fresh per spawn, kernel operations only, never comparable | process-identity witness tests |
| `RO-OBL-005` | keep every other value semantically identical only: closure allocation, record sharing, message copying unobservable | closure-and-record agreement tests |
| `RO-OBL-006` | keep finalization declared absent with its gate: no cleanup form exists or arrives ungated | absence tests |
| `RO-OBL-007` | keep stack use observable only through completion versus the tail guarantee | tail-guarantee regression tests |
| `RO-OBL-008` | keep the classification deterministic and outside G080s/G084/G085/G095/G124 claims with zero new families | repeated-result and exclusion tests |

Every obligation has at least one tagged passing test. The sibling
compiler gates the complete `RO-OBL-*` set against unknown and
uncovered identifiers before C037 conformance is claimed.

## Required evidence sets

Positive evidence includes records built at distinct construction
sites comparing equal on evaluator and BEAM; a let-bound closure
applied twice yielding equal results; two kernel spawns yielding two
distinct processes with distinct handles in the outcome record; `self`
round-tripping through send; and determinism across repeated runs.

Negative evidence — in the definitional sense — includes no address,
reference, identity, or cleanup entry points existing anywhere in the
public surface; no value form carrying identity besides the handle;
and no stack-depth observable.

Exclusion evidence demonstrates no in-language identity operations, no
cleanup forms, unchanged predecessor diagnostic identities, and
predecessor APIs retaining their exact selections and defaults.

## Revision and persistence separation

Revision `0.1.33` adds the classification, the identity rule, the
finalization absence, and the debugging-channel statement; it adds no
JSON AST version, kernel S-expression version, interface version,
artifact version, signature domain, typing rule, runtime behavior,
BEAM representation, manifest field, public API name, or diagnostic
family, and amends no retained revision (`RO-OBL-001`, `RO-OBL-008`).

The source-text decoder accepts cumulative revisions `0.1.9` through
`0.1.33`; every predecessor API retains its exact selection. The next
unused semantic patch is `0.1.34`.

## Rationale and evidence (non-normative)

The design route is preserved in the
[observability synthesis](../../20-notes/catena-resource-observability.md),
the [resolved inquiry](../../40-inquiries/what-may-programs-observe-of-resources.md),
and the [topic map](../../10-maps/resource-observability.md). The
C037 evidence record will preserve the sibling-compiler commands and
archive validation.
