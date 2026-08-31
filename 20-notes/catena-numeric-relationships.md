---
title: "Catena Numeric Relationships"
kind: note
created: "2026-08-31"
maturity: developing
tags:
  - catena
  - numerics
  - language-design
aliases:
  - "closed-set numeric instantiation"
---

# Catena Numeric Relationships

## Executive conclusion

Numeric operators are built-in primitive forms with one typing
rule: the operands unify with each other and the operator
instantiates over exactly the closed set `{Int, Float}`. No trait
dispatch, no user overloadability, no defaulting, no implicit
coercion, no literal constraints — three of those four exclusions
were already frozen by C018, and this slice adds the fourth
(dispatch) as the actual G061 decision. Arithmetic joins ordering
and negation over `Float` at `0.1.40`: `add`/`subtract`/`multiply`
become same-type over `{Int, Float}`, witnessed end-to-end through
annotated float parameters because the frozen frontends carry no
float literals. Division and remainder belong to G105's numeric
library.

## Scope, method, and definitions

This note synthesizes the archive's evidence for closing G061 at
revision `0.1.40`. It reads C018's no-defaulting and no-coercion
clauses, C019's operator routing, C035's comparable set and
dormant float ordering, C040's numeric classification, and the two
checkers' existing rules; it invents no syntax.

- **Closed set** — the numeric runtime types of the current data
  model: `Int` and `Float` (C040). A future numeric type (decimal,
  arbitrary-precision integer) joins by amending this set in its
  own revision.
- **Same-type instantiation** — both operands unify to one member
  of the closed set; mixed operands are ill-typed (`NM-OBL-006`
  unchanged).

## Why instantiation, not dispatch

The corpus had already answered most of the question. C018 froze
no defaulting (consistent with 0.1.1/0.1.4's no-defaulting and
ambiguity rejection), no implicit coercion, and no constraint
generation. Ordering already types as same-type Int-or-Float by
operand unification, and negation is total over both. Only
arithmetic lagged — Int-only in both checkers, an asymmetry with
no principled defender. The remaining fork — a `Numeric` trait
with dispatch — would make operators user-overloadable in
principle and put instance evidence on every operator site,
cutting against operators-as-fixed-forms (C001/C019). Instantiation
keeps one fixed rule, checks in one place, and errors as one
unification failure.

## The witness without literals

Floats are values without literal spellings in either frozen
frontend. But an annotation types an operand: a definition
`f : Float → Float` whose body applies `add` to its parameter
needs no literal, so the extension is expressible, checkable, and
runnable today — the C035 dormant pattern becomes live. The
evaluator's arithmetic already computes Elixir floats; only the
checkers pinned the rule to Int.

## Tradeoffs, limitations, falsification

The closed set is an enumeration: a future numeric type amends it
by a new revision, and until then float arithmetic beyond
`+`/`-`/`*` (division, remainder, transcendental functions) simply
does not exist — G105's territory. If an operator ever resolves by
instance search or accepts mixed operands, this contract is
falsified and must be amended, not extended silently.

## Route to sources

- The Numeric Relationships Specification (candidate, then
  normative at promotion, in `60-specification/numeric-relationships/`)
  will define the contract this note argues for.
- [Numeric Types and Literal Typing](../60-specification/numeric-literal-semantics/numeric-types-and-literal-typing.md)
  — C018's no-defaulting and no-coercion clauses this slice
  inherits.
- [Precedence and Associativity](../60-specification/operators-and-punctuation/precedence-and-associativity.md)
  — C019's routing of dispatch and division to G061/G105.
- [The Comparable Set](../60-specification/equality-and-ordering/the-comparable-set.md)
  — the same-type pattern ordering already uses.
- [Numeric literal semantics map](../10-maps/numeric-literal-semantics.md)
  and the [resolved inquiry](../40-inquiries/how-should-int-and-float-relate-across-operators.md).
