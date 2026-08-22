---
title: "Namespace Inventory and Spelling"
kind: specification
created: "2026-08-22"
status: normative
spec_version: "0.1.17"
tags:
  - namespaces
  - specification
aliases:
  - "Catena namespace inventory"
---

# Namespace Inventory and Spelling

## Status and authority

This chapter is the normative Catena 0.1.17 namespace inventory and
spelling-class contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It generalizes the name rules of the
[C010 kernel](../formal-semantic-kernel/canonical-kernel-syntax.md),
consumes the identifier spelling of
[C014](../identifiers/identifier-syntax-and-equivalence.md), and the
qualified-name tokens of
[C019](../operators-and-punctuation/token-inventory-and-maximal-munch.md),
and the flat module names of [C020](../files-and-modules/README.md).

The rules apply only to source-language revision `0.1.17`. They do not
reinterpret retained JSON ASTs, kernel S-expressions, interfaces,
artifacts, or signed formats.

## Namespace categories

Every name in a Catena program belongs to exactly one namespace category
(`NS-OBL-002`):

> **Normative definition.**

```text
value-class categories (lowercase-initial spellings only):
  values        module and lexical value bindings
  fields        record fields of one owning type declaration
  operations    effect operations of one owning effect declaration
  typevars      type variables bound by one quantifier

capitalized-class categories (uppercase-initial spellings only):
  types         nominal type names
  constructors  data constructors
  traits        trait names
  effects       effect names
  handlers      handler names
  entries       process-entry names
  modules       module names of the package

separate categories (never in program-name resolution):
  governed      claim, evidence, assumption, decision, actor, and
                trust-root identities under the C006 typed identity model
```

Categories are disjoint: a resolution request names its category, and a
spelling resolves in at most that one category in any scope. The same
spelling may bind names in different categories simultaneously without
collision (`NS-OBL-002`).

## Spelling-class partition

The partition is hard and symmetric (`NS-OBL-003`): a declaration event
whose category is value-class MUST carry a C014 identifier with a
lowercase-initial spelling, and a declaration event whose category is
capitalized-class MUST carry a C014 identifier with an uppercase-initial
spelling. A declaration event violating its class is static invalidity
reported as `NSP002`. Type variables use lowercase-initial spellings
under C014's identifier rules.

## Uniqueness domains

Within one category (`NS-OBL-004`):

- `values`, `types`, `constructors`, `traits`, `effects`, `handlers`,
  `entries`, and `modules` are unique per module for module-level
  declarations, extending the kernel's duplicate-rejection and
  flat-constructor rules; constructor names are unique across the whole
  module, not per owning type.
- `fields` are unique within one owning type declaration; `operations`
  are unique within one owning effect declaration; handler clauses are
  unique within one owning handler declaration; parameters are unique
  within one declaration, all per the kernel.
- `typevars` are unique within one quantifier.
- `modules` are unique across the package; cross-file duplicate module
  names follow the package-assembly owner (G025) and file-level binding
  (C020).

A same-scope duplicate declaration in one category is static invalidity
reported as `NSP001`, regardless of whether the duplicate arises from two
local declarations or one local declaration colliding with an import in
the same lexical scope under the precedence rules of
[Shadowing and Ambiguity](shadowing-and-ambiguity.md).

## Governed identity separation

Claim, evidence, assumption, decision, actor, and trust-root identities
occupy their own categories under the C006 typed identity model. They
MUST NOT resolve as program names in any program category, and program
names MUST NOT resolve as governed identities (`NS-OBL-005`). No spelling
identity or collision relationship exists between a governed identity and
a program name.

## Qualification depth

A qualified reference is exactly two C014 identifier segments joined by
the C019 qualification separator: `Module.member` (`NS-OBL-006`). The
first segment resolves in the `modules` category; the second resolves in
one program category of that module's exported names, where export
selection remains G022's. A three-or-more-segment chain is a reserved
spelling reported as `NSP005`, not a nested-module resolution, until a
later revision admits deeper qualification with its own evidence.

## Deliberately separate work

Import and export syntax, visibility defaults, renaming, and wildcard
exclusion remain G022. Module recursion and initialization order remain
G024. Package assembly and cross-file duplicate module rejection remain
G025. Prelude contents and opt-out remain G026. Whether any resolution may
depend on inferred types remains G066. The declaration surface grammar
that emits these events remains P109.

## Rationale and evidence (non-normative)

The [namespaces synthesis](../../20-notes/catena-namespaces-and-shadowing.md)
compares Haskell's six-name-kind model, SML's per-category environments,
and the Erlang flat-atom and OCaml open-shadowing contrasts. The
[resolved inquiry](../../40-inquiries/how-should-catena-organize-namespaces-and-shadowing.md)
and [topic map](../../10-maps/namespaces-and-shadowing.md) preserve the
decision route.
