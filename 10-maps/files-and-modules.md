---
title: "Files and Modules"
kind: map
created: "2026-08-21"
tags:
  - archive-navigation
  - catena
  - files
  - modules
aliases:
  - "Catena files map"
---

# Files and Modules

## Scope

This map connects the C013–C019 source stack and the one-module semantic
units that constrain the adopted file binding, the primary declared-name and
filename-derived evidence, the C020 decision artifacts, and the owners of
everything the file layer deliberately does not decide.

## Start here

- [Catena Files and Modules](../20-notes/catena-files-and-modules.md)
  develops the at-most-one module rule, basename verification, the `.cat`
  extension, ASCII module words, and the generated-file marker.
- [Resolved file-unit inquiry](../40-inquiries/how-should-catena-relate-files-to-modules.md)
  records the operational question, hypotheses, and resolution.
- [Files and Modules Specification](../60-specification/files-and-modules/README.md)
  is the normative version 0.1.16 contract.
- [C020 evidence record](../50-journal/2026-08-22-c020-files-and-modules.md)
  records the executable file-unit resolver and verification.
- [Operators and Punctuation map](operators-and-punctuation.md) fixes the
  token stream over which the file layer sits.

## Trails

### Foundations that constrain any answer

- [Formal Semantic Kernel](../60-specification/formal-semantic-kernel/canonical-kernel-syntax.md)
  fixes the one-`(module ...)` kernel unit with import digests.
- The retained JSON AST's single `"module"` field and its spelling align
  the file rule with the semantic frontends.
- [Source Text](../60-specification/source-text/README.md) and
  [Comments](../60-specification/comments-and-documentation-comments/README.md)
  supply the byte-accurate units and comment forms the marker rides on.

### Primary evidence

- [Erlang/OTP Modules and Code Loading](../30-sources/erlang-otp-modules-and-code-loading.md)
  supplies the declared-name-plus-basename precedent and generated-source
  mechanism on the target.
- [The Rust Reference: Crates and Modules](../30-sources/rust-project-2026-crates-and-modules.md)
  supplies the filename-derived contrast.
- [Haskell 2010 module findings](../30-sources/marlow-2010-haskell-language-report.md)
  supply the declared-header model with tooling file pairing and the
  `Main` defaulting to decline.

### Limits and traceability

- [Implementation Limits and Portability map](implementation-limits-and-portability.md)
  carries the aggregate-input policy that file-size limits defer to under
  G129.
- [Conformance Traceability](conformance-traceability.md) registers
  `FU-OBL-001` through `FU-OBL-012` against normative anchors and sibling
  compiler tests.

## Open questions

C020 is complete at revision `0.1.16`. P109 retains the
concrete module-header syntax; G022 retains import/export syntax over the C021
namespace rules;
C025 has since fixed package assembly, with cross-file duplicate handling owned by its tooling consumers; C027
has since fixed entry modules; G121/G128 retain build and reproducibility policy
for generated inputs.
