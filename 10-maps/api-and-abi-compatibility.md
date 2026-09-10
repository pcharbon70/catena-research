---
title: "API and ABI Compatibility"
kind: map
created: "2026-08-24"
tags:
  - archive-navigation
  - catena
  - compatibility
  - api
  - abi
aliases:
  - "Catena compatibility map"
---

# API and ABI Compatibility

## Scope

This map connects the C002 interface and C008 lifecycle foundations
that pre-commit the compatibility shape, the C023 representation
exclusions and C024/C025 digest machinery whose meanings this slice
completes, the C026/C027 deferrals it resolves, the OTP and SemVer
evidence, the C028 decision artifacts — layered stances, the strict
diff matrix, minor-as-breaking under 0.x, the facade exclusion, the
claim validator — and the owners of migration, registry, and runtime
contracts.

## Start here

- [Catena API and ABI Compatibility](../20-notes/catena-api-and-abi-compatibility.md)
  develops the four layers, the breaking matrix, version meanings, the
  re-export closure, and the executable classifier.
- [Resolved compatibility inquiry](../40-inquiries/how-should-catena-define-api-and-abi-compatibility.md)
  records the operational question, hypotheses, and resolution.
- [API and ABI Compatibility Specification](../60-specification/api-and-abi-compatibility/README.md)
  is the normative version 0.1.24 contract.
- [Compatibility Suite](../60-specification/compatibility-suite/README.md)
  turns the layered contract into bounded, digest-bound executable evidence.
- [C028 evidence record](../50-journal/2026-08-24-c028-api-compat.md)
  records the executable classifier and verification.
- [Package Identity and Dependencies map](package-identity-and-dependencies.md)
  fixes the SemVer grammar and lock machinery whose meaning side
  completes here.

## Trails

### Foundations that constrain any answer

- [Feature Lifecycle and Compatibility](../60-specification/editions-and-feature-lifecycle/feature-lifecycle-and-compatibility.md)
  fixes the per-dimension change classification this slice finishes.
- [Interfaces and Representation](../60-specification/data-and-patterns/interfaces-and-representation.md)
  fixes the deterministic interface the diff matrix lives in.
- [Authority and Representation Exclusions](../60-specification/abstraction-boundaries/authority-and-representation-exclusions.md)
  fixes the representation exclusions this slice converts to decided
  absence.
- [Resolution and Lockfile](../60-specification/package-identity-and-dependencies/resolution-and-lockfile.md)
  fixes single-version resolution and digest identity — never
  compatibility surfaces.

### Evidence

- [Erlang/OTP Support, Compatibility, Deprecations, and Removal](../30-sources/erlang-otp-compatibility-and-upgrading.md)
  supplies the target runtime's tiered promises, explicit refusals,
  and deprecation-then-removal process.
- [Semantic Versioning](../30-sources/preston-werner-2013-semantic-versioning.md)
  and [Hex packages](../30-sources/hex-project-2026-packages.md)
  supply the numeric convention and ecosystem precedent.

### Deferrals resolved

- [Prelude Policy](prelude-policy.md) — prelude-bump meanings.
- [Entry Points](entry-points.md) — entry-set classification.
- [Module Dependency Cycles](module-dependency-cycles.md) — joint
  digests as identity, not surface.

### Limits and traceability

- [Conformance Traceability](conformance-traceability.md) registers
  `CP-OBL-001` through `CP-OBL-010` against normative anchors and
  immutable sibling compiler evidence.
- C116 owns historical migration, C130 registry status, C092 hot upgrade, and
  C121 build tooling. Representation, calling-convention, and foreign-term
  refinements remain with P093/P094/G095.

## Open questions

C028 is complete at revision `0.1.24`, and C136 adds bounded compatibility
evidence at `0.1.82` without choosing the future `1.0` convention. Any future
layout-stability contract belongs to P093/P094/G095 over this absence.
