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
  - bytes
  - language-design
  - layout
  - literals
  - python
  - text
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
Python combine line handling with numeric, string, byte, raw, and formatted
literal families?

## Method

The official lexical chapter was read through its line-structure,
continuation, indentation, whitespace-between-token, string/bytes, formatted
string, and numeric-literal sections. The comparison uses specified language
behavior, not CPython implementation code.

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
- String and byte literals use a family of prefixes and single-, double-, or
  triple-quoted delimiters. Raw prefixes change escape handling, while bytes
  and formatted strings define separate decoded domains.
- Formatted strings contain replacement fields and therefore need lexical and
  expression-processing rules beyond ordinary static text.
- Integer literals use binary, octal, decimal, and hexadecimal forms. Floats
  are decimal, and underscores can separate digits only at defined positions.
- Decimal integer spellings disallow redundant leading zeros, while based
  spellings and several literal families add distinct prefix and boundary
  cases.

## Relevance

Python supplies a clear counterfactual for Catena. If Catena made indentation
semantic, it would need to specify column measurement, tabs, mixed
indentation, stack transitions, blank lines, continuation, and EOF closure.
Rejecting semantic indentation lets G015 avoid those obligations while still
borrowing the useful physical/logical-line distinction. The literal sections
also provide a useful complexity comparison for C017: prefix combinations,
quote choices, raw processing, multiline content, bytes, and interpolation
multiply rather than merely add lexical cases.

## Limits

Python has statement suites, explicit backslash joining, form-feed behavior,
implicit adjacent string concatenation, multiple quote styles, and an
interactive mode that Catena has not selected. Its newline normalization also
accepts lone CR, unlike C013. Its prefix and literal rules are evidence about
design cost and separable concerns, not defaults for Catena.

## Derived work

- [Catena Whitespace, Layout, and Line Continuation](../20-notes/catena-whitespace-layout-and-line-continuation.md)
- [Resolved layout inquiry](../40-inquiries/how-should-catena-treat-whitespace-and-line-breaks.md)
- [Whitespace, Layout, and Line Continuation map](../10-maps/whitespace-layout-and-line-continuation.md)
- [Catena Literal Grammar](../20-notes/catena-literal-grammar.md)
- [Resolved literal inquiry](../40-inquiries/how-should-catena-spell-and-decode-literals.md)
- [Literal Grammar map](../10-maps/literal-grammar.md)
