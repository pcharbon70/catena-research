---
title: "Profunctor Optics: Modular Data Accessors"
kind: source
created: "2026-07-31"
authors:
  - "Matthew Pickering"
  - "Jeremy Gibbons"
  - "Nicolas Wu"
published: 2017
citation_key: "pickeringEtAl2017ProfunctorOptics"
container: "The Art, Science, and Engineering of Programming 1(2), Article 7"
edition: null
isbn: null
doi: "10.22152/programming-journal.org/2017/1/7"
url: "https://programming-journal.org/2017/1/7/"
accessed: "2026-07-31"
tags:
  - category-theory
  - optics
  - profunctors
  - program-structure
aliases:
  - "Pickering Gibbons and Wu on profunctor optics"
---

# Profunctor Optics: Modular Data Accessors

## Reference

Matthew Pickering, Jeremy Gibbons, and Nicolas Wu, “Profunctor Optics: Modular
Data Accessors,” *The Art, Science, and Engineering of Programming* 1, no. 2,
Article 7 (2017).
[DOI and journal record](https://doi.org/10.22152/programming-journal.org/2017/1/7),
[open repository record](https://ora.ox.ac.uk/objects/uuid%3A9989be57-a045-4504-b9d7-dc93fd508365),
and [accompanying code](https://doi.org/10.5281/zenodo.400437).

## Research question

How can lenses, prisms, traversals, and related data accessors become
first-class values that compose uniformly even when the concrete accessor
representations differ?

## Method

The paper represents an optic as a polymorphic transformation over a profunctor
with capabilities determined by the optic kind. It implements the construction
as a literate Haskell program and proves representation results connecting the
profunctor encodings to familiar concrete accessors. A Scala presentation
illustrates that the approach depends on general language features rather than
one Haskell primitive.

## Findings

- Profunctors generalize functions contravariantly in their input and
  covariantly in their output.
- Lenses, prisms, and traversals can share ordinary function composition while
  requiring different structural capabilities—products, sums, and monoidal
  traversal—from the profunctor.
- The representation exposes a lattice of optic strength and permits mixed
  composition that concrete getter/setter pairs do not support directly.
- Higher-order functions, higher-kinded parameterization, and interface or
  module abstraction are the important implementation requirements.

## Relevance

Optics are a compelling library-level application of categorical design:
composition solves a concrete nested-data problem. For Catena, generated field
and variant accessors could provide the accessible surface, with a profunctor
encoding considered later if higher-rank and higher-kinded abstraction are
coherent and diagnostics remain usable.

## Limits

The paper proves representational properties and supplies executable code; it
does not compare learning cost, compiler errors, runtime specialization, or
API discoverability across languages. Lawful optics still require semantic
laws that their type-class constraints do not by themselves enforce.

## Derived work

- [Category Theory for Programming](../20-notes/category-theory-for-programming.md)
- [Which Categorical Abstractions Should Catena Expose?](../40-inquiries/which-categorical-abstractions-should-catena-expose.md)
- [Category Theory for Programming map](../10-maps/category-theory-for-programming.md)
