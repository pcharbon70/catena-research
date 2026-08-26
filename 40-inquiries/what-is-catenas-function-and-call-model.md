---
title: "What Is Catena's Function and Call Model?"
kind: inquiry
created: "2026-08-25"
status: resolved
tags:
  - catena
  - functions
  - calls
  - currying
  - tail-calls
  - language-design
aliases:
  - "G032 functions and calls inquiry"
---

# What Is Catena's Function and Call Model?

## Purpose

G032 asks the checklist question: "Define currying or fixed arity,
partial application, closure capture, named functions, anonymous
functions, local functions, and tail-call guarantees." The kernel and
the compiled evidence already fix most of the substance — closures as
values with one-argument substitution, multi-argument calls as
repeated unary application, and the proper-tail-call guarantee — but
scattered across the 0.1.8 calculus, the backend chapter, and test
behavior. This inquiry elevates the model and closes the two open
forms: local functions and the arity statement.

## Operational definitions

- **Semantic-unary** — every function takes exactly one argument;
  multi-parameter definitions desugar to nested unary functions.
- **Partial application** — applying a multi-parameter function to
  fewer arguments than its parameter count yields a closure value.
- **Lexical capture** — a closure carries its defining environment;
  captured bindings are immutable values.
- **Tail position** — a call whose value is immediately the enclosing
  definition's result, including after pattern or handler selection
  and a process loop after receive.

## Hypotheses

1. The arity model is **semantic-unary curried** — elevation of what
   the kernel, evaluator, and compiled evidence already do; zero arity
   errors to diagnose. *(Recommended: fixed arity would contradict the
   shipped curried-value behavior.)*
2. Partial application is **free prefix application** — any prefix
   application is a value; one sentence, already true everywhere.
3. Closure capture is **lexical and immutable** — the kernel's
   closure form elevated; allocation identity stays G037's exclusion.
4. The local-function form **is the let-bound closure** (C031's
   discipline): `let f = fn x -> …; …` — non-recursive, lexically
   captured, first-class. Local recursion stays definitions-only; any
   future local-recursion form goes through the edition gate.
5. Tail calls elevate the kernel guarantee verbatim, with a deep
   BEAM witness (a 1M-iteration tail recursion completing) and a
   stepper termination witness.

## Paths explored

- **Fixed arity** with over/under-application errors — rejected:
  contradicts shipped currying behavior; a behavior change, not an
  elevation.
- **Hybrid arity** (named fixed, anonymous curried) — rejected: two
  disciplines to keep consistent forever, with no evidence demanding
  it.
- **By-reference capture** — rejected: nothing mutates; a distinction
  with no witness.
- **Explicit capture lists** — rejected: new syntax, P109 territory.
- **Local recursive functions now** — rejected: reopens C031's
  just-shipped non-recursion boundary one slice after fixing it.
- **New local sugar form** — rejected: the desugaring statement covers
  multi-parameter spellings without a new form.
- **Tail-call deferral** — rejected: the kernel normatively fixes
  them; deferral leaves a shipped rule unelevated.
- **Arity diagnostics / normative-only** — incoherent or rejected
  patterns.

## Findings

All five hypotheses held; the developer chose the recommended option
on every fork (six of six, no overrides). One confirmation worth
recording: the proper-tail-call guarantee's strongest clause — a call
after pattern selection — is also the easiest to witness deeply,
because a counting recursion's match dispatch sits exactly there;
BEAM's last-call optimization is the native implementation, so the
witness proves the compiled path keeps what the kernel promises.

## Outcome

Resolved as C032 at revision `0.1.28`: the contract will live in
`60-specification/functions-and-calls/`, the reasoning in
[Catena Functions and Calls](../20-notes/catena-functions-and-calls.md),
and the forks in the [design decision
register](../20-notes/design-decision-register.md). G033 branching,
P034 termination beyond the tail guarantee, G037 closure allocation
identity, and P109 surface syntax remain open with their owners.
