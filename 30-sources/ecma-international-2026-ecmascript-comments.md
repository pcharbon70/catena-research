---
title: "ECMAScript 2026 Language Specification: Comments"
kind: source
created: "2026-08-18"
authors:
  - "Ecma International"
published: 2026
citation_key: "ecmaInternational2026Comments"
container: "ECMAScript 2026 Language Specification"
edition: "ECMAScript 2026"
isbn: null
doi: null
url: "https://tc39.es/ecma262/2026/multipage/ecmascript-language-lexical-grammar.html#sec-comments"
accessed: "2026-08-18"
tags:
  - comments
  - ecmascript
  - language-design
  - layout
  - syntax
aliases:
  - "ECMAScript comments"
---

# ECMAScript 2026 Language Specification: Comments

## Reference

Ecma International, “Comments,” *ECMAScript 2026 Language Specification*,
2026. [Official specification](https://tc39.es/ecma262/2026/multipage/ecmascript-language-lexical-grammar.html#sec-comments).

## Contribution

The lexical chapter explicitly states how line terminators at and inside
comments remain visible to later syntactic processing.

## Findings

- A single-line comment consumes source through the end of the line but does
  not consume the terminating line terminator; that terminator is a separate
  lexical input element.
- A multiline comment containing a line terminator is treated as a line
  terminator for syntactic parsing.
- ECMAScript comments otherwise behave as discarded whitespace, and its
  multiline comments do not nest.

## Relevance

This is strong evidence against erasing comment-owned line boundaries before
layout. Catena adopts the separate line-comment terminator principle and goes
further: every C013 logical LF inside a block comment remains individually
available to C015 classification, preserving blank-line count and exact spans.

## Limits

ECMAScript's automatic semicolon insertion and non-nesting block syntax are not
Catena features. Treating an entire multiline comment as one line terminator is
also less lossless than Catena's event model.

## Derived work

- [Catena Comments and Documentation Comments](../20-notes/catena-comments-and-documentation-comments.md)
- [Resolved comments inquiry](../40-inquiries/how-should-catena-handle-comments-and-documentation-comments.md)
- [Comments and Documentation Comments map](../10-maps/comments-and-documentation-comments.md)
