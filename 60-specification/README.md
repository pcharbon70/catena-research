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
The companion
[Catena Conformance Vocabulary](../CONFORMANCE-VOCABULARY.md) defines
requirement force, behavior and failure classes, visible variability
declarations, limits, explicit traps, and implementation profiles across every
normative area.
The repository-level
[Catena Implementation Limits and Portability](../IMPLEMENTATION-LIMITS.md)
defines portable minima, machine-readable reporting, finite-resource
measurement, and exhaustion obligations without adding language semantics.

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
The normative C008 boundary is `0.1.7`; its explicitly authorized immutable
compiler evidence is recorded in the linked conformance journal. The
normative C010 formal semantic kernel is version `0.1.8`; its explicitly
authorized immutable compiler evidence is recorded in the
[C010 conformance journal](../50-journal/2026-08-06-c010-formal-semantic-kernel.md).
C012 governs finite implementation resources across these areas without
changing their normative status or consuming a language revision; its
[evidence record](../50-journal/2026-08-17-c012-implementation-limits.md)
preserves the coordinated compiler identity.
The normative C013 source-text envelope is version `0.1.9`; its strict UTF-8,
newline, normalization, location, and executable evidence are recorded in the
[C013 conformance journal](../50-journal/2026-08-17-c013-source-text-encoding-and-normalization.md).

## Index

### Subdirectories

- [Source Text](source-text/README.md) — the normative version 0.1.9 strict
  UTF-8, BOM, logical-newline, normalization-preservation, original-byte
  location, diagnostics, and conformance contract.
- [Formal Semantic Kernel](formal-semantic-kernel/README.md) — the normative
  version 0.1.8 exact S-expression syntax, row and process typing, sequential
  and actor dynamics, metatheory, BEAM correspondence, diagnostics, and
  completed promotion record.
- [Editions and Feature Lifecycle](editions-and-feature-lifecycle/README.md) —
  the normative version 0.1.7 package-local edition, exact-revision, preview,
  compatibility, migration, diagnostics, selection-bound artifact, and
  version-aware governance contract.
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
[Specification Authority](../SPECIFICATION-AUTHORITY.md). Keep each area's
variability register and all normative wording aligned with the
[Catena Conformance Vocabulary](../CONFORMANCE-VOCABULARY.md).
Keep finite resource boundaries and profile disclosures aligned with
[Catena Implementation Limits and Portability](../IMPLEMENTATION-LIMITS.md).
