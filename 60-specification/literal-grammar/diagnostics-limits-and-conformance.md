---
title: "Literal Diagnostics, Limits, and Conformance"
kind: specification
created: "2026-08-18"
status: normative
spec_version: "0.1.13"
tags:
  - conformance
  - diagnostics
  - limits
  - literals
  - specification
  - testing
aliases:
  - "Catena 0.1.13 literal conformance"
---

# Literal Diagnostics, Limits, and Conformance

## Status and authority

This chapter is the normative Catena 0.1.13 literal diagnostic, limit,
abstract-frontend, and conformance contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies [Literal Forms and Boundaries](literal-forms-and-boundaries.md) and
[Text, Characters, and Bytes](text-characters-and-bytes.md).

## Stable diagnostics

| ID | Required meaning |
| --- | --- |
| `LIT001` | the supplied logical-unit index is invalid or the selected position does not begin an atomic 0.1.13 literal |
| `LIT002` | an opened cooked or raw delimiter reaches EOF without its required closer |
| `LIT003` | a numeric spelling, escape, Unicode scalar, character arity, cooked source line, or direct byte scalar is malformed |

An exact-selection mismatch remains `EDN001`. Every source-derived literal
rejection carries the stable diagnostic ID, a primary original-byte span, and
a stable reason that distinguishes the cases represented by that family
(`LT-OBL-009`). An invalid unit index uses a stable option path.

Malformed input produces no successful literal, decoded payload, next index,
or other successful frontend result. Diagnostic prose can improve only within
the bounded presentation rules of the repository conformance vocabulary;
identity, severity, reason, source span, acceptance, and repair meaning do not
vary.

## Literal implementation limits

`LIM002` applies to every accepted integer base. The measured value is the
count of decimal digits in the exact nonnegative mathematical integer value,
with zero measuring one digit. A value through 4,096 decimal digits crosses no
integer-magnitude limit. The next digit is refused under the configured bound
with the common structured limit fields (`LT-OBL-008`).

`LIM004` applies independently to each decoded text or byte literal. Text is
measured as bytes in the decoded UTF-8 scalar sequence; bytes are measured as
decoded payload octets. A payload through 65,536 bytes crosses no decoded
literal limit. The next byte is refused under the configured bound with the
common structured limit fields (`LT-OBL-008`). Character literals do not use
this payload-size dimension.

Both limits follow the portable-floor, configured-value, disclosure, and
transactional-failure rules in the repository implementation-limit policy.
They do not turn otherwise malformed input into limit exhaustion. The language
defines no separate raw-hash-count limit.

## Abstract public boundary

A conforming implementation exposes an equivalent atomic scan operation. It
accepts C013 source bytes, exact 0.1.13 selection, and a logical-unit index. It
returns one complete literal, the next unconsumed logical-unit index, and the
resolved selection, or exactly one diagnostic (`LT-OBL-010`).

The successful record exposes the kind, form, logical lexeme, original units
and span, decoded payload, provenance pieces, and literal-owned logical LFs
defined by the preceding chapters. Numeric results expose exact normalized
components rather than an implementation float. The operation neither scans
preceding input nor guesses a following parser production.

The bootstrap evidence names this operation `Catena.scan_literal/2` and its
records `Catena.Literal`, `Catena.Literal.Numeric`,
`Catena.Literal.Piece`, and `Catena.Literal.ScanResult`. These Elixir names and
structs are evidence API names, not required names for every implementation.

C017 defines no whole-source lexer, parser, source compiler, literal renderer,
runtime numeric type, collection parser, or CLI. Implementations MUST NOT use
this abstract boundary to claim those later phases (`LT-OBL-010`,
`LT-OBL-012`).

## Determinism

Equal source bytes, exact language selection, and unit index produce equal
successful records or equal stable diagnostics. Raw delimiter matching,
numeric value calculation, scalar decoding, payload-size measurement, and
provenance splitting are deterministic (`LT-OBL-011`).

## Conformance obligations

