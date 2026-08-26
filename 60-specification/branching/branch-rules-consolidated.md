---
title: "Branch Rules Consolidated"
kind: specification
created: "2026-08-25"
status: candidate
spec_version: "0.1.29"
tags:
  - branching
  - specification
aliases:
  - "Catena consolidated branch rules"
---

# Branch Rules Consolidated

## Status and authority

This chapter is the normative Catena 0.1.29 consolidated statement of
the branch rules. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It consolidates, without amending or displacing, the rules of
[Match Semantics and Coverage](../data-and-patterns/match-semantics-and-coverage.md),
[Syntax and Safety](../clause-conditions/syntax-and-safety.md),
[Sequential Dynamics](../formal-semantic-kernel/sequential-dynamics.md),
[Strictness and Terminal Outcomes](../values-and-evaluation/strictness-and-terminal-outcomes.md),
[Ordered Forms and Entry Rule](../evaluation-order/ordered-forms-and-entry-rule.md),
and
[Closures and Tail Calls](../functions-and-calls/closures-and-tail-calls.md).

The rules apply only to source-language revision `0.1.29`.

## The consolidated rules

One table states the branch rules at the language level; each row's
semantics remain its citing area's (`BR-OBL-004`):

> **Normative definition.**

| Rule | Statement | Home |
| --- | --- | --- |
| Scrutinee-once | the scrutinee evaluates exactly once, to a value, before any clause test | C002 / C030 |
| Clause order | clauses test in source order | C010 |
| Pattern before condition | a clause tests its pattern first; only structural success evaluates its condition | C003 |
| Condition typing | a condition is `Bool`-typed, from the closed safe operator set | C003 |
| Condition-once | a selected clause's condition evaluates exactly once | C003 |
| Fallthrough | a false condition continues with later clauses | C003 / C010 |
| Commitment | selection commits irreversibly to the chosen body; no other body runs | C003 / C010 |
| Branch typing | every clause body unifies with the match's type | C002 |
| Missing alternatives | a non-exhaustive match is invalid, `M001` carrying a witness | C002 |
| Redundancy | an unreachable clause is invalid per the coverage calculus | C002 |
| Boolean composition | conditions compose with `and`/`or` under the C029-gated skips | C010 / C029 |
| Tail position | a call after clause selection keeps the proper-tail-call guarantee | C032 |

No row changes its home's rule or diagnostic; `M001` and the
rejections remain C002's families with their identities unchanged
(`BR-OBL-008`).

## Statement-like control forms

**None exist** (`BR-OBL-005`):

> **Normative definition.**

Catena has no statement-like control forms. Every construct is an
expression: branching yields values through clause bodies; sequencing
for effect is the
[let idiom](../bindings-and-sequencing/unused-bindings-and-sequencing.md#the-sequencing-idiom);
failure is a trap terminal under the kernel taxonomy. There is no
early return, no break, no continue, and no statement tier at 0.1.29,
and any future exception enters through the edition-record gate C029
fixed — never as a compatible addition.

## Determinism

A closed match with exhaustive clauses selects deterministically:
equal scrutinees select equal bodies with equal traces on every
conformant target (`BR-OBL-008`).

## Deliberately separate work

Termination beyond tail guarantees remains P034's. Scrutinee-trap
classification remains G036's. Cancellation between scrutinee
evaluation and body evaluation remains G088's.

## Rationale and evidence (non-normative)

The [branching synthesis](../../20-notes/catena-branching.md) records
why consolidation-with-citations follows the C030 pattern and why the
statement absence is an answer rather than a gap — the kernel's
everything-is-an-expression architecture leaves no room for a second
sequencing semantics. The [topic map](../../10-maps/branching.md)
routes the decision.
