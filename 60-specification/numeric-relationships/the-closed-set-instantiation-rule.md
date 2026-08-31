---
title: "The Closed-Set Instantiation Rule"
kind: specification
created: "2026-08-31"
status: normative
spec_version: "0.1.40"
tags:
  - numerics
  - specification
aliases:
  - "Catena numeric instantiation"
---

# The Closed-Set Instantiation Rule

## Status and authority

This chapter is the normative Catena 0.1.40 numeric-operator
typing rule. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It generalizes the same-type pattern of
[The Comparable Set](../equality-and-ordering/the-comparable-set.md)
and keeps the literal rules of
[Numeric Types and Literal Typing](../numeric-literal-semantics/numeric-types-and-literal-typing.md)
unchanged.

The rules apply only to source-language revision `0.1.40`. They do
not reinterpret retained manifests, interfaces, artifacts, or
signed formats.

## The rule

> **Normative definition.**

Every numeric operator is a built-in primitive form with one fixed
typing rule (`NR-OBL-002`): the operand types unify with each
other, and the operator instantiates over exactly the closed set
`{Int, Float}` — the numeric runtime types of
[The Twelve-Way Classification](../built-in-data-model/the-twelve-way-classification.md).
Mixed `Int`/`Float` operands are static invalidity everywhere
(`NR-OBL-004`, unchanged `NM-OBL-006`).

| Operator class | Operands | Result |
| --- | --- | --- |
| Arithmetic (`add`, `subtract`, `multiply`) | same-type member of the closed set | the operand type (`NR-OBL-005`) |
| Ordering (`less`, `less_equal`, `greater`, `greater_equal`) | same-type member of the closed set | `Bool` (unchanged, C035) |
| Equality | the comparable set (unchanged, C035) | `Bool` |
| Negation (unary) | member of the closed set | the operand type (unchanged, C018) |

No operator resolves by instance search, trait dispatch, or any
user-provided declaration (`NR-OBL-003`).

## Float arithmetic

> **Normative definition.**

At `0.1.40`, `add`, `subtract`, and `multiply` accept same-type
`Float` operands and produce `Float` results, joining ordering and
negation over the closed set (`NR-OBL-005`). Float arithmetic
follows C018's finite binary64 semantics — no NaN, infinities
excluded by conversion — and the same-type rule: a `Float`
operand's partner MUST also be `Float`. No float literal spelling
and no float type spelling exist in any frozen frontend, so the
rule is **correct-but-dormant**: the executable witness drives the
inference engine directly with float-typed operands, and the rule
becomes input-reachable with the first float-bearing frontend
(`NR-OBL-005`).

## The closed set

> **Normative definition.**

The closed set is `{Int, Float}` and only that (`NR-OBL-002`). A
future numeric type (decimal, arbitrary-precision integer, or any
other) joins the set only by a new revision that amends this
chapter's enumeration explicitly; no implementation, library, or
trait declaration widens it (`NR-OBL-008`).

## Rationale and evidence (non-normative)

The [numeric-relationships synthesis](../../20-notes/catena-numeric-relationships.md)
argues why instantiation beats dispatch and how the annotated-
parameter witness makes float arithmetic expressible without new
syntax. The [resolved
inquiry](../../40-inquiries/how-should-int-and-float-relate-across-operators.md)
preserves the decision route.
