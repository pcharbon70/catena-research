---
title: "Whitespace and Layout Diagnostics and Conformance"
kind: specification
created: "2026-08-17"
status: normative
spec_version: "0.1.11"
tags:
  - conformance
  - diagnostics
  - layout
  - specification
  - testing
  - whitespace
aliases:
  - "Catena 0.1.11 layout conformance"
---

# Whitespace and Layout Diagnostics and Conformance

## Status and authority

This chapter is the normative Catena 0.1.11 whitespace/layout diagnostic,
public engine, and conformance contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies [Whitespace and Indentation](whitespace-and-indentation.md) and
[Separators and Line Continuation](separators-and-line-continuation.md).

## Stable diagnostics

| ID | Required meaning |
| --- | --- |
| `LAY001` | prohibited layout-whitespace scalar or malformed logical-LF layout event |
| `LAY002` | unexpected, mismatched, or unclosed delimiter context |
| `LAY003` | a hard separator or EOF interrupts a required left/right continuation |

Every rejection includes the stable ID and the primary original-byte span when
an offending source event or token exists (`LY-OBL-008`, `LY-OBL-009`).
`LAY001` identifies the scalar and reason. `LAY002` identifies the observed and,
when available, expected delimiter family. `LAY003` distinguishes missing left
expression, semicolon interruption, and EOF interruption.

Diagnostic prose and map-key presentation can improve only within the bounded
rules of the repository conformance vocabulary. Stable ID, source span,
meaning-bearing details, severity class, and acceptance do not vary.

## Public library boundary

A conforming implementation exposes an equivalent operation that accepts an
ordered lexer-supplied event stream and exact language selection, then returns
the lossless classified stream or one diagnostic. Significant tokens are
opaque except for source span, `join_before`, `join_after`, and optional open or
close delimiter capability.

The bootstrap evidence names the operation `Catena.resolve_layout/2`. Its
events represent significant tokens, horizontal source units, logical LF,
and semicolon. Its result classifies logical LF as `soft`, `separator`, or
`blank` and carries exact selection. These Elixir names and structs are evidence
API names, not required names for every implementation.

C015 defines no whole-source CLI. C016 now supplies comments through a separate
abstract event resolver; a command accepting arbitrary source would still have
to guess C017 literals and G019 token capabilities. The public token-event
operation is the executable integration boundary until those lexical owners
are complete (`LY-OBL-011`).

## Conformance obligations

| ID | Obligation | Required executable evidence |
| --- | --- | --- |
| `LY-OBL-001` | apply layout only at 0.1.11 and retain source-only revision separation | selection and forged-format tests |
| `LY-OBL-002` | accept only SPACE, TAB, and logical LF as layout whitespace | exact positive and Unicode-negative tests |
| `LY-OBL-003` | make indentation and tab width semantically inert | equivalent-layout tests |
| `LY-OBL-004` | preserve hard LF and semicolon separators | separator-stream tests |
| `LY-OBL-005` | classify blank lines and complete or incomplete EOF exactly | leading, repeated, trailing, and no-final-LF tests |
| `LY-OBL-006` | resolve `join_before` and `join_after` continuation | leading/trailing capability tests |
| `LY-OBL-007` | distinguish nested continued and block delimiter frames | mixed-frame and mismatch tests |
| `LY-OBL-008` | emit stable `LAY001`–`LAY003` failures | every reason-family test |
| `LY-OBL-009` | retain original-byte spans including CRLF and multibyte scalars | exact span tests |
| `LY-OBL-010` | return a lossless deterministic event stream | repeated-result and preservation tests |
| `LY-OBL-011` | keep comment, literal, and operator ownership outside G015 | opaque-token and interface-boundary tests |

Every obligation has at least one tagged passing test. The sibling compiler
gates the complete `LY-OBL-*` set against unknown and uncovered identifiers
before C015 conformance is claimed.

## Required evidence sets

Positive evidence includes spaces, tabs, LF, CRLF, blank lines, optional final
LF, semicolons, before/after continuation, continued frames, block frames, and
mixed nesting. Negative evidence includes vertical tab, form feed, nonbreaking
space, Unicode direction marks and line separators, leading left-dependent
tokens, interrupted right-dependent tokens, and malformed delimiter stacks.

An opaque token containing whitespace-like scalars demonstrates that layout is
applied only outside token-owned content. Concrete comment and literal syntax
is not inferred from that test.

## Revision and persistence separation

Revision `0.1.11` is a compatible source-acceptance and static-structure
addition. It adds no JSON AST version, kernel S-expression version, interface
version, artifact version, signature domain, typed-core form, runtime behavior,
or BEAM representation (`LY-OBL-001`).

The source-text decoder accepts cumulative revisions `0.1.9`, `0.1.10`, and
`0.1.11`. The standalone C014 identifier APIs retain their exact 0.1.10
selection boundary. Layout resolution requires exact 0.1.11 token events.

## Rationale and evidence (non-normative)

The design route is preserved in the
[layout synthesis](../../20-notes/catena-whitespace-layout-and-line-continuation.md),
[resolved inquiry](../../40-inquiries/how-should-catena-treat-whitespace-and-line-breaks.md),
and [topic map](../../10-maps/whitespace-layout-and-line-continuation.md). The
[C015 record](../../50-journal/2026-08-17-c015-whitespace-and-layout.md)
records the concrete sibling-compiler commands and archive validation.
