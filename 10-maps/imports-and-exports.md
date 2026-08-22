---
title: "Imports and Exports"
kind: map
created: "2026-08-22"
tags:
  - archive-navigation
  - catena
  - imports
  - exports
  - modules
aliases:
  - "Catena imports map"
---

# Imports and Exports

## Scope

This map connects the kernel's explicit export and digest-backed import
precedent and the C002/C021 contracts that bound the adopted answer, the primary
Haskell/SML/Erlang/Rust boundary evidence, the C022 decision artifacts,
and the owners of everything the import layer deliberately does not
decide.

## Start here

- [Catena Imports and Exports](../20-notes/catena-imports-and-exports.md)
  develops explicit private-by-default exports, qualification-plus-list
  import admission, the declared exclusions, and the deny-able
  unused-import warning.
- [Resolved import inquiry](../40-inquiries/how-should-catena-handle-imports-and-exports.md)
  records the operational question, hypotheses, and resolution.
- [Imports and Exports Specification](../60-specification/imports-and-exports/README.md)
  is the normative version 0.1.18 contract.
- [C022 evidence record](../50-journal/2026-08-22-c022-imports-and-exports.md)
  records the executable validation and analysis and verification.
- [Namespaces and Shadowing map](namespaces-and-shadowing.md) fixes the
  precedence and collision rules imports feed.

## Trails

### Foundations that constrain any answer

- [Canonical Kernel Syntax](../60-specification/formal-semantic-kernel/canonical-kernel-syntax.md)
  fixes explicit export forms and digest-backed imports without
  wildcards.
- [Interfaces and Representation](../60-specification/data-and-patterns/interfaces-and-representation.md)
  fixes transparent versus abstract type export over layout-free
  interfaces.
- [Shadowing and Ambiguity](../60-specification/namespaces-and-shadowing/shadowing-and-ambiguity.md)
  fixes local-over-imported precedence and reference-time `NSP004`.
- [Editions and Feature Lifecycle](../60-specification/editions-and-feature-lifecycle/README.md)
  fixes the deny-able warning machinery `IMP001` joins.

### Primary evidence

- [Haskell 2010 import/export findings](../30-sources/marlow-2010-haskell-language-report.md)
  supply explicit lists, the empty qualified-only form, mention-time
  clashes, and the declined `hiding`/alias/re-export machinery.
- [The SML Definition](../30-sources/milner-et-al-1997-definition-standard-ml.md)
  supplies signature-controlled export surfaces.
- [Erlang/OTP Modules](../30-sources/erlang-otp-modules-and-code-loading.md)
  and [Rust crates](../30-sources/rust-project-2026-crates-and-modules.md)
  supply the qualification-only and re-export contrasts.

### Limits and traceability

- [Conformance Traceability](conformance-traceability.md) registers
  `IM-OBL-001` through `IM-OBL-013` against normative anchors and sibling
  compiler tests.
- [Implementation Limits and Portability map](implementation-limits-and-portability.md)
  carries the aggregate-input policy relevant to export-set validation
  under G129.

## Open questions

C022 is complete at revision `0.1.18`. G024 retains module recursion; G025 retains package identity, re-export
assembly, and duplicate-module rejection; G026 retains prelude contents;
G027 retains entry modules; P109 retains the concrete `use`/`export`
punctuation; P117 retains warning prose quality.
