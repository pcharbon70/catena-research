---
title: "Module Dependency Cycles"
kind: map
created: "2026-08-24"
tags:
  - archive-navigation
  - catena
  - modules
  - separate-compilation
aliases:
  - "Catena module cycles map"
---

# Module Dependency Cycles

## Scope

This map connects the digest-bound import model whose circularity
motivated the design, the Haskell recursion evidence with its named
price, the SML/Erlang DAG contrasts, the C024 decision artifacts that
admitted strongly-connected components with their two resolution regimes
and consequence confirmations, and the owners of what stays outside the
slice.

## Start here

- [Catena Dependency Cycles](../20-notes/catena-dependency-cycles.md)
  develops SCC admission, signature-based intra-component resolution,
  joint digests, the three consequence clauses, and the inversion
  alternative.
- [Resolved cycles inquiry](../40-inquiries/how-should-catena-handle-module-dependency-cycles.md)
  records the operational question, hypotheses, and resolution.
- [Module Dependency Cycles Specification](../60-specification/module-dependency-cycles/README.md)
  is the normative version 0.1.20 contract.
- [C024 evidence record](../50-journal/2026-08-24-c024-dependency-cycles.md)
  records the executable SCC grouping, component compilation, and
  verification.
- [Imports and Exports map](imports-and-exports.md) fixes the cross-SCC
  regime the design leaves unchanged.

## Trails

### Foundations that constrain any answer

- [Canonical Kernel Syntax](../60-specification/formal-semantic-kernel/canonical-kernel-syntax.md)
  fixes the digest-bound import form and definition-only modules.
- [Import Declarations and Admission](../60-specification/imports-and-exports/import-declarations-and-admission.md)
  fixes digest-bound admission and defers context acquisition to
  G025/G121 — the grouping this design supplies.
- [Declarations and Nominal Identity](../60-specification/data-and-patterns/declarations-and-nominal-identity.md)
  fixes intra-module recursive groups cycles must not touch.
- [Editions and Feature Lifecycle](../60-specification/editions-and-feature-lifecycle/README.md)
  fixes the digest-addressed caches SCC units extend.

### Evidence

- [Haskell 2010 recursion findings](../30-sources/marlow-2010-haskell-language-report.md)
  ground mutual recursion as a specified feature with the
  signatures-and-group-units price.
- [The SML Definition](../30-sources/milner-et-al-1997-definition-standard-ml.md)
  and [Erlang/OTP modules](../30-sources/erlang-otp-modules-and-code-loading.md)
  ground the non-recursive and inversion-only contrasts.

### Limits and traceability

- [Conformance Traceability](conformance-traceability.md) registers
  `CY-OBL-001` through `CY-OBL-010` against normative anchors and
  sibling compiler tests.
- [Implementation Limits and Portability map](implementation-limits-and-portability.md)
  carries the aggregate-input policy relevant to multi-module SCC
  checking under G129.

## Open questions

C024 is complete at revision `0.1.20`. G025 retains package
assembly and lockfile representation of joint digests; P109 retains the
concrete recursive `use` surface; G028 retains joint-digest compatibility
treatment; the pre-declared-interface alternative stays available to a
future revision.
