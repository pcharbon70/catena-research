---
title: "The Swift Programming Language: Lexical Structure"
kind: source
created: "2026-08-18"
authors:
  - "Swift Project"
published: null
citation_key: "swiftProject2026LexicalStructure"
container: "The Swift Programming Language"
edition: null
isbn: null
doi: null
url: "https://docs.swift.org/swift-book/ReferenceManual/LexicalStructure.html"
accessed: "2026-08-18"
tags:
  - comments
  - language-design
  - literals
  - text
  - swift
  - syntax
aliases:
  - "Swift lexical structure"
---

# The Swift Programming Language: Lexical Structure

## Reference

Swift Project, “Lexical Structure,” *The Swift Programming Language*, accessed
2026-08-18. [Official reference](https://docs.swift.org/swift-book/ReferenceManual/LexicalStructure.html).

## Research question

How can a C-family lexical grammar support nested comments and extended string
delimiters without making comment, escape, and interpolation boundaries
ambiguous?

## Findings

- Single-line comments begin with `//` and end at a line break.
- Multiline comments begin with `/*`, end with `*/`, and can nest when all
  markers balance.
- Comments are treated as whitespace by the compiler.
- The lexical grammar separates comment recognition from token recognition and
  uses maximal matching for tokens generally.
- String literals can use extended delimiters made from number-sign characters.
  Escapes and interpolation in such a literal use a matching delimiter count,
  allowing ordinary backslashes and delimiter-looking content to remain text.
- Swift distinguishes ordinary and multiline string forms and gives
  interpolation an explicit lexical marker inside the selected string form.

## Relevance

Swift independently supports the main ergonomic argument for nested block
comments: an outer block can safely enclose source that already contains block
comments. This reinforces Catena's choice to balance every nested `/*` rather
than terminate at the first `*/`. Extended string delimiters separately
support C017's exact-hash raw delimiter and the compatibility principle that
future interpolation should be explicitly selected rather than inferred from
braces inside an established static string.

## Limits

Swift admits physical CR and other whitespace forms that C013 rejects or
normalizes differently. Its documentation markup, interpolation semantics,
multiline indentation rules, and operator-token rules are also separate from
the narrow delimiter evidence used here. Swift's choices do not establish
Catena's escape set or value model.

## Derived work

- [Catena Comments and Documentation Comments](../20-notes/catena-comments-and-documentation-comments.md)
- [Comments and Documentation Comments map](../10-maps/comments-and-documentation-comments.md)
- [Catena Literal Grammar](../20-notes/catena-literal-grammar.md)
- [Resolved literal inquiry](../40-inquiries/how-should-catena-spell-and-decode-literals.md)
- [Literal Grammar map](../10-maps/literal-grammar.md)
