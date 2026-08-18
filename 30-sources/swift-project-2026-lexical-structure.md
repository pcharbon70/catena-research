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

How can a C-family comment syntax safely support commenting out regions that
already contain block comments?

## Findings

- Single-line comments begin with `//` and end at a line break.
- Multiline comments begin with `/*`, end with `*/`, and can nest when all
  markers balance.
- Comments are treated as whitespace by the compiler.
- The lexical grammar separates comment recognition from token recognition and
  uses maximal matching for tokens generally.

## Relevance

Swift independently supports the main ergonomic argument for nested block
comments: an outer block can safely enclose source that already contains block
comments. This reinforces Catena's choice to balance every nested `/*` rather
than terminate at the first `*/`.

## Limits

Swift admits physical CR and other whitespace forms that C013 rejects or
normalizes differently. Its documentation markup and operator-token rules are
also separate from the narrow nesting evidence used here.

## Derived work

- [Catena Comments and Documentation Comments](../20-notes/catena-comments-and-documentation-comments.md)
- [Comments and Documentation Comments map](../10-maps/comments-and-documentation-comments.md)
