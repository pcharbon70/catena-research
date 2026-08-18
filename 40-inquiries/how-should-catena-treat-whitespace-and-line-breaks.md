---
title: "How Should Catena Treat Whitespace and Line Breaks?"
kind: inquiry
created: "2026-08-17"
status: resolved
tags:
  - catena
  - language-design
  - layout
  - syntax
  - whitespace
aliases:
  - "Catena whitespace inquiry"
---

# How Should Catena Treat Whitespace and Line Breaks?

## Why this matters

Until G015, a valid C013 source stream and valid C014 standalone names could
not be arranged into predictable multiline source. The language had not said
whether indentation forms blocks, whether newline ends an expression, whether
semicolon exists, or why one physical line continues another.

These decisions affect generated code, formatters, parser recovery, source
spans, copy-and-paste behavior, and every provisional multiline example in the
corpus.

## Operational question

Choose a model in which two independent implementations agree on:

- the source scalars that count as layout whitespace;
- whether changing indentation can change token or block structure;
- which events separate complete sibling forms;
- when a logical LF is soft rather than a separator;
- how delimiters interact with expression blocks; and
- which failures occur at semicolon and EOF.

The answer must compose with C013 and C014 without choosing G016 comments,
G017 literals, or G019's concrete operator table.

## Paths explored

- [Elixir](../30-sources/elixir-project-2026-elixir-syntax-and-unicode.md)
  combines explicit blocks, newline/semicolon separation, and grammar-aware
  continuation without semantic indentation.
- [Python](../30-sources/python-software-foundation-2026-python-lexical-analysis.md)
  demonstrates both bracket continuation and the full column-stack cost of
  indentation-defined suites.
- [Haskell 2010](../30-sources/marlow-2010-haskell-language-report.md) translates
  offside layout into inserted punctuation through lexer/parser cooperation.
- [Rust](../30-sources/rust-project-2026-rust-whitespace.md) supplies a strong
  free-form indentation-invariance principle but treats a broader Unicode set
  as whitespace.

## Findings

Semantic indentation would force Catena to define tab expansion, display
columns, mixed indentation, dedentation, and generated-source behavior before
the concrete grammar exists. The corpus supplies no semantic need for that
coupling, and its comprehension work explicitly warns against layout-dependent
meaning.

Treating every newline as an ordinary space is also insufficient. The
provisional language uses multiline sequences of clauses, declarations, and
qualifiers, and later tools need to distinguish a sibling-form boundary from
an incomplete expression.

An abstract token-capability protocol closes G015 without stealing G019.
Tokens can request a left or right expression; delimiter frames can be
continued or block-like. The layout engine can then classify every logical LF
while remaining ignorant of concrete operators and AST forms.

## Outcome

Resolved as C015 and source-only language revision `0.1.11`. Indentation is
non-semantic. Layout whitespace is ASCII space, ASCII tab, and C013 logical LF.
Hard LF and semicolon separate sibling forms. A line is soft only in a
continued delimiter frame or where an adjacent token capability requires the
expression to continue. Block frames retain newline separation.

The [synthesis](../20-notes/catena-whitespace-layout-and-line-continuation.md)
develops the comparison, the
[normative specification](../60-specification/whitespace-and-layout/README.md)
defines the exact contract, and the
[C015 journal](../50-journal/2026-08-17-c015-whitespace-and-layout.md) records
the executable sibling-compiler evidence.
