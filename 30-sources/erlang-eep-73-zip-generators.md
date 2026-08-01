---
title: "EEP 73: Zip Generator"
kind: source
created: "2026-08-01"
authors:
  - "Isabell Huang"
published: 2024
citation_key: "huang2024Eep73ZipGenerator"
container: "Erlang Enhancement Proposal 73"
edition: null
isbn: null
doi: null
url: "https://www.erlang.org/eeps/eep-0073"
accessed: "2026-08-01"
tags:
  - comprehensions
  - language-design
  - streams
aliases:
  - "Erlang zip generators"
---

# EEP 73: Zip Generator

## Reference

Isabell Huang, “EEP 73: Zip Generator,” standards-track Erlang Enhancement
Proposal, created 2024 and implemented in Erlang/OTP 28.
[Canonical EEP](https://www.erlang.org/eeps/eep-0073).

## Research question

What semantic and diagnostic obligations appear when multiple comprehension
generators advance in lockstep instead of nesting?

## Method

The proposal derives zip generators from existing Erlang comprehension forms,
specifies their syntax, precedence, pattern behavior, and errors, compares them
with `lists:zip`, and links a compiler implementation.

## Findings

- Adjacent ordinary generators are dependent and nested, producing a Cartesian
  product. A zip generator connects two or more generators with `&&` and
  advances them as one unit.
- Zipped generators may draw from lists, bit strings, or maps and can be mixed
  with ordinary generators and filters. This makes syntax precedence part of
  the semantic contract.
- The construct avoids allocating the intermediate tuples that an explicit
  `lists:zip` followed by a comprehension would create. The compiler retains
  source intent in its generated form.
- Unequal generator lengths raise a `bad generators` error rather than
  truncating to the shortest input. This is a substantive policy, not an
  inevitable meaning of `zip`.
- Relaxed pattern failures skip one position from every zipped input. Strict
  pattern failures and unequal lengths share a composite error that exposes
  the remaining inputs.
- Every strict pattern is attempted in each zip round even if a relaxed peer
  has already failed. Evaluation multiplicity and error priority therefore
  require explicit rules.
- Filters cannot appear inside the zipped generator group; the compiler reports
  this structural error.

## Relevance

The EEP demonstrates that “two generators” is ambiguous between nested and
lockstep traversal. Catena already has reason to distinguish `zip_exact` and
`zip_shortest`; an initial list comprehension should use ordinary nested
generators and leave zip policy in explicitly named library operations. If
lockstep syntax is later added, it must state length mismatch, pattern failure,
evaluation order, and error precedence together.

## Limits

The proposal targets Erlang's dynamic patterns and three existing
comprehension result forms. Its compiler-allocation argument is relevant to
BEAM lowering, but it does not establish that dedicated zip syntax is more
approachable than calling a clearly named zip function.

## Derived work

- [List Comprehensions](../20-notes/list-comprehensions.md)
- [How Should Catena Specify List Comprehensions?](../40-inquiries/how-should-catena-specify-list-comprehensions.md)
- [List Comprehensions map](../10-maps/list-comprehensions.md)
