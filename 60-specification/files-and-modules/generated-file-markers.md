---
title: "Generated File Markers"
kind: specification
created: "2026-08-22"
status: normative
spec_version: "0.1.16"
tags:
  - files
  - specification
  - tooling
aliases:
  - "Catena generated markers"
---

# Generated File Markers

## Status and authority

This chapter is the normative Catena 0.1.16 generated-file recognition
contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It consumes the comment forms of
[C016](../comments-and-documentation-comments/comment-lexing-and-layout.md)
and the logical-unit stream of
[C013](../source-text/source-text-envelope.md).

The rules apply only to source-language revision `0.1.16`.

## Marker spelling

A generated-file marker is one plain line comment with the exact form
(`FU-OBL-007`):

> **Normative definition.**

```text
generated-marker = "//", " ", "catena:generated", " ", "by", " ", tool-identifier ;
tool-identifier  = ascii-letter-or-digit-or-underscore-or-hyphen, { ascii-letter-or-digit-or-underscore-or-hyphen } ;
```

The tool identifier is nonempty and built from ASCII letters, digits,
underscore, and hyphen. The marker comment body is exactly the matched text
with one ASCII space between each component; no trailing content is
permitted inside the marker comment. The marker rides on a C016 plain
comment form only: a documentation comment (`///`) never carries a marker.

## First-unit placement

A file is generated when its first significant logical unit is a marker
comment. Only layout whitespace may precede it (`FU-OBL-008`). A marker
appearing after any other significant unit — a name, literal, operator,
punctuation, another comment, or any token — does not mark the file.

## Single marker

At most one marker exists per file. A second first-position-shaped marker
cannot exist by the placement rule; a file whose content would otherwise
match the marker grammar more than once is recognized by its first unit
alone, and no distinct duplicate-marker condition arises
(`FU-OBL-008`).

## Inert elsewhere

The text `catena:generated ...` inside a documentation comment, inside a
later plain comment after another significant unit, inside a literal, or
split across comments is ordinary comment or literal content with no
marker meaning (`FU-OBL-009`). Recognition depends only on the exact
first-unit spelling.

## Failure and provenance

A first-unit comment that begins the marker text but fails the grammar —
wrong spacing, empty or invalid tool identifier, or trailing content — is
static invalidity reported as `FIL005` (`FU-OBL-009`). A recognized marker
yields the tool identifier as file provenance; consumption by builds,
formatters, editors, and reproducibility policy remains G121/G128, and
editing or regeneration policy remains G118/G123. A no-module file may
still be generated and carry a marker.

## Deliberately separate work

How tools generate, regenerate, or verify generated files remains tooling
and build work (G118/G121/G123/G128). Whether specific declarations admit
generated implementations, and any generation of `.cati.json` interfaces or
BEAM artifacts, remain their own slices.

## Rationale and evidence (non-normative)

The [files synthesis](../../20-notes/catena-files-and-modules.md) compares
Erlang's `-file` provenance attribute, filename-convention approaches, and
sidecar manifests, and records why an exact first-line marker was selected.
