---
title: "Comments and Documentation Comments"
kind: map
created: "2026-08-18"
tags:
  - archive-navigation
  - catena
  - comments
  - documentation
  - language-design
  - syntax
aliases:
  - "Catena comments map"
---

# Comments and Documentation Comments

## Scope

This map connects C013 source units, C015 layout, comparative comment and
documentation systems, the C016 decision, its normative 0.1.12 contract, and
the later grammar and tooling work that will consume documentation metadata.

## Start here

- [Catena Comments and Documentation Comments](../20-notes/catena-comments-and-documentation-comments.md)
  develops the lexical, layout, attachment, Markdown, HTML, and doctest model.
- [Resolved comments inquiry](../40-inquiries/how-should-catena-handle-comments-and-documentation-comments.md)
  records the operational question and final choice.
- [Comments and Documentation Comments Specification](../60-specification/comments-and-documentation-comments/README.md)
  is the normative version 0.1.12 contract.
- [C016 evidence record](../50-journal/2026-08-18-c016-comments-and-documentation-comments.md)
  records the executable abstract scanner and resolver.

## Trails

### Input and layout foundations

- [Source Text Encoding and Normalization](source-text-encoding-and-normalization.md)
  supplies the preserving C013 logical-unit and original-byte-span boundary.
- [Whitespace, Layout, and Line Continuation](whitespace-layout-and-line-continuation.md)
  supplies the C015 classifier that receives every comment-internal LF.

### Comparative syntax and attachment

- [Rust Comments](../30-sources/rust-project-2026-rust-comments.md) provides the
  delimiter family, nested balancing, outer/inner distinction, and prefix edge
  cases.
- [Swift Lexical Structure](../30-sources/swift-project-2026-lexical-structure.md)
  reinforces the case for nested block comments.
- [ECMAScript Comments](../30-sources/ecma-international-2026-ecmascript-comments.md)
  shows why comment line terminators remain syntactically observable.
- [Elixir Writing Documentation](../30-sources/elixir-project-2026-writing-documentation.md)
  separates source comments, API documentation, and explicit doctest testing.

### Documentation format and conformance

- [CommonMark 0.31.2](../30-sources/macfarlane-2024-commonmark-specification.md)
  fixes the document grammar and exposes the raw-HTML trust boundary.
- [Conformance Traceability](conformance-traceability.md) registers
  `CM-OBL-001` through `CM-OBL-012` against normative anchors and compiler
  tests.
- [Approachable Catena Language Design](approachable-catena-language-design.md)
  places declaration documentation in the larger reader-facing language.

## Open questions

G019 must assign comment recognition among concrete token alternatives and
P109 must enumerate documentable declarations. G020 still owns file/module
attachment and generated-file behavior. G118 owns formatting preservation,
documentation rendering is part of G110, and G119 owns the isolated executable
doctest runner and its budgets.
