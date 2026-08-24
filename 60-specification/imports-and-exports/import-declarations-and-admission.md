---
title: "Import Declarations and Admission"
kind: specification
created: "2026-08-22"
status: normative
spec_version: "0.1.18"
tags:
  - imports
  - specification
aliases:
  - "Catena import admission"
---

# Import Declarations and Admission

## Status and authority

This chapter is the normative Catena 0.1.18 import admission contract.
It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It generalizes the digest-backed import of the
[C010 kernel](../formal-semantic-kernel/canonical-kernel-syntax.md) and
feeds the precedence model of
[C021](../namespaces-and-shadowing/shadowing-and-ambiguity.md).

The rules apply only to source-language revision `0.1.18`.

## Import declaration events

An import declaration event carries a module name, its interface digest,
and an explicit possibly-empty list of (category, spelling) pairs
(`IM-OBL-005`):

> **Normative definition.**

```text
import-event ::= module-name, digest, name-list ;
name-list    ::= { category, spelling } ;
```

The module name satisfies C020's uppercase-initial module spelling. The
digest is opaque identity under C006/C008; this chapter adds no
verification rule for it. Each listed pair satisfies its category's C021
spelling class.

## Admission

An import has exactly two effects (`IM-OBL-005`):

1. the module is admitted for two-segment qualification: every name in
   its exported set resolves as `Module.member` in the appropriate
   category, and no other name of that module resolves;
2. each listed name that the module exports is admitted unqualified into
   its category, joining C021's import origins under
   local-over-imported precedence and reference-time `NSP004`.

The empty list is qualified-only admission: no unqualified admission,
full qualification rights. Multiple imports of one module are cumulative
and order-independent; importing one name twice from one module is a C021
`NSP001` duplicate.

## Validation

Importing a listed name absent from the module's exported set in that
category is static invalidity reported as `IMP002`, naming the module,
category, and spelling (`IM-OBL-006`). Importing a module that is not
known to the resolution context is static invalidity reported as
`IMP003`, naming the module (`IM-OBL-006`). Qualification against a
module not admitted by any import is an `NSP003` unbound reference under
C021.

A known module is one whose export set and digest the resolution context
holds; how contexts acquire modules — package assembly, build inputs —
remains G025/G121.

## Declared exclusions

0.1.18 defines no wildcard, `hiding`-style exclusion, renaming, alias,
or re-export form (`IM-OBL-007`). Each is a declared absence:

- wildcards and exclusions would make unqualified admission implicit
  rather than listed, contradicting the kernel's explicitness;
- renaming and aliases add a second spelling for names or modules before
  any demonstrated need; collisions already resolve by qualification;
- re-exports belong to package assembly under G025, where a package's
  public surface over its dependencies is designed once.

A later revision admitting any of these requires its own lifecycle
record; this chapter reserves no spellings for them beyond P109's token
inventory.

## Precedence interaction

Imported names participate in C021 resolution exactly as the `import`
origin class: a local declaration wins over every import; two import
origins colliding on one unqualified spelling in one category reject at
reference time as `NSP004` with every origin named; a future prelude
origin follows the same precedence under G026 (`IM-OBL-008`). Admission
never changes resolution order, scope structure, or spelling classes.

## Deliberately separate work

Module recursion across imports remains G024. Module discovery,
package identity, and re-exports remain G025/G121. Prelude contents and
opt-out remain G026. Entry modules are subsequently fixed by C027. The concrete `use`
surface punctuation remains P109.

## Rationale and evidence (non-normative)

The [imports synthesis](../../20-notes/catena-imports-and-exports.md)
records the Haskell empty-list precedent for qualified-only admission,
the Erlang qualification-only contrast, and why the explicit list was
selected as the single admission mechanism.
