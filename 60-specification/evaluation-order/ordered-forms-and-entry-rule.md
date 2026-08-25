---
title: "Ordered Forms and Entry Rule"
kind: specification
created: "2026-08-25"
status: normative
spec_version: "0.1.26"
tags:
  - evaluation-order
  - specification
aliases:
  - "Catena ordered forms"
---

# Ordered Forms and Entry Rule

## Status and authority

This chapter is the normative Catena 0.1.26 ordered-forms contract. It
is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It elevates, without amending, the order rules of
[Sequential Dynamics](../formal-semantic-kernel/sequential-dynamics.md)
and the fragments of C002, C003, C004, and C005, under the invariant
of [Strictness and Terminal Outcomes](../values-and-evaluation/strictness-and-terminal-outcomes.md).

The rules apply only to source-language revision `0.1.26`. They do not
reinterpret retained manifests, interfaces, artifacts, or signed formats,
and they change no 0.1.8 kernel rule.

## The ordered-forms table

Every compound form that exists at 0.1.26 has exactly one declared
order (`EO-OBL-002`, `EO-OBL-003`):

> **Normative definition.**

| Form | Declared order |
| --- | --- |
| Call (curried) | callee first, then arguments left-to-right as repeated unary application |
| Tuple construction | elements in written order |
| Record construction | fields in written order |
| Record update | base first, then the replacement value |
| Constructor application | fields in written order |
| Variant injection | payload after label selection |
| Match scrutinee | once, before any clause test |
| Operation arguments | written order |
| Spawn arguments | written order |
| Send | target first, then message |
| Trap | reason before the trap terminal |
| Binary operator | left operand, then right, each exactly once |
| `and` / `or` | left operand; right only when not skipped — the named exceptions C029 gates |
| `let` binding | right-hand side to a value, then substitution |
| Sequence | first to a value, then second |
| Trait call | subject first, then arguments |
| Handler | installation, then body |
| Annotate | transparent — the wrapped form's order, unchanged |

Clause-level order stays exactly as its owning area fixed it:
single-scrutinee evaluation and source-order commitment (C002);
pattern-before-condition, one condition evaluation, lazy left-to-right
Boolean composition, false fallthrough, irreversible body commitment,
and shared or-pattern continuations (C003); trait subject order and
callback positions (C004); handler order and resumed-prefix order
(C005). This table consolidates; it does not restate or alter those
rules.

## Typed-core completions

Three completions are new language-level content, fixing what the
kernel's unary calculus did not cover (`EO-OBL-003`):

- **Curried multi-argument application** — a call with several
  arguments is repeated unary application, left-to-right: the callee
  evaluates first, then each argument in written order before its
  application step.
- **Trait call** — the subject evaluates first, then the arguments,
  carrying C004's traversal rule into the call form itself.
- **Handler** — a handler expression installs its handler before its
  body evaluates, generalizing C005's clause to the expression; and
  **annotate** is order-transparent: wrapping a form in a type
  annotation changes nothing about its evaluation.

## The entry rule

A compound form not in the table has **no declared order** until its
own normative slice states one (`EO-OBL-005`). Collections,
interpolation, and every compound a future G040 built-in introduces
enter the language with their order entry declared where they are
introduced. Order never widens silently — the same discipline C029
fixed for value membership.

Any future exception to a declared order — a lazy form, a skip, a
reordering — requires the edition-record gate C029 fixed; no such
exception exists at 0.1.26.

## Order versus structure

This area owns **when** every existing compound evaluates. It does not
own the structure of what evaluates (`EO-OBL-008`): binding scope,
recursive bindings, mutual recursion, and unused-value rules remain
G031's (the `let` row above fixes only its evaluation schedule);
arity, currying as a typing concern, partial application, closure
capture, and tail-call guarantees remain G032's (the curried-call row
fixes only its evaluation fact); branch forms remain G033's.

## Deliberately separate work

G031–G033 as above; equality and ordering of values remain P035's;
the failure taxonomy beyond traps remains G036's; allocation
observability remains G037's; collections and interpolation remain
G040's with their table entries; cancellation mid-evaluation remains
G088's; surface syntax remains P109's.

## Rationale and evidence (non-normative)

The [order synthesis](../../20-notes/catena-evaluation-order.md)
records why consolidation-as-elevation was selected, why the
typed-core completions are the only new content, and why the entry
rule mirrors C029's. The [resolved
inquiry](../../40-inquiries/when-does-each-subexpression-evaluate.md)
and [topic map](../../10-maps/evaluation-order.md) preserve the
decision route.
