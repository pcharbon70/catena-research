---
title: "The Comparable Set"
kind: specification
created: "2026-08-26"
status: candidate
spec_version: "0.1.30"
tags:
  - equality
  - ordering
  - specification
aliases:
  - "Catena comparable set"
---

# The Comparable Set

## Status and authority

This chapter is the normative Catena 0.1.30 comparable-set contract.
It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It elevates, without amending, the equality fragment of
[Syntax and Safety](../clause-conditions/syntax-and-safety.md), the
value grammar of
[Value Forms and First-Classness](../values-and-evaluation/value-forms-and-first-classness.md),
and the record-equality rule of
[Sequential Dynamics](../formal-semantic-kernel/sequential-dynamics.md),
over the operator inventory of
[Operators and Punctuation](../operators-and-punctuation/README.md).

The rules apply only to source-language revision `0.1.30`. They do not
reinterpret retained manifests, interfaces, artifacts, or signed formats.

## The comparable and orderable domains

> **Normative definition.**

```text
comparable ::= integer | boolean | float
            | tuple { comparable }          -- every element comparable
            | record { comparable }         -- semantic label-to-value map
            | injection ( label , comparable )
            | constructor-value             -- fields comparable

orderable ::= integer | float
```

- **Equality** (`equal`, `not_equal`) admits exactly the comparable
  set, with both operands unified to one type (`EQ-OBL-002`).
- **Ordering** (`less`, `less_equal`, `greater`, `greater_equal`)
  admits exactly `Int` and `Float`, both operands unified to one
  orderable type (`EQ-OBL-003`). `Bool` is equality-only.
- **Structural recursion** is over the closed grammar: a composite is
  comparable iff every contained value is comparable. Record equality
  is semantic — field order never affects it, elevating the kernel's
  rule.

## The exclusion list

**Closures and process handles are never comparable** (`EQ-OBL-004`):
comparing them is `EQN001`. Their identity observability belongs to
G037 and G084; admitting identity equality here would pre-decide those
owners' answers — the overreach C029's uniform-first-classness
deliberately declined (all values are first-class; not all values
compare).

## Monomorphism

The comparison operators are **monomorphic** (`EQ-OBL-005`): both
operands unify to one type, and `Int`-versus-`Float` comparison is the
existing type error — no coercion, no promotion, no mixed comparison
operator. This elevates C018's no-coercion stance from literals to
operators; a heterogeneous numeric comparison, if ever wanted, is a
G061-era library function, not a primitive.

## The entry rule

A type not in the closed set has no comparability until its own slice
declares it (`EQ-OBL-006`): strings and binaries do not exist, and
every G040 built-in enters with its comparability stated where it is
introduced — the same discipline as C029's value-membership rule.

## The guard split

C003's condition fragment stays frozen (`EQ-OBL-007`): guards accept
the safe operator set over `Int` and `Bool` only, enforced
independently of the general rule. A `Float` comparison is legal in a
general expression and rejected in a guard, by two different checkers;
widening the general set can never widen the fragment.

## Deliberately separate work

The operator inventory and spellings remain C019's. The value grammar
remains C029's. Identity observability remains G037's; handle
semantics G084's. Future types' entries remain G040's. Eq/Ord trait
layers remain G061/G101's — the built-ins are non-overloadable, and
any overloading-by-trait requires an edition record.

## Rationale and evidence (non-normative)

The [equality synthesis](../../20-notes/catena-equality-and-ordering.md)
records why structural equality elevates the kernel's record fact, why
the exclusion list mirrors C029's deferred identity questions, and why
monomorphism follows C018. The [resolved
inquiry](../../40-inquiries/which-values-compare-and-how.md) and
[topic map](../../10-maps/equality-and-ordering.md) preserve the
decision route.
