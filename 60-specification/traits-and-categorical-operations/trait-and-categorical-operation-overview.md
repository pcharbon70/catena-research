---
title: "Trait and Categorical Operation Overview"
kind: specification
created: "2026-08-02"
status: normative
spec_version: "0.1.4"
tags:
  - category-theory
  - specification
  - trait-constraints
aliases:
  - "Catena 0.1.4 trait boundary"
---

# Trait and Categorical Operation Overview

## Status and authority

This chapter and its six sibling chapters are the normative Catena 0.1.4 trait
slice. They extend the [0.1.1 type system](../type-system/README.md), the
[0.1.2 data model](../data-and-patterns/README.md), and the
[0.1.3 clause-condition boundary](../clause-conditions/README.md). Requirement
words, invalidity, permitted variation, limits, and explicit failures follow
the repository
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md).

The historical immutable semantic evidence is recorded in
[C004 Executable Trait Conformance](../../50-journal/2026-08-02-c004-executable-trait-conformance.md).
It used the retired `0.1` through `0.4` identifiers; the fresh renumbered
executable-identity gate is recorded in
[Prototype Slice Renumbering](../../50-journal/2026-08-04-prototype-slice-renumbering.md).
Conflicts with compiler behavior are defects to resolve, not silent changes to
this specification or earlier normative versions.

Document status, content labels, rule references, and conflict handling follow
the repository
[Specification Authority](../../SPECIFICATION-AUTHORITY.md).

## User-facing model

Programmers ask for recognizable behaviors such as “can these values be
compared?”, “can I transform every item?”, or “can these steps be chained?”
The public traits therefore use behavior-first names. Formal category-theory
names appear once in reference material and metadata; they are not competing
aliases in source code.

An implementation states the behavior it provides, the compiler selects one
coherent implementation from types, and package linking replaces the selected
method with a direct specialized call. Trait evidence is never a runtime value
ordinary Catena code can inspect.

## Compiler boundary

The bootstrap boundary is versioned JSON AST 0.1.4, not a frozen source parser:

> **Non-normative diagram.**

```mermaid
flowchart LR
    A[JSON AST 0.1.4] --> K[Kind and declaration checking]
    K --> R[Coherent instance registry]
    R --> E[Compile-time evidence resolution]
    E --> I[Digest-bound interface and templates]
    I --> M[Explicit package build manifest]
    M --> S[Downstream specialization]
    S --> V[Independent core and template checks]
    V --> F[Erlang Abstract Format]
    F --> O[OTP 29 compile:noenv_forms]
    O --> B[Module BEAM plus one companion BEAM]
```

The compiler implementation remains Elixir. OTP 29's supported Erlang
Abstract Format compiler interface is the only `.beam` production boundary;
0.1.4 adds no Rust, Python, Core Erlang emitter, BEAM assembler, runtime
dictionary library, or second target VM.

## Guarantees

Version 0.1.4 provides:

- kind-aware traits over `Type`, `Type -> Type`, and
  `Type -> Type -> Type` parameters;
- the seventeen-capability hierarchy fixed in the
  [hierarchy chapter](standard-hierarchy-and-vocabulary.md);
- trait-or-type ownership, global non-overlap, deterministic ambiguity
  rejection, functional dependencies, and associated types;
- shared parent evidence across diamonds and terminating bounded resolution;
- law metadata with `promised`, `tested`, and `derived` evidence only;
- six explicit structural derivations with no operation override surface;
- strict, sequential, left-to-right operational contracts independent of
  algebraic laws;
- canonical, digest-bound standard and module interfaces;
- manifest-directed downstream specialization with verified helper closure;
  and
- direct BEAM calls after complete erasure of trait and law evidence.

## Deliberate exclusions

Version 0.1.4 does not add law-directed rewrites, runtime dictionary identity,
trait reflection, local overlapping instances, associated constants, a
general theorem language, `trusted` or `proved` user evidence, automatic
parallelism, cryptographic package signing, a source package manager, or
public parser syntax. Collection-specific short-circuiting remains a distinct
operation rather than a hidden property of mapping or reduction.

## Connections (non-normative)

The research rationale and evidence trail remain in
[Category Theory for Programming](../../20-notes/category-theory-for-programming.md),
the [categorical hierarchy inquiry](../../40-inquiries/how-should-catena-specify-its-initial-categorical-hierarchy.md),
and the [category-theory map](../../10-maps/category-theory-for-programming.md).
