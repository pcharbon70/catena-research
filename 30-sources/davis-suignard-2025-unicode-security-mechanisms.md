---
title: "Unicode Technical Standard #39: Unicode Security Mechanisms"
kind: source
created: "2026-08-17"
authors:
  - "Mark Davis"
  - "Michel Suignard"
published: 2025
citation_key: "davis-suignard-2025-unicode-security-mechanisms"
container: "Unicode Technical Standard #39"
edition: "Revision 32, Unicode 17.0.0"
isbn: null
doi: null
url: "https://www.unicode.org/reports/tr39/tr39-32.html"
accessed: "2026-08-17"
tags:
  - identifiers
  - security
  - unicode
aliases:
  - "UTS #39 Revision 32"
---

# Unicode Technical Standard #39: Unicode Security Mechanisms

## Reference

Mark Davis and Michel Suignard, “Unicode Security Mechanisms,” Unicode
Technical Standard #39, Revision 32, Unicode 17.0.0, 4 September 2025.
[Official publication](https://www.unicode.org/reports/tr39/tr39-32.html).

## Contribution

UTS #39 publishes data and algorithms for narrowing identifier repertoires,
detecting mixed scripts, assigning restriction levels, and finding visually
confusable strings. It separates syntactic validity from security screening:
an XID character may still be uncommon, invisible, obsolete, technical, or
visually deceptive.

## Findings

- The General Security Profile filters a language's syntactic repertoire by
  `Identifier_Status=Allowed`; restricted characters include unassigned,
  deprecated, default-ignorable, obsolete, uncommon, technical, and limited-
  use cases.
- Restriction levels account for `Script_Extensions`, shared Common and
  Inherited characters, and Japanese, Korean, and Bopomofo writing systems.
  “Highly Restrictive” admits a single script plus specific Latin/East Asian
  combinations while excluding arbitrary Latin/Greek/Cyrillic mixtures.
- Confusable data maps characters to visual prototypes. An internal skeleton
  canonically decomposes the input, removes default ignorables, substitutes
  prototypes, and decomposes again.
- Confusable detection is intentionally conservative and version-sensitive.
  Equal skeletons indicate a review risk, not proof of malicious intent or
  semantic equality.

## Relevance

Catena intersects Unicode 17 XID with the unmodified General Security Profile,
applies Highly Restrictive checking per identifier segment, and uses the pinned
confusable mapping for warnings over a caller-supplied name domain. The warning
can be promoted by project policy without making visual similarity part of
identifier equality.

## Limits

UTS #39 is a collection of mechanisms rather than a mandate to reject every
detected similarity. Full bidirectional display skeletons depend on display
direction and Unicode Bidirectional Algorithm processing. Catena 0.1.10 uses
the stable internal prototype skeleton for compiler warnings and leaves source
display ordering to later tooling work.

## Derived work

- [Catena Identifiers and Name Security](../20-notes/catena-identifiers-and-name-security.md)
- [Identifier and Name Security map](../10-maps/identifier-and-name-security.md)
- [Identifier security rules](../60-specification/identifiers/qualification-keywords-and-security.md)
