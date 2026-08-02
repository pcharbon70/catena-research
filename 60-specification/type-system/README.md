---
title: "Type-System Specification"
kind: map
created: "2026-08-01"
tags:
  - archive-navigation
  - directory-index
  - specification
  - type-inference
aliases:
  - "Catena type-system specification index"
---

# Type-System Specification (`60-specification/type-system`)

## Purpose

These chapters define Catena 0.1's two named type-checking profiles and their
shared elaboration contract.

## What belongs here

Keep normative type syntax, inference, generalization, rows, traits, effects,
advanced checking, typed-core verification, metatheory targets, diagnostics,
and conformance requirements here. Datatype, pattern, and handler rules remain
partial unless a chapter explicitly incorporates them.

## Index

### Subdirectories

- None yet.

### Documents

- [Type-System Overview](type-system-overview.md) — authority, profiles,
  conformance language, and the boundary of C001.
- [Type Language and Kinds](type-language-and-kinds.md) — type grammar,
  quantification, constraints, kinds, signatures, and exports.
- [Principal Inference and Generalization](principal-inference-and-generalization.md)
  — Algorithm W obligations, recursive groups, subsumption, and the
  effect-aware hybrid generalization rule.
- [Rows, Traits, and Effects](rows-traits-and-effects.md) — distinct value and
  effect rows plus terminating, open, coherent trait resolution.
- [Advanced Type Checking](advanced-type-checking.md) — explicit predicative
  higher rank, GADT branch equalities, rigid existentials, and exclusions.
- [Typed-Core Elaboration](typed-core-elaboration.md) — explicit evidence,
  capabilities, annotations, verifier boundary, and OTP 29 backend contract.
- [Metatheory](metatheory.md) — precise soundness, principality, coherence, and
  termination claims and their current proof status.
- [Diagnostics and Conformance](diagnostics-and-conformance.md) — stable
  diagnostic families, JSON test boundary, and promotion gate.

## Executable evidence

The clean bootstrap implementation lives in the sibling
[Catena compiler repository](https://github.com/pcharbon70/catena). Its
`.tool-versions` pins Erlang/OTP 29.0.4 and Elixir 1.20.2 for OTP 29. From that
repository, run:

```bash
asdf exec mix compile --warnings-as-errors
asdf exec mix test
asdf exec mix escript.build
```

The exact environment, observations, and limits of the current run are in
[C001 Executable Type-System Conformance](../../50-journal/2026-08-01-c001-executable-type-system-conformance.md).

## Maintaining this index

Version related chapters together. A normative rule change requires a
conformance case, updated executable model where applicable, and an explicit
compatibility decision.
