---
title: "Qualification, Keywords, and Identifier Security"
kind: specification
created: "2026-08-17"
status: normative
spec_version: "0.1.10"
tags:
  - identifiers
  - security
  - specification
  - unicode
aliases:
  - "Catena qualified names and confusables"
---

# Qualification, Keywords, and Identifier Security

## Status and authority

This chapter is the normative Catena 0.1.10 qualification, keyword, escape,
security-profile, and confusable-warning contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
Segment shape and identity come from
[Identifier Syntax and Equivalence](identifier-syntax-and-equivalence.md).

## Qualified names

A standalone qualified name has the following form.

> **Normative definition.**

```text
name-segment   ::= identifier-segment | "`" identifier-segment "`"
qualified-name ::= name-segment ("." name-segment)*
```

The dot is ASCII U+002E. No whitespace or other scalar occurs between a
segment and a dot. A qualified name MUST contain at least one nonempty segment
and MUST NOT begin or end with a dot or contain adjacent dots
(`ID-OBL-009`). Every segment is validated independently before the sequence is
accepted.

The canonical identity is the ordered sequence of canonical segment
identities. This chapter does not assign module meaning to a prefix or define
lookup, namespace membership, shadowing, imports, exports, or ambiguity.

## Reserved words and escaping

The complete case-sensitive 0.1.10 reserved-word set is: `as`, `condition`,
`derives`, `effect`, `exists`, `false`, `fn`, `forall`, `handle`, `handler`,
`import`, `let`, `match`, `or`, `request`, `resume`, `returns`, `true`, `type`,
`uses`, `when`, `where`, and `with` (`ID-OBL-007`).

An unescaped segment equal to a reserved word is invalid as an identifier and
reports `IDN005`. Surrounding an otherwise-valid segment with one ASCII
backtick on each side makes it an escaped identifier (`ID-OBL-008`). The
backticks are not part of canonical identity. Thus `` `type` `` has canonical
identity `type`.

Escaping MUST NOT bypass XID, NFC, security-profile, or script validation
(`ID-OBL-008`). An empty, nested, unclosed, misplaced, or trailing-content
escape is invalid. Escaping a valid nonkeyword is accepted and yields the same
canonical identity as its unescaped spelling.

## General Security Profile

After XID and NFC validation, every segment scalar MUST have
`Identifier_Status=Allowed` in UTS #39 Revision 32 for Unicode 17
(`ID-OBL-005`). Catena uses the unmodified General Security Profile and adds no
exception character. A restricted scalar reports `IDN003` and makes the name
invalid.

## Highly Restrictive scripts

Every segment MUST satisfy the UTS #39 Highly Restrictive level using Unicode
17 `Script` and `Script_Extensions` data (`ID-OBL-006`). The calculation treats
Common and Inherited scalars as compatible with all scripts and uses the UTS
#39 augmented Japanese, Korean, and Bopomofo writing-system sets.

ASCII-only and single-script segments pass. The specified Latin-plus-Japanese,
Latin-plus-Korean, and Latin-plus-Bopomofo covers pass. A segment requiring any
other cross-script cover reports `IDN004` and is invalid. The check applies per
segment, not to the union of scripts across an entire qualified name.

## Confusable comparison

For each valid segment, an implementation computes the Unicode 17 UTS #39
internal confusable skeleton by canonical decomposition, removal of
`Default_Ignorable_Code_Point` scalars, prototype substitution from
`confusables.txt`, and canonical decomposition of the result. The skeleton of
a qualified name is the ordered segment skeletons joined with ASCII dot.

An identifier audit receives one explicit ordered comparison domain. When a
name has the same skeleton as an earlier name in that domain but a different
canonical identity, the implementation MUST emit `IDN007` on the later name
(`ID-OBL-010`). Exact duplicate canonical names do not produce this warning.
Diagnostics remain in input order and identify the first earlier distinct
collision.

`IDN007` is a warning by default. If the explicit denied-diagnostic set
contains `IDN007`, the implementation MUST promote it to an error and mark the
promotion in structured details (`ID-OBL-010`). Skeleton equality MUST NOT make
the names semantically equal, rename either name, or change repertoire
acceptance.

## Variability and limits

All Unicode property, script, and confusable data are pinned. The General
Security Profile has no implementation exception. Diagnostic promotion is an
explicit program or project selection; a conforming implementation does not
choose it. This chapter adds no implementation limit.

## Rationale and evidence (non-normative)

[UTS #39](../../30-sources/davis-suignard-2025-unicode-security-mechanisms.md)
supplies the profile, restriction level, and prototype data.
[UTS #55](../../30-sources/leroy-davis-2024-unicode-source-code-handling.md)
supports layered compiler warnings rather than treating all visual similarity
as name equality. Qualification follows established `Option.Some`,
`Rules.positive`, and `console.ask` examples while deferring their lookup
meaning.
