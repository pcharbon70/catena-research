---
title: "The Surface Contract"
kind: specification
created: "2026-08-31"
status: candidate
spec_version: "0.1.39"
tags:
  - comprehensions
  - specification
aliases:
  - "Catena comprehension grammar"
---

# The Surface Contract

## Status and authority

This chapter is the normative Catena 0.1.39 comprehension surface
contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It consumes the generator principle of
[The Three Context Classes](../pattern-contexts/the-three-context-classes.md)
and the collection machinery settled by C042.

The rules apply only to source-language revision `0.1.39`. They do
not reinterpret retained manifests, interfaces, artifacts, or
signed formats.

## The grammar's semantic roles

> **Normative definition.**

A comprehension is `for pattern in source qualifier* yield
expression` (`LC-OBL-002`):

| Role | Form | Rule |
| --- | --- | --- |
| Ordinary generator | `pattern in source` | the pattern MUST be total for the element type (C044's irrefutable-only class; the usefulness relation decides) |
| Filtering generator | `case pattern in source` | the pattern MAY be refutable; a mismatch alone skips that element — this is the only explicit-failure binding context in the grammar |
| Boolean filter | `when expression` | the expression MUST have type `Bool`; `false` skips; effects are visible |
| Local binding | `let pattern = expression` | the pattern MUST be total for the expression's type (C031's plain-name `let` is unchanged outside comprehensions) |
| Result | `yield expression` | exactly one, last, producing every element |

A comprehension contains at least one generator and its first
qualifier is a generator (`LC-OBL-002`). Comprehension-local
`let`-pattern bindings are irrefutable-only per C044; they are not
the C031 statement-level `let`.

## Keywords and the adoption boundary

> **Normative definition.**

`for`, `in`, `case`, `when`, `let`, `=` (in the binding role), and
`yield` are the comprehension keywords of this grammar
(`LC-OBL-002`). No frozen frontend (JSON AST `0.1.1`–`0.1.7`,
kernel `0.1.8`, source-text revisions through `0.1.39`) carries
comprehension expressions; adoption is the surface-grammar
capstone's, which MUST realize these semantic roles and keywords
and owns token-level punctuation, layout, and block forms
(`LC-OBL-002`). Until adoption, the executable surface of this
contract is the dormant elaboration boundary of
[Elaboration and Lowering](elaboration-and-lowering.md#the-dormant-adoption-boundary).

## Eager ordered production

> **Normative definition.**

A comprehension produces its complete `List B` result eagerly in
traversal order before the expression's value exists
(`LC-OBL-009`). Lazy streams, generators as producers, and infinite
inputs are excluded from this revision; any future form carries
its own resource-lifetime, cancellation, and backpressure contract
in its own slice (`LC-OBL-009`).

## The result-type boundary

> **Normative definition.**

The result is `List B` where `B` is the yield expression's type
(`LC-OBL-011`). Map, set, binary, stream, validation-value, and
arbitrary `Applicative` or `Monad` targets are excluded
(`LC-OBL-011`); a target other than a list requires its own slice
naming its construction, failure, and ordering semantics.

## Rationale and evidence (non-normative)

The [list-comprehensions synthesis](../../20-notes/list-comprehensions.md)
argues the result-last form (bindings read in execution order), the
`case` marker (silent data loss motivated EEP 70's explicit strict
form), and lists-only (generic carriers blur categorical `map` with
effectful traversal). The [resolved
inquiry](../../40-inquiries/how-should-catena-specify-list-comprehensions.md)
preserves the decision route; the [topic
map](../../10-maps/list-comprehensions.md) organizes it.
