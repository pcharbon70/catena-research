---
title: "Trait and Categorical Operation Specification"
kind: map
created: "2026-08-02"
tags:
  - archive-navigation
  - category-theory
  - directory-index
  - specification
  - trait-constraints
aliases:
  - "Catena trait specification index"
---

# Trait and Categorical Operation Specification (`60-specification/traits-and-categorical-operations`)

## Purpose

These normative chapters define Catena 0.4 traits and its initial
category-inspired standard operations: their behavior-first vocabulary,
kinds, coherence, laws, derivation, execution, interface evidence, package
specialization, BEAM erasure, and conformance obligations.

## What belongs here

Keep rules for declaring, selecting, deriving, testing, specializing, and
executing trait-defined operations here. General effect handling, public
parser punctuation, collection-specific APIs, package distribution, proof
languages, cryptographic publisher identity, and law-directed optimization
remain in their own specification areas.

Document authority and rendered content labels follow the repository
[Specification Authority](../../SPECIFICATION-AUTHORITY.md).

Every chapter is `normative`. The implementation commit, merged compiler PR,
reproducible verification sequence, deterministic specialization evidence,
and direct-call artifact inspection are recorded in
[C004 Executable Trait Conformance](../../50-journal/2026-08-02-c004-executable-trait-conformance.md).

## Index

### Subdirectories

- None yet.

### Documents

- [Trait and Categorical Operation Overview](trait-and-categorical-operation-overview.md)
  — authority, scope, compiler boundary, guarantees, and exclusions.
- [Standard Hierarchy and Vocabulary](standard-hierarchy-and-vocabulary.md) —
  all seventeen public capabilities, formal reference names, kinds, parents,
  and actual method ABI.
- [Declarations, Instances, and Coherence](declarations-instances-and-coherence.md)
  — declarations, ownership, overlap, functional dependencies, associated
  types, parent evidence, termination, and ambiguity.
- [Laws, Derivation, and Testing](laws-derivation-and-testing.md) — law domains,
  evidence tiers, absence of rewrites, structural derivation, and bounded law
  checks.
- [Operational Semantics](operational-semantics.md) — strict order,
  multiplicity, subject placement, composition direction, divergence, early
  termination, concurrency, and stack safety.
- [Interfaces, Specialization, and BEAM](interfaces-specialization-and-beam.md)
  — digest-bound interfaces, standard hierarchy delivery, build manifests,
  verified template closure, specialization, deterministic output, and
  evidence erasure.
- [Trait Diagnostics and Conformance](diagnostics-and-conformance.md) — stable
  diagnostics, positive and negative corpus requirements, differential tests,
  compatibility checks, and promotion gates.

## Executable evidence

The sibling [Catena compiler](https://github.com/pcharbon70/catena) implements
JSON AST and interface version 0.4 at immutable commit
[`b69f6f7e3da6015bf9b3385152ca3f3687422472`](https://github.com/pcharbon70/catena/commit/b69f6f7e3da6015bf9b3385152ca3f3687422472),
merged by [PR #66](https://github.com/pcharbon70/catena/pull/66). It retains 0.2
and 0.3 interface decoding, uses an Elixir/OTP 29/BEAM-only toolchain, and
exercises the normative rules, including stack-safe standard `List` mapping
and reduction over 250,000 elements.

## Maintaining this index

Version these chapters together. A future lifecycle change must update the
compiler identity, conformance journal, C004 family checklist entries,
categorical inquiry, category-theory map, root specification index, and
affected cross-version rules atomically.
