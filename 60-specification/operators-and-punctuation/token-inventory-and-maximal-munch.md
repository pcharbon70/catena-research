---
title: "Token Inventory and Maximal Munch"
kind: specification
created: "2026-08-21"
status: candidate
spec_version: "0.1.15"
tags:
  - operators
  - specification
  - syntax
aliases:
  - "Catena token inventory"
---

# Token Inventory and Maximal Munch

## Status and authority

This chapter is the normative Catena 0.1.15 operator and punctuation token
inventory and boundary contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It consumes the identifier and qualified-name spellings fixed by
[C014](../identifiers/README.md), the atomic literal spellings fixed by
[C017](../literal-grammar/literal-forms-and-boundaries.md), and the layout
whitespace fixed by [C015](../whitespace-and-layout/whitespace-and-indentation.md).

The rules apply only to source-language revision `0.1.15`. They do not
reinterpret retained JSON ASTs, the exact 0.1.8 kernel, interfaces,
artifacts, or signed formats.

## Closed inventory

The complete 0.1.15 operator and punctuation inventory is:

| Class | Spelling | Role |
| --- | --- | --- |
| Arithmetic | `+` `-` `*` | binary `add`, `subtract`, `multiply` |
| Comparison | `<` `<=` `>` `>=` | binary `less`, `less_equal`, `greater`, `greater_equal` |
| Equality | `==` `!=` | binary `equal`, `not_equal` |
| Boolean | `!` `&&` `||` | prefix `not`, binary `and`, binary `or` |
| Structural | `->` `|>` | reserved clause arrow; pipe |
| Delimiters | `(` `)` `[` `]` `{` `}` | grouping and future collection delimiters |
| Separators | `,` `;` `.` | in-frame separator; hard separator; qualification |

Every token is exactly the ASCII sequence shown. The inventory is closed:
no other operator or punctuation token exists in 0.1.15 (`OP-OBL-002`).

The unary minus spelling `-` denotes C018 negation in prefix position and
C003/C010 `subtract` in binary position; the two roles are resolved by the
[precedence rules](precedence-and-associativity.md), not by different
tokens. The unary `!` denotes Boolean `not`.

## Maximal munch

At every position the lexer selects the longest inventory spelling that
matches (`OP-OBL-003`). Consequences:

- `!=` is one equality token; `<=` and `>=` are one comparison token each.
- `!!` is two prefix `!` tokens, because no `!!` spelling exists.
- `->` wins over `-` followed by `>`; `|>` wins over `|` (which does not
  exist) followed by `>`.

Munching composes with the atom scanners by the same longest-match rule
applied to the combined grammar of inventory spellings, C014 identifier and
qualified-name spellings, C017 literal spellings, and C016 comment
openers. Numeric and textual atoms take priority inside their own
productions: `1.0e3` is one C017 float, `1.` scans as integer `1` followed
by the `.` token, and `x.y.z` scans as one C014 qualified name while a
qualified-name production matches. A `.` that does not continue a numeric
spelling or a qualified name is the qualification separator token awaiting
its G021 resolution meaning; it is not field access (`OP-OBL-012`).

## Spacing has no token effect

Horizontal whitespace between tokens is trivia. Replacing any inter-token
whitespace run with any other legal run — including removing it entirely or
inserting a line break that C015 classifies soft — leaves the token
sequence unchanged (`OP-OBL-003`). In particular `a-1`, `a - 1`, and
`a -1` produce the same three tokens `a`, `-`, `1`. Only C015's
soft/hard/separator classification, not tokenization, may differ across
line breaks.

## Reserved and invalid spellings

A position at which no inventory spelling and no atom production matches is
invalid (`OP-OBL-004`). This includes `/`, `%`, `^`, `<<`, `>>`, `&`, `~`,
`++`, `--`, `**`, `..`, `:=`, `<-`, `=>`, a lone `=`, a lone `|`,
near-miss orderings such as `=!`, and every non-ASCII symbol scalar
outside a token-owned literal region. These spellings are reserved for
future revisions or excluded entirely; rejecting them now keeps every later
admission a compatible addition rather than a silent meaning change of
currently accepted programs.

The failure is the stable `OPR001` diagnostic over the offending
original-byte span. An implementation MUST NOT tokenize a reserved
spelling into shorter pieces that would change program meaning.

## Delimiter and separator tokens

`(`, `[`, and `{` are opening delimiters; `)`, `]`, and `}` are closing
delimiters; their capabilities and frame assignments are fixed by
[Capabilities and Delimiter Frames](capabilities-and-delimiter-frames.md).
`,` separates elements inside one frame; `;` is the C015 hard separator;
neither is an operator, and neither participates in the precedence ladder.
`->` is tokenized but participates in no 0.1.15 expression rule; it is
reserved for P109 clause structure (`OP-OBL-011`).

## Deliberately separate work

Application syntax, declaration grammar, and the `->` clause structure
remain P109. File-to-module relations remain G020. Which `.`-separated
prefixes name modules, namespace search, and ambiguity remain G021/G022.
Field-like access and collection bodies remain G040/P109. Operator trait
dispatch and overloaded operators remain G061.

## Rationale and evidence (non-normative)

The [operators synthesis](../../20-notes/catena-operators-and-punctuation.md)
compares the Rust, OCaml, Haskell, and Erlang designs and explains the
closed semantic-mapped set. The
[open inquiry](../../40-inquiries/how-should-catena-fix-operators-and-punctuation.md)
and [topic map](../../10-maps/operators-and-punctuation.md) preserve the
decision route.
