---
title: "Type Classes with Functional Dependencies"
kind: source
created: "2026-07-31"
authors:
  - "Mark P. Jones"
published: 2000
citation_key: "jones2000FunctionalDependencies"
container: "ESOP 2000, Lecture Notes in Computer Science 1782: 230–244"
edition: null
isbn: null
doi: "10.1007/3-540-46425-5_15"
url: "https://web.cecs.pdx.edu/~mpj/pubs/fundeps-esop2000.pdf"
accessed: "2026-07-31"
tags:
  - functional-dependencies
  - qualified-types
  - trait-constraints
  - type-inference
aliases:
  - "Jones functional dependencies"
---

# Type Classes with Functional Dependencies

## Reference

Mark P. Jones, “Type Classes with Functional Dependencies,” in *Programming
Languages and Systems, ESOP 2000*, LNCS 1782, 230–244.
[DOI](https://doi.org/10.1007/3-540-46425-5_15) and
[author-hosted paper](https://web.cecs.pdx.edu/~mpj/pubs/fundeps-esop2000.pdf).

## Research question

How can multi-parameter type classes express relationships among types without
creating ambiguous or needlessly imprecise inferred schemes?

## Method

Jones interprets class parameters relationally and imports the database notion
of a functional dependency. The paper extends qualified typing with declared
dependencies, describes an improvement process that derives type equalities
from them, and applies the mechanism to collections, state monads, and
overloaded multiplication.

## Findings

- Unrestricted multi-parameter classes often leave variables that occur only
  in predicates, producing ambiguous inferred types.
- A declaration such as `container -> element` states that the container type
  uniquely determines the element type. The solver may use that fact to improve
  an inferred scheme.
- Instance declarations must respect the declared relationship; incompatible
  instances make the class relation inconsistent.
- Improvement can make errors appear earlier and can turn otherwise ambiguous
  uses into determined types.
- Functional dependencies add a second solving layer beyond ordinary class
  entailment and unification. Their benefits therefore come with additional
  consistency and termination obligations.

## Relevance

The result supports a conservative trait roadmap for a greenfield Catena:
start with single-parameter coherent traits; add multi-parameter relations only
alongside explicit dependency declarations and solver rules. A broad trait
surface without an ambiguity policy would weaken the inference contract.

## Limits

The paper explores a powerful extension rather than prescribing a minimal
language. Later work refines coverage and termination conditions. This note
therefore uses it to justify staging and explicit dependencies, not to claim
that every functional-dependency program has principal terminating inference.

## Derived work

- [A Greenfield Type System for Catena](../20-notes/catena-greenfield-type-system.md)
- [What Should a Greenfield Catena Type System Guarantee?](../40-inquiries/what-should-a-greenfield-catena-type-system-guarantee.md)
- [Catena Type-System Design](../10-maps/catena-type-system-design.md)
