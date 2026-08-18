---
title: "The Rust Reference: Whitespace"
kind: source
created: "2026-08-17"
authors:
  - "Rust Project Developers"
published: null
citation_key: "rustProject2026Whitespace"
container: "The Rust Reference"
edition: null
isbn: null
doi: null
url: "https://doc.rust-lang.org/reference/whitespace.html"
accessed: "2026-08-17"
tags:
  - language-design
  - rust
  - syntax
  - whitespace
aliases:
  - "Rust whitespace reference"
---

# The Rust Reference: Whitespace

## Reference

Rust Project Developers, “Whitespace,” *The Rust Reference*, accessed
2026-08-17.
[Official reference](https://doc.rust-lang.org/reference/whitespace.html).

## Contribution

The chapter defines Rust as a free-form language and gives its source
whitespace repertoire through Unicode `Pattern_White_Space`.

## Findings

- Whitespace separates tokens but has no semantic significance.
- Replacing one legal whitespace element with another preserves program
  meaning.
- The recognized set includes ASCII tab, line feed, vertical tab, form feed,
  carriage return, and space, plus U+0085, U+200E, U+200F, U+2028, and U+2029.

## Relevance

Rust demonstrates a strong indentation-invariance rule. Catena adopts that
principle but not the complete whitespace repertoire: invisible direction
marks and alternate line separators would undermine C013's single logical-LF
boundary. Catena also retains hard newline events because its future grammar
needs an explicit account of sibling forms and continuation.

## Limits

This short lexical chapter does not define Rust's complete token adjacency,
delimiter, statement, or parser rules. It therefore supports only the
free-form-whitespace comparison, not Catena's separator algorithm.

## Derived work

- [Catena Whitespace, Layout, and Line Continuation](../20-notes/catena-whitespace-layout-and-line-continuation.md)
- [Resolved layout inquiry](../40-inquiries/how-should-catena-treat-whitespace-and-line-breaks.md)
- [Whitespace, Layout, and Line Continuation map](../10-maps/whitespace-layout-and-line-continuation.md)
