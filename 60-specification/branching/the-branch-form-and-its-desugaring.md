---
title: "The Branch Form and Its Desugaring"
kind: specification
created: "2026-08-25"
status: normative
spec_version: "0.1.29"
tags:
  - branching
  - specification
  - conditionals
aliases:
  - "Catena branch form"
---

# The Branch Form and Its Desugaring

## Status and authority

This chapter is the normative Catena 0.1.29 branch-form contract. It
is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It elevates, without amending, the match contract of
[Match Semantics and Coverage](../data-and-patterns/match-semantics-and-coverage.md)
and the condition fragment of
[Syntax and Safety](../clause-conditions/syntax-and-safety.md).

The rules apply only to source-language revision `0.1.29`. They do not
reinterpret retained manifests, interfaces, artifacts, or signed formats,
and they change no C002, C003, or C010 rule.

## Match is the only branch form

> **Normative definition.**

```text
match scrutinee { clause* }
clause := pattern [ when condition ] -> body
```

The match expression is the **single** branch form of the language
(`BR-OBL-002`): every selection among alternative computations — by
datatype structure, by Boolean value, or by guarded condition — is a
match. No other branch form exists at 0.1.29, and no retained input
encodes one.

## The conditional sugar promise

Any future conditional surface spelling a revision or edition
introduces **desugars to shipped semantics** (`BR-OBL-003`):

> **Normative definition.**

```text
if e then a else b    ⟺    match e { true -> a , false -> b }
```

- An `if`-like spelling is a match on a `Bool` scrutinee with `true`
  and `false` patterns; a guarded spelling is C003's
  `pattern when condition -> body` clause. The desugaring is fixed
  now; only the punctuation remains P109's to draw, and the widened
  P109 scope note's grammar exercise consumes this promise rather than
  inventing conditional semantics.
- An implementation MUST NOT use this chapter's boundary to claim a
  conditional form with semantics match does not already carry; any
  non-desugaring conditional requires an edition record naming the
  form and why match's semantics are insufficient.

## Boolean-pattern dispatch

Matching a `Bool` scrutinee against `true`/`false` patterns is the
conditional's executable form (`BR-OBL-003`): both patterns present,
the match is exhaustive; the scrutinee evaluates once; exactly one
body runs. Conditions inside clauses compose with `and`/`or` under
the C029-gated skips, exactly as
[Syntax and Safety](../clause-conditions/syntax-and-safety.md) fixes.

## Deliberately separate work

Match typing, coverage, and redundancy remain C002's. The condition
fragment remains C003's. Termination beyond tail guarantees remains
P034's. The failure taxonomy for a trapping scrutinee remains G036's.
Future scrutinee types enter with their coverage entries in their own
G040 slices. Surface spellings remain P109's.

## Rationale and evidence (non-normative)

The [branching synthesis](../../20-notes/catena-branching.md) records
why match-only is an elevation — every conditional in the corpus's
evidence is already a match or guarded clause, and the retained inputs'
frozen tags admit no new form — and why the promise follows the C032
multi-param-sugar pattern. The [resolved
inquiry](../../40-inquiries/what-is-catenas-branching-model.md) and
[topic map](../../10-maps/branching.md) preserve the decision route.
