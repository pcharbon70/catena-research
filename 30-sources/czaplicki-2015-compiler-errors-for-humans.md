---
title: "Compiler Errors for Humans"
kind: source
created: "2026-08-01"
authors:
  - "Evan Czaplicki"
published: "2015-06-30"
citation_key: "czaplicki2015CompilerErrorsForHumans"
container: "Elm News"
edition: null
isbn: null
doi: null
url: "https://elm-lang.org/news/compiler-errors-for-humans"
accessed: "2026-08-01"
tags:
  - compilers
  - diagnostics
  - language-design
  - usability
aliases:
  - "Elm compiler errors for humans"
---

# Compiler Errors for Humans

## Reference

Evan Czaplicki, “Compiler Errors for Humans,” *Elm News*, June 30,
2015. [Official article](https://elm-lang.org/news/compiler-errors-for-humans).

## Contribution

The article documents an Elm compiler redesign that treats terminal error
messages as a user-experience surface. It argues that precise types only help
when the compiler connects an internal failure to the programmer's source and
likely intent.

## Method

Czaplicki presents before-and-after diagnostic examples from Elm 0.15.1 and
describes the design reasoning behind source display, location, color,
context-specific hints, and layout. The work also introduces an error-message
catalog: a collection of small programs that intentionally trigger messages
so compiler output can be reviewed and improved systematically.

This is a project design report, not a controlled user study.

## Findings

- Showing the exact source expression reduces the translation from line and
  column coordinates or compiler-pretty-printed terms back to user code.
- A useful headline and local source highlight establish the problem before
  technical details are introduced.
- Context-specific hints connect a type mismatch to the role of an argument,
  field, branch, or surrounding expression rather than reporting only that two
  internal types failed to unify.
- Layout can reveal detail progressively: short context first, precise source
  next, and deeper explanation afterward.
- A diagnostic corpus makes wording and recovery behavior testable across
  compiler changes instead of relying only on anecdotes from memorable errors.

## Relevance

Catena's accessibility goal depends as much on diagnostics as naming. Every
generic capability, ADT derivation, effect requirement, and inference boundary
needs failing examples in a diagnostic corpus. Errors should preserve source
operations such as `map`, `and_then`, `collect_map`, `handle`, and `match`
instead of exposing elaborated evidence terms or solver vocabulary.

The catalog approach also supplies a practical design test before full guides
exist: each proposed capability name can be exercised through successful and
failed programs, with expected explanations stored beside the compiler.

## Limits

The article reports the reasoning and examples of one language author for an
older Elm release. It does not isolate which message feature improves repair
time or comprehension, compare mathematical and behavioral vocabulary, or
establish that the same presentation works for higher-kinded constraints,
effect rows, resumptions, or BEAM process errors.

## Derived work

- [An Approachable Vocabulary for Catena](../20-notes/approachable-language-vocabulary.md)
- [How Should Catena Expose Mathematical Structure Without Mathematical Jargon?](../40-inquiries/how-should-catena-expose-mathematical-structure-without-mathematical-jargon.md)
- [Approachable Catena Language Design map](../10-maps/approachable-catena-language-design.md)
