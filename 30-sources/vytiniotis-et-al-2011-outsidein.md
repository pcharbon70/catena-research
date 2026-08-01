---
title: "OutsideIn(X): Modular Type Inference with Local Assumptions"
kind: source
created: "2026-07-31"
authors:
  - "Dimitrios Vytiniotis"
  - "Simon Peyton Jones"
  - "Tom Schrijvers"
  - "Martin Sulzmann"
published: 2011
citation_key: "vytiniotisEtAl2011OutsideIn"
container: "Journal of Functional Programming 21(4–5): 333–412"
edition: null
isbn: null
doi: "10.1017/S0956796811000098"
url: "https://simon.peytonjones.org/assets/pdfs/outsideinx.pdf"
accessed: "2026-07-31"
tags:
  - constraint-solving
  - local-assumptions
  - principal-types
  - type-inference
aliases:
  - "OutsideIn(X)"
---

# OutsideIn(X): Modular Type Inference with Local Assumptions

## Reference

Dimitrios Vytiniotis, Simon Peyton Jones, Tom Schrijvers, and Martin Sulzmann,
“OutsideIn(X): Modular Type Inference with Local Assumptions,” *Journal of
Functional Programming* 21, nos. 4–5 (2011), 333–412.
[DOI](https://doi.org/10.1017/S0956796811000098) and
[author-hosted paper](https://simon.peytonjones.org/assets/pdfs/outsideinx.pdf).

## Research question

How can constraint-based inference remain modular and return principal results
when features such as GADTs, type classes, and type families introduce local
type assumptions and implication constraints?

## Method

The paper separates constraint generation from solving and parameterizes the
framework over an underlying constraint domain `X`. It characterizes solver
properties, gives a concrete solver for Haskell-like constraints, proves
metatheoretic results for the framework, and reports an empirical study of
local `let` generalization in Haskell code.

## Findings

- Local assumptions can destroy principal types even when the surface typing
  rules appear natural. A sound algorithm therefore needs an explicit policy
  for programs whose declarative typings have incomparable solutions.
- The proposed algorithm deliberately accepts only programs for which it can
  compute principal types; completeness with respect to a more permissive
  declarative relation is not assumed.
- Constraint generation, simplification, and generalization have separable
  contracts. The simplifier must be terminating and satisfy principality and
  evidence requirements appropriate to the constraint domain.
- Implication constraints capture the scope of local givens. Flattening every
  obligation into one global bag loses information needed for correct solving.
- The paper argues against generalizing arbitrary local bindings in the
  presence of local assumptions. Top-level closed bindings remain a clearer
  generalization boundary.

## Relevance

This is a warning against presenting every advanced feature as “HM plus one
more unifier.” A greenfield Catena should expose a small principal-inference
fragment, scope constraints explicitly, and require signatures at boundaries
where local equalities or richer polymorphism would otherwise make inference
unpredictable.

## Limits

The concrete system is shaped by Haskell's GADTs, classes, and type families.
Its recommendation to restrict local generalization follows from that feature
set; a smaller language without local equality assumptions need not inherit the
same restriction wholesale.

## Derived work

- [Algebraic Data Types](../20-notes/algebraic-data-types.md)
- [How Should Catena Specify Algebraic Data Types?](../40-inquiries/how-should-catena-specify-algebraic-data-types.md)
- [Algebraic Data Types map](../10-maps/algebraic-data-types.md)
- [A Greenfield Type System for Catena](../20-notes/catena-greenfield-type-system.md)
- [What Should a Greenfield Catena Type System Guarantee?](../40-inquiries/what-should-a-greenfield-catena-type-system-guarantee.md)
- [Catena Type-System Design](../10-maps/catena-type-system-design.md)
