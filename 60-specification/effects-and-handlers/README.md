---
title: "Effect and Handler Specification"
kind: map
created: "2026-08-02"
tags:
  - algebraic-effects
  - archive-navigation
  - directory-index
  - effect-handlers
  - specification
aliases:
  - "Catena effect specification index"
---

# Effect and Handler Specification (`60-specification/effects-and-handlers`)

## Purpose

These normative chapters define Catena 0.1.5 first-order effects and handlers:
nominal request families, behavior-first signatures, lexical capabilities,
identity-aware effect rows, named deep handlers, affine resumptions, typed
core, effect-directed CPS, BEAM execution, and conformance obligations.

## What belongs here

Keep rules for declaring, selecting, typing, handling, elaborating, and
lowering first-order requests here. Cleanup and resource scopes, exception
taxonomy, application host effects, structured concurrency, higher-order and
scoped operations, shallow handlers, and multi-shot resumptions remain outside
0.1.5.

Document authority and rendered content labels follow the repository
[Specification Authority](../../SPECIFICATION-AUTHORITY.md).

Every chapter is `normative`. The immutable sibling-compiler commit and
reproducible results are recorded in
[C005 Executable Effect Conformance](../../50-journal/2026-08-03-c005-executable-effect-conformance.md).
That historical evidence used the retired `0.1` through `0.5` identifiers. It
supports the unchanged semantics, but not the exact renumbered wire identities.
The hard cutover and fresh cross-slice evidence requirement are recorded in
[Prototype Slice Renumbering](../../50-journal/2026-08-04-prototype-slice-renumbering.md).
C005, C076, and C079 were completed atomically with that record; C077 and C078
are the earlier normative constraints preserved by 0.1.5.

## Index

### Subdirectories

- None yet.

### Documents

- [Effect and Handler Overview](effect-and-handler-overview.md) — authority,
  scope, public model, guarantees, and exclusions.
- [Declarations, Requests, and Signatures](declarations-requests-and-signatures.md)
  — nominal families, ordinary operation parameters, `request`, `uses`, and
  module-level handler declarations.
- [Capabilities, Rows, and Selection](capabilities-rows-and-selection.md) —
  lexical identities, unique inference, hybrid row equality, union,
  subtraction, and non-escape.
- [Deep Handlers and Affine Resumptions](deep-handlers-and-affine-resumptions.md)
  — evaluation order, forwarding, handler order, deep resume, clause effects,
  abort, and affine control.
- [Typed Core, CPS, and BEAM](typed-core-cps-and-beam.md) — explicit evidence,
  independent verification, reference semantics, effect-directed CPS, pure
  direct paths, and OTP 29 lowering.
- [Effect Diagnostics and Conformance](diagnostics-and-conformance.md) — stable
  diagnostic families, positive and negative corpora, differential traces,
  compatibility, and conformance identity requirements.

## Maintaining this index

Version these chapters together. A lifecycle change must update the compiler
identity, conformance journal, C005-family checklist entries, effect inquiry,
effect map, root specification index, and affected type-system rules
atomically.
