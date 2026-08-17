---
title: "Unicode Technical Standard #55: Unicode Source Code Handling"
kind: source
created: "2026-08-17"
authors:
  - "Robin Leroy"
  - "Mark Davis"
published: 2024
citation_key: "leroy-davis-2024-unicode-source-code-handling"
container: "Unicode Technical Standard #55"
edition: "Version 2, Revision 5"
isbn: null
doi: null
url: "https://www.unicode.org/reports/tr55/tr55-5.html"
accessed: "2026-08-17"
tags:
  - identifiers
  - security
  - tooling
  - unicode
aliases:
  - "UTS #55 Revision 5"
---

# Unicode Technical Standard #55: Unicode Source Code Handling

## Reference

Robin Leroy and Mark Davis, “Unicode Source Code Handling,” Unicode Technical
Standard #55, Version 2, Revision 5, 29 January 2024.
[Official publication](https://www.unicode.org/reports/tr55/tr55-5.html).

## Contribution

UTS #55 applies Unicode identifier and security mechanisms specifically to
programming languages, editors, review tools, and compiler diagnostics. It
distinguishes language equality from visual-review risks and recommends
addressing spoofing at multiple ecosystem layers.

## Findings

- Case-sensitive languages are directed toward NFC and should not make case
  the only way to express a semantic distinction because many writing systems
  are uncased.
- Equivalent-normalized identifiers under UAX31-R4 are recommended for input
  usability. UAX31-R6 filtered normalization remains a defined alternative,
  but some input methods can produce decomposed text and therefore require a
  clear repair path.
- Confusability and mixed-script risks are usually better surfaced by compiler
  warnings, linters, editors, and review tools than by treating every visual
  collision as malformed syntax.
- Token-aware bidirectional display and visible treatment of hidden characters
  remain necessary even when identifier repertoires are restricted.

## Relevance

Catena follows the recommendation not to encode namespace role in case and
uses deny-able confusable warnings. It deliberately chooses filtered NFC for
the initial standalone boundary so source spelling, identity, diagnostics, and
artifact names cannot diverge; the required machine-applicable replacement is
the mitigation for decomposed input.

## Limits

The document is guidance for an ecosystem broader than a compiler. C014 does
not claim token-aware display, editor rendering, formatter behavior, complete
bidirectional source handling, or scope-aware linting. Those require the later
lexer, parser, namespace, diagnostics, and tooling gaps.

## Derived work

- [Resolved identifier inquiry](../40-inquiries/how-should-catena-define-and-secure-identifiers.md)
- [Catena Identifiers and Name Security](../20-notes/catena-identifiers-and-name-security.md)
- [C014 evidence record](../50-journal/2026-08-17-c014-identifiers-and-name-security.md)
