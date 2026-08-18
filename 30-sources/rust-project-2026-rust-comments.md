---
title: "The Rust Reference: Comments"
kind: source
created: "2026-08-18"
authors:
  - "Rust Project Developers"
published: null
citation_key: "rustProject2026Comments"
container: "The Rust Reference"
edition: null
isbn: null
doi: null
url: "https://doc.rust-lang.org/stable/reference/comments.html"
accessed: "2026-08-18"
tags:
  - comments
  - documentation
  - language-design
  - rust
  - syntax
aliases:
  - "Rust comments reference"
---

# The Rust Reference: Comments

## Reference

Rust Project Developers, “Comments,” *The Rust Reference*, accessed
2026-08-18. [Official reference](https://doc.rust-lang.org/stable/reference/comments.html).

## Contribution

The chapter gives one precise lexical family for ordinary line/block comments,
nested block comments, and outer versus inner documentation comments.

## Findings

- `//` and `/* ... */` are ordinary comments, and block comments nest.
- Exactly `///` and `/** ... */` identify outer documentation comments;
  `////`, `/***`, and the empty `/**/` are ordinary-comment edge cases.
- `//!` and `/*! ... */` identify a distinct inner-documentation model.
- Any block-comment kind can be nested inside another block-comment kind, but
  the outer opener determines the outer comment's classification.
- Outer documentation must precede a construct that accepts an outer
  attribute. Markdown is conventional documentation content, but comment
  delimiters remain active inside it.

## Relevance

The delimiter family is compact, familiar, and already specifies the awkward
prefix cases that independent lexers otherwise tend to disagree about. Catena
adopts the ordinary and outer forms plus nested balancing, while rejecting the
inner-documentation family so attachment always points forward to one
declaration.

## Limits

Rust lowers documentation comments to attributes and has crate/item ownership
rules that do not define Catena declarations. Rust's exact body preservation,
CR exclusion, rustdoc behavior, and inner comments are therefore comparisons,
not imported Catena semantics.

## Derived work

- [Catena Comments and Documentation Comments](../20-notes/catena-comments-and-documentation-comments.md)
- [Resolved comments inquiry](../40-inquiries/how-should-catena-handle-comments-and-documentation-comments.md)
- [Comments and Documentation Comments map](../10-maps/comments-and-documentation-comments.md)
