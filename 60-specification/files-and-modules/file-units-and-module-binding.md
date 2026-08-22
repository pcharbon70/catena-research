---
title: "File Units and Module Binding"
kind: specification
created: "2026-08-22"
status: normative
spec_version: "0.1.16"
tags:
  - files
  - modules
  - specification
aliases:
  - "Catena file units"
---

# File Units and Module Binding

## Status and authority

This chapter is the normative Catena 0.1.16 file-unit, extension, and
module-binding contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It consumes the byte-accurate source units of
[C013](../source-text/README.md) and the comment forms of
[C016](../comments-and-documentation-comments/README.md), and aligns with
the one-module semantic units of the retained JSON frontend and the exact
[C010 kernel](../formal-semantic-kernel/canonical-kernel-syntax.md).

The rules apply only to source-language revision `0.1.16`. They do not
reinterpret retained JSON ASTs, kernel S-expressions, interfaces,
artifacts, or signed formats.

## Source-file extension

A Catena source file carries exactly the `.cat` extension. The file-unit
resolver of [Diagnostics and Conformance](diagnostics-and-conformance.md)
requires the extension and reports `FIL001` otherwise (`FU-OBL-002`).
Discovery tooling simply does not treat other files as Catena source; this
chapter assigns no meaning to other extensions.

## File units

A file unit is one complete `.cat` file together with its filename. Every
file unit is exactly one of (`FU-OBL-003`):

- a **module file**: containing at most one module declaration; or
- a **no-module file**: containing no module declaration.

A no-module file whose content is empty, layout whitespace, or comments
only is valid, and builds MUST NOT treat it as declaring anything
(`FU-OBL-003`). A module declaration is emitted by a later declaration
grammar as an abstract event; its concrete syntax remains P109's and no
other rule of this chapter depends on that syntax.

## Module multiplicity

A file unit MUST NOT contain more than one module declaration. Two or more
module-declaration events are static invalidity reported as `FIL002`, and
no file-unit result is published (`FU-OBL-004`).

## File-level module-name spelling

A file-level module name is one ASCII uppercase-initial word matching
`[A-Z][A-Za-z0-9_]*` (`FU-OBL-005`). This spelling is identical to the
retained JSON frontend's `"module"` field and to the C010 kernel's
module-name class, so all three frontends accept the same module names.
C014 identifier spelling and its Unicode repertoire do not apply at file
level; keeping module names ASCII keeps basenames portable across
filesystems. A module-declaration event carrying any other spelling is
static invalidity reported as `FIL003`.

## Declared-name basename verification

The module name of a module file comes solely from its module declaration,
never from the filesystem. When a module is declared, the file's basename
minus the `.cat` extension MUST equal the declared module name
(`FU-OBL-006`).

A mismatch is static invalidity reported as `FIL004`, identifying both the
declared name and the expected basename-derived name in its details. It is
not a warning and admits no implementation variance.

A no-module file has no name to verify: it matches no module basename and
is never reported as mismatched (`FU-OBL-006`).

## Deliberately separate work

The concrete module-header syntax and declaration grammar remain P109.
Module-name resolution, namespaces, imports, and qualification remain
G021/G022. Package assembly, cross-file duplicate module names, directory
layout, and package identity remain G025. Entry-point selection remains
G027. Build caching, code loading, and hot replacement remain later
runtime and tooling work.

## Rationale and evidence (non-normative)

The [files synthesis](../../20-notes/catena-files-and-modules.md) compares
the Erlang declared-name-plus-basename precedent, the Rust filename-derived
contrast, and the Haskell header model with `Main` defaulting, and records
why declared-name verification was selected. The
[resolved inquiry](../../40-inquiries/how-should-catena-relate-files-to-modules.md)
and [topic map](../../10-maps/files-and-modules.md) preserve the decision
route.
