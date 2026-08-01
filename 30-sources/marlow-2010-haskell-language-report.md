---
title: "Haskell 2010 Language Report"
kind: source
created: "2026-08-01"
authors:
  - "Simon Marlow (editor)"
published: 2010
citation_key: "marlow2010Haskell2010"
container: null
edition: "Haskell 2010"
isbn: null
doi: null
url: "https://www.haskell.org/definition/haskell2010.pdf"
accessed: "2026-08-01"
tags:
  - language-design
  - pattern-matching
aliases:
  - "Haskell 2010 Report"
---

# Haskell 2010 Language Report

## Reference

Simon Marlow, ed., *Haskell 2010 Language Report* (2010).
[Official report](https://www.haskell.org/definition/haskell2010.pdf).

## Research question

How can Boolean conditions, refutable matches, and local bindings be composed
as ordered guards with a kernel translation?

## Method

The report is the language definition. Sections 3.13 and 3.17 give syntax,
informal behavior, and translation rules for case alternatives and pattern
matching.

## Findings

- A guarded case alternative may contain a sequence of Boolean guards,
  pattern guards, and local declarations.
- Guards in a sequence are evaluated in order. A false Boolean guard or failed
  pattern guard falls through; bindings from successful earlier steps are
  available to later steps and the body.
- The report reduces guarded alternatives to nested case and conditional
  expressions. This gives guards a kernel meaning rather than making them a
  special backend facility.
- The translation preserves source alternative order and ultimately raises a
  no-match error if every alternative fails.
- Guard evaluation affects strictness. A structurally irrefutable pattern may
  still force values when its guard evaluates them.

## Relevance

The report demonstrates a compositional path from a rich guard surface to a
small core. It also makes clear that pattern guards are more than Boolean
filters: they run expressions, perform additional refutable matches, introduce
bindings, and affect evaluation. Catena can therefore stage Boolean clause
conditions separately from pattern guards instead of treating the richer form
as harmless syntax sugar.

## Limits

Haskell is non-strict and pure, while Catena is proposed to be strict with
explicit effect rows. Haskell's bottom and strictness considerations therefore
do not map directly to Catena's proposed total guard fragment. The report also
defines the language, not the precision or performance of a modern coverage
checker.

## Derived work

- [Clause Guards](../20-notes/clause-guards.md)
- [How Should Catena Design Clause Guards?](../40-inquiries/how-should-catena-design-clause-guards.md)
- [Clause Guards map](../10-maps/clause-guards.md)
