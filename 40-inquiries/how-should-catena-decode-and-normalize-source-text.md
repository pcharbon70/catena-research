---
title: "How Should Catena Decode and Normalize Source Text?"
kind: inquiry
created: "2026-08-17"
status: resolved
tags:
  - language-design
  - parsing
  - unicode
  - utf-8
aliases:
  - "Catena C013 inquiry"
---

# How Should Catena Decode and Normalize Source Text?

## Why this matters

Every later source-language decision depends on a shared answer to a more
basic question: which bytes form text, which serialized line endings define
one logical newline, whether Unicode spellings are changed, and how a
diagnostic points back into the original file. Leaving this to a host string
library would make compiler behavior rather than normative text define the
language.

## Operational question

Choose a source envelope for which independent implementations can agree on
acceptance, the decoded logical scalar sequence, original-byte locations, and
stable failure categories for every finite byte sequence. The answer must not
prematurely settle identifiers, literals, comments, layout, or module grammar.

## Working hypotheses

- UTF-8 alone provides the smallest portable Unicode boundary.
- A BOM should be rejected because the encoding is already fixed.
- LF and CRLF should share one logical representation while retaining original
  byte spans.
- Whole-file Unicode normalization is too broad; identifier-specific policy
  should remain with G014.
- Byte offsets plus scalar line/columns provide a deterministic language
  coordinate while leaving display placement to tools.

## Paths explored

The [Unicode 17 encoding rules](../30-sources/unicode-consortium-2025-unicode-standard-17.md)
were used for strict UTF-8 and scalar validity. [RFC 3629](../30-sources/yergeau-2003-utf-8.md)
was used for invalid-sequence and BOM protocol analysis. [UAX #15](../30-sources/whistler-2025-unicode-normalization-forms.md)
was used to evaluate the semantic and location consequences of normalization.

The current [0.1.8 kernel envelope](../60-specification/formal-semantic-kernel/canonical-kernel-syntax.md#input-envelope)
was treated as a separate exact conformance syntax, not a template for
ergonomic source. The [C012 limit policy](../IMPLEMENTATION-LIMITS.md) was
checked to ensure C013 did not invent an aggregate source-size refusal.

## Findings

Replacement decoding is unsuitable because it can turn multiple malformed
byte sequences into one accepted token stream. Whole-file normalization is
unsuitable because it can reorder or replace scalar sequences in future
literals and comments and breaks simple original-byte mapping. Broad Unicode
newline recognition would create invisible structure before layout and
literal rules exist.

The bounded strict profile is sufficient to close G013 independently. A
source file can satisfy the envelope without satisfying any later token or
module grammar, so C013 does not need to invent placeholder syntax.

The complete comparison and rejected alternatives are developed in
[Catena Source-Text Encoding and Normalization](../20-notes/catena-source-text-encoding-and-normalization.md).

## Outcome

Resolved as C013 and language revision `0.1.9`. Catena uses strict UTF-8,
rejects a leading BOM and alternate encoding signatures, accepts LF and CRLF
as one logical LF, rejects lone CR, preserves every other scalar without
Unicode normalization, and records zero-based original-byte offsets with
one-based scalar lines and columns.

The [normative source-text area](../60-specification/source-text/README.md)
defines `SRC001`–`SRC003` and `ST-OBL-001` through `ST-OBL-010`. The sibling
compiler supplies a reusable decoder, source units, exact revision separation,
the `check-source-text` command, and focused adversarial coverage. G019–G020
remain responsible for the actual lexical and file grammar now that
C014–C018 have fixed identifiers, layout, comments, literals, and numeric
literal meaning; P117 and G118
retain cross-language diagnostics and formatter behavior.
