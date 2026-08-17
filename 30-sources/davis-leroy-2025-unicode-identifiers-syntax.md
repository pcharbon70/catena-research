---
title: "Unicode Standard Annex #31: Unicode Identifiers and Syntax"
kind: source
created: "2026-08-17"
authors:
  - "Mark Davis"
  - "Robin Leroy"
published: 2025
citation_key: "davis-leroy-2025-unicode-identifiers-syntax"
container: "Unicode Standard Annex #31"
edition: "Revision 43, Unicode 17.0.0"
isbn: null
doi: null
url: "https://www.unicode.org/reports/tr31/tr31-43.html"
accessed: "2026-08-17"
tags:
  - identifiers
  - language-design
  - unicode
aliases:
  - "UAX #31 Revision 43"
---

# Unicode Standard Annex #31: Unicode Identifiers and Syntax

## Reference

Mark Davis and Robin Leroy, “Unicode Identifiers and Syntax,” Unicode Standard
Annex #31, Revision 43, Unicode 17.0.0, 20 August 2025.
[Official publication](https://www.unicode.org/reports/tr31/tr31-43.html).

## Contribution

UAX #31 defines stable property-based identifier classes, conformance profiles,
normalization choices, and pattern-syntax boundaries for Unicode-aware parsers.
Its default identifier production starts with `XID_Start` and continues with
`XID_Continue`; those classes are closed under the normalization-related
adjustments that make them preferable to the older `ID_*` properties.

## Findings

- Requirement R1 permits a language to use the default XID production directly
  or publish an exact profile of additions, removals, and constraints.
- XID start and continuation classes grow compatibly as Unicode assigns new
  characters, but a language must identify the Unicode/UAX version on which a
  conformance claim depends.
- Canonically equivalent combining-mark sequences require an explicit
  normalization policy. R4 treats equal normalized forms as equivalent; R6
  instead admits only source spellings already in the selected form.
- NFC is the natural normalization form for a case-sensitive language because
  it preserves compatibility distinctions while removing canonical spelling
  alternatives.
- Default-ignorable characters and other visually deceptive cases require a
  narrower profile or higher-level security diagnostics; XID membership alone
  is not a spoofing defense.

## Relevance

Catena 0.1.10 profiles UAX31-R1 with Unicode 17 `XID_Start` and
`XID_Continue`, adds no initial punctuation, and adopts filtered NFC under R6.
The annex also supports keeping role and namespace semantics independent of
letter case.

The resulting model is developed in
[Catena Identifiers and Name Security](../20-notes/catena-identifiers-and-name-security.md)
and made normative in the
[Identifier Specification](../60-specification/identifiers/README.md).

## Limits

UAX #31 supplies general identifier mechanisms, not one complete programming-
language security policy. It does not choose Catena's keywords, qualification
syntax, namespaces, diagnostic severity, or comparison domains. Those require
language-specific rules and UTS #39/UTS #55 guidance.

## Derived work

- [Identifier and Name Security map](../10-maps/identifier-and-name-security.md)
- [Resolved identifier inquiry](../40-inquiries/how-should-catena-define-and-secure-identifiers.md)
- [C014 evidence record](../50-journal/2026-08-17-c014-identifiers-and-name-security.md)
