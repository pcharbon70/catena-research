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
