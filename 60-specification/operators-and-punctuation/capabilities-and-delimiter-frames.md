---
title: "Capabilities and Delimiter Frames"
kind: specification
created: "2026-08-21"
status: normative
spec_version: "0.1.15"
tags:
  - layout
  - operators
  - specification
  - syntax
aliases:
  - "Catena token capabilities"
---

# Capabilities and Delimiter Frames

## Status and authority

This chapter is the normative Catena 0.1.15 assignment of concrete
continuation capabilities and delimiter frames. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies the abstract obligations of
[Separators and Line Continuation](../whitespace-and-layout/separators-and-line-continuation.md)
to the tokens fixed by
[Token Inventory and Maximal Munch](token-inventory-and-maximal-munch.md).

The rules apply only to source-language revision `0.1.15`.

## Token continuation capabilities

Every significant 0.1.15 token supplies the two C015 layout capabilities.
The complete assignment is (`OP-OBL-005`):

| Tokens | `join_before` | `join_after` |
| --- | --- | --- |
| `+` `-` `*` `<` `<=` `>` `>=` `==` `!=` `&&` `\|\|` `\|>` | true | true |
| prefix `-` and `!` | false | true |
| `)` `]` `}` | true | false |
| `(` `[` `{` `,` `;` `.` `->` | false | false |
| C014 names, C017 literals, C017 text/character/bytes | false | false |

The prefix-role `-` and `!` are distinguished from their binary roles by
parser position, not by token identity: a `-` in prefix position carries
the prefix capabilities, and a `-` in binary position carries the binary
capabilities. A C015 engine that consumes only token streams may conservatively
take the union (both capabilities true) for `-` and `!`; the classification
rules of C015 operate on the stream it is given, and the exact positions
are resolved by the operator-expression layer.

A Boolean-literal, name, or other atom token joins nothing: two adjacent
atoms remain an error of the operator-expression layer, not a layout error.

## Delimiter families and frame modes

The complete frame assignment is (`OP-OBL-006`):

| Opening | Family | Mode | Closing |
| --- | --- | --- | --- |
| `(` | `paren` | `continued` | `)` |
| `[` | `bracket` | `continued` | `]` |
| `{` | `brace` | `block` | `}` |

A closing token closes the innermost open frame of its own family under the
C015 rule. An unmatched close, a close of a family that is not open, or an
open frame at end of input is invalid and surfaces through the C015
`LAY002` diagnostic over the token stream; this chapter adds no new
delimiter-failure mechanism.

While a `paren` or `bracket` frame is innermost, eligible line breaks inside
it are soft, so argument and collection elements may span lines. While a
`brace` frame is innermost, eligible line breaks remain hard-separator
candidates, so brace bodies may be newline-separated sibling forms under a
later P109 body grammar. This assignment does not itself decide what a
brace body contains.

## Separator roles

`,` separates sibling elements inside one frame and carries no join
capabilities; it is valid only where a later grammar admits an element
list. `;` is the C015 hard separator between complete forms; a `;` inside a
`paren` or `bracket` frame is valid only where a later grammar admits it,
and this chapter fixes no such grammar. Neither token ever opens or closes
a frame.

## The dot interaction

`.` is a token only in three cases: inside a C017 numeric spelling
(`1.0`), inside a C014 qualified-name production (`x.y.z`), and as the
standalone qualification separator token between tokens that a later
resolution layer will interpret. It carries no join capabilities and no
frame behavior. It is not field access: `expr.field` is not decided here
and remains with G040/P109 (`OP-OBL-012`).

## Abstract events preserved

A conforming token stream exposes, for every token, its original-byte span
and its capability pair, and exposes frame open/close events for
delimiters, so an independent C015 resolver reproduces soft, separator,
blank, and semicolon classifications from the stream alone (`OP-OBL-013`).

## Deliberately separate work

Body grammars for `paren`, `bracket`, and `brace` contents remain P109 and
G040. Keyword-delimited frames and any future additional delimiters remain
P109. Qualification resolution remains G021/G022.

## Rationale and evidence (non-normative)

The [operators synthesis](../../20-notes/catena-operators-and-punctuation.md)
explains the continued/block split and its multiline-argument motivation.
The [layout synthesis](../../20-notes/catena-whitespace-layout-and-line-continuation.md)
defines the abstract machinery this chapter populates.
