---
title: "The Three Context Classes"
kind: specification
created: "2026-08-31"
status: normative
spec_version: "0.1.38"
tags:
  - patterns
  - refutability
  - specification
aliases:
  - "Catena pattern context classes"
---

# The Three Context Classes

## Status and authority

This chapter is the normative Catena 0.1.38 context-classification
rule set. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It executes the refutability boundary of
[Construction and Pattern Typing](../data-and-patterns/construction-and-pattern-typing.md),
keeps the usefulness relation of
[Match Semantics and Coverage](../data-and-patterns/match-semantics-and-coverage.md)
authoritative, and applies the failure taxonomy of
[The Six Categories](../runtime-failure-taxonomy/the-six-categories.md).

The rules apply only to source-language revision `0.1.38`. They do
not reinterpret retained manifests, interfaces, artifacts, or
signed formats.

## The classification

> **Normative definition.**

Every pattern context — every syntactic position that binds by
pattern — belongs to exactly one of three classes (`PC-OBL-002`):

| Class | Rule on refutable patterns |
| --- | --- |
| **Exhaustive context** | patterns MUST cover the scrutinee type; the C045 usefulness relation decides, `M001` on a missing witness, `M002` on a useless row |
| **Irrefutable-only context** | a pattern MUST be proved total for the bound type by the same relation, or the form is static invalidity; no failure construct exists in the context |
| **Explicit-failure context** | the construct visibly names its mismatch behavior as part of its grammar; a refutable pattern is admissible only through that named behavior |

No pattern context in any Catena revision possesses an implicit
runtime match failure (`PC-OBL-003`): a mismatch either cannot
occur (proved total), selects the next clause (exhaustive context
selection), or produces the construct's named failure behavior.
Nothing raises an unnamed dynamic match exception.

## Match is the only exhaustive context

> **Normative definition.**

Match clauses are the exhaustive context, and C045's usefulness
relation and its diagnostics remain the sole authority for them,
unchanged by this area (`PC-OBL-003`). No other context acquires
coverage obligations, and no other context performs clause
selection over refutable patterns.

## The default

> **Normative definition.**

A binding position that does not visibly name a mismatch behavior
is irrefutable-only on arrival (`PC-OBL-004`): a new binding
context MUST either prove patterns total for the bound type or
define its explicit failure construct in the slice that introduces
it, following the C002 reservation. A refutable destructure has
three honest spellings — prove it total, make the failure a value
(a total result type such as `Option`), or make the selection
visible (`match` or an explicit filtering form) — and each
spelling's owner is named in
[Context Rules and Reservations](context-rules-and-reservations.md).

## Rationale and evidence (non-normative)

The [pattern-contexts synthesis](../../20-notes/catena-pattern-contexts.md)
argues why irrefutable-only is the forced default: C002 reserved
it, C036 leaves no exception to catch a mismatch with, C031 made
`let` a plain name so sequencing never hides selection, and the ADT
synthesis's refutability conclusions (an accidental partial
destructure must not become an invisible filter or a hidden crash)
supply the design evidence. The [resolved
inquiry](../../40-inquiries/which-pattern-contexts-admit-refutable-patterns.md)
preserves the decision route.
