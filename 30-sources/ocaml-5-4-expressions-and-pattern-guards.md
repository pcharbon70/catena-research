---
title: "OCaml 5.4 Expressions and Pattern-Matching Guards"
kind: source
created: "2026-08-01"
published: null
citation_key: null
container: "The OCaml Manual"
edition: "5.4"
isbn: null
doi: null
url: "https://ocaml.org/manual/5.4/expr.html"
accessed: "2026-08-01"
tags:
  - pattern-matching
aliases:
  - "OCaml guard expressions"
---

# OCaml 5.4 Expressions and Pattern-Matching Guards

## Reference

OCaml, “The OCaml Language: Expressions,” *The OCaml Manual*, version 5.4,
section 7.
[Official manual](https://ocaml.org/manual/5.4/expr.html).

## Research question

What is the simplest mainstream ML account of an arbitrary Boolean clause
guard?

## Findings

- Function, `match`, and `try` cases may carry a `when`
  guard.
- The guard is an arbitrary expression required to have Boolean type.
- It is evaluated only after its pattern succeeds, in an environment extended
  by the pattern's bindings.
- A true result selects the associated body. A false result resumes matching
  at the following pattern rather than retrying the same pattern.
- Match alternatives are ordered; absent a successful case, ordinary
  `Match_failure` behavior applies.

Because the guard is an arbitrary expression, the ordinary OCaml semantics of
function calls, effects, divergence, and exceptions remain available inside
it. This last point is an inference from the unrestricted expression grammar
and the manual's general expression semantics, not a separate guard-specific
guarantee.

## Relevance

OCaml supplies the clean baseline rule Catena should keep: pattern first,
Boolean condition second, body on true, next clause on false. It also provides
the contrasting design Catena should not adopt without qualification. A
Boolean type alone says nothing about effects, termination, hidden failure, or
the cost of evaluating a guard.

## Limits

The manual specifies OCaml behavior rather than evaluating usability or
coverage precision. Its unrestricted guards coexist with OCaml's own effect,
exception, and exhaustiveness policies and cannot be transplanted into
Catena's explicit-effect architecture unchanged.

## Derived work

- [Clause Guards](../20-notes/clause-guards.md)
- [Clause Guards map](../10-maps/clause-guards.md)
