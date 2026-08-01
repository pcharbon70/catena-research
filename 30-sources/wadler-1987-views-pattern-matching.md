---
title: "Views: A Way for Pattern Matching to Cohabit with Data Abstraction"
kind: source
created: "2026-07-31"
authors:
  - "Philip Wadler"
published: 1987
citation_key: "wadler1987Views"
container: "POPL '87: Proceedings of the 14th ACM SIGACT-SIGPLAN Symposium on Principles of Programming Languages, 307–313"
edition: null
isbn: "0-89791-215-2"
doi: "10.1145/41625.41653"
url: "https://dl.acm.org/doi/10.1145/41625.41653"
accessed: "2026-07-31"
tags:
  - algebraic-data-types
  - data-abstraction
  - pattern-matching
  - program-semantics
aliases:
  - "Wadler on views"
---

# Views: A Way for Pattern Matching to Cohabit with Data Abstraction

## Reference

Philip Wadler, “Views: A Way for Pattern Matching to Cohabit with Data
Abstraction,” in *POPL '87: Proceedings of the 14th ACM SIGACT-SIGPLAN
Symposium on Principles of Programming Languages* (ACM, 1987), 307–313.
[DOI and publisher record](https://doi.org/10.1145/41625.41653).

## Research question

Can a language preserve the notation and reasoning benefits of pattern
matching without forcing an abstract datatype to expose its concrete
constructor representation?

## Method

Wadler introduces a *view*: a programmer-defined conversion from an arbitrary
source representation to a freely constructed datatype whose constructors may
be used in patterns. Examples show multiple pattern interfaces over the same
representation and explain how view-based equations can be translated into
ordinary matching and function application.

## Findings

- Ordinary constructor patterns reveal the datatype's free representation.
  This gives concise case analysis but conflicts with representation hiding.
- A view separates the representation accepted by a function from the
  constructor vocabulary in which its cases are written.
- One representation may support several views, so an abstraction need not be
  limited to a single canonical decomposition.
- View-shaped cases can recover familiar structural induction and equational
  reasoning when the conversion has the expected semantic properties.
- Because matching now invokes a conversion rather than merely inspecting a
  constructor tag, the language must specify when conversion happens, whether
  it can fail, and what effects or costs it may have.

## Relevance

Catena should initially keep the rule simple: clients may pattern-match only
on constructors that the defining module exports. Smart constructors and
ordinary observations preserve invariants without extending pattern
semantics. If that proves too restrictive, total and pure views or pattern
synonyms are a plausible later feature—but only with explicit typing,
evaluation, coverage, trust, and cost rules.

## Limits

The proposal predates modern effect systems, GADTs, row-polymorphic variants,
separate-compilation coverage checking, and contemporary pattern-synonym
designs. A view declaration does not by itself prove that the conversion is
total, faithful, inexpensive, or compatible with abstraction invariants.

## Derived work

- [Algebraic Data Types](../20-notes/algebraic-data-types.md)
- [How Should Catena Specify Algebraic Data Types?](../40-inquiries/how-should-catena-specify-algebraic-data-types.md)
- [Algebraic Data Types map](../10-maps/algebraic-data-types.md)
