---
title: "How Should Catena Version Editions and Language Features?"
kind: inquiry
created: "2026-08-05"
status: resolved
tags:
  - compatibility
  - language-design
  - migration
  - specification
aliases:
  - "Catena C008 inquiry"
---

# How Should Catena Version Editions and Language Features?

## Why this matters

Catena already names cumulative prototype slices, serialized interfaces,
governance records, and compiler releases. Without an explicit relationship
among those identities, a package cannot state which semantics it expects,
and a compiler cannot explain whether a change is compatible, preview-only,
deprecated, removed, or merely a new encoding.

## Operational question

A successful answer must let a package select one reproducible language,
permit independently migrating dependencies to interoperate, bind all
compile-time artifacts to that selection, preserve historical verification,
and give both people and tools an unambiguous migration path. The model is not
complete until malformed, stale, missing, downgraded, and preview-dependent
cases have deterministic compiler outcomes.

## Working hypotheses

- A `major.minor` edition plus an exact `major.minor.patch` revision separates
  compatibility identity from reproducible semantics.
- Package-local selection and normalized interfaces avoid ecosystem-wide
  lockstep migration.
- Named previews are more approachable than an undifferentiated “unstable”
  mode and make public dependency propagation precise.
- Migration should expose structured safe edits without applying uncertain
  transformations.
- Version-aware signature domains can preserve 0.1.6 evidence while binding
  the richer 0.1.7 identity.

## Paths to explore

- Compare package-local editions and conservative migration in the
  [Rust Edition Guide](../30-sources/rust-project-edition-guide.md).
- Compare release-bound impermanent capabilities in
  [JEP 12](../30-sources/buckley-2018-preview-features.md).
- Separate Catena's language promises from the generic rules in
  [Semantic Versioning 2.0.0](../30-sources/preston-werner-2013-semantic-versioning.md).
- Exercise selection, interfaces, signatures, governance, and BEAM metadata in
  the clean compiler rewrite.

## Findings

The bounded design selects edition `0.1`, exact cumulative revisions, required
manifest fields, retained old pins, a five-state feature lifecycle, one-revision
minimum deprecation in 0.1, standard post-1.0 compatibility meanings, named
package previews, public-use propagation, structured non-mutating fixes, and
version-aware signature domains. The synthesis is recorded in
[Language Editions and Feature Lifecycle](../20-notes/language-editions-and-feature-lifecycle.md).

Compiler self-hosting is not an edition synonym. It needs a separate late-0.x
bootstrap gate after Catena can express its parser, module compiler, required
tool effects, diagnostics, and reproducible build chain. That work is tracked
as G141 in the
[completeness checklist](../00-inbox/language-specification-completeness-checklist.md#16-formal-validation-and-release-gates).

## Outcome

The design question is resolved for the bounded 0.1.7 slice. Archive
validation and the compiler's positive and adversarial suites pass against the
authorized immutable compiler identity, as recorded in the
[C008 conformance journal](../50-journal/2026-08-05-c008-edition-conformance.md).
The normative contract lives in the
[Catena 0.1.7 Editions and Feature Lifecycle Specification](../60-specification/editions-and-feature-lifecycle/README.md).

Broader API/ABI compatibility, long-term governance-schema migration,
transactional edit application, ecosystem compatibility testing, reproducible
release packaging, and compiler self-hosting remain separately identified
work; they do not reopen this bounded inquiry.
