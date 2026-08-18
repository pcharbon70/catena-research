---
title: "Separators and Line Continuation"
kind: specification
created: "2026-08-17"
status: normative
spec_version: "0.1.11"
tags:
  - layout
  - specification
  - syntax
  - whitespace
aliases:
  - "Catena line continuation"
---

# Separators and Line Continuation

## Status and authority

This chapter is the normative Catena 0.1.11 separator and continuation
contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It builds on [Whitespace and Indentation](whitespace-and-indentation.md).

## Hard separators

A complete sibling form is separated from the next sibling form by at least
one hard logical LF or one U+003B SEMICOLON. The concrete grammar determines
which forms are siblings and reports a syntax error when the required event is
absent (`LY-OBL-004`).

A semicolon is always a hard separator. Delimiter mode and adjacent token
capabilities MUST NOT soften it. Semicolon remains an explicit separator inside
a block frame; the later grammar determines whether a particular block accepts
multiple forms or an empty position.

The first hard logical LF in a gap after a significant token is classified
`separator`. Further logical LFs in the same gap are classified `blank`. Every
source event and original-byte span remains ordered in the output.

## Token continuation capabilities

Each significant token supplies two Boolean layout capabilities
(`LY-OBL-006`):

- `join_before` states that the token requires a preceding expression in the
  same continued form;
- `join_after` states that the token requires a following expression in the
  same continued form.

The names are abstract language obligations, not required implementation field
names. G019 assigns these capabilities to concrete operators and punctuation.
G015 assigns no precedence, associativity, fixity, or operator spelling.

A horizontal-whitespace gap containing at least one logical LF is soft when it
has a preceding significant token and at least one of these conditions holds:

1. the innermost open delimiter frame is `continued`;
2. the preceding token has `join_after`; or
3. the following token has `join_before`.

Every logical LF in a soft gap is classified `soft`. Horizontal whitespace in
the gap remains trivia. Indentation and the number of blank physical lines do
not affect the result.

A token with `join_before` is invalid at the beginning of input or immediately
after a hard separator. A semicolon after a token with `join_after` is invalid.
End of file after a token with `join_after` is invalid. These failures produce
`LAY003` rather than converting an incomplete form into a complete one.

## Delimiter frames

An opening token can push one delimiter family with one of two line modes
(`LY-OBL-007`):

- `continued` makes eligible LF-containing gaps soft while that frame is
  innermost;
- `block` leaves LF-containing gaps eligible to become hard separators.

A closing token names the family it closes. It closes only the innermost frame
of the same family. An unmatched close, mismatched close, or open frame left at
EOF is invalid and produces `LAY002`.

The innermost frame controls delimiter-based softness. Therefore a block frame
inside a continued frame can contain newline-separated sibling forms, and a
continued frame inside a block can contain multiline arguments. Adjacent token
capabilities still soften a specific gap in either frame.

Concrete parentheses, brackets, braces, keywords, and their frame modes remain
owned by G019 and P109. No indentation level creates a frame.

## Resolution order

A conforming resolver performs these observable steps:

1. require exact source-only revision `0.1.11`;
2. validate layout-whitespace and logical-LF events;
3. traverse significant tokens and delimiter frames in source order;
4. classify each LF-containing gap from the innermost frame and adjacent token
   capabilities;
5. preserve semicolons as hard separators;
6. reject mismatched frames and interrupted continuation; and
7. return the lossless ordered event stream and exact selection.

Repeating resolution over equal events and selection produces an equal result
(`LY-OBL-010`). Implementations MUST NOT consult indentation, parser recovery
heuristics, ambient editor settings, or display width.

## EOF and incomplete input

EOF completes a final token when no frame remains open and that token does not
have `join_after`. EOF emits no synthetic source newline or semicolon. An open
frame takes `LAY002`; otherwise an unsatisfied `join_after` takes `LAY003`
(`LY-OBL-005`, `LY-OBL-008`).

## Rationale and evidence (non-normative)

The token-capability interface preserves Elixir-like grammar-aware continuation
without moving G019's operator decisions into C015. The executable form and
focused boundary cases are recorded in the
[C015 journal](../../50-journal/2026-08-17-c015-whitespace-and-layout.md).
