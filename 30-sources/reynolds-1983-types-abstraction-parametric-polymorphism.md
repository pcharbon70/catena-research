---
title: "Types, Abstraction and Parametric Polymorphism"
kind: source
created: "2026-07-31"
authors:
  - "John C. Reynolds"
published: 1983
citation_key: "reynolds1983TypesAbstraction"
container: "Information Processing 83: 513–523"
edition: null
isbn: "0-444-86729-5"
doi: null
url: "https://www.cs.cmu.edu/afs/cs/user/crary/www/819-f09/Reynolds83.pdf"
accessed: "2026-07-31"
tags:
  - abstraction
  - parametricity
  - polymorphism
  - type-systems
aliases:
  - "Reynolds on relational parametricity"
---

# Types, Abstraction and Parametric Polymorphism

## Reference

John C. Reynolds, “Types, Abstraction and Parametric Polymorphism,” in
*Information Processing 83*, edited by R. E. A. Mason (North-Holland, 1983),
513–523. [Archived paper](https://www.cs.cmu.edu/afs/cs/user/crary/www/819-f09/Reynolds83.pdf)
and [bibliographic listing](https://dblp.org/rec/conf/ifip/Reynolds83.html).

## Research question

How can a semantic account distinguish genuinely parametric polymorphism from
code that selects behavior using the representation of a type argument, and
what abstraction principle follows for polymorphic programs?

## Method

Reynolds interprets types relationally as well as extensionally. A polymorphic
term must preserve relations chosen between its type instantiations. The paper
states the resulting abstraction theorem and uses it to explain representation
independence and uniform behavior.

## Findings

- Parametric polymorphism is a uniformity condition, not merely syntax that
  permits one term to be instantiated at many types.
- A polymorphic function maps related inputs to related outputs. Relations can
  encode two implementations of an abstract representation, yielding a proof
  principle for representation independence.
- Uniformity sharply restricts inhabitants of highly polymorphic types. This
  is the semantic basis for later “free theorem” reasoning and for many
  naturality laws used in categorical programming.
- Ad-hoc type analysis is incompatible with the unconstrained relational
  interpretation. Runtime type inspection, unsafe coercion, or operations that
  distinguish representations therefore narrow the theorem.

## Relevance

Functor and natural-transformation laws in programming are often trusted
because polymorphic implementations cannot inspect their type arguments. This
paper supplies the missing premise. Catena should not claim that a generic
signature alone proves those laws unless its semantics establishes the needed
parametricity result for that fragment.

It also gives law testing a clear role: tests can catch mistakes in ad-hoc
instances, while a parametricity theorem can rule out broader classes of
implementations. These are different strengths of evidence.

## Limits

The original model is for a strongly normalizing polymorphic calculus, not a
full language with general recursion, exceptions, mutable state, typecase,
foreign calls, or nontermination. Transferring its conclusions to Catena
requires a language-specific logical relation and explicit treatment of every
feature that can observe or disrupt relations.

## Derived work

- [Algebraic Data Types](../20-notes/algebraic-data-types.md)
- [How Should Catena Specify Algebraic Data Types?](../40-inquiries/how-should-catena-specify-algebraic-data-types.md)
- [Algebraic Data Types map](../10-maps/algebraic-data-types.md)
- [Category Theory for Programming](../20-notes/category-theory-for-programming.md)
- [How Should Catena Specify Its Initial Categorical Hierarchy?](../40-inquiries/how-should-catena-specify-its-initial-categorical-hierarchy.md)
- [Category Theory for Programming map](../10-maps/category-theory-for-programming.md)
