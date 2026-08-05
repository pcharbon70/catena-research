---
title: "Language Editions and Feature Lifecycle"
kind: map
created: "2026-08-05"
tags:
  - compatibility
  - language-design
  - migration
aliases:
  - "Catena editions map"
---

# Language Editions and Feature Lifecycle

## Scope

This map connects Catena's edition, exact revision, preview, compatibility,
migration, artifact, and compiler-bootstrap boundaries. It distinguishes
external evidence from the local synthesis and normative contract.

## Start here

- [Language Editions and Feature Lifecycle](../20-notes/language-editions-and-feature-lifecycle.md)
  explains the four version axes and the recommended package-local model.
- [How Should Catena Version Editions and Language Features?](../40-inquiries/how-should-catena-version-editions-and-language-features.md)
  records the operational question, accepted decisions, and bounded resolution.
- [Catena 0.1.7 Editions and Feature Lifecycle Specification](../60-specification/editions-and-feature-lifecycle/README.md)
  is the normative route through selection, lifecycle, artifacts,
  migration, diagnostics, and conformance.
- [C008 Edition and Feature-Lifecycle Conformance](../50-journal/2026-08-05-c008-edition-conformance.md)
  records the authorized immutable compiler identity, post-commit checks,
  artifact hashes, promotion result, and release-packaging limitation.

## Trails

### Package-local compatibility

[The Rust Edition Guide](../30-sources/rust-project-edition-guide.md) motivates
independent package selection, retained earlier editions, interoperable
dependencies, and conservative migration. Catena adapts those properties to
major/minor editions and exact revisions.

### Version meanings

[Semantic Versioning 2.0.0](../30-sources/preston-werner-2013-semantic-versioning.md)
supplies the post-1.0 compatibility vocabulary. The Catena synthesis adds the
pre-1.0 breaking-change record and distinguishes language from artifact and
compiler-package versions.

### Impermanent capabilities

[JEP 12](../30-sources/buckley-2018-preview-features.md) supplies evidence for
explicit opt-in, impermanent-but-complete features, and artifact marking.
Catena uses named previews, package manifests, semantic interfaces, and no
runtime edition switch.

### Existing authority and artifacts

[Specification Authority](../SPECIFICATION-AUTHORITY.md) governs chapter
applicability and conflict handling. The
[Specification and Governance map](language-integrated-specifications-and-governance.md)
connects the signed artifacts whose version domains must remain historically
verifiable.

## Remaining questions

The bounded C008 inquiry is resolved.
Broader API/ABI compatibility, long-term governance-schema migration,
file-edit application, ecosystem compatibility testing, and compiler
self-hosting retain separate checklist identities.
