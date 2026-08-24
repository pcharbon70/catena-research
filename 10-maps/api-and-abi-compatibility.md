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
  is the candidate version 0.1.24 contract.
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

- [Conformance Traceability](conformance-traceability.md) will
  register `CP-OBL-001` through `CP-OBL-010` against normative anchors
  and sibling compiler tests.
- Migration engines (G116/P125), registry retirement and yanks
  (G130), hot upgrade (G092), representation/calling-convention/
  foreign-term contracts (P093/G094/G095), and tooling (G121) remain
  the future owners.

## Open questions

C028 is complete at revision `0.1.24`. Whether 1.0 keeps the Cargo 0.x
rule's switch semantics belongs to the G136 edition-policy era; any
future layout-stability contract belongs to P093/G094/G095 over this
absence.
