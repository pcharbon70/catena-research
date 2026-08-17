---
title: "Unicode Standard Annex #15: Unicode Normalization Forms"
kind: source
created: "2026-08-17"
authors:
  - "Ken Whistler"
published: 2025
citation_key: "whistler-2025-unicode-normalization-forms"
container: "The Unicode Standard, Version 17.0.0"
edition: "Revision 57"
isbn: null
doi: null
url: "https://www.unicode.org/reports/tr15/tr15-57.html"
accessed: "2026-08-17"
tags:
  - unicode
  - unicode-normalization
aliases:
  - "UAX #15 Revision 57"
---

# Unicode Standard Annex #15: Unicode Normalization Forms

## Reference

Ken Whistler, editor. “Unicode Normalization Forms.” Unicode Standard Annex
#15, Revision 57, for Unicode 17.0.0, July 30, 2025.
[Canonical version](https://www.unicode.org/reports/tr15/tr15-57.html).

## Contribution

UAX #15 explains canonical and compatibility equivalence and the NFC, NFD,
NFKC, and NFKD transformation forms. It records how normalization decomposes,
reorders, and sometimes recomposes scalar sequences and discusses stability
across Unicode versions.

## Findings

- NFC and NFD preserve compatibility distinctions while selecting canonical
  representations; NFKC and NFKD additionally erase compatibility
  distinctions.
- Every normalization form can reorder combining marks. Composite forms can
  replace decomposed sequences with precomposed scalars, while decomposition
  forms can do the reverse.
- Compatibility normalization is unsafe as a blind arbitrary-text transform
  because it can remove distinctions important to content semantics.
- Normalized forms have strong stability guarantees, but applying a
  transformation still changes byte and scalar positions in the input.
- Identifier normalization is a narrower domain than normalization of an
  entire source file containing comments, literals, punctuation, and other
  text classes.

## Relevance

This evidence supports C013's decision not to normalize the whole decoded
source stream. Preserving source scalars avoids changing future literal or
comment content and keeps diagnostics mapped to written bytes. It leaves G014
free to select an identifier-specific equivalence policy using the more
appropriate identifier evidence.

## Limits

UAX #15 defines transformations and conformance tests but does not require a
programming language to normalize source files or identifiers. Confusable
detection, identifier repertoires, and security profiles belong to UAX #31 and
UTS #39 and remain G014 work rather than C013 evidence.

## Derived work

- [Catena Source-Text Encoding and Normalization](../20-notes/catena-source-text-encoding-and-normalization.md)
- [How Should Catena Decode and Normalize Source Text?](../40-inquiries/how-should-catena-decode-and-normalize-source-text.md)
- [Source-Text Envelope](../60-specification/source-text/source-text-envelope.md)
