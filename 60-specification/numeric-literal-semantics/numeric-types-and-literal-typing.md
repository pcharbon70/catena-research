---
title: "Numeric Types and Literal Typing"
kind: specification
created: "2026-08-21"
status: normative
spec_version: "0.1.14"
tags:
  - floats
  - integers
  - literals
  - specification
aliases:
  - "Catena numeric types and literal typing"
---

# Numeric Types and Literal Typing

## Status and authority

This chapter is the normative Catena 0.1.14 numeric value-domain and
literal-typing contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It consumes the exact numeric components defined by
[Literal Forms and Boundaries](../literal-grammar/literal-forms-and-boundaries.md)
and must preserve the inference contract of the
[Type System](../type-system/type-language-and-kinds.md).

The rules apply only to source-language revision `0.1.14`. They do not
reinterpret retained JSON AST literals, exact 0.1.8 kernel terms, interfaces,
artifacts, or signed formats, and they do not change 0.1.13 token spelling.

## Numeric value domains

The integer literal type is `Int`. `Int` is the set of all mathematical
integers, consolidating the exact domains already fixed by
[Clause Conditions](../clause-conditions/syntax-and-safety.md) and the
[Formal Semantic Kernel](../formal-semantic-kernel/canonical-kernel-syntax.md).
`Int` arithmetic has no overflow; input magnitude is bounded only by the
`LIM002` implementation limit of the literal-grammar area
(`NM-OBL-002`).

The decimal literal type is `Float`. `Float` is the set of finite IEEE
754-2019 binary64 values: zero, subnormal, and normal magnitudes with either
sign. The largest finite magnitude is (2 − 2⁻⁵²) × 2¹⁰²³; the smallest
positive normal magnitude is 2⁻¹⁰²²; the smallest positive subnormal
magnitude is 2⁻¹⁰⁷⁴ (`NM-OBL-003`).

`+0.0` and `-0.0` are two encodings of one arithmetic zero and are members
of `Float`. Equality, ordering, hashing, and pattern matching of the two
zero encodings are owned by P035 and are not decided here.

Infinities and NaNs are not members of `Float` in 0.1.14. No literal,
elaboration rule, or 0.1.14 operation constructs them. Arithmetic whose
IEEE 754 result would be infinite or NaN is outside this area's literal
boundary; classifying its runtime outcome is owned by G036 and MUST NOT be
supplied by an implementation of this chapter (`NM-OBL-003`).

## Literal typing

An integer token elaborates to a literal of type `Int` whose value is its
exact C017 mathematical value. A decimal token elaborates to a literal of
type `Float` whose value is the correctly rounded result defined by
[Decimal Conversion and Overflow](decimal-conversion-and-overflow.md)
(`NM-OBL-004`).

These typings are fixed and monomorphic. A numeric literal generates no
class or trait constraint, adopts no type from an expected type or
annotation, and resolves no type from its use sites. An unconstrained
integer literal is exactly as typed as one applied to a known `Int`
function.

## No defaulting and no implicit coercion

This chapter introduces no numeric defaulting. It is consistent with, and
adds no exception to, the 0.1.1 rule that Catena has no numeric or other
type defaulting and the 0.1.4 rule that ambiguous trait variables are
rejected rather than defaulted (`NM-OBL-005`).

This chapter introduces no implicit numeric coercion. An operation expecting
`Int` does not accept a `Float` operand or literal, an operation expecting
`Float` does not accept an `Int` operand or literal, and mixed numeric
operations such as integer-plus-decimal are ill-typed. Conversions between
`Int` and `Float` are explicit named operations whose library placement is
owned by G105 (`NM-OBL-006`).

## Numeric negation

Numeric unary negation is fixed as an elaboration operation on numeric
literals and numeric expressions. Applied to an `Int` value it yields the
additive inverse; the operation is total and has no overflow case
(`NM-OBL-007`).

Applied to a `Float` value it yields the value with the opposite sign
encoding, preserving magnitude: negating `0.0` yields `-0.0`, negating
`-0.0` yields `0.0`, and negating any nonzero value yields the opposite
value of equal magnitude. Negation performs no rounding; a negated literal
denotes the negation of the literal's converted value.

The surface spelling, precedence, and fixity of negation are owned by G019
and are not decided here. A leading `-` remains outside the 0.1.13 token.

## Pattern boundary

The pattern grammar of 0.1.2 is unchanged: integer patterns admit only
unsigned integer tokens, and `Float` has no literal pattern form in 0.1.14.
A negative value therefore matches nothing through a literal pattern, and
any negative or floating pattern extension is future pattern work with its
own coverage and usefulness story (`NM-OBL-008`).

## Deliberately separate work

G019/P109 own negation spelling, precedence, and operator tokens. G040 owns
placing `Int` and `Float` inside the complete built-in data model, including
sendability, serialization, and any further numeric types. G061 owns numeric
trait relationships and any overloaded operators. G105 owns explicit
conversions, checked and decimal arithmetic, and the numeric library. P035
owns primitive equality and ordering, including mixed-type comparisons and
the two zero encodings. G036 owns the runtime failure taxonomy for
arithmetic that cannot produce a value in the 0.1.14 domains.

## Rationale and evidence (non-normative)

The [numeric literal synthesis](../../20-notes/catena-numeric-literal-semantics.md)
compares IEEE, Erlang, Haskell, and Rust designs and explains the
monomorphic, finite-domain choice. The
[resolved inquiry](../../40-inquiries/how-should-catena-define-numeric-literal-semantics.md)
and [topic map](../../10-maps/numeric-literal-semantics.md) preserve the
decision route.
