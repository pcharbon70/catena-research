---
title: "Unicode Standard Annex #29: Unicode Text Segmentation"
kind: source
created: "2026-09-09"
authors: ["Josh Hadley"]
published: 2025
citation_key: "hadley-2025-unicode-text-segmentation"
container: "The Unicode Standard, Version 17.0.0"
edition: "Revision 47"
isbn: null
doi: null
url: "https://www.unicode.org/reports/tr29/tr29-47.html"
accessed: "2026-09-09"
tags: [unicode, conformance]
aliases: []
---

# Unicode Standard Annex #29: Unicode Text Segmentation

## Reference

Josh Hadley, editor. “Unicode Text Segmentation.” UAX #29, revision 47,
Unicode 17.0.0, August 17, 2025.
[Canonical publication](https://www.unicode.org/reports/tr29/tr29-47.html).

## Findings

The annex distinguishes default extended grapheme boundaries from legacy and
tailored profiles. Its ordered rules use grapheme, Indic-conjunct and emoji
properties; default rules can operate on original text without first normalizing
it. Boundary rules account for context, so adjacent scalar or fragment counts do
not determine grapheme count.

## Relevance and limits

C104 selects default extended segmentation and pins the associated data. The
annex does not define Catena index types, slice failures, memory costs or public
syntax. Grapheme clusters approximate user-perceived text elements; they are not
a universal measure of display width or locale-sensitive editing behavior.

## Derived work

- [Text and Binary Model](../60-specification/text-binary-model/README.md) — the
  selected language contract.
- [Implementation journal](../50-journal/2026-09-09-text-binary-model.md) — local
  algorithm, official vectors and compiled evidence, distinct from source claims.
