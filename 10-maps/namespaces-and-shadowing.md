---
title: "Namespaces and Shadowing"
kind: map
created: "2026-08-22"
tags:
  - archive-navigation
  - catena
  - language-design
  - namespaces
aliases:
  - "Catena namespaces map"
---

# Namespaces and Shadowing

## Scope

This map connects the kernel's fixed namespace law and the C014/C019/C020
spelling, qualification, and module constraints that bound the adopted answer, the
primary Haskell/SML namespace evidence, the C021 decision artifacts, and
the owners of everything the namespace layer deliberately does not decide.

## Start here

- [Catena Namespaces and Shadowing](../20-notes/catena-namespaces-and-shadowing.md)
  develops the per-category inventory with spelling classes, the
  deterministic silent-shadowing model, type-variable scoping,
  local-over-imported precedence with collision rejection, and governance
  separation.
- [Resolved namespace inquiry](../40-inquiries/how-should-catena-organize-namespaces-and-shadowing.md)
  records the operational question, hypotheses, and resolution.
- [Namespaces and Shadowing Specification](../60-specification/namespaces-and-shadowing/README.md)
  is the normative version 0.1.17 contract.
- [C021 evidence record](../50-journal/2026-08-22-c021-namespaces-and-shadowing.md)
  records the executable scope-event resolver and verification.
- [Files and Modules map](files-and-modules.md) fixes the flat module
  names two-segment qualification rides on.

## Trails

### Foundations that constrain any answer

- [Canonical Kernel Syntax](../60-specification/formal-semantic-kernel/canonical-kernel-syntax.md)
  fixes the two spelling classes, per-namespace duplicate rejection, flat
  constructor uniqueness, lexical shadowing, and no-wildcard imports.
- [Identifier Specification](../60-specification/identifiers/README.md)
  fixes spelling identity and the C014 qualification separator.
- [Operators and Punctuation](../60-specification/operators-and-punctuation/token-inventory-and-maximal-munch.md)
  fixes `.`-joined qualified names as single tokens.
- [Specifications and Governance](../60-specification/specifications-and-governance/README.md)
  types the governed identities that must stay out of program namespaces.

### Primary evidence

- [Haskell 2010 namespace findings](../30-sources/marlow-2010-haskell-language-report.md)
  supply six name kinds, two spelling classes, silent shadowing, and
  qualification as the escape.
- [SML Definition namespace findings](../30-sources/milner-et-al-1997-definition-standard-ml.md)
  supply per-category environments, identifier status, and flat
  constructor namespaces.
- [Erlang/OTP Modules](../30-sources/erlang-otp-modules-and-code-loading.md)
  and [OCaml 5.4](../30-sources/ocaml-5-4-expressions-and-pattern-guards.md)
  supply the flat-namespace and order-based-shadowing contrasts.

### Limits and traceability

- [Conformance Traceability](conformance-traceability.md) registers
  `NS-OBL-001` through `NS-OBL-014` against normative anchors and sibling
  compiler tests.
- [Implementation Limits and Portability map](implementation-limits-and-portability.md)
  carries the aggregate-input policy relevant to scope-event streams under
  G129.

## Open questions

C021 is complete at revision `0.1.17`. G022 retains
import/export syntax and visibility defaults; C024 has admitted module
recursion; G025 retains package-level module uniqueness; G026 retains
prelude contents; G066 retains type-directed resolution questions; P109
retains the declaration grammar that emits scope events.
