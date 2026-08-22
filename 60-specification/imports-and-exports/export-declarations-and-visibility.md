---
title: "Export Declarations and Visibility"
kind: specification
created: "2026-08-22"
status: normative
spec_version: "0.1.18"
tags:
  - exports
  - specification
  - visibility
aliases:
  - "Catena export declarations"
---

# Export Declarations and Visibility

## Status and authority

This chapter is the normative Catena 0.1.18 export and visibility
contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It generalizes the export forms of the
[C010 kernel](../formal-semantic-kernel/canonical-kernel-syntax.md), rides
on the transparency contract of
[C002](../data-and-patterns/interfaces-and-representation.md), and feeds
the interface identity of
[C008](../editions-and-feature-lifecycle/README.md).

The rules apply only to source-language revision `0.1.18`. They do not
reinterpret retained JSON ASTs, kernel S-expressions, interfaces,
artifacts, or signed formats.

## Private by default

Nothing is exported without an explicit export declaration
(`IM-OBL-002`). Every module-level declaration not named by an export
declaration of this module is private: it resolves inside the module
under C021 rules and MUST NOT resolve, qualified or unqualified, in any
other module. An implementation MUST NOT expose private names through an
interface, diagnostic suggestion, or any other observable surface.

## Export declaration events

An export declaration event carries a category, a spelling, and — for the
`types` category — a transparency mode (`IM-OBL-003`):

> **Normative definition.**

```text
export-event ::= category, spelling [, transparency] ;
category     ::= "values" | "types" | "constructors" | "traits"
               | "effects" | "handlers" | "entries" | "fields"
               | "operations" ;
transparency ::= "transparent" | "abstract" ;
```

The spelling must satisfy its category's C021 spelling class. The
transparency mode names C002's contract — `transparent` exports the type
together with its constructor surface, `abstract` exports the type
without it — and this chapter adds no condition beyond naming it; the
abstraction guarantees are C002's. Non-`types` categories carry no
transparency mode.

## Validation

An export declaration naming a name the module does not declare in that
category is static invalidity reported as `EXP001`, identifying the
category and spelling (`IM-OBL-004`). Two export declarations of one
spelling in one category are C021 `NSP001` duplicates; export events do
not create a separate duplicate diagnostic.

Constructor export follows C002: a constructor is reachable from other
modules when its parent type is exported `transparent` and the
constructor is part of the exported surface; the `constructors` export
event names an individual constructor's admissibility within that
surface. An abstract type's constructors MUST NOT be exported
(`IM-OBL-003`).

## Interface reflection

The exported set — categories, spellings, transparency modes — is what a
module's interface records, and its digest is the module's C008 interface
identity. This layer consumes digests opaquely: it adds no verification
rule, and every digest obligation remains C006/C008 property. An import
in another module validates against exactly this exported set under
[Import Declarations and Admission](import-declarations-and-admission.md).

## Deliberately separate work

Module recursion and initialization order remain G024. Package-level
re-export assembly and cross-module duplicate rejection remain G025.
Prelude contents remain G026. Entry-module selection remains G027. The
concrete `export` surface punctuation remains P109. Interface format and
digest computation remain C006/C008.

## Rationale and evidence (non-normative)

The [imports synthesis](../../20-notes/catena-imports-and-exports.md)
compares Haskell's public-by-default exports, SML's signature surfaces,
and the kernel's explicit forms. The
[resolved inquiry](../../40-inquiries/how-should-catena-handle-imports-and-exports.md)
and [topic map](../../10-maps/imports-and-exports.md) preserve the
decision route.
