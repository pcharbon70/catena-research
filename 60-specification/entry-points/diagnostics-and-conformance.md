---
title: "Entry Points Diagnostics and Conformance"
kind: specification
created: "2026-08-24"
status: candidate
spec_version: "0.1.23"
tags:
  - conformance
  - diagnostics
  - entry-points
  - specification
  - testing
aliases:
  - "Catena 0.1.23 entry points conformance"
---

# Entry Points Diagnostics and Conformance

## Status and authority

This chapter is the normative Catena 0.1.23 entry-point diagnostic,
abstract frontend, and conformance contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies [Entry Declarations](entry-declarations.md) and
[Startup and Shutdown](startup-and-shutdown.md).

## Stable diagnostics

| ID | Required meaning |
| --- | --- |
| `ENT001` | a malformed entry declaration: non-array `entries`, non-object entry, missing or non-string `name`/`result`, `launch` not `true`, duplicated `name`, unknown export, non-zero-argument export, non-effect-closed export, `result` mismatch, or a second `launch` marker |
| `ENT002` | a launch naming an entry the package does not declare |
| `ENT003` | a launch report of failure, carrying the kernel trap identity |

All other entry-adjacent failures reuse existing families unchanged:
manifest framing outside the entries shapes is `PKG001`; selection
mismatches are `EDN001` (`EN-OBL-009`). Failure is transactional;
diagnostics carry the offending field and shape. Diagnostic prose can
improve only within the bounded presentation rules.

## Abstract public boundaries

Three boundaries gain entry wiring (`EN-OBL-001`):

- **Manifest decode** — the optional `entries` array validates per the
  grammar of [Entry Declarations](entry-declarations.md) or rejects as
  `ENT001`; absent, `null`, and `[]` all decode to a library.
- **Package validation** — each declared entry is checked against the
  package's compiled exports: existence, zero arity, empty effect row,
  and result-type equality, rejecting as `ENT001`; the check reuses the
  recorded export rows of the interface format.
- **Launch** — a launch operation takes a validated package and an
  entry name, rejects unknown names as `ENT002`, evaluates the entry's
  function to completion under the kernel semantics, and returns the
  completed report with the entry's value or the failed report with the
  trap identity as `ENT003`.

Implementations MUST NOT use these boundaries to claim supervision,
scheduling, CLI tooling, or any excluded machinery (`EN-OBL-010`). The
bootstrap evidence adds no new public API names beyond the `entries`
field on the manifest boundary and the launch operation.

## Determinism

Equal manifests, packages, and entry names produce equal validation
results, launch reports, or diagnostics; nothing about entry
declaration, validation, or launch varies by registry, environment, or
tool (`EN-OBL-010`).

## Conformance obligations

| ID | Obligation | Required executable evidence |
| --- | --- | --- |
| `EN-OBL-001` | apply entry behavior only at exact 0.1.23 and register the stable lifecycle addition | exact selection, registry, and lifecycle tests |
| `EN-OBL-002` | accept the optional `entries` array with the entry object grammar and optional `launch: true` | decode and shape tests |
| `EN-OBL-003` | reject every malformed entry declaration as `ENT001` with the offending shape | malformed matrix tests |
| `EN-OBL-004` | derive libraries from zero declared entries with absent/`null`/`[]` equivalence and no kind flag | derivation and equivalence tests |
| `EN-OBL-005` | enforce at most one launch marker and allow launching any declared entry by name | marker-rule and named-launch tests |
| `EN-OBL-006` | launch by invoking the entry's function to completion under unchanged strict kernel semantics, introducing no scope or process | launch evaluation tests |
| `EN-OBL-007` | report `{ completed, value }` or `{ failed, trap }` — return-is-shutdown with the trap identity | completion and failure-report tests |
| `EN-OBL-008` | reject a launch naming an undeclared entry as `ENT002` | unknown-name launch tests |
| `EN-OBL-009` | emit stable diagnostics: `ENT001`–`ENT003` plus the reused families with unchanged identities | every diagnostic family test |
| `EN-OBL-010` | keep the wiring deterministic, source-only, and outside G084/G088/G121 machinery, with compilation roots unchanged | repeated-report and exclusion tests |

Every obligation has at least one tagged passing test. The sibling
compiler gates the complete `EN-OBL-*` set against unknown and
uncovered identifiers before C027 conformance is claimed.

## Required evidence sets

Positive evidence includes a manifest with `entries` decoding and
validating; a library manifest with the field absent, `null`, and `[]`
producing identical results; a multi-entry manifest with and without a
launch marker; launching a declared entry that returns a value, with
the report carrying exactly that value; and launching each of several
entries by name.

Negative evidence includes every `ENT001` shape; a launch naming an
undeclared entry as `ENT002`; a launch whose evaluation traps reported
as `ENT003` with the kernel trap identity; and framing failures outside
the entries shapes remaining `PKG001`.

Exclusion evidence demonstrates that entry validation launches nothing,
that launch binds no names and spawns no process, that compilation
roots validate and emit unchanged with and without `entries`, and that
predecessor APIs retain their exact selections and defaults.

## Revision and persistence separation

Revision `0.1.23` adds the `entries` field, entry validation, the
launch operation and reports, and `ENT001`–`ENT003`; it adds no JSON
AST version, kernel S-expression version, interface version, artifact
version, signature domain, typing rule, runtime behavior, or BEAM
representation (`EN-OBL-001`, `EN-OBL-010`). The manifest extension is
optional and backward-compatible: every previously valid manifest
remains valid.

The source-text decoder accepts cumulative revisions `0.1.9` through
`0.1.23`; every predecessor API retains its exact selection, with the
manifest decoder and package validation advancing to accept `entries`.
The next unused semantic patch is `0.1.24`.

## Rationale and evidence (non-normative)

The design route is preserved in the
[entry-points synthesis](../../20-notes/catena-entry-points.md), the
[resolved inquiry](../../40-inquiries/how-should-catena-define-entry-points-and-application-structure.md),
and the [topic map](../../10-maps/entry-points.md). The C027 evidence
record will preserve the sibling-compiler commands and archive
validation.
