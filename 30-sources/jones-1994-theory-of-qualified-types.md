---
title: "A Theory of Qualified Types"
kind: source
created: "2026-07-31"
authors:
  - "Mark P. Jones"
published: 1994
citation_key: "jones1994QualifiedTypes"
container: "Science of Computer Programming 22(3): 231–256"
edition: null
isbn: null
doi: "10.1016/0167-6423(94)00005-0"
url: "https://www.sciencedirect.com/science/article/pii/0167642394000050"
accessed: "2026-07-31"
tags:
  - principal-types
  - qualified-types
  - trait-constraints
  - type-inference
aliases:
  - "Jones qualified types"
---

# A Theory of Qualified Types

## Reference

Mark P. Jones, “A Theory of Qualified Types,” *Science of Computer
Programming* 22, no. 3 (1994), 231–256.
[DOI and journal record](https://doi.org/10.1016/0167-6423(94)00005-0).
The [author-hosted revised paper](https://web.cecs.pdx.edu/~mpj/pubs/rev-qual-types.pdf)
develops the formal system used in these notes.

## Contribution

Jones extends the Damas–Milner framework with qualified types of the form
`P => τ`, where `P` is a finite set of predicates. A predicate system supplies
an entailment relation; different interpretations recover type classes,
extensible records, or subtyping constraints.

## Method

The paper defines declarative and syntax-directed systems, an evidence
translation for overloaded operations, and an extension of Algorithm W that
synthesizes predicates alongside substitutions and types. It proves soundness,
completeness, and a principal-type theorem under stated properties of predicate
entailment.

## Findings

- Qualified types retain an HM-shaped inference algorithm: instantiate the
  type and predicates at variable use, accumulate predicates during traversal,
  substitute through them, and generalize `P => τ` at `let`.
- Predicate entailment must be monotone, transitive, and closed under type
  substitution for the generic development.
- A trait or type-class constraint needs runtime or compile-time *evidence*;
  for a class constraint, that evidence is naturally a dictionary of methods.
- Principal qualified types exist under the paper's assumptions, but a
  principal type can still be semantically ambiguous. The paper's coherence
  result requires unambiguous schemes, roughly ensuring that constrained
  variables are determined by the visible result type.
- Constraint simplification may reduce evidence parameters while preserving
  principality when replacement predicate sets are equivalent under
  entailment.

## Relevance

The paper makes clear that retaining predicates in schemes is only one part of
a trait design: entailment, satisfiability, evidence selection, ambiguity, and
coherence are all part of the semantic contract.

## Limits

The generic theory assumes suitable properties of the chosen predicate system.
It does not prove those properties for any concrete trait hierarchy or instance
database. Multi-parameter classes and improving substitutions require
additional design beyond the base presentation.

## Derived work

- [Hindley–Milner type inference](../20-notes/hindley-milner-type-inference.md)
- [A greenfield type system for Catena](../20-notes/catena-greenfield-type-system.md)
- [What should a greenfield Catena type system guarantee?](../40-inquiries/what-should-a-greenfield-catena-type-system-guarantee.md)
- [Catena type-system design map](../10-maps/catena-type-system-design.md)
