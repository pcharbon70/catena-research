---
title: "Elixir 1.19 Syntax and Unicode"
kind: source
created: "2026-08-17"
authors:
  - "Elixir Project"
published: "1.19.5"
citation_key: "elixirProject2026SyntaxUnicode"
container: "Elixir Documentation"
edition: "1.19.5"
isbn: null
doi: null
url: "https://hexdocs.pm/elixir/1.19.5/syntax-reference.html"
accessed: "2026-08-17"
tags:
  - elixir
  - language-design
  - layout
  - syntax
  - whitespace
aliases:
  - "Elixir syntax reference"
---

# Elixir 1.19 Syntax and Unicode

## Reference

Elixir Project, “Syntax Reference” and “Unicode Syntax,” *Elixir
Documentation*, version 1.19.5, accessed 2026-08-17.
[Syntax reference](https://hexdocs.pm/elixir/1.19.5/syntax-reference.html) and
[Unicode syntax](https://hexdocs.pm/elixir/1.19.5/unicode-syntax.html).

## Research question

How does Elixir combine indentation-insensitive source, expression separators,
explicit blocks, multiline forms, and a narrow Unicode whitespace repertoire?

## Method

The syntax reference was read for expression blocks, `do`/`end` forms,
parenthesized blocks, calls, and separators. The Unicode reference was checked
for the exact source whitespace code points. These are official language
documents rather than empirical observations of one parser release.

## Findings

- Indentation does not create blocks. Explicit delimiters and `do`/`end`
  establish structure.
- Blocks contain expressions separated by newline or semicolon.
- Parentheses can delimit a block of multiple expressions; an open delimiter
  does not universally erase every newline.
- Multiline calls and operator expressions are grammar-aware. Delimiters,
  commas, and incomplete operator positions allow continuation, while a
  completed expression can end at newline.
- Elixir recognizes only tab, LF, CR, and ASCII space as source whitespace,
  rather than every Unicode `Pattern_White_Space` scalar.
- Optional call parentheses and operator syntax create ambiguities that the
  formatter manages by canonical presentation, illustrating that layout and
  formatting remain related even when indentation is non-semantic.

## Relevance

Elixir is the closest mature BEAM-language comparison for Catena. It supports
explicit blocks, same-line semicolon separation, and readable multiline forms
without an indentation stack. Catena adopts that high-level division while
using C013's stricter line decoder and an abstract token-capability interface
until G019 fixes concrete operators.

## Limits

Elixir's parser and AST are designed around calls and macros, whereas Catena
has a typed semantic kernel and unsettled concrete grammar. The references do
not expose one small independent layout algorithm, and Catena must not infer
its future operator precedence or optional-call rules from Elixir.

## Derived work

- [Catena Whitespace, Layout, and Line Continuation](../20-notes/catena-whitespace-layout-and-line-continuation.md)
- [Resolved layout inquiry](../40-inquiries/how-should-catena-treat-whitespace-and-line-breaks.md)
- [Whitespace, Layout, and Line Continuation map](../10-maps/whitespace-layout-and-line-continuation.md)
