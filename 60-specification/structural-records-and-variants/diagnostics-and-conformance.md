---
title: "Structural Records Diagnostics and Conformance"
kind: specification
created: "2026-08-29"
status: candidate
spec_version: "0.1.36"
tags:
  - conformance
  - diagnostics
  - records
  - specification
  - testing
aliases:
  - "Catena 0.1.36 records conformance"
---

# Structural Records Diagnostics and Conformance

## Status and authority

This chapter is the normative Catena 0.1.36 records diagnostic,
abstract frontend, and conformance contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies [The Operation Table](the-operation-table.md) and
[Rows and Representation](rows-and-representation.md).

## Stable diagnostics

This area introduces **zero new diagnostic families** (`SR-OBL-001`,
`SR-OBL-008`). The kernel's duplicate-label rejection keeps its
identity at its own boundary; no new invalid input exists — the JSON
AST carries no record tags, and the kernel's rules are unchanged.

## Abstract public boundaries

Two shipped boundaries witness the contract; the bootstrap adds no
new public API (`SR-OBL-001`):

- **Kernel stepper** — the definitional record and variant dynamics:
  the fixture's operation round-trip, duplicate rejection, and
  variant dispatch with labeled outcomes.
- **Compiled BEAM (kernel path)** — `check_kernel` + `compile_kernel`
  produce a module whose record operations agree with the stepper's
  selected values; assertions check selected values, not map shapes,
  since representation is invisible by contract.

Implementations MUST NOT use these boundaries to claim frontend
encodings, open-record literals, stable layouts, or collection
semantics (`SR-OBL-008`).

## Determinism

Equal kernel programs produce equal record results, variant
dispatches, and traces on every target (`SR-OBL-008`).

## Conformance obligations

| ID | Obligation | Required executable evidence |
| --- | --- | --- |
| `SR-OBL-001` | apply record behavior only at exact 0.1.36 and register the stable lifecycle addition | exact selection, registry, and lifecycle tests |
| `SR-OBL-002` | fix the seven-operation table with cited homes unchanged | operation-shape tests |
| `SR-OBL-003` | enforce closed literals: duplicate labels reject; missing-label operations statically unreachable; no expression produces an open row | duplicate and closure tests |
| `SR-OBL-004` | keep field order an effect-order fact only, with tails composing through type positions | order and row-substitution tests |
| `SR-OBL-005` | keep records semantic maps: order never affects equality; representation invisible | equality-agreement tests |
| `SR-OBL-006` | state the frontend absence: kernel calculus only; spellings at P109 | absence tests |
| `SR-OBL-007` | keep variant inject a value and dispatch by semantic label then payload | variant-dispatch tests |
| `SR-OBL-008` | keep the contract deterministic and outside G042/G062/P044/P109 claims with zero new families | repeated-result and exclusion tests |

Every obligation has at least one tagged passing test. The sibling
compiler gates the complete `SR-OBL-*` set against unknown and
uncovered identifiers before C041 conformance is claimed.

## Required evidence sets

Positive evidence includes the fixture's operation round-trip —
literal, update, select, extend/restrict, select — agreeing on
stepper and compiled BEAM by selected values; variant injection and
match dispatch agreeing by selected payloads; a signature with an
open tail instantiating over a closed record; and determinism across
repeated runs.

Negative evidence — in the definitional sense — includes a
duplicate-label literal rejecting at the kernel boundary; no JSON-AST
record encoding existing; and no new family appearing.

Exclusion evidence demonstrates unchanged kernel diagnostic
identities, unchanged predecessor APIs, and no frontend, layout, or
collection claims.

## Revision and persistence separation

Revision `0.1.36` adds the operation table, the row model, and the
representation clause; it adds no JSON AST version, kernel
S-expression version, interface version, artifact version, signature
domain, typing rule, runtime behavior, BEAM representation, manifest
field, public API name, or diagnostic family, and amends no retained
revision (`SR-OBL-001`, `SR-OBL-008`).

The source-text decoder accepts cumulative revisions `0.1.9` through
`0.1.36`; every predecessor API retains its exact selection. The next
unused semantic patch is `0.1.37`.

## Rationale and evidence (non-normative)

The design route is preserved in the
[records synthesis](../../20-notes/catena-structural-records.md), the
[resolved inquiry](../../40-inquiries/what-are-structural-records-and-variants.md),
and the [topic map](../../10-maps/structural-records.md). The C041
evidence record will preserve the sibling-compiler commands and
archive validation.
