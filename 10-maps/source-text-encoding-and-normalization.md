---
title: "Source Text Encoding and Normalization"
kind: map
created: "2026-08-17"
tags:
  - language-design
  - parsing
  - unicode
  - utf-8
aliases:
  - "C013 source-text map"
---

# Source Text Encoding and Normalization

## Scope

This map connects Catena 0.1.9's strict UTF-8 envelope, BOM and newline
decisions, normalization boundary, original-byte source locations, compiler
validation, and the lexical questions deliberately left open.

## Start here

- [Catena Source-Text Encoding and Normalization](../20-notes/catena-source-text-encoding-and-normalization.md)
  develops the design, relation to the corpus, alternatives, and falsification
  criteria.
- [How Should Catena Decode and Normalize Source Text?](../40-inquiries/how-should-catena-decode-and-normalize-source-text.md)
  records the bounded question and its C013 resolution.
- [Source Text Specification](../60-specification/source-text/README.md) is the
  normative 0.1.9 contract.
- [C013 verification record](../50-journal/2026-08-17-c013-source-text-encoding-and-normalization.md)
  records executable evidence and archive validation.

## Trails

### Encoding validity and security

[Unicode 17's conformance and encoding definitions](../30-sources/unicode-consortium-2025-unicode-standard-17.md)
define scalar values and well-formed UTF-8. [RFC 3629](../30-sources/yergeau-2003-utf-8.md)
connects invalid decoding to security and explains why an already-UTF-8
protocol gains no byte-order information from a BOM. These sources support the
strict rejection rules in the
[Source-Text Envelope](../60-specification/source-text/source-text-envelope.md#utf-8-byte-domain).

### Preservation and normalization

[UAX #15](../30-sources/whistler-2025-unicode-normalization-forms.md) shows that
normalization can reorder or replace scalar sequences and that compatibility
forms erase distinctions. C013 therefore preserves the whole source stream.
C014 now requires NFC source spelling for each identifier segment without
changing future comment and literal contents. The separate
[Identifier and Name Security map](identifier-and-name-security.md) explains
that filtered normalization and its exact replacement diagnostic.

### Newlines and coordinates

The [logical-newline rule](../60-specification/source-text/source-text-envelope.md#logical-newlines)
maps LF and CRLF to one logical LF and rejects lone CR. The
[location rule](../60-specification/source-text/source-text-envelope.md#source-units-and-locations)
retains original zero-based byte ranges and one-based scalar columns. This
gives later lexers stable spans without making grapheme or display width part
of the language.

### Conformance and version separation

[Diagnostics and Conformance](../60-specification/source-text/diagnostics-and-conformance.md)
defines `SRC001`–`SRC003`, the public decoder result, CLI validation, and ten
`ST-OBL-*` obligations. The [Conformance Traceability map](conformance-traceability.md)
connects them to focused sibling-compiler tests and guards against 0.1.9
leaking into JSON, kernel, interface, or compiled-artifact formats.

### Existing exact inputs

The [formal semantic kernel map](formal-semantic-kernel.md) remains the route
for the ASCII-bounded exact 0.1.8 S-expression. C013 does not reinterpret that
input. The [edition and lifecycle map](language-editions-and-feature-lifecycle.md)
supplies the exact revision and compatible-addition record used to expose the
new source-text feature.

## Open questions

C013 through C017 are resolved. Follow the
[Whitespace, Layout, and Line Continuation map](whitespace-layout-and-line-continuation.md)
for C015's classification and the
[Comments and Documentation Comments map](comments-and-documentation-comments.md)
for C016's preserving use of the logical stream and the
[Literal Grammar map](literal-grammar.md) for C017's preserving decoding and
raw line ownership. G020 owns file-to-module relations and P109 owns the
declaration grammar over the C019 token stream. P117 owns the complete
cross-language diagnostic model; G118 owns canonical formatting and comment-
preserving trees. Aggregate source-size and hostile-input performance remain
outside the current portable-floor set.
