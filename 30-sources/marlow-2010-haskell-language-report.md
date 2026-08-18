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
  - comprehensions
  - language-design
  - layout
  - pattern-matching
  - syntax
  - whitespace
aliases:
  - "Haskell 2010 Report"
---

# Haskell 2010 Language Report

## Reference

Simon Marlow, ed., *Haskell 2010 Language Report* (2010).
[Official report](https://www.haskell.org/definition/haskell2010.pdf).

## Research question

How does Haskell give layout, ordered clause guards, and list comprehensions
precise translations, and what do those translations imply for lexical and
semantic structure?

## Method

The report is the language definition. Sections 2.7 and 10.3 specify layout;
Sections 3.11, 3.13, and 3.17 give syntax, informal behavior, and translation
rules for list comprehensions, case alternatives, and pattern matching.

## Findings

### Layout

- Layout-sensitive contexts begin after selected keywords when an explicit
  opening brace is absent. The next lexeme's indentation establishes the
  context column.
- Equal indentation inserts a semicolon, lesser indentation closes one or more
  implicit contexts, and greater indentation continues the current item.
- Explicit braces push a distinct zero context in which the surrounding
  implicit layout rule is suspended.
- The specification fixes one-based columns, eight-column tab stops, and a
  one-column width for every Unicode character. It warns against programs whose
  meaning depends on non-space display width.
- A parser-prefix test can trigger an implicit closing brace when the next
  token would otherwise make the prefix invalid. Layout therefore is not a
  purely local whitespace rewrite.
- EOF closes remaining implicit contexts but is an error in an unclosed
  explicit context.

### Clause guards

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

### List comprehensions

- A list comprehension contains a result expression followed by one or more
  qualifiers. Qualifiers are list generators, local declarations, or arbitrary
  expressions of type `Bool`.
- Generators are evaluated as nested, depth-first traversals. Bindings from an
  earlier qualifier are visible in later qualifiers and the result.
- A generator pattern mismatch silently skips that source element. This makes
  pattern selection part of generator semantics rather than an ordinary match
  failure.
- A false Boolean qualifier contributes no result. Local declarations scope
  over the remaining qualifiers and result.
- The kernel translation maps a generator through a fresh pattern-matching
  function and `concatMap`, maps a false filter to the empty list, and nests a
  local declaration around the remaining comprehension.
- Generator bindings are lambda-bound and monomorphic, while local `let`
  declarations can be generalized. Surface similarity therefore does not make
  the two binders statically interchangeable.

## Relevance

The report demonstrates compositional paths from layout and rich expression
surfaces to explicit structure. Its offside translation is evidence that
semantic indentation requires column, tab, delimiter-stack, EOF, and parser
interaction rules; Catena avoids those costs by making indentation
non-semantic.

It also makes clear that clause guards, comprehension filters, generator
patterns, and local declarations have related syntax but different failure and
binding roles.

The list translation supplies an extensional model for Catena's pure
comprehensions. Catena should not inherit silent pattern filtering without an
explicit marker, and its strict effectful semantics require a more direct
operational account than Haskell's non-strict `concatMap` equation.

## Limits

Haskell is non-strict and pure, while Catena is proposed to be strict with
explicit effect rows. Haskell's bottom and strictness considerations therefore
do not map directly to Catena's proposed total guard fragment or its
left-to-right effect traces. The report defines extensional language behavior,
not stack safety, allocation, fusion constraints, or modern coverage-checker
precision.

## Derived work

- [Clause Guards](../20-notes/clause-guards.md)
- [How Should Catena Design Clause Guards?](../40-inquiries/how-should-catena-design-clause-guards.md)
- [Clause Guards map](../10-maps/clause-guards.md)
- [List Comprehensions](../20-notes/list-comprehensions.md)
- [How Should Catena Specify List Comprehensions?](../40-inquiries/how-should-catena-specify-list-comprehensions.md)
- [List Comprehensions map](../10-maps/list-comprehensions.md)
- [Catena Whitespace, Layout, and Line Continuation](../20-notes/catena-whitespace-layout-and-line-continuation.md)
- [Resolved layout inquiry](../40-inquiries/how-should-catena-treat-whitespace-and-line-breaks.md)
- [Whitespace, Layout, and Line Continuation map](../10-maps/whitespace-layout-and-line-continuation.md)
