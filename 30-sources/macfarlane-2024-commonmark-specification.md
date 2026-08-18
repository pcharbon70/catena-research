---
title: "CommonMark Specification 0.31.2"
kind: source
created: "2026-08-18"
authors:
  - "John MacFarlane"
published: "2024-01-28"
citation_key: "macfarlane2024CommonMark"
container: "CommonMark"
edition: "0.31.2"
isbn: null
doi: null
url: "https://spec.commonmark.org/0.31.2/"
accessed: "2026-08-18"
tags:
  - commonmark
  - documentation
  - language-design
  - markdown
aliases:
  - "CommonMark 0.31.2"
---

# CommonMark Specification 0.31.2

## Reference

John MacFarlane, *CommonMark Specification*, version 0.31.2, 2024-01-28.
[Official specification](https://spec.commonmark.org/0.31.2/).

## Contribution

CommonMark 0.31.2 supplies a versioned, testable Markdown grammar rather than
an unversioned promise to accept “Markdown.”

## Findings

- The specification fixes block and inline parsing, including fenced code
  blocks, info strings, HTML blocks, and inline raw HTML.
- Fenced-code contents are literal text. CommonMark notes that the first info-
  string word is often used as a language label but does not itself prescribe
  execution behavior.
- HTML-looking blocks and inline tags can remain raw HTML in HTML output.
- The official version index identifies 0.31.2, dated 2024-01-28, as the
  current published version consulted for this work.

## Relevance

Pinning `commonmark-0.31.2` gives documentation tools an interoperable parsing
contract. Because raw HTML can survive parsing, Catena separately requires
renderers never to execute it unsanitized. Because CommonMark does not define
code execution, Catena can reserve one exact trimmed info string, `catena
doctest`, without changing ordinary fenced-block meaning.

## Limits

CommonMark defines parsing and representative HTML output, not trusted HTML
sanitization, Catena symbol linking, declaration attachment, code evaluation,
or doctest isolation. Those remain explicit Catena and tooling obligations.

## Derived work

- [Catena Comments and Documentation Comments](../20-notes/catena-comments-and-documentation-comments.md)
- [Resolved comments inquiry](../40-inquiries/how-should-catena-handle-comments-and-documentation-comments.md)
- [Comments and Documentation Comments map](../10-maps/comments-and-documentation-comments.md)
