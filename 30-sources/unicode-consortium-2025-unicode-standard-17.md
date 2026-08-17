---
title: "The Unicode Standard, Version 17.0: Conformance and Encoding Forms"
kind: source
created: "2026-08-17"
authors:
  - "The Unicode Consortium"
published: 2025
citation_key: "unicode-consortium-2025-unicode-standard-17"
container: "The Unicode Standard"
edition: "Version 17.0.0"
isbn: "978-1-936213-35-1"
doi: null
url: "https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-3/"
accessed: "2026-08-17"
tags:
  - conformance
  - unicode
  - utf-8
aliases:
  - "Unicode 17 Chapter 3"
---

# The Unicode Standard, Version 17.0: Conformance and Encoding Forms

## Reference

The Unicode Consortium. *The Unicode Standard, Version 17.0.0*, Chapter 3,
“Conformance,” especially section 3.9, “Unicode Encoding Forms.” South San
Francisco: The Unicode Consortium, 2025. ISBN 978-1-936213-35-1.
[Canonical chapter](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-3/).

## Contribution

Chapter 3 defines Unicode scalar values, well- and ill-formed code-unit
sequences, and the exact UTF-8 encoding form. Definitions D84 through D92 and
table 3-7 provide a direct conformance boundary for deciding which source byte
sequences can be interpreted as Unicode scalars.

## Findings

- UTF-8 maps every Unicode scalar value to one unique sequence of one through
  four bytes.
- The well-formed sequence table excludes overlong spellings, surrogate code
  points, values beyond U+10FFFF, and invalid leading or continuation ranges.
- A verifying process cannot identify an ill-formed sequence as UTF-8, and an
  interpreting process cannot treat ill-formed subsequences as characters.
- Noncharacters and unassigned code points are still Unicode scalar values and
  therefore have unique valid encodings. Assignment and suitability for a
  particular token class are separate from encoding well-formedness.
- Error recovery that continues past malformed bytes must not absorb adjacent
  well-formed sequences into the malformed subsequence. A decoder that stops
  at the first error avoids inventing replacement semantics.

## Relevance

This chapter supplies C013's exact meaning of strict UTF-8 and supports
accepting every scalar at the encoding envelope before later identifier,
whitespace, comment, and literal rules narrow their own repertoires. It also
supports calculating a diagnostic from the accepted prefix without decoding
the offending bytes as characters.

## Limits

The Unicode Standard defines encoding conformance, not Catena's BOM policy,
newline set, source columns, token grammar, or normalization boundary. Those
are protocol and language-design decisions that C013 must state separately.

## Derived work

- [Catena Source-Text Encoding and Normalization](../20-notes/catena-source-text-encoding-and-normalization.md)
- [How Should Catena Decode and Normalize Source Text?](../40-inquiries/how-should-catena-decode-and-normalize-source-text.md)
- [Source-Text Envelope](../60-specification/source-text/source-text-envelope.md)
