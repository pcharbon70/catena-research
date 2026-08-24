---
title: "Entry Points"
kind: map
created: "2026-08-24"
tags:
  - archive-navigation
  - catena
  - entry-points
aliases:
  - "Catena entry points map"
---

# Entry Points

## Scope

This map connects the C010 completion rule and C026 zero-implicit-names
guarantee that pre-commit the entry shape, the C025 package machinery
entries ride, the OTP applications precedent in both its useful and
heavyweight directions, the C027 decision artifacts — named entry
exports, effect-closure, invocation-only startup, return-is-shutdown,
derived libraries — and the owners of supervision, tooling, and
compatibility.

## Start here

- [Catena Entry Points](../20-notes/catena-entry-points.md) develops
  the manifest `entries` field, effect-closure, invocation-only
  startup, return-is-shutdown, and the derived library distinction.
- [Resolved entry-points inquiry](../40-inquiries/how-should-catena-define-entry-points-and-application-structure.md)
  records the operational question, hypotheses, and resolution.
- [Package Identity and Dependencies map](package-identity-and-dependencies.md)
  fixes the manifest machinery entries extend.

## Trails

### Foundations that constrain any answer

- [Canonical Kernel Syntax](../60-specification/formal-semantic-kernel/canonical-kernel-syntax.md)
  fixes the strict invocation semantics and the completion rule
  entries obey.
- [Prelude Selection and Admission](../60-specification/prelude-policy/prelude-selection-and-admission.md)
  fixes the zero-implicit-names guarantee a reserved `main` would
  break.
- [Manifest Dependencies and Versions](../60-specification/package-identity-and-dependencies/manifest-dependencies-and-versions.md)
  fixes the optional-field pattern `entries` follows.
- [Processes and Concurrency](../60-specification/effects-and-handlers/README.md)
  fixes the handler semantics whose closure entries require.

### Evidence

- [Erlang/OTP Applications](../30-sources/erlang-otp-applications.md)
  supplies the target-runtime precedent: package-shaped units, derived
  libraries, and the supervision-first startup Catena declines for
  0.1.

### Limits and traceability

- [Conformance Traceability](conformance-traceability.md) will register
  `EN-OBL-001` through `EN-OBL-010` against normative anchors and
  sibling compiler tests.
- [Approachable Catena Language Design](approachable-catena-language-design.md)
  holds the application-shape context a future `catena run` serves.

## Open questions

C027 is complete at revision `0.1.23`. G084 and G089 retain
supervision and process lifetime; G088 retains cancellation; G121
retains the CLI and host-process boundary; G028 retains the
compatibility meaning of entry-set changes.
