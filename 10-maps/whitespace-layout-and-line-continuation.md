---
title: "Whitespace, Layout, and Line Continuation"
kind: map
created: "2026-08-17"
tags:
  - archive-navigation
  - catena
  - language-design
  - layout
  - syntax
  - whitespace
aliases:
  - "Catena whitespace and layout map"
---

# Whitespace, Layout, and Line Continuation

## Scope

This map connects the C013 logical source stream, C014 name boundary,
comparative layout evidence, the C015 decision, its normative 0.1.11 contract,
and the later lexical work that will supply concrete tokens.

## Start here

- [Catena Whitespace, Layout, and Line Continuation](../20-notes/catena-whitespace-layout-and-line-continuation.md)
  explains why Catena combines non-semantic indentation with explicit
  separators and token-directed continuation.
- [Resolved layout inquiry](../40-inquiries/how-should-catena-treat-whitespace-and-line-breaks.md)
  records the operational question, alternatives, and resolution.
- [Whitespace and Layout Specification](../60-specification/whitespace-and-layout/README.md)
  is the normative version 0.1.11 contract.
- [C015 evidence record](../50-journal/2026-08-17-c015-whitespace-and-layout.md)
  records the executable layout engine and verification.

## Trails

### Input foundations

- [Source Text Encoding and Normalization](source-text-encoding-and-normalization.md)
  routes through C013's strict UTF-8, logical LF, and original-byte spans.
- [Identifier and Name Security](identifier-and-name-security.md) fixes the
  C014 name production that later tokenization must preserve.

### Comparative designs

- [Elixir Syntax and Unicode](../30-sources/elixir-project-2026-elixir-syntax-and-unicode.md)
  supplies the closest explicit-block, newline/semicolon, grammar-aware model.
- [Python Lexical Analysis](../30-sources/python-software-foundation-2026-python-lexical-analysis.md)
  exposes the machinery required by semantic indentation and bracket joining.
- [Haskell 2010](../30-sources/marlow-2010-haskell-language-report.md) defines
  offside translation with implicit punctuation and grammar feedback.
- [Rust Whitespace](../30-sources/rust-project-2026-rust-whitespace.md) provides
  the free-form indentation-invariance comparison.

### Conformance route

- [Conformance Traceability](conformance-traceability.md) registers
  `LY-OBL-001` through `LY-OBL-011` against normative anchors and compiler
  tests.
- [Approachable Catena Language Design](approachable-catena-language-design.md)
  places the layout model inside the broader source-language program.

## Open questions

C016 now sends every comment-owned logical LF through this layout classifier;
see the [comments map](comments-and-documentation-comments.md). G017 must
protect literal-contained whitespace. G019 must assign concrete tokens to the
continuation and delimiter capabilities and define precedence, associativity,
and recovery. The complete surface grammar remains P109.
