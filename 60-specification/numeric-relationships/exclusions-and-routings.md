---
title: "Exclusions and Routings"
kind: specification
created: "2026-08-31"
status: candidate
spec_version: "0.1.40"
tags:
  - numerics
  - specification
aliases:
  - "Catena numeric exclusions"
---

# Exclusions and Routings

## Status and authority

This chapter is the normative Catena 0.1.40 numeric exclusion and
routing rule set. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It re-affirms the frozen exclusions of
[Numeric Types and Literal Typing](../numeric-literal-semantics/numeric-types-and-literal-typing.md)
and executes the routing of
[Precedence and Associativity](../operators-and-punctuation/precedence-and-associativity.md).

The rules apply only to source-language revision `0.1.40`.

## No dispatch, no overloadability

> **Normative definition.**

Numeric operators are never user-overloadable: no trait, instance,
derivation, or library declaration can add a meaning to an
operator, attach evidence to an operator site, or introduce a new
operator through any mechanism other than a new language revision
(`NR-OBL-003`). Operator tokens, precedence, and fixity remain
C019's closed inventory; reserved spellings stay reserved.

## The frozen exclusions, re-affirmed

> **Normative definition.**

- **No defaulting** — no numeric or other type defaulting exists
  (`NR-OBL-004`, `NM-OBL-005` unchanged).
- **No implicit coercion** — an operation expecting `Int` accepts
  no `Float` operand or literal, and vice versa; mixed numeric
  operands are ill-typed (`NR-OBL-004`, `NM-OBL-006` unchanged).
- **No literal constraints** — literals carry no constraints,
  generate none, and adapt to no expected type; their meaning is
  fixed by spelling under C017/C018 (`NR-OBL-004`).

## Division and remainder

> **Normative definition.**

Division, remainder, and every reserved spelling's eventual
semantics belong to the numeric library's own revision (`NR-OBL-007`):
checked and decimal arithmetic, division-by-zero classification
under C036's taxonomy, truncation and remainder sign rules, and
explicit `Int`/`Float` conversions are all G105's. No divide or
remainder operator exists in this revision (`NR-OBL-007`).

## Conversion boundary

> **Normative definition.**

Conversions between `Int` and `Float` are explicit named
operations whose library placement is G105's (`NR-OBL-004`,
`NM-OBL-006` unchanged); no context performs, inserts, or elides a
conversion.

## Rationale and evidence (non-normative)

The [numeric-relationships synthesis](../../20-notes/catena-numeric-relationships.md)
records why three of G061's five original options were already
rejected and why the fourth (dispatch) is rejected here. The
[routing](../operators-and-punctuation/precedence-and-associativity.md#deliberately-separate-work)
is C019's own.
