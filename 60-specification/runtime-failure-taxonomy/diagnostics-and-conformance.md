---
title: "Runtime Failure Taxonomy Diagnostics and Conformance"
kind: specification
created: "2026-08-26"
status: candidate
spec_version: "0.1.32"
tags:
  - conformance
  - diagnostics
  - failure
  - specification
  - testing
aliases:
  - "Catena 0.1.32 failure conformance"
---

# Runtime Failure Taxonomy Diagnostics and Conformance

## Status and authority

This chapter is the normative Catena 0.1.32 failure-taxonomy
diagnostic, abstract frontend, and conformance contract. It is
governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies [The Single Outcome](the-single-outcome.md) and
[The Six Categories](the-six-categories.md).

## Stable diagnostics

This area introduces **zero new diagnostic families** (`FT-OBL-001`,
`FT-OBL-008`). Runtime failure is an outcome, not invalidity: nothing
new is rejected. Traps report through the terminal contract
(`ENT003` at the entry boundary is C027's launch-report family and
keeps its meaning); divergent programs report nothing, by C034.

## Abstract public boundaries

Three shipped boundaries witness the contract; the bootstrap adds no
new public API (`FT-OBL-001`):

- **Kernel stepper** — the process-context witness: a trapping
  process discards its mailbox and affects no spawner, with the trap
  label in the outcome record.
- **Reference evaluator and compiled BEAM** — trap agreement: the
  same trapping program reports the same reason value on both
  targets.
- **Value classification** — `Catena.Values` classifies trap shapes
  as non-values and typed-failure-shaped values (constructor values)
  as values — the typed-failure-is-not-failure witness.

Implementations MUST NOT use these boundaries to claim a second
outcome class, exit signals, cancellation, or any excluded machinery
(`FT-OBL-008`).

## Determinism

Equal programs trap with equal reasons or terminate with equal values
on every target (`FT-OBL-008`).

## Conformance obligations

| ID | Obligation | Required executable evidence |
| --- | --- | --- |
| `FT-OBL-001` | apply failure behavior only at exact 0.1.32 and register the stable lifecycle addition | exact selection, registry, and lifecycle tests |
| `FT-OBL-002` | keep `trap(reason)` the single runtime failure outcome with the three-way partition stated | outcome-classification tests |
| `FT-OBL-003` | keep trap observability kernel-verbatim: mailbox discarded, no exit signal, no spawner effect, uninterceptable | process-context witness tests |
| `FT-OBL-004` | keep trap reason identity stable and agreeing across evaluator and BEAM | reason-identity agreement tests |
| `FT-OBL-005` | keep the six-category mapping exactly as classified | mapping-shape tests |
| `FT-OBL-006` | enforce the entry rule: no unclassified failure kind, no second outcome class | absence tests |
| `FT-OBL-007` | keep typed failure classified as values, not failures | classification tests |
| `FT-OBL-008` | keep the taxonomy deterministic and outside G084/G088/G092/G095/G105/P109 claims with zero new families | repeated-result and exclusion tests |

Every obligation has at least one tagged passing test. The sibling
compiler gates the complete `FT-OBL-*` set against unknown and
uncovered identifiers before C036 conformance is claimed.

## Required evidence sets

Positive evidence includes a trapping program agreeing on its reason
value across evaluator and BEAM (two distinct reasons, stably); the
kernel process-context witness — a spawned child traps while the
spawner terminates normally with its own value, the child's pending
message discarded; trap shapes classifying as non-values; and
constructor values (Option-shaped) classifying as values.

Negative evidence — in the definitional sense — includes divergence
remaining budget exhaustion, never a trap (C034 regression); no
faulting-operator, assert, or foreign-raise entry points existing;
and no new family appearing for any failure shape.

Exclusion evidence demonstrates no second outcome class, no exit
signal or monitor machinery, no cancellation conflation, unchanged
predecessor diagnostic identities, and predecessor APIs retaining
their exact selections and defaults.

## Revision and persistence separation

Revision `0.1.32` adds the single-outcome stance, the mapping, the
entry rule, and the observability elevation; it adds no JSON AST
version, kernel S-expression version, interface version, artifact
version, signature domain, typing rule, runtime behavior, BEAM
representation, manifest field, public API name, or diagnostic
family, and amends no retained revision (`FT-OBL-001`, `FT-OBL-008`).

The source-text decoder accepts cumulative revisions `0.1.9` through
`0.1.32`; every predecessor API retains its exact selection. The next
unused semantic patch is `0.1.33`.

## Rationale and evidence (non-normative)

The design route is preserved in the
[failure synthesis](../../20-notes/catena-runtime-failure-taxonomy.md),
the [resolved inquiry](../../40-inquiries/what-counts-as-runtime-failure.md),
and the [topic map](../../10-maps/runtime-failure-taxonomy.md). The
C036 evidence record will preserve the sibling-compiler commands and
archive validation.
