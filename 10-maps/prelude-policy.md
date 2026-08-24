---
title: "Prelude Policy"
kind: map
created: "2026-08-24"
tags:
  - archive-navigation
  - catena
  - prelude
aliases:
  - "Catena prelude map"
---

# Prelude Policy

## Scope

This map connects the C021 precedence promise and C022 import machinery
that pre-commit the prelude's shape, the C025 package identity the
prelude rides, the Haskell fully-specified declined model, the C026
decision artifacts — opt-in selection, ordinary-origin precedence,
absent-means-out, the zero-implicit-names edition guarantee — and the
owners of contents, protocols, and tooling.

## Start here

- [Catena Prelude Policy](../20-notes/catena-prelude-policy.md) develops
  the manifest `prelude` field, ordinary import-class precedence,
  absent/`null` opt-out, the edition guarantee, and lockfile treatment.
- [Resolved prelude inquiry](../40-inquiries/how-should-catena-define-its-prelude-policy.md)
  records the operational question, hypotheses, and resolution.
- [Prelude Policy Specification](../60-specification/prelude-policy/README.md)
  is the normative version 0.1.22 contract.
- [C026 evidence record](../50-journal/2026-08-24-c026-prelude-policy.md)
  records the executable prelude wiring and verification.
- [Package Identity and Dependencies map](package-identity-and-dependencies.md)
  fixes the machinery a prelude selection reuses.

## Trails

### Foundations that constrain any answer

- [Shadowing and Ambiguity](../60-specification/namespaces-and-shadowing/shadowing-and-ambiguity.md)
  fixes the precedence and pre-commits "never a silent default."
- [Import Declarations and Admission](../60-specification/imports-and-exports/import-declarations-and-admission.md)
  fixes the origin class and diagnostics.
- [Resolution and Lockfile](../60-specification/package-identity-and-dependencies/resolution-and-lockfile.md)
  fixes identity, resolution, and lock pinning.
- [Canonical Kernel Syntax](../60-specification/formal-semantic-kernel/canonical-kernel-syntax.md)
  fixes the explicitness stance.

### Evidence

- [Haskell 2010 Prelude sections 5.6–5.6.2](../30-sources/marlow-2010-haskell-language-report.md)
  supply the fully-specified declined model with its ambiguity-transfer
  and frozen-core costs.

### Limits and traceability

- [Conformance Traceability](conformance-traceability.md) will register
  `PL-OBL-001` through `PL-OBL-010` against normative anchors and sibling compiler tests.
- [Approachable Catena Language Design](approachable-catena-language-design.md)
  holds the vocabulary context a future prelude serves.

## Open questions

C026 is complete at revision `0.1.22`. G101 retains contents and the name freeze; P102
retains collection protocols; G121 retains scaffolding defaults; G028
and G136 retain compatibility meanings of prelude version bumps.
