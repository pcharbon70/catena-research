---
title: "Identifier Syntax and Equivalence"
kind: specification
created: "2026-08-17"
status: normative
spec_version: "0.1.10"
tags:
  - identifiers
  - language-design
  - specification
  - unicode
aliases:
  - "Catena identifier syntax"
---

# Identifier Syntax and Equivalence

## Status and authority

This chapter is the normative Catena 0.1.10 identifier-shape, normalization,
case, and identity contract. It extends the normative
[Source-Text Envelope](../source-text/source-text-envelope.md) and is governed
by [Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).

The rules apply only when the selected exact language revision is `0.1.10`.
They do not reinterpret retained JSON AST names or the exact 0.1.8 kernel.
Passing these rules establishes one standalone lexical name, not a valid token
stream, declaration, binding, module, or program.

## Unicode data and profile

Version 0.1.10 uses the character properties and normalization data of Unicode
17.0.0 and UAX #31 Revision 43. A conforming implementation MUST use those
pinned values when deciding identifier acceptance (`ID-OBL-001`). Host runtime
or library upgrades MUST NOT change the accepted set for this revision
(`ID-OBL-001`).

An unescaped identifier segment has the following production.

> **Normative definition.**

```text
identifier-segment ::= XID_Start XID_Continue*
```

`XID_Start` and `XID_Continue` denote the Unicode 17 properties. Catena adds no
character to either class. In particular, `_` and decimal digits may continue
a segment where the property permits them but MUST NOT begin one
(`ID-OBL-002`). Empty segments are invalid.

## NFC spelling

Every identifier segment MUST already be in Unicode Normalization Form C
under Unicode 17 (`ID-OBL-004`). Validation implements UAX31-R6 Filtered
Normalized Identifiers. An implementation MUST NOT silently rewrite a segment
and continue (`ID-OBL-004`). It reports `IDN002` and supplies the exact NFC
replacement over the segment's original-byte span.

The NFC requirement is confined to identifier content. It does not normalize
the complete source stream, string or character literals, comments, or other
future lexical elements. The source-text decoder continues to preserve their
scalars exactly.

## Case and canonical identity

Identifier identity is case-sensitive. Two valid unescaped segments are equal
exactly when their Unicode scalar sequences are equal. NFC validity ensures
canonically equivalent alternatives cannot both be admitted as distinct
spellings. No case folding, locale mapping, compatibility normalization, or
default-ignorable removal participates in equality (`ID-OBL-003`).

Capitalization MUST NOT determine whether an identifier denotes a value, type,
variant, trait, effect, handler, module, or any other semantic role
(`ID-OBL-003`). The grammar context and later namespace rules determine role.
Names in uncased scripts remain eligible for every role those later rules
permit.

## Source spans and selection

Validation consumes the logical scalar units and original-byte spans defined
by the [Source-Text Envelope](../source-text/source-text-envelope.md#source-units-and-locations).
The span of a segment begins at its first delimiter or content scalar and ends
after its last delimiter or content scalar. A normalization fix covers only
the underlying identifier content.

The source-text frontend accepts both `0.1.9` and cumulative `0.1.10`, but the
identifier and qualified-name frontends MUST reject a selected revision other
than `0.1.10` as `EDN001` (`ID-OBL-013`). Revision `0.1.10` MUST NOT be admitted
by JSON, kernel, interface, artifact, or signed-format registries
(`ID-OBL-013`).

## Invalidity and limits

An empty segment, invalid start, invalid continuation, non-NFC spelling, or
wrong frontend revision is invalid input. Validation stops without producing a
successful identifier. No rule in this chapter introduces an implementation
limit or permits acceptance to depend on available Unicode support.

## Rationale and evidence (non-normative)

[UAX #31](../../30-sources/davis-leroy-2025-unicode-identifiers-syntax.md)
supplies the default profile and filtered-normalization requirements.
[UTS #55](../../30-sources/leroy-davis-2024-unicode-source-code-handling.md)
supports NFC for case-sensitive languages and avoiding case-only semantics.
The deliberate R6 tradeoff and alternatives are developed in
[Catena Identifiers and Name Security](../../20-notes/catena-identifiers-and-name-security.md).
