---
title: "EEP 70: Strict and Relaxed Generators"
kind: source
created: "2026-08-01"
authors:
  - "Dániel Szoboszlay"
published: 2024
citation_key: "szoboszlay2024Eep70StrictRelaxedGenerators"
container: "Erlang Enhancement Proposal 70"
edition: null
isbn: null
doi: null
url: "https://www.erlang.org/eeps/eep-0070"
accessed: "2026-08-01"
tags:
  - comprehensions
  - language-design
  - pattern-matching
aliases:
  - "Erlang strict generators"
---

# EEP 70: Strict and Relaxed Generators

## Reference

Dániel Szoboszlay, “EEP 70: Strict and Relaxed Generators,” standards-track
Erlang Enhancement Proposal, created 2024 and implemented in Erlang/OTP 28.
[Canonical EEP](https://www.erlang.org/eeps/eep-0070).

## Research question

How should a comprehension distinguish pattern matching that intentionally
filters elements from pattern matching that asserts the input shape?

## Method

The proposal compares the established relaxed generator with a new strict
form, evaluates alternative encodings, specifies failure behavior and syntax,
and links the reference implementation. Its `Final/28.0` status means the
design is deployed language behavior rather than an untested sketch.

## Findings

- Erlang's older generator silently skips every source element that fails the
  generator pattern. The proposal calls this form **relaxed**.
- The strict variants `<:-` for lists and maps and `<:=` for bit strings raise
  `badmatch` on a pattern mismatch. The source program therefore states whether
  a mismatch is selection or evidence of malformed input.
- The motivating example shows why the distinction matters: extracting fields
  from externally obtained user records can silently discard incomplete or
  corrupt records under relaxed semantics.
- Rewriting the strict intent with a mapping function, a match in the result
  expression, or an awkward Boolean filter either loses compactness, delays
  bindings, obscures intent, or fails to cover bit-string remainders.
- Bit-string generators expose a deeper issue than list traversal. The pattern
  determines segmentation, so unmatched final bits require an explicit
  consumption policy rather than ordinary element filtering.
- The proposal adds new syntax instead of changing the old operator, preserving
  compatibility at the cost of two nearly identical generator operators.

## Relevance

The EEP supplies direct production evidence that silent pattern filtering and
assertive matching are different operations. Catena can preserve that
distinction more readably by requiring an exhaustive pattern in an ordinary
generator and an explicit word such as `case` for a filtering generator,
rather than differentiating the behaviors by a punctuation character.

It also shows why a future binary comprehension cannot be obtained merely by
generalizing a list iterator: segmentation, incomplete input, and failure
location form an independent contract.

## Limits

Erlang is dynamically typed, so many strict mismatches that Catena can reject
as non-exhaustive generator patterns remain runtime events. The EEP evaluates
compatibility and expressiveness within Erlang; it does not compare the
learnability of symbolic strictness with keyword-based alternatives.

## Derived work

- [List Comprehensions](../20-notes/list-comprehensions.md)
- [How Should Catena Specify List Comprehensions?](../40-inquiries/how-should-catena-specify-list-comprehensions.md)
- [List Comprehensions map](../10-maps/list-comprehensions.md)
