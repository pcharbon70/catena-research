---
title: "The Principal Type-Scheme of an Object in Combinatory Logic"
kind: source
created: "2026-07-31"
authors:
  - "Roger Hindley"
published: 1969
citation_key: "hindley1969PrincipalTypeScheme"
container: "Transactions of the American Mathematical Society 146: 29–60"
edition: null
isbn: null
doi: "10.1090/S0002-9947-1969-0253905-6"
url: "https://www.ams.org/journals/tran/1969-146-00/S0002-9947-1969-0253905-6/S0002-9947-1969-0253905-6.pdf"
accessed: "2026-07-31"
tags:
  - hindley-milner
  - principal-types
  - type-inference
aliases:
  - "Hindley 1969"
---

# The Principal Type-Scheme of an Object in Combinatory Logic

## Reference

Roger Hindley, “The Principal Type-Scheme of an Object in Combinatory Logic,”
*Transactions of the American Mathematical Society* 146 (December 1969),
29–60. [DOI and publisher PDF](https://doi.org/10.1090/S0002-9947-1969-0253905-6).

## Research question

Given a combinatory-logic object, can one decide whether it has a type scheme
and, when it does, calculate a single scheme from which all its other typings
follow by substitution?

## Method

Hindley develops a formal assignment system for combinatory logic. He defines
substitution between type schemes, principal deductions, and algorithms for
combining the typings of subobjects. Robinson-style unification supplies the
most-general substitutions needed when two type shapes must agree.

## Findings

- Typable combinatory objects have principal type schemes: one most-general
  scheme represents the entire family of their valid types.
- Principal is an ordering claim, not merely a convenient display choice. Any
  other valid typing is an instance of the principal scheme under a
  substitution.
- Self-application remains expressible syntactically but is not thereby
  typable. Typability is decided by whether the generated type equations have
  a finite solution.
- The paper establishes the principal-type result in combinatory logic. It
  does not present ML's `let`-polymorphic language or Milner's Algorithm W.

## Relevance

This is the historical and mathematical foundation for the “principal” in
Hindley–Milner. It tells Catena what a strong inference contract would mean:
when inference succeeds, the result should be maximally reusable, and every
more-specific valid type should be obtainable by instantiation.

## Limits

The object language is combinatory logic rather than the lambda calculus with
`let`, algebraic data, traits, kinds, or effects. The result therefore supports
the principal-type idea but does not by itself justify Catena's extensions.

## Derived work

- [Hindley–Milner type inference](../20-notes/hindley-milner-type-inference.md)
- [How should Catena preserve principal inference while extending HM?](../40-inquiries/how-should-catena-preserve-principal-inference.md)
- [Hindley–Milner type inference map](../10-maps/hindley-milner-type-inference.md)
