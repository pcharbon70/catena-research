---
title: "Python 3.14 Lexical Analysis"
kind: source
created: "2026-08-17"
authors:
  - "Python Software Foundation"
published: "3.14.7"
citation_key: "pythonSoftwareFoundation2026LexicalAnalysis"
container: "Python Language Reference"
edition: "3.14"
isbn: null
doi: null
url: "https://docs.python.org/3.14/reference/lexical_analysis.html"
accessed: "2026-08-17"
tags:
  - language-design
  - layout
  - python
  - syntax
  - whitespace
aliases:
  - "Python lexical reference"
---

# Python 3.14 Lexical Analysis

## Reference

Python Software Foundation, “Lexical Analysis,” *Python Language Reference*,
Python 3.14.7, accessed 2026-08-17.
[Official reference](https://docs.python.org/3.14/reference/lexical_analysis.html).

## Research question

What exact machinery follows from making indentation semantic, and how does
Python distinguish physical lines, logical lines, blank lines, and implicit
continuation?

## Method

The official lexical chapter was read through its line-structure,
continuation, indentation, whitespace-between-token, and token sections. The
comparison uses specified language behavior, not CPython implementation code.

## Findings

- Physical line endings are normalized before tokenization, and EOF also ends
  the last physical line.
- Logical lines arise after explicit backslash and implicit delimiter-based
  joining. Implicitly joined lines produce no `NEWLINE` token and ignore their
  indentation.
- Semantic indentation expands tabs to eight-column stops, checks
  inconsistent tab/space mixtures, and produces `INDENT` and `DEDENT` tokens
  from a strictly increasing stack.
- Blank logical lines do not produce `NEWLINE` tokens in file input.
- Outside indentation and literals, space, tab, and form feed can separate
  tokens when concatenation would otherwise form a different token.
- The parser remains involved in some apparent indentation failures; the
  lexical stack alone does not decide every malformed suite.

## Relevance

Python supplies a clear counterfactual for Catena. If Catena made indentation
semantic, it would need to specify column measurement, tabs, mixed
indentation, stack transitions, blank lines, continuation, and EOF closure.
Rejecting semantic indentation lets G015 avoid those obligations while still
borrowing the useful physical/logical-line distinction.

## Limits

Python has statement suites, explicit backslash joining, form-feed behavior,
and an interactive mode that Catena has not selected. Its newline normalization
also accepts lone CR, unlike C013. Those rules are evidence about design cost,
not defaults for Catena.

## Derived work

- [Catena Whitespace, Layout, and Line Continuation](../20-notes/catena-whitespace-layout-and-line-continuation.md)
- [Resolved layout inquiry](../40-inquiries/how-should-catena-treat-whitespace-and-line-breaks.md)
- [Whitespace, Layout, and Line Continuation map](../10-maps/whitespace-layout-and-line-continuation.md)
