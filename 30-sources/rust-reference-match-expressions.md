---
title: "The Rust Reference: Match Expressions"
kind: source
created: "2026-08-01"
published: null
citation_key: null
container: "The Rust Reference"
edition: null
isbn: null
doi: null
url: "https://doc.rust-lang.org/reference/expressions/match-expr.html"
accessed: "2026-08-01"
tags:
  - language-design
  - pattern-matching
aliases:
  - "Rust match guards"
---

# The Rust Reference: Match Expressions

## Reference

The Rust Project, “Match Expressions,” *The Rust Reference*, current online
edition accessed 2026-08-01.
[Official reference](https://doc.rust-lang.org/reference/expressions/match-expr.html).

## Research question

What problems appear when a clause guard admits general expressions,
conditional pattern bindings, ownership-sensitive values, and effects?

## Findings

- A Rust match guard may be a Boolean expression or a chain containing
  conditional `let` matches.
- The guard runs after its arm pattern succeeds and may use names bound by that
  pattern. False or a failed conditional match continues selection.
- Guard-chain operands run left to right and short-circuit. A successful
  conditional `let` introduces bindings for subsequent operands and the
  arm body.
- The reference explicitly warns that an or-pattern can cause a guard and its
  side effects to run more than once.
- Rust borrows matched values through a shared reference while checking the
  guard. This prevents mutation through those bindings and delays a move until
  the guard succeeds, but does not make the guard globally effect-free.

## Relevance

Rust demonstrates why “the guard runs after the pattern” is insufficient as an
operational contract. The language must also specify how or-patterns expand,
whether a guard may run more than once, when bindings become available, and
whether effects elsewhere in the guard are legal.

Catena's immutable values avoid Rust's move-and-borrow problem, but the
multiple-evaluation example remains directly relevant. Requiring pure,
guard-safe expressions lets the match compiler share or duplicate some tests
without duplicating user-visible actions, while an explicit cost contract is
still needed.

## Limits

Rust's ownership model, expression effects, and evolving guard-chain syntax
differ substantially from Catena's proposed functional core. The reference is
a semantic source, not empirical evidence that conditional bindings improve
comprehension.

## Derived work

- [Clause Guards](../20-notes/clause-guards.md)
- [Clause Guards map](../10-maps/clause-guards.md)
