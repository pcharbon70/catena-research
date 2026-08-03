---
title: "Language Specification"
kind: map
created: "2026-08-01"
tags:
  - archive-navigation
  - directory-index
  - specification
aliases:
  - "Normative language definition"
---

# Language Specification (`60-specification`)

## Purpose

This directory contains Catena's versioned candidate and normative language
rules. Research notes supply rationale and evidence; normative chapters
determine conformance, while candidate chapters state the contract being
tested for promotion.

## What belongs here

Put separately versioned candidate or normative specification areas and their local indexes here. A
chapter becomes `normative` only when its required executable evidence and
cross-references are present. Conflicts are resolved in this order: a newer
normative specification version, its linked conformance cases, then compiler
behavior. Compiler behavior alone never changes the language.

## Index

### Subdirectories

- [Effects and Handlers](effects-and-handlers/README.md) — the normative
  version 0.5 nominal request, lexical capability, identity-aware row, deep
  handler, affine resumption, typed-core, and effect-directed CPS contract.
- [Traits and Categorical Operations](traits-and-categorical-operations/README.md)
  — the normative version 0.4 behavior-first hierarchy, coherent evidence,
  laws, structural derivation, operational contracts, specialization, and
  BEAM erasure rules.
- [Clause Conditions](clause-conditions/README.md) — the normative version 0.3
  safe expression, reusable predicate, ordered guard-tree, coverage-fact,
  interface-evidence, BEAM lowering, and typed receive-harness contract.
- [Data and Patterns](data-and-patterns/README.md) — the normative version 0.2 nominal
  datatype, construction, pattern, match coverage, GADT, interface, layout,
  and derived-fold contract.
- [Type System](type-system/README.md) — the version 0.1 principal and
  annotation-directed static semantics, elaboration contract, and evidence.

### Documents

- None yet.

## Maintaining this index

Keep lifecycle state and versions explicit. Candidate chapters may record
local evidence but do not become authoritative until their immutable
conformance identity is published. Update the relevant research map, inquiry,
conformance evidence, and every affected index in the same change as a
normative rule.
