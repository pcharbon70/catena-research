---
title: "Arity and Application"
kind: specification
created: "2026-08-25"
status: normative
spec_version: "0.1.28"
tags:
  - functions
  - specification
  - currying
aliases:
  - "Catena arity model"
---

# Arity and Application

## Status and authority

This chapter is the normative Catena 0.1.28 arity and application
contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It elevates, without amending, the closure and application rules of
[Sequential Dynamics](../formal-semantic-kernel/sequential-dynamics.md)
and the schedule of
[Ordered Forms and Entry Rule](../evaluation-order/ordered-forms-and-entry-rule.md).

The rules apply only to source-language revision `0.1.28`. They do not
reinterpret retained manifests, interfaces, artifacts, or signed formats,
and they change no 0.1.8 kernel rule.

## The semantic-unary model

Every Catena function takes exactly one argument (`FC-OBL-002`):

> **Normative definition.**

```text
fn (x) -> body                  -- one parameter, one body
def name (p1, ..., pn) = rhs    -- sugar: nested unary functions
name a1 a2 ... an               -- repeated unary application
```

- A multi-parameter definition desugars to nested unary functions:
  `def name (p1, p2) = rhs` means `def name (p1) = fn (p2) -> rhs`.
  The desugaring is total and deterministic; the surface spelling is
  P109's, and this chapter fixes its semantics (`FC-OBL-002`).
- A multi-argument call is repeated unary application under C030's
  curried-call row: the callee evaluates first, then each argument in
  written order before its application step.
- There is no fixed arity to check: under- and over-application are
  impossible states, and no arity diagnostic exists (`FC-OBL-008`).

## Partial application

Applying a multi-parameter function to a prefix of its arguments
yields a closure value (`FC-OBL-003`): first-class, storable,
returnable, and callable later. Partial application is free — no
explicit form, marker, or permission exists, and every prefix
application is a value under C029's grammar.

## Named and anonymous functions

- A **named function** is a module definition, callable through C031's
  definitions-only recursion environment and exportable under C022.
- An **anonymous function** is the one-parameter `fn` expression: a
  closure value when evaluated, under C029's value grammar.

Both forms are shipped behavior; this chapter states them at the
language level.

## Deliberately separate work

Application evaluation order remains C030's. Binding structure and
non-recursion remain C031's. Branch forms remain G033's. Closure
allocation and identity observability remain G037's. Calling
conventions remain G094's. Multi-parameter and application surface
spellings remain P109's.

## Rationale and evidence (non-normative)

The [functions synthesis](../../20-notes/catena-functions-and-calls.md)
records why semantic-unary is an elevation of shipped behavior rather
than a choice, with the curried-value compiler evidence. The
[resolved inquiry](../../40-inquiries/what-is-catenas-function-and-call-model.md)
and [topic map](../../10-maps/functions-and-calls.md) preserve the
decision route.
