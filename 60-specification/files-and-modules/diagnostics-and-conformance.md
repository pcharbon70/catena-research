---
title: "File Diagnostics and Conformance"
kind: specification
created: "2026-08-22"
status: candidate
spec_version: "0.1.16"
tags:
  - conformance
  - diagnostics
  - files
  - specification
  - testing
aliases:
  - "Catena 0.1.16 file conformance"
---

# File Diagnostics and Conformance

## Status and authority

This chapter is the normative Catena 0.1.16 file diagnostic, abstract
frontend, and conformance contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies [File Units and Module Binding](file-units-and-module-binding.md)
and [Generated File Markers](generated-file-markers.md).

## Stable diagnostics

| ID | Required meaning |
| --- | --- |
| `FIL001` | the supplied filename does not carry the `.cat` extension |
| `FIL002` | more than one module declaration appears in one file unit |
| `FIL003` | a module-declaration name violates the ASCII uppercase-initial spelling |
| `FIL004` | the declared module name does not equal the file basename minus extension |
| `FIL005` | a first-unit marker comment fails the exact marker grammar |

An exact-selection mismatch remains `EDN001`. Every file-unit rejection
carries the stable diagnostic ID and, where the failure is content-derived,
a primary original-byte span; basename mismatches carry both the declared
and expected names in their details (`FU-OBL-010`).

Invalid input produces no file-unit result or other successful output for
the affected action. Diagnostic prose can improve only within the bounded
presentation rules of the repository conformance vocabulary; identity,
severity, reason, acceptance, and repair meaning do not vary.

## Abstract public boundary

A conforming implementation exposes a file-unit resolver. It accepts
source bytes, a filename, an ordered list of module-declaration events —
each carrying a declared name and an original-byte span, supplied by a
later declaration grammar — and an exact language selection. It returns
one complete file unit — the kind `module` or `no_module`, the declared
module name when present with its span, the generated flag, and the tool
identifier when generated — or exactly one diagnostic (`FU-OBL-011`).

The resolver does not parse declarations, tokenize source, resolve names,
load code, or compile; the concrete module-header syntax that produces the
events remains P109's, and implementations MUST NOT use this boundary to
claim those later phases (`FU-OBL-012`).

The bootstrap evidence names this operation `Catena.resolve_file_unit/3`
and its records `Catena.FileUnit.Result` and
`Catena.FileUnit.ModuleDeclaration`. These Elixir names are evidence API
names, not required names for every implementation.

## Determinism

Equal source bytes, filename, declaration events, and exact language
selection produce equal file-unit results or equal stable diagnostics
(`FU-OBL-011`). Marker recognition, name spelling, and basename comparison
are byte-exact and case-sensitive.

## Conformance obligations

| ID | Obligation | Required executable evidence |
| --- | --- | --- |
| `FU-OBL-001` | apply file-unit behavior only at exact 0.1.16 and register the stable lifecycle addition | exact selection, registry, and lifecycle tests |
| `FU-OBL-002` | require the `.cat` extension and report `FIL001` otherwise | extension matrix tests |
| `FU-OBL-003` | classify module and no-module files with valid empty and comment-only units | empty, whitespace, and comment-only tests |
| `FU-OBL-004` | reject more than one module declaration as `FIL002` | multiplicity tests |
| `FU-OBL-005` | enforce the ASCII uppercase-initial module-name spelling with `FIL003` | spelling matrix tests |
| `FU-OBL-006` | verify the declared name against the basename with `FIL004`, matching no name for no-module files | match, mismatch, and no-module tests |
| `FU-OBL-007` | recognize the exact marker grammar with its tool identifier | exact spelling tests |
| `FU-OBL-008` | enforce first-unit placement and single recognition | placement and inert-position tests |
| `FU-OBL-009` | reject malformed first-unit markers as `FIL005` and keep the text inert elsewhere | malformed, documentation-comment, literal, and later-comment tests |
| `FU-OBL-010` | emit stable file diagnostics with spans and both names on mismatch | every diagnostic family test |
| `FU-OBL-011` | expose the lossless resolver boundary deterministically | repeated-result and event-shape tests |
| `FU-OBL-012` | preserve source-only and persisted-format separation and claim no later phase | registry, pinned-predecessor, forged-format, and absent-phase tests |

Every obligation has at least one tagged passing test. The sibling compiler
gates the complete `FU-OBL-*` set against unknown and uncovered identifiers
before C020 conformance is claimed.

## Required evidence sets

Positive evidence includes empty files, whitespace-only files, comment-only
files; one-declaration module files with matching basenames; marker files
with varied tool identifiers; markers before comments and after whitespace;
no-module files carrying markers; and mixed CRLF/LF first lines.

Negative evidence includes other extensions; two and three declarations;
lowercase, digit-initial, Unicode, and hyphenated declaration names;
basename mismatches including case mismatches; malformed markers with wrong
spacing, empty identifiers, trailing content, and documentation-comment
forms; and exact-selection mismatches.

Exclusion evidence demonstrates that the resolver does not tokenize source,
parse declarations, resolve names, or emit interfaces or BEAM, and that
predecessor APIs retain their exact 0.1.10 through 0.1.15 selections and
defaults.

## Revision and persistence separation

Revision `0.1.16` is a compatible source-acceptance and static-structure
addition. It adds no JSON AST version, kernel S-expression version,
interface version, artifact version, signature domain, typing rule, runtime
behavior, or BEAM representation (`FU-OBL-001`, `FU-OBL-012`).

The source-text decoder accepts cumulative revisions `0.1.9` through
`0.1.16`. Standalone identifier, layout, comment, literal scanning, numeric
elaboration, tokenization, and operator-expression APIs retain their exact
0.1.10 through 0.1.15 selections and defaults. File-unit resolution
requires exact `0.1.16`. The next unused semantic patch is `0.1.17`.

## Rationale and evidence (non-normative)

The design route is preserved in the
[files synthesis](../../20-notes/catena-files-and-modules.md), the
[open inquiry](../../40-inquiries/how-should-catena-relate-files-to-modules.md),
and the [topic map](../../10-maps/files-and-modules.md). The C020 evidence
record will preserve the sibling-compiler commands and archive validation.
