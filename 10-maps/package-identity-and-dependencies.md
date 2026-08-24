---
title: "Package Identity and Dependencies"
kind: map
created: "2026-08-24"
tags:
  - archive-navigation
  - catena
  - packages
  - versioning
aliases:
  - "Catena packages map"
---

# Package Identity and Dependencies

## Scope

This map connects the C008 manifest and C024 component digests that bounded
any package model, the SemVer grammar and Hex requirement evidence, the
C025 decision artifacts — dependencies field, version operators,
single-version resolution, `catena.lock`, registry-neutral identity with
a Hex transport profile — and the owners of what stays outside this
slice.

## Start here

- [Catena Package Identity and Dependencies](../20-notes/catena-package-identity-and-dependencies.md)
  develops the declaration form, SemVer grammar, exact/caret/tilde
  semantics with the Cargo-style 0.x rule, single-version resolution, the
  generated lockfile, and (name, version, bundle digest) identity.
- [Resolved package inquiry](../40-inquiries/how-should-catena-define-package-identity-and-dependency-resolution.md)
  records the operational question, hypotheses, and resolution.
- [Package Identity and Dependencies Specification](../60-specification/package-identity-and-dependencies/README.md)
  is the normative version 0.1.21 contract.
- [C025 evidence record](../50-journal/2026-08-24-c025-package-identity.md)
  records the executable dependency engine and verification.
- [Module Dependency Cycles map](module-dependency-cycles.md) fixes the
  component joint digests the lockfile records.

## Trails

### Foundations that constrain any answer

- [Edition Selection and Applicability](../60-specification/editions-and-feature-lifecycle/edition-selection-and-applicability.md)
  fixes the manifest that gains `dependencies` and the
  no-selection-inheritance rule.
- [SCC Admission and Resolution](../60-specification/module-dependency-cycles/scc-admission-and-resolution.md)
  fixes component joint digests.
- [Claims, Examples, and Checking](../60-specification/specifications-and-governance/claims-examples-and-checking.md)
  fixes the JCS and SHA-256 machinery identity reuses.
- [Canonical Kernel Syntax](../60-specification/formal-semantic-kernel/canonical-kernel-syntax.md)
  fixes the `origin::module::name` identity that mandates one version per
  name.

### Evidence

- [Semantic Versioning 2.0.0](../30-sources/preston-werner-2013-semantic-versioning.md)
  supplies the version grammar and precedence.
- [Hex Package Manager: Packages and Requirements](../30-sources/hex-project-2026-packages.md)
  supplies the transport profile's operators and pre-release default.
- [Package Publishing Hypothesis: Hex Registry](../00-inbox/package-publishing-hypothesis-hex.md)
  supplies the registry direction.

### Limits and traceability

- [Conformance Traceability](conformance-traceability.md) registers
  `PK-OBL-001` through `PK-OBL-012` against normative anchors and
  sibling compiler tests.
- [Implementation Limits and Portability map](implementation-limits-and-portability.md)
  carries the specialization bound package linking already uses.

## Open questions

C025 is complete at revision `0.1.21`. G121 retains build and fetch tooling; G128 retains
reproducible-build consumption; G130 retains supply-chain signing and
threat modeling; G028 retains compatibility policy and the re-export
facades re-owned by its era; G026 and G027 retain prelude and entry-point
decisions.
