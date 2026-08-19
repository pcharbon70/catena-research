---
title: "Literal Grammar"
kind: map
created: "2026-08-18"
tags:
  - archive-navigation
  - bytes
  - catena
  - language-design
  - literals
  - syntax
  - text
aliases:
  - "Catena literal map"
---

# Literal Grammar

## Scope

This map connects C013–C016 source foundations, comparative literal systems,
the C017 atomic decision, its normative 0.1.13 contract, active C012 limits,
executable traceability, and the numeric/data/token questions deliberately
left open.

## Start here

- [Catena Literal Grammar](../20-notes/catena-literal-grammar.md) develops the
  atomic set, numeric spelling, string/byte model, provenance, rejected
  alternatives, and compatibility boundary.
- [Resolved literal inquiry](../40-inquiries/how-should-catena-spell-and-decode-literals.md)
  records the operational question and final choice.
- [Literal Grammar Specification](../60-specification/literal-grammar/README.md)
  is the normative version 0.1.13 contract.
- [C017 evidence record](../50-journal/2026-08-18-c017-literal-grammar.md)
  records the executable atomic scanner and verification.

## Trails

### Source and token ownership

- [Source Text Encoding and Normalization](source-text-encoding-and-normalization.md)
  supplies preserving logical scalars and original-byte spans.
- [Identifier and Name Security](identifier-and-name-security.md) supplies
  exact XID continuation for keyword and numeric suffix boundaries.
- [Whitespace, Layout, and Line Continuation](whitespace-layout-and-line-continuation.md)
  supplies the outside-token LF classifier that raw literal content bypasses.
- [Comments and Documentation Comments](comments-and-documentation-comments.md)
  supplies the parallel caller-indexed atomic comment boundary.

### Comparative literal systems

- [Rust Literal Tokens](../30-sources/rust-project-2026-literal-tokens.md)
  provides exact raw hashes, byte/text separation, escapes, and numeric token
  evidence.
- [Python 3.14 Lexical Analysis](../30-sources/python-software-foundation-2026-python-lexical-analysis.md)
  demonstrates the feature cross product of prefixes, quoting, raw strings,
  bytes, interpolation, based numbers, and separators.
- [Swift Lexical Structure](../30-sources/swift-project-2026-lexical-structure.md)
  provides extended delimiters and an interpolation opt-in comparison.

### Limits and conformance

- [Implementation Limits and Portability](implementation-limits-and-portability.md)
  supplies the `LIM002` mathematical-integer and `LIM004` decoded-payload
  portable floors.
- [Conformance Traceability](conformance-traceability.md) registers
  `LT-OBL-001` through `LT-OBL-012` against normative anchors and sibling
  compiler tests.
- [Approachable Catena Language Design](approachable-catena-language-design.md)
  places the literal surface inside the broader source-language program.

## Open questions

G018 must define numeric runtime types, defaulting, coercions, rounding,
overflow, exceptional values, and negative-expression elaboration. G019 and
P109 must combine C014–C017 into a complete token stream and grammar. G040,
G042, P093, and G097 retain atoms/symbols, collection forms, and BEAM-native
data. A future interpolation form requires a new prefix and explicit semantic
revision; 0.1.13 text remains static.