| ID | Obligation | Required executable evidence |
| --- | --- | --- |
| `LT-OBL-001` | apply literal behavior only at exact 0.1.13 and register the stable lifecycle addition | exact selection, registry, and lifecycle tests |
| `LT-OBL-002` | recognize exactly the six atomic kinds and reject or defer the named exclusions | form matrix, boundary, sign, collection, symbol, byte-character, and interpolation-prefix tests |
| `LT-OBL-003` | enforce numeric bases, component grammar, separators, leading zeros, suffix boundary, and exact normalized result | positive metadata and malformed spelling tests |
| `LT-OBL-004` | recognize cooked delimiters and arbitrary exact raw hash delimiters without a language hash ceiling | delimiter, mismatch, unterminated, and deep-hash tests |
| `LT-OBL-005` | preserve logical lexeme, C013 units and spans, scalar spelling, decoded pieces, and no normalization | Unicode, CRLF, verbatim, escape, and span tests |
| `LT-OBL-006` | enforce the closed escape set, scalar validity, one-scalar characters, and direct-ASCII byte rules | escape, character, Unicode, and octet boundary tests |
| `LT-OBL-007` | keep every raw LF inside the token and outside C015 layout | multiline raw text/bytes and owned-unit tests |
| `LT-OBL-008` | accept the `LIM002` and `LIM004` floors and refuse the next unit with structured measurements | exact boundary tests in decimal, based integer, text, and bytes |
| `LT-OBL-009` | emit stable selection, literal, and limit failures with reasons and original-byte spans | every diagnostic family and representative reason test |
| `LT-OBL-010` | keep the scanner atomic, lossless, and independent of whole lexing, parsing, rendering, and runtime typing | unit-index, next-index, record-shape, and absent-phase tests |
| `LT-OBL-011` | produce deterministic literal results and diagnostics | repeated-result tests |
| `LT-OBL-012` | preserve source-only and persisted-format separation and permanent static meaning of existing text forms | registry, forged-format, and excluded-interpolation tests |

Every obligation has at least one tagged passing test. The sibling compiler
gates the complete `LT-OBL-*` set against unknown and uncovered identifiers
before C017 conformance is claimed.

## Required evidence sets

Positive evidence includes both Booleans; all integer bases and hexadecimal
case; separator placement; dotted and exponent-only decimal floats; every
simple, hexadecimal, and Unicode escape; supplementary and combining scalars;
one-scalar characters; cooked and raw bytes; zero and large raw hash counts;
multiline raw literals; source-unit offsets; CRLF and multibyte spans; and
exact accepted implementation-limit boundaries.

Negative evidence includes invalid unit indexes and nonliteral candidates;
missing or invalid based digits; leading zeros; misplaced or repeated
separators; incomplete fractions and exponents; identifier suffixes;
unsupported signs, prefixes, suffixes, and based floats; unknown or incomplete
escapes; invalid scalars; cooked source LF and backslash continuation; empty or
multi-scalar characters; direct non-ASCII bytes; Unicode byte escapes;
unterminated delimiters; and the first values beyond both configured limits.

Exclusion evidence includes atom/symbol, byte-character, list, tuple, record,
map, and interpolation-looking prefixes. It demonstrates that the atomic API
does not expose a whole parser or compiler.

## Revision and persistence separation

Revision `0.1.13` is a compatible source-acceptance and diagnostic addition.
It adds no JSON AST version, kernel S-expression version, interface version,
artifact version, signature domain, typed-core form, runtime numeric behavior,
or BEAM representation (`LT-OBL-001`, `LT-OBL-012`).

The source-text decoder accepts cumulative revisions `0.1.9` through
`0.1.13`. Standalone identifier, layout, and comment operations retain their
exact 0.1.10, 0.1.11, and 0.1.12 selections and defaults. Literal scanning
requires exact 0.1.13. The next unused semantic patch is `0.1.14`.

Unprefixed cooked text and `r`-prefixed raw text remain static under future
same-edition revisions. Interpolation can be added only through a new opt-in
prefix and explicit lifecycle record; an implementation cannot reinterpret
0.1.13 text from surrounding syntax.

## Rationale and evidence (non-normative)

The design route is preserved in the
[literal synthesis](../../20-notes/catena-literal-grammar.md),
[resolved inquiry](../../40-inquiries/how-should-catena-spell-and-decode-literals.md),
and [topic map](../../10-maps/literal-grammar.md). The
[C017 record](../../50-journal/2026-08-18-c017-literal-grammar.md) records the
concrete sibling-compiler commands and archive validation.
