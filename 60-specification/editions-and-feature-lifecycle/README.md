---
title: "Editions and Feature Lifecycle Specification"
kind: map
created: "2026-08-05"
tags:
  - archive-navigation
  - compatibility
  - directory-index
  - specification
aliases:
  - "Catena 0.1.7 edition specification index"
---

# Editions and Feature Lifecycle Specification (`60-specification/editions-and-feature-lifecycle`)

## Purpose

These normative chapters define Catena 0.1.7's package-local edition,
exact-revision, preview, compatibility, deprecation, migration, artifact, and
governance contract.

## What belongs here

Keep the bounded language-selection registry, cumulative applicability rules,
feature lifecycle, normalized interface obligations, selection-aware artifact
formats, migration records, diagnostics, and conformance gate here. Detailed
source/API/ABI evolution, general governance-schema evolution, edit
application, the ecosystem compatibility suite, and compiler self-hosting
remain separate work.

Document authority and rendered content labels follow the repository
[Specification Authority](../../SPECIFICATION-AUTHORITY.md). All four chapters
are `normative`. Their coordinated promotion is supported by the immutable
compiler identity and reproducible evidence described in
[Migration, Diagnostics, and Conformance](migration-diagnostics-and-conformance.md#promotion-gate)
and the linked conformance journal.
Requirement words, behavior classes, permitted variation, limits, and profile
disclosure follow the repository
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md).

## Variability register

| Governing rule | Classification and bound |
| --- | --- |
| [Edition Selection and Applicability — Package selection](edition-selection-and-applicability.md#package-selection) | A frontend schema `MAY` differ from the selected language revision, but decoded forms are checked against the exact package selection. |
| [Edition Selection and Applicability — Standalone and interactive selection](edition-selection-and-applicability.md#standalone-and-interactive-selection) | A legacy frontend `MAY` imply its historical revision with mandatory `EDN002` disclosure. The bootstrap profile records that this compatibility inference is enabled. |
| [Edition Selection and Applicability — Prototype compatibility boundary](edition-selection-and-applicability.md#prototype-compatibility-boundary) | A later 0.1 patch `MAY` contain a documented breaking change only at a revision boundary with the required migration and lifecycle record. |
| [Feature Lifecycle and Compatibility — Preview selection](feature-lifecycle-and-compatibility.md#preview-selection) | A semantics-preserving stale-preview removal edit is a `SHOULD` migration-quality recommendation. The bootstrap deviation is tracked by P125. |
| [Feature Lifecycle and Compatibility — Deprecation and removal](feature-lifecycle-and-compatibility.md#deprecation-and-removal) | Diagnostic or governance policy `MAY` deny a deprecation warning, transactionally failing the build. |
| [Feature Lifecycle and Compatibility — Package-local interoperation](feature-lifecycle-and-compatibility.md#package-local-interoperation) | Retained editions `MAY` coexist as dependencies through verified semantic interfaces; different selections `MAY` change compile metadata and artifact digests but never introduce runtime selection dispatch. |
| [Interfaces, Artifacts, and Governance — BEAM metadata and erasure](interfaces-artifacts-and-governance.md#beam-metadata-and-erasure) | Selection metadata `MAY` remain only in the non-executable compile-information chunk. The bootstrap profile records that it is emitted. |
| [Interfaces, Artifacts, and Governance — Optional governance constraints](interfaces-artifacts-and-governance.md#optional-governance-constraints) | Governance `MAY` narrow an otherwise valid selection but cannot admit a selection or diagnostic state rejected by language rules. |

## Index

### Subdirectories

- None yet.

### Documents

- [Edition Selection and Applicability](edition-selection-and-applicability.md)
  — version axes, package and standalone selection, exact pins, cumulative
  normative applicability, retention, and the prototype boundary.
- [Feature Lifecycle and Compatibility](feature-lifecycle-and-compatibility.md)
  — preview, stable, withdrawn, deprecated, and removed states; transition
  rules; SemVer policy; and package-local interoperation.
- [Interfaces, Artifacts, and Governance](interfaces-artifacts-and-governance.md)
  — public preview propagation, edition-neutral interfaces, BEAM metadata,
  cache and assurance binding, version-aware signatures, and optional policy.
- [Migration, Diagnostics, and Conformance](migration-diagnostics-and-conformance.md)
  — machine-readable change records, safe edit suggestions, stable
  diagnostics, legacy behavior, adversarial tests, and the promotion gate.

## Maintaining this index

Version the chapters together. Every edition, revision, feature transition,
compatibility classification, or artifact-field change must update the
registry, migration record, compiler implementation, guides, conformance
evidence, authority policy, checklist, map, inquiry, and affected indexes in
one coordinated change.
