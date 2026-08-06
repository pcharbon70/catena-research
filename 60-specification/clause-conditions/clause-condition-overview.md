---
title: "Clause Condition Overview"
kind: specification
created: "2026-08-02"
status: normative
spec_version: "0.1.3"
tags:
  - catena
  - pattern-matching
  - specification
aliases:
  - "Catena 0.1.3 clause condition boundary"
---

# Clause Condition Overview

## Status and authority

This chapter and its eight sibling chapters are the normative Catena 0.1.3
clause-condition slice. They refine the conservative guard boundary in the
[0.1.2 data-and-pattern specification](../data-and-patterns/README.md) and use
the types fixed by the [0.1.1 type-system specification](../type-system/README.md).

Requirement words, invalidity, permitted variation, limits, and explicit
failures follow the repository
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md). These
chapters are backed by published executable evidence at Catena compiler commit
[`165fc4837f101d01016248e62479ef4caa0f20ce`](https://github.com/pcharbon70/catena/commit/165fc4837f101d01016248e62479ef4caa0f20ce).
The 0.1.3 condition rules explicitly apply where 0.1.2 left nonliteral condition
behavior conservative; the 0.1.2 structural pattern rules remain applicable.
Document status, content labels, rule references, and conflict handling follow
the repository
[Specification Authority](../../SPECIFICATION-AUTHORITY.md).

## User-facing model

A clause condition answers one approachable question: “After this pattern
matches, should this clause run?” The source forms below demonstrate the model
without fixing parser punctuation or layout:

> **Non-normative example.**

```catena
condition positive(value: Int) -> Bool = value > 0

classify(value: Int) -> Int
classify(value) when positive(value) -> 1
classify(0) -> 0
classify(value) when value < 0 -> -1
```

`condition` distinguishes reusable selection predicates from unrestricted
functions. `when` attaches one Boolean expression to one clause. The temporary
JSON AST used by the bootstrap compiler is an implementation input and does
not freeze punctuation, annotation placement, or layout in the eventual
parser.

## Guarantees

Version 0.1.3 provides:

- Boolean-only conditions over immutable pattern and lexical bindings;
- a closed, total, deterministic, empty-effect expression fragment;
- lazy left-to-right `and` and `or`;
- exact Boolean and integer equality plus a defined integer arithmetic and
  ordering subset;
- explicitly signed, first-order, non-recursive reusable condition predicates;
- explicit condition imports carrying canonical, digest-bound bodies;
- one condition evaluation after structural success;
- false fallthrough and irreversible commitment before body evaluation;
- a typed ordered guard tree shared by checking, verification, and lowering;
- conservative exhaustiveness and redundancy reasoning over Boolean formulas
  and integer difference constraints;
- native and ordinary BEAM lowering with equivalent source observations; and
- a native-only typed lowering harness for selective receive.

Condition truth does not refine the ordinary Hindley–Milner type environment
inside the body. It affects clause selection and certified coverage only.

## Compiler boundary

The executable bootstrap accepts JSON AST 0.1.3 and follows this path:

> **Non-normative diagram.**

```mermaid
flowchart LR
    A[JSON AST 0.1.3] --> D[Decode declarations and clauses]
    D --> S[Check explicit condition signatures]
    S --> N[Normalize safe condition core]
    N --> T[Infer and check typed clauses]
    T --> F[Recheck coverage facts]
    F --> G[Build ordered guard tree]
    G --> V[Independent typed-core verifier]
    V --> L[Native or ordinary lowering]
    L --> E[Erlang Abstract Format]
    E --> O[OTP 29 compile:noenv_forms]
    O --> B[BEAM plus version 0.1.3 interface]
```

The compiler MUST use OTP's supported Abstract Format compiler interface as
the `.beam` generation boundary. A conforming implementation may have another
front end or implementation language, but it MUST preserve the typed core,
condition evidence, selection semantics, and observable BEAM behavior fixed by
these chapters.

## Deliberate exclusions

Version 0.1.3 does not add:

- unrestricted function calls, recursion, termination proofs, or higher-order
  values inside conditions;
- division, remainder, indexing, lookup, decoding, foreign calls, or another
  partial primitive;
- trait-dispatched equality, ordering, or arithmetic;
- effects, handlers, sends, receives, spawning, time, or randomness inside a
  condition;
- condition-established occurrence typing or result refinements;
- pattern guards, local guard bindings, programmable views, or handler guards;
- a public receive expression, timeout semantics, mailbox protocol type, or
  actor effect calculus; or
- an external SMT solver or acceptance-changing unchecked assertion.

Those are explicit boundaries. Later versions MUST specify them rather than
silently broadening the meaning of a 0.1.3 condition.

## Connections (non-normative)

The design rationale and primary-source trail remain in
[Clause Guards](../../20-notes/clause-guards.md) and its
[topic map](../../10-maps/clause-guards.md). The exact published implementation
observations are in the [C003 journal entry](../../50-journal/2026-08-02-c003-executable-clause-condition-conformance.md).
