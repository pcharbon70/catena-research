---
title: "The Definition of Standard ML (Revised)"
kind: source
created: "2026-07-31"
authors:
  - "Robin Milner"
  - "Mads Tofte"
  - "Robert Harper"
  - "David MacQueen"
published: 1997
citation_key: "milnerEtAl1997DefinitionStandardML"
container: "The MIT Press"
edition: "Revised edition"
isbn: "978-0-262-63181-5"
doi: null
url: "https://mitpress.mit.edu/9780262631815/the-definition-of-standard-ml/"
accessed: "2026-07-31"
tags:
  - algebraic-data-types
  - pattern-matching
  - program-semantics
  - type-inference
aliases:
  - "The Definition of Standard ML"
  - "SML '97 Definition"
---

# The Definition of Standard ML (Revised)

## Reference

Robin Milner, Mads Tofte, Robert Harper, and David MacQueen, *The Definition of
Standard ML (Revised)* (MIT Press, 1997). ISBN 978-0-262-63181-5.
[Publisher record](https://mitpress.mit.edu/9780262631815/the-definition-of-standard-ml/)
and [community-hosted definition](https://smlfamily.github.io/sml97-defn.pdf).

## Contribution

The book gives Standard ML a formal static and dynamic semantics. Its datatype
rules make precise several properties that informal descriptions often merge:
fresh nominal type identity, recursive scope, polymorphic constructor schemes,
constructor status in patterns, ordered match evaluation, abstraction, and
runtime failure for flagged partial matches.

## Method

The authors define syntax and semantic objects, then give relational inference
rules for elaboration and evaluation. Contexts record type names, type
functions, value environments, identifier status, and equality attributes.
Separate rules describe datatype generation, constructor bindings, patterns,
matches, modules, and opaque signature matching.

## Findings

- An ordinary datatype binding generates a fresh type name. Two declarations
  with the same spelling and constructor shape therefore introduce distinct
  nominal types; datatype replication is explicitly non-generative.
- All mutually declared type names enter scope while constructor argument
  types are elaborated, which gives recursive and mutually recursive
  declarations their intended meaning.
- A nullary constructor has the result datatype as its type. A payload-bearing
  constructor has a function type from its payload to that same result, closed
  over the declaration's type parameters.
- Identifier status distinguishes variables, value constructors, and exception
  constructors, so a name in a pattern is not interpreted merely by spelling.
- Matches are ordered: evaluation chooses the first matching rule. The
  definition requires implementations to report redundant and non-exhaustive
  function matches, while still defining a runtime `Match` failure for a
  flagged partial match.
- Abstract datatype and opaque module rules can hide generated type names and
  constructor environments while exposing selected operations.
- Whether a generated datatype admits structural equality depends on the
  equality properties of its components; equality is a checked attribute, not
  an automatic consequence of having constructors.

## Relevance

This source demonstrates that ordinary ADTs can be specified rigorously inside
an HM-family language without GADT-style local equalities. It supports nominal
generativity, typed constructor namespaces, recursive-group elaboration, and a
separation between pattern typing, coverage diagnostics, and runtime matching.
Catena need not copy Standard ML syntax, but it should match this level of
semantic precision.

## Limits

The definition specifies Standard ML, including historical choices Catena may
reject: non-exhaustive matches are warnings rather than errors, pattern failure
raises exceptions, constructor and variable namespaces have SML-specific
rules, and state affects the wider dynamic semantics. It does not cover GADTs,
row-polymorphic structural variants, effects as rows, or modern layout
optimization.

## Derived work

- [Algebraic Data Types](../20-notes/algebraic-data-types.md)
- [A Greenfield Type System for Catena](../20-notes/catena-greenfield-type-system.md)
- [How Should Catena Specify Algebraic Data Types?](../40-inquiries/how-should-catena-specify-algebraic-data-types.md)
- [Algebraic Data Types map](../10-maps/algebraic-data-types.md)
