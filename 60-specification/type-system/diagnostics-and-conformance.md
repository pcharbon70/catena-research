---
title: "Type-System Diagnostics and Conformance"
kind: specification
created: "2026-08-01"
status: normative
spec_version: "0.1"
tags:
  - catena
  - diagnostics
  - specification
  - type-inference
aliases:
  - "Catena 0.1 type-system conformance"
---

# Type-System Diagnostics and Conformance

## Diagnostic contract

Every rejection MUST have a stable family identifier, a primary source span,
and a human explanation. Relevant inferred types, originating constraints, and
secondary spans SHOULD be included. Version 0.1 reserves:

| Family | Meaning |
| --- | --- |
| `T001` | unbound value name |
| `T002` | value-type mismatch |
| `T003` | infinite type or row |
| `T004` | kind mismatch |
| `T005` | missing or duplicate unique-row label |
| `T006` | ambiguous constraint |
| `T007` | unsatisfied, overlapping, or nonterminating trait resolution |
| `T008` | missing required signature |
| `T009` | rigid type, existential, or equality escapes scope |
| `T010` | unsupported advanced-profile inference |
| `T011` | affine resumption consumed more than once or escapes |
| `T012` | malformed or unsupported versioned AST input |

Adding detail to a diagnostic does not change its identity. A later edition
may subdivide a family but MUST document the compatibility mapping.

## Executable input boundary

Until Catena source syntax is normative, executable conformance cases use a
canonical JSON document containing `version`, `module`, `exports`, and
`definitions`. Version 0.1 expressions include variables, integer and Boolean
literals, lambdas, calls, non-recursive lets, tuples, and annotations. Unknown
versions or node tags are `T012`.

Each accepted case records its normalized inferred scheme, profile, typed-core
shape, and—when in the executable subset—BEAM result. Each rejected case
records at least its diagnostic family. Alpha-renaming and declaration-order
variants MUST normalize to the same result where scope is unchanged.

## Conformance gate

The C001 normative slice requires all of the following:

- positive and negative tests for every diagnostic family exercised by the
  implemented slice;
- principal-core examples compared with a separately structured declarative
  checker over a bounded generated corpus;
- solver-order and alpha-renaming stability tests;
- typed-core verification for every accepted compiler fixture;
- actual OTP 29 compilation through `compile:noenv_forms/2`, followed by
  loading and executing representative `.beam` binaries;
- a runtime double-consumption test for the affine resumption token; and
- no direct BEAM or Core Erlang output path in the toolchain.

The current executable model lives in the sibling Catena toolchain repository;
its path and commands are recorded in the
[Type-System Specification index](README.md). These tests cover C001, not the
unimplemented surface parser or every broader language checklist item.

## Rationale (non-normative)

Research rationale remains available through the
[Hindley–Milner map](../../10-maps/hindley-milner-type-inference.md) and the
[greenfield type-system inquiry](../../40-inquiries/what-should-a-greenfield-catena-type-system-guarantee.md).
