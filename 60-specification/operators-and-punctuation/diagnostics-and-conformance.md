---
title: "Operator Diagnostics and Conformance"
kind: specification
created: "2026-08-21"
status: candidate
spec_version: "0.1.15"
tags:
  - conformance
  - diagnostics
  - operators
  - specification
  - syntax
  - testing
aliases:
  - "Catena 0.1.15 operator conformance"
---

# Operator Diagnostics and Conformance

## Status and authority

This chapter is the normative Catena 0.1.15 operator diagnostic, abstract
frontend, and conformance contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies [Token Inventory and Maximal Munch](token-inventory-and-maximal-munch.md),
[Capabilities and Delimiter Frames](capabilities-and-delimiter-frames.md),
and [Precedence and Associativity](precedence-and-associativity.md).

## Stable diagnostics

| ID | Required meaning |
| --- | --- |
| `OPR001` | a symbol position matches no operator, punctuation, or atom spelling — a reserved or invalid spelling |
| `OPR002` | an operator-expression form is invalid: a missing operand, an interrupted prefix form, or a chained comparison or equality |

Delimiter imbalance and interrupted continuation surface through the C015
`LAY002` and `LAY003` diagnostics over the token stream; this area adds no
duplicate mechanism. An exact-selection mismatch remains `EDN001`
(`OP-OBL-014`).

Every rejection carries the stable diagnostic ID and a primary
original-byte span. Invalid input produces no token stream, no expression
tree, and no other successful output for the affected action. Diagnostic
prose can improve only within the bounded presentation rules of the
repository conformance vocabulary.

## Recovery

0.1.15 defines no parse-error recovery. Tokenization and parsing reject
the whole input transactionally with exactly one diagnostic per failing
action; no partial stream, partial tree, resynchronization, or multi-error
run exists in this revision (`OP-OBL-014`). Editor-protocol recovery
remains G123; formatter tolerance remains G118.

## Abstract public boundaries

A conforming implementation exposes two operations.

**Tokenization** accepts C013 source bytes and an exact language selection
and returns one complete, lossless, ordered token stream — every C014 name,
C016 comment, C017 literal, and operator/punctuation token with its kind,
spelling, original-byte span, capability pair, and delimiter frame events —
or exactly one diagnostic (`OP-OBL-013`).

**Operator-expression parsing** accepts one token stream region and returns
one expression tree over atomic operands and the fixed ladder, or exactly
one diagnostic (`OP-OBL-013`).

Neither operation type-checks, resolves names, elaborates declarations,
evaluates, or lowers to BEAM; implementations MUST NOT use these boundaries
to claim those later phases (`OP-OBL-016`).

The bootstrap evidence names these operations `Catena.tokenize_source/2`
and `Catena.parse_operator_expression/1`, and the records `Catena.Operator`
and `Catena.Operator.Expression`. These Elixir names are evidence API
names, not required names for every implementation.

## Determinism

Equal source bytes and exact language selection produce equal token
streams or equal stable diagnostics; equal token stream regions produce
equal expression trees or equal diagnostics (`OP-OBL-015`). Tokenization
is insensitive to inter-token whitespace beyond trivia retention and C015
classification.

## Conformance obligations

| ID | Obligation | Required executable evidence |
| --- | --- | --- |
| `OP-OBL-001` | apply operator behavior only at exact 0.1.15 and register the stable lifecycle addition | exact selection, registry, and lifecycle tests |
| `OP-OBL-002` | recognize exactly the closed inventory and no other operator or punctuation spelling | inventory matrix and exclusion tests |
| `OP-OBL-003` | enforce maximal munch and spacing-invariant tokenization against every atom | `1.0e3`, `1.`, `x.y`, `a-1` vs `a - 1` boundary tests |
| `OP-OBL-004` | reject reserved and invalid symbol spellings as `OPR001` without re-tokenization | `/`, `%`, `=`, `|`, `=&`, Unicode-symbol tests |
| `OP-OBL-005` | assign the exact `join_before`/`join_after` capability pair to every token | capability table tests |
| `OP-OBL-006` | push `paren`/`bracket` continued and `brace` block frames and close innermost matching | frame-mode, nesting, and `LAY002` integration tests |
| `OP-OBL-007` | fix the precedence ladder and per-level associativity exactly, with no fixity declarations | grouping and associativity tree tests |
| `OP-OBL-008` | reject comparison and equality chains as `OPR002`, accepting parenthesized regrouping | chain and regrouping tests |
| `OP-OBL-009` | fix prefix `-`/`!` above the binary ladder, right-recursively, never inside a literal | prefix, `--x`, `-1`, and pattern-boundary tests |
| `OP-OBL-010` | fix `\|>` left-associative at the loosest level denoting application of right to left | pipe grouping and nesting tests |
| `OP-OBL-011` | tokenize `->` while excluding it from 0.1.15 expression rules | arrow exclusion tests |
| `OP-OBL-012` | fix `.` as qualification-only, never field access | dot-boundary and exclusion tests |
| `OP-OBL-013` | expose the lossless whole-source stream and the tree-or-diagnostic parse boundary | round-trip, span, trivia, and no-partial-output tests |
| `OP-OBL-014` | reject transactionally with `OPR001`/`OPR002`/C015 events and no recovery | single-diagnostic and no-recovery tests |
| `OP-OBL-015` | produce deterministic streams and trees | repeated-result tests |
| `OP-OBL-016` | preserve source-only and persisted-format separation and claim no later phase | registry, pinned-predecessor, forged-format, and absent-phase tests |

Every obligation has at least one tagged passing test. The sibling compiler
gates the complete `OP-OBL-*` set against unknown and uncovered identifiers
before C019 conformance is claimed.

## Required evidence sets

Positive evidence includes every inventory spelling; grouped expressions
at every level; left-associative groupings for `* + - && || |>`; prefix
nesting `--x`, `!-x`; pipe chains; multiline `paren`/`bracket` contents with
soft newlines; newline-separated brace contents with hard-separator
classification; qualified names through the stream; and full-file
round trips with spans and trivia preserved.

Negative evidence includes reserved spellings, a lone `=`, `|`, and `&`;
near-miss orderings; chained and mixed comparisons; missing operands
before `;`, EOF, and closers; unbalanced and mismatched delimiters; `->` in
expression position; and `expr.field` forms.

Exclusion evidence demonstrates that neither boundary type-checks, resolves
names, elaborates declarations, evaluates, or emits interfaces or BEAM, and
that predecessor APIs retain their exact 0.1.10 through 0.1.14 selections
and defaults.

## Revision and persistence separation

Revision `0.1.15` is a compatible source-acceptance and static-structure
addition. It adds no JSON AST version, kernel S-expression version,
interface version, artifact version, signature domain, typing rule, runtime
behavior, or BEAM representation (`OP-OBL-001`, `OP-OBL-016`).

The source-text decoder accepts cumulative revisions `0.1.9` through
`0.1.15`. Standalone identifier, layout, comment, literal scanning, and
numeric elaboration retain their exact 0.1.10 through 0.1.14 selections
and defaults. Tokenization and operator-expression parsing require exact
`0.1.15`. The next unused semantic patch is `0.1.16`.

## Rationale and evidence (non-normative)

The design route is preserved in the
[operators synthesis](../../20-notes/catena-operators-and-punctuation.md),
the [open inquiry](../../40-inquiries/how-should-catena-fix-operators-and-punctuation.md),
and the [topic map](../../10-maps/operators-and-punctuation.md). The C019
evidence record will preserve the sibling-compiler commands and archive
validation.
