---
title: "Typing Haskell in Haskell"
kind: source
created: "2026-07-31"
authors:
  - "Mark P. Jones"
published: 1999
citation_key: "jones1999TypingHaskell"
container: "Haskell Workshop 1999"
edition: "Haskell Workshop version, 1999-09-01"
isbn: null
doi: null
url: "https://web.cecs.pdx.edu/~mpj/thih/thih-sep1-1999/thih.pdf"
accessed: "2026-07-31"
tags:
  - executable-specification
  - higher-kinded-types
  - qualified-types
  - type-inference
aliases:
  - "THIH"
---

# Typing Haskell in Haskell

## Reference

Mark P. Jones, “Typing Haskell in Haskell,” Haskell Workshop version,
September 1, 1999. [Author-hosted PDF](https://web.cecs.pdx.edu/~mpj/thih/thih-sep1-1999/thih.pdf)
and [project page](https://web.cecs.pdx.edu/~mpj/thih/).

## Contribution

Jones gives an executable Haskell specification of a Haskell 98 type checker.
It connects the compact formal literature to implementation concerns including
kinds, substitutions, matching, qualified schemes, class environments,
patterns, recursive binding groups, context reduction, and explicit
signatures.

## Method

The paper is literate executable code. Its data structures and functions form
a specification that can be typechecked and tested. The author optimizes for
clarity and completeness of the account rather than production performance.

## Findings

- Type substitutions should be kind-preserving, compose in a specified order,
  and apply uniformly to types, predicates, schemes, and assumptions.
- Most-general unification is the mechanism that keeps an inferred result as
  general as possible. Binding a variable requires both an occurs check and a
  kind check.
- Haskell-style class resolution is not ordinary two-way unification.
  Instance selection uses one-way matching, then recursively proves generated
  predicate subgoals under termination and non-overlap restrictions.
- Qualified schemes canonically bind generic variables and instantiate them
  freshly at use sites.
- Practical binding-group inference must divide inferred predicates into those
  retained in a scheme and those deferred to an enclosing scope. Simply
  attaching every accumulated constraint to every local binding is not an
  adequate general algorithm.
- Making an inference specification executable enables differential testing
  across implementations, but does not replace a separate declarative system
  and a proof of principality.

## Relevance

The paper offers concrete invariants and a useful model for a small executable
reference implementation: explicit substitutions, kinds, qualified types,
patterns, binding groups, and class-like instance lookup can be presented in
code clearly enough to support differential testing.

## Limits

The paper describes Haskell 98, including design choices such as its
monomorphism restriction and class rules that a new language need not adopt.
Jones explicitly states that the program is not intended as an efficient
production implementation and, because it gives only an inference
presentation, does not itself prove that its result is principal.

## Derived work

- [Hindley–Milner type inference](../20-notes/hindley-milner-type-inference.md)
- [A greenfield type system for Catena](../20-notes/catena-greenfield-type-system.md)
- [What should a greenfield Catena type system guarantee?](../40-inquiries/what-should-a-greenfield-catena-type-system-guarantee.md)
- [Catena type-system design map](../10-maps/catena-type-system-design.md)
