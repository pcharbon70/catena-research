---
title: "Numeric Diagnostics, Limits, and Conformance"
kind: specification
created: "2026-08-21"
status: normative
spec_version: "0.1.14"
tags:
  - conformance
  - diagnostics
  - floats
  - integers
  - limits
  - literals
  - specification
  - testing
aliases:
  - "Catena 0.1.14 numeric conformance"
---

# Numeric Diagnostics, Limits, and Conformance

## Status and authority

This chapter is the normative Catena 0.1.14 numeric diagnostic, limit,
abstract-frontend, representation, and conformance contract. It is governed
by [Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies [Numeric Types and Literal Typing](numeric-types-and-literal-typing.md)
and [Decimal Conversion and Overflow](decimal-conversion-and-overflow.md).

## Stable diagnostics

| ID | Required meaning |
| --- | --- |
| `NUM001` | a decimal literal's correctly rounded result is not a finite binary64 value |

Every numeric-literal rejection carries the stable diagnostic ID, a primary
original-byte span derived from the C017 provenance of the token, and a
stable reason. Malformed numeric spelling remains `LIT003`; oversized
integer magnitude remains `LIM002`; oversized decimal components are refused
under `LIM005` below. An exact-selection mismatch remains `EDN001`
(`NM-OBL-012`).

Invalid input produces no successful elaboration result, converted value, or
other successful frontend output for the affected action. Diagnostic prose
can improve only within the bounded presentation rules of the repository
conformance vocabulary; identity, severity, reason, source span, acceptance,
and repair meaning do not vary.

## Numeric literal implementation limits

`LIM005` applies to each decimal token. The measured value is the total
count of decimal digits across the separator-free integral digits,
fractional digits, and exponent-magnitude digits of the C017 numeric
components. A token whose total is at or below 4,096 digits crosses no
decimal-component limit. The next digit is refused under the configured
bound with the common structured limit fields (`NM-OBL-013`).

`LIM005` bounds conversion work, not meaning: below the floor, conversion is
exact and deterministic; the limit never turns a representable decimal into
a refusal, and it does not apply to integer tokens, whose magnitude remains
governed by `LIM002`. Both limits follow the portable-floor,
configured-value, disclosure, and transactional-failure rules in the
repository implementation-limit policy.

## Abstract public boundary

A conforming implementation exposes an equivalent numeric elaboration
operation. It accepts the exact numeric components of one C017-scanned
numeric token and an exact language selection. It returns one complete typed
literal meaning — the kind `integer` or `decimal`, the type `Int` or
`Float`, and the exact integer value or the correctly rounded float value —
or exactly one diagnostic (`NM-OBL-001`). A separate total negation
operation yields the additive inverse on `Int` and the sign-flipped value on
`Float`.

The operation elaborates one token. It does not lex, parse, type-check a
program, resolve operators, evaluate arithmetic, or select a numeric library
operation. C018 defines no whole-source lexer, parser, type checker,
reference evaluator, or numeric CLI; implementations MUST NOT use this
boundary to claim those later phases (`NM-OBL-014`).

The bootstrap evidence names this operation `Catena.elaborate_numeric_literal/2`,
its records `Catena.Numeric.Meaning`, and the negation operation
`Catena.Numeric.negate/1`. These Elixir names are evidence API names, not
required names for every implementation.

## BEAM representation

A conforming BEAM implementation represents every `Int` value as an Erlang
integer and every `Float` value as an Erlang float. Erlang integers are
arbitrary precision and Erlang floats are finite binary64, so both mappings
are exact and value-preserving; an implementation MUST NOT introduce a
narrower integer representation or a saturating float representation
(`NM-OBL-014`).

Arithmetic on these values and its exceptional outcomes are outside this
area and remain owned by G036; nothing in this chapter licenses an
implementation to inherit host mixed-type numeric comparison or host
exceptional-float behavior as Catena semantics.

## Determinism

Equal numeric components and exact language selection produce equal
successful meanings or equal stable diagnostics on every conforming
implementation. Exact integer values, correctly rounded float values,
negation dispositions, limit measurement, and diagnostic identity are
deterministic (`NM-OBL-011` refers).

## Conformance obligations

| ID | Obligation | Required executable evidence |
| --- | --- | --- |
| `NM-OBL-001` | apply numeric meaning only at exact 0.1.14 and register the stable lifecycle addition | exact selection, registry, and lifecycle tests |
| `NM-OBL-002` | fix `Int` as the unbounded mathematical integers with no value overflow | domain and exact-value tests |
| `NM-OBL-003` | fix `Float` as finite binary64 with signed zero and no infinities or NaN | domain, zero-encoding, and exclusion tests |
| `NM-OBL-004` | type integer literals `Int` and decimal literals `Float`, monomorphically and independent of context | typing and context-independence tests |
| `NM-OBL-005` | introduce no numeric defaulting, constraint generation, or expected-type adaptation | unconstrained-literal and no-constraint tests |
| `NM-OBL-006` | introduce no implicit numeric coercion; mixed numeric operands are ill-typed | mixed-type rejection tests |
| `NM-OBL-007` | elaborate numeric negation total on `Int` and sign-flipping on `Float`, including `-0.0` | negation and negative-zero tests |
| `NM-OBL-008` | keep pattern grammar unsigned; negative and float pattern forms stay excluded | pattern-boundary tests |
| `NM-OBL-009` | denote an integer literal by its exact C017 mathematical value | based-integer exact-value tests |
| `NM-OBL-010` | construct the exact rational meaning from the C017 components | component-to-meaning tests |
| `NM-OBL-011` | round once to nearest binary64 with ties to even, admitting subnormals and underflow to zero | tie, subnormal, underflow, and boundary-value tests |
| `NM-OBL-012` | refuse a decimal whose rounded result is not finite as `NUM001` static invalidity | overflow and largest-finite boundary tests |
| `NM-OBL-013` | accept the `LIM005` 4,096-digit floor and refuse the next digit with structured measurements | exact decimal-component boundary tests |
| `NM-OBL-014` | map `Int` to the Erlang integer and `Float` to the Erlang float and preserve source-only/persisted-format separation | representation, pinned 0.1.13 scanning, and forged-format tests |

Every obligation has at least one tagged passing test. The sibling compiler
gates the complete `NM-OBL-*` set against unknown and uncovered identifiers
before C018 conformance is claimed.

## Required evidence sets

Positive evidence includes integer tokens in every C017 base with exact
values; decimals that round to normal, subnormal, and zero magnitudes; the
shortest and exact decimal spellings of the largest finite magnitude; ties
resolving to even significands at normal, subnormal, and half-subnormal
boundaries; signed zero from negation; and exact accepted `LIM005`
boundaries.

Negative evidence includes the first decimal past the halfway magnitude, an
extreme exponent overflow, mixed-type operand rejection, constraint or
defaulting absence probes, and the first decimal component digit beyond the
configured `LIM005` bound.

Exclusion evidence demonstrates that infinities and NaNs are not constructible
by any 0.1.14 literal or elaboration, that no runtime arithmetic, operator
resolution, or numeric library behavior is claimed through this boundary, and
that C017 scanning remains pinned to exact 0.1.13 while numeric elaboration
requires exact 0.1.14.

## Revision and persistence separation

Revision `0.1.14` is a compatible semantic addition for numeric literal
meaning. It adds no JSON AST version, kernel S-expression version, interface
version, artifact version, signature domain, operator token, pattern form,
or runtime arithmetic rule (`NM-OBL-001`, `NM-OBL-014`).

The source-text decoder accepts cumulative revisions `0.1.9` through
`0.1.14`. Literal scanning and its default remain pinned to exact `0.1.13`;
standalone identifier, layout, and comment operations retain their exact
0.1.10, 0.1.11, and 0.1.12 selections and defaults. Numeric elaboration
requires exact `0.1.14`. The next unused semantic patch is `0.1.15`.

## Rationale and evidence (non-normative)

The design route is preserved in the
[numeric literal synthesis](../../20-notes/catena-numeric-literal-semantics.md),
the [resolved inquiry](../../40-inquiries/how-should-catena-define-numeric-literal-semantics.md),
and the [topic map](../../10-maps/numeric-literal-semantics.md). The
[C018 record](../../50-journal/2026-08-21-c018-numeric-literal-semantics.md)
preserves the sibling-compiler commands, boundary-value derivations, and
archive validation.
