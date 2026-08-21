---
title: "Decimal Conversion and Overflow"
kind: specification
created: "2026-08-21"
status: normative
spec_version: "0.1.14"
tags:
  - floats
  - literals
  - specification
aliases:
  - "Catena decimal conversion and overflow"
---

# Decimal Conversion and Overflow

## Status and authority

This chapter is the normative Catena 0.1.14 decimal-conversion, rounding,
and overflow contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It consumes the exact integral, fractional, and exponent components defined
by [Exact Numeric Result](../literal-grammar/literal-forms-and-boundaries.md#exact-numeric-result)
and defines the `Float` values required by
[Numeric Types and Literal Typing](numeric-types-and-literal-typing.md).

The rules apply only to source-language revision `0.1.14`.

## Exact decimal meaning

The exact meaning of a decimal token is the rational number defined as
follows.

> **Normative definition.**

```text
value = M × 10^E
```

where `M` is the nonnegative integer formed by the separator-free integral
and fractional digits with the decimal point removed, and `E` is the signed
integer formed by the exponent sign class and the separator-free exponent
digits, minus the count of fractional digits (`NM-OBL-010`).

An implementation MUST construct this exact meaning from the C017
components without first passing the spelling through a host
decimal-to-float parser, unless the facility used is shown to return the
correctly rounded result defined below for the supplied components. The
bootstrap evidence computes `M` and `E` with exact integer arithmetic.

## Correct rounding

The `Float` value of a decimal literal is the binary64 value nearest to its
exact meaning under the `roundTiesToEven` attribute: the result is rounded
once, to nearest, and an exact halfway value between two adjacent binary64
numbers rounds to the one whose least significant significand bit is zero
(`NM-OBL-011`).

Conversion is deterministic from the components alone: equal components
produce equal results on every conforming implementation. Any conversion
algorithm MAY be used, including scaled exact integer arithmetic with
explicit significand alignment, provided it yields the correctly rounded
result for every accepted token.

## Underflow and subnormal results

A correctly rounded result below the smallest normal magnitude 2⁻¹⁰²² is a
subnormal value with reduced precision and is a valid `Float` result. An
exact meaning too small to round up to the smallest subnormal 2⁻¹⁰⁷⁴ rounds
to zero with the literal's sign and is valid; it is not an error, a
diagnostic, or a limit (`NM-OBL-011`).

## Overflow and static invalidity

A decimal literal whose correctly rounded result is not a finite binary64
value is statically invalid. Under `roundTiesToEven` this is exactly the
set of tokens whose exact meaning has magnitude greater than or equal to
2¹⁰²⁴ − 2⁹⁷⁰, the halfway point between the largest finite magnitude and
the next would-be magnitude. The largest finite magnitude itself and every
value rounding to it are valid (`NM-OBL-012`).

Overflow refusal is semantic invalidity carried by `NUM001`, not an
implementation limit and not a runtime trap: the token denotes no `Float`
value, so the input is rejected before any successful elaboration result is
published, following the transactional failure rules of the repository
conformance vocabulary.

> **Normative conformance example.**

```text
1.7976931348623157e308
     rounds to the largest finite magnitude and is valid
179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.0
     is exactly the largest finite magnitude and is valid
1.7976931348623159e308
     exceeds the halfway magnitude and is statically invalid as NUM001
1.0e400
     is statically invalid as NUM001
4.9406564584124654e-324
     rounds to the smallest subnormal and is valid
2.4703282292062327e-324
     is exactly half the smallest subnormal, ties to even zero, and is valid
1.0e-400
     underflows to zero and is valid
```

## Integer literal values

An integer literal denotes exactly the nonnegative mathematical integer
returned by C017 scanning; negation, where elaborated, denotes its additive
inverse. No rounding, width, or representation limit applies to the value
itself; input magnitude remains governed by the literal-grammar area's
`LIM002` (`NM-OBL-009`).

## Deliberately separate work

Runtime float arithmetic, its exceptional outcomes, and its failure
taxonomy remain G036. Explicit `Int`/`Float` conversions, decimal types, and
checked arithmetic remain G105. Numeric literal spelling and components
remain the exact 0.1.13 literal-grammar contract.

## Rationale and evidence (non-normative)

The [numeric literal synthesis](../../20-notes/catena-numeric-literal-semantics.md)
records the IEEE 754 basis, the BEAM `badarith` and host-parser evidence,
and the rejected overflow alternatives. Local OTP 29 verification of the
boundary constants is preserved in the
[C018 evidence record](../../50-journal/2026-08-21-c018-numeric-literal-semantics.md).
