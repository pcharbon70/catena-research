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

The repository-level [Specification Authority](../SPECIFICATION-AUTHORITY.md)
defines document status, rendered content labels, rule references, and
conflict handling independently of Catena language versions.

## What belongs here

Put separately versioned candidate or normative specification areas and their local indexes here. A
chapter becomes `normative` only when its required executable evidence and
cross-references are present. A version number, conformance case, executable
reference, or compiler behavior never overrides normative text by itself. An
explicit normative applicability or replacement statement is required when
language chapters overlap.

The C001 through C006 chapters retain normative semantic status through the
identifier-only `0.1.1` through `0.1.6` migration. Their historical commits
remain semantic evidence, while the exact renumbered protocol identity awaits
the fresh gate in
[Prototype Slice Renumbering](../50-journal/2026-08-04-prototype-slice-renumbering.md).

## Index

### Subdirectories

- [Specifications and Governance](specifications-and-governance/README.md) —
  the normative version 0.1.6 typed-rule, exact-example, additive-policy,
  offline-trust, lifecycle, artifact-binding, and total-erasure contract.
- [Effects and Handlers](effects-and-handlers/README.md) — the normative
  version 0.1.5 nominal request, lexical capability, identity-aware row, deep
  handler, affine resumption, typed-core, and effect-directed CPS contract.
- [Traits and Categorical Operations](traits-and-categorical-operations/README.md)
  — the normative version 0.1.4 behavior-first hierarchy, coherent evidence,
  laws, structural derivation, operational contracts, specialization, and
  BEAM erasure rules.
- [Clause Conditions](clause-conditions/README.md) — the normative version 0.1.3
  safe expression, reusable predicate, ordered guard-tree, coverage-fact,
  interface-evidence, BEAM lowering, and typed receive-harness contract.
- [Data and Patterns](data-and-patterns/README.md) — the normative version 0.1.2 nominal
  datatype, construction, pattern, match coverage, GADT, interface, layout,
  and derived-fold contract.
- [Type System](type-system/README.md) — the version 0.1.1 principal and
  annotation-directed static semantics, elaboration contract, and evidence.

### Documents

- None yet.

## Maintaining this index

Keep lifecycle state and versions explicit. Candidate chapters may record
local evidence but do not become authoritative until their immutable
conformance identity is published. A recorded identifier-only migration of an
already normative slice may preserve its semantic authority while requiring a
fresh executable protocol identity. Update the relevant research map, inquiry,
conformance evidence, and every affected index in the same change as a
normative rule. Keep every fenced block and every non-normative section visibly
classified according to the
[Specification Authority](../SPECIFICATION-AUTHORITY.md).
