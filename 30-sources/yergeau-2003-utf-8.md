---
title: "RFC 3629: UTF-8, a Transformation Format of ISO 10646"
kind: source
created: "2026-08-17"
authors:
  - "François Yergeau"
published: 2003
citation_key: "yergeau-2003-rfc-3629"
container: "Internet Standard STD 63"
edition: null
isbn: null
doi: "10.17487/RFC3629"
url: "https://www.rfc-editor.org/rfc/rfc3629"
accessed: "2026-08-17"
tags:
  - conformance
  - unicode
  - utf-8
aliases:
  - "RFC 3629"
---

# RFC 3629: UTF-8, a Transformation Format of ISO 10646

## Reference

François Yergeau. “UTF-8, a Transformation Format of ISO 10646.” RFC 3629,
STD 63, November 2003. DOI
[10.17487/RFC3629](https://doi.org/10.17487/RFC3629).

## Contribution

RFC 3629 defines the Internet UTF-8 format, gives an implementable byte
grammar, discusses invalid-sequence security consequences, and analyzes the
special role of a leading U+FEFF byte-order signature.

## Findings

- A Unicode character has one valid UTF-8 encoding of one through four bytes;
  the ranges exclude C0, C1, and F5 through FF as leading bytes.
- Decoders must defend against invalid sequences such as overlong NUL and
  UTF-8-like encodings of surrogate pairs because accepting them can create
  security and interpretation inconsistencies.
- UTF-8 uses one-byte encoding units, so a BOM does not communicate byte
  order. Its encoded signature is always `EF BB BF`.
- The RFC recommends forbidding the U+FEFF signature in protocols that already
  mandate UTF-8 because the signature function is unnecessary there.
- U+FEFF away from the beginning is a character in the stream, not a signature
  to strip during concatenation or parsing.

## Relevance

The source supports Catena's UTF-8-only and leading-BOM rejection decisions,
as well as the distinction between a prohibited leading signature and an
embedded U+FEFF scalar preserved for later lexical classification.

## Limits

RFC 3629 is an encoding protocol rather than a programming-language lexical
specification. It does not choose Catena's newline set, normalization policy,
source-coordinate units, or diagnostic identities. The Unicode Standard
remains the authoritative source for current encoding-form definitions.

## Derived work

- [Catena Source-Text Encoding and Normalization](../20-notes/catena-source-text-encoding-and-normalization.md)
- [Source Text Encoding and Normalization map](../10-maps/source-text-encoding-and-normalization.md)
- [Source-Text Envelope](../60-specification/source-text/source-text-envelope.md)
