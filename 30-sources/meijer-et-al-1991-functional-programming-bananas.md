---
title: "Functional Programming with Bananas, Lenses, Envelopes and Barbed Wire"
kind: source
created: "2026-07-31"
authors:
  - "Erik Meijer"
  - "Maarten Fokkinga"
  - "Ross Paterson"
published: 1991
citation_key: "meijerEtAl1991Bananas"
container: "Functional Programming Languages and Computer Architecture, LNCS 523: 124–144"
edition: null
isbn: null
doi: "10.1007/3540543961_7"
url: "https://research.utwente.nl/en/publications/functional-programming-with-bananas-lenses-envelopes-and-barbed-w"
accessed: "2026-07-31"
tags:
  - algebraic-data-types
  - category-theory
  - program-calculation
  - recursion-schemes
aliases:
  - "Bananas lenses envelopes and barbed wire"
  - "Meijer Fokkinga and Paterson on recursion schemes"
---

# Functional Programming with Bananas, Lenses, Envelopes and Barbed Wire

## Reference

Erik Meijer, Maarten Fokkinga, and Ross Paterson, “Functional Programming with
Bananas, Lenses, Envelopes and Barbed Wire,” in *Functional Programming
Languages and Computer Architecture*, LNCS 523 (1991), 124–144.
[DOI](https://doi.org/10.1007/3540543961_7),
[author manuscript](https://ris.utwente.nl/ws/files/6142049/meijer91functional.pdf),
and [official bibliographic record](https://research.utwente.nl/en/publications/functional-programming-with-bananas-lenses-envelopes-and-barbed-w).

## Contribution

The paper develops a calculus for lazy functional programs from standard
recursion operators associated with datatype definitions. Catamorphisms fold
inductive data, anamorphisms unfold it, hylomorphisms compose the two, and
paramorphisms retain access to an original substructure while folding.

## Method

Recursive datatypes are modeled as fixed points of pattern functors. The
authors define recursion schemes, derive algebraic laws for them, and express
the example functions from Bird and Wadler's introductory text using the
operators. The evaluation is one of expressibility and equational
calculation, not usability or runtime benchmarking.

## Findings

- Datatype declarations determine canonical producers and consumers through
  their functorial shape.
- Universal properties provide uniqueness principles. A function satisfying
  a fold equation is the corresponding catamorphism, which makes fusion and
  other transformations calculable rather than ad hoc.
- Hylomorphisms expose intermediate recursive structures algebraically and
  create opportunities for deforestation-style reasoning.
- A small family of schemes expresses a broad introductory corpus, although
  the exact operator vocabulary and laws assume the paper's lazy setting and
  datatype restrictions.

## Relevance

This is the strongest case for letting Catena derive `map`, `fold`, `unfold`,
and `traverse`-like operations from suitable algebraic datatype declarations.
The declaration already supplies the shape; generated operators can package
the corresponding laws without demanding symbolic categorical notation from
ordinary users.

## Limits

Expressing textbook examples does not show that programmers prefer recursion
schemes, that diagnostics remain clear, or that generated programs are fast.
Fusion depends on purity, totality or strictness conditions that change across
evaluation strategies. Negative and nested occurrences also complicate the
simple fixed-point account.

## Derived work

- [Algebraic Data Types](../20-notes/algebraic-data-types.md)
- [How Should Catena Specify Algebraic Data Types?](../40-inquiries/how-should-catena-specify-algebraic-data-types.md)
- [Algebraic Data Types map](../10-maps/algebraic-data-types.md)
- [Category Theory for Programming](../20-notes/category-theory-for-programming.md)
- [How Should Catena Specify Its Initial Categorical Hierarchy?](../40-inquiries/how-should-catena-specify-its-initial-categorical-hierarchy.md)
- [Category Theory for Programming map](../10-maps/category-theory-for-programming.md)
