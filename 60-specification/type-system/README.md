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

These chapters define Catena 0.1.1's two named type-checking profiles and their
shared elaboration contract.

## What belongs here

Keep normative type syntax, inference, generalization, rows, traits, effects,
advanced checking, typed-core verification, metatheory targets, diagnostics,
and conformance requirements here. Normative nominal datatype and pattern rules are
defined by the sibling [Data and Pattern Specification](../data-and-patterns/README.md);
the normative [Clause Condition Specification](../clause-conditions/README.md)
uses the fixed `Bool` and `Int` types without changing inference or adding body
refinement. Handler rules remain partial unless a chapter explicitly
incorporates them.

Document authority and rendered content labels follow the repository
[Specification Authority](../../SPECIFICATION-AUTHORITY.md).
Requirement words, behavior classes, permitted variation, limits, and profile
disclosure follow the repository
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md).
Portable minima, finite-resource measurement, and exhaustion reporting follow
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).

Every chapter is `normative`. The historical C001 run exercised these
semantics under the retired `0.1` protocol identifier. It remains semantic
evidence, but it is not evidence for the exact `0.1.1` wire identity. The hard
cutover and fresh cross-slice evidence requirement are recorded in
[Prototype Slice Renumbering](../../50-journal/2026-08-04-prototype-slice-renumbering.md).

## Variability register

| Governing rule | Classification and bound |
| --- | --- |
| [Type-System Overview — Two guarantee profiles](type-system-overview.md#two-guarantee-profiles) | Private principal-core inference and an optional candidate export-signature display are source/tool permissions; the written export signature remains mandatory. |
| [Principal Inference — Determinism and failure](principal-inference-and-generalization.md#determinism-and-failure) | Fresh names and equivalent constraint order are bounded unspecified presentation; alpha-equivalence, stable diagnostic identity, typed core, and artifact identity cannot change. |
| [Diagnostics — Diagnostic contract](diagnostics-and-conformance.md#diagnostic-contract) | Secondary spans are a `SHOULD` quality recommendation. A deviation needs a conformance-profile rationale and remains tracked by P117. |
| [Typed-Core Elaboration — BEAM-only backend boundary](typed-core-elaboration.md#beam-only-backend-boundary) | Original Catena locations and toolchain metadata are a `SHOULD` provenance recommendation. Missing source locations need a profile disposition and remain tracked by P117 and the source-file gaps. |
| [Metatheory — Normative claims](metatheory.md#normative-claims) | An explicit resource limit may refuse otherwise typable input only as an implementation limit, not as a semantic counterexample. The bootstrap profile publishes its current trait-resolution budget. |

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

> **Non-normative evidence.**

```bash
asdf exec mix compile --warnings-as-errors
asdf exec mix test
asdf exec mix escript.build
```

The exact environment, observations, and limits of the current run are in
[C001 Executable Type-System Conformance](../../50-journal/2026-08-01-c001-executable-type-system-conformance.md).
That record is historical; publication of the renumbered executable identity
awaits the migration gate linked above.

## Maintaining this index

Version related chapters together. A normative rule change requires a
conformance case, updated executable model where applicable, and an explicit
compatibility decision.
