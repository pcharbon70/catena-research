---
title: "IEEE Std 754-2019: Floating-Point Arithmetic"
kind: source
created: "2026-08-21"
authors:
  - "IEEE"
published: 2019
citation_key: "ieee2019Std754"
container: "IEEE Standards Association"
edition: "Revision of IEEE Std 754-2008"
isbn: null
doi: "10.1109/IEEESTD.2019.8766229"
url: "https://doi.org/10.1109/IEEESTD.2019.8766229"
accessed: "2026-08-21"
tags:
  - floats
  - language-design
aliases:
  - "IEEE 754-2019"
---

# IEEE Std 754-2019: Floating-Point Arithmetic

## Reference

IEEE, *IEEE Standard for Floating-Point Arithmetic*, IEEE Std 754-2019
(Revision of IEEE Std 754-2008), 2019.
[Canonical DOI record](https://doi.org/10.1109/IEEESTD.2019.8766229).

## Research question or contribution

What exact value domain, rounding behavior, and conversion obligations does the
interchange standard assign to IEEE binary64 floating point, and which of those
obligations can a language specification adopt without also adopting
infinities and NaN?

## Method

The standard's requirements for the binary64 interchange format, rounding
attributes, subnormal results, and correctly rounded decimal conversion are
the portions consulted for Catena's numeric literal work. The boundary values
recorded below were additionally cross-checked against local OTP 29 behavior
(bit-pattern construction and arithmetic failure modes) so that no claim rests
on remembered constants. The 2019 revision's augmented operations, exchange
and reproducibility clauses, and decimal interchange formats were not needed
and are not summarized.

## Findings

- The binary64 format has one sign bit, an 11-bit exponent field with bias
  1023, and a 53-bit precision significand of which 52 trailing bits are
  stored. The unbiased exponent range runs from −1022 to +1023.
- The largest finite binary64 value is (2 − 2⁻⁵²) × 2¹⁰²³, approximately
  1.7976931348623157 × 10³⁰⁸. The smallest positive normal value is 2⁻¹⁰²²,
  approximately 2.2250738585072014 × 10⁻³⁰⁸. The smallest positive subnormal
  value is 2⁻¹⁰⁷⁴, approximately 4.9406564584124654 × 10⁻³²⁴.
- Zero is signed: +0 and −0 are distinct encodings of the same arithmetic
  value.
- `roundTiesToEven` is the default round-direction attribute for binary
  formats: a result is rounded to the nearest representable value, and an
  exact halfway result is rounded so that the least significant significand
  bit is even.
- Under `roundTiesToEven`, a result whose rounded magnitude exceeds the
  largest finite value overflows to an infinity of the result's sign. The
  standard defines infinities, quiet NaNs, and signaling NaNs as part of the
  format's encodings and operations.
- Nonzero results with magnitude below the smallest normal are subnormal:
  they are represented with reduced precision, giving gradual underflow. A
  correctly rounded result may be subnormal, and a nonzero exact value small
  enough rounds to a signed zero.
- Conversion between decimal character strings and a binary format is
  correctly rounded under the applicable rounding attribute: the converted
  result is the one obtainable by a single rounding of the exact decimal
  value.

## Relevance

C018 adopts the standard's binary64 finite domain, signed zeros,
subnormals, `roundTiesToEven`, and the correctly rounded conversion
obligation as the meaning of Catena decimal literals. It deliberately does
not adopt infinities or NaNs into the 0.1.14 `Float` value domain, because
the BEAM target raises on arithmetic that would produce them and because
Catena's conformance vocabulary forbids leaving such outcomes unspecified.
The standard is therefore the authority for what a correctly rounded finite
result is, while Catena's own normative text decides which results exist in
its domain.

## Limits

The standard defines an arithmetic system, not a programming language. It
assigns no literal syntax, no diagnostic identities, no static typing, and no
distinction between compile-time and runtime conversion. Its operation and
encoding clauses beyond binary64, its alternate rounding attributes, and its
decimal formats have no direct role in the bounded 0.1.14 decision, and the
clause-level structure of the 2019 revision differs from 754-2008 where
Catena cites only the requirements by name.

## Derived work

- [Catena Numeric Literal Semantics](../20-notes/catena-numeric-literal-semantics.md)
- [How Should Catena Define Numeric Literal Semantics?](../40-inquiries/how-should-catena-define-numeric-literal-semantics.md)
- [Numeric Literal Semantics map](../10-maps/numeric-literal-semantics.md)
